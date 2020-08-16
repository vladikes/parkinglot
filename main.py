import datetime
from car import Car
from parking_lot import ParkingLot


def main():
    entrance_time = datetime.datetime.utcnow()
    hours_added = datetime.timedelta(hours=8)
    exit_time = entrance_time + hours_added

    parking = ParkingLot()

    parking.park_car(
        [
            Car(
                action_type={'Type': 'ENTER'},
                car_id=10,
                utc_enter_timestamp=entrance_time,
                utc_exit_timestamp=exit_time),
            Car(
                action_type={'Type': 'EXIT'},
                car_id=10,
                utc_enter_timestamp=entrance_time,
                utc_exit_timestamp=exit_time),
            Car(
                action_type={'Type': 'ENTER'},
                car_id=11,
                utc_enter_timestamp=entrance_time,
                utc_exit_timestamp=exit_time),
            Car(
                action_type={'Type': 'EXIT'},
                car_id=11,
                utc_enter_timestamp=entrance_time,
                utc_exit_timestamp=exit_time),
        ]
    )
    vehicles = parking.get_vehicles()

    return parking.calculate_num_of_cars_duration(vehicles)


if __name__ == '__main__':
    print(main())