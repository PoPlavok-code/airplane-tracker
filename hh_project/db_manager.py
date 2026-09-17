import psycopg2
from psycopg2.extras import RealDictCursor
from typing import List, Dict, Optional


class DBManager:
    """
    Класс для управления подключением к базе данных PostgreSQL
    и выполнения операций с таблицами работодателей и вакансий.

    Этот класс предоставляет методы для:
    - Создания таблиц в базе данных
    - Вставки данных о работодателях и вакансиях
    - Получения статистики по вакансиям и зарплатам
    - Поиска вакансий по ключевым словам

    Attributes:
        params (dict): Параметры подключения к базе данных.
        conn: Объект подключения к базе данных psycopg2.

    Example:
        >>> db = DBManager(DB_CONFIG)
        >>> db.create_tables('schema.sql')
        >>> companies = db.get_companies_and_vacancies_count()
    """

    def __init__(self, params: dict):
        """
        Инициализирует подключение к базе данных.

        Args:
            params (dict): Параметры подключения (host, port, database, user, password).
        """
        self.params = params
        self.conn = psycopg2.connect(**self.params)
        self.conn.autocommit = True

    def close(self):
        """Закрывает подключение к базе данных."""
        self.conn.close()

    def create_tables(self, schema_file: str):
        """
        Создаёт таблицы в базе данных из SQL-файла.

        Args:
            schema_file (str): Путь к SQL-файлу со схемой таблиц.
        """
        with open(schema_file, "r", encoding="utf-8") as f:
            sql = f.read()
        with self.conn.cursor() as cur:
            cur.execute(sql)
        print("Таблицы созданы успешно.")

    def insert_employers(self, employers: list):
        """
        Вставляет данные о работодателях в таблицу employers.

        Args:
            employers (list): Список словарей с данными о работодателях.
        """
        sql = """
            INSERT INTO employers (employer_id, employer_name, employer_area, employer_url)
            VALUES (%s, %s, %s, %s)
            ON CONFLICT (employer_id) DO NOTHING
        """
        with self.conn.cursor() as cur:
            for emp in employers:
                cur.execute(sql, (
                    emp["id"],
                    emp["name"],
                    emp.get("area", {}).get("name"),
                    emp.get("alternate_url")
                ))
        print(f"Работодатели добавлены: {len(employers)}")

    def insert_vacancies(self, vacancies: list):
        """
        Вставляет данные о вакансиях в таблицу vacancies.

        Args:
            vacancies (list): Список словарей с данными о вакансиях.
        """
        sql = """
            INSERT INTO vacancies (vacancy_id, vacancy_name, employer_id, 
                                   salary_from, salary_to, salary_currency, 
                                   vacancy_url, published_at)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            ON CONFLICT (vacancy_id) DO NOTHING
        """
        with self.conn.cursor() as cur:
            for vac in vacancies:
                salary = vac.get("salary")
                cur.execute(sql, (
                    vac["id"],
                    vac["name"],
                    vac["employer"]["id"],
                    salary.get("from") if salary else None,
                    salary.get("to") if salary else None,
                    salary.get("currency") if salary else None,
                    vac.get("alternate_url"),
                    vac.get("published_at")
                ))
        print(f"Вакансии добавлены: {len(vacancies)}")

    def get_companies_and_vacancies_count(self) -> List[Dict]:
        """
        Получает список всех компаний и количество вакансий у каждой компании.

        Returns:
            List[Dict]: Список словарей с полями employer_name и vacancy_count.
        """
        sql = """
            SELECT e.employer_name, COUNT(v.vacancy_id) as vacancy_count
            FROM employers e
            LEFT JOIN vacancies v ON e.employer_id = v.employer_id
            GROUP BY e.employer_name
            ORDER BY vacancy_count DESC
        """
        with self.conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute(sql)
            return cur.fetchall()

    def get_all_vacancies(self) -> List[Dict]:
        """
        Получает список всех вакансий с указанием названия компании,
        названия вакансии, зарплаты и ссылки на вакансию.

        Returns:
            List[Dict]: Список словарей с данными о вакансиях.
        """
        sql = """
            SELECT e.employer_name, v.vacancy_name, 
                   v.salary_from, v.salary_to, v.salary_currency,
                   v.vacancy_url
            FROM vacancies v
            JOIN employers e ON v.employer_id = e.employer_id
            ORDER BY v.vacancy_id
        """
        with self.conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute(sql)
            return cur.fetchall()

    def get_avg_salary(self) -> float:
        """
        Получает среднюю зарплату по всем вакансиям.

        Returns:
            float: Средняя зарплата (округлённая до 2 знаков).
        """
        sql = """
            SELECT AVG(
                CASE 
                    WHEN salary_from IS NOT NULL AND salary_to IS NOT NULL 
                        THEN (salary_from + salary_to) / 2.0
                    WHEN salary_from IS NOT NULL THEN salary_from
                    WHEN salary_to IS NOT NULL THEN salary_to
                    ELSE NULL
                END
            ) as avg_salary
            FROM vacancies
        """
        with self.conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute(sql)
            result = cur.fetchone()
            return round(result["avg_salary"], 2) if result["avg_salary"] else 0

    def get_vacancies_with_higher_salary(self) -> List[Dict]:
        """
        Получает список всех вакансий, у которых зарплата выше средней.

        Returns:
            List[Dict]: Список вакансий с зарплатой выше средней.
        """
        avg = self.get_avg_salary()
        if avg == 0:
            return []

        sql = """
            SELECT e.employer_name, v.vacancy_name, 
                   v.salary_from, v.salary_to, v.salary_currency,
                   v.vacancy_url
            FROM vacancies v
            JOIN employers e ON v.employer_id = e.employer_id
            WHERE (
                CASE 
                    WHEN salary_from IS NOT NULL AND salary_to IS NOT NULL 
                        THEN (salary_from + salary_to) / 2.0
                    WHEN salary_from IS NOT NULL THEN salary_from
                    WHEN salary_to IS NOT NULL THEN salary_to
                    ELSE 0
                END
            ) > %s
            ORDER BY salary_from DESC
        """
        with self.conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute(sql, (avg,))
            return cur.fetchall()

    def get_vacancies_with_keyword(self, keyword: str) -> List[Dict]:
        """
        Получает список всех вакансий, в названии которых содержится ключевое слово.

        Args:
            keyword (str): Ключевое слово для поиска (например, 'python').

        Returns:
            List[Dict]: Список найденных вакансий.
        """
        sql = """
            SELECT e.employer_name, v.vacancy_name, 
                   v.salary_from, v.salary_to, v.salary_currency,
                   v.vacancy_url
            FROM vacancies v
            JOIN employers e ON v.employer_id = e.employer_id
            WHERE v.vacancy_name ILIKE %s
            ORDER BY v.vacancy_id
        """
        with self.conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute(sql, (f"%{keyword}%",))
            return cur.fetchall()
