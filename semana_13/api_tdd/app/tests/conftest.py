import pytest
from flask_jwt_extended import create_access_token

from app.database import db
from app.run import app


@pytest.fixture(scope="module")
def test_client():
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
    app.config["JWT_SECRET_KEY"] = "test_secret_key"

    with app.test_client() as testing_client:
        with app.app_context():
            db.create_all()
            yield testing_client
            db.drop_all()


@pytest.fixture(scope="module")
def auth_headers():
    with app.app_context():
        access_token = create_access_token(
            identity={"username": "testuser", "roles": '["admin"]'}
        )
        headers = {"Authorization": f"Bearer {access_token}"}
        return headers
    
def test_get_animals(test_client, auth_headers):
    response = test_client.get('/animals', headers=auth_headers)
    assert response.status_code == 200

def test_create_animal_as_user(test_client, auth_headers):
    new_animal = {"name": "Lion", "species": "Panthera leo"}
    response = test_client.post('/animals', json=new_animal, headers=auth_headers)
    assert response.status_code == 403  # Assuming 'user' role cannot create animals

def test_update_animal_as_user(test_client, auth_headers):
    update_data = {"name": "Lion", "species": "Panthera leo"}
    response = test_client.put('/animals/1', json=update_data, headers=auth_headers)
    assert response.status_code == 403  # Assuming 'user' role cannot update animals

def test_delete_animal_as_user(test_client, auth_headers):
    response = test_client.delete('/animals/1', headers=auth_headers)
    assert response.status_code == 403  # Assuming 'user' role cannot delete animals

def test_create_user_with_invalid_data(test_client):
    invalid_user_data = {"username": "", "password": "short"}
    response = test_client.post('/users', json=invalid_user_data)
    assert response.status_code == 400  # Bad request due to invalid data

def test_access_with_invalid_token(test_client):
    headers = {"Authorization": "Bearer invalidtoken"}
    response = test_client.get('/animals', headers=headers)
    assert response.status_code == 401  # Unauthorized due to invalid token
