# user accounts
USERS = {
    'resource_methods': ['POST', 'GET'],
    'item_methods': ['GET', 'DELETE', 'PATCH', 'PUT'],
    'hateoas': False,
    'schema': {
        'username': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 50,
            'required': True,
            'unique': True
        },
        'scores': {
            'type': 'list',
            'schema': {
                'type': 'objectid',
                'data_relation': {
                    'resource': 'scores',
                    # make the owner embeddable with ?embedded={"scores":1}
                    'embeddable': True
                },
            },
        },
    }
}
