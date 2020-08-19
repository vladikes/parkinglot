from dataclasses import dataclass, field
import datetime


@dataclass
class ParkingLot:
    @staticmethod
    def is_open(
        opening_time='06:00:00',
        closing_time='23:30:00',
    ):
        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M:%S")

        if opening_time < current_time < closing_time:
            print(f'parking lot is open {current_time}')
            return True
        else:
            print(f'parking lot is closed {current_time}')
            return False

    @staticmethod
    def calculate_num_of_cars_duration(vehicles):
        for vehicle in vehicles:
            elapsed_time = datetime.datetime.strptime(
                vehicle['utc_exit_date'],
                '%Y-%m-%d %H:%M:%S.%f').hour - datetime.datetime.strptime(
                vehicle['utc_entry_date'],
                '%Y-%m-%d %H:%M:%S.%f'
            ).hour

            if elapsed_time > 2:

                yield {
                    'car_id': vehicle['_id'],
                    'action_type': vehicle['action type'],
                    'hours_parked': elapsed_time,
                    'entry_time': vehicle['utc_entry_date'],
                    'exit_time': vehicle['utc_exit_date'],
                }




