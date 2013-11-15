Simplerun
=========

Simple shell wrapper written by Python

Usage
=====

Simplest usage:
---------------

    import simplerun
    r = simplerun.run('ps aux | grep Firefox')
  

Feed data by yourself:
----------------------

    import simplerun
    r = simplerun.run('grep def', open('simplerun.py'))
    print r.std_out
    

