from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..services.user_service import get_user_role, get_user_userStatus
from ..services.notification_service import create_notification, get_notification
from ..schemas.notification_schema import notification_schema

notification_blueprint = Blueprint('notification_blueprint', __name__)


@notification_blueprint.route('/add_notification', methods=['POST'])
@jwt_required()
def add_notification():
    current_user = get_jwt_identity()
    data = request.json
    notification = create_notification(data, current_user)
    return notification_schema.jsonify(notification), 201


@notification_blueprint.route('/get_notification_list', methods=['GET'])
@jwt_required()
def get_notification_list():
    current_user = get_jwt_identity()
    user_role = get_user_role(current_user)
    notificationlist = get_notification()
    current_user = get_jwt_identity()
    notification_data = []
    for notification in notificationlist:
        notification_data = {
            "notificationid": notification.notificationid,
            "userid":notification.userid,
            "notificationdesc":notification.notificationdesc,
            "notificationcreateddate":notification.notificationcreateddate,
            "notificationtype":notification.notificationtype,
            "notificationstatus":notification.notificationstatus,
            "createddate":notification.createddate,
            "updateddate":notification.updateddate,


        }
        notification_data.append(notification_data)
    # Use jsonify to convert the list of dictionaries to a JSON response
    return jsonify(notification_data)
