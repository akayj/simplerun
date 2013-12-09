import unittest
import simplerun

from simplerun.compat import SRTest


class BasicTest(SRTest):

    def test_list(self):
        r = simplerun.run('ls -l')
        self.assert_eq(r.status_code, 0)


class InputTest(SRTest):

    def test_iterableInput(self):
        with open('setup.py') as f:
            r = simplerun.run('grep def', f)
        self.assert_eq(r.status_code, 0)

    def test_Result(self):
        r_data = simplerun.run('ps aux')
        r = simplerun.run('grep python', r_data)
        self.assert_eq(r.std_err, '')
        self.assert_eq(r.exc, None)


class DebugTest(SRTest):

    def setUp(self):
        r = simplerun.run('ps aux | stranger | grep keyword')
        self.r = r

    def tearDown(self):
        del self.r

    def test_debug(self):
        self.assert_not_eq(self.r.exc, None)
        self.assert_eq(len(self.r.history), 1)

    def test_rest(self):
        self.assert_eq(self.r.rest, [['grep', 'keyword']])
        r2 = simplerun.run(self.r.rest, '''Good line contains the keyword
                                           but not this line, sorry.''')
        self.assert_eq(r2.status_code, 0)
        self.assert_eq(r2.std_out, 'Good line contains the keyword\n')


class ConCurrentRunTest(SRTest):

    def test_concurrent_run(self):
        batchs = ['ps aux', 'top -n 10', 'ps aux | grep Chrome']
        r = simplerun.concurrent_run(batchs)
        self.assert_eq(len(r), 3)

        r = simplerun.crun(batchs)
        self.assert_eq(len(r), 3)


class ParallelRunTest(SRTest):

    def test_prun(self):
        batchs = ['ps aux', 'top -n 10', 'ps aux | grep Chrome']
        results = simplerun.prun(batchs)
        self.assert_eq(len(results), 3)
        map(lambda r: self.assert_not_eq(r.et, -1), results)


if __name__ == "__main__":
    unittest.main()
