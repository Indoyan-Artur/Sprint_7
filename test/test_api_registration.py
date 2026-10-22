import requests


BASE_URL = "https://qa-scooter.education-services.ru"

class TestApiCreatingCourier:
    def test_create_courier(self, user_registration_fixture):
        response = user_registration_fixture["response"]

        assert response.status_code == 201, f"Курьер не создался {response.status_code}"
        assert response.json() == {"ok": True}, f"Курьер не создался {response.json()}"

    def test_two_couriers_not_createdd(self, user_registration_fixture):
        login = user_registration_fixture["login"]
        password = user_registration_fixture["password"]
        name = user_registration_fixture["name"]

        payload = {
            "login": login,
            "password": password,
            "firstName": name
            }
        response = requests.post(f"{BASE_URL}/api/v1/courier", data=payload)

        assert response.status_code == 409, f"Баг ждали 409, получили {response.status_code}"
        assert response.json() == {"code": 409, "message": "Этот логин уже используется."}, f"Баг ждали cod: 409, message: Этот логин уже используется., получили {response.json()}"

    def test_login_field_required(self):
        payload = {
            "password": "33465",
            "firstName": "tryt"
        }
        response = requests.post(f"{BASE_URL}/api/v1/courier", data=payload)

        assert response.status_code == 400, f"Баг ждали 400, получили {response.status_code}"
        assert response.json() == {"code": 400, "message": "Недостаточно данных для создания учетной записи"}, f"Баг ждали code: 400, message: Недостаточно данных для создания учетной записи, получили {response.json()}"

    def test_password_field_required(self):
        payload = {
            "login": "trty",
            "firstName": "tryt"
        }
        response = requests.post(f"{BASE_URL}/api/v1/courier", data=payload)

        assert response.status_code == 400, f"Баг ждали 400, получили {response.status_code}"
        assert response.json() == {"code": 400, "message": "Недостаточно данных для создания учетной записи"}, f"Баг ждали code: 400, message: Недостаточно данных для создания учетной записи, получили {response.json()}"

    #Тест падает, курьер регистрируется без обязательного поля "firstName"
    def test_name_field_required(self):
        payload = {
            "login": "trty",
            "password": "33465"
        }
        response = requests.post(f"{BASE_URL}/api/v1/courier", data=payload)

        assert response.status_code == 400, f"Баг ждали 400, получили {response.status_code}"
        assert response.json() == {"code": 400, "message": "Недостаточно данных для создания учетной записи"}, f"Баг ждали code: 400, message: Недостаточно данных для создания учетной записи, получили {response.json()}"

    