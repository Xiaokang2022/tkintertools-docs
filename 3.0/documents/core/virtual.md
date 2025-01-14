# tkintertools.core.virtual

<small>:octicons-mark-github-16: 源代码：[`tkintertools/core/virtual.py`](https://github.com/Xiaokang2022/tkintertools/blob/3.0.0rc6/tkintertools/core/virtual.py){ target='_blank' }</small>

All virtual classes.

The `virtual.Widget` consists of five parts, which are `Shape`, `Text`, `Image`,
`Style` and `Feature`. In addition, they can be nested within each other.

Where `Feature` is the function of widgets, `Style` control the color of the
widget, and each widget can be bound to up to one `Feature` and one `Style`,
but in terms of appearance, there is no limit to the number of `Shape`, `Text`,
and `Image`.

`Shape`, `Text`, and `Image` are all appearance elements that inherit from
abstract base class `Elements`.


## 🟢`Element`



<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code> | `ABC`


```python
def __init__(
    self,
    widget: Widget,
    position: tuple[int, int] = (0, 0),
    size: tuple[int, int] | None = None,
    *,
    name: str | None = None,
    gradient_animation: bool | None = None,
    **kwargs,
) -> None: ...
```
The basic visible part of a `virtual.Widget`.

* `widget`: parent widget
* `position`: position relative to its widgets
* `size`: size of element
* `name`: name of element
* `gradient_animation`: Wether use animation to change color
* `kwargs`: extra parameters for CanvasItem


### 🟡`center`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def center(
    self,
) -> tuple[float, float]: ...
```
Return the geometric center of the `Element`.

### 🟡`configure`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def configure(
    self,
    style: dict[str, str],
    *,
    gradient_animation: bool = True,
) -> None: ...
```
Configure properties of `Element` and update them immediately.

* `style`: style data
* `gradient_animation`: whether use gradient animation


### 🟡`coords`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def coords(
    self,
    size: tuple[float, float] | None = None,
    position: tuple[float, float] | None = None,
) -> None: ...
```
Resize the `Element`.

* `size`: new size of the element
* `position`: new position of the element


### 🟡`destroy`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def destroy(
    self,
) -> None: ...
```
Destroy the `Element`.

### 🟡`detect`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def detect(
    self,
    x: float,
    y: float,
) -> bool: ...
```
Detect whether the specified coordinates are within `Element`.

* `x`: x-coordinate of the location to be detected
* `y`: y-coordinate of the location to be detected


### 🟡`display`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def display(
    self,
) -> None: ...
```
Display the `Element` on a `Canvas`.

### 🟡`forget`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def forget(
    self,
    value: bool = True,
    *,
    gradient_animation: bool = False,
) -> None: ...
```
Let the element to forget.

* `value`: whether to forget
* `gradient_animation`: whether use gradient animation


### 🟡`move`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def move(
    self,
    dx: float,
    dy: float,
) -> None: ...
```
Move the `Element`.

* `dx`: x-coordinate offset
* `dy`: y-coordinate offset


### 🟡`moveto`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def moveto(
    self,
    x: float,
    y: float,
) -> None: ...
```
Move the `Element` to a certain position.

* `x`: x-coordinate of the target location
* `y`: y-coordinate of the target location


### 🟡`region`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def region(
    self,
) -> tuple[int, int, int, int]: ...
```
Return the decision region of the `Element`.

### 🟡`update`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def update(
    self,
    state: str | None = None,
    *,
    gradient_animation: bool = False,
) -> None: ...
```
Update the style of the `Element` to the corresponding state.

* `state`: the state of the `Element`
* `gradient_animation`: whether use gradient animation


### 🟡`zoom`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def zoom(
    self,
    ratios: tuple[float, float],
    *,
    zoom_position: bool = True,
    zoom_size: bool = True,
) -> None: ...
```
Zoom the `Element`.

* `ratios`: ratios of zooming
* `zoom_position`: whether or not to zoom the location of the element
* `zoom_size`: whether or not to zoom the size of the element




## 🟢`Feature`



<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code> | `object`


```python
def __init__(
    self,
    widget: Widget,
) -> None: ...
```
The features of a `Widget`.

* `widget`: parent widget


### 🟡`_parse_method_name`


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _parse_method_name(
    name: str,
) -> str: ...
```
Parse the name to method name.

* `name`: original name

Example:

* `"<Ctrl-C>"` -> `"_ctrl_c"`
* `"<MouseWheel>"` -> `"_mouse_wheel"`


### 🟡`get_method`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def get_method(
    self,
    name: str,
) -> collections.abc.Callable: ...
```
Return method by name.

* `name`: name of the method




## 🟢`Image`



<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code> | `Element`


```python
def __init__(
    self,
    widget: Widget,
    relative_position: tuple[int, int] = (0, 0),
    size: tuple[int, int] | None = None,
    *,
    image: enhanced.PhotoImage | None = None,
    name: str | None = None,
    gradient_animation: bool = True,
    **kwargs,
) -> None: ...
```
The Image of a `Widget`.

