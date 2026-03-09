import pytest
from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)


def test_get_activities():
    # Arrange
    # No setup needed for this test

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    assert isinstance(response.json(), dict)


def test_signup_activity():
    # Arrange
    email = "test@example.com"
    activity_name = "Chess Club"
    url = f"/activities/{activity_name}/signup?email={email}"

    # Act
    response = client.post(url)

    # Assert
    assert response.status_code == 200
    assert response.json()["message"] == f"Signed up {email} for {activity_name}"


def test_unregister_activity():
    # Arrange
    email = "test@example.com"
    activity_name = "Chess Club"
    signup_url = f"/activities/{activity_name}/signup?email={email}"
    unregister_url = f"/activities/{activity_name}/participants?email={email}"

    # Ensure the user is signed up first
    client.post(signup_url)

    # Act
    response = client.delete(unregister_url)

    # Assert
    assert response.status_code == 200
    assert response.json()["message"] == f"Unregistered {email} from {activity_name}"