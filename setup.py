"""
============
   About
============

Running shell in a Pythonic way.

============
Installation
============

.. code-block :: bash

    $ pip install simplerun

============
   Usage
============

Basic
=====

.. code-block :: python

    >> from simplerun import run
    >> r = run('ls -l')
    >> r
    <[0] `ls -l`>

`0` refers to the exit code here.

.. code-block :: python

    >> print r.std_out
    total 8
    -rw-r--r-- 1 yj staff 664 11 19 21:46 README.md
    -rw-r--r-- 1 yj staff 829 11 18 22:39 setup.py
    drwxr-xr-x 6 yj staff 204 11 19 21:46 simplerun


Iterable as input data
======================

.. code-block :: python

    >> with open('setup.py') as data:
    >>     r = run('grep def', data)
    >> print(r.std_out)

`Result` object as input data
=============================

.. code-block :: python

    >> r_data = run('ps aux')
    >> r = run('grep Chrome', r_data)

Use as a debugger
=================

.. code-block :: python

    >> r = run('ps aux | stranger | grep keyword')
    >> r
    <[-1] `stranger`>
    >> r.exc
    OSError(2, 'No such file or directory')

Found the `stanger` is the evil

.. code-block :: python

    >> r.history
    [<[0] `ps aux`>]

review history, and keep going with good input:

.. code-block :: python

    >> r.rest
    [['grep', 'keyword']]
    >>
    >> r2 = run(r.rest, '''Good line that contains the keyword,
                           but not this line, sorry.''')
    >> print(r2.std_out)
    'Good line that contains the keyword\n'
"""

import simplerun

try:
    from setuptools import setup
    setup   # make pep8 happy
except ImportError:
    from distutils.core import setup

setup(name='simplerun',
      version=simplerun.__version__,
      author='Yu Jian',
      author_email='askingyj@gmail.com',
      packages=['simplerun'],
      url='https://github.com/netspyer/simplerun',
      description=simplerun.__doc__,
      long_description=__doc__,
      zip_safe=False,
      classifiers=(
          'Development Status :: 4 - Beta',
          'Environment :: Console',
          'Intended Audience :: Developers',
          'Natural Language :: English',
          'License :: OSI Approved :: Apache Software License',
          'Operating System :: MacOS',
          'Operating System :: POSIX :: Linux',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.3',),
      )
