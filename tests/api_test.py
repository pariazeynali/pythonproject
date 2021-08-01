import unittest
import json

from sqlalchemy.orm import Session, sessionmaker

from app import app as test_app
from test_engine import engine
from db.modelbase import SQLAlchemyBase

Session = sessionmaker()


class TestApi(unittest.TestCase):

    def setUp(self) -> None:
        self.app = test_app.test_client()
        self.connection = engine.connect()
        self.session = Session(bind=self.connection)
        SQLAlchemyBase.metadata.create_all(engine)

    def tearDown(self) -> None:
        for table in reversed(SQLAlchemyBase.metadata.sorted_tables):
            self.session.execute(table.delete())
        self.connection.close()

    def test_successful_signup(self):
        user = json.dumps({
            "username": "user1",
            "password": "123456"
        })

        response = self.app.post('/register', headers={"Content-Type": "application/json"}, data=user)
        self.assertEqual(response.status_code, 200)

    def test_successful_add_package(self):
        package = json.dumps({
            "name": "p5",
            "summary": "sp1",
            "description": "dp1"
        })

        response = self.app.post('/add-package', headers={"Content-Type": "application/json"}, data=package)
        self.assertEqual(response.status_code, 200)
