import os

PORT = int(os.environ.get('PORT', 5000))
# use '0.0.0.0' to ensure your REST API is reachable from all your
# network (and not only your computer).
HOST = os.environ.get('HOST', '127.0.0.1')

URL_DB = 'localhost'
PORT_DB = 27017 
USER_DB = 'admin'
PASS_DB = '12345'
NAME_DB = 'admin'

MONGO_URI = os.environ.get('MONGODB_URI',
                           'mongodb://%s:%s@%s:%s/%s' % (USER_DB, PASS_DB, URL_DB, PORT_DB, NAME_DB))
JWT_KEY = os.environ.get('JWT_KEY', '1234567890')
JWT_EXP = os.environ.get('JWT_EXP', '15')
ENV = os.environ.get('ENV', 'dev')
HEALTHCHECK_URI = os.environ.get('HEALTHCHECK_URI', '/healthcheck')
PERMISSION_KEY = os.environ.get('PERMISSION_KEY', '123456')
