Simplerun
=========

Simple shell wrapper written by Python

Usage
=====

Basic usage:
---------------

    import simplerun
    r = simplerun.run('ls -l')


Use iterable as input data:
--------------------------

    r = simplerun.run('grep def', open('simplerun.py'))
    print r.std_out


Use `Result` as input data:
--------------------------

    r_data = simplerun.run('ps aux')
    r = simplerun.run('grep Chrome', r_data)