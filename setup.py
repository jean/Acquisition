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
import platform
import sys
from setuptools import setup, find_packages, Extension

README = open(os.path.join('src', 'Acquisition', 'README.txt')).read()
CHANGES = open('CHANGES.rst').read()

# PyPy won't build the extension.
py_impl = getattr(platform, 'python_implementation', lambda: None)
is_pypy = py_impl() == 'PyPy'
is_pure = 'PURE_PYTHON' in os.environ
py3k = sys.version_info >= (3, )
if is_pypy or is_pure or py3k:
    ext_modules = []
else:
    ext_modules = [
        Extension("Acquisition._Acquisition",
                  [os.path.join('src', 'Acquisition', '_Acquisition.c')],
                  include_dirs=['include', 'src']),
    ]

setup(
    name='Acquisition',
    version='4.0.1dev',
    url='http://pypi.python.org/pypi/Acquisition',
    license='ZPL 2.1',
    description="Acquisition is a mechanism that allows objects to obtain "
        "attributes from the containment hierarchy they're in.",
    author='Zope Foundation and Contributors',
    author_email='zope-dev@zope.org',
    long_description='\n\n'.join([README, CHANGES]),
    packages=find_packages('src'),
    package_dir={'': 'src'},
    classifiers=[
        "Development Status :: 6 - Mature",
        "Environment :: Web Environment",
        "Framework :: Zope2",
        "License :: OSI Approved :: Zope Public License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2 :: Only",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: Implementation :: CPython",
    ],
    ext_modules=ext_modules,
    install_requires=[
        'ExtensionClass >= 4.1a1',
        'zope.interface',
    ],
    include_package_data=True,
    zip_safe=False,
)
