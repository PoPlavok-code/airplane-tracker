from abc import ABC, abstractmethod
import json
import os
from typing import List, Optional, Dict, Any
from .models import Aeroplane


class BaseStorage(ABC):
    """Абстрактный класс для хранения данных"""

    @abstractmethod
    def add_aeroplane(self, aeroplane: Aeroplane) -> bool:
        pass

    @abstractmethod
    def get_aeroplanes(self, filter_criteria: Optional[Dict] = None) -> List[Aeroplane]:
        pass

    @abstractmethod
    def delete_aeroplane(self, icao24: str) -> bool:
        pass

    @abstractmethod
    def clear_all(self) -> bool:
        pass


class JSONStorage(BaseStorage):
    """Класс для сохранения данных в JSON файл"""

    def __init__(self, filepath: str = "data/aeroplanes.json"):
        self.filepath = filepath
        self._ensure_directory()
        self._ensure_file()

    def _ensure_directory(self):
        directory = os.path.dirname(self.filepath)
        if directory and not os.path.exists(directory):
            os.makedirs(directory)

    def _ensure_file(self):
        if not os.path.exists(self.filepath):
            with open(self.filepath, 'w', encoding='utf-8') as f:
                json.dump([], f, ensure_ascii=False, indent=2)

    def _read_data(self) -> List[Dict[str, Any]]:
        try:
            with open(self.filepath, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            return []

    def _write_data(self, data: List[Dict[str, Any]]):
        with open(self.filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def _aeroplane_to_dict(self, aeroplane: Aeroplane) -> Dict[str, Any]:
        return {
            'icao24': aeroplane.icao24,
            'callsign': aeroplane.callsign,
            'origin_country': aeroplane.origin_country,
            'velocity': aeroplane.velocity,
            'altitude': aeroplane.altitude,
            'on_ground': aeroplane.on_ground,
            'longitude': aeroplane.longitude,
            'latitude': aeroplane.latitude
        }

    def _dict_to_aeroplane(self, data: Dict[str, Any]) -> Aeroplane:
        return Aeroplane(
            icao24=data['icao24'],
            callsign=data['callsign'],
            origin_country=data['origin_country'],
            velocity=data['velocity'],
            altitude=data['altitude'],
            on_ground=data['on_ground'],
            longitude=data.get('longitude'),
            latitude=data.get('latitude')
        )

    def add_aeroplane(self, aeroplane: Aeroplane) -> bool:
        try:
            data = self._read_data()
            for item in data:
                if item['icao24'] == aeroplane.icao24:
                    return False
            data.append(self._aeroplane_to_dict(aeroplane))
            self._write_data(data)
            return True
        except Exception as e:
            print(f"Ошибка при добавлении самолета: {e}")
            return False

    def get_aeroplanes(self, filter_criteria: Optional[Dict] = None) -> List[Aeroplane]:
        try:
            data = self._read_data()
            aeroplanes = [self._dict_to_aeroplane(item) for item in data]

            if filter_criteria:
                if 'origin_country' in filter_criteria:
                    country = filter_criteria['origin_country'].lower()
                    aeroplanes = [a for a in aeroplanes if country in a.origin_country.lower()]

                if 'min_altitude' in filter_criteria:
                    aeroplanes = [a for a in aeroplanes if a.altitude >= filter_criteria['min_altitude']]

                if 'max_altitude' in filter_criteria:
                    aeroplanes = [a for a in aeroplanes if a.altitude <= filter_criteria['max_altitude']]

                if 'min_velocity' in filter_criteria:
                    aeroplanes = [a for a in aeroplanes if a.velocity >= filter_criteria['min_velocity']]

            return aeroplanes
        except Exception as e:
            print(f"Ошибка при получении самолетов: {e}")
            return []

    def delete_aeroplane(self, icao24: str) -> bool:
        try:
            data = self._read_data()
            initial_length = len(data)
            data = [item for item in data if item['icao24'] != icao24]
            if len(data) < initial_length:
                self._write_data(data)
                return True
            return False
        except Exception as e:
            print(f"Ошибка при удалении самолета: {e}")
            return False

    def clear_all(self) -> bool:
        try:
            self._write_data([])
            return True
        except Exception as e:
            print(f"Ошибка при очистке данных: {e}")
            return False