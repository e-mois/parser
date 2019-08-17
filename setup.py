#!/usr/bin/env python
import os
from setuptools import setup, find_packages
import parser.__version__ as ver


setup(name=ver.__title__,
      version=ver.__version__,
      package=find_packages(),
      url=ver.__url__,
      install_requires=[
          'requests',
          'bs4'
      ],
      include_package_data=True,
      zip_safe=False,
      )
