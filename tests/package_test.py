import unittest

from sqlalchemy.orm import Session, sessionmaker

from test_engine import engine
from db.modelbase import SQLAlchemyBase
from data.packages import Package


Session = sessionmaker()


class TestPackage(unittest.TestCase):

    def setUp(self) -> None:
        self.connection = engine.connect()
        self.session = Session(bind=self.connection)
        for table in reversed(SQLAlchemyBase.metadata.sorted_tables):
            self.session.execute(table.delete())

    def test_when_add_new_package(self) -> None:
        p = Package()

        p.name = 'p1'
        p.summary = 'summary of p1'
        p.description = 'description of p1'

        self.session.add(p)
        self.session.commit()
        self.assertEqual(1, self.session.query(Package).count())

    def test_when_update_a_package(self) -> None:
        p = Package()

        p.name = 'p1'
        p.summary = 'summary of p1'
        p.description = 'description of p1'

        self.session.add(p)
        self.session.commit()

        new_summary = 'summary of package 1'
        p.summary = new_summary

        self.session.add(p)
        self.session.commit()

        p1 = p

        self.assertEqual(1, self.session.query(Package).count())
        self.assertEqual(new_summary, p1.summary)

    def test_when_delete_package(self) -> None:
        p = Package()

        p.name = 'p1'
        p.summary = 'summary of p1'
        p.description = 'description of p1'

        self.session.add(p)
        self.session.commit()
        self.assertEqual(1, self.session.query(Package).count())
        self.session.delete(p)
        self.session.commit()
        self.assertEqual(0, self.session.query(Package).count())
