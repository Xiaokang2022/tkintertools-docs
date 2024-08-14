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

# __version__ = "0.0.1"
# __author__ = "Xiaokang2022 <2951256653@qq.com>"

import importlib
import inspect
import pathlib
import pkgutil
import types
import typing

import tkintertools as tkt
import tkintertools.toolbox as toolbox
from rich import print


def get_package_contents(package: types.ModuleType) -> dict:
    """"""
    contents = {}

    for _, modname, ispkg in pkgutil.iter_modules(package.__path__, package.__name__ + '.'):
        if ispkg:
            subpkg = importlib.import_module(modname)
            contents[modname.split('.')[-1]] = get_package_contents(subpkg)
        else:
            contents[modname.split('.')[-1]] = None

    return contents


def get_function_data(func: types.FunctionType) -> dict:
    """"""
    signature = inspect.signature(func)

    data = {
        "name": func.__name__,
        "parameters": [],
        "return_type": signature.return_annotation,
        "docstring": func.__doc__,
    }

    positional_only_flag = False
    keyword_only_flag = False

    for para in signature.parameters.values():
        if para.kind is inspect.Parameter.POSITIONAL_ONLY:
            positional_only_flag = True
        elif positional_only_flag:
            positional_only_flag = False
            data["parameters"].append({"name": "/"})

        if not keyword_only_flag and para.kind is inspect.Parameter.KEYWORD_ONLY:
            data["parameters"].append({"name": "*"})
            keyword_only_flag = True
        elif not keyword_only_flag and para.kind is inspect.Parameter.VAR_POSITIONAL:
            keyword_only_flag = True

        data["parameters"].append({
            "name": para.name,
            "kind": para.kind,
            "type": para.annotation,
            "default": para.default,
        })

    return data


def _get_para_name(name: str, kind) -> str:
    """"""
    match kind:
        case inspect.Parameter.VAR_POSITIONAL: return f"*{name}"
        case inspect.Parameter.VAR_KEYWORD: return f"**{name}"
        case _: return name


def _get_type_hint_string(type_hint) -> str:
    """"""
    if type_hint.__class__ is type:
        return type_hint.__name__
    return type_hint


def _get_value_string(value) -> str:
    """"""
    if isinstance(value, str):
        return f"'{value}'"
    return value


def get_function_define(func_data: dict) -> str:
    """"""
    define = f"def {func_data["name"]}(\n"

    for para in func_data["parameters"]:
        if para.get("kind") is None:
            para_define = para["name"]
        elif para["name"] == "self":
            para_define = para["name"]
        elif para["type"] is inspect.Parameter.empty and para["default"] is inspect.Parameter.empty:
            para_define = _get_para_name(para["name"], para["kind"])
        elif para["type"] is not inspect.Parameter.empty and para["default"] is inspect.Parameter.empty:
            para_define = f"{_get_para_name(para["name"], para["kind"])}: {
                _get_type_hint_string(para["type"])}"
        elif para["type"] is inspect.Parameter.empty and para["default"] is inspect.Parameter.empty:
            para_define = f"{_get_para_name(para["name"], para["kind"])} = {
                _get_value_string(para["default"])}"
        else:
            para_define = f"{_get_para_name(para["name"], para["kind"])}: {
                _get_type_hint_string(para["type"])} = {_get_value_string(para["default"])}"

        define += f"    {para_define},\n"

    return define + f") -> {_get_type_hint_string(func_data["return_type"])}: ..."


def parse_doc_string(doc_string: str) -> dict:
    """"""


if __name__ == "__main__":
    print(get_package_contents(tkt))
    print(get_function_define(get_function_data(tkt.InputBox.__init__)))
