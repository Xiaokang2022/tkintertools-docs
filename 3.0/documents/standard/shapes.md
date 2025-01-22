# maliang.standard.shapes

<small>:octicons-mark-github-16: 源代码：[`maliang/standard/shapes.py`](https://github.com/Xiaokang2022/maliang/blob/3.0.0rc6/maliang/standard/shapes.py){ target='_blank' }</small>

All standard `Shape` classes

## 🟢`Arc`



<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code> | `Shape`

### 🟡`coords`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def coords(
    self,
    size: tuple[float, float] | None = None,
    position: tuple[float, float] | None = None,
) -> None: ...
```
Resize the `Element`

### 🟡`display`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def display(
    self,
) -> None: ...
```
Display the `Element` on a `Canvas`



## 🟢`HalfRoundedRectangle`



<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code> | `Shape`


```python
def __init__(
    self,
    widget: virtual.Widget,
    relative_position: tuple[int, int] = (0, 0),
    size: tuple[int, int] | None = None,
    *,
    radius: int = 5,
    ignore: typing.Literal['left', 'right'] = 'left',
    name: str | None = None,
    gradient_animation: bool = True,
    **kwargs,
) -> None: ...
```
Create a half rounded rectangle for a widget

* `widget`: parent widget
* `relative_position`: position relative to its widgets
* `size`: size of element
* `radius`: radius of the fillet
* `ignore`: edges to ignore
* `name`: name of element
* `gradient_animation`: Wether use animation to change color
* `kwargs`: extra parameters for CanvasItem


### 🟡`coords`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def coords(
    self,
    size: tuple[float, float] | None = None,
    position: tuple[float, float] | None = None,
) -> None: ...
```
Resize the `Element`

### 🟡`display`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def display(
    self,
) -> None: ...
```
Display the `Element` on a `Canvas`



## 🟢`Line`



<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code> | `Shape`


```python
def __init__(
    self,
    widget: virtual.Widget,
    relative_position: tuple[int, int] = (0, 0),
    size: tuple[int, int] | None = None,
    *,
    points: list[tuple[float, float]] | None = None,
    name: str | None = None,
    gradient_animation: bool = True,
    **kwargs,
) -> None: ...
```
Create a line for a widget

* `widget`: parent widget
* `relative_position`: position relative to its widgets
* `size`: size of element
* `points`: key points of line
* `name`: name of element
* `gradient_animation`: Wether use animation to change color
* `kwargs`: extra parameters for CanvasItem


### 🟡`coords`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def coords(
    self,
    size: tuple[float, float] | None = None,
    position: tuple[float, float] | None = None,
) -> None: ...
```
Resize the `Element`

### 🟡`display`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def display(
    self,
) -> None: ...
```
Display the `Element` on a `Canvas`



## 🟢`Oval`



<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code> | `Shape`

### 🟡`coords`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def coords(
    self,
    size: tuple[float, float] | None = None,
    position: tuple[float, float] | None = None,
) -> None: ...
```
Resize the `Element`

### 🟡`detect`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def detect(
    self,
    x: int,
    y: int,
) -> bool: ...
```
Detect whether the specified coordinates are within `Element`

### 🟡`display`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def display(
    self,
) -> None: ...
```
Display the `Element` on a `Canvas`



## 🟢`Parallelogram`



<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code> | `Shape`


```python
def __init__(
    self,
    widget: virtual.Widget,
    relative_position: tuple[int, int] = (0, 0),
    size: tuple[int, int] | None = None,
    *,
    theta: float = 0.5235987755982988,
    name: str | None = None,
    gradient_animation: bool = True,
    **kwargs,
) -> None: ...
```
Create a parallelogram for a widget

* `widget`: parent widget
* `relative_position`: position relative to its widgets
* `size`: size of element
* `theta`: number of radians that the parallelogram is inclined to
* `name`: name of element
* `gradient_animation`: Wether use animation to change color
* `kwargs`: extra parameters for CanvasItem


### 🟡`coords`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def coords(
    self,
    size: tuple[float, float] | None = None,
    position: tuple[float, float] | None = None,
) -> None: ...
```
Resize the `Element`

