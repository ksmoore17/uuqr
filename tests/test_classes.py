import pytest

from uuqr import Unit, Resource

TEST_DOMAIN = "moore.com"
r = Resource(domain=TEST_DOMAIN)

u = Unit()

class TestClasses:
    def test_creation(self):
        assert isinstance(u, Unit)
        assert isinstance(r, Resource)

    def test_url(self):
        assert r.get_url() == TEST_DOMAIN
        assert u.get_url() == u.code

    def test_registration(self):
        u.certify(r)
        assert u.status == "certified"

        u.authenticate()
        assert u.status == "authenticated"

    def test_composite_url(self):
        assert u.get_url() == TEST_DOMAIN + '/' + u.code
