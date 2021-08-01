import unittest

from sqlalchemy.orm import Session, sessionmaker

from test_engine import engine
from data.users import UserModel
from db.modelbase import SQLAlchemyBase

Session = sessionmaker()


class TestUser(unittest.TestCase):

    def setUp(self) -> None:
        self.connection = engine.connect()
        self.session = Session(bind=self.connection)
        SQLAlchemyBase.metadata.create_all(engine)
        for table in reversed(SQLAlchemyBase.metadata.sorted_tables):
            self.session.execute(table.delete())

    def test_when_user_sign_in(self) -> None:
        u = UserModel()
        u.username = 'ppp'
        u.password = '1234'
        self.session.add(u)
        self.session.commit()
        assert 1 == self.session.query(UserModel).count()


