# The DOMAIN dict explains which resources will be available and how they will
# be accessible to the API consumer.
from .scores import SCORES
from .users import USERS

DOMAIN = {
    'users': USERS,
    'scores': SCORES,
}
