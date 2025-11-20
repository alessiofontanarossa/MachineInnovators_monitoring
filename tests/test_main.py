from fastapi.testclient import TestClient # to simulate a post
from src.main import app

client = TestClient(app)
def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the Machine Innovators Main Page."}

def test_get_predictions():
    test_sentences = {"sentences": ["I hate this", "I am neutral.", "I love this."]}
    expected_output = [0, 1, 2] 
    response = client.post("/inference", json = test_sentences)
    assert response.status_code == 200
    assert response.json()['predictions'] == expected_output