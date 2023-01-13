import pytest

@pytest.mark.second_run
@pytest.mark.first_run
def test_smoke1():
    assert 1 == 4

#@pytest.ini.mark.skip()
@pytest.mark.skip(reason='Skip because IP')
def test_smoke2():
    assert 1 == 1

@pytest.mark.skip(reason='Skip because IP')
def test_smoke4():
    assert 1 == 1



@pytest.mark.skipif(reason='Skip because OS', condition=True)
@pytest.mark.second_run
def test_smoke3():
    assert 1 == 1