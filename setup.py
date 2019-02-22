#!/usr/bin/env python

from distutils.core import setup

setup(name='PyAsynch',
      version='1.0',
      description='Python ASynch Distrbiuted Scalable Queue Services',
      author='Roberto Forlani',
      author_email='roberto.forlani@gmail.com',
      url='https://www.python.org/sigs/distutils-sig/',
      packages=['pyasynch','pika','python-dateutil','tornado']
      )
