import jwt
import falcon
from falcon import testing
import pytest
import json
from datetime import datetime, timedelta
import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')
from app import api

JWT_SECRET = 'secret'
JWT_ALGORITHM = 'HS256'
JWT_EXP_DELTA_SECONDS = 86400

token = jwt.encode(dict(
    user_id = int(1),
    exp = datetime.utcnow() + timedelta(seconds=int(JWT_EXP_DELTA_SECONDS))
), JWT_SECRET, algorithm = JWT_ALGORITHM).decode('UTF-8')

customer1 = {
    'id': 1,
    'name': 'Ronaldo',
    'dob': '1991-01-08'
}

@pytest.fixture()
def client():
    # Assume the hypothetical `myapp` package has a function called
    # `create()` to initialize and return a `falcon.API` instance.
    return testing.TestClient(api)


def test_customers(client):
    hdrs = {'Authorization': 'Bearer ' + token}
    print(hdrs)
    result = client.simulate_get('/customer', headers=hdrs)
    assert result.status == falcon.HTTP_200

def test_customer_1(client):
    hdrs = {'Authorization': 'Bearer ' + token}
    result = client.simulate_get('/customer/1', headers=hdrs)
    assert result.status == falcon.HTTP_200
    assert json.loads(result.content.decode()) == customer1
