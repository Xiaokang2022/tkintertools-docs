# tkintertools.style.parser


Parse the style file path and get it

Structure of theme folder:

* format of ".py": see tkintertools/theme/__init__.py
* format of ".json":

```
theme/
  ├─theme01_name/
  │   ├─container01_name.json
  │   ├─container02_name.json
  │   ├─ ...
  │   ├─widget01_name.json
  │   ├─widget02_name.json
  │   └─ ...
  ├─theme02_name/
  └─ ...
```

* Structure of `container_name.json`:

```json
{
    "arg01": "value01",
    "arg02": "value02",
    ...
}
```

* Structure of `widget_name.extra.json`:

```json
{
    "component01": {
        "state01": {
            "arg01": "color",
            "arg02": "color",
            ...
        },
        "state02": {
            ...
        },
        ...
    },
    "component02": {
        ...
    },
    ...
}
```

Style files in JSON format must strictly follow the above format, and the
missing parts are empty by default.


## 🔵`_get_name`


<code style='color: royalblue;'>function</code> <code style='color: orange;'>protected</code>

```python
def _get_name(
    obj: str | virtual.Widget | virtual.Component | None,
) -> str | None: ...
```
Get the name of the object

## 🔵`get`


<code style='color: royalblue;'>function</code> <code style='color: green;'>public</code>

```python
def get(
    widget: str | virtual.Widget | containers.Canvas,
    component: str | virtual.Component | None = None,
    *,
    theme: str | pathlib._local.Path | module | None = None,
) -> dict[str, dict[str, str]] | dict[str, typing.Any]: ...
```

Get style data based on parameters

* `widget`: widget that need to get styles
* `component`: component that need to get styles
* `theme`: path to the style folder


