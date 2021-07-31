import unittest
import json

from sqlalchemy.orm import Session, sessionmaker

from app import app as test_app
from test_engine import engine
from data.modelbase import SQLAlchemyBase

Session = sessionmaker()


class TestApi(unittest.TestCase):

    def setUp(self) -> None:
        self.app = test_app.test_client()
        self.connection = engine.connect()
        self.session = Session(bind=self.connection)
        SQLAlchemyBase.metadata.create_all(engine)
        for table in reversed(SQLAlchemyBase.metadata.sorted_tables):
            self.session.execute(table.delete())
        self.connection.close()

    def test_successful_signup(self):
        # Given
        user = json.dumps({
            "username": "user1",
            "password": "123456"
        })

        # When
        response = self.app.post('/register', headers={"Content-Type": "application/json"}, data=user)
        print(response)
        assert 400 == response.status_code

    # def test_successful_login(self):
    #    pass

    def test_successful_add_package(self):
        package = json.dumps({
            "name": "p1",
            "summary": "sp1",
            "description": "dp1"
        })

        response = self.app.post('/add-package', headers={"Content-Type": "application/json"}, data=package)
        assert 400 == response.status_code
        assert response.json == {'massage': 'package with name p1 already exists'}
