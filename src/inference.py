# this file is used to manually test the API

import requests

url = "http://127.0.0.1:8000/inference"
new_data = {"sentences": ["I am very sad", "I am beautiful", "I am neutral"]}
response = requests.post(url, json = new_data)

if response.status_code == 200:
    print(response.json()) 
else:
    print(f"Error {response.json()}: status code {response.status_code}")