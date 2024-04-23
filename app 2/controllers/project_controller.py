from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..services.project_service import create_project, get_projects_by_language, get_projects, \
    get_projects_with_annotation_counts_with_language, get_projects_with_annotation_counts
from ..schemas.project_schema import project_schema, projects_schema
from ..services.user_service import get_user_language, get_user_role

project_blueprint = Blueprint('project_blueprint', __name__)


@project_blueprint.route('/add_project', methods=['POST'])
@jwt_required()
def add_project():
    current_user = get_jwt_identity()
    data = request.json
    project = create_project(data, current_user)
    return project_schema.jsonify(project), 201


@project_blueprint.route('/get_project_list', methods=['GET'])
@jwt_required()
def get_project_list():
    current_user = get_jwt_identity()
    user_role = get_user_role(current_user)
    user_language = get_user_language(current_user)
    if user_role == 'Admin':
        projects_with_counts = get_projects_with_annotation_counts()
    else:
        projects_with_counts = get_projects_with_annotation_counts_with_language(user_language)

    projects_data = []

    for project, annotated_count, unannotated_count in projects_with_counts:
        project_data = {
            "id": project.id,
            "title": project.title,
            "description": project.description,
            "language": project.language,
            "annotated": annotated_count,
            "unannotated": unannotated_count
        }
        projects_data.append(project_data)

    # Use jsonify to convert the list of dictionaries to a JSON response
    return jsonify(projects_data)
