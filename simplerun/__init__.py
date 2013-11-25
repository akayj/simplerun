'''Make shell script running in a Pythonic way.'''

from . import compat
from .simplerun import run, concurrent_run

run, concurrent_run  # make tricky with pep8

__version__ = '0.3'
