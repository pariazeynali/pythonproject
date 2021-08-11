import os
import sys

from flask import Flask
from flask_jwt_extended import JWTManager
from flask_restful import Api
from dotenv import load_dotenv, find_dotenv

from db.db_session import engine
from db.modelbase import SQLAlchemyBase
from resourse.user_resourse import UserRegister, User, UsersList, UserLogin
from resourse.package_resourse import Package, PackageList, AddPackage

folder = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, folder)

app = Flask(__name__)
app.config['PROPAGATE_EXCEPTION'] = True
app.secret_key = os.getenv('SECRET_KEY')
api = Api(app)


def main():
    setup_db()
    app.run( debug=True)
    load_dotenv(find_dotenv())


# noinspection PyUnresolvedReferences
def setup_db():
    import data.__all_models
    SQLAlchemyBase.metadata.create_all(engine)


jwt = JWTManager(app)


@jwt.additional_claims_loader
def add_claims_to_jwt(identity):
    admin_username = os.getenv('ADMIN_USERNAME')
    if identity == admin_username:
        return {'is_admin': True}
    return {'is_admin': False}


api.add_resource(UserRegister, '/register')
api.add_resource(Package, '/package/<string:name>')
api.add_resource(AddPackage, '/add-package')
api.add_resource(PackageList, '/packages')
api.add_resource(User, '/user/<string:username>')
api.add_resource(UsersList, '/users')
api.add_resource(UserLogin, '/login')

if __name__ == '__main__':
    main()
