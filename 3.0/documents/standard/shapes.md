# tkintertools.standard.shapes

All standard Shapes

## 🟢 Classes / 类

### HalfRoundedRectangle


<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code>


```python
def __init__(
    self,
    widget: Widget,
    relative_position: tuple[int, int] = (0, 0),
    size: tuple[int, int] | None = None,
    *,
    radius: int = 5,
    ignore: typing.Literal['left', 'right'] = 'left',
    name: str | None = None,
    animation: bool = True,
    styles: dict[str, dict[str, str]] | None = None,
    **kwargs,
) -> None: ...
```
Create a half rounded rectangle for a widget

* `widget`: parent widget
* `relative_position`: position relative to its widgets
* `size`: size of component
* `radius`: radius of the fillet
* `ignore`: edges to ignore
* `name`: name of component
* `animation`: Wether use animation to change color
* `styles`: style dict of component
* `kwargs`: extra parameters for CanvasItem


#### coords

<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def coords(
    self,
    size: tuple[float, float] | None = None,
    position: tuple[float, float] | None = None,
) -> None: ...
```


#### display

<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def display(
    self,
) -> None: ...
```




### Line


<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code>


```python
def __init__(
    self,
    widget: Widget,
    relative_position: tuple[int, int] = (0, 0),
    size: tuple[int, int] | None = None,
    *,
    points: list[tuple[float, float]] = [],
    name: str | None = None,
    animation: bool = True,
    styles: dict[str | int, dict[str | int, dict[str, str]]] | None = None,
    **kwargs,
) -> None: ...
```
Create a line for a widget

* `widget`: parent widget
* `relative_position`: position relative to its widgets
* `size`: size of component
* `points`: key points of line
* `name`: name of component
* `animation`: Wether use animation to change color
* `styles`: style dict of component
* `kwargs`: extra parameters for CanvasItem


#### coords

<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def coords(
    self,
    size: tuple[float, float] | None = None,
    position: tuple[float, float] | None = None,
) -> None: ...
```


#### display

<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def display(
    self,
) -> None: ...
```




### Oval


<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code>

#### coords

<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def coords(
    self,
    size: tuple[float, float] | None = None,
    position: tuple[float, float] | None = None,
) -> None: ...
```


#### detect

<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def detect(
    self,
    x: int,
    y: int,
) -> bool: ...
```


#### display

<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def display(
    self,
) -> None: ...
```




### Parallelogram


<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code>


```python
def __init__(
    self,
    widget: Widget,
    relative_position: tuple[int, int] = (0, 0),
    size: tuple[int, int] | None = None,
    *,
    theta: float = 0.5235987755982988,
    name: str | None = None,
    animation: bool = True,
    styles: dict[str, dict[str, str]] | None = None,
    **kwargs,
) -> None: ...
```
Create a parallelogram for a widget

* `widget`: parent widget
* `relative_position`: position relative to its widgets
* `size`: size of component
* `theta`: number of radians that the parallelogram is inclined to
* `name`: name of component
* `animation`: Wether use animation to change color
* `styles`: style dict of component
* `kwargs`: extra parameters for CanvasItem


#### coords

<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def coords(
    self,
    size: tuple[float, float] | None = None,
    position: tuple[float, float] | None = None,
) -> None: ...
```


#### display

<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def display(
    self,
) -> None: ...
```




### Rectangle


<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code>

#### coords

<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def coords(
    self,
    size: tuple[float, float] | None = None,
    position: tuple[float, float] | None = None,
) -> None: ...
```


#### display

<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def display(
    self,
) -> None: ...
```




### RegularPolygon


<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code>


```python
def __init__(
    self,
    widget: Widget,
    relative_position: tuple[int, int] = (0, 0),
    size: tuple[int, int] | None = None,
    *,
    side: int = 3,
    angle: float = 0,
    name: str | None = None,
    animation: bool = True,
    styles: dict[str, dict[str, str]] | None = None,
    **kwargs,
) -> None: ...
```
Create a regular polygon for a widget

* `widget`: parent widget
* `relative_position`: position relative to its widgets
* `size`: size of component
* `side`: number of sides of a regular polygon
* `angle`: number of radians of a regular polygon rotated clockwise
* `name`: name of component
* `animation`: Wether use animation to change color
* `styles`: style dict of component
* `kwargs`: extra parameters for CanvasItem


#### coords

<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def coords(
    self,
    size: tuple[float, float] | None = None,
    position: tuple[float, float] | None = None,
) -> None: ...
```


#### display

<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def display(
    self,
) -> None: ...
```




### RoundedRectangle


<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code>


```python
def __init__(
    self,
    widget: Widget,
    relative_position: tuple[int, int] = (0, 0),
    size: tuple[int, int] | None = None,
    *,
    radius: int = 5,
    name: str | None = None,
    animation: bool = True,
    styles: dict[str, dict[str, str]] | None = None,
    **kwargs,
) -> None: ...
```
Create a rounded rectangle for a widget

* `widget`: parent widget
* `relative_position`: position relative to its widgets
* `size`: size of component
* `radius`: radius of the fillet
* `name`: name of component
* `animation`: Wether use animation to change color
* `styles`: style dict of component
* `kwargs`: extra parameters for CanvasItem


#### coords

<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def coords(
    self,
    size: tuple[float, float] | None = None,
    position: tuple[float, float] | None = None,
) -> None: ...
```


#### display

<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def display(
    self,
) -> None: ...
```




### SemicircularRectangle


<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code>

#### coords

<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def coords(
    self,
    size: tuple[float, float] | None = None,
    position: tuple[float, float] | None = None,
) -> None: ...
```


#### detect

<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def detect(
    self,
    x: int,
    y: int,
) -> bool: ...
```


#### display

<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def display(
    self,
) -> None: ...
```




### SharpRectangle


<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code>


```python
def __init__(
    self,
    widget: Widget,
    relative_position: tuple[int, int] = (0, 0),
    size: tuple[int, int] | None = None,
    *,
    theta: float = 0.5235987755982988,
    ratio: tuple[float, float] = (0.5, 0.5),
    name: str | None = None,
    animation: bool = True,
    styles: dict[str, dict[str, str]] | None = None,
    **kwargs,
) -> None: ...
```
Create a sharp rectangle for a widget

* `widget`: parent widget
* `relative_position`: position relative to its widgets
* `size`: size of component
* `theta`: number of radians of sharp corners
* `ratio`: height ratio of the left and right sharp corners
* `name`: name of component
* `animation`: Wether use animation to change color
* `styles`: style dict of component
* `kwargs`: extra parameters for CanvasItem


#### coords

<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def coords(
    self,
    size: tuple[float, float] | None = None,
    position: tuple[float, float] | None = None,
) -> None: ...
```


#### display

<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def display(
    self,
) -> None: ...
```




