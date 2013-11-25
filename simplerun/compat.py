import unittest
import sys

PY3 = (sys.version[0] == '3')

class SRTest(unittest.TestCase):

    def assert_eq(self, x, y):
        self.failUnlessEqual(x, y)

    def assert_not_eq(self, x, y):
        self.failIfEqual(x, y)

    if PY3:
        assert_eq = unittest.TestCase.assertEqual
        assert_not_eq = unittest.TestCase.assertNotEqual
