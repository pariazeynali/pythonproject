import datetime

import sqlalchemy as sa

from data.modelbase import SQLAlchemyBase


class UserModel(SQLAlchemyBase):
    __tablename__ = 'users'
    id = sa.Column(sa.Integer, autoincrement=True)
    username = sa.Column(sa.String, primary_key=True)
    password = sa.Column(sa.String)
    create_date = sa.Column(sa.DateTime, default=datetime.datetime.now, index=True)
    updated_date = sa.Column(sa.DateTime, default=datetime.datetime.now, index=True)

    def __repr__(self):
        return '<User{}'.format(self.id)

