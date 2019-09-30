import falcon
import jwt

JWT_SECRET = 'secret'
JWT_ALGORITHM = 'HS256'
JWT_EXP_DELTA_SECONDS = 86400

class AuthMiddleware(object):
    def __init__(self, exclude_routes=[]):
        self.exclude_routes = exclude_routes

    def process_request(self, req, resp):
        for route in self.exclude_routes:
            if route in req.path:
                return

        value = req.get_header('Authorization')
        print(value)
        challenges = ['Token type="Bearer"']

        if value is None:
            description = ('Please provide an auth token '
                           'as part of the request.')
            raise falcon.HTTPUnauthorized('Auth token required',
                                          description,
                                          challenges,
                                          href='https://auth0.com/docs/jwt')
        token = value.split(' ')[1]
        print(token)
        if not self._is_token_valid(token):
            description = ('The provided auth token is not valid. '
                           'Please request a new token and try again.')
            raise falcon.HTTPUnauthorized('Authentication required',
                                          description,
                                          challenges,
                                          href='https://auth0.com/docs/jwt')

    def _is_token_valid(self, token):
        try:
            jwt.decode(bytes(token, encoding='UTF-8'), JWT_SECRET,
             algorithm = JWT_ALGORITHM, verify=True)
        except (jwt.InvalidTokenError, jwt.DecodeError) as e:
            print(">>> TOKEN ERROR", e)
            return False
        return True
