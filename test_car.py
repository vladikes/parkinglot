import datetime
from car import Car
from dataclasses import asdict


class TestCar:
    @classmethod
    def setup_class(cls):
        cls.entrance_time = datetime.datetime.utcnow()
        cls.hours_added = datetime.timedelta(hours=8)
        cls.exit_time = cls.entrance_time + cls.hours_added

    @classmethod
    def teardown_class(cls):
        """ teardown any state that was previously setup with a call to
        setup_class.
        """

    def test_car_dataclass(self):
        car = Car(
            action_type={'Type': 'ENTER'},
            car_id=10,
            utc_enter_timestamp=self.entrance_time,
            utc_exit_timestamp=self.exit_time,
        )

        assert len(asdict(car)) == 4

    def test_car_generator(self):
        car = Car(
            action_type={'Type': 'ENTER'},
            car_id=10,
            utc_enter_timestamp=self.entrance_time,
            utc_exit_timestamp=self.exit_time,
        )

        generated_car = car.generate_car()

        assert len(asdict(generated_car)) == 4