import pytest
from fastapi.testclient import TestClient
from app.app import app, create_access_token, authenticate_user, fake_users_db

client = TestClient(app)

def test_get_producao():
    response = client.get("/producao")
    assert response.status_code == 200
    assert response.json() is not None

def test_login_for_access_token():
    response = client.post(
        "/token",
        data={"username": "johndoe", "password": "fakehashedpassword"},
    )
    assert response.status_code == 200
    assert "access_token" in response.json()
    assert response.json()["token_type"] == "bearer"

def test_login_for_access_token_invalid_credentials():
    response = client.post(
        "/token",
        data={"username": "johndoe", "password": "wrongpassword"},
    )
    assert response.status_code == 401
    assert response.json() == {"detail": "Incorrect username or password"}

def test_read_users_me():
    # First, get a token
    response = client.post(
        "/token",
        data={"username": "johndoe", "password": "fakehashedpassword"},
    )
    token = response.json()["access_token"]

    # Use the token to access the protected endpoint
    response = client.get(
        "/users/me",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == 200
    assert response.json() == {"username": "johndoe"}

def test_read_users_me_no_token():
    response = client.get("/users/me")
    assert response.status_code == 401
    assert response.json() == {"detail": "Not authenticated"}

def test_create_access_token():
    data = {"sub": "johndoe"}
    token = create_access_token(data)
    assert token is not None

def test_authenticate_user():
    user = authenticate_user(fake_users_db, "johndoe", "fakehashedpassword")
    assert user is not None
    assert user.username == "johndoe"

def test_authenticate_user_invalid():
    user = authenticate_user(fake_users_db, "johndoe", "wrongpassword")
    assert user is False