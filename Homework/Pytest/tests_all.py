import pytest


def test_length_new(new_issue):
    """New instance creating"""
    assert new_issue.length == 0


"""<<<<Tests for one element>>>>"""
@pytest.mark.one_el
def test_length_one(add_one):
    assert add_one.length == 1

@pytest.mark.one_el
def test_get_one(add_one):
    assert add_one.get(1) == 'Hello first'

@pytest.mark.one_el
def test_del_one(add_one):
    add_one.delete(1)
    assert add_one.length == 0

@pytest.mark.one_el
def test_raise_one(add_one):
    """Test fo IndexError"""
    add_one.delete(1)
    with pytest.raises(IndexError):
        add_one.get(1)


"""<<<<Tests for few elements>>>>"""

def test_length_five(add_five1):
    """Length test"""
    assert add_five1.length == 5


"""GET tests"""
def test_get_third(add_five1):
    assert add_five1.get(3) == 'Hello third'

def test_get_fifth(add_five1):
    assert add_five1.get(5) == 'Hello fifth'

def test_get_second(add_five1):
    add_five1.get(2)
    assert add_five1.get(2) == 'Hello second'

def test_get_fourth(add_five1):
    assert add_five1.get(4) == 'Hello fourth'

def test_get_first(add_five1):
    assert add_five1.get(1) == 'Hello first'

def test_get_any(add_five1, any_number):
    """Test with random number generator """
    assert add_five1.get(any_number[0]) == f'Hello {any_number[1]}'


"""<<<<DELETE tests>>>>"""

"""Delete current element"""
@pytest.mark.del_last
def test_del_last5(add_five4):
    add_five4.delete(5)
    with pytest.raises(IndexError):
        add_five4.get(5)

@pytest.mark.del_last
def test_del_last4(add_five4):
    add_five4.delete(4)
    with pytest.raises(IndexError):
        add_five4.get(4)

@pytest.mark.del_last
def test_del_last3(add_five4):
    add_five4.delete(3)
    with pytest.raises(IndexError):
        add_five4.get(3)

@pytest.mark.del_last
def test_del_last2(add_five4):
    add_five4.delete(2)
    with pytest.raises(IndexError):
        add_five4.get(2)

@pytest.mark.del_last
def test_del_last1(add_five4):
    add_five4.delete(1)
    with pytest.raises(IndexError):
        add_five4.get(1)

@pytest.mark.del_last
def test_del_last_len(add_five4):
    """Length test"""
    assert add_five4.length == 0

"""Delete all elements by number"""
@pytest.mark.delete
def test_del_first(add_five2):
    add_five2.delete(1)
    assert add_five2.get(1) == 'Hello second' and add_five2.length == 4

@pytest.mark.delete
def test_del_second(add_five2):
    add_five2.delete(1)
    assert add_five2.get(1) == 'Hello third' and add_five2.length == 3

@pytest.mark.delete
def test_del_third(add_five2):
    add_five2.delete(1)
    assert add_five2.get(1) == 'Hello fourth' and add_five2.length == 2

@pytest.mark.delete
def test_del_fourth(add_five2):
    add_five2.delete(1)
    assert add_five2.get(1) == 'Hello fifth' and add_five2.length == 1

@pytest.mark.delete
def test_del_fifth(add_five2):
    add_five2.delete(1)
    assert add_five2.length == 0

@pytest.mark.delete
def test_raise_one_five(add_five2):
    """Test fo IndexError"""
    with pytest.raises(IndexError):
        add_five2.get(1)


"""<<<<Tests for correct index changes while delete>>>>"""
@pytest.mark.del_ind
def test_del_fourth2(add_five1):
    add_five1.delete(4)
    assert add_five1.get(4) == 'Hello fifth' and add_five1.length == 4

@pytest.mark.del_ind
def test_del_second2(add_five1):
    add_five1.delete(1)
    assert add_five1.get(3) == 'Hello fifth' and add_five1.length == 3

@pytest.mark.del_ind
def test_del_first2(add_five1):
    add_five1.delete(1)
    assert add_five1.get(1) == 'Hello third' and add_five1.get(2) == 'Hello fifth' \
           and add_five1.length == 2


"""<<<<Tests for correct index changes while delete and add>>>>"""

@pytest.mark.del_add
def test_del_third3(add_five3):
    add_five3.delete(3)
    assert add_five3.get(3) == 'Hello fourth' and add_five3.get(4) == 'Hello fifth' \
           and add_five3.length == 4

@pytest.mark.del_add
def test_add_third3(add_five3):
    add_five3.add('Hello third')
    assert add_five3.get(5) == 'Hello third' and add_five3.length == 5

@pytest.mark.del_add
def test_del_second3(add_five3):
    add_five3.delete(2)
    assert add_five3.get(2) == 'Hello fourth' and add_five3.get(3) == 'Hello fifth' \
           and add_five3.length == 4

@pytest.mark.skip
@pytest.mark.del_add
def test_add_second3(add_five3):
    add_five3.add('Hello second')
    assert add_five3.get(5) == 'Hello second' and add_five3.length == 5


"""Test get_add_get"""
@pytest.mark.del_get_add
def test_add_second4444(add_five5):
    add_five5.get(1)
    add_five5.add('Hello sixth')
    add_five5.get(2)
    assert add_five5.get(2) == 'Hello second'