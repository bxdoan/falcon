import falcon
import json
from model import Customer
from sqlalchemy.orm import class_mapper
from config import db

class CustomersResource():

    def on_get(self, req, resp):
        dbsession = db
        customers = dbsession.query(Customer)\
            .order_by(Customer.id.desc())\
            .all()
        resp.status = falcon.HTTP_200
        customers = [dict(
                    id = row.id,
                    name = row.name,
                    dob = row.dob.strftime('%Y-%m-%d')
                    ) for row in customers]
        resp.body = json.dumps(customers)
        dbsession.close()
