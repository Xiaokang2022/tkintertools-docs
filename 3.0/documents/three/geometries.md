# tkintertools.three.geometries

Standard Geometries

## 🟢 Classes / 类

### <big>`Cuboid`</big>



<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code> | `Geometry`


```python
def __init__(
    self,
    canvas: tkintertools.three.engine.Canvas | tkintertools.three.engine.Space,
    x: float,
    y: float,
    z: float,
    length: float,
    width: float,
    height: float,
    *,
    boardwidth: int = 1,
    color_fill_up: str = '',
    color_fill_down: str = '',
    color_fill_left: str = '',
    color_fill_right: str = '',
    color_fill_front: str = '',
    color_fill_back: str = '',
    color_outline_up: str = '#000000',
    color_outline_down: str = '#000000',
    color_outline_left: str = '#000000',
    color_outline_right: str = '#000000',
    color_outline_front: str = '#000000',
    color_outline_back: str = '#000000',
) -> None: ...
```
Cuboid




### <big>`Tetrahedron`</big>



<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code> | `Geometry`


```python
def __init__(
    self,
    canvas: tkintertools.three.engine.Canvas | tkintertools.three.engine.Space,
    point_1: tuple[float, float, float],
    point_2: tuple[float, float, float],
    point_3: tuple[float, float, float],
    point_4: tuple[float, float, float],
    *,
    boardwidth: int = 1,
    color_fill: tuple[str, str, str, str] = ('', '', '', ''),
    color_outline: tuple[str, str, str, str] = ('#000000', '#000000', '#000000', '#000000'),
) -> None: ...
```
Tetrahedron



