import datetime

import sqlalchemy as sa
import sqlalchemy.orm as orm

from db.modelbase import SQLAlchemyBase


class Release(SQLAlchemyBase):
    __tablename__ = 'releases'

    name = sa.Column(sa.String, primary_key=True, unique=True)
    major_var: int = sa.Column(sa.BigInteger, index=True)
    minor_var: int = sa.Column(sa.BigInteger, index=True)
    build_var: int = sa.Column(sa.BigInteger, index=True)

    create_date = sa.Column(sa.DateTime, default=datetime, index=True)

    package_id = sa.Column(sa.String, sa.ForeignKey("packages.id"))
    package = orm.relation('Package')

    @property
    def version_text(self):
        return '{}.{}.{}'.format(self.major_ver, self.minor_ver, self.build_ver)
