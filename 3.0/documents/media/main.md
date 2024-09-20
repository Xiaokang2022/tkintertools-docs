# tkintertools.media.main

APIs for playing videos

## 🟢`VideoCanvas`



<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code> | `Canvas`


```python
def __init__(
    self,
    master: containers.Tk | containers.Canvas,
    *,
    controls: bool = False,
    loop: bool = False,
    click_pause: bool = True,
    expand: typing.Literal['', 'x', 'y', 'xy'] = 'xy',
    zoom_item: bool = False,
    keep_ratio: typing.Optional[typing.Literal['min', 'max']] = None,
    free_anchor: bool = False,
    name: str = 'Canvas',
    **kwargs,
) -> None: ...
```
A canvas that is scalable and playable for videos

* `master`: parent widget
* `control`: whether to enable the built-in UI
* `click_pause`: whether to pause when clicked
* `expand`: the mode of expand, `x` is horizontal, and `y` is vertical
* `zoom_item`: whether or not to scale its items
* `keep_ratio`: the mode of aspect ratio, `min` follows the minimum
value, `max` follows the maximum value
* `free_anchor`: whether the anchor point is free-floating
* `kwargs`: compatible with other parameters of class `tkinter.Canvas`


### 🟡`_display_control_bar`


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _display_control_bar(
    self,
    value: bool,
) -> None: ...
```
Animation for bottom bar

### 🟡`_initialization`


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _initialization(
    self,
) -> None: ...
```


### 🟡`_load_control_bar`


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _load_control_bar(
    self,
) -> None: ...
```
UI for bottom bar

### 🟡`_play`


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _play(
    self,
    init_prams: dict[str, bool] | None = None,
) -> None: ...
```
Refresh the canvas

### 🟡`_re_place`


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _re_place(
    self,
) -> None: ...
```


### 🟡`_refresh_control_bar`


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _refresh_control_bar(
    self,
    pts: float,
) -> None: ...
```
Refresh the stat of the control bar

### 🟡`_resize`


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _resize(
    self,
) -> None: ...
```
Resize the size of video

### 🟡`close`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def close(
    self,
) -> None: ...
```
Close the video player

### 🟡`open`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def open(
    self,
    file: str,
    *,
    auto_play: bool = False,
    muted: bool = False,
) -> None: ...
```

Open a video file and play

* `file`: the video file path
* `auto_play`: whether to start playing the video automatically
* `muted`: whether or not to mute the video at the start




## 🟢`_AudioImage`



<code style='color: limegreen;'>class</code> <code style='color: orange;'>protected</code> | `Image` `_CustomizedWidget`


```python
def __init__(
    self,
    *args,
    **kwargs,
) -> None: ...
```
Customized image widget for displaying audio icon




## 🟢`_CustomizedWidget`



<code style='color: limegreen;'>class</code> <code style='color: orange;'>protected</code> | `Widget` `ABC`

### 🟡`_bind`


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _bind(
    self,
    *,
    icon: str,
) -> None: ...
```
process some thing about theme

### 🟡`_theme`


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _theme(
    self,
    dark: bool,
) -> None: ...
```
Switch the icon theme of the widget



## 🟢`_FullscreenToggleButton`



<code style='color: limegreen;'>class</code> <code style='color: orange;'>protected</code> | `ToggleButton` `_CustomizedWidget`


```python
def __init__(
    self,
    *args,
    **kwargs,
) -> None: ...
```
Customized toggle button for function of fullscreen




## 🟢`_PlayButton`



<code style='color: limegreen;'>class</code> <code style='color: orange;'>protected</code> | `Button` `_CustomizedWidget`


```python
def __init__(
    self,
    *args,
    **kwargs,
) -> None: ...
```
Customized Button for the ability to play or pause the video


### 🟡`_toggle`


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _toggle(
    self,
) -> None: ...
```
Force to change the icon image



