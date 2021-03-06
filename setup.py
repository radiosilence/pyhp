from setuptools import setup, find_packages
from pyhp import VERSION

NAME = 'pyhp'

setup(
    name=NAME,
    version=VERSION,
    description='a simple tool to hit websites at a given interval and'
        +' display whether they are up or not',
    long_description=open('README.rst').read(),
    url='https://github.com/radiosilence/pyhp',
    author='James Cleveland',
    author_email='jamescleveland@gmail.com',
    py_modules=['pyhp'],
    scripts=['scripts/pyhp'],
    include_package_data=True,
    license="LICENSE.txt",
    install_requires=open('requirements.txt').read().split("\n")
)
