import pytest

"""<<<<Tests for few elements>>>>"""


@pytest.mark.smoke
def test_length_five(add_five):
    """Length test"""
    assert add_five.length == 5


"""GET tests"""


def test_get_third(add_five):
    assert add_five.get(3) == 'Hello third'


def test_get_fifth(add_five):
    assert add_five.get(5) == 'Hello fifth'


def test_get_second(add_five):
    add_five.get(2)
    assert add_five.get(2) == 'Hello second'


def test_get_fourth(add_five):
    assert add_five.get(4) == 'Hello fourth'


def test_get_first(add_five):
    assert add_five.get(1) == 'Hello first'


@pytest.mark.smoke
def test_get_any(add_five, any_number):
    """Test with random number generator """
    assert add_five.get(any_number[0]) == f'Hello {any_number[1]}'

