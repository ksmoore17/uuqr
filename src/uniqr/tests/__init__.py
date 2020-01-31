from unittest import TestCase

import uniqr

class TestCode(TestCase):
    def test_creation(self):
        u = uniqr.Unit.create()

        self.assertTrue(isinstance(u, uniqr.Unit))
