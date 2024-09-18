# tkintertools.core.containers


All container widgets

There are two container widgets at the window level: `Tk` and `Toplevel`. `Tk`
is generally used for the main window, while `Toplevel` is a pop-up window.

There are two container widgets at the canvas level: `Canvas` and `Frame`.
`Canvas` is the main widget carrier in tkintertools, and `Frame` is similar to
`Canvas`, but with a different default color. `Frame` is generally used for
layout.


## 🟢 类

### <big>`Canvas`</big>



<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code> | `Canvas`


```python
def __init__(
    self,
    master: Tk | Canvas,
    *,
    expand: typing.Literal['', 'x', 'y', 'xy'] = 'xy',
    zoom_item: bool = False,
    keep_ratio: typing.Optional[typing.Literal['min', 'max']] = None,
    free_anchor: bool = False,
    name: str | None = None,
    **kwargs,
) -> None: ...
```

Scalable Canvas

The parent widget of all virtual widgets of tkintertools is `Canvas`


* `master`: parent widget
* `expand`: the mode of expand, `x` is horizontal, and `y` is vertical
* `zoom_item`: whether or not to scale its items
* `keep_ratio`: the mode of aspect ratio, `min` follows the minimum
value, `max` follows the maximum value
* `free_anchor`: whether the anchor point is free-floating
* `kwargs`: compatible with other parameters of class `tkinter.Canvas`


#### <big>`_click`</big>


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _click(
    self,
    event: Event,
    type_: typing.Literal['left', 'center', 'right'],
) -> None: ...
```
Events to active the mouse

#### <big>`_copy`</big>


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _copy(
    self,
    event: Event,
) -> None: ...
```
Event for copy operation

#### <big>`_cut`</big>


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _cut(
    self,
    event: Event,
) -> None: ...
```
Event for cut operation

#### <big>`_initialization`</big>


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _initialization(
    self,
) -> None: ...
```
Initialization of size data

#### <big>`_input`</big>


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _input(
    self,
    event: Event,
) -> None: ...
```
Event for typing

#### <big>`_move`</big>


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _move(
    self,
    event: Event,
    type_: typing.Literal['left', 'center', 'right', 'none'],
) -> None: ...
```
Internal Method: Events to move the mouse

#### <big>`_paste`</big>


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _paste(
    self,
    event: Event,
) -> None: ...
```
Event for paste operation

#### <big>`_re_place`</big>


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _re_place(
    self,
) -> None: ...
```

Resize and position the `Canvas` based on the relevant parameters

WARNING:

This method only works for Canvas with Place layout


#### <big>`_release`</big>


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _release(
    self,
    event: Event,
    type_: typing.Literal['left', 'center', 'right'],
) -> None: ...
```
Events to release the mouse

#### <big>`_select_all`</big>


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _select_all(
    self,
    event: Event,
) -> None: ...
```
Event for operation of selecting all

#### <big>`_theme`</big>


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _theme(
    self,
    dark: bool,
) -> None: ...
```

Change the color theme of the Canvas and its items

* `dark`: whether it is in dark mode


#### <big>`_wheel`</big>


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _wheel(
    self,
    event: Event,
    type_: typing.Optional[typing.Literal['up', 'down']] = None,
) -> None: ...
```
Events to scroll the mouse wheel

#### <big>`_zoom_children`</big>


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _zoom_children(
    self,
    relative_ratio: tuple[float, float],
) -> None: ...
```
Experimental: Scale the tkinter Widgets

#### <big>`_zoom_self`</big>


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _zoom_self(
    self,
) -> None: ...
```
Scale the `Canvas` itself

#### <big>`clear`</big>


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def clear(
    self,
) -> None: ...
```
Clear all things in the Canvas

#### <big>`create_text`</big>


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def create_text(
    self,
    x: float,
    y: float,
    /,
    **kwargs,
) -> int: ...
```


#### <big>`destroy`</big>


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def destroy(
    self,
) -> None: ...
```




### <big>`Frame`</big>



<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code> | `Canvas`


```python
def __init__(
    self,
    master: Tk | Canvas | Frame,
    *,
    expand: typing.Literal['', 'x', 'y', 'xy'] = 'xy',
    zoom_item: bool = False,
    keep_ratio: typing.Optional[typing.Literal['min', 'max']] = None,
    free_anchor: bool = False,
    name: str | None = None,
    **kwargs,
) -> None: ...
```
A frame for auxiliary layouts

* `master`: parent widget
* `expand`: the mode of expand, `x` is horizontal, and `y` is vertical
* `zoom_item`: whether or not to scale its items
* `keep_ratio`: the mode of aspect ratio, `min` follows the minimum
value, `max` follows the maximum value
* `free_anchor`: whether the anchor point is free-floating
* `kwargs`: compatible with other parameters of class `tkinter.Canvas`




### <big>`Tk`</big>



<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code> | `Tk`


```python
def __init__(
    self,
    size: tuple[int, int] = (1280, 720),
    position: tuple[int, int] | None = None,
    *,
    title: str = '',
    **kwargs,
) -> None: ...
```

Main window

In general, there is only one main window


* `size`: the size of the window, default value is 1280x720(px)
* `position`: the position of the window, default value indicates that
the location is random
* `title`: the title of the window, default value is an empty string
* `**kwargs`: compatible with other parameters of class `tkinter.Tk`


#### <big>`_fixed_theme`</big>


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _fixed_theme(
    method,
) -> _empty: ...
```

