import os

from dotenv import load_dotenv, find_dotenv
from flask import request
from jwt import decode
from functools import wraps


def Auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):

        load_dotenv(find_dotenv())

        token = None

        if "Authorization" in request.headers:
            token = request.headers["Authorization"].split(" ")[1]
        if not token:
            return {
                "message": "token not found"
            }, 204

        try:
            data = decode(token, os.environ.get("JWT_SECRET"), algorithms=["HS256"])

            user = data["userId"]
            if user is None:
                return {
                    "message": "Invalid token, not permission"
                }, 401

        except Exception as E:
            return {
                "message": "Internal Server Error",
                "token": data,
                "error": str(E)
            }, 500

        return f(user, *args, **kwargs)

    return decorated
