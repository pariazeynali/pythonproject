from typing import Any

from flask import jsonify


def template(data, code=500):
    return {
        'message': {
            'errors': {
                'body': data
            }
        },
        'status_code': code
    }


USER_NOT_FOUND = template(['user not found'], code=404)
USER_ALREADY_REGISTERED = template(['User already registered'], code=422)
UNKNOWN_ERROR = template([], code=500)
PACKAGE_NOT_FOUND = template(['package not found'], code=404)
PACKAGE_ALREADY_EXISTS = template(['package with this name already exists'], code=422)
ADMIN_PRIVILEGE_REQUIRED = template(['admin privilege required'], code=406)
INVALID_CREDENTIALS = template(['invalid credentials'], code=401)


class InvalidUsage(Exception):
    status_code = 200

    def __init__(self, message: str, status_code: int = None, payload: Any = None):
        super().__init__()
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_json(self):
        message = self.message
        return jsonify(message)

    @classmethod
    def user_not_found(cls) -> object:
        return cls(**USER_NOT_FOUND)

    @classmethod
    def user_already_registered(cls) -> object:
        return cls(**USER_ALREADY_REGISTERED)

    @classmethod
    def unknown_error(cls) -> object:
        return cls(**UNKNOWN_ERROR)

    @classmethod
    def package_not_found(cls) -> object:
        return cls(**PACKAGE_NOT_FOUND)

    @classmethod
    def package_already_exists(cls) -> object:
        return cls(**PACKAGE_ALREADY_EXISTS)

    @classmethod
    def admin_privilege_required(cls) -> object:
        return cls(**ADMIN_PRIVILEGE_REQUIRED)

    @classmethod
    def invalid_credentials(cls) -> object:
        return cls(**INVALID_CREDENTIALS)
