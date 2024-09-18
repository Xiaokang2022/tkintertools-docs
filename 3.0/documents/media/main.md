# tkintertools.media.main

APIs for playing videos

## 🟢`VideoCanvas`



<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code> | `Canvas`


```python
def __init__(
    self,
    master: tkintertools.core.containers.Tk             | tkintertools.core.containers.Canvas,
    *,
    control: bool = False,
    auto_play: bool = False,
    click_pause: bool = True,
    expand: typing.Literal['', 'x', 'y', 'xy'] = 'xy',
    zoom_item: bool = True,
    keep_ratio: typing.Optional[typing.Literal['min', 'max']] = None,
    free_anchor: bool = False,
    name: str = 'Canvas',
    **kwargs,
) -> None: ...
```
A canvas that is scalable and playable for videos

* `master`: parent widget
* `control`: whether to enable the built-in UI
* `auto_play`: whether to start playing the video automatically
* `click_pause`: whether to pause when clicked
* `expand`: the mode of expand, `x` is horizontal, and `y` is vertical
* `zoom_item`: whether or not to scale its items
* `keep_ratio`: the mode of aspect ratio, `min` follows the minimum
value, `max` follows the maximum value
* `free_anchor`: whether the anchor point is free-floating
* `kwargs`: compatible with other parameters of class `tkinter.Canvas`


### 🟡`_an`


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _an(
    self,
    up: bool,
) -> None: ...
```
Animation for bottom bar

### 🟡`_control_ui`


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _control_ui(
    self,
) -> None: ...
```
UI for bottom bar

### 🟡`_initialization`


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _initialization(
    self,
) -> None: ...
```


### 🟡`_re_place`


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _re_place(
    self,
) -> None: ...
```


### 🟡`_refresh`


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _refresh(
    self,
) -> None: ...
```
Refresh the canvas

### 🟡`_tiem_convert`


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _tiem_convert(
    self,
    t: float,
) -> str: ...
```
Convert seconds to a special format

### 🟡`play`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def play(
    self,
    file: str,
) -> None: ...
```
Play the video



