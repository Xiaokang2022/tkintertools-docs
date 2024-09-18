# tkintertools.animation.animations


Standard animation classes

The built-in basic animation classes are: `MoveTkWidget`, `MoveWidget`,
`MoveComponent`, `MoveItem`, `GradientTkWidget`, `GradientItem`, `ScaleFontSize`


## 🟢 类

### <big>`Animation`</big>



<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code> | `object`


```python
def __init__(
    self,
    ms: int,
    controller: typing.Callable[[float], float],
    *,
    callback: typing.Optional[typing.Callable[[float], typing.Any]] = None,
    end: typing.Optional[typing.Callable[[], typing.Any]] = None,
    repeat: int = 0,
    fps: int = 30,
    derivation: bool = False,
) -> None: ...
```
Animation base class

* `ms`: duration of the animation, in milliseconds
* `controller`: control functions that determine the course of the
entire animation movement
* `callback`: callback function, which will be called once per frame,
with the parameter being the percentage of the current animation
progress
* `end`: ending function, which is called once at the end of the
animation
* `repeat`: number of repetitions of the entire animation process
* `fps`: the FPS of the animation
* `derivation`: whether the callback function is derivative


#### <big>`_wrapper`</big>


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _wrapper(
    self,
    func: typing.Callable[[float], float],
) -> typing.Callable[[float], float]: ...
```

Make the ending function call correctly

* `func`: the callback function to be wrapped


#### <big>`start`</big>


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def start(
    self,
    *,
    delay: int = 0,
) -> None: ...
```

Start the animation

* `delay`: length of the delay before the animation starts, in
milliseconds 


