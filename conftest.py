from faker import Faker
import requests
import pytest


fake = Faker(locale="ru_RU")
BASE_URL = "https://qa-scooter.education-services.ru"

@pytest.fixture()
def user_registration_fixture():
    login = fake.name()
    password = fake.password()
    name = fake.name()

    payload = {
        "login": login,
        "password": password,
        "firstName": name
    }
    response = requests.post(f"{BASE_URL}/api/v1/courier", data=payload)

    yield {
        "login": login,
        "password": password,
        "name": name,
        "response": response
    }


    
