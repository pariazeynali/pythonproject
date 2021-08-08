from flask_jwt_extended import jwt_required, get_jwt_claims, jwt_optional, get_jwt_identity
from flask_restful import Resource, reqparse

from services.package_services import find_package_by_name, create_package, delete_package_from_db, all_packages
from schemas.package_schema import package_schema, packages_schema
from exceptions import InvalidUsage

_package_parser = reqparse.RequestParser()
_package_parser.add_argument('name', type=str, required=True, help='this field cannot be blank!')
_package_parser.add_argument('summary', type=str)
_package_parser.add_argument('description', type=str)


class Package(Resource):

    def get(self, name):
        package = find_package_by_name(name)
        if package is not None:
            return package_schema.dump(package)
        return InvalidUsage.package_not_found()

    @jwt_required
    def put(self, name):
        claims = get_jwt_claims()
        if not claims['is_admin']:
            return InvalidUsage.admin_privilege_required()
        data = _package_parser.parse_args()
        package = find_package_by_name(name)
        if package is not None:
            package.summary = data['summary']
            package.description = data['description']
        else:
            package = Package(name, **data)

        create_package(package.name, package.summary, package.description)
        return {"massage": "package updated successfully"}, 200

    @jwt_required
    def delete(self, name):
        claims = get_jwt_claims()
        if not claims['is_admin']:
            return InvalidUsage.admin_privilege_required()

        try:
            delete_package_from_db(name)
            return {"massage": "package deleted"}, 200
        except:
            InvalidUsage.unknown_error()


class AddPackage(Resource):
    @jwt_required
    def post(self):
        claims = get_jwt_claims()
        if not claims['is_admin']:
            return InvalidUsage.admin_privilege_required()
        data = _package_parser.parse_args()
        # package = find_package_by_name(data['name'])
        # if package is not None:
        #     return InvalidUsage.package_already_exists()
        try:
            create_package(data['name'], data['summary'], data['description'])
            return {"massage": "package created successfully!"}, 200
        except:
            return InvalidUsage.unknown_error()


class PackageList(Resource):
    @jwt_optional
    def get(self):
        username = get_jwt_identity()
        packages = packages_schema.dump(all_packages())
        if username:
            return {"packages": packages}
        return {
            "packages": [package['name'] for package in packages],
            "massage": "more information if you login"
        }
