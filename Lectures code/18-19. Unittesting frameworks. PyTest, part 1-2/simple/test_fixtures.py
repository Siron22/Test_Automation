import sys
sys.path.append('/home/olytvynov/Projects/HL/hl_pyauto_17oct22')
print(sys.path)

from L19.car import Car

import pytest


# @pytest.fixture()
# def default_car():
#     car = Car('ABC9999', 'John Smith')
#     print(car.number_plate)
#     return car

def test_default_seat_numbers(default_car):
    print(default_car.number_of_seats)
    #raise ValueError
    assert default_car.number_of_seats == 5

def test_default_passengers(default_car):
    assert default_car.passengers == []

# @pytest.fixture()
# def random_value():
#     import random
#     return random.randint(0, 100)
#
# def test_random1(random_value):
#     print(f"random_value: {random_value}")
#
# def test_random2(random_value):
#     print(f"random_value: {random_value}")

def test_valid_number(car_with_valid_number):
    assert car_with_valid_number.validate_number_plate()

def test_invalid_numbers(invalid_cars):
    assert not invalid_cars.validate_number_plate()

def test_fixture_with_long_name(short_name):
    assert 3 == 3