from marshmallow import Schema, fields

from data.users import UserModel


class UserSchema(Schema):
    class Meta:
        model = UserModel
        include_relationships = True
        load_instance = True

    username = fields.Str()


user_schema = UserSchema()
users_schema = UserSchema(many=True)
