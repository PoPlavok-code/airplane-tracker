from typing import List
from .api import AeroplanesAPI
from .models import Aeroplane
from .storage import JSONStorage


def print_menu():
    print("\n" + "=" * 50)
    print("СИСТЕМА ОТСЛЕЖИВАНИЯ САМОЛЕТОВ")
    print("=" * 50)
    print("1. Получить информацию о самолетах над страной")
    print("2. Получить топ N самолетов по высоте")
    print("3. Найти самолеты по стране регистрации")
    print("4. Найти самолеты в диапазоне высот")
    print("5. Сохранить все самолеты в файл")
    print("6. Загрузить самолеты из файла")
    print("7. Очистить хранилище")
    print("0. Выход")
    print("=" * 50)


def get_aeroplanes_by_country(api: AeroplanesAPI) -> List[Aeroplane]:
    country = input("Введите название страны (на английском): ").strip()
    if not country:
        print("Название страны не может быть пустым!")
        return []

    print(f"\nЗапрос данных о самолетах над {country}...")
    states = api.get_aeroplanes(country)

    if not states:
        print(f"Не удалось получить данные или самолеты не найдены над {country}")
        return []

    aeroplanes = Aeroplane.cast_to_object_list(states)
    print(f"\nНайдено самолетов: {len(aeroplanes)}")
    return aeroplanes


def get_top_n_by_altitude(aeroplanes: List[Aeroplane]):
    if not aeroplanes:
        print("Список самолетов пуст!")
        return

    try:
        n = int(input("Введите количество самолетов для топ-N: "))
        if n <= 0:
            print("Число должно быть положительным!")
            return
    except ValueError:
        print("Неверный формат числа!")
        return

    sorted_aeroplanes = sorted(aeroplanes, key=lambda x: x.altitude, reverse=True)
    top_aeroplanes = sorted_aeroplanes[:n]

    print(f"\nТОП-{n} самолетов по высоте:")
    print("-" * 70)
    for i, aeroplane in enumerate(top_aeroplanes, 1):
        print(f"{i}. {aeroplane}")


def filter_by_country(aeroplanes: List[Aeroplane]):
    if not aeroplanes:
        print("Список самолетов пуст!")
        return

    country = input("Введите страну регистрации для фильтрации: ").strip()
    if not country:
        print("Название страны не может быть пустым!")
        return

    filtered = [a for a in aeroplanes if country.lower() in a.origin_country.lower()]

    if not filtered:
        print(f"Самолеты из {country} не найдены")
        return

    print(f"\nНайдено {len(filtered)} самолетов из {country}:")
    print("-" * 70)
    for aeroplane in filtered:
        print(aeroplane)


def filter_by_altitude_range(aeroplanes: List[Aeroplane]):
    if not aeroplanes:
        print("Список самолетов пуст!")
        return

    try:
        range_input = input("Введите диапазон высот (например: 10000 15000): ").strip()
        min_alt, max_alt = map(float, range_input.split())

        if min_alt < 0 or max_alt < 0:
            print("Высота не может быть отрицательной!")
            return

        filtered = [a for a in aeroplanes if min_alt <= a.altitude <= max_alt]

        if not filtered:
            print(f"Самолеты в диапазоне {min_alt}-{max_alt}м не найдены")
            return

        print(f"\nНайдено {len(filtered)} самолетов в диапазоне {min_alt}-{max_alt}м:")
        print("-" * 70)
        for aeroplane in filtered:
            print(aeroplane)

    except ValueError:
        print("Неверный формат диапазона! Используйте формат: min max")


def save_to_file(aeroplanes: List[Aeroplane], storage: JSONStorage):
    if not aeroplanes:
        print("Нечего сохранять!")
        return

    count = 0
    for aeroplane in aeroplanes:
        if storage.add_aeroplane(aeroplane):
            count += 1

    print(f"Сохранено {count} самолетов (пропущено дубликатов: {len(aeroplanes) - count})")


def load_from_file(storage: JSONStorage) -> List[Aeroplane]:
    aeroplanes = storage.get_aeroplanes()

    if not aeroplanes:
        print("Файл пуст или не найден")
        return []

    print(f"\nЗагружено {len(aeroplanes)} самолетов из файла:")
    print("-" * 70)
    for aeroplane in aeroplanes:
        print(aeroplane)

    return aeroplanes


def user_interaction():
    api = AeroplanesAPI()
    storage = JSONStorage()
    current_aeroplanes: List[Aeroplane] = []

    while True:
        print_menu()
        choice = input("Выберите действие: ").strip()

        if choice == '1':
            current_aeroplanes = get_aeroplanes_by_country(api)
        elif choice == '2':
            get_top_n_by_altitude(current_aeroplanes)
        elif choice == '3':
            filter_by_country(current_aeroplanes)
        elif choice == '4':
            filter_by_altitude_range(current_aeroplanes)
        elif choice == '5':
            save_to_file(current_aeroplanes, storage)
        elif choice == '6':
            current_aeroplanes = load_from_file(storage)
        elif choice == '7':
            if input("Вы уверены? (y/n): ").lower() == 'y':
                if storage.clear_all():
                    print("Хранилище очищено")
        elif choice == '0':
            print("До свидания!")
            break
        else:
            print("Неверный выбор! Попробуйте снова.")


if __name__ == "__main__":
    user_interaction()