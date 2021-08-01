from marshmallow import Schema, fields
from data.packages import Package


class PackageSchema(Schema):

    class Meta:
        model = Package
        include_relationships = True
        load_instance = True

    name = fields.Str()
    summary = fields.Str()
    description = fields.Str()


package_schema = PackageSchema()
packages_schema = PackageSchema(many=True)
