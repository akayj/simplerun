'''Make shell script running in a Pythonic way.'''

from . import compat
from .simplerun import run, prun, concurrent_run, crun

# make tricky with pep8t
compat
run, concurrent_run, prun, crun

__version__ = '0.3.2'
