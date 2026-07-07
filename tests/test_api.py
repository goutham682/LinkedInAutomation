import requests

def test_get_api():
    url = "https://jsonplaceholder.typicode.com/posts/1"

    response = requests.get(url)

    assert response.status_code == 200

    data = response.json()

    assert "id" in data
    assert "title" in data
def test_post_api():
    url = "https://jsonplaceholder.typicode.com/posts"

    payload = {
        "title": "API Automation Test",
        "body": "Testing POST request using Python",
        "userId": 1
    }

    response = requests.post(url, json=payload)

    assert response.status_code == 201

    data = response.json()

    assert data["title"] == "API Automation Test"