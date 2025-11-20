import os, csv
from unittest.mock import patch # to leave the original sentiment.csv clean from the test productions
from fastapi.testclient import TestClient # to simulate a post
from src.main import app

client = TestClient(app)
def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the Machine Innovators Main Page."}

def test_get_predictions():
    TEST_CSV_PATH = "data/test_sentiment.csv"
    test_sentences = {"sentences": ["I hate this", "I am neutral.", "I love this."]}
    expected_output = [0, 1, 2] 
    with patch("src.main.CSV_PATH", TEST_CSV_PATH):
        response = client.post("/inference", json=test_sentences)
        assert response.status_code == 200
        assert response.json()['predictions'] == expected_output
        assert os.path.exists(TEST_CSV_PATH)
  
    if os.path.exists(TEST_CSV_PATH): # clean the test file
        os.remove(TEST_CSV_PATH)