def add(a, b):
    return a + b


def test_add_3_56():
    assert add(3, 56) == 59


def test_add_4_5():
    assert add(4, 5) == 9


def test_add_4_1():
    res = add(4, 1)
    assert res == 10, f'Expected {10}, but got {res}'


def test_list111():
    print("In test_list")
    assert [1, 2, 3, 4] == [1, 2, 3, 4]

def test_tuple():
    print("In test_tuple")
    assert (1, 2, 3, 4) == (1, 5, 3, 4)

def test_with_several_assetions():
    assert 1 == 1
    assert 1 == 2, 'faileed'
    assert 1 == 3, 'failed 2'


# def QQQadd_4_1_test():
#     res = add(4, 1)
#     assert res == 10, f'Expected {10}, but got {res}'

