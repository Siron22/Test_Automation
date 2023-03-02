import pytest


class Consumer:

    def __init__(self):
        pass

    def consume(self):
        return [1, 2, 3, 4]

    def stop(self):
        print("Stopped")


@pytest.fixture
def consumer():
    c = Consumer()
    yield c
    c.stop()


# def test_consumer1():
#     #init
#     c = Consumer()
#     data = c.consume()
#
#     assert data == [1, 2, 3, 4, 5]
#
#     c.stop()


# def test_consumer2(consumer):
#     data = consumer.consume()
#     assert data == [1, 2, 3, 4, 5]

@pytest.fixture()
def keeper():
    storage = []
    yield storage
    for consumer in storage:
        consumer.stop()

def test_consumer3(keeper):
    #start service
    c = Consumer()
    keeper.append(c)
    data = c.consume()
    assert data == [1, 2, 3, 4, 5]
