import datetime

import sqlalchemy as sa

from data.modelbase import SQLAlchemyBase


class Package(SQLAlchemyBase):
    __tablename__ = 'packages'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    name = sa.Column(sa.String)
    create_date = sa.Column(sa.DateTime, default=datetime.datetime.now, index=True)
    updated_date = sa.Column(sa.DateTime, default=datetime.datetime.now, index=True)
    summary = sa.Column(sa.String)
    description = sa.Column(sa.String)

    def __repr__(self):
        return '<Package{}'.format(self.id)
