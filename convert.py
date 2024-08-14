"""Convert the documentation of a given Python package into Markdown"""

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
import pkgutil
import types
import typing

from rich import print


def get_package_contents(package: types.ModuleType) -> dict:
    """Get the contents of a package"""
    contents = {}

    for _, modname, ispkg in pkgutil.iter_modules(package.__path__, package.__name__ + '.'):
        if ispkg:
            subpkg = importlib.import_module(modname)
            contents[modname.split('.')[-1]] = get_package_contents(subpkg)
        else:
            contents[modname.split('.')[-1]] = None

    return contents


def get_module_data(module: types.ModuleType) -> dict:
    """Get the data for a module"""
    data = {
        'docstring': module.__doc__,
        'classes': [],
        'functions': [],
        'variables': []
    }

    for name, member in inspect.getmembers(module):
        if inspect.ismodule(member) or name.startswith('__'):
            continue

        if inspect.isclass(member) and member.__module__ == module.__name__:
            data['classes'].append(name)
        elif inspect.isfunction(member) and member.__module__ == module.__name__:
            data['functions'].append(name)
        elif not inspect.isbuiltin(member) and not inspect.isroutine(member):
            if not inspect.isclass(member) and not inspect.isfunction(member):
                data['variables'].append(name)

    return data


def get_class_data(cls: object) -> dict:
    """Get the data for a class"""
    data = {
        "name": cls.__name__,
        "parents": cls.__bases__,
        "methods": [method for method in set(cls.__dict__.values()) if callable(method)],
        "docstring": cls.__doc__,
    }

    return data


def get_function_data(func: types.FunctionType) -> dict:
    """Get the data for a function"""
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


def _get_para_name(name: str, kind: str) -> str:
    """Get the string form of a parameter"""
    match kind:
        case inspect.Parameter.VAR_POSITIONAL: return f"*{name}"
        case inspect.Parameter.VAR_KEYWORD: return f"**{name}"
        case _: return name


def _get_type_hint_string(type_hint: typing.Any) -> str:
    """Get the string form of a type hint"""
    if type_hint.__class__ is type:
        return type_hint.__name__
    return type_hint


def _get_value_string(value: typing.Any) -> str:
    """Get the string form of a value"""
    if isinstance(value, str):
        return f"'{value}'"
    return value


def get_function_define(func_data: dict) -> str:
    """Get the definition of a function"""
    define = f"def {func_data["name"]}(\n"

    for para in func_data["parameters"]:
        if para.get("kind") is None:
            para_define = para["name"]
        elif para["name"] == "self":
            para_define = para["name"]
        else:
            name = _get_para_name(para["name"], para["kind"])
            if para["type"] is inspect.Parameter.empty:
                type = ""
            else:
                type = f": {_get_type_hint_string(para["type"])}"
            if para["default"] is inspect.Parameter.empty:
                default = ""
            else:
                default = f" = {_get_value_string(para["default"])}"

            para_define = f"{name}{type}{default}"

        define += f"    {para_define},\n"

    return define + f") -> {_get_type_hint_string(func_data["return_type"])}: ..."
