# maliang.standard.dialogs

<small>:octicons-mark-github-16: 源代码：[`maliang/standard/dialogs.py`](https://github.com/Xiaokang2022/maliang/blob/3.0.0rc6/maliang/standard/dialogs.py){ target='_blank' }</small>

All standard dialog classes

## 🟢`TkColorChooser`



<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code> | `object`


```python
def __init__(
    self,
    *,
    title: str | None = None,
    color: str | None = None,
    master: tkinter.Tk | None = None,
    command: collections.abc.Callable[[str], typing.Any] | None = None,
) -> None: ...
```
Color chooser pop-up

* `title`: title of the window
* `color`: default color
* `master`: parent widget of the window
* `command`: callback function




## 🟢`TkFontChooser`



<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code> | `object`


```python
def __init__(
    self,
    *,
    title: str | None = None,
    font: str | None = None,
    master: tkinter.Tk | None = None,
    command: collections.abc.Callable[[str], typing.Any] | None = None,
) -> None: ...
```
Font chooser pop-up

* `title`: title of the window
* `font`: default font
* `master`: parent widget of the window
* `command`: callback function




## 🟢`TkMessage`



<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code> | `object`


```python
def __init__(
    self,
    message: str | None = None,
    detail: str | None = None,
    *,
    title: str | None = None,
    icon: typing.Literal['error', 'info', 'question', 'warning'] = 'info',
    option: typing.Literal['abortretryignore', 'ok', 'okcancel', 'retrycancel', 'yesno', 'yesnocancel'] = 'ok',
    default: typing.Literal['abort', 'retry', 'ignore', 'ok', 'cancel', 'yes', 'no'] | None = None,
    master: tkinter.Tk | None = None,
    command: collections.abc.Callable[[typing.Literal['abort', 'retry', 'ignore', 'ok', 'cancel', 'yes', 'no']], typing.Any] | None = None,
) -> None: ...
```
Message pop-up

* `message`: message
* `detail`: detail message
* `title`: title of the window
* `icon`: icon
* `option`: type of the message pop-up
* `default`: button where the focus is, default is the leftmost one
* `master`: parent widget of the window
* `command`: callback function




