# this file is used to manually test the API or the container

import requests

url_api = "http://127.0.0.1:8000/inference"
url_container = "http://localhost:7500/inference"
new_data = {"sentences": ["I am very sad", "I am beautiful", "I am neutral"]}
response = requests.post(url_container, json = new_data)

if response.status_code == 200:
    print(response.json()) 
else:
    print(f"Error {response.json()}: status code {response.status_code}")