# maliang.animation.animations

<small>:octicons-mark-github-16: 源代码：[`maliang/animation/animations.py`](https://github.com/Xiaokang2022/maliang/blob/3.0.0/maliang/animation/animations.py){ target='_blank' }</small>

Base and standard animation classes.

The animation base class can be inherited or called directly. Other standard
animation classes are best used by direct calls, rather than inheritance.


## 🟢`Animation`



<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code> | `object`


```python
def __init__(
    self,
    duration: int,
    command: collections.abc.Callable[[float], typing.Any],
    *,
    controller: collections.abc.Callable[[float], float] = linear,
    end: collections.abc.Callable[[], typing.Any] | None = None,
    fps: int = 30,
    repeat: int = 0,
    repeat_delay: int = 0,
    derivation: bool = False,
) -> None: ...
```
Base animation class.

* `duration`: duration of the animation, in milliseconds
* `command`: callback function, which will be called once per frame
* `controller`: a function that controls the animation process
* `end`: end function, which is called once at the end of the animation
* `fps`: frame rate of the animation
* `repeat`: number of repetitions of the animation
* `repeat_delay`: length of the delay before the animation repeats
* `derivation`: whether the callback function is derivative


### 🟡`_repeat`


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _repeat(
    self,
) -> None: ...
```
Processing of the number of repetitions.

### 🟡`skip`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def skip(
    self,
    count: int = 1,
) -> None: ...
```
Skip some loops.

* `count`: count of skipping


### 🟡`start`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def start(
    self,
    *,
    delay: int = 0,
) -> str | None: ...
```
Start the animation.

* `delay`: length of the delay before the animation starts


### 🟡`stop`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def stop(
    self,
    *,
    delay: int = 0,
) -> str | None: ...
```
Stop the animation.

* `delay`: length of the delay before the animation stops




## 🟢`GradientItem`



<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code> | `Animation`


```python
def __init__(
    self,
    canvas: tkinter.Canvas | containers.Canvas,
    item: int,
    parameter: str,
    colors: tuple[str, str],
    duration: int,
    *,
    controller: collections.abc.Callable[[float], float] = linear,
    end: collections.abc.Callable[[], typing.Any] | None = None,
    fps: int = 30,
    repeat: int = 0,
    repeat_delay: int = 0,
    derivation: bool = False,
) -> None: ...
```
Animation of making the color of canvas item to be gradient.

* `canvas`: an instance of `tkinter.Canvas` that contains the item
* `item`: item whose color is to be gradient
* `parameter`: parameter name of item that is to be modified in color
* `colors`: a tuple of the initial and ending colors
* `duration`: duration of the animation, in milliseconds
* `controller`: a function that controls the animation process
* `end`: end function, which is called once at the end of the animation
* `fps`: frame rate of the animation
* `repeat`: number of repetitions of the animation
* `repeat_delay`: length of the delay before the animation repeats
* `derivation`: whether the callback function is derivative




## 🟢`GradientTkWidget`



<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code> | `Animation`


```python
def __init__(
    self,
    widget: tkinter.Widget,
    parameter: str,
    colors: tuple[str, str],
    duration: int,
    *,
    controller: collections.abc.Callable[[float], float] = linear,
    end: collections.abc.Callable[[], typing.Any] | None = None,
    fps: int = 30,
    repeat: int = 0,
    repeat_delay: int = 0,
    derivation: bool = False,
) -> None: ...
```
Animation of making the color of `tkinter.Widget` to be gradient.

* `widget`: the `tkinter.Widget` whose color is to be gradient
* `parameter`: parameter name of widget that is to be modified in color
* `colors`: a tuple of the initial and ending colors
* `duration`: duration of the animation, in milliseconds
* `controller`: a function that controls the animation process
* `end`: end function, which is called once at the end of the animation
* `fps`: frame rate of the animation
* `repeat`: number of repetitions of the animation
* `repeat_delay`: length of the delay before the animation repeats
* `derivation`: whether the callback function is derivative




## 🟢`MoveElement`



<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code> | `Animation`


```python
def __init__(
    self,
    element: virtual.Element,
    offset: tuple[float, float],
    duration: int,
    *,
    controller: collections.abc.Callable[[float], float] = linear,
    end: collections.abc.Callable[[], typing.Any] | None = None,
    fps: int = 30,
    repeat: int = 0,
    repeat_delay: int = 0,
) -> None: ...
```
Animation of moving `virtual.Element`.

* `element`: the `virtual.Element` to be moved
* `offset`: relative offset of the coordinates
* `duration`: duration of the animation, in milliseconds
* `controller`: a function that controls the animation process
* `end`: end function, which is called once at the end of the animation
* `fps`: frame rate of the animation
* `repeat`: number of repetitions of the animation
* `repeat_delay`: length of the delay before the animation repeats




