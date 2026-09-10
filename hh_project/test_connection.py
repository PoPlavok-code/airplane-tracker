import psycopg2
import os

print("Проверка подключения к PostgreSQL...")
print(f"Путь к проекту: {os.getcwd()}")

# Попробуем разные способы подключения
configs = [
    {
        "name": "Способ 1: Через параметры",
        "params": {
            "host": "127.0.0.1",
            "port": 5432,
            "database": "hh_vacancies",
            "user": "postgres",
            "password": "200303Nh"
        }
    },
    {
        "name": "Способ 2: Через DSN строку",
        "dsn": "postgresql://postgres:200303Nh@127.0.0.1:5432/hh_vacancies"
    }
]

for config in configs:
    print(f"\n{config['name']}")
    try:
        if "params" in config:
            conn = psycopg2.connect(**config["params"])
        else:
            conn = psycopg2.connect(config["dsn"])

        cursor = conn.cursor()
        cursor.execute("SELECT version();")
        version = cursor.fetchone()
        print(f"  ✅ УСПЕХ! PostgreSQL: {version[0][:50]}...")
        cursor.close()
        conn.close()
        break
    except Exception as e:
        print(f"  ❌ Ошибка: {type(e).__name__}: {e}")