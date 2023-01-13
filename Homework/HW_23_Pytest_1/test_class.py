import pytest


def test_length_new(new_issue):
    """New instance creating"""
    assert new_issue.length == 0


class TestOne:
    """Tests for one element"""

    def test_length_one(self, add_one):
        assert add_one.length == 1

    def test_get_one(self, add_one):
        assert add_one.get(1) == 'Hello first'

    def test_del_one(self, add_one):
        add_one.delete(1)
        assert add_one.length == 0

    def test_raise_one(self, add_one):
        """Test fo IndexError"""
        add_one.delete(1)
        with pytest.raises(IndexError):
            add_one.get(1)


"""Tests for few elements"""


class TestAddFive:
    """ADD tests for five elements"""

    def test_length_five(self, add_five_cls):
        """Length test"""
        assert add_five_cls.length == 5

    def test_get_first(self, add_five_cls):
        assert add_five_cls.get(1) == 'Hello first'

    def test_get_second(self, add_five_cls):
        assert add_five_cls.get(2) == 'Hello second'

    def test_get_third(self, add_five_cls):
        assert add_five_cls.get(3) == 'Hello third'

    def test_get_fourth(self, add_five_cls):
        assert add_five_cls.get(4) == 'Hello fourth'

    def test_get_fifth(self, add_five_cls):
        assert add_five_cls.get(5) == 'Hello fifth'

    def test_get_any(self, add_five_cls, any_number):
        """Test with random number generator """
        assert add_five_cls.get(any_number[0]) == f'Hello {any_number[1]}'


"""DELETE tests"""


class TestDelFive:
    """Delete all elements by number"""
    def test_del_first(self, add_five_cls):
        add_five_cls.delete(1)
        assert add_five_cls.get(1) == 'Hello second' and add_five_cls.length == 4

    def test_del_second(self, add_five_cls):
        add_five_cls.delete(1)
        assert add_five_cls.get(1) == 'Hello third' and add_five_cls.length == 3

    def test_del_third(self, add_five_cls):
        add_five_cls.delete(1)
        assert add_five_cls.get(1) == 'Hello fourth' and add_five_cls.length == 2

    def test_del_fourth(self, add_five_cls):
        add_five_cls.delete(1)
        assert add_five_cls.get(1) == 'Hello fifth' and add_five_cls.length == 1

    def test_del_fifth(self, add_five_cls):
        add_five_cls.delete(1)
        assert add_five_cls.length == 0

    def test_raise_five(self, add_five_cls):
        """Test fo IndexError"""
        with pytest.raises(IndexError):
            add_five_cls.get(1)


class TestDelIndex:
    """Tests for correct index changes while delete"""

    def test_del_fourth(self, add_five_cls):
        add_five_cls.delete(4)
        assert add_five_cls.get(4) == 'Hello fifth' and add_five_cls.length == 4

    def test_del_second(self, add_five_cls):
        add_five_cls.delete(1)
        assert add_five_cls.get(3) == 'Hello fifth' and add_five_cls.length == 3

    def test_del_first(self, add_five_cls):
        add_five_cls.delete(1)
        assert add_five_cls.get(1) == 'Hello third' and add_five_cls.get(2) == 'Hello fifth' \
               and add_five_cls.length == 2

class TestDelCurElement:

    def test_del_last5(self, add_five_cls):
        add_five_cls.delete(5)
        with pytest.raises(IndexError):
            add_five_cls.get(5)

    def test_del_last4(self, add_five_cls):
        add_five_cls.delete(4)
        with pytest.raises(IndexError):
            add_five_cls.get(4)

    def test_del_last3(self, add_five_cls):
        add_five_cls.delete(3)
        with pytest.raises(IndexError):
            add_five_cls.get(3)

    def test_del_last2(self, add_five_cls):
        add_five_cls.delete(2)
        with pytest.raises(IndexError):
            add_five_cls.get(2)

    def test_del_last1(self, add_five_cls):
        add_five_cls.delete(1)
        with pytest.raises(IndexError):
            add_five_cls.get(1)

    def test_del_last_len(self, add_five_cls):
        """Length test"""
        assert add_five_cls.length == 0


class TestDelAddIndex:
    def test_del_third3(self, add_five_cls):
        add_five_cls.delete(3)
        assert add_five_cls.get(3) == 'Hello fourth' and add_five_cls.get(4) == 'Hello fifth' \
               and add_five_cls.length == 4

    def test_add_third3(self, add_five_cls):
        add_five_cls.add('Hello third')
        assert add_five_cls.get(5) == 'Hello third' and add_five_cls.length == 5

    def test_del_second3(self, add_five_cls):
        add_five_cls.delete(2)
        assert add_five_cls.get(2) == 'Hello fourth' and add_five_cls.get(3) == 'Hello fifth' \
               and add_five_cls.length == 4

    def test_add_second3(self, add_five_cls):
        add_five_cls.add('Hello second')
        assert add_five_cls.get(5) == 'Hello second' and add_five_cls.length == 5