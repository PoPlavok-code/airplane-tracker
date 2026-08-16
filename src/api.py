from abc import ABC, abstractmethod
import requests
from typing import Dict, List, Any, Optional


class BaseAPI(ABC):
    """Абстрактный класс для работы с API"""

    @abstractmethod
    def get_data(self, country: str) -> Any:
        """Получить данные по стране"""
        pass

    @abstractmethod
    def validate_response(self, response: requests.Response) -> bool:
        """Проверить валидность ответа"""
        pass


class AeroplanesAPI(BaseAPI):
    """Класс для работы с API nominatim и opensky-network"""

    def __init__(self):
        self.nominatim_url = "https://nominatim.openstreetmap.org/search"
        self.opensky_url = "https://opensky-network.org/api/states/all"
        self.headers = {
            'User-Agent': 'AirplaneTracker/1.0 (your.email@example.com)'
        }

    def validate_response(self, response: requests.Response) -> bool:
        """Проверка статуса ответа"""
        return response.status_code == 200

    def get_country_bbox(self, country: str) -> Optional[List[float]]:
        """Получить bounding box страны через Nominatim API"""
        try:
            params = {
                'q': country,
                'format': 'json',
                'limit': 1
            }
            response = requests.get(self.nominatim_url, params=params, headers=self.headers)

            if self.validate_response(response):
                data = response.json()
                if data:
                    bbox = data[0]['boundingbox']
                    return [float(bbox[2]), float(bbox[0]), float(bbox[3]), float(bbox[1])]
            return None
        except Exception as e:
            print(f"Ошибка при получении координат: {e}")
            return None

    def get_data(self, country: str) -> Optional[Dict[str, Any]]:
        """Получить данные о самолетах над страной"""
        bbox = self.get_country_bbox(country)
        if not bbox:
            return None

        try:
            params = {
                'lamin': bbox[1],
                'lamax': bbox[3],
                'lomin': bbox[0],
                'lomax': bbox[2],
            }
            response = requests.get(self.opensky_url, params=params)

            if self.validate_response(response):
                data = response.json()
                return {
                    'country': country,
                    'bbox': bbox,
                    'states': data.get('states', [])
                }
            return None
        except Exception as e:
            print(f"Ошибка при получении данных о самолетах: {e}")
            return None

    def get_aeroplanes(self, country: str) -> List[List]:
        """Получить список самолетов над страной"""
        data = self.get_data(country)
        if data and data['states']:
            return data['states']
        return []