* `widget`: parent widget
* `relative_position`: position relative to its widgets
* `size`: size of element
* `image`: image object of the element
* `name`: name of element
* `gradient_animation`: Wether use animation to change color
* `kwargs`: extra parameters for CanvasItem


### 🟡`region`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def region(
    self,
) -> tuple[int, int, int, int]: ...
```
Return the decision region of the `Image`.

### 🟡`zoom`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def zoom(
    self,
    ratios: tuple[float, float],
    *,
    zoom_position: bool = True,
    zoom_size: bool = True,
) -> None: ...
```
Scale the image.

* `ratios`: ratios of zooming
* `zoom_position`: whether or not to zoom the location of the image
* `zoom_size`: whether or not to zoom the size of the image




## 🟢`Shape`



<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code> | `Element`

### 🟡`zoom`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def zoom(
    self,
    ratios: tuple[float, float],
    *,
    zoom_position: bool = True,
    zoom_size: bool = True,
) -> None: ...
```
Scale the shape.

* `ratios`: ratios of zooming
* `zoom_position`: whether or not to zoom the location of the shape
* `zoom_size`: whether or not to zoom the size of the shape




## 🟢`Style`



<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code> | `object`


```python
def __init__(
    self,
    widget: Widget,
    *,
    auto_update: bool | None = None,
) -> None: ...
```
The styles of a `Widget`.

* `widget`: parent widget
* `auto_update`: whether the theme manager update it automatically


### 🟡`__getitem__`


<code style='color: #BBBB00;'>method</code> <code style='color: purple;'>special</code>

```python
def __getitem__(
    self,
    key: Element | str | int,
) -> dict[str, dict[str, str]]: ...
```


### 🟡`_get_key`


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _get_key(
    self,
    key: Element | str | int,
) -> str: ...
```
Get the key.

* `key`: the object related to the key


### 🟡`_set`


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _set(
    self,
    theme: typing.Literal['light', 'dark'] | None = None,
    data: tuple[str | types.EllipsisType, ...] | str | None = None,
    **kwargs: tuple[Element | str | int, ...] | Element | str | int,
) -> None: ...
```
Set the color of a style conveniently.

* `theme`: the theme name, None indicates both
* `data`: data of color
* `kwargs`: { arg name: element key or element keys tuple }


### 🟡`_wrap_arg`


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _wrap_arg(
    arg: tuple[str | types.EllipsisType | None, ...] | str,
) -> tuple[str | types.EllipsisType | None, ...]: ...
```
Wrap the argument to a tuple.

* `arg`: argument


### 🟡`get`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def get(
    self,
    *,
    theme: typing.Literal['light', 'dark'] | None = None,
) -> dict[str, dict[str, dict[str, str]]]: ...
```
Return the style of the widget.

* `theme`: the theme of the widget, None indicates the current theme


### 🟡`get_disabled_style`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def get_disabled_style(
    self,
    *,
    element: Element,
) -> dict[str, str]: ...
```
Get the style data of disabled state.

* `element`: element that style to be calculated


### 🟡`init`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def init(
    self,
    key: Element | str | int,
    *,
    theme: typing.Literal['light', 'dark'] | None = None,
) -> None: ...
```
Initialize some style of an element.

* `name`: the key of the element
* `theme`: the theme name, None indicates both


### 🟡`reset`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def reset(
    self,
    *,
    theme: typing.Literal['light', 'dark'] | None = None,
) -> None: ...
```
Reset the style of the widget and update.

* `theme`: the theme to be reset, None indicates both


### 🟡`set`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def set(
    self,
) -> None: ...
```
Set the style of the widget.



## 🟢`Text`



<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code> | `Element`


```python
def __init__(
    self,
    widget: Widget,
    relative_position: tuple[int, int] = (0, 0),
    size: tuple[int, int] | None = None,
    *,
    text: str = '',
    limit: int = -1,
    show: str | None = None,
    placeholder: str = '',
    family: str | None = None,
    fontsize: int | None = None,
    weight: typing.Literal['normal', 'bold'] = 'normal',
    slant: typing.Literal['roman', 'italic'] = 'roman',
    underline: bool = False,
    overstrike: bool = False,
    name: str | None = None,
    gradient_animation: bool = True,
    **kwargs,
) -> None: ...
```
The Text of a `Widget`.

* `widget`: parent widget
* `relative_position`: position relative to its widgets
* `size`: size of element
* `text`: text value
* `family`: font family
* `fontsize`: font size
* `weight`: weight of the font
* `slant`: slant of the font
* `underline`: wether text is underline
* `overstrike`: wether text is overstrike
* `limit`: limit on the number of characters
* `show`: display a value that obscures the original content
* `placeholder`: a placeholder for the prompt
* `name`: name of element
* `gradient_animation`: Wether use animation to change color
* `kwargs`: extra parameters for CanvasItem


### 🟡`region`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def region(
    self,
) -> tuple[int, int, int, int]: ...
```
Return the decision region of the `Text`.

