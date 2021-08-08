from typing import Optional

from flask_bcrypt import Bcrypt

from db import db_session
from data.users import UserModel

bcrypt = Bcrypt()


def find_user_by_username(uname) -> Optional[UserModel]:
    session = db_session.create_session()
    return session.query(UserModel).filter(UserModel.username == uname).first()


def find_user_by_userid(userid) -> Optional[UserModel]:
    session = db_session.create_session()
    return session.query(UserModel).filter(UserModel.id == userid).first()


def hash_pass(password) -> str:
    hashed_password = bcrypt.generate_password_hash(password)
    return hashed_password


def delete_user_from_db(name) -> None:
    session = db_session.create_session()
    user = session.query(UserModel).filter(UserModel.username == name).one()
    session.delete(user)
    session.commit()


def create_user(username: str, password: str) -> Optional[UserModel]:
    session = db_session.create_session()
    user = UserModel()
    user.username = username
    user.password = hash_pass(password)
    session.add(user)
    session.commit()


def all_users() ->Optional[UserModel]:
    session = db_session.create_session()
    return session.query(UserModel).all()
