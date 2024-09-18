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

import importlib
import inspect
import os
import pkgutil
import pprint
import types
import typing

import tkintertools
import tkintertools.media
import tkintertools.mpl
import tkintertools.three

__version__ = "0.2.3"
__author__ = "Xiaokang2022 <2951256653@qq.com>"

TAGS: dict[str, str] = {
    "public": "green",
    "protected": "orange",
    "private": "red",
    "built-in": "purple",
    "special": "purple",
    "class": "limegreen",
    "function": "royalblue",
    "method": "#BBBB00",
    "variable": "#BBBB00",
    "constant": "skyblue",
}

TAGS = {n: f"<code style='color: {c};'>{n}</code>" for n, c in TAGS.items()}


def get_package_data(package: types.ModuleType) -> dict:
    """Get the data of a package"""
    data = {}

    for _, modname, ispkg in pkgutil.iter_modules(package.__path__, package.__name__ + '.'):
        if ispkg:
            subpkg = importlib.import_module(modname)
            data[modname.split('.')[-1]] = get_package_data(subpkg)
        else:
            data[modname.split('.')[-1]] = None

    return data


def get_module_data(module: types.ModuleType) -> dict:
    """Get the data for a module"""
    data = {
        "name": module.__name__,
        "docstring": module.__doc__,
        "classes": [],
        "functions": [],
        "variables": []
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


def _get_value_string(value: typing.Any, *, pp: bool = False) -> str:
    """Get the string form of a value"""
    if isinstance(value, str) and not pp:
        return f"'{value}'"
    elif inspect.ismodule(value):
        return value.__name__
    elif inspect.isfunction(value):
        return value.__name__
    elif inspect.ismethod(value):
        return value.__name__
    elif inspect.isclass(value):
        return value.__name__
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


def create_index(package: types.ModuleType) -> None:
    """"""
    data_package = get_package_data(package)

    with open("./3.0/documents/index.md", "w", encoding="utf-8") as file:
        file.write(f"""\
---
comments: true
icon: material/file-document
---

# 官方文档

!!! warning "特别说明"

    本文档仍在测试中，由于是直接通过程序将 Python 源代码转换成的数据，因此语言为英语，且可能存在数据不完整的问题，请大家查阅时注意甄别！

    条目类型：

    * 📦 **Package / 包**
    * 📑 **Module / 模块**
    * 🟢 **Class / 类**
    * 🔵 **Function / 函数**
    * 🟡 **Method / 方法**
    * 🟣 **Variable / 变量**

    当前文档适用版本：

    * tkintertools: `{tkintertools.__version__}`
    * tkintertools-mpl (EX): `{tkintertools.mpl.__version__}`
    * tkintertools-media (EX): `{tkintertools.media.__version__}`
    * tkintertools-3d (EX): `{tkintertools.three.__version__}`
""")

        for sub_package, modules in data_package.items():
            _sub_package = importlib.import_module(
                f"{package.__name__}.{sub_package}")
            data_sub_package = get_module_data(_sub_package)
            file.write(
                f"\n* 📦 [`{data_sub_package["name"]}`](./{sub_package}/index.md)\n")

            for module in modules:
                _module = importlib.import_module(
                    f"{_sub_package.__name__}.{module}")
                data_module = get_module_data(_module)
                file.write(
                    f"    - 📑 [`{data_module["name"]}`](./{sub_package}/{module}.md)\n")


def create_pages(module: types.ModuleType) -> None:
    """"""
    data_module = get_module_data(module)

    *_, sub_package_name, module_name = data_module["name"].split(".")
    file = f"./3.0/documents/{sub_package_name}/{
        module_name}.md".replace("__init__", "index")

    with open(file, "w", encoding="utf-8") as file:
        file.write(f"# {data_module["name"].replace(".__init__", "")}\n\n")
        file.write(f"{data_module["docstring"]}\n\n")
        if module_name != "__init__":
            if data_module["classes"]:
                for cls in sorted(data_module["classes"]):
                    file.write(create_class_md(getattr(module, cls)))
            if data_module["functions"]:
                for func in sorted(data_module["functions"]):
                    file.write(create_function_md(getattr(module, func)))
            if data_module["variables"]:
                for var in sorted(data_module["variables"]):
                    file.write(create_variable_md(
                        getattr(module, var), name=var))


