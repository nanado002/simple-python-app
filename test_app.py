from app import app

def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"Welcome" in response.data

def test_add():
    client = app.test_client()
    response = client.get("/add?a=5&b=7")
    assert response.status_code == 200
    assert response.get_json() == {"sum": 12}

