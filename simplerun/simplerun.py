import shlex
import subprocess


def split_cmd(cmd_str):
    lexer = shlex.shlex(cmd_str)
    lexer.whitespace = '|'
    lexer.whitespace_split = True

    return map(shlex.split, tuple(lexer))


class Command(object):
    """Command object can run and return a `Result` object."""

    def __init__(self, stmt):
        self.stmt = stmt
        self.exc = None
        self.out = None
        self.err = None
        self.returncode = 0

    def run(self, data=None):
        try:
            proc = subprocess.Popen(self.stmt,
                                    universal_newlines=True,
                                    stdout=subprocess.PIPE,
                                    stdin=subprocess.PIPE,
                                    shell=False)
            self.out, self.err = proc.communicate(data)
        except Exception as exc:
            self.out = None
            self.err = None
            self.returncode = -1
            self.exc = exc

        r = Result(self)
        r.std_out, r.std_err = self.out, self.err
        r.status_code = self.returncode
        r.exc = self.exc

        return r

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
        return '<Result [{0}]>'.format(self.status_code)


def run(cmds, data=None):
    if isinstance(cmds, basestring):
        cmds = split_cmd(cmds)

    cmds = iter(cmds)
    data = data

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


if __name__ == "__main__":
    r = run('wc -l', open('simplerun.py').read())
    print r.std_out,

    r2 = run('grep def', open('simplerun.py').read())
    print r2.std_out,
