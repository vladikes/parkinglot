import datetime

from car import Car
from parking_lot import ParkingLot


class TestParkingLot:
    @classmethod
    def setup_class(cls):
        cls.entrance_time = datetime.datetime.utcnow()
        cls.hours_added = datetime.timedelta(hours=8)
        cls.exit_time = cls.entrance_time + cls.hours_added

        cls.parking = ParkingLot()
        cls.parking.park_car(
            [
                Car(
                    action_type={'Type': 'ENTER'},
                    car_id=10,
                    utc_enter_timestamp=cls.entrance_time,
                    utc_exit_timestamp=cls.exit_time),
                Car(
                    action_type={'Type': 'EXIT'},
                    car_id=10,
                    utc_enter_timestamp=cls.entrance_time,
                    utc_exit_timestamp=cls.exit_time),
                Car(
                    action_type={'Type': 'ENTER'},
                    car_id=11,
                    utc_enter_timestamp=cls.entrance_time,
                    utc_exit_timestamp=cls.exit_time),
                Car(
                    action_type={'Type': 'EXIT'},
                    car_id=11,
                    utc_enter_timestamp=cls.entrance_time,
                    utc_exit_timestamp=cls.exit_time),
            ]
        )

    def test_park_car(self):

        vehicles = self.parking.get_vehicles()

        assert len(vehicles) == 4

    def test_parking_duration(self):
        vehicles = self.parking.get_vehicles()
        num_of_cars = self.parking.calculate_num_of_cars_duration(vehicles)

        assert num_of_cars['Number of cars'] == 4
        assert len(num_of_cars['list of cars']) == 4
