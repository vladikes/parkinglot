# Parking Lot

Simple parking lot application for testing purposes

## Installation

Run pip3 install -r requirements.txt (Python 3) to install the Pytest package.

## Usage
See main.py for an example

```python
from parking_lot import ParkingLot
from car import Car

car.Car(
           action_type={'Type': 'ENTER'},
           car_id=10,
           utc_enter_timestamp=entrance_time,
           utc_exit_timestamp=exit_time), # returns a car dataclass

ParkingLot().park_car([Car(...)]) # Accepts a list of Cars
ParkingLot().get_vehicles # returns vehicles parked in the lot
ParkingLot().calculate_num_of_cars_duration(vehicles) # returnsa dict with vehicles parked over 2 hours including the cars themselves
```