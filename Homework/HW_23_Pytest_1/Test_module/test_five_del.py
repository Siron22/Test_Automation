import pytest

"""<<<<DELETE tests>>>>"""

"""Delete current element"""


def test_del_last5(add_five_d):
    add_five_d.delete(5)
    with pytest.raises(IndexError):
        add_five_d.get(5)


def test_del_last4(add_five_d):
    total = 5
    for i in range(2):
        add_five_d.delete(total)
        total -= 1
    with pytest.raises(IndexError):
        add_five_d.get(4)


def test_del_last3(add_five_d):
    total = 5
    for i in range(3):
        add_five_d.delete(total)
        total -= 1
    with pytest.raises(IndexError):
        add_five_d.get(3)


def test_del_last2(add_five_d):
    total = 5
    for i in range(4):
        add_five_d.delete(total)
        total -= 1
    with pytest.raises(IndexError):
        add_five_d.get(2)


@pytest.mark.smoke
def test_del_last1(add_five_d):
    total = 5
    for i in range(5):
        add_five_d.delete(total)
        total -= 1
    with pytest.raises(IndexError):
        add_five_d.get(1)


@pytest.mark.smoke
def test_del_last_len(add_five_d):
    """Length test"""
    total = 5
    for i in range(5):
        add_five_d.delete(total)
        total -= 1
    assert add_five_d.length == 0


"""<<<<Tests for correct index changes while delete>>>>"""


def test_del_first(add_five_d):
    add_five_d.delete(1)
    assert add_five_d.get(1) == 'Hello second' and add_five_d.length == 4


def test_del_second(add_five_d):
    for _ in range(2):
        add_five_d.delete(1)
    assert add_five_d.get(1) == 'Hello third' and add_five_d.length == 3


def test_del_third(add_five_d):
    for _ in range(3):
        add_five_d.delete(1)
    assert add_five_d.get(1) == 'Hello fourth' and add_five_d.length == 2


def test_del_fourth(add_five_d):
    for _ in range(4):
        add_five_d.delete(1)
    assert add_five_d.get(1) == 'Hello fifth' and add_five_d.length == 1


@pytest.mark.smoke
def test_del_fifth(add_five_d):
    for _ in range(5):
        add_five_d.delete(1)
    assert add_five_d.length == 0


@pytest.mark.smoke
def test_raise_one_five(add_five_d):
    """Test fo IndexError"""
    for _ in range(5):
        add_five_d.delete(1)
    with pytest.raises(IndexError):
        add_five_d.get(1)