#### <big>`stop`</big>


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def stop(
    self,
) -> None: ...
```
Stop the animation



### <big>`GradientItem`</big>



<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code> | `Animation`


```python
def __init__(
    self,
    canvas: Canvas,
    item: int,
    parameter: str,
    ms: int,
    colors: tuple[str, str],
    *,
    controller: typing.Callable[[float], float] = flat,
    end: typing.Optional[typing.Callable[[], typing.Any]] = None,
    repeat: int = 0,
    fps: int = 30,
    derivation: bool = False,
) -> None: ...
```
Animation that makes color of canvas item gradient

* `canvas`: an instance of `tkinter.Canvas` that contains the item
* `item`: item whose color is to be gradient
* `parameter`: parameter name of the part of the item that needs to be
modified in color
* `ms`: duration of the animation, in milliseconds
* `colors`: a tuple of the initial and ending colors
* `controller`: control functions that determine the course of the
entire animation movement
* `end`: ending function, which is called once at the end of the
animation
* `repeat`: number of repetitions of the entire animation process
* `fps`: the FPS of the animation
* `derivation`: whether the callback function is derivative




### <big>`GradientTkWidget`</big>



<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code> | `Animation`


```python
def __init__(
    self,
    widget: Widget,
    parameter: str,
    ms: int,
    colors: tuple[str, str],
    *,
    controller: typing.Callable[[float], float] = flat,
    end: typing.Optional[typing.Callable[[], typing.Any]] = None,
    repeat: int = 0,
    fps: int = 30,
    derivation: bool = False,
) -> None: ...
```
Animation that makes color of `tkinter.Widget` gradient

* `widget`: tkinter widget whose color is to be gradient
* `parameter`: parameter name of the part of the item that needs to be
modified in color
* `ms`: duration of the animation, in milliseconds
* `colors`: a tuple of the initial and ending colors
* `controller`: control functions that determine the course of the
entire animation movement
* `end`: ending function, which is called once at the end of the
animation
* `repeat`: number of repetitions of the entire animation process
* `fps`: the FPS of the animation
* `derivation`: whether the callback function is derivative




### <big>`MoveComponent`</big>



<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code> | `Animation`


```python
def __init__(
    self,
    component: virtual.Component,
    ms: int,
    offset: tuple[float, float],
    *,
    controller: typing.Callable[[float], float] = flat,
    end: typing.Optional[typing.Callable[[], typing.Any]] = None,
    repeat: int = 0,
    fps: int = 30,
) -> None: ...
```
Animation of moving `Component`

* `component`: component to be moved
* `ms`: duration of the animation, in milliseconds
* `offset`: relative offset of the coordinates
* `controller`: control functions that determine the course of the
entire animation movement
* `end`: ending function, which is called once at the end of the
animation
* `repeat`: number of repetitions of the entire animation process
* `fps`: the FPS of the animation




### <big>`MoveItem`</big>



<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code> | `Animation`


```python
def __init__(
    self,
    canvas: Canvas,
    item: int,
    ms: int,
    offset: tuple[float, float],
    *,
    controller: typing.Callable[[float], float] = flat,
    end: typing.Optional[typing.Callable[[], typing.Any]] = None,
    repeat: int = 0,
    fps: int = 30,
) -> None: ...
```
Animation of moving a item

* `canvas`: an instance of `tkinter.Canvas` that contains the item
* `item`: the item to be moved
* `ms`: duration of the animation, in milliseconds
* `offset`: relative offset of the coordinates
* `controller`: control functions that determine the course of the
entire animation movement
* `end`: ending function, which is called once at the end of the
animation
* `repeat`: number of repetitions of the entire animation process
* `fps`: the FPS of the animation




### <big>`MoveTkWidget`</big>



<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code> | `Animation`


```python
def __init__(
    self,
    widget: Widget,
    ms: int,
    offset: tuple[float, float],
    *,
    controller: typing.Callable[[float], float] = flat,
    end: typing.Optional[typing.Callable[[], typing.Any]] = None,
    repeat: int = 0,
    fps: int = 30,
) -> None: ...
```
Animation of moving `tkinter.Widget`

* `widget`: tkinter widget to be moved
* `ms`: duration of the animation, in milliseconds
* `offset`: relative offset of the coordinates
* `controller`: control functions that determine the course of the
entire animation movement
* `end`: ending function, which is called once at the end of the
animation
* `repeat`: number of repetitions of the entire animation process
* `fps`: the FPS of the animation




### <big>`MoveWidget`</big>



<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code> | `Animation`


```python
def __init__(
    self,
    widget: virtual.Widget,
    ms: int,
    offset: tuple[float, float],
    *,
    controller: typing.Callable[[float], float] = flat,
    end: typing.Optional[typing.Callable[[], typing.Any]] = None,
    repeat: int = 0,
    fps: int = 30,
) -> None: ...
```
Animation of moving `Widget`

* `widget`: widget to be moved
* `ms`: duration of the animation, in milliseconds
* `offset`: relative offset of the coordinates
* `controller`: control functions that determine the course of the
entire animation movement
* `end`: ending function, which is called once at the end of the
animation
* `repeat`: number of repetitions of the entire animation process
* `fps`: the FPS of the animation




### <big>`ScaleFontSize`</big>



<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code> | `Animation`


```python
def __init__(
    self,
    text: virtual.Text,
    ms: int,
    sizes: tuple[float, float] | float,
    *,
    controller: typing.Callable[[float], float] = flat,
    end: typing.Optional[typing.Callable[[], typing.Any]] = None,
    repeat: int = 0,
    fps: int = 30,
    derivation: bool = False,
) -> None: ...
```
Animation of scaling the font size

* `text`: an instance of `virtual.Text` that needs to be scaled in font
size
* `ms`: duration of the animation, in milliseconds
* `sizes`: a tuple of the initial and ending sizes or target font size
* `controller`: control functions that determine the course of the
entire animation movement
* `end`: ending function, which is called once at the end of the
animation
* `repeat`: number of repetitions of the entire animation process
* `fps`: the FPS of the animation
* `derivation`: whether the callback function is derivative


#### <big>`_scale`</big>


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _scale(
    self,
    size: int,
) -> None: ...
```
Scale font size



