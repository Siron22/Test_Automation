import sys
import random
from structure_without_list import StructureWithoutList
import pytest

sys.path.append('/home/serhii/PycharmProjects/Test_Automation')
print(sys.path)


@pytest.fixture()
def new_issue():
    issue = StructureWithoutList()
    return issue


@pytest.fixture()
def add_one():
    issue = StructureWithoutList()
    issue.add('Hello first')
    return issue

@pytest.fixture(scope='class')
def add_five_cls():
    issue = StructureWithoutList()
    issue.add('Hello first')
    issue.add('Hello second')
    issue.add('Hello third')
    issue.add('Hello fourth')
    issue.add('Hello fifth')
    return issue

@pytest.fixture(scope='module')
def add_five():
    issue = StructureWithoutList()
    issue.add('Hello first')
    issue.add('Hello second')
    issue.add('Hello third')
    issue.add('Hello fourth')
    issue.add('Hello fifth')
    return issue

@pytest.fixture(scope='function')
def add_five_d():
    issue = StructureWithoutList()
    issue.add('Hello first')
    issue.add('Hello second')
    issue.add('Hello third')
    issue.add('Hello fourth')
    issue.add('Hello fifth')
    return issue




@pytest.fixture(scope='module')
def add_five1():
    issue = StructureWithoutList()
    issue.add('Hello first')
    issue.add('Hello second')
    issue.add('Hello third')
    issue.add('Hello fourth')
    issue.add('Hello fifth')
    return issue


@pytest.fixture()
def any_number():
    numbers = {
        1: 'first',
        2: 'second',
        3: 'third',
        4: 'fourth',
        5: 'fifth'
    }
    a, b = random.choice(list(numbers.items()))
    return a, b


@pytest.fixture(scope='module')
def add_five2():
    issue = StructureWithoutList()
    issue.add('Hello first')
    issue.add('Hello second')
    issue.add('Hello third')
    issue.add('Hello fourth')
    issue.add('Hello fifth')
    return issue

@pytest.fixture(scope='module')
def add_five3():
    issue = StructureWithoutList()
    issue.add('Hello first')
    issue.add('Hello second')
    issue.add('Hello third')
    issue.add('Hello fourth')
    issue.add('Hello fifth')
    return issue

@pytest.fixture(scope='module')
def add_five4():
    issue = StructureWithoutList()
    issue.add('Hello first')
    issue.add('Hello second')
    issue.add('Hello third')
    issue.add('Hello fourth')
    issue.add('Hello fifth')
    return issue

@pytest.fixture(scope='module')
def add_five5():
    issue = StructureWithoutList()
    issue.add('Hello first')
    issue.add('Hello second')
    issue.add('Hello third')
    issue.add('Hello fourth')
    issue.add('Hello fifth')
    return issue