from dataclasses import dataclass, field
import datetime
from car import Car
import random


@dataclass
class ParkingLot:
    lot = []

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

    def park_car(self, vehicles: list):
        if self.is_open():
            for vehicle in vehicles:
                self.lot.append(vehicle)

    @staticmethod
    def calculate_num_of_cars_duration(vehicles):
        list_of_cars = []

        for vehicle in vehicles:
            elapsed_time = vehicle.utc_exit_timestamp.hour - vehicle.utc_enter_timestamp.hour
            if elapsed_time > 2:
                list_of_cars.append(vehicle)

        return {'Number of cars': len(list_of_cars), 'list of cars': list_of_cars}

    def get_vehicles(self):
        return self.lot





