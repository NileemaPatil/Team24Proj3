from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from ..schemas.sentence_schema import sentences_schema
from ..services.project_service import create_project, get_projects_by_language, get_projects, \
    get_projects_with_annotation_counts_with_language, get_projects_with_annotation_counts
from ..schemas.project_schema import project_schema, projects_schema
from ..services.sentence_service import get_sentences
from ..services.user_service import get_user_userStatus, get_user_role

sentence_blueprint = Blueprint('sentence_blueprint', __name__)


@sentence_blueprint.route('/get_sentences', methods=['POST'])
@jwt_required()
def get_sentence():
    current_user = get_jwt_identity()
    data = request.json
    sentences = get_sentences(data)
    return sentences_schema.jsonify(sentences), 200

