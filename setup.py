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
      license='GPL v2',
      description=simplerun.__doc__,
      platform='All',
      )
