# tkintertools.theme

<small>:octicons-mark-github-16: 源代码：[`tkintertools/theme/__init__.py`](https://github.com/Xiaokang2022/tkintertools/blob/3.0.0rc5/tkintertools/theme/__init__.py){ target='_blank' }</small>

Default style data

Base structure for `theme_name.py`:

```python
container_name01: dict[str, str | int] = {
    "attr01": value,
    "attr02": ...,
}

...

widget_name01: dict[str, dict[str, dict[str, str]]] = {
    "component01": {
        "state01": { attr01: "color", attr02: "color", ...},
        "state02": ...,
    },
    "component02": ...,
}

...
```

It is not mandatory for the variable to be a constant, it is enough to conform to the above format,
and the missing style will be empty by default and will not affect the operation of the program.


