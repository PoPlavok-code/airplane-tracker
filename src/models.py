from typing import Optional, List
from dataclasses import dataclass


@dataclass
class Aeroplane:
    """Класс для представления самолета"""

    icao24: str
    callsign: str
    origin_country: str
    velocity: float
    altitude: float
    on_ground: bool
    longitude: Optional[float] = None
    latitude: Optional[float] = None

    def __post_init__(self):
        """Валидация данных после инициализации"""
        self._validate_data()

    def _validate_data(self):
        """Валидация атрибутов"""
        if not isinstance(self.icao24, str) or not self.icao24:
            raise ValueError("ICAO24 должен быть непустой строкой")

        if not isinstance(self.origin_country, str):
            raise ValueError("Страна должна быть строкой")

        if self.velocity < 0:
            raise ValueError("Скорость не может быть отрицательной")

        if self.altitude < 0:
            raise ValueError("Высота не может быть отрицательной")

    def __str__(self):
        """Строковое представление"""
        status = "на земле" if self.on_ground else f"на высоте {self.altitude:.2f}м"
        return (f"Самолет {self.callsign or 'N/A'} ({self.icao24}): "
                f"страна {self.origin_country}, скорость {self.velocity:.2f} м/с, {status}")

    def __repr__(self):
        return f"Aeroplane('{self.icao24}', '{self.callsign}', '{self.origin_country}', {self.velocity}, {self.altitude})"

    def __eq__(self, other):
        """Сравнение по ICAO24"""
        if not isinstance(other, Aeroplane):
            return False
        return self.icao24 == other.icao24

    def __lt__(self, other):
        """Сравнение для сортировки по высоте"""
        if not isinstance(other, Aeroplane):
            return NotImplemented
        return self.altitude < other.altitude

    def __gt__(self, other):
        """Сравнение для сортировки по высоте"""
        if not isinstance(other, Aeroplane):
            return NotImplemented
        return self.altitude > other.altitude

    def compare_by_speed(self, other: 'Aeroplane') -> str:
        """Сравнение по скорости"""
        if not isinstance(other, Aeroplane):
            raise TypeError("Можно сравнивать только с Aeroplane")

        if self.velocity > other.velocity:
            return f"{self.callsign} быстрее {other.callsign}"
        elif self.velocity < other.velocity:
            return f"{self.callsign} медленнее {other.callsign}"
        else:
            return f"{self.callsign} и {other.callsign} имеют одинаковую скорость"

    def compare_by_altitude(self, other: 'Aeroplane') -> str:
        """Сравнение по высоте"""
        if not isinstance(other, Aeroplane):
            raise TypeError("Можно сравнивать только с Aeroplane")

        if self.altitude > other.altitude:
            return f"{self.callsign} летит выше {other.callsign}"
        elif self.altitude < other.altitude:
            return f"{self.callsign} летит ниже {other.callsign}"
        else:
            return f"{self.callsign} и {other.callsign} летят на одинаковой высоте"

    @classmethod
    def cast_to_object_list(cls, states: List[List]) -> List['Aeroplane']:
        """Преобразовать список списков в список объектов Aeroplane"""
        aeroplanes = []
        for state in states:
            try:
                if len(state) >= 10:
                    aeroplane = cls(
                        icao24=state[0] or '',
                        callsign=state[1] or '',
                        origin_country=state[2] or 'Unknown',
                        velocity=state[9] if state[9] is not None else 0.0,
                        altitude=state[7] if state[7] is not None else 0.0,
                        on_ground=state[8] if state[8] is not None else False,
                        longitude=state[5],
                        latitude=state[6]
                    )
                    aeroplanes.append(aeroplane)
            except (IndexError, ValueError) as e:
                print(f"Ошибка при создании самолета: {e}")
                continue
        return aeroplanes