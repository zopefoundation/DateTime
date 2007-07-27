##############################################################################
#
# Copyright (c) 2007 Zope Corporation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""Setup for the Acquisition egg package
"""
import os
from setuptools import setup, find_packages, Extension

setup(name='DateTime',
      version = '2.11.0a1',
      url='http://cheeseshop.python.org/pypi/DateTime',
      license='ZPL 2.1',
      description='DateTime data type',
      author='Zope Corporation and Contributors',
      author_email='zope-dev@zope.org',
      long_description="""\
This package provides a DateTime data type, as known from Zope 2.
Unless you need to communicate with Zope 2 APIs, you're probably
better off using Python's bult-in datetime module.""",
      
	  packages=find_packages('src'),
	  package_dir={'': 'src'},

      install_requires=['zope.interface'],
      include_package_data=True,
      zip_safe=False,
      )
