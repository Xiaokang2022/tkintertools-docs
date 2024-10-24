# tkintertools.toolbox.tools

Some useful utility classes or utility functions

## 🟢`_Trigger`



<code style='color: limegreen;'>class</code> <code style='color: orange;'>protected</code> | `object`


```python
def __init__(
    self,
    command: typing.Callable,
) -> None: ...
```
Single trigger

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
Get the status of the trigger

### 🟡`lock`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def lock(
    self,
) -> None: ...
```
Lock the trigger so that it can't be updated

### 🟡`reset`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def reset(
    self,
) -> None: ...
```
Reset the status of the trigger

### 🟡`unlock`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def unlock(
    self,
) -> None: ...
```
Unlock this trigger so that it can be updated again

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
Update the status of the trigger

`value`: updated value




## 🔵`embed_window`


<code style='color: royalblue;'>function</code> <code style='color: green;'>public</code>

```python
def embed_window(
    window: Misc,
    parent: tkinter.Misc | None,
    *,
    focus: bool = False,
) -> None: ...
```
Embed a widget into another widget

* `window`: Widget that will be embedded in
* `parent`: parent widget, `None` indicates that the parent widget is the
screen
* `focus`: whether direct input focus to this window


## 🔵`get_hwnd`


<code style='color: royalblue;'>function</code> <code style='color: green;'>public</code>

```python
def get_hwnd(
    widget: Widget,
) -> int: ...
```
Get the HWND of `tkinter.Widget`

## 🔵`get_text_size`


<code style='color: royalblue;'>function</code> <code style='color: green;'>public</code>

```python
def get_text_size(
    text: str,
    fontsize: int | None = None,
    family: str | None = None,
    *,
    padding: int = 0,
    master: tkinter.Canvas | tkintertools.core.virtual.Widget | None = None,
    **kwargs,
) -> tuple[int, int]: ...
```
Get the size of a text with a special font family and font size

* `text`: the text
* `fontsize`: font size of the text
* `family`: font family of the text
* `padding`: extra padding of the size
* `master`: default canvas or widget provided
* `kwargs`: kwargs of `tkinter.font.Font`

ATTENTION:

* This function only works when the fontsize is negative number!


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
return `True` if the operation succeeds, `False` otherwise

* `font_path`: the font file path
* `private`: if True, other processes cannot see this
font(Only Windows OS), and this font will be unloaded when the process dies
* `enumerable`: if True, this font will appear when enumerating
fonts(Only Windows OS)

ATTENTION:

* This function is referenced from `customtkinter.FontManager.load_font`,
CustomTkinter: https://github.com/TomSchimansky/CustomTkinter
* This function only works on Windows and Linux OS


## 🔵`screen_size`


<code style='color: royalblue;'>function</code> <code style='color: green;'>public</code>

```python
def screen_size(
) -> tuple[int, int]: ...
```
Return the size of the screen

## 🔵`set_mouse_position`


<code style='color: royalblue;'>function</code> <code style='color: green;'>public</code>

```python
def set_mouse_position(
    x: int,
    y: int,
) -> None: ...
```
Set mouse cursor position

ATTENTION:

This function only works on Windows OS!


## 🟣`_LINUX_FONTS_DIR`


<code style='color: skyblue;'>constant</code> <code style='color: orange;'>protected</code>

```python linenums="0"
_LINUX_FONTS_DIR: str = 'C:\\Users\\Yzk/.fonts/'
```


