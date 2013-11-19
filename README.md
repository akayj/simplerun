Simplerun
=========

Make shell script running in a Pythonic way.

Installation
============

    pip install simplerun

or

    python setup.py install

Usage
=====

Basic usage:
---------------

    >> import simplerun
    >> r = simplerun.run('ls -l')
    >> r

    return a formated text, `0` infer to the exit code here.
    <[0] `ls -l`>

    >> print r.std_out

    total 8
    -rw-r--r-- 1 yj staff 664 11 19 21:46 README.md
    -rw-r--r-- 1 yj staff 829 11 18 22:39 setup.py
    drwxr-xr-x 6 yj staff 204 11 19 21:46 simplerun


Use iterable as input data:
--------------------------

    with open('simplerun.py') as f:
        r = simplerun.run('grep def', f)
        print r.std_out


Use `Result` as input data:
--------------------------

    r_data = simplerun.run('ps aux')
    r = simplerun.run('grep Chrome', r_data)

