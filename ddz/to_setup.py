from setuptools import setup, find_packages

setup(
    name='tableK732',
    packages=find_packages(),
    entry_points={'console_scripts': ['tableK732 = main_prog.main:main']},
    install_requires=['openpyxl']
)
