from flask_jwt_extended import jwt_required, get_jwt_claims, jwt_optional, get_jwt_identity
from flask_restful import Resource, reqparse

from services.package_services import *
from schemas.package_schema import package_schema, packages_schema

_package_parser = reqparse.RequestParser()
_package_parser.add_argument('name', type=str, required=True, help='this field cannot be blank!')
_package_parser.add_argument('summary', type=str)
_package_parser.add_argument('description', type=str)


class Package(Resource):

    def get(self, name):
        package = find_package_by_name(name)
        if package:
            return package_schema.dump(package)
        return {"massage": "Package not found"}, 404

    def put(self, name):
        data = _package_parser.parse_args()
        package = find_package_by_name(name)
        if package:
            package.summary = data['summary']
            package.description = data['description']
        else:
            package = Package(name, **data)

        create_package(package.name, package.summary, package.description)

    @classmethod
    @jwt_required
    def delete(cls, name):
        claims = get_jwt_claims()
        if not claims['is_admin']:
            return {"massage": "admin privilege required"}

        delete_package_from_db(name)

        return {"massage": "package deleted"}


class APackage(Resource):
    def post(self):
        data = _package_parser.parse_args()
        if find_package_by_name(data['name']):
            return {"massage": "package with name {} already exists".format(data['name'])}, 400
        try:
            create_package(data['name'], data['summary'], data['description'])
            return {"massage": "package created successfully!"}, 200
        except:
            return {"massage": "unknown error"}, 500


class PackageList(Resource):
    @jwt_optional
    def get(self):
        username = get_jwt_identity()
        packages = packages_schema.dump(all_packages())
        if username:
            return {"packages": packages}
        return {
            "items": [package['name'] for package in packages],
            "massage": "more information if you login"
        }
