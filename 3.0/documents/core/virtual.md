# tkintertools.core.virtual


Various virtual classes

The virtual `Widget` consists of 5 parts, which are `Widget`, `Shape`, `Text`,
`Image` and `Feature`.

Where `Feature` is the function of widgets, and each widget can be bound to up
to one, but in terms of appearance, there is no limit to the number of `Shape`,
`Text`, and `Image`.

`Shape`, `Text`, and `Image` are all appearance components that inherit from
abstract base class `Components`.


## 🟢`Component`



<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code> | `ABC`


```python
def __init__(
    self,
    widget: Widget,
    relative_position: tuple[int, int] = (0, 0),
    size: tuple[int, int] | None = None,
    *,
    name: str | None = None,
    animation: bool = True,
    styles: dict[str, dict[str, str]] | None = None,
    **kwargs,
) -> None: ...
```
The basic part of a `Widget`

* `widget`: parent widget
* `relative_position`: position relative to its widgets
* `size`: size of component
* `name`: name of component
* `animation`: Wether use animation to change color
* `styles`: style dict of component
* `kwargs`: extra parameters for CanvasItem


### 🟡`__getitem__`


<code style='color: #BBBB00;'>method</code> <code style='color: purple;'>special</code>

```python
def __getitem__(
    self,
    key: str,
) -> dict[str, str]: ...
```
Easy to get style data

### 🟡`__setitem__`


<code style='color: #BBBB00;'>method</code> <code style='color: purple;'>special</code>

```python
def __setitem__(
    self,
    key: str,
    value: dict[str, str],
) -> None: ...
```
Easy to set style data

### 🟡`_get_disabled_style`


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _get_disabled_style(
    self,
    refer_state: str | None = None,
) -> dict[str, str]: ...
```
Get the style data of disabled state

### 🟡`appear`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def appear(
    self,
    *,
    no_delay: bool = True,
) -> None: ...
```
Let the component to appear

### 🟡`center`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def center(
    self,
) -> tuple[int, int]: ...
```
Return the geometric center of the `Component`

### 🟡`configure`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def configure(
    self,
    style: dict[str, str],
    *,
    no_delay: bool = False,
) -> None: ...
```
Configure properties of `Component` and update them immediately

### 🟡`coords`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def coords(
    self,
    size: tuple[float, float] | None = None,
    position: tuple[float, float] | None = None,
) -> None: ...
```
Resize the `Component`

### 🟡`destroy`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def destroy(
    self,
) -> None: ...
```
Destroy the `Component`

### 🟡`detect`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def detect(
    self,
    x: int,
    y: int,
) -> bool: ...
```
Detect whether the specified coordinates are within `Component`

### 🟡`disappear`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def disappear(
    self,
    *,
    no_delay: bool = True,
) -> None: ...
```
Let the component to disappear

### 🟡`display`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def display(
    self,
) -> None: ...
```
Display the `Component` on a `Canvas`

### 🟡`move`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def move(
    self,
    dx: float,
    dy: float,
) -> None: ...
```
Move the `Component`

### 🟡`moveto`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def moveto(
    self,
    x: float,
    y: float,
) -> None: ...
```
Move the `Component` to a certain position

### 🟡`region`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def region(
    self,
) -> tuple[int, int, int, int]: ...
```
Return the decision region of the `Component`

### 🟡`update`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def update(
    self,
    state: str | None = None,
    *,
    no_delay: bool = False,
) -> None: ...
```

Update the style of the `Component` to the corresponding state

* `state`: the state of the `Component`


### 🟡`zoom`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def zoom(
    self,
    ratios: tuple[float, float],
) -> None: ...
```
Zoom the `Component`



## 🟢`Feature`



<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code> | `ABC`


```python
def __init__(
    self,
    widget: Widget,
) -> None: ...
```
The features of a `Widget`

* `widget`: parent widget


### 🟡`_click_center`


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _click_center(
    self,
    event: Event,
) -> bool: ...
```
Event of pressing the center mouse button

### 🟡`_click_left`


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _click_left(
    self,
    event: Event,
) -> bool: ...
```
Event of pressing the left mouse button

### 🟡`_click_right`


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _click_right(
    self,
    event: Event,
) -> bool: ...
```
Event of pressing the right mouse button

### 🟡`_copy`


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _copy(
    self,
    event: Event,
) -> bool: ...
```
Event of copy operation

### 🟡`_cut`


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _cut(
    self,
    event: Event,
) -> bool: ...
```
Event of cut operation

### 🟡`_input`


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _input(
    self,
    event: Event,
) -> bool: ...
```
Event of typing

### 🟡`_move_center`


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _move_center(
    self,
    event: Event,
) -> bool: ...
```
Event of holding down the center mouse button to move the mouse

### 🟡`_move_left`


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _move_left(
    self,
    event: Event,
) -> bool: ...
```
Event of holding down the left mouse button to move the mouse

### 🟡`_move_none`


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _move_none(
    self,
    event: Event,
) -> bool: ...
```
Event of moving the mouse

### 🟡`_move_right`


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _move_right(
    self,
    event: Event,
) -> bool: ...
```
Event of holding down the right mouse button to move the mouse

### 🟡`_paste`


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _paste(
    self,
    event: Event,
) -> bool: ...
```
Event of paste operation

### 🟡`_release_center`


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _release_center(
    self,
    event: Event,
) -> bool: ...
```
Event of releasing the center mouse button

