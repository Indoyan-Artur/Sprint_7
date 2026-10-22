import requests
import pytest
from test_data.order_creation_data import ORDER_DATA


BASE_URL = "https://qa-scooter.education-services.ru"

class TestApiOrderCreation:
    @pytest.mark.parametrize(
        "colors",
        [
            ["GREY"],
            ["BLACK", "GREY"],
            [None]
        ],
        ids=["grey", "black_grey", "none"],
    )
    def test_order_creation(self, colors):
        payload = dict(ORDER_DATA)        # копия, оригинал не трогаем
        payload["color"] = colors         # подставляем цвет из параметра
        response = requests.post(f"{BASE_URL}/api/v1/orders", json=payload, timeout=10)
        assert response.status_code == 201, f"Баг: ждали 201, получили {response.status_code}"
        assert "track" in response.text, f"Баг: ждали track, получили: {response.text}"