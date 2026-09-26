import requests


BASE_URL = "https://jsonplaceholder.typicode.com"


def test_get_user():
    response = requests.get(f"{BASE_URL}/users/1")

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == 1
    assert "name" in data
    assert "email" in data


def test_get_all_users():
    response = requests.get(f"{BASE_URL}/users")

    assert response.status_code == 200

    data = response.json()

    assert isinstance(data, list)
    assert len(data) > 0


def test_get_non_existing_user():
    response = requests.get(f"{BASE_URL}/users/999")

    assert response.status_code == 404


def test_create_user():
    payload = {
        "name": "Aditi Pawar",
        "username": "aditi",
        "email": "aditi@example.com"
    }

    response = requests.post(
        f"{BASE_URL}/users",
        json=payload
    )

    assert response.status_code == 201

    data = response.json()

    assert data["name"] == "Aditi Pawar"
    assert data["username"] == "aditi"
    assert data["email"] == "aditi@example.com"