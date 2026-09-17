from config import DB_CONFIG
from hh_api import collect_all_data
from db_manager import DBManager
from create_db import create_database  # <-- ДОБАВЬ ЭТУ СТРОКУ
from vacancy import Vacancy  # <-- И ЭТУ (если будешь использовать)
from file_manager import FileManager  # <-- И ЭТУ (если будешь использовать)


def main():
    # ========== ШАГ 0: Создаём базу данных (если её нет) ==========
    print("=== Проверка и создание базы данных ===")
    create_database()  # <-- ДОБАВЬ ЭТОТ ВЫЗОВ!
    print("База данных готова к работе.\n")

    # ========== ШАГ 1: Собираем данные с hh.ru ==========
    print("=== Сбор данных с hh.ru ===")
    employers, vacancies = collect_all_data()
    print(f"Получено работодателей: {len(employers)}")
    print(f"Получено вакансий: {len(vacancies)}\n")

    # ========== ШАГ 2: Работаем с БД ==========
    print("=== Работа с базой данных ===")
    db = DBManager(DB_CONFIG)

    # Создаём таблицы
    db.create_tables("schema.sql")
    print("Таблицы созданы.\n")

    # Заполняем данными
    db.insert_employers(employers)
    db.insert_vacancies(vacancies)
    print("Данные загружены в базу.\n")

    # ========== ШАГ 3: Тестируем методы DBManager ==========
    print("=== Тестирование методов DBManager ===\n")

    print("--- Компании и количество вакансий ---")
    companies = db.get_companies_and_vacancies_count()
    for row in companies:
        print(f"{row['employer_name']}: {row['vacancy_count']} вакансий")

    print(f"\n--- Средняя зарплата ---")
    avg = db.get_avg_salary()
    print(f"Средняя зарплата: {avg}")

    print(f"\n--- Вакансии с зарплатой выше средней ---")
    high_salary = db.get_vacancies_with_higher_salary()
    print(f"Найдено вакансий: {len(high_salary)}")
    for row in high_salary[:5]:  # Показываем первые 5
        print(f"  {row['vacancy_name']} — {row['salary_from']} - {row['salary_to']} {row['salary_currency']}")

    print(f"\n--- Вакансии с ключевым словом 'python' ---")
    python_vacs = db.get_vacancies_with_keyword("python")
    print(f"Найдено вакансий: {len(python_vacs)}")
    for row in python_vacs[:5]:  # Показываем первые 5
        print(f"  {row['vacancy_name']}")

    # Закрываем подключение
    db.close()
    print("\n=== Работа завершена ===")


if __name__ == "__main__":
    main()