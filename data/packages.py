import datetime

import sqlalchemy as sa

from db.modelbase import SQLAlchemyBase


class Package(SQLAlchemyBase):
    __tablename__ = 'packages'

    id: int = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    name: str = sa.Column(sa.String(100))
    create_date: datetime = sa.Column(sa.DateTime, default=datetime.datetime.now, index=True)
    updated_date: datetime = sa.Column(sa.DateTime, onupdate=datetime.datetime.now, index=True)
    summary: str = sa.Column(sa.String(100))
    description: str = sa.Column(sa.String(100))

    def __repr__(self) -> str:
        return '<Package{}'.format(self.id)
