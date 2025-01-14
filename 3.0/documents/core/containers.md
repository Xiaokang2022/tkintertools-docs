# tkintertools.core.containers

<small>:octicons-mark-github-16: 源代码：[`tkintertools/core/containers.py`](https://github.com/Xiaokang2022/tkintertools/blob/3.0.0rc6/tkintertools/core/containers.py){ target='_blank' }</small>

All containers.

There are two containers at the window level: `Tk` and `Toplevel`. `Tk` is
generally used for the main window, while `Toplevel` is a pop-up window.

There is another container at the canvas level: `Canvas`. `Canvas` is the main
container carrier.


## 🟢`Canvas`



<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code> | `Canvas` `Misc`


```python
def __init__(
    self,
    master: Tk | Toplevel | Canvas | None = None,
    *,
    expand: typing.Literal['', 'x', 'y', 'xy'] = 'xy',
    auto_zoom: bool = False,
    keep_ratio: typing.Literal['min', 'max'] | None = None,
    free_anchor: bool = False,
    auto_update: bool | None = None,
    zoom_all_items: bool = False,
    **kwargs,
) -> None: ...
```
Main contrainer: Canvas.

The parent widget of all virtual widgets is `Canvas`.


* `master`: parent widget
* `expand`: the mode of expand, `x` is horizontal, and `y` is vertical
* `auto_zoom`: whether or not to scale its items automatically
* `keep_ratio`: the mode of aspect ratio, `min` follows the minimum
value, `max` follows the maximum value
* `free_anchor`: whether the anchor point is free-floating
* `auto_update`: whether the theme manager update it automatically
* `zoom_all_items`: (Experimental) whether or not to scale its all items
* `kwargs`: compatible with other parameters of class `tkinter.Canvas`


### 🟡`_initialization`


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _initialization(
    self,
) -> None: ...
```
Initialization of size data.

### 🟡`_zoom_self`


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _zoom_self(
    self,
) -> None: ...
```
Scale the `Canvas` itself.

### 🟡`_zoom_tk_widgets`


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _zoom_tk_widgets(
    self,
    rel_ratio: tuple[float, float],
) -> None: ...
```
Scale the tkinter widgets of the Canvas.

* `rel_ratio`: the ratio of the current size to the previous size


### 🟡`clear`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def clear(
    self,
) -> None: ...
```
Clear all things in the Canvas.

### 🟡`create_text`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def create_text(
    self,
    x: float,
    y: float,
    /,
    *args,
    **kwargs,
) -> int: ...
```
Create text with coordinates x, y.

### 🟡`destroy`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def destroy(
    self,
) -> None: ...
```
Destroy this and all descendants widgets.

### 🟡`on_click`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def on_click(
    self,
    event: tkinter.Event,
    name: str,
) -> None: ...
```
Events to active the mouse

### 🟡`on_key_press`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def on_key_press(
    self,
    event: tkinter.Event,
) -> None: ...
```
Events for typing

### 🟡`on_key_release`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def on_key_release(
    self,
    event: tkinter.Event,
) -> None: ...
```
Events for typing

### 🟡`on_motion`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def on_motion(
    self,
    event: tkinter.Event,
    name: str,
) -> None: ...
```
Events to move the mouse

### 🟡`on_release`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def on_release(
    self,
    event: tkinter.Event,
    name: str,
) -> None: ...
```
Events to release the mouse

### 🟡`on_wheel`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def on_wheel(
    self,
    event: tkinter.Event,
    type_: bool | None,
) -> None: ...
```
Events to scroll the mouse wheel

### 🟡`register_event`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def register_event(
    self,
    name: str,
    *,
    add: bool | typing.Literal['', '+'] | None = None,
) -> str: ...
```
Register a event to process.

* `name`: event name, such as "<Alt-A>"
* `add`: whether it is an attached call

In general, you don't need to call this method, but when the event to
be bound is not in the predefined event, you need to manually call the
method once.


### 🟡`theme`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def theme(
    self,
    value: typing.Literal['light', 'dark'],
) -> None: ...
```
Change the color theme of the Canvas and its items

* `value`: theme name


### 🟡`zoom`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def zoom(
    self,
) -> None: ...
```
Resize and position the `Canvas` based on the relevant parameters.

This method only works for Canvas with Place layout.




## 🟢`Misc`



<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code> | `ABC`

### 🟡`__enter__`


<code style='color: #BBBB00;'>method</code> <code style='color: purple;'>special</code>

```python
def __enter__(
    self,
) -> typing_extensions.Self: ...
```


### 🟡`__exit__`


<code style='color: #BBBB00;'>method</code> <code style='color: purple;'>special</code>

```python
def __exit__(
    self,
    *args,
    **kwargs,
) -> None: ...
```


### 🟡`destroy`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def destroy(
    self,
) -> None: ...
```
Destroy the object.



## 🟢`Tk`



<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code> | `Tk` `Misc`


