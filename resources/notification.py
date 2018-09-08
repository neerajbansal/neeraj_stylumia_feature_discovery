from models.notification import NotificationModel
from models.user import UserModel
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required, current_identity


class AddNotification(Resource):

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('user_id',
                            type=int,
                            required=True,
                            help='User ID is required!')

        parser.add_argument('msg',
                            type=str,
                            required=True,
                            help='Message is required!')

        data_payload = parser.parse_args()

        print(data_payload)
        if UserModel.find_by_id(data_payload['user_id']):
            user_id = data_payload.get('user_id', None)
            msg = data_payload.get('msg', None)
            NotificationModel.insert_new_user_notification(
                user_id, 1, msg, True, '', 'version1')
            return {'message': 'Notification successfully Added!'}, 200
        else:
            return {'message': 'No such user exist'}, 200


class UserNotifications(Resource):
    @jwt_required()
    def get(self, id):
        notifications = NotificationModel.find_all_user_notifications(id)
        if notifications:
            return {'notifications': [notification.json() for notification in notifications]}, 200
        return {'message': 'No notifications found!'}, 200


class DeleteUserNotification(Resource):
    @jwt_required()
    def delete(self, id):
        NotificationModel.delete_user_notification_by_id(id)
        return {'message': 'successfully deleted from database!'}, 200
