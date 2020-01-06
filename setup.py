#!/usr/bin/env python
import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

about = dict()
with open(os.path.join(here, 'parser', '__version__.py'), 'r') as f:
    exec(f.read(), about)

setup(name=about['__title__'],
      version=about['__version__'],
      package=find_packages(),
      url=about['__url__'],
      install_requires=[
          'requests',
          'bs4',
          'lxml'
      ],
      include_package_data=True,
      zip_safe=False,
      )
