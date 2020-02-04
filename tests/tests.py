from unittest import TestCase

from uuqr import *

class TestCreates(TestCase):
    def test_creation(self):
        u = Unit()

        self.assertTrue(isinstance(u, Unit))

        r = Resource(host="moore.com")

        self.assertTrue(isinstance(r, Resource))

class TestRegisters(TestCase):
    def test_registration(self):
        u = Unit()

        r = Resource(host="moore.com")

        u.certify(r)

        self.assertTrue(u.status == "certified")

        u.authenticate()

        self.assertTrue(u.status == "authenticated")

if __name__ == '__main__':
    unittest.main()
