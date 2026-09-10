import requests
import time

EMPLOYER_IDS = [
    178921,  # Яндекс
    30377,  # Сбер
    1496,  # Тинькофф
    774,  # VK
    93766,  # Ozon
    15478,  # Wildberries
    118518,  # Авито
    26545,  # Ростелеком
    104512,  # МТС
    99359,  # X5 Retail Group
]


def get_employer(employer_id: int) -> dict:
    """Получить информацию о работодателе."""
    url = f"https://api.hh.ru/employers/{employer_id}"
    response = requests.get(url, headers={"User-Agent": "MyApp/1.0 (test@test.com)"})
    response.raise_for_status()
    return response.json()


def get_employer_vacancies(employer_id: int) -> list:
    """Получить все вакансии работодателя с пагинацией."""
    url = "https://api.hh.ru/vacancies"
    params = {"employer_id": employer_id, "per_page": 100, "page": 0}
    headers = {"User-Agent": "MyApp/1.0 (test@test.com)"}

    all_vacancies = []

    while True:
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()
        data = response.json()

        all_vacancies.extend(data.get("items", []))

        # Проверяем, есть ли следующая страница
        if params["page"] >= data.get("pages", 1) - 1:
            break

        params["page"] += 1
        time.sleep(0.5)  # чтобы не превысить лимит API

    return all_vacancies


def collect_all_data() -> tuple[list, list]:
    """Собрать данные по всем работодателям."""
    employers = []
    vacancies = []

    for emp_id in EMPLOYER_IDS:
        try:
            print(f"Получаем данные работодателя {emp_id}...")
            employer = get_employer(emp_id)
            employers.append(employer)

            emp_vacancies = get_employer_vacancies(emp_id)
            vacancies.extend(emp_vacancies)

            print(f"  Получено вакансий: {len(emp_vacancies)}")
            time.sleep(1)
        except Exception as e:
            print(f"  Ошибка с работодателем {emp_id}: {e}")

    return employers, vacancies