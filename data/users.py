import datetime

import sqlalchemy as sa

from db.modelbase import SQLAlchemyBase


class UserModel(SQLAlchemyBase):
    __tablename__ = 'users'
    id: int = sa.Column(sa.Integer, autoincrement=True)
    username: str = sa.Column(sa.String(100), primary_key=True)
    password: str = sa.Column(sa.String(100))
    create_date: datetime = sa.Column(sa.DateTime, default=datetime.datetime.now, index=True)
    updated_date: datetime = sa.Column(sa.DateTime, default=datetime.datetime.now, index=True)

    def __repr__(self) -> str:
        return '<User{}'.format(self.id)
