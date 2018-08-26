from datetime import datetime, timedelta

import jwt

from env import JWT_KEY, JWT_EXP


def decode_token(token, options=None):
    return jwt.decode(token, JWT_KEY, algorithms=['HS256'], options=options)


def generate_token():
    return jwt.encode(
        {
            'exp': datetime.utcnow() + timedelta(minutes=float(JWT_EXP)),
            'iat': datetime.utcnow()
        }, JWT_KEY, algorithm='HS256').decode("utf-8")
