# -*- coding: utf-8 -*-
import ez_setup
from setuptools import setup, find_packages


ez_setup.use_setuptools()

setup(
    name="django-mobile",
    version="0.2",
    packages=find_packages(),
    author="Jeferson Farias Calazans",
    author_email="calazans10@gmail.com",
    description="A package to help dealing with mobile clients in Django",
    url="http://github.com/calazans10/django-mobile-helper",
    include_package_data=True
)
