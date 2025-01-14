# tkintertools.three.geometries

<small>:octicons-mark-github-16: 源代码：[`tkintertools/three/geometries.py`](https://github.com/Xiaokang2022/tkintertools-3d/blob/1.0.3/tkintertools/three/geometries.py){ target='_blank' }</small>

Standard Geometries

## 🟢`Cuboid`



<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code> | `Geometry`


```python
def __init__(
    self,
    canvas: engine.Canvas | engine.Space,
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




## 🟢`Tetrahedron`



<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code> | `Geometry`


```python
def __init__(
    self,
    canvas: engine.Canvas | engine.Space,
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




