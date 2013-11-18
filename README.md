Simplerun
=========

Simple shell wrapper written by Python

Installation
============

    pip install simplerun

or

    python setup.py install

Usage
=====

Basic usage:
---------------

    import simplerun
    r = simplerun.run('ls -l')


Use iterable as input data:
--------------------------

    with open('simplerun.py') as f:
        r = simplerun.run('grep def', f)
        print r.std_out


Use `Result` as input data:
--------------------------

    r_data = simplerun.run('ps aux')
    r = simplerun.run('grep Chrome', r_data)

