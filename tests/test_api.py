def test_ping(test_client):
    response = test_client.get("/ping")
    assert response.status_code == 200
    assert response.json["message"] == "pong"

def test_addition(test_client):
    response = test_client.post("/add", json={"a": 2, "b": 3})
    print("Status:", response.status_code)
    print("Response JSON:", response.json)
    assert response.status_code == 200
    assert response.json["result"] == 5
