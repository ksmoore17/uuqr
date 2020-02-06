import pytest

from uuqr import *


host = "moore.com"
r = Resource(host="moore.com")

u = Unit()

class TestClasses:
    def test_creation(self):
        assert isinstance(u, Unit)
        assert isinstance(r, Resource)

    def test_url(self):
        assert r.get_url() == r.host
        assert u.get_url() == u.code

    def test_registration(self):
        u.certify(r)
        assert u.status == "certified"

        u.authenticate()
        assert u.status == "authenticated"

    def test_composite_url(self):
        assert u.get_url() == r.host + '/' + u.code
