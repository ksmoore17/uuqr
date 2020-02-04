import pytest

from uuqr import *

class TestCreates:
    def test_creation(self):
        u = Unit()

        assert isinstance(u, Unit)

        r = Resource(host="moore.com")

        assert isinstance(r, Resource)

class TestRegisters:
    def test_registration(self):
        u = Unit()

        r = Resource(host="moore.com")

        u.certify(r)

        assert u.status == "certified"

        u.authenticate()

        assert u.status == "authenticated"
