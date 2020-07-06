#!/usr/bin/env python3

__author__ = 'Rafael Zamora-Resendiz, rzamoraresendiz@protonmail.com'

from setuptools import setup, find_packages

setup(
    name="iposter",
    version="0.0.0",
    description="LBNL template For Dash interactive posters.",
    license="MIT",
    keywords="",
    packages=find_packages(exclude=[]),
    package_data={
        'iposter': ['*.py'],
    },
    install_requires = ["dash", "plotly", "dash_bootstrap_components"],
)
