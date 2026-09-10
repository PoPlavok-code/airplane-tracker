import os

print("Ищем кириллицу в системных переменных...\n")
found_issue = False

# Переменные, которые проверяет psycopg2
keys_to_check = ['USERPROFILE', 'APPDATA', 'LOCALAPPDATA', 'PATH', 'PGHOST', 'PGUSER', 'PGPASSWORD']

for key in keys_to_check:
    val = os.environ.get(key, '')
    if val:
        try:
            # Пробуем закодировать в чистый английский (ASCII)
            val.encode('ascii')
        except UnicodeEncodeError:
            print(f"❌ НАЙДЕНО: {key}")
            print(f"   Значение: {val}")
            print("   👆 В этом пути есть русские буквы или спецсимволы! Это ломает psycopg2.\n")
            found_issue = True

if not found_issue:
    print("✅ В основных переменных кириллицы не найдено.")
    print("Скорее всего, кириллица есть в пути установки самого PostgreSQL.")