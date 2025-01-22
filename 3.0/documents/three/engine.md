# maliang.three.engine

<small>:octicons-mark-github-16: 源代码：[`maliang/three/engine.py`](https://github.com/Xiaokang2022/maliang-three/blob/1.0.3/maliang/three/engine.py){ target='_blank' }</small>

Core codes of 3D

## 🟢`Canvas`



<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code> | `Canvas`


```python
def __init__(
    self,
    master: containers.Tk | containers.Toplevel | containers.Canvas | None = None,
    *,
    expand: typing.Literal['', 'x', 'y', 'xy'] = 'xy',
    auto_zoom: bool = False,
    keep_ratio: typing.Literal['min', 'max'] | None = None,
    free_anchor: bool = False,
    **kwargs,
) -> None: ...
```
Base class of 3D Canvas


### 🟡`space_sort`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def space_sort(
    self,
) -> None: ...
```
Sort the contextual relationship between the spatial positions of the components



## 🟢`Component`



<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code> | `object`


```python
def __init__(
    self,
    *coordinates,
) -> _empty: ...
```
3D 对象基类


### 🟡`_project`


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _project(
    self,
    distance,
    canvas = None,
) -> _empty: ...
```
投影对象自身

* `distance`: 对象与观察者的距离
* `canvas`: 投影到的画布


### 🟡`center`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def center(
    self,
) -> _empty: ...
```
几何中心

### 🟡`rotate`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def rotate(
    self,
    dx = 0,
    dy = 0,
    dz = 0,
    *,
    center = (0, 0, 0),
    axis = None,
) -> _empty: ...
```
旋转对象本身

* `dx`: x 方向逆时针旋转弧度，或者绕旋转轴线的旋转弧度
* `dy`: y 方向逆时针旋转弧度
* `dz`: z 方向逆时针旋转弧度
* `center`: 旋转中心，默认为原点
* `axis`: 旋转轴线，无默认值


### 🟡`scale`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def scale(
    self,
    kx = 1,
    ky = 1,
    kz = 1,
    *,
    center = None,
) -> _empty: ...
```
缩放对象本身

* `kx`: x 方向缩放比例
* `ky`: y 方向缩放比例
* `kz`: z 方向缩放比例
* `center`: 缩放中心，默认为几何中心


### 🟡`translate`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def translate(
    self,
    dx = 0,
    dy = 0,
    dz = 0,
) -> _empty: ...
```
平移对象本身

* `dx`: x 方向位移长度
* `dy`: y 方向位移长度
* `dz`: z 方向位移长度


### 🟡`update`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def update(
    self,
) -> None: ...
```
Update



## 🟢`Geometry`



<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code> | `object`


```python
def __init__(
    self,
    canvas,
    *sides,
) -> _empty: ...
```
几何体

* `canvas`: 父画布
* `sides`: 组成几何体的面


### 🟡`append`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def append(
    self,
    *sides,
) -> _empty: ...
```
给几何体添加更多新的面

* `sides`: `Side` 类


### 🟡`center`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def center(
    self,
) -> _empty: ...
```
几何中心

### 🟡`rotate`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def rotate(
    self,
    dx = 0,
    dy = 0,
    dz = 0,
    *,
    center = (0, 0, 0),
    axis = None,
) -> _empty: ...
```
旋转几何体中的所有 3D 对象

* `dx`: x 方向逆时针旋转弧度，或者绕旋转轴线的旋转弧度
* `dy`: y 方向逆时针旋转弧度
* `dz`: z 方向逆时针旋转弧度
* `center`: 旋转中心，默认为原点
* `axis`: 旋转轴线，无默认值


### 🟡`scale`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def scale(
    self,
    kx = 1,
    ky = 1,
    kz = 1,
    *,
    center = None,
) -> _empty: ...
```
缩放几何体中的所有 3D 对象

* `kx`: x 方向缩放比例
* `ky`: y 方向缩放比例
* `kz`: z 方向缩放比例
* `center`: 缩放中心，默认为几何中心


### 🟡`translate`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def translate(
    self,
    dx = 0,
    dy = 0,
    dz = 0,
) -> _empty: ...
```
平移几何体中的所有 3D 对象

* `dx`: x 方向位移长度
* `dy`: y 方向位移长度
* `dz`: z 方向位移长度


### 🟡`update`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def update(
    self,
) -> _empty: ...
```
更新几何体



## 🟢`Line`



<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code> | `Component`


```python
def __init__(
    self,
    canvas,
    point_start,
    point_end,
    *,
    width = 1,
    fill = '#000000',
) -> _empty: ...
```
线

* `canvas`: 父画布
* `point_start`: 起点坐标
* `point_end`: 终点坐标
* `width`: 线的宽度
* `fill`: 线的颜色


### 🟡`_camera_distance`


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _camera_distance(
    self,
) -> _empty: ...
```
与相机距离

### 🟡`update`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def update(
    self,
) -> _empty: ...
```
更新对象的显示



## 🟢`Plane`



<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code> | `Component`


```python
def __init__(
    self,
    canvas,
    *points,
    width = 1,
    fill = '',
    outline = '#000000',
) -> _empty: ...
```
面

* `canvas`: 父画布
* `points`: 各点的空间坐标
* `width`: 面轮廓的宽度
* `fill`: 面内部的填充颜色
* `outline`: 面轮廓的颜色


### 🟡`_camera_distance`


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _camera_distance(
    self,
) -> _empty: ...
```
与相机距离

