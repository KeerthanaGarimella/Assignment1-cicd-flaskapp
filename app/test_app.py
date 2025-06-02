import pytest
from app import app  # ✅ Make sure you're importing correctly

# ✅ 1st test - basic route works
def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200

# ✅ 2nd test - content is correct
def test_content():
    client = app.test_client()
    response = client.get("/")
    assert response.data == b"Hello from CI/CD!"

# ✅ 3rd test - 404 on non-existing page
def test_not_found():
    client = app.test_client()
    response = client.get("/doesnotexist")
    assert response.status_code == 404
