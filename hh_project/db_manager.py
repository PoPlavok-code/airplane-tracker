import psycopg2
from psycopg2.extras import RealDictCursor
from config import DB_CONFIG


class DBManager:
    def __init__(self):
        # Теперь, когда в pg_hba.conf стоит 'trust', подключение пройдет без ошибок кодировки
        self.conn = psycopg2.connect(
            host=DB_CONFIG["host"],
            port=DB_CONFIG["port"],
            dbname=DB_CONFIG["database"],
            user=DB_CONFIG["user"],
            password=DB_CONFIG["password"]
        )
        self.conn.autocommit = True

    def close(self):
        self.conn.close()

    def create_tables(self, schema_file: str):
        with open(schema_file, "r", encoding="utf-8") as f:
            sql = f.read()
        with self.conn.cursor() as cur:
            cur.execute(sql)
        print("✅ Таблицы созданы.")

    def insert_employers(self, employers: list):
        sql = """
            INSERT INTO employers (employer_id, employer_name, employer_area, employer_url)
            VALUES (%s, %s, %s, %s)
            ON CONFLICT (employer_id) DO NOTHING
        """
        with self.conn.cursor() as cur:
            for emp in employers:
                area_name = emp.get('area', {}).get('name', '') if emp.get('area') else ''
                cur.execute(sql, (emp['id'], emp['name'], area_name, emp.get('alternate_url', '')))
        print(f"✅ Вставлено {len(employers)} работодателей")

    def insert_vacancies(self, vacancies: list):
        sql = """
            INSERT INTO vacancies (vacancy_id, vacancy_name, employer_id, 
                                   salary_from, salary_to, salary_currency, 
                                   vacancy_url, published_at)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            ON CONFLICT (vacancy_id) DO NOTHING
        """
        with self.conn.cursor() as cur:
            for vac in vacancies:
                salary = vac.get("salary") or {}
                cur.execute(sql, (
                    vac['id'], vac['name'], vac['employer']['id'],
                    salary.get('from'), salary.get('to'), salary.get('currency', ''),
                    vac.get('alternate_url', ''), vac.get('published_at', '')
                ))
        print(f"✅ Вставлено {len(vacancies)} вакансий")

    def get_companies_and_vacancies_count(self):
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

    def get_all_vacancies(self):
        sql = """
            SELECT e.employer_name, v.vacancy_name, 
                   v.salary_from, v.salary_to, v.salary_currency, v.vacancy_url
            FROM vacancies v
            JOIN employers e ON v.employer_id = e.employer_id
        """
        with self.conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute(sql)
            return cur.fetchall()

    def get_avg_salary(self):
        sql = """
            SELECT AVG(
                CASE 
                    WHEN salary_from IS NOT NULL AND salary_to IS NOT NULL THEN (salary_from + salary_to) / 2.0
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
            return round(float(result["avg_salary"]), 2) if result["avg_salary"] else 0.0

    def get_vacancies_with_higher_salary(self):
        avg = self.get_avg_salary()
        if avg == 0:
            return []
        sql = """
            SELECT e.employer_name, v.vacancy_name, v.salary_from, v.salary_to, v.salary_currency, v.vacancy_url
            FROM vacancies v
            JOIN employers e ON v.employer_id = e.employer_id
            WHERE (
                CASE 
                    WHEN salary_from IS NOT NULL AND salary_to IS NOT NULL THEN (salary_from + salary_to) / 2.0
                    WHEN salary_from IS NOT NULL THEN salary_from
                    WHEN salary_to IS NOT NULL THEN salary_to
                    ELSE 0
                END
            ) > %s
        """
        with self.conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute(sql, (avg,))
            return cur.fetchall()

    def get_vacancies_with_keyword(self, keyword: str):
        sql = """
            SELECT e.employer_name, v.vacancy_name, v.salary_from, v.salary_to, v.salary_currency, v.vacancy_url
            FROM vacancies v
            JOIN employers e ON v.employer_id = e.employer_id
            WHERE v.vacancy_name ILIKE %s
        """
        with self.conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute(sql, (f"%{keyword}%",))
            return cur.fetchall()