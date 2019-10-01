import falcon
import falcon_jsonify
from middleware.AuthMiddleware import AuthMiddleware
import psycopg2
from resource.customer import *
from resource.auth import *
from config import engine

api = application = falcon.API(
    middleware=[AuthMiddleware(exclude_routes=['/login'])])

api.add_route('/login', Login())
api.add_route('/registration', UserRegistration())
api.add_route('/customer', CustomersResource())
