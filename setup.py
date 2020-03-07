#!/usr/bin/env python
from setuptools import setup

with open('README.md') as f:
    long_description = f.read()

setup(
    name="tomlet",
    version='0.1',
    author="bib",
    author_email="bib@users.noreply.github.com",
    description="TOML select value",
    long_description=long_description,
    url="https://github.com/bib/tomlet",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    py_modules=['tomlet'],    
    entry_points={
        'console_scripts': [
            'tomlet=tomlet:main',
            ],
    }
)
