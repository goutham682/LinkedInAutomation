import requests

def test_get_api():
    url = "https://jsonplaceholder.typicode.com/posts/1"

    response = requests.get(url)

    assert response.status_code == 200

    data = response.json()

    assert "id" in data
    assert "title" in data