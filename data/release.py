import datetime

import sqlalchemy as sa
import sqlalchemy.orm as orm

from db.modelbase import SQLAlchemyBase


class Release(SQLAlchemyBase):
    __tablename__ = 'releases'

    name: str = sa.Column(sa.String(100), primary_key=True, unique=True)
    major_var: int = sa.Column(sa.BigInteger, index=True)
    minor_var: int = sa.Column(sa.BigInteger, index=True)
    build_var: int = sa.Column(sa.BigInteger, index=True)

    create_date: datetime = sa.Column(sa.DateTime, default=datetime, index=True)

    package_id: int = sa.Column(sa.Integer, sa.ForeignKey("packages.id"))
    package = orm.relation('Package')

    @property
    def version_text(self):
        return '{}.{}.{}'.format(self.major_ver, self.minor_ver, self.build_ver)
