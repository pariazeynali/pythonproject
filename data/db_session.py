import sqlalchemy as sa
import sqlalchemy.orm as orm
from sqlalchemy.orm import Session

engine = sa.create_engine('sqlite:///db/database.db', echo=True)
__factory = orm.sessionmaker(bind=engine)


def create_session() -> Session:
    global __factory

    session: Session = __factory()
    session.expire_on_commit = False

    return session
