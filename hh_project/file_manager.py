import json
from typing import List, Dict, Any


class FileManager:
    """
    Класс для работы с файлами (сохранение и загрузка данных в формате JSON).

    Methods:
        save_to_json: Сохраняет данные в JSON-файл.
        load_from_json: Загружает данные из JSON-файла.
    """

    @staticmethod
    def save_to_json(data: List[Dict[str, Any]], filename: str) -> None:
        """
        Сохраняет список словарей в JSON-файл.

        Args:
            data (List[Dict[str, Any]]): Данные для сохранения.
            filename (str): Имя файла.
        """
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print(f"Данные сохранены в файл {filename}")

    @staticmethod
    def load_from_json(filename: str) -> List[Dict[str, Any]]:
        """
        Загружает данные из JSON-файла.

        Args:
            filename (str): Имя файла.

        Returns:
            List[Dict[str, Any]]: Загруженные данные.
        """
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
        print(f"Данные загружены из файла {filename}")
        return data