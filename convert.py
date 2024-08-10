"""
Convert the documentation of a given Python package into Markdown

Usage:


"""

# MIT License

# Copyright (c) 2024 Xiaokang2022

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

__version__ = "0.0.1"
__author__ = "Xiaokang2022 <2951256653@qq.com>"

import inspect
import pathlib
import pkgutil
import types
import typing

import tkintertools.standard
from rich import print


def get_packages(path: typing.Iterable[str], prefix: str = "    ") -> None:
    """"""
    for _, modname, ispkg in pkgutil.iter_modules(path):
        if ispkg:
            print(f"{prefix}{modname}/", )
            get_packages([f"{path[0]}\\{modname}"], prefix + "    ")
        else:
            print(f"{prefix}{modname}.py")


print("tkintertools/")
get_packages(tkintertools.__path__)
