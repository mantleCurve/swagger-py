#!/usr/bin/env python3

#
# Copyright (c) 2013, Digium, Inc.
#

"""Setup script
"""

import os

from setuptools import setup

setup(
    name="swaggerpy",
    version="0.2.1",
    license="BSD 3-Clause License",
    description="Library for accessing Swagger-enabled API's",
    long_description=open(os.path.join(os.path.dirname(__file__),
                                       "README.rst")).read(),
    author="Digium, Inc.",
    author_email="dlee@digium.com",
    url="https://github.com/digium/swagger-py",
    packages=["swaggerpy"],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires='>=3.6',
    tests_require=["nose", "coverage", "httpretty>=1.1.4"],
    install_requires=["requests>=2.25.0", "websocket-client>=1.0.0"],
    entry_points="""
    [console_scripts]
    swagger-codegen = swaggerpy.codegen:main
    """
)
