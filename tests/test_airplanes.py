import pytest
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.models import Aeroplane
from src.storage import JSONStorage


class TestAeroplane:
    def test_create_aeroplane(self):
        plane = Aeroplane(
            icao24="123456",
            callsign="UAL123",
            origin_country="United States",
            velocity=250.5,
            altitude=10000.0,
            on_ground=False
        )
        assert plane.icao24 == "123456"
        assert plane.callsign == "UAL123"
        assert plane.velocity == 250.5
        assert plane.altitude == 10000.0
        assert plane.on_ground == False

    def test_validate_negative_velocity(self):
        with pytest.raises(ValueError):
            Aeroplane("123456", "TEST", "Test", -100, 1000, False)

    def test_validate_negative_altitude(self):
        with pytest.raises(ValueError):
            Aeroplane("123456", "TEST", "Test", 100, -1000, False)

    def test_compare_by_speed(self):
        plane1 = Aeroplane("111", "P1", "USA", 300, 10000, False)
        plane2 = Aeroplane("222", "P2", "USA", 250, 10000, False)
        result = plane1.compare_by_speed(plane2)
        assert "быстрее" in result

    def test_compare_by_altitude(self):
        plane1 = Aeroplane("111", "P1", "USA", 250, 12000, False)
        plane2 = Aeroplane("222", "P2", "USA", 250, 10000, False)
        result = plane1.compare_by_altitude(plane2)
        assert "выше" in result

    def test_str_representation(self):
        plane = Aeroplane("123", "TEST", "Russia", 200, 5000, False)
        str_repr = str(plane)
        assert "TEST" in str_repr
        assert "5000" in str_repr

    def test_equality(self):
        plane1 = Aeroplane("123", "P1", "USA", 250, 10000, False)
        plane2 = Aeroplane("123", "P2", "USA", 300, 12000, False)
        plane3 = Aeroplane("456", "P3", "USA", 250, 10000, False)
        assert plane1 == plane2
        assert plane1 != plane3

    def test_cast_to_object_list(self):
        states = [
            ["123456", "UAL123", "United States", 0, 0, -75.0, 40.0, 10000.0, False, 250.0],
            ["789012", "DLH456", "Germany", 0, 0, -74.0, 41.0, 12000.0, False, 280.0]
        ]
        planes = Aeroplane.cast_to_object_list(states)
        assert len(planes) == 2
        assert all(isinstance(p, Aeroplane) for p in planes)


class TestJSONStorage:
    @pytest.fixture
    def storage(self, tmp_path):
        filepath = tmp_path / "test_aeroplanes.json"
        return JSONStorage(str(filepath))

    def test_add_aeroplane(self, storage):
        plane = Aeroplane("123", "TEST", "USA", 250, 10000, False)
        assert storage.add_aeroplane(plane) == True

    def test_add_duplicate_aeroplane(self, storage):
        plane = Aeroplane("123", "TEST", "USA", 250, 10000, False)
        storage.add_aeroplane(plane)
        assert storage.add_aeroplane(plane) == False

    def test_get_aeroplanes(self, storage):
        plane1 = Aeroplane("123", "TEST1", "USA", 250, 10000, False)
        plane2 = Aeroplane("456", "TEST2", "Germany", 280, 12000, False)
        storage.add_aeroplane(plane1)
        storage.add_aeroplane(plane2)
        planes = storage.get_aeroplanes()
        assert len(planes) == 2

    def test_filter_by_country(self, storage):
        plane1 = Aeroplane("123", "TEST1", "United States", 250, 10000, False)
        plane2 = Aeroplane("456", "TEST2", "Germany", 280, 12000, False)
        storage.add_aeroplane(plane1)
        storage.add_aeroplane(plane2)
        filtered = storage.get_aeroplanes({'origin_country': 'United'})
        assert len(filtered) == 1

    def test_delete_aeroplane(self, storage):
        plane = Aeroplane("123", "TEST", "USA", 250, 10000, False)
        storage.add_aeroplane(plane)
        assert storage.delete_aeroplane("123") == True
        assert storage.delete_aeroplane("123") == False

    def test_clear_all(self, storage):
        plane1 = Aeroplane("123", "TEST1", "USA", 250, 10000, False)
        plane2 = Aeroplane("456", "TEST2", "USA", 280, 12000, False)
        storage.add_aeroplane(plane1)
        storage.add_aeroplane(plane2)
        assert storage.clear_all() == True
        assert len(storage.get_aeroplanes()) == 0