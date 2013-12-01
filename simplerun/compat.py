import unittest
import sys

PY3 = (sys.version[0] == '3')

if PY3:
    basestring = str
else:
    basestring = basestring


class SRTest(unittest.TestCase):

    if PY3:
        assert_eq = unittest.TestCase.assertEqual
        assert_not_eq = unittest.TestCase.assertNotEqual
    else:
        def assert_eq(self, x, y):
            self.failUnlessEqual(x, y)

        def assert_not_eq(self, x, y):
            self.failIfEqual(x, y)
