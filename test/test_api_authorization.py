import requests


BASE_URL = "https://qa-scooter.education-services.ru"

class TestApiCourierLogin:
    def test_courier_authorization(self, user_registration_fixture):
        login = user_registration_fixture["login"]
        password = user_registration_fixture["password"]
    
        payload = {
            "login": login,
            "password": password
        }
        response = requests.post(f"{BASE_URL}/api/v1/courier/login", data=payload)

        dada = response.json()
        assert response.status_code == 200, f"Баг ждали 200, получили {response.status_code}"
        assert "id" in dada, f"Баг ждали id, получили {dada}"

    def test_login_field_required(self, user_registration_fixture):
        password = user_registration_fixture["password"]

        payload = {
            "password": password
        }
        response = requests.post(f"{BASE_URL}/api/v1/courier/login", data=payload)

        assert response.status_code == 400, f"Баг ждали 400, получили {response.status_code}"
        assert response.json() == {"code": 400,"message":  "Недостаточно данных для входа"}, f"Баг ждали code: 400, message: Недостаточно данных для входа, получили {response.json()}"

    #Тест падает с кодом 504 Gateway Timeout что не соответствует документации
    def test_password_field_required(self, user_registration_fixture):
        login = user_registration_fixture["login"]
        
        payload = {
            "login": login
        }
        response = requests.post(f"{BASE_URL}/api/v1/courier/login", data=payload)

        assert response.status_code == 400, f"Баг ждали 400, получили {response.status_code}"
        assert response.json() == {"code": 400,"message":  "Недостаточно данных для входа"}, f"Баг ждали code: 400, message: Недостаточно данных для входа, получили {response.json()}"


    def test_incorrect_login(self, user_registration_fixture):
        login = user_registration_fixture["login"] + "x" 
        password = user_registration_fixture["password"]

        payload = {
            "login": login,
            "password": password
        }
        response = requests.post(f"{BASE_URL}/api/v1/courier/login", data=payload)

        assert response.status_code == 404, f"Баг ждали 404, получили {response.status_code}"
        assert response.json() == {"code": 404,"message": "Учетная запись не найдена"}, f"Баг ждали code: 404, message: Учетная запись не найдена, получили {response.json()}"

    def test_incorrect_password(self, user_registration_fixture):
        login = user_registration_fixture["login"]
        password = user_registration_fixture["password"] + "3"

        payload = {
            "login": login,
            "password": password
        }
        response = requests.post(f"{BASE_URL}/api/v1/courier/login", data=payload)

        assert response.status_code == 404, f"Баг ждали 404, получили {response.status_code}"
        assert response.json() == {"code": 404,"message": "Учетная запись не найдена"}, f"Баг ждали code: 404, message: Учетная запись не найдена, получили {response.json()}"

    def test_there_is_no_login_field(self, user_registration_fixture):
        password = user_registration_fixture["password"]

        payload = {
            "password": password
        }
        response = requests.post(f"{BASE_URL}/api/v1/courier/login", data=payload)
        
        assert response.status_code == 400, f"Баг ждали 400, получили {response.status_code}"
        assert response.json() == {"code": 400,"message": "Недостаточно данных для входа"}, f"Баг ждали code: 400, message: Недостаточно данных для входа, получили {response.json()}"
    # 504
    def test_there_is_no_password_field(self, user_registration_fixture):
        login = user_registration_fixture["login"]
    
        payload = {
            "login": login
        }
        response = requests.post(f"{BASE_URL}/api/v1/courier/login", data=payload)
            
        assert response.status_code == 400, f"Баг ждали 400, получили {response.status_code}"
        assert response.json() == {"code": 400,"message": "Недостаточно данных для входа"}, f"Баг ждали code: 400, message: Недостаточно данных для входа, получили {response.json()}"    

    def test_non_existent_login(self, user_registration_fixture):
        password = user_registration_fixture["password"]
        payload = {
            "login": "dhgdsfdff",
            "password": password
        }
        response = requests.post(f"{BASE_URL}/api/v1/courier/login", data=payload)

        dada = response.json()
        assert response.status_code == 404, f"Баг ждали 404, получили {response.status_code}"
        assert response.json() == {"code": 404,"message": "Учетная запись не найдена"}, f"Баг ждали code: 404, message: Учетная запись не найдена, получили {response.json()}"    

    def test_non_existent_login(self, user_registration_fixture):
        login = user_registration_fixture["login"]
        payload = {
            "login": login,
            "password": "56546456456456"
        }
        response = requests.post(f"{BASE_URL}/api/v1/courier/login", data=payload)
        
        dada = response.json()
        assert response.status_code == 404, f"Баг ждали 404, получили {response.status_code}"
        assert response.json() == {"code": 404,"message": "Учетная запись не найдена"}, f"Баг ждали code: 404, message: Учетная запись не найдена, получили {response.json()}"    
        