#!/usr/bin/env python

import sys
try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

if sys.version_info < (2, 6):
    raise NotImplementedError("Sorry, you need at least Python 2.6 or Python 3.2+ to use py-term.")

import telegram

with open('README.rst', 'r') as f:
    longDesc = f.read()

setup(name='telegram-bot',
      version=telegram.__version__,
      description='telegram-bot help creating telegram bots in python.',
      long_description=longDesc,
      author='Rene Tanczos',
      author_email='gravmatt@gmail.com',
      url='https://github.com/gravmatt/telegram-bot',
      packages = find_packages(),
    #   py_modules=['telegram'],
    #   scripts=['telegram.py', 'http.py', 'bottle.py'],
      license='MIT',
      platforms='all',
      classifiers=['Intended Audience :: Developers',
                   'License :: OSI Approved :: MIT License',
                   'Programming Language :: Python :: 2.5',
                   'Programming Language :: Python :: 2.6',
                   'Programming Language :: Python :: 2.7',
                #    'Programming Language :: Python :: 3',
                #    'Programming Language :: Python :: 3.2',
                #    'Programming Language :: Python :: 3.3',
                   'Intended Audience :: Developers',
                   'Programming Language :: Python',
                   ],
      )
