import sqlalchemy as sa
import sqlalchemy.orm as orm
from sqlalchemy.orm import Session

engine = sa.create_engine('mysql+mysqlconnector://paria:123456@localhost:3306/python', echo=True)


def create_session() -> Session:
    Session = orm.sessionmaker(bind=engine)
    session = Session()
    return session
