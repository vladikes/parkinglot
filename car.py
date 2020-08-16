from dataclasses import dataclass, field
import random
import uuid

action_type_list = [
    'ENTER',
    'EXIT',
]

@dataclass
class Car:
    car_id: int
    utc_enter_timestamp: field(default_factory=dict)
    utc_exit_timestamp: field(default_factory=dict)
    action_type: field(default_factory=dict)

    def generate_car(self):
        return self.__class__(
            car_id=uuid.uuid4(),
            utc_enter_timestamp={
                'Entrance time': self.utc_enter_timestamp,
            },
            utc_exit_timestamp={
                'Exit time': self.utc_exit_timestamp,
            },
            action_type={'Type': random.choice(action_type_list)},
        )
