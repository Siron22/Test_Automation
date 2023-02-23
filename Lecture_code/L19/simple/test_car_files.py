import sys

sys.path.append('/home/olytvynov/Projects/HL/hl_pyauto_17oct22')
print(sys.path)

from L19.car import Car

import pytest
import os

def test_save_car_info(tmp_path):
    file_path = os.path.join(tmp_path, 'car_data.txt')
    print(file_path)
    number_plate = 'RTY5478'
    owner = 'Jack Edwards'
    car = Car(number_plate, 'Jack Edwards')
    car.save_car_info(file_path)

    with open(file_path, 'r') as f:
        observed_car_data = f.read()

    expected_car_data = f"CAR {number_plate}\nOWNER: {owner}"
    assert observed_car_data == expected_car_data


def test_session_directory_1(initial_car_data):
    print(initial_car_data)
    with open(initial_car_data) as f:
        print(f.read())


def test_session_directory_2(initial_car_data):
    print(initial_car_data)
    with open(initial_car_data) as f:
        print(f.read())


def test_simple_with_car():
    number_letter_part = "AOT"
    number_digits_part = 3462
    number_plate = f"{number_letter_part}{number_digits_part}"
    owner = 'Andrew Smith'
    seating_number = 54
    car = Car(number_plate, owner, number_of_seats=seating_number)
    car.add_passenger('Another Andrew')
    assert 'Another Andrew2' in car.passengers

