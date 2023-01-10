import sys
sys.path.append('/home/olytvynov/Projects/HL/hl_pyauto_17oct22')
print(sys.path)

from L19.car import Car

import pytest

@pytest.mark.parametrize('number,owner', [(), ()])
class TestCar:

    def setup_class(self):

        print("Setup class")

    def setup_method(self):
        self.car = Car('1111', '11111')
        print("In setup method")

    #@pytest.mark.xfail(reason="JIRA-123")
    def test_default_seat_numbers(self, number, owner, default_car):
        #assert default_car.number_of_seats == 5
        self.car.add_passenger('Another John')

        assert self.car.number_of_seats == 5


    def test_default_passengers(self, default_car):
        #assert default_car.passengers == []
        assert self.car.passengers == []

    def teardown_method(self):
        print("IN teardown method")

    def teardown_class(self):
        #self.car.close_connection()
        print("Teardown class")