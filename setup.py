#!/usr/bin/env python
import os
from setuptools import setup, find_package
from __version__ import about


setup(name=about['__title__'],
      version=about['__version__'],
      package=find_packages(),
      url=about['__url__'],
      install_requires=REQUIRED,
      include_package_data=True,
      zip_safe=False,
      )