### 🟡`zoom`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def zoom(
    self,
    ratios: tuple[float, float],
    *,
    zoom_position: bool = True,
    zoom_size: bool = True,
) -> None: ...
```
Scale the text.

* `ratios`: ratios of zooming
* `zoom_position`: whether or not to zoom the location of the text
* `zoom_size`: whether or not to zoom the size of the text




## 🟢`Widget`



<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code> | `object`


```python
def __init__(
    self,
    master: containers.Canvas | Widget,
    position: tuple[int, int] = (0, 0),
    size: tuple[int, int] | None = None,
    *,
    anchor: typing.Literal['n', 's', 'w', 'e', 'nw', 'ne', 'sw', 'se', 'center'] = 'nw',
    capture_events: bool | None = None,
    gradient_animation: bool | None = None,
    auto_update: bool | None = None,
    style: type[Style] | None = None,
) -> None: ...
```
Base Widget Class.

`Widget` = `Element` + `Style` + `Feature`


* `master`: parent canvas
* `position`: position of the widget
* `size`: size of the widget
* `anchor`: layout anchor of the widget
* `capture_events`: wether detect another widget under the widget
* `gradient_animation`: wether enable animation
* `auto_update`: whether the theme manager update it automatically
* `style`: style of the widget


### 🟡`bind`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def bind(
    self,
    sequence: str,
    command: collections.abc.Callable[[tkinter.Event], typing.Any],
    add: bool | typing.Literal['', '+'] | None = None,
) -> None: ...
```
Bind to this widget at event sequence a call to function command.

* `sequence`: event name
* `command`: callback function
* `add`: if True, original callback function will not be overwritten


### 🟡`bind_on_update`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def bind_on_update(
    self,
    command: collections.abc.Callable[[str, bool], typing.Any],
) -> None: ...
```
Bind an extra function to the widget on update.

This extra function has two positional arguments, both of which are
arguments to the method `update`. And this extra function will be
called when the widget is updated (whether it's automatically updated
or manually updated).

* `command`: the extra function that is bound


### 🟡`deregister_elements`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def deregister_elements(
    self,
    *elements: Element,
) -> None: ...
```
Deregister a element from the widget.

* `elements`: elements to be deregistered


### 🟡`destroy`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def destroy(
    self,
) -> None: ...
```
Destroy the widget.

### 🟡`detect`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def detect(
    self,
    x: float,
    y: float,
) -> bool: ...
```
Detect whether the specified coordinates are within the `Widget`.

* `x`: x-coordinate of the location to be detected
* `y`: y-coordinate of the location to be detected


### 🟡`disable`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def disable(
    self,
    value: bool = True,
) -> None: ...
```
Disable the widget.

* `value`: whether to disable


### 🟡`forget`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def forget(
    self,
    value: bool = True,
) -> None: ...
```
Let all elements of the widget to forget.

* `value`: whether to forget the widget


### 🟡`generate_event`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def generate_event(
    self,
    sequence: str,
    event: tkinter.Event | None = None,
    **kwargs,
) -> None: ...
```
Generate an event sequence. Additional keyword arguments specify
parameter of the event.

* `sequence`: event name
* `event`: event
* `kwargs`: attr of event


### 🟡`move`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def move(
    self,
    dx: float,
    dy: float,
) -> None: ...
```
Move the widget.

* `dx`: x-coordinate offset
* `dy`: y-coordinate offset


### 🟡`moveto`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def moveto(
    self,
    x: float,
    y: float,
) -> None: ...
```
Move the Widget to a certain position.

* `x`: x-coordinate of the target location
* `y`: y-coordinate of the target location


### 🟡`register_elements`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def register_elements(
    self,
    *elements: Element,
) -> None: ...
```
Register elements to the widget.

* `elements`: elements to be registered


### 🟡`unbind`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def unbind(
    self,
    sequence: str,
    command: collections.abc.Callable[[tkinter.Event], typing.Any],
) -> None: ...
```
Unbind for this widget the event sequence.

* `sequence`: event name
* `command`: callback function


### 🟡`unbind_on_update`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def unbind_on_update(
    self,
    command: collections.abc.Callable[[str, bool], typing.Any],
) -> None: ...
```
Unbind an extra function to the widget on update.

* `command`: the extra function that is bound


### 🟡`update`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def update(
    self,
    state: str | None = None,
    *,
    gradient_animation: bool | None = None,
    nested: bool = True,
) -> None: ...
```
Update the widget.

* `state`: state of the widget
* `gradient_animation`: whether use gradient animation
* `nested`: whether nested


### 🟡`zoom`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def zoom(
    self,
    ratios: tuple[float, float] | None = None,
    *,
    zoom_position: bool = True,
    zoom_size: bool = True,
) -> None: ...
```
Zoom widget ifself.

* `ratios`: ratios of zooming
* `zoom_position`: whether or not to zoom the location of the widget
* `zoom_size`: whether or not to zoom the size of the widget




