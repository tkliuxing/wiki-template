# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

try:
    long_description = open("README.rst").read()
except IOError:
    long_description = ""

setup(
    name="wiki-template",
    version="0.1",
    description="A pip package",
    license="GPLv3",
    author="Ronald White",
    packages=find_packages(),
    install_requires=[],
    long_description=long_description,
    install_requires=[
        "wiki>=0.1",
    ]
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.4",
    ]
)