## 🟢`MoveItem`



<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code> | `Animation`


```python
def __init__(
    self,
    canvas: tkinter.Canvas | containers.Canvas,
    item: int,
    offset: tuple[float, float],
    duration: int,
    *,
    controller: collections.abc.Callable[[float], float] = linear,
    end: collections.abc.Callable[[], typing.Any] | None = None,
    fps: int = 30,
    repeat: int = 0,
    repeat_delay: int = 0,
) -> None: ...
```
Animation of moving a item of `tkinter.Canvas`.

* `canvas`: an instance of `tkinter.Canvas` that contains the item
* `item`: the item to be moved
* `offset`: relative offset of the coordinates
* `duration`: duration of the animation, in milliseconds
* `controller`: a function that controls the animation process
* `end`: end function, which is called once at the end of the animation
* `fps`: frame rate of the animation
* `repeat`: number of repetitions of the animation
* `repeat_delay`: length of the delay before the animation repeats




## 🟢`MoveTkWidget`



<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code> | `Animation`


```python
def __init__(
    self,
    widget: tkinter.Widget,
    offset: tuple[float, float],
    duration: int,
    *,
    controller: collections.abc.Callable[[float], float] = linear,
    end: collections.abc.Callable[[], typing.Any] | None = None,
    fps: int = 30,
    repeat: int = 0,
    repeat_delay: int = 0,
) -> None: ...
```
Animation of moving `tkinter.Widget`.

* `widget`: the `tkinter.Widget` to be moved
* `offset`: relative offset of the coordinates
* `duration`: duration of the animation, in milliseconds
* `controller`: a function that controls the animation process
* `end`: end function, which is called once at the end of the animation
* `fps`: frame rate of the animation
* `repeat`: number of repetitions of the animation
* `repeat_delay`: length of the delay before the animation repeats




## 🟢`MoveWidget`



<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code> | `Animation`


```python
def __init__(
    self,
    widget: virtual.Widget,
    offset: tuple[float, float],
    duration: int,
    *,
    controller: collections.abc.Callable[[float], float] = linear,
    end: collections.abc.Callable[[], typing.Any] | None = None,
    fps: int = 30,
    repeat: int = 0,
    repeat_delay: int = 0,
) -> None: ...
```
Animation of moving `virtual.Widget`.

* `widget`: the `virtual.Widget` to be moved
* `offset`: relative offset of the coordinates
* `duration`: duration of the animation, in milliseconds
* `controller`: a function that controls the animation process
* `end`: end function, which is called once at the end of the animation
* `fps`: frame rate of the animation
* `repeat`: number of repetitions of the animation
* `repeat_delay`: length of the delay before the animation repeats




## 🟢`MoveWindow`



<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code> | `Animation`


```python
def __init__(
    self,
    window: tkinter.Tk | tkinter.Toplevel | containers.Tk | containers.Toplevel,
    offset: tuple[float, float],
    duration: int,
    *,
    controller: collections.abc.Callable[[float], float] = linear,
    end: collections.abc.Callable[[], typing.Any] | None = None,
    fps: int = 30,
    repeat: int = 0,
    repeat_delay: int = 0,
) -> None: ...
```
Animation of moving the window.

* `window`: the window to be moved
* `offset`: relative offset of the coordinates
* `duration`: duration of the animation, in milliseconds
* `controller`: a function that controls the animation process
* `end`: end function, which is called once at the end of the animation
* `fps`: frame rate of the animation
* `repeat`: number of repetitions of the animation
* `repeat_delay`: length of the delay before the animation repeats




## 🟢`ScaleFontSize`



<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code> | `Animation`


```python
def __init__(
    self,
    text: virtual.Text,
    sizes: float | tuple[float, float],
    duration: int,
    *,
    controller: collections.abc.Callable[[float], float] = linear,
    end: collections.abc.Callable[[], typing.Any] | None = None,
    fps: int = 30,
    repeat: int = 0,
    repeat_delay: int = 0,
    derivation: bool = False,
) -> None: ...
```
Animation of scaling the font size of `virtual.Text`.

* `text`: an instance of `virtual.Text` that needs to be scaled
* `sizes`: a tuple of the initial and ending sizes or target font size
* `duration`: duration of the animation, in milliseconds
* `controller`: a function that controls the animation process
* `end`: end function, which is called once at the end of the animation
* `fps`: frame rate of the animation
* `repeat`: number of repetitions of the animation
* `repeat_delay`: length of the delay before the animation repeats
* `derivation`: whether the callback function is derivative




