from app import app

def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200

def test_content():
    client = app.test_client()
    response = client.get("/")
    assert response.data == b"Hello from CI/CD!"

def test_not_found():
    client = app.test_client()
    response = client.get("/notfound")
    assert response.status_code == 404
