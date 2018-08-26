import json

from eve.auth import TokenAuth

from jwt_helper import decode_token


# noinspection PyBroadException
class TokenAuthCutom(TokenAuth):
    def check_auth(self, token, allowed_roles, resource, method):
        try:
            payload = decode_token(token)
            # check if payload is valid and if allowed_roles is not empty check if role is valid
            return payload
        except:
            return json.dumps({
                'error': 'token expired.'
            })
