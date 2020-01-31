from unittest import TestCase
from mongoengine import *

from uniqr import *

class TestCode(TestCase):
    def test_creation(self):
        connect()

        u = Unit()

        self.assertTrue(isinstance(u, mongo.Unit))

if __name__ == '__main__':
    unittest.main()
