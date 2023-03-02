import sys
sys.path.append('/home/olytvynov/Projects/HL/hl_pyauto_17oct22')
print(sys.path)

from L18.car import Car

import pytest

# def test_number_validation1():
#     car = Car('ABC1234', 'Owner1')
#     assert car.validate_number_plate()
#
# def test_number_validation2():
#     car = Car('QWE5432', 'Owner2')
#     assert car.validate_number_plate()
#
# def test_number_validation3():
#     car = Car('QW4543E', 'Owner3')
#     assert car.validate_number_plate()

# def test_number_validation_invalid1():
#     car = Car('A54BC1234', 'Owner1')
#     assert not car.validate_number_plate()
#
# def test_number_validation_invalid2():
#     car = Car('12344', 'Owner1')
#     assert not car.validate_number_plate()
#
# def test_number_validation_invalid3():
#     car = Car('', 'Owner1')
#     assert not car.validate_number_plate()


# @pytest.mark.parametrize('number,owner', [('ABC1234', 'Owner1'), ('QWE5432', 'Owner2'), ('QW4543E', 'Owner3')])
# def test_number_validation_valid(number, owner):
#     car = Car(number, owner)
#     assert car.validate_number_plate()
#
# param = '3333333333333333333333'
# invalid_input_data = [(param, 'Owner1'), ('12344', 'Owner1'), ('', 'Owner1')]
#
# @pytest.mark.parametrize('number,owner', invalid_input_data)
# def test_number_validation_invalid(number, owner):
#     car = Car(number, owner)
#     assert not car.validate_number_plate()


validation_input_data = [('ABC1234', 'Owner1', True), ('QWE5432', 'Owner2', True), ('QW4543E', 'Owner3', True),
                         ('3333333333333333333', 'Owner1', False), ('12344', 'Owner1', False), ('', 'Owner1', False)]
@pytest.mark.parametrize('number,owner,expected_result', validation_input_data)
def test_number_validation(number, owner, expected_result):
    car = Car(number, owner)
    assert car.validate_number_plate() is expected_result


lst_input_data = [([], 0), ([1], 1), ([1,2,3], 3)]
lst_ids = [f"{item[0]}_LEN{item[1]}" for item in lst_input_data]
lst_ids = ['first', 'second', 'third']


@pytest.mark.parametrize('lst,length', lst_input_data, ids=lst_ids)
def test_list_len(lst, length):
    assert len(lst) == length


lst_input_data = [
    pytest.param([], 0, id='first'),
    pytest.param([1], 1, id='second'),
    pytest.param([1,2,3], 3, id='third')]


@pytest.mark.parametrize('lst,length', lst_input_data, ids=lst_ids)
def test_list_len_ids(lst, length):
    assert len(lst) == length


lst_input_data = [
    pytest.param([], 0, id='first'),
    pytest.param([1], 1, id='second', marks=pytest.mark.skip(reason="Just don't want to run it")),
    pytest.param([1, 2, 3], 3, id='third', marks=pytest.mark.custom_parametrized_mark),
    pytest.param([1, 2, 3], 123, id='fourth', marks=pytest.mark.xfail(reason='Failed intentionally'))
]


@pytest.mark.parametrize('lst,length', lst_input_data)
def test_list_len_ids_with_skip_scenario(lst, length):
    assert len(lst) == length
