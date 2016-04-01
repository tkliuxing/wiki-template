# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
from wiki_template import __version__

try:
    long_description = open("README.rst").read()
except IOError:
    long_description = ""

setup(
    name="wiki-template",
    version=__version__,
    description="A django-wiki plugin that MediaWiki style template implemented.",
    url="https://github.com/tkliuxing/wiki-template",
    license="GPLv3",
    author="Ronald White",
    packages=find_packages(),
    include_package_data=True,
    long_description=long_description,
    zip_safe=False,
    keywords=["wiki", "template"],
    install_requires=[
        "wiki>=0.1",
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
    ]
)
