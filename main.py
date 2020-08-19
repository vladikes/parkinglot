from parking_lot import ParkingLot
from logentry import cars


def main():
    parking_lot = ParkingLot()
    cars_parked = parking_lot.calculate_num_of_cars_duration(cars)
    return list(cars_parked)


if __name__ == '__main__':
    print(main())

