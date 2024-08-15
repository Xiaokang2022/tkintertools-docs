# tkintertools.toolbox.tools

Some useful utility classes or utility functions

## 🟢 Classes / 类

### <big>`_Trigger`</big>



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


#### <big>`get`</big>


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def get(
    self,
) -> bool: ...
```
Get the status of the trigger

#### <big>`lock`</big>


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def lock(
    self,
) -> None: ...
```
Lock the trigger so that it can't be updated

#### <big>`reset`</big>


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def reset(
    self,
) -> None: ...
```
Reset the status of the trigger

#### <big>`unlock`</big>


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def unlock(
    self,
) -> None: ...
```
Unlock this trigger so that it can be updated again

#### <big>`update`</big>


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def update(
    self,
    value: bool = True,
    *args,
    **kwargs,
) -> None: ...
```

Update the status of the trigger

`value`: updated value




## 🔵 Functions / 函数

### <big>`embed_window`</big>


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
* `parent`: parent widget, `None` indicates that the parent widget is the screen
* `focus`: whether direct input focus to this window


### <big>`get_hwnd`</big>


<code style='color: royalblue;'>function</code> <code style='color: green;'>public</code>

```python
def get_hwnd(
    widget: Widget,
) -> int: ...
```
Get the HWND of `tkinter.Widget`

### <big>`get_text_size`</big>


<code style='color: royalblue;'>function</code> <code style='color: green;'>public</code>

```python
def get_text_size(
    text: str,
    fontsize: int | None = None,
    family: str | None = None,
    *,
    padding: int = 0,
) -> tuple[int, int]: ...
```

Get the size of a text with a special font family and font size

* `text`: the text
* `fontsize`: font size of the text
* `family`: font family of the text
* `padding`: extra padding of the size

ATTENTION:

* This function only works when the fontsize is negative number!
* When there is a line break, the return value will be inaccurate!


### <big>`load_font`</big>


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
* `private`: if True, other processes cannot see this font, and this font
will be unloaded when the process dies
* `enumerable`: if True, this font will appear when enumerating fonts

ATTENTION:

* This function is referenced from `customtkinter.FontManager.load_font`,
CustomTkinter: https://github.com/TomSchimansky/CustomTkinter
* This function only works on Windows and Linux operating systems


### <big>`screen_size`</big>


<code style='color: royalblue;'>function</code> <code style='color: green;'>public</code>

```python
def screen_size(
) -> tuple[int, int]: ...
```
Return the size of the screen

### <big>`set_mouse_position`</big>


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


