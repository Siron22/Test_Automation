import sys
sys.path.append('/home/olytvynov/Projects/HL/hl_pyauto_17oct22')
print(sys.path)

from L18.car import Car, PassengersNumberExceededError

import pytest

def test_car_exception():
    car = Car('ABC1234', 'John Smith', number_of_seats=3)
    car.add_passenger('Passenger1')
    car.add_passenger('Passenger2')
    car.add_passenger('Passenger3')
    with pytest.raises(PassengersNumberExceededError) as exc_info:
        car.add_passenger('Passenger4')
    assert str(exc_info.value) == 'Expected 3 passengers in the car, but one more wants take a seat.'