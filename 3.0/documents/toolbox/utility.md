# tkintertools.toolbox.utility

<small>:octicons-mark-github-16: 源代码：[`tkintertools/toolbox/utility.py`](https://github.com/Xiaokang2022/tkintertools/blob/3.0.0rc6/tkintertools/toolbox/utility.py){ target='_blank' }</small>

Some useful utility classes or utility functions.

## 🟢`Trigger`



<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code> | `object`


```python
def __init__(
    self,
    command: collections.abc.Callable[..., typing.Any],
) -> None: ...
```
Single trigger.

It can only be triggered once before the reset, and multiple triggers are
invalid. When triggered, the callback function is called.


* `command`: the function that is called when triggered


### 🟡`get`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def get(
    self,
) -> bool: ...
```
Get the status of the trigger.

### 🟡`lock`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def lock(
    self,
) -> None: ...
```
Lock the trigger so that it can't be updated.

### 🟡`reset`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def reset(
    self,
) -> None: ...
```
Reset the status of the trigger.

### 🟡`unlock`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def unlock(
    self,
) -> None: ...
```
Unlock this trigger so that it can be updated again.

### 🟡`update`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def update(
    self,
    value: bool = True,
    /,
    *args,
    **kwargs,
) -> None: ...
```
Update the status of the trigger.

* `value`: updated value
* `args`: args of the command
* `kwargs`: kwargs of the command




## 🔵`create_smoke`


<code style='color: royalblue;'>function</code> <code style='color: green;'>public</code>

```python
def create_smoke(
    size: tuple[int, int],
    *,
    color: str | tuple[int, int, int, int] = '#00000066',
) -> enhanced.PhotoImage: ...
```
Create a temporary smoke zone. Return the `enhanced.PhotoImage`.

* `size`: size of the smoke zone
* `color`: color of the smoke zone

This function need `PIL` to run.

About the "smoke", see: https://fluent2.microsoft.design/material#smoke


## 🔵`embed_window`


<code style='color: royalblue;'>function</code> <code style='color: green;'>public</code>

```python
def embed_window(
    window: tkinter.Misc,
    parent: tkinter.Misc | None,
    *,
    focus: bool = False,
) -> None: ...
```
Embed a widget into another widget.

* `window`: Widget that will be embedded in
* `parent`: parent widget, `None` indicates that the parent widget is the screen
* `focus`: whether direct input focus to this window


## 🔵`fix_cursor`


<code style='color: royalblue;'>function</code> <code style='color: green;'>public</code>

```python
def fix_cursor(
    name: str,
) -> str: ...
```
Fix the cursor name.

* `name`: name of cursor


## 🔵`get_parent`


<code style='color: royalblue;'>function</code> <code style='color: green;'>public</code>

```python
def get_parent(
    widget: tkinter.Misc,
) -> int: ...
```
Get the HWND of `tkinter.Widget`.

* `widget`: the widget


## 🔵`get_text_size`


<code style='color: royalblue;'>function</code> <code style='color: green;'>public</code>

```python
def get_text_size(
    text: str,
    fontsize: int | None = None,
    family: str | None = None,
    *,
    padding: int = 0,
    master: tkinter.Canvas | virtual.Widget | None = None,
    **kwargs,
) -> tuple[int, int]: ...
```
Get the size of a text with a special font family and font size.

* `text`: the text
* `fontsize`: font size of the text
* `family`: font family of the text
* `padding`: extra padding of the size
* `master`: default canvas or widget provided
* `kwargs`: kwargs of `tkinter.font.Font`

This function only works when the fontsize is negative number!


## 🔵`load_font`


<code style='color: royalblue;'>function</code> <code style='color: green;'>public</code>

```python
def load_font(
    font_path: str | bytes,
    *,
    private: bool = True,
    enumerable: bool = False,
) -> bool: ...
```
Make fonts located in file `font_path` available to the font system, and
return `True` if the operation succeeds, `False` otherwise.

* `font_path`: the font file path
* `private`: if True, other processes cannot see this font(Only Windows OS),
and this font will be unloaded when the process dies
* `enumerable`: if True, this font will appear when enumerating fonts(Only Windows OS)

This function only works on Windows and Linux OS.

This function is referenced from `customtkinter.FontManager.load_font`,
CustomTkinter: https://github.com/TomSchimansky/CustomTkinter.


## 🔵`screen_size`


<code style='color: royalblue;'>function</code> <code style='color: green;'>public</code>

```python
def screen_size(
) -> tuple[int, int]: ...
```
Returns the size of the screen.

