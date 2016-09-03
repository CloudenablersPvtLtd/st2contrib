class HTTP_CODES(object):
    SUCCESS = 200
    CREATED = 201
    NO_CONTENT = 204
    BAD_REQUEST = 400
    UNAUTHORIZED = 401
    FORBIDDEN = 403
    NOT_FOUND = 404


class RESPONSE_MESSAGES(object):
    SUCCESS = 'success'
    FAILED = 'failed'
    CREATE_SUCCESS = 'Created Successfully'
    DELETE_SUCCESS = 'Deleted Successfully'


class RESOURCE_MAP(object):
    TICKETS = 'tickets'
    USERS = 'users'
    ORGANIZATIONS = 'organizations'
