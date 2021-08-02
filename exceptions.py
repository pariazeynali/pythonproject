from typing import Any

from flask import jsonify


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
        return {"massage": "user not found"}, 404

    @classmethod
    def user_already_registered(cls) -> object:
        return {"massage": "user already registered"}, 422

    @classmethod
    def unknown_error(cls) -> object:
        return {"massage": "unknown error"}, 500

    @classmethod
    def package_not_found(cls) -> object:
        return {"massage": "package not found"}, 404

    @classmethod
    def package_already_exists(cls) -> object:
        return {"massage": "package already exists"}, 422

    @classmethod
    def admin_privilege_required(cls) -> object:
        return {"massage": "admin privilege required"}, 406

    @classmethod
    def invalid_credentials(cls) -> object:
        return {"massage": "invalid credentials"}, 401
