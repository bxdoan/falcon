import falcon
import json
from model import Customer
from sqlalchemy.orm import class_mapper
from config import db

class CustomersResource():
    def on_get(self, req, resp):
        customers = db.query(Customer)\
            .order_by(Customer.id.desc())\
            .all()
        resp.status = falcon.HTTP_200
        customers = [dict(
                    id = row.id,
                    name = row.name,
                    dob = row.dob.strftime('%Y-%m-%d')
                    ) for row in customers]
        resp.body = json.dumps(customers)
        db.close()

class CustomerSingleResource():
    def on_get(self, req, resp, id):
        customer = db.query(Customer).filter(Customer.id == id).first()
        if customer is None:
            raise falcon.HTTPNotFound()
        customer = dict(
            id=customer.id,
            name=customer.name,
            dob=customer.dob.strftime('%Y-%m-%d')
        )
        resp.body = json.dumps(customer)
        db.close()

    def on_put(self, req, resp, id):
        body = req.media
        if not body:
            raise falcon.HTTPBadRequest('Empty request body',
                                        'A valid JSON document is required.')
        customer = db.query(Customer).filter(Customer.id == id).first()
        if customer is None:
            raise falcon.HTTPNotFound()
        customer.name = body['name']
        customer.dob = body['dob']
        if len(db.dirty) > 0:
            db.commit()
        new_customer = dict(
            id = customer.id,
            name = customer.name,
            dob = customer.dob.strftime('%Y-%d-%m')
        )
        resp.body = json.dumps(new_customer)
        db.close()

    def on_delete(self, req, resq, id):
        customer = db.query(Customer).filter(Customer.id == id).first()
        if customer is None:
            raise falcon.HTTPNotFound()
        db.delete(customer)
        db.commit()
        db.close()
