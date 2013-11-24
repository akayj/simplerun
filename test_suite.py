import unittest
import simplerun


class BasicTest(unittest.TestCase):

    def test_list(self):
        r = simplerun.run('ls -l')
        self.failUnlessEqual(r.status_code, 0)


class InputTest(unittest.TestCase):

    def test_iterableInput(self):
        with open('setup.py') as f:
            r = simplerun.run('grep def', f)
        self.failUnlessEqual(r.status_code, 0)

    def test_Result(self):
        r_data = simplerun.run('ps aux')
        r = simplerun.run('grep python', r_data)
        self.failUnlessEqual(r.std_err, '')
        self.failUnlessEqual(r.exc, None)


class DebugTest(unittest.TestCase):

    def setUp(self):
        r = simplerun.run('ps aux | stranger | grep keyword')
        self.r = r

    def tearDown(self):
        del self.r

    def test_debug(self):
        self.failIfEqual(self.r.exc, None)
        self.failUnlessEqual(len(self.r.history), 1)

    def test_rest(self):
        self.failUnlessEqual(self.r.rest, [['grep', 'keyword']])
        r2 = simplerun.run(self.r.rest, '''Good line contains the keyword
                                           but not this line, sorry.''')
        self.failUnlessEqual(r2.status_code, 0)
        self.failUnlessEqual(r2.std_out, 'Good line contains the keyword\n')


if __name__ == "__main__":
    unittest.main()
