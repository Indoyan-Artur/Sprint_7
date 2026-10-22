Sprint 7 — API-тесты курьерского сервиса
Автотесты API курьерского сервиса: Python + pytest + requests + Allure.
Покрыты 4 ручки: создание курьера, логин курьера, создание заказа, список заказов.
Структура
Sprint_7/
├── config.py    # BASE_URL, URL ручек, ожидаемые HTTP-коды
├── conftest.py  # фикстуры: courier_payload, registered_courier, courier_id
├── requirements.txt
└── test/
    ├── test_courier_creation.py          # 1. Создание курьера
    ├── test_courier_login.py             # 2. Логин курьера
    ├── test_order_creation.py            # 3. Создание заказа (цвет: BLACK / GREY / оба / нет)
    └── test_obtaining_list_of_orders.py  # 4. Список заказов

Запуск
pip install -r requirements.txt
export BASE_URL=http://ваш-адрес:порт   # дефолт http://localhost:8080
pytest test/ -v

Allure-отчёт
pytest test/ --alluredir=./allure-results
allure serve ./allure-results