This is a decorator that to fix a problem that some methods cause the
window to lose its theme

* `method`: the method of being decorated


#### <big>`_theme`</big>


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _theme(
    self,
    dark: bool,
    *,
    include_children: bool = True,
    include_canvases: bool = True,
) -> None: ...
```

Change the color theme of the window

* `dark`: whether it is in dark mode
* `include_children`: wether include its children, like Toplevel
* `include_canvases`: wether include its canvases


#### <big>`_wrap_method`</big>


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _wrap_method(
    self,
    method_name: str,
) -> None: ...
```
Some problems can be fixed by decorating the original method

#### <big>`_zoom`</big>


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _zoom(
    self,
) -> None: ...
```
Zoom contents of the window

#### <big>`alpha`</big>


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def alpha(
    self,
    value: float | None = None,
) -> float | None: ...
```

Set or get the transparency of the window

* `value`: the transparency of the window, range is 0~1


#### <big>`center`</big>


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def center(
    self,
    master: tkinter.Misc | None = None,
) -> None: ...
```

Center the widget

`master`: The area of the reference widget, if it is None,
means that the reference area is the entire screen


#### <big>`fullscreen`</big>


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def fullscreen(
    self,
    value: bool | None = True,
) -> bool | None: ...
```

Set or get whether the window is full-screen

* `value`: indicate whether the window is full-screen

TIPS:

The method should be called at the end of the code,
or after some time after the program has started


#### <big>`geometry`</big>


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def geometry(
    self,
    *,
    size: tuple[int, int] | None = None,
    position: tuple[int, int] | None = None,
) -> tuple[int, int, int, int] | None: ...
```

Change the size and position of the window and return the current size
and position of the window

* `size`: the size of the window, if it is None, does not change
anything
* `position`: the position of the window, if it is None, does not
change anything

TIPS:

If you want to use `tkinter.Tk.geometry`, please use
`tkinter.Tk.wm_geometry` instead

CAUTION:

This method causes the event `<configure>` to be triggered


#### <big>`shutdown`</big>


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def shutdown(
    self,
    command: typing.Optional[typing.Callable],
    ensure_destroy: bool = False,
    *args,
    **kwargs,
) -> None: ...
```

Set a function that will be called when the window is closed

* `command`: the function that was called
* `ensure_destroy`: whether the window is guaranteed to be closed
* `args`: the variable-length argument of the called function
* `kwargs`: the keyword argument of the function being called

TIPS:

Regardless of whether the function is successfully called or not,
the window will still close gracefully


#### <big>`toolwindow`</big>


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def toolwindow(
    self,
    value: bool | None = True,
) -> bool | None: ...
```

Set or get whether the window is tool-window

* `value`: indicate whether the window is tool-window


#### <big>`topmost`</big>


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def topmost(
    self,
    value: bool | None = True,
) -> bool | None: ...
```

Set or get whether the window is pinned or not

* `value`: indicate whether the window is topmost


#### <big>`transparentcolor`</big>


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def transparentcolor(
    self,
    value: str | None = None,
) -> str | None: ...
```

Set or get the penetration color of the window

* `value`: the penetration color of the window




### <big>`Toplevel`</big>



<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code> | `Toplevel` `Tk`


```python
def __init__(
    self,
    master: tkintertools.core.containers.Tk | None = None,
    size: tuple[int, int] = (960, 540),
    position: tuple[int, int] | None = None,
    *,
    title: str | None = None,
    grab: bool = False,
    focus: bool = True,
    **kwargs,
) -> None: ...
```

Toplevel window

It can be used as a pop-up window,
or it can be customized to put anything you want to show in it


* `master`: parent widget
* `size`: the size of the window, default value is 960x540(px)
* `position`: the position of the window, default value indicates that
the location is random
* `title`: title of window, default is the same as title of master
* `grab`: set grab for this window
* `focus`: whether direct input focus to this window
* `**kwargs`: compatible with other parameters of class
`tkinter.Toplevel`


#### <big>`destroy`</big>


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def destroy(
    self,
) -> None: ...
```




