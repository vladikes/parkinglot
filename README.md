# Parking Lot

Simple parking lot application for testing purposes

## Installation

Run pip3 install -r requirements.txt (Python 3) to install the Pytest package.

## Usage
See main.py for an example
Run Pytest in the command line in order to execute tests

```python
from parking_lot import ParkingLot
from logentry import cars

def main():
    parking_lot = ParkingLot()
    cars_parked = parking_lot.calculate_num_of_cars_duration(cars)
    for i in cars_parked:
        print(i)

ParkingLot().calculate_num_of_cars_duration(vehicles) # returns a generator with vehicles parked over 2 hours including the cars themselves
```