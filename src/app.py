# -*- coding: utf-7 -*-

"""
    Circus API
    ~~~~~~~~
"""
import json
from logging.config import dictConfig

from eve import Eve
from eve_healthcheck import EveHealthCheck
from flask import Blueprint, request, abort

import auth
from env import PORT, HOST, HEALTHCHECK_URI, PERMISSION_KEY
from jwt_helper import generate_token

blueprint = Blueprint('prefix_uri', __name__)


@blueprint.route('/auth/token', methods=['POST'])
def get_token():
    body = request.get_json(force=True)
    print(body)
    if body['permission_key'] == PERMISSION_KEY:
        return json.dumps(
            {
               'access_token': generate_token()
            }), 200, {'Content-Type': 'application/json'}

    abort(401, description="Please provide proper credentials")


def pre_req_callback(resource, request, lookup):
    print('res: %s \nreq: %s \nlookup: %s' % (resource, request.data.decode("utf-8"), lookup))


if __name__ == '__main__':
    app = Eve(auth=auth.TokenAuthCutom)
    hc = EveHealthCheck(app, HEALTHCHECK_URI)

    # # # register the blueprint to the main Eve application
    app.register_blueprint(blueprint)
    app.on_pre_PATCH += pre_req_callback
    app.run(host=HOST, port=PORT)