def create_class_md(cls: object) -> str:
    """"""
    data = get_class_data(cls)

    string = f"## 🟢`{data["name"]}`\n\n"

    if data["name"].startswith("__") and data["name"].endswith("__"):
        label = TAGS["built-in"]
    elif data["name"].startswith("__"):
        label = TAGS["private"]
    elif data["name"].startswith("_"):
        label = TAGS["protected"]
    else:
        label = TAGS["public"]

    if data["parents"]:
        parent = f" | {" ".join(f"`{p.__name__}`" for p in data["parents"])}"
    else:
        parent = ""

    string += f"\n\n{"<code style='color: limegreen;'>class</code>"} {label}{parent}\n\n"

    for method in data["methods"]:
        if method.__name__ == "__init__":
            string += create_function_md(
                method, is_method=True, init_doc=data["docstring"])

    for method in sorted(data["methods"], key=lambda m: m.__name__):
        if method.__name__ == "__init__":
            continue
        string += create_function_md(method, is_method=True)

    return string + "\n\n"


def create_function_md(func: types.FunctionType | types.MethodType, *, is_method: bool = False, init_doc: str | None = None) -> str:
    """"""
    data = get_function_data(func)
    string = ""
    if init_doc is None:
        string = f"## 🔵`{data["name"]}`\n\n"
        if is_method:
            string = "#" + string.replace("🔵", "🟡")

    if data["name"].startswith("__") and data["name"].endswith("__"):
        label = TAGS["special"]
    elif data["name"].startswith("__"):
        label = TAGS["private"]
    elif data["name"].startswith("_"):
        label = TAGS["protected"]
    else:
        label = TAGS["public"]

    if is_method:
        kind = TAGS["method"]
    else:
        kind = TAGS["function"]

    if init_doc is not None:
        string += f"\n```python\n{get_function_define(data)}\n```\n"
    else:
        string += f"""
{kind} {label}

```python
{get_function_define(data)}
```
"""

    if init_doc is not None:
        string += init_doc.replace("    ", "") + "\n"
    if data["docstring"]:
        string += data["docstring"].replace("    ", "")

    return string + "\n\n"


def create_variable_md(var: object, *, name: str) -> str:
    """"""
    string = f"## 🟣`{name}`\n\n"

    if name.isupper():
        kind = TAGS["constant"]
    else:
        kind = TAGS["variable"]

    if name.startswith("__") and name.endswith("__"):
        label = TAGS["special"]
    elif name.startswith("__"):
        label = TAGS["private"]
    elif name.startswith("_"):
        label = TAGS["protected"]
    else:
        label = TAGS["public"]

    ps = pprint.pformat(_get_value_string(var, pp=True), width=100)

    if ps[0] in "{[(" and var:
        l = ps[0] + "\n"
        r = ",\n" + "}])"["{[(".index(ps[0])]
        ps = "    " + ps[1:-1]
    else:
        l = r = ""

    ps = "\n   ".join(ps.split("\n"))

    string += f"""
{kind} {label}

```python linenums="0"
{name}: {_get_type_hint_string(type(var))} = {l}{ps}{r}
```
"""

    return string + "\n\n"


def create_docs(lib: types.ModuleType) -> None:
    """"""
    create_index(lib)

    for sub_package, modules in get_package_data(lib).items():
        os.makedirs(f"./3.0/documents/{sub_package}/", exist_ok=True)
        create_pages(importlib.import_module(
            f"{lib.__name__}.{sub_package}.__init__"))
        for module in modules:
            create_pages(importlib.import_module(
                f"{lib.__name__}.{sub_package}.{module}"))


if __name__ == "__main__":
    create_docs(tkintertools)
