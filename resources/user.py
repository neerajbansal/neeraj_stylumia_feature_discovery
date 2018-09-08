from models.user import UserModel
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required, current_identity


class User(Resource):

    @jwt_required()
    def get(self, id):
        users = UserModel.find_by_id(id)
        if users:
            return {'user': users}, 200
        return {'message': 'User not found!'}, 404
