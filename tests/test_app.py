"""
Integration tests for the Flask application.
"""
import pytest
from app import app

@pytest.fixture
def client():
    """
    Flask test client fixture.
    """
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_home_page(client):
    """
    Test that the home page loads successfully.
    """
    response = client.get("/")
    assert response.status_code == 200
    assert b"Blog Personal" in response.data

def test_login_logout_flow(client):
    """
    Test the admin login and logout flow.
    """
    # Login with correct credentials
    response = client.post(
        "/admin/login",
        data={"username": "admin", "password": "password"},
        follow_redirects=True
    )
    assert b"Dashboard" in response.data or b"dashboard" in response.data

    # Logout
    response = client.get("/admin/logout", follow_redirects=True)
    assert b"Blog Personal" in response.data

def test_dashboard_requires_login(client):
    """
    Test that the dashboard redirects to login if not authenticated.
    """
    response = client.get("/admin/dashboard", follow_redirects=True)
    assert b"Iniciar sesi" in response.data or b"Login" in response.data
