"""Setup tools"""
import os

from setuptools import setup

# pylint: disable=W1501,W1514
with open(os.path.join(os.path.dirname(__file__), "README.md")) as readme:
    README = readme.read()

setup(
    name="micropy",
    version="0.4.0",
    author="Pradeep",
    author_email="pkyisky@gmail.com",
    description="Micro Py package",
    # flake8: noqa
    url="https://github.com/mwpnava/Python-Code/tree/master/My_own_Python_package",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    py_modules=["micropy/mymodule"],
)
