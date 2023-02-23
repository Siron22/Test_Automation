from unittest import TestCase, main

class TestNewSimpleTest(TestCase):

    def setUp(self) -> None:
        print("Setup")

    def test_first(self):
        self.assertIn(1, [2, 3, 4])

    def tearDown(self) -> None:
        print("Teardown")



