from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from data.packages import Package


class PackageSchema(SQLAlchemySchema):
    class Meta:
        model = Package
        include_relationships = True
        load_instance = True

    name = auto_field()
    summary = auto_field()
    description = auto_field()


package_schema = PackageSchema()
packages_schema = PackageSchema(many=True)
