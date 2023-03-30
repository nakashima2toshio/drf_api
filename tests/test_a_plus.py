# TestCase description Template
import os
from unittest import TestCase


class APlusTestCase(TestCase):

    def setUp(self) -> None:

        print('setUp-->', __class__.__name__)

    def tearDown(self):
        print('tearDown-->', __class__.__name__)

    def test_a_plus(self):
        print('test-1a')
        a = 5
        assert a is self.answer

    def test_4a(self):
        print('test-4a')
        self.assertTrue(True)

    def test_5a(self):
        print('test-5a')
        self.assertTrue(True)
