#!/usr/bin/env python

from setuptools import setup, find_packages


with open("README.md", "r") as fh:
      long_description = fh.read()

setup(name='PyAsynch',
      version='1.2.2',
      description='Python asynch distributed and scalable Queue Services',
      long_description=long_description,
      long_description_content_type="text/markdown",
      author='Roberto Forlani',
      author_email='roberto.forlani@gmail.com',
      url='https://github.com/hoploop/pyasynch',
      install_requires=["pika","python-dateutil","tornado"],
      packages=find_packages()
      )
