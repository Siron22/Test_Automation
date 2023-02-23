import sys
sys.path.append('/home/olytvynov/Projects/HL/hl_pyauto_17oct22')
print(sys.path)

from L19.car import Car

import pytest


# @pytest.fixture()
# def default_car():
#     car = Car('ABC1234', 'John Smith')
#     return car

@pytest.fixture(scope='function')
def default_car():
    car = Car('ABC1234', 'John Smith')
    print(car.number_plate)
    #car.start_loading()
    yield car
    car.close_connection()

# @pytest.fixture(scope='function')
# def default_car(request):
#     car = Car('ABC1234', 'John Smith')
#     print(car.number_plate)
#
#     def close_connection():
#         car.close_connection()
#     request.addfinalizer(close_connection)
#
#     return car


@pytest.fixture()
def configurable_car():
    def config_car(number, owner):
        return Car(number, owner)
    return config_car

# @pytest.fixture()
# def start_service():
#     start_service_()
#     yield
#     stop_service_()

@pytest.fixture()
def valid_number():
    return "ABC1234"

@pytest.fixture()
def default_owner():
    return "John Owner"

@pytest.fixture()
def car_with_valid_number(valid_number, default_owner):
    return Car(valid_number, default_owner)

# @pytest.fixture()
# def client(service):
#     pass
#
# @pytest.fixture()
# def service():
#     pass

@pytest.fixture(params=['A', '1111', 'dcd24'])
def invalid_cars(request):
    number = request.param
    return Car(number, 'John')

@pytest.fixture(autouse=True, scope='session')
def create_environment():
    print("Create environment")

@pytest.fixture(name='short_name')
def fixture_with_looooooooooooooooooooooooooooong_name():
    print("fixture_with_looooooooooooooooooooooooooooong_name")


@pytest.fixture(scope='session')
def initial_car_data(tmp_path_factory):
    print(tmp_path_factory.getbasetemp())
    file_path = tmp_path_factory.mktemp('own_temp', numbered=False) / 'initial_cars_data.txt'
    with open(file_path, 'w') as f:
        f.write('QWE1234 Jack\nASD5423 Olga Smith')
    return file_path
