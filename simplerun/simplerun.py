import time
import shlex
import subprocess
import threading
import multiprocessing

from .compat import basestring


def split_cmd(cmd_str):
    lexer = shlex.shlex(cmd_str)
    lexer.whitespace = '|'
    lexer.whitespace_split = True

    return map(shlex.split, tuple(lexer))


class Command(object):
    """Command object can run and return a `Result` object."""

    def __init__(self, stmt):
        self.stmt = stmt

    def run(self, data=None):
        exc = None
        start = time.time()
        try:
            proc = subprocess.Popen(self.stmt,
                                    universal_newlines=True,
                                    stdout=subprocess.PIPE,
                                    stdin=subprocess.PIPE,
                                    stderr=subprocess.PIPE,
                                    shell=False)
            out, err = proc.communicate(data)
            returncode = proc.returncode
        except Exception as e:
            out, err = '', ''
            returncode = -1
            exc = e
        finally:
            end = time.time()

        r = Result(self)
        r.std_out, r.std_err = out, err
        r.status_code = returncode
        r.et = float('%.2f' % (end - start))
        r.exc = exc

        return r

    def __str__(self):
        return ' '.join(self.stmt)

    def __repr__(self):
        return '<Command "{0}">'.format(' '.join(self.stmt))


class Result(object):
    """Result object including stdout, stderr, status_code."""

    def __init__(self, command):
        self.command = command
        self.std_out = None
        self.std_err = None
        self.status_code = None
        self.history = None
        self.rest = None
        self.exc = None
        self.et = -1    # elapse time

    def __repr__(self):
        return "<[{status_code}] `{command}` {et}s>".format(**self.__dict__)


def run(cmds, data=None):
    if isinstance(cmds, basestring):
        cmds = split_cmd(cmds)
    cmds = iter(cmds)

    if isinstance(data, Result):
        data = data.std_out
    elif hasattr(data, '__iter__'):
        data = ''.join(data)

    history = []

    for c in cmds:
        cmd = Command(c)
        r = cmd.run(data)
        history.append(r)

        if r.exc:
            break

        data = r.std_out

    result = history.pop()
    result.history = history
    result.rest = list(cmds)

    return result


def concurrent_run(batches, data=None):
    if not batches:
        return

    def worker(bat, data=None):
        cur = threading.currentThread()
        cur.ret = run(bat, data)

    threads = []
    for bat in batches:
        t = threading.Thread(name=bat.split()[0], target=worker, args=(bat,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    return [t.ret for t in threads]


def prun(batches, data=None):
    if not batches:
        return

    pool_size = multiprocessing.cpu_count() * 2
    pool = multiprocessing.Pool(processes=pool_size,
                                maxtasksperchild=2)
    results = pool.map(run, batches)
    pool.close()
    pool.join()

    return results
