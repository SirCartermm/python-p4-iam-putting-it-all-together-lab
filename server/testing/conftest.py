import pytest
from app import app, db
from models import User, Recipe

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

@pytest.fixture
def db_session():
    db.create_all()
    yield db.session
    db.drop_all()

@pytest.fixture
def user(db_session):
    user = User(username='testuser', password='testpassword', image_url='https://example.com/image', bio='Test bio')
    db_session.add(user)
    db_session.commit()
    return user

@pytest.fixture
def recipe(db_session, user):
    recipe = Recipe(title='Test recipe', instructions='Test instructions', minutes_to_complete=30, user_id=user.id)
    db_session.add(recipe)
    db_session.commit()
    return recipe

@pytest.fixture
def login(client, user):
    response = client.post('/login', json={'username': user.username, 'password': 'testpassword'})
    assert response.status_code == 200
    return response

@pytest.fixture
def logout(client):
    response = client.delete('/logout')
    assert response.status_code == 204
    return response