### 🟡`_release_left`


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _release_left(
    self,
    event: Event,
) -> bool: ...
```
Event of releasing the left mouse button

### 🟡`_release_right`


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _release_right(
    self,
    event: Event,
) -> bool: ...
```
Event of releasing the right mouse button

### 🟡`_select_all`


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _select_all(
    self,
    event: Event,
) -> bool: ...
```
Event of selecting all operation

### 🟡`_wheel`


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _wheel(
    self,
    event: Event,
) -> bool: ...
```
Event of scrolling the mouse wheel



## 🟢`Image`



<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code> | `Component`


```python
def __init__(
    self,
    widget: Widget,
    relative_position: tuple[int, int] = (0, 0),
    size: tuple[int, int] | None = None,
    *,
    image: tkintertools.toolbox.enhanced.PhotoImage | None = None,
    name: str | None = None,
    animation: bool = True,
    styles: dict[str, dict[str, str]] | None = None,
    **kwargs,
) -> None: ...
```
The Image of a `Widget`

* `widget`: parent widget
* `relative_position`: position relative to its widgets
* `size`: size of component
* `image`: image object of the component
* `name`: name of component
* `animation`: Wether use animation to change color
* `styles`: style dict of component
* `kwargs`: extra parameters for CanvasItem


### 🟡`zoom`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def zoom(
    self,
    ratios: tuple[float, float],
) -> None: ...
```
Scale the image



## 🟢`Shape`



<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code> | `Component`

### 🟡`zoom`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def zoom(
    self,
    ratios: tuple[float, float],
) -> None: ...
```
Scale the shape



## 🟢`Text`



<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code> | `Component`


```python
def __init__(
    self,
    widget: Widget,
    relative_position: tuple[int, int] = (0, 0),
    size: tuple[int, int] | None = None,
    *,
    text: str = '',
    limit: int = inf,
    show: str | None = None,
    placeholder: str = '',
    anchor: typing.Literal['n', 'e', 'w', 's', 'nw', 'ne', 'sw', 'se', 'center'] = 'center',
    justify: typing.Literal['left', 'center', 'right'] = 'left',
    family: str | None = None,
    fontsize: int | None = None,
    weight: typing.Literal['normal', 'bold'] = 'normal',
    slant: typing.Literal['roman', 'italic'] = 'roman',
    underline: bool = False,
    overstrike: bool = False,
    name: str | None = None,
    animation: bool = True,
    styles: dict[str, dict[str, str]] | None = None,
    **kwargs,
) -> None: ...
```
The Text of a `Widget`

* `widget`: parent widget
* `relative_position`: position relative to its widgets
* `size`: size of component
* `text`: text value
* `family`: font family
* `fontsize`: font size
* `weight`: weight of the font
* `slant`: slant of the font
* `underline`: wether text is underline
* `overstrike`: wether text is overstrike
* `justify`: justify of the text
* `anchor`: anchor of the text
* `limit`: limit on the number of characters
* `show`: display a value that obscures the original content
* `placeholder`: a placeholder for the prompt
* `name`: name of component
* `animation`: Wether use animation to change color
* `styles`: style dict of component
* `kwargs`: extra parameters for CanvasItem


### 🟡`region`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def region(
    self,
) -> tuple[int, int, int, int]: ...
```
Return the decision region of the `Text`

### 🟡`zoom`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def zoom(
    self,
    ratios: tuple[float, float],
) -> None: ...
```
Scale the text



## 🟢`Widget`



<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code> | `object`


```python
def __init__(
    self,
    master: containers.Canvas | Widget,
    position: tuple[int, int] = (0, 0),
    size: tuple[int, int] | None = None,
    *,
    name: str | None = None,
    state: str = 'normal',
    through: bool = False,
    animation: bool = True,
) -> None: ...
```

Base Widget Class

`Widget` = `Shape` + `Text` + `Image` + `Feature` + `Widget`


* `master`: parent canvas
* `position`: position of the widget
* `size`: size of the widget
* `name`: name of the widget
* `state`: default state of the widget
* `through`: wether detect another widget under the widget
* `animation`: wether enable animation


### 🟡`appear`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def appear(
    self,
) -> None: ...
```
Let all components of the widget to appear

### 🟡`deregister`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def deregister(
    self,
    component: <class 'tkintertools.core.virtual.Component'>,
) -> None: ...
```
Deregister a component from the widget

### 🟡`destroy`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def destroy(
    self,
) -> None: ...
```
Destroy the widget

### 🟡`detect`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def detect(
    self,
    x: int,
    y: int,
) -> bool: ...
```
Detect whether the specified coordinates are within the `Widget`

### 🟡`disabled`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def disabled(
    self,
    value: bool = True,
) -> None: ...
```
Disable the widget

### 🟡`disappear`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def disappear(
    self,
) -> None: ...
```
Let all components of the widget to disappear

### 🟡`move`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def move(
    self,
    dx: int,
    dy: int,
) -> None: ...
```
Move the widget

### 🟡`moveto`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def moveto(
    self,
    x: int,
    y: int,
) -> None: ...
```
Move the Widget to a certain position

### 🟡`register`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def register(
    self,
    component: <class 'tkintertools.core.virtual.Component'>,
) -> None: ...
```
Register a component to the widget

### 🟡`update`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def update(
    self,
    state: str | None = None,
    *,
    no_delay: bool = False,
) -> None: ...
```
Update the widget

### 🟡`zoom`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def zoom(
    self,
    ratios: tuple[float, float] | None = None,
) -> None: ...
```
Zoom self



