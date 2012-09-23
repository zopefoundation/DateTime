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
      version = '3.0.1',
      url='http://pypi.python.org/pypi/DateTime',
      license='ZPL 2.1',
      description="""\
This package provides a DateTime data type, as known from Zope 2.
Unless you need to communicate with Zope 2 APIs, you're probably
better off using Python's built-in datetime module.""",
      author='Zope Foundation and Contributors',
      author_email='zope-dev@zope.org',
      long_description=open(
          os.path.join('src', 'DateTime', 'DateTime.txt')).read() + \
          '\n\n' + open('CHANGES.txt').read(),
      packages=find_packages('src'),
      package_dir={'': 'src'},

      install_requires=['zope.interface',
                        'pytz',
                       ],
      include_package_data=True,
      test_suite='DateTime.tests.testDateTime.test_suite',
      zip_safe=False,
      )
