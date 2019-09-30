import jwt
import bcrypt
import falcon
import json
from datetime import datetime, timedelta
from config import db
from model import User
from passlib.hash import pbkdf2_sha256 as sha256

JWT_SECRET = 'secret'
JWT_ALGORITHM = 'HS256'
JWT_EXP_DELTA_SECONDS = 86400

class Login():
    def on_post(self, req, resp):
        body = req.media
        if not body:
            raise falcon.HTTPBadRequest('Empty request body',
                                        'A valid JSON document is required.')
        username = body['username']
        password = body['password']
        user = db.query(User).filter(User.username == username).first()
        print(user.password)
        print(password)
        if user is None or not sha256.verify(body['password'], user.password):
            raise falcon.HTTPUnauthorized(title='Unauthorized',
                                          description='Authentication failed!!!')
        token = jwt.encode(dict(
            user_id = user.id,
            exp = datetime.utcnow() + timedelta(seconds=int(JWT_EXP_DELTA_SECONDS))
        ), JWT_SECRET, algorithm = JWT_ALGORITHM)
        resp.status = falcon.HTTP_200
        resp.body = json.dumps(dict(
            id = user.id,
            username = user.username,
            token = token.decode('UTF-8')
        ))

class UserRegistration():
    def on_post(self, req, resp):
        try:
            body = req.media
            if not body:
                raise falcon.HTTPBadRequest('Empty request body',
                                            'A valid JSON document is required.')
            new_user = User(
                    username = body['username'],
                    password = sha256.hash(body['password']),
                    dob = '1990-01-10')
            db.add(new_user)
            db.commit()
            resp.status = falcon.HTTP_200
            resp.body = {'msg': 'register done!!!'}
        except:
            raise falcon.HTTPBadRequest('registration', 'Can NOT create user!!!')