### 🟡`update`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def update(
    self,
) -> _empty: ...
```
更新对象的显示



## 🟢`Point`



<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code> | `Component`


```python
def __init__(
    self,
    canvas,
    coords,
    *,
    size = 1,
    width = 1,
    fill = '#000000',
    outline = '#000000',
    markuptext = '',
    markupdelta = (0, 0),
    markupfont = ('Microsoft YaHei', -20),
    markupfill = '#000000',
    markupjustify = 'center',
) -> _empty: ...
```
点

* `canvas`: 父画布
* `coords`: 点的空间坐标
* `size`: 点的大小
* `width`: 点轮廓的宽度
* `fill`: 点内部的填充颜色
* `outline`: 点轮廓的颜色
* `markuptext`: 标记文本
* `markupdelta`: 标记文本显示位置的偏移量
* `markupfont`: 标记文本字体
* `markupfill`: 标记文本颜色
* `markupjustify`: 标记文本多行对齐方式


### 🟡`_camera_distance`


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _camera_distance(
    self,
) -> _empty: ...
```
与相机距离

### 🟡`update`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def update(
    self,
) -> _empty: ...
```
更新对象的显示



## 🟢`Space`



<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code> | `Canvas`


```python
def __init__(
    self,
    master: containers.Tk | containers.Toplevel | containers.Canvas | None = None,
    *,
    expand: typing.Literal['', 'x', 'y', 'xy'] = 'xy',
    auto_zoom: bool = False,
    keep_ratio: typing.Literal['min', 'max'] | None = None,
    free_anchor: bool = False,
    **kwargs,
) -> None: ...
```
A canvas where you can view 3D objects


### 🟡`_initialization`


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _initialization(
    self,
) -> None: ...
```


### 🟡`_rotate`


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _rotate(
    self,
    event: tkinter.Event,
    press: bool | None = None,
    _cache: list[float] = [],
) -> None: ...
```

Triggering of a rotation event

* `event`: Event
* `press`: True, False, and None represent press, release, and move events, respectively
* `_cache`: cache values that record the coordinates of mouse presses


### 🟡`_scale`


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _scale(
    self,
    event: tkinter.Event,
    flag: bool | None = None,
) -> None: ...
```
Triggering of a scaling event

### 🟡`_translate`


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _translate(
    self,
    event: tkinter.Event,
    press: bool | None = None,
    _cache: list[float] = [],
) -> None: ...
```

Triggering of a translation event

* `event`: Event
* `press`: True, False, and None represent press, release, and move events, respectively
* `_cache`: cache values that record the coordinates of mouse presses


### 🟡`_zoom_self`


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _zoom_self(
    self,
) -> None: ...
```




## 🟢`Text3D`



<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code> | `Component`


```python
def __init__(
    self,
    canvas,
    coords,
    text = '',
    *,
    font = ('Microsoft YaHei', -20),
    justify = 'center',
    fill = '#000000',
) -> _empty: ...
```
三维文本

* `canvas`: 父画布
* `coords`: 点的空间坐标
* `text`: 显示的文本
* `size`: 点的大小
* `font`: 点轮廓的宽度
* `justify`: 多行文本对齐方式
* `fill`: 点内部的填充颜色


### 🟡`_camera_distance`


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _camera_distance(
    self,
) -> _empty: ...
```
与相机距离

### 🟡`update`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def update(
    self,
) -> _empty: ...
```
更新对象的显示



## 🔵`project`


<code style='color: royalblue;'>function</code> <code style='color: green;'>public</code>

```python
def project(
    coordinate,
    distance,
) -> _empty: ...
```
将一个三维空间中的点投影到指定距离的正向平面上，并返回在该平面上的坐标

* `coordinate`: 点的空间坐标
* `distance`: 正向平面的距离（平面正对着我们）


## 🔵`rotate`


<code style='color: royalblue;'>function</code> <code style='color: green;'>public</code>

```python
def rotate(
    coordinate,
    dx = 0,
    dy = 0,
    dz = 0,
    *,
    center,
    axis = None,
) -> _empty: ...
```
将一个三维空间中的点以一个点或线为参照进行旋转（实现方式为欧拉角）

* `coordinate`: 点的空间坐标
* `dx`: x 方向逆时针旋转弧度，或者绕旋转轴线的旋转弧度
* `dy`: y 方向逆时针旋转弧度
* `dz`: z 方向逆时针旋转弧度
* `center`: 旋转中心的空间坐标
* `axis`: 旋转轴线的空间坐标


## 🔵`scale`


<code style='color: royalblue;'>function</code> <code style='color: green;'>public</code>

```python
def scale(
    coordinate,
    kx = 1,
    ky = 1,
    kz = 1,
    *,
    center,
) -> _empty: ...
```
将一个三维空间中的点以另一个点为缩放中心进行缩放

* `coordinate`: 点的空间坐标
* `kx`: x 方向缩放比例
* `ky`: y 方向缩放比例
* `kz`: z 方向缩放比例
* `center`: 缩放中心的空间坐标


## 🔵`translate`


<code style='color: royalblue;'>function</code> <code style='color: green;'>public</code>

```python
def translate(
    coordinate: tuple[float, float, float],
    dx: float = 0,
    dy: float = 0,
    dz: float = 0,
) -> None: ...
```
将一个三维空间中的点进行平移

* `coordinate`: 点的空间坐标
* `dx`: x 方向位移长度
* `dy`: y 方向位移长度
* `dz`: z 方向位移长度


