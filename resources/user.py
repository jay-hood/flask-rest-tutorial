from werkzeug.security import safe_str_cmp
from flask_restful import Resource, reqparse
from flask_jwt_extended import create_refresh_token, create_access_token
from models.user import UserModel

_user_parser = reqparse.RequestParser()
_user_parser.add_argument('username', type=str, required=True, help="This field cannot be blank")
_user_parser.add_argument('password', type=str, required=True, help="This field cannot be blank")

class UserRegister(Resource):


    def post(self):

        data = _user_parser.parse_args()
        if UserModel.find_by_username(data['username']):
            return {"message": "User already exists"}, 400
        else:
            user = UserModel(**data)
            user.save_to_db()

            return {"message": "User created successfully."}, 201

class User(Resource):

    @classmethod
    def get(cls, user_id):
        user = UserModel.find_by_id(user_id)
        if not user:
            return {'message': 'User not found'}, 404
        return user.json(), 200

    @classmethod
    def delete(cls, user_id):
        user = UserModel.find_by_id(user_id)
        if not user:
            return {'message': 'User does not exist'}
        user.delete_from_db()
        return {'message': 'User deleted'}

class UserLogin(Resource):

    @classmethod
    def post(cls):
        data = _user_parser.parse_args()
        user = UserModel.find_by_username(data['username'])
        if user and safe_str_cmp(user.password, data['password']):
            access_token = create_access_token(identity=user.id, fresh=True)
            refresh_token = create_access_token(user.id)
            return {
                'access_token': access_token,
                'refresh_token': refresh_token
            }, 200
        return {'message': 'Invalid credentials'}, 401

