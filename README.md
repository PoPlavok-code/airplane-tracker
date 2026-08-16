
# Airplane Tracker

Курсовая работа: Система отслеживания самолетов в реальном времени.

## Описание

Проект для интеграции с внешними API:
- **Nominatim API** (OpenStreetMap) - получение географических координат стран
- **OpenSky Network API** - получение информации о самолетах

## Функционал

- ✅ Получение информации о самолетах над выбранной страной
- ✅ Фильтрация по стране регистрации
- ✅ Фильтрация по диапазону высот
- ✅ Сортировка по высоте (ТОП-N)
- ✅ Сохранение данных в JSON файл
- ✅ Сравнение самолетов по скорости и высоте

## Установка
bash
pip install -r requirements.txt

## Использование

```bash
python -m src.main
Структура проекта
airplane-tracker/
├── src/
│   ├── api.py          # Работа с внешними API
│   ├── models.py       # Класс Aeroplane
│   ├── storage.py      # Работа с JSON файлами
│   └── main.py         # Взаимодействие с пользователем
├── tests/
│   └── test_airplanes.py
├── data/
├── requirements.txt
└── README.md

Принципы SOLID
Проект реализует принципы:
Single Responsibility - каждый класс отвечает за одну задачу
Open/Closed - абстрактные классы позволяют расширять функциональность
Liskov Substitution - наследники заменяют родительские классы
Тестирование
pytest tests/ -v
Автор
Никита Назаров
Лицензия
MIT

---

## 🚀 Шаг 3: Запушь README

После обновления README выполни:

```bash
git add README.md
git commit -m "docs: update README with project description"
git push origin main