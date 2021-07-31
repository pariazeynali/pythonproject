from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field

from data.users import UserModel


class UserSchema(SQLAlchemySchema):
    class Meta:
        model = UserModel
        include_relationships = True
        load_instance = True

    username = auto_field()
    password = auto_field()


user_schema = UserSchema()
users_schema = UserSchema(many=True)
