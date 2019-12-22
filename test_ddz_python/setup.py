from setuptools import setup, find_packages
from os.path import join, dirname
import src

setup(
    name='timetable-classes',
    version=src.__version__,
    packages=find_packages(),
    long_description=open(join(dirname(__file__), 'README.md')).read(),
    entry_points={
        'console_scripts': ['timetable-classes = src.main:main']
    },
    install_requires=[
        'openpyxl'
    ]
)