```python
def __init__(
    self,
    size: tuple[int, int] = (1280, 720),
    position: tuple[int, int] | None = None,
    *,
    title: str | None = None,
    icon: str | enhanced.PhotoImage | None = None,
    **kwargs,
) -> None: ...
```
Main window.

In general, there is only one main window. But after destroying it, another
one can be created.


* `size`: size of the window
* `position`: position of the window, based on the upper left (nw)
corner. And negative numbers are based on the bottom right (se) corner.
* `title`: title of the window, default value is `"tk"`
* `icon`: icon of the window, default value is the icon of tk
* `**kwargs`: compatible with other parameters of class `tkinter.Tk`


### 🟡`_fixed_theme`


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _fixed_theme(
    method,
) -> collections.abc.Callable: ...
```
This is a decorator that to fix a problem that some methods cause
the window to lose its theme.

* `method`: the method of being decorated


### 🟡`_wrap_method`


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _wrap_method(
    self,
    method_name: str,
) -> None: ...
```
Some problems can be fixed by decorating the original method.

* `method_name`: the name of the method to be decorated


### 🟡`_zoom`


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _zoom(
    self,
) -> None: ...
```
Zoom contents of the window.

### 🟡`alpha`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def alpha(
    self,
    value: float | None = None,
) -> float | None: ...
```
Set or get the transparency of the window

* `value`: the transparency of the window, range is 0~1


### 🟡`at_exit`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def at_exit(
    self,
    command: collections.abc.Callable[[], typing.Any],
    *,
    ensure_destroy: bool = True,
) -> None: ...
```
Set a function that will be called when the window is closed.

* `command`: the function that was called
* `ensure_destroy`: whether the window is guaranteed to be closed


### 🟡`center`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def center(
    self,
    *,
    refer: tkinter.Misc | None = None,
) -> None: ...
```
Center the container

`refer`: The area of the reference widget, if it is None, means that
the reference area is the entire screen.


### 🟡`destroy`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def destroy(
    self,
) -> None: ...
```
Destroy this and all descendants widgets.

### 🟡`fullscreen`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def fullscreen(
    self,
    value: bool | None = True,
) -> bool | None: ...
```
Set or get whether the window is full-screen.

* `value`: indicate whether the window is full-screen

The method should be called at the end of the code, or after some time
after the program has started.


### 🟡`geometry`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def geometry(
    self,
    *,
    size: tuple[int, int] | None = None,
    position: tuple[int, int] | None = None,
) -> tuple[int, int, int, int] | None: ...
```
Change the size and position of the window and return the current
size and position of the window.

* `size`: the size of the window, if it is None, does not change anything
* `position`: the position of the window, if it is None, does not change anything

If you want to use `tkinter.Tk.geometry`, please use
`tkinter.Tk.wm_geometry` instead.


### 🟡`icon`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def icon(
    self,
    value: str | enhanced.PhotoImage,
) -> None: ...
```
Set the icon of the window.

* `value`: the icon


### 🟡`theme`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def theme(
    self,
    value: typing.Literal['light', 'dark'],
    *,
    include_children: bool = True,
    include_canvases: bool = True,
) -> None: ...
```
Change the color theme of the window

* `value`: theme name
* `include_children`: wether include its children, like Toplevel
* `include_canvases`: wether include its canvases


### 🟡`toolwindow`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def toolwindow(
    self,
    value: bool | None = True,
) -> bool | None: ...
```
Set or get whether the window is tool-window

* `value`: indicate whether the window is tool-window

This method only works on Windows!


### 🟡`topmost`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def topmost(
    self,
    value: bool | None = True,
) -> bool | None: ...
```
Set or get whether the window is pinned or not

* `value`: indicate whether the window is topmost


### 🟡`transparentcolor`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def transparentcolor(
    self,
    value: str | None = None,
) -> str | None: ...
```
Set or get the penetration color of the window

* `value`: the penetration color of the window

This method only works on Windows!




## 🟢`Toplevel`



<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code> | `Toplevel` `Tk` `Misc`


```python
def __init__(
    self,
    master: Tk | Toplevel | None = None,
    size: tuple[int, int] = (960, 540),
    position: tuple[int, int] | None = None,
    *,
    title: str | None = None,
    icon: str | enhanced.PhotoImage | None = None,
    grab: bool = False,
    focus: bool = True,
    **kwargs,
) -> None: ...
```
Toplevel window.

It can be used as a pop-up window, or it can be customized to put anything
you want to show.


* `master`: parent widget
* `size`: size of the window, default value is 960x540(px)
* `position`: position of the window, default value indicates random
* `title`: title of window, default is the same as title of master
* `icon`: icon of the window, default is the same as title of master
* `grab`: set grab for this window
* `focus`: whether direct input focus to this window
* `**kwargs`: compatible with other parameters of class `tkinter.Toplevel`


### 🟡`destroy`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def destroy(
    self,
) -> None: ...
```
Destroy this and all descendants widgets.



