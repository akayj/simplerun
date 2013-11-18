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
      long_description=simplerun.__doc__,
      zip_safe=False,
      classifiers=(
          'Development Status :: 4 - Beta',
          'Intended Audience :: Developers',
          'Natural Language :: English',
          'License :: OSI Approved :: Apache Software License',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
      ),
      )
