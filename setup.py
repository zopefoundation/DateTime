##############################################################################
#
# Copyright (c) 2007 Zope Foundation and Contributors.
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

import os
from setuptools import setup, find_packages

setup(name='DateTime',
      version='3.0.4dev',
      url='http://pypi.python.org/pypi/DateTime',
      license='ZPL 2.1',
      description="""\
This package provides a DateTime data type, as known from Zope 2.
Unless you need to communicate with Zope 2 APIs, you're probably
better off using Python's built-in datetime module.""",
      author='Zope Foundation and Contributors',
      author_email='zope-dev@zope.org',
      long_description=open(
          os.path.join('src', 'DateTime', 'DateTime.txt')).read() +
          '\n\n' + open('CHANGES.txt').read(),
      packages=find_packages('src'),
      package_dir={'': 'src'},
      classifiers=[
          "Development Status :: 6 - Mature",
          "Environment :: Web Environment",
          "Framework :: Zope2",
          "License :: OSI Approved :: Zope Public License",
          "Operating System :: OS Independent",
          "Programming Language :: Python",
          "Programming Language :: Python :: 2",
          "Programming Language :: Python :: 2 :: Only",
          "Programming Language :: Python :: 2.6",
          "Programming Language :: Python :: 2.7",
          "Programming Language :: Python :: 3",
          "Programming Language :: Python :: 3.2",
          "Programming Language :: Python :: 3.3",
          "Programming Language :: Python :: Implementation :: CPython",
      ],
      install_requires=[
          'zope.interface',
          'pytz',
      ],
      include_package_data=True,
      test_suite='DateTime.tests.test_datetime.test_suite',
      zip_safe=False,
      )
