"""
Setup for bibble, a better BibTeX-to-HTML (or BibTeX-to-whatever) converter
using Pybtex and Jinja2.
"""

from setuptools import setup

setup(
    name='bibble',
    version='0.0.1',
    packages=['bibble'],
    include_package_data=True,
    install_requires=[
        'click',
        'jinja2',
        'pybtex',
    ],
    entry_points={
        'console_scripts': [
            'bibble = bibble.main:main',
        ]
    },
)
