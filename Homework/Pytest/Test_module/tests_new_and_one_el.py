import pytest


@pytest.mark.smoke
def test_length_new(new_issue):
    """New instance creating"""
    assert new_issue.length == 0


"""<<<<Tests for one element>>>>"""


@pytest.mark.smoke
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
