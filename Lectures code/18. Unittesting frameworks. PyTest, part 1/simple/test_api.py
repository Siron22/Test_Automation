import pytest


def test_api1():
    assert 3 == 3

@pytest.mark.first_run
def test_api2():
    assert 3 == 4

@pytest.mark.xfail(reason='JIRA-123')
def test_api3():
    assert 6 == 6