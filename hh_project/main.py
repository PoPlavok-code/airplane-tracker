import json
from db_manager import DBManager


def main():
    print("=== Загрузка данных из локального файла ===")

    with open("mock_data.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    employers = data["employers"]
    vacancies = data["vacancies"]

    print(f"Загружено работодателей: {len(employers)}")
    print(f"Загружено вакансий: {len(vacancies)}")

    print("\n=== Работа с БД ===")
    db = DBManager()  # ← без параметров!

    db.create_tables("schema.sql")

    db.insert_employers(employers)
    db.insert_vacancies(vacancies)
    print("Данные загружены в БД!")

    # Тесты методов
    print("\n--- 1. Компании и количество вакансий ---")
    for row in db.get_companies_and_vacancies_count():
        print(f"  {row['employer_name']}: {row['vacancy_count']}")

    print("\n--- 2. Средняя зарплата ---")
    avg = db.get_avg_salary()
    print(f"  Средняя: {avg} руб.")

    print("\n--- 3. Вакансии с ЗП выше средней ---")
    for row in db.get_vacancies_with_higher_salary():
        print(f"  {row['vacancy_name']}")

    print("\n--- 4. Вакансии с 'Python' ---")
    for row in db.get_vacancies_with_keyword("Python"):
        print(f"  {row['vacancy_name']}")

    db.close()
    print("\n✅ Готово!")


if __name__ == "__main__":
    main()