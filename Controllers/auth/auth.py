from flask import request
from jwt import decode
from functools import wraps

def Auth(f):
    @wraps(f)
    def __Auth(*args, **kwargs):
                
        token = request.authorization
        if not token:
            return 204

        else: 
            try:
                decoded = decode(token, os.environ.get("JWT_SECRET"), algorithms=["HS256"])
                if decoded:
                    return 200
            except Exception as E:
                return 401

    return __Auth()