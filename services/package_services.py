from typing import Optional

from db import db_session
from data.packages import Package


def find_package_by_name(pname) -> Optional[Package]:
    session = db_session.create_session()
    return session.query(Package).filter(Package.name == pname)


def find_package_by_id(packageid) -> Optional[Package]:
    session = db_session.create_session()
    return session.query(Package).filter(Package.id == packageid).first()


def all_packages() -> Optional[Package]:
    session = db_session.create_session()
    return session.query(Package).all()


def create_package(name: str, summary: str, description: str) -> Optional[Package]:
    session = db_session.create_session()
    package = Package()
    package.name = name
    package.summary = summary
    package.description = description
    session.add(package)
    session.commit()


def delete_package_from_db(name) -> None:
    session = db_session.create_session()
    package = session.query(Package).filter(Package.name == name).one()
    session.delete(package)
    session.commit()
