import json
from unittest.mock import patch

import pytest
from flask import Flask

from api.endpoints.persona import router


@pytest.fixture
def app():
    app = Flask(__name__)
    app.register_blueprint(router)
    return app


@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture(autouse=True)
def mock_persons_db():
    mock_persons_db = {
        'user1': {'username': 'user1', 'name': 'User One', 'mail': 'user1@example.com'},
        'user2': {'username': 'user2', 'name': 'User Two', 'mail': 'user2@example.com'}
    }
    with patch('models.persons_db', mock_persons_db):
        yield mock_persons_db

def test_list_persons(client):
    response = client.get('/people')
    assert response.status_code == 200
    result = response.get_json()
    assert len(result['persons']) == 2  # Assuming 2 mock persons


def test_get_person_endpoint(client):
    username = 'user1'
    response = client.get(f'/search/{username}')
    assert response.status_code == 200
    person = json.loads(response.data.decode('utf-8'))
    assert person['username'] == username


def test_get_person_endpoint_closematch(client):
    username = 'user'
    response = client.get(f'/search/{username}')
    assert response.status_code == 404
    close_matches = json.loads(response.data.decode('utf-8'))
    assert isinstance(close_matches['suggestions'], list)
    assert len(close_matches['suggestions']) > 0
    assert close_matches['suggestions'][0] == 'user2'


def test_get_person_endpoint_not_found(client):
    username = 'nonexistentuser'
    response = client.get(f'/search/{username}')
    assert response.status_code == 404


def test_create_person(client):
    new_person_data = {'username': 'user3', 'name': 'User Three', 'mail': 'user3@example.com'}
    response = client.post('/people', json=new_person_data)
    assert response.status_code == 201
    created_person = json.loads(response.data.decode('utf-8'))
    assert created_person['username'] == new_person_data['username']


def test_update_person(client):
    username = 'user1'
    updated_person_data = {'name': 'Updated Name'}
    response = client.put(f'/people/{username}', json=updated_person_data)
    assert response.status_code == 200
    updated_person = json.loads(response.data.decode('utf-8'))
    assert updated_person['name'] == updated_person_data['name']


def test_update_person_not_found(client):
    username = 'nonexistentuser'
    updated_person_data = {'name': 'Updated Name'}
    response = client.put(f'/people/{username}', json=updated_person_data)
    assert response.status_code == 404
    error_message = json.loads(response.data.decode('utf-8'))
    assert error_message['error'] == 'Person not found'


def test_delete_person(client):
    username = 'user1'
    response = client.delete(f'/people/{username}')
    assert response.status_code == 200
    deleted_person = json.loads(response.data.decode('utf-8'))
    assert deleted_person['message'] == 'Person deleted'


def test_delete_person_not_found(client):
    username = 'nonexistentuser'
    response = client.delete(f'/people/{username}')
    assert response.status_code == 404
    error_message = json.loads(response.data.decode('utf-8'))
    assert error_message['error'] == 'Person not found'


if __name__ == '__main__':
    pytest.main()
