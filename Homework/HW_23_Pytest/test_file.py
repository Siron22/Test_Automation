from structure_without_list import StructureWithoutList, Item

"""New instance creating"""


def test_length_new(new_issue):
    assert new_issue.length == 0


"""Tests for one element"""


def test_length_one(add_one):
    assert add_one.length == 1


def test_get_one(add_one):
    assert add_one.get(1) == 'Hello first'


def test_del_one(add_one):
    add_one.delete(1)
    assert add_one.length == 0


"""Tests for few elements"""

"""Length test"""
def test_length_five(add_five1):
    assert add_five1.length == 5

"""GET tests"""
def test_get_first(add_five1):
    assert add_five1.get(1) == 'Hello first'

def test_get_second(add_five1):
    assert add_five1.get(2) == 'Hello second'

def test_get_third(add_five1):
    assert add_five1.get(3) == 'Hello third'

def test_get_fourth(add_five1):
    assert add_five1.get(4) == 'Hello fourth'

def test_get_fifth(add_five1):
    assert add_five1.get(5) == 'Hello fifth'

"""Test with random number generator """
def test_get_any(add_five1, any_number):
    assert add_five1.get(any_number[0]) == f'Hello {any_number[1]}'

"""DELETE tests"""

"""Delete all elements by number"""
def test_del_first(add_five2):
    add_five2.delete(1)
    assert add_five2.get(1) == 'Hello second' and add_five2.length == 4

def test_del_second(add_five2):
    add_five2.delete(1)
    assert add_five2.get(1) == 'Hello third' and add_five2.length == 3

def test_del_third(add_five2):
    add_five2.delete(1)
    assert add_five2.get(1) == 'Hello fourth' and add_five2.length == 2

def test_del_fourth(add_five2):
    add_five2.delete(1)
    assert add_five2.get(1) == 'Hello fifth' and add_five2.length == 1

def test_del_fifth(add_five2):
    add_five2.delete(1)
    assert add_five2.length == 0



