from logentry import cars
from parking_lot import ParkingLot


class TestParkingLot:
    @classmethod
    def setup_class(cls):
        cls.parking_lot = ParkingLot()
        cls.cars_parked = cls.parking_lot.calculate_num_of_cars_duration(cars)

    def test_calculate_duration(self):
        assert len(list(self.cars_parked)) == 3

    def test_car_entries_exist(self):
        expected_keys = ['car_id', 'action_type', 'hours_parked', 'entry_time', 'exit_time']

        cars_entry = list(self.cars_parked)

        for car in cars_entry:
            assert set(expected_keys).issubset(car)