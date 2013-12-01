'''Make shell script running in a Pythonic way.'''

from . import compat
from .simplerun import run, prun, concurrent_run

compat, run, concurrent_run  # make tricky with pep8
prun

__version__ = '0.3.1'
