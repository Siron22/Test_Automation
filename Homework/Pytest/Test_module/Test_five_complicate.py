import pytest

"""<<<< Test for add->delete->get >>>>"""


@pytest.mark.bug
def test_add_del_get(add_five_d):
    add_five_d.delete(3)
    add_five_d.add('Hello third')
    add_five_d.get(5)
    assert add_five_d.get(5) == 'Hello third' and add_five_d.length == 5


"""<<<< Test for delete->add->delete->add >>>>"""


@pytest.mark.bug
def test_del_third3(add_five_d):
    add_five_d.delete(3)
    add_five_d.add('Hello third')
    add_five_d.delete(2)
    add_five_d.add('Hello second')
    assert add_five_d.get(5) == 'Hello second'


"""<<<< Test for get->add->get >>>>"""


@pytest.mark.bug
def test_add_second4444(add_five5):
    add_five5.get(1)
    add_five5.add('Hello sixth')
    add_five5.get(2)
    assert add_five5.get(2) == 'Hello second'
