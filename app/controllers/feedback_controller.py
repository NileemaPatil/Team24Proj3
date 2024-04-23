from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..services.user_service import get_user_role, get_user_userStatus
from ..services.feedback_service import create_feedback, get_feedback
from ..schemas.feedback_schema import feedback_schema

feedback_blueprint = Blueprint('feedback_blueprint', __name__)


@feedback_blueprint.route('/add_feedback', methods=['POST'])
@jwt_required()
def add_feedback():
    current_user = get_jwt_identity()
    data = request.json
    feedback = create_feedback(data, current_user)
    return feedback_schema.jsonify(feedback), 201


@feedback_blueprint.route('/get_feedback_list', methods=['GET'])
@jwt_required()
def get_feedback_list():
    current_user = get_jwt_identity()
    user_role = get_user_role(current_user)
    feedbacklist = get_feedback()
    current_user = get_jwt_identity()
    feedback_data = []
    for feedback in feedbacklist:
        feedback_data = {
            "feedbackid": feedback.feedbackid,
            "feedbackuserid":feedback.feedbackuserid,
            "feedbackdesc":feedback.feedbackdesc,
            "orderid":feedback.orderid,
            "menuitemid":feedback.menuitemid,
            "feedbackdate":feedback.feedbackdate,
            "feedbackstatus":feedback.feedbackstatus,
            "feedbackaction":feedback.feedbackaction,
            "feedbackclosureremarks":feedback.feedbackclosureremarks,
            "feedbackactionuserid":feedback.feedbackactionuserid,
            "feedbackusername":feedback.feedbackusername

        }
        feedback_data.append(feedback_data)
    # Use jsonify to convert the list of dictionaries to a JSON response
    return jsonify(feedback_data)
