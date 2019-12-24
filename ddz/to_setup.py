from setuptools import setup, find_packages
import programm

setup(
    name='table732',
    version=programm.__version__,
    entry_points={
        'console_scripts': ['table732 = programm.main:main']
    },
    install_requires=[
        'openpyxl'
    ]
)
