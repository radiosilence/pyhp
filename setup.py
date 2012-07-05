from setuptools import setup, find_packages

NAME = 'hping'

setup(
    name=NAME,
    version="0.1",
    description='a simple tool to hit websites at a given interval and'
        +' display whether they are up or not',
    long_description=open('README.rst').read(),
    url='https://github.com/radiosilence/hping',
    author='James Cleveland',
    author_email='jamescleveland@gmail.com',
    py_modules=['hping'],
    scripts=['scripts/hping'],
    include_package_data=True,
    license="LICENSE.txt",
    install_requires=open('requirements.txt').read().split("\n")
)
