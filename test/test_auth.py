import falcon
from falcon import testing
import pytest
import json
import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')
from app import api

@pytest.fixture()
def client():
    # Assume the hypothetical `myapp` package has a function called
    # `create()` to initialize and return a `falcon.API` instance.
    return testing.TestClient(api)


def test_login(client):
    body = {
        'username': 'doan',
        'password': 'doan'
    }
    result = client.simulate_post('/login', body=json.dumps(body))
    assert result.status == falcon.HTTP_200
