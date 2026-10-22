import requests


BASE_URL = "https://qa-scooter.education-services.ru"

class TestObtainingListOfOrders():
    def test_obtaining_list_of_orders(self, user_registration_fixture):
        login = user_registration_fixture["login"]
        password = user_registration_fixture["password"]
    
        payload = {
            "login": login,
            "password": password
        }
        response_ = requests.post(f"{BASE_URL}/api/v1/courier/login", data=payload)
        id = response_.json()["id"]

        payload_ = {"courierId":id}
        response = requests.get(f"{BASE_URL}/api/v1/orders", params=payload_)

        assert response.status_code == 200, f"Баг ждали 200, получили {response.status_code}"
        data = response.json()
        assert "orders" in data, f"Баг: нет 'orders' в ответе: {data}"
        assert isinstance(data["orders"], list), f"Баг: 'orders' не список: {data['orders']}"