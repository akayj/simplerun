import sys
import shlex
import subprocess


PY3 = (sys.version[0] == '3')

if PY3:
    basestring = str


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
        try:
            proc = subprocess.Popen(self.stmt,
                                    universal_newlines=True,
                                    stdout=subprocess.PIPE,
                                    stdin=subprocess.PIPE,
                                    stderr=subprocess.PIPE,
                                    shell=False)
            out, err = proc.communicate(data)
            returncode = proc.returncode
        except Exception as exc:
            out, err = None, None
            returncode = -1
            exc = exc

        r = Result(self)
        r.std_out, r.std_err = out, err
        r.status_code = returncode
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

    def __repr__(self):
        return "<[{}] `{}`>".format(self.status_code, self.command)


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
