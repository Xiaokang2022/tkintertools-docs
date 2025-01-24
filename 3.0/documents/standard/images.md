# maliang.standard.images

<small>:octicons-mark-github-16: 源代码：[`maliang/standard/images.py`](https://github.com/Xiaokang2022/maliang/blob/3.0.0rc6/maliang/standard/images.py){ target='_blank' }</small>

All standard `Image` classes

## 🟢`Smoke`



<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code> | `Image`


```python
def __init__(
    self,
    widget: virtual.Widget,
    relative_position: tuple[int, int] = (0, 0),
    size: tuple[int, int] | None = None,
    *,
    color: str | None = '#00000066',
    name: str | None = None,
    animation: bool = True,
    **kwargs,
) -> None: ...
```
A special Image with only one color

* `widget`: parent widget
* `relative_position`: position relative to its widgets
* `size`: size of element
* `color`: color of the image object of the element
* `name`: name of element
* `animation`: Wether use animation to change color
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



## 🟢`StillImage`



<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code> | `Image`

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



