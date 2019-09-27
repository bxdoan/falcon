import falcon
import falcon_jsonify
from falcon_autocrud.middleware import Middleware
import psycopg2
from resource.customer import *
from config import db

api = application = falcon.API(middleware=[Middleware()])
#     middleware=[
#     AuthMiddleware(exclude_routes=['/auth']),
#     falcon_jsonify.Middleware(help_messages=True),
# ])

api.add_route('/customer', CustomersResource())
# api.add_route('/customer/{id:int}', CustomerSingleResource(db))
