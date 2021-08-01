from flask_jwt_extended import create_access_token, create_refresh_token, jwt_refresh_token_required, get_jwt_identity
from flask_restful import Resource, reqparse

from services.user_services import find_user_by_username, delete_from_db, create_user, bcrypt, all_users
from schemas.user_schema import user_schema, users_schema
from exceptions import InvalidUsage

_user_parser = reqparse.RequestParser()
_user_parser.add_argument('username', type=str, required=True, help='Enter username')
_user_parser.add_argument('password', type=str, required=True, help='Enter password')


class UserRegister(Resource):
    def post(self):
        data = _user_parser.parse_args()
        if find_user_by_username(data['username']):
            return InvalidUsage.user_already_registered()
        try:
            create_user(data['username'], data['password'])
            return {"massage": "user created successfully"}, 201
        except:
            return InvalidUsage.unknown_error()


class User(Resource):
    @classmethod
    def get(cls, username):
        user = find_user_by_username(username)
        if user is None:
            return InvalidUsage.user_not_found()
        return user_schema.dump(user)

    @classmethod
    def delete(cls, username):
        user = find_user_by_username(username)
        if not user:
            return InvalidUsage.user_not_found()
        delete_from_db(user)
        return {"massage": "User deleted successfully"}, 200


class UserLogin(Resource):

    @classmethod
    def post(cls):
        data = _user_parser.parse_args()
        user = find_user_by_username(data['username'])
        if user and bcrypt.check_password_hash(user.password, data['password']):
            access_token = create_access_token(identity=user.username, fresh=True)
            refresh_token = create_refresh_token(user.id)
            return {
                       'access_token': access_token,
                       'refresh_token': refresh_token,
                   }, 200
        return InvalidUsage.invalid_credentials()


class UsersList(Resource):
    def get(self):
        return users_schema.dump(all_users())


class TokenRefresh(Resource):
    @jwt_refresh_token_required
    def post(self):
        current_user = get_jwt_identity()
        new_token = create_access_token(identity=current_user, fresh=False)
        return {'access_token': new_token}, 200