### 🟡`display`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def display(
    self,
) -> None: ...
```
Display the `Element` on a `Canvas`



## 🟢`Rectangle`



<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code> | `Shape`

### 🟡`coords`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def coords(
    self,
    size: tuple[float, float] | None = None,
    position: tuple[float, float] | None = None,
) -> None: ...
```
Resize the `Element`

### 🟡`display`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def display(
    self,
) -> None: ...
```
Display the `Element` on a `Canvas`



## 🟢`RegularPolygon`



<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code> | `Shape`


```python
def __init__(
    self,
    widget: virtual.Widget,
    relative_position: tuple[int, int] = (0, 0),
    size: tuple[int, int] | None = None,
    *,
    side: int = 3,
    angle: float = 0,
    name: str | None = None,
    gradient_animation: bool = True,
    **kwargs,
) -> None: ...
```
Create a regular polygon for a widget

* `widget`: parent widget
* `relative_position`: position relative to its widgets
* `size`: size of element
* `side`: number of sides of a regular polygon
* `angle`: number of radians of a regular polygon rotated clockwise
* `name`: name of element
* `gradient_animation`: Wether use animation to change color
* `kwargs`: extra parameters for CanvasItem


### 🟡`coords`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def coords(
    self,
    size: tuple[float, float] | None = None,
    position: tuple[float, float] | None = None,
) -> None: ...
```
Resize the `Element`

### 🟡`display`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def display(
    self,
) -> None: ...
```
Display the `Element` on a `Canvas`



## 🟢`RoundedRectangle`



<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code> | `Shape`


```python
def __init__(
    self,
    widget: virtual.Widget,
    relative_position: tuple[int, int] = (0, 0),
    size: tuple[int, int] | None = None,
    *,
    radius: int = 5,
    name: str | None = None,
    gradient_animation: bool = True,
    **kwargs,
) -> None: ...
```
Create a rounded rectangle for a widget

* `widget`: parent widget
* `relative_position`: position relative to its widgets
* `size`: size of element
* `radius`: radius of the fillet
* `name`: name of element
* `gradient_animation`: Wether use animation to change color
* `kwargs`: extra parameters for CanvasItem


### 🟡`coords`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def coords(
    self,
    size: tuple[float, float] | None = None,
    position: tuple[float, float] | None = None,
) -> None: ...
```
Resize the `Element`

### 🟡`display`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def display(
    self,
) -> None: ...
```
Display the `Element` on a `Canvas`



## 🟢`SemicircularRectangle`



<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code> | `Shape`

### 🟡`coords`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def coords(
    self,
    size: tuple[float, float] | None = None,
    position: tuple[float, float] | None = None,
) -> None: ...
```
Resize the `Element`

### 🟡`detect`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def detect(
    self,
    x: int,
    y: int,
) -> bool: ...
```
Detect whether the specified coordinates are within `Element`

### 🟡`display`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def display(
    self,
) -> None: ...
```
Display the `Element` on a `Canvas`



## 🟢`SharpRectangle`



<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code> | `Shape`


```python
def __init__(
    self,
    widget: virtual.Widget,
    relative_position: tuple[int, int] = (0, 0),
    size: tuple[int, int] | None = None,
    *,
    theta: float = 0.5235987755982988,
    ratio: tuple[float, float] = (0.5, 0.5),
    name: str | None = None,
    gradient_animation: bool = True,
    **kwargs,
) -> None: ...
```
Create a sharp rectangle for a widget

* `widget`: parent widget
* `relative_position`: position relative to its widgets
* `size`: size of element
* `theta`: number of radians of sharp corners
* `ratio`: height ratio of the left and right sharp corners
* `name`: name of element
* `gradient_animation`: Wether use animation to change color
* `kwargs`: extra parameters for CanvasItem


### 🟡`coords`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def coords(
    self,
    size: tuple[float, float] | None = None,
    position: tuple[float, float] | None = None,
) -> None: ...
```
Resize the `Element`

### 🟡`display`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def display(
    self,
) -> None: ...
```
Display the `Element` on a `Canvas`



