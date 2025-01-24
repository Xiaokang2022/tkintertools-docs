# maliang.standard.widgets

<small>:octicons-mark-github-16: 源代码：[`maliang/standard/widgets.py`](https://github.com/Xiaokang2022/maliang/blob/3.0.0rc6/maliang/standard/widgets.py){ target='_blank' }</small>

All standard `Widget` classes

## 🟢`Button`



<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code> | `Widget`


```python
def __init__(
    self,
    master: containers.Canvas | virtual.Widget,
    position: tuple[int, int],
    size: tuple[int, int] | None = None,
    *,
    text: str = '',
    family: str | None = None,
    fontsize: int | None = None,
    weight: typing.Literal['normal', 'bold'] = 'normal',
    slant: typing.Literal['roman', 'italic'] = 'roman',
    underline: bool = False,
    overstrike: bool = False,
    justify: typing.Literal['left', 'center', 'right'] = 'left',
    command: collections.abc.Callable | None = None,
    image: enhanced.PhotoImage | None = None,
    anchor: typing.Literal['n', 'e', 'w', 's', 'nw', 'ne', 'sw', 'se', 'center'] = 'nw',
    capture_events: bool | None = None,
    gradient_animation: bool | None = None,
    auto_update: bool | None = None,
    style: type[virtual.Style] | None = None,
) -> None: ...
```
Button widget, typically used to trigger a function

* `master`: parent canvas
* `position`: position of the widget
* `size`: size of the widget
* `text`: text of the widget
* `family`: font family
* `fontsize`: font size
* `weight`: weight of the text
* `slant`: slant of the text
* `underline`: whether the text is underline
* `overstrike`: whether the text is overstrike
* `justify`: justify mode of the text
* `command`: a function that is triggered when the button is pressed
* `image`: image of the widget
* `anchor`: anchor of the widget
* `capture_events`: wether detect another widget under the widget
* `gradient_animation`: wether enable gradient_animation
* `auto_update`: whether the theme manager update it automatically
* `style`: style of the widget




## 🟢`CheckBox`



<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code> | `Widget`


```python
def __init__(
    self,
    master: containers.Canvas | virtual.Widget,
    position: tuple[int, int],
    length: int = 30,
    *,
    default: bool | None = None,
    command: collections.abc.Callable[[bool], typing.Any] | None = None,
    image: enhanced.PhotoImage | None = None,
    anchor: typing.Literal['n', 'e', 'w', 's', 'nw', 'ne', 'sw', 'se', 'center'] = 'nw',
    capture_events: bool | None = None,
    gradient_animation: bool | None = None,
    auto_update: bool | None = None,
    style: type[virtual.Style] | None = None,
) -> None: ...
```
Checkbox button widget, generally used to check some options

* `master`: parent canvas
* `position`: position of the widget
* `length`: length of the widget
* `default`: default state of the widget
* `command`: a function that is triggered when the state of check button is on
* `image`: image of the widget
* `anchor`: anchor of the widget
* `capture_events`: wether detect another widget under the widget
* `gradient_animation`: wether enable gradient_animation
* `auto_update`: whether the theme manager update it automatically
* `style`: style of the widget


### 🟡`get`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def get(
    self,
) -> bool: ...
```
Get the state of the check button

### 🟡`set`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def set(
    self,
    value: bool,
    *,
    callback: bool = False,
) -> None: ...
```
Set the state of the check button



## 🟢`ComboBox`



<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code> | `Widget`


```python
def __init__(
    self,
    master: containers.Canvas | virtual.Widget,
    position: tuple[int, int],
    size: tuple[int, int] | None = None,
    *,
    text: tuple[str, ...] = (),
    family: str | None = None,
    fontsize: int | None = None,
    weight: typing.Literal['normal', 'bold'] = 'normal',
    slant: typing.Literal['roman', 'italic'] = 'roman',
    underline: bool = False,
    overstrike: bool = False,
    justify: typing.Literal['left', 'center', 'right'] = 'left',
    default: int | None = None,
    command: collections.abc.Callable[[int | None], typing.Any] | None = None,
    image: tuple[enhanced.PhotoImage | None, ...] = (),
    anchor: typing.Literal['n', 'e', 'w', 's', 'nw', 'ne', 'sw', 'se', 'center'] = 'nw',
    align: typing.Literal['up', 'down'] = 'down',
    capture_events: bool | None = None,
    gradient_animation: bool | None = None,
    auto_update: bool | None = None,
    style: type[virtual.Style] | None = None,
) -> None: ...
```
An input box that can provide several options

* `master`: parent canvas
* `position`: position of the widget
* `size`: size of the widget
* `text`: text of the widget
* `family`: font family
* `fontsize`: font size
* `weight`: weight of the text
* `slant`: slant of the text
* `underline`: whether the text is underline
* `overstrike`: whether the text is overstrike
* `justify`: justify mode of the text
* `default`: default value of the widget
* `command`: a function that is triggered when the button is pressed
* `image`: image of the widget
* `anchor`: anchor of the widget
* `align`: align of the widget
* `capture_events`: wether detect another widget under the widget
* `gradient_animation`: wether enable gradient_animation
* `auto_update`: whether the theme manager update it automatically
* `style`: style of the widget


### 🟡`_close_options`


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _close_options(
    self,
    index: int | None = None,
) -> None: ...
```
Close the options

### 🟡`_extra_bind`


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _extra_bind(
    self,
    event,
) -> None: ...
```


### 🟡`_get_position`


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _get_position(
    self,
    align: typing.Literal['up', 'center', 'down'],
) -> tuple[int, int]: ...
```
Get the position of "pop-up" SegmentedButton

### 🟡`_open_options`


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _open_options(
    self,
) -> None: ...
```
Open the options

### 🟡`get`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def get(
    self,
) -> int | None: ...
```
Get the index of the child toggle button with a value of True. If not, None is
returned.

### 🟡`set`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def set(
    self,
    value: int | None,
    *,
    callback: bool = False,
) -> None: ...
```
Activate the child toggle button for the specified index



## 🟢`HighlightButton`



<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code> | `Widget`


```python
def __init__(
    self,
    master: containers.Canvas | virtual.Widget,
    position: tuple[int, int],
    *,
    text: str = '',
    family: str | None = None,
    fontsize: int | None = None,
    weight: typing.Literal['normal', 'bold'] = 'normal',
    slant: typing.Literal['roman', 'italic'] = 'roman',
    underline: bool = False,
    overstrike: bool = False,
    justify: typing.Literal['left', 'center', 'right'] = 'left',
    command: collections.abc.Callable | None = None,
    image: enhanced.PhotoImage | None = None,
    anchor: typing.Literal['n', 'e', 'w', 's', 'nw', 'ne', 'sw', 'se', 'center'] = 'nw',
    capture_events: bool | None = None,
    gradient_animation: bool | None = None,
    auto_update: bool | None = None,
    style: type[virtual.Style] | None = None,
) -> None: ...
```
Highlight button, no outline, which added a highlight effect

* `master`: parent canvas
* `position`: position of the widget
* `text`: text of the widget
* `family`: font family
* `fontsize`: font size
* `weight`: weight of the text
* `slant`: slant of the text
* `underline`: whether the text is underline
* `overstrike`: whether the text is overstrike
* `justify`: justify mode of the text
* `command`: a function that is triggered when the hightlight button is pressed
* `image`: image of the widget
* `anchor`: anchor of the widget
* `capture_events`: wether detect another widget under the widget
* `gradient_animation`: wether enable gradient_animation
* `auto_update`: whether the theme manager update it automatically
* `style`: style of the widget




## 🟢`IconButton`



<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code> | `Widget`


```python
def __init__(
    self,
    master: containers.Canvas | virtual.Widget,
    position: tuple[int, int],
    size: tuple[int, int] | None = None,
    *,
    text: str = '',
    family: str | None = None,
    fontsize: int | None = None,
    weight: typing.Literal['normal', 'bold'] = 'normal',
    slant: typing.Literal['roman', 'italic'] = 'roman',
    underline: bool = False,
    overstrike: bool = False,
    justify: typing.Literal['left', 'center', 'right'] = 'left',
    command: collections.abc.Callable | None = None,
    image: enhanced.PhotoImage | None = None,
    anchor: typing.Literal['n', 'e', 'w', 's', 'nw', 'ne', 'sw', 'se', 'center'] = 'nw',
    capture_events: bool | None = None,
    gradient_animation: bool | None = None,
    auto_update: bool | None = None,
    style: type[virtual.Style] | None = None,
) -> None: ...
```
A button with an icon on the left side

* `master`: parent canvas
* `position`: position of the widget
* `size`: size of the widget
* `text`: text of the widget
* `family`: font family
* `fontsize`: font size
* `weight`: weight of the text
* `slant`: slant of the text
* `underline`: whether the text is underline
* `overstrike`: whether the text is overstrike
* `justify`: justify mode of the text
* `command`: a function that is triggered when the button is pressed
* `image`: image of the widget
* `anchor`: anchor of the widget
* `capture_events`: wether detect another widget under the widget
* `gradient_animation`: wether enable gradient_animation
* `auto_update`: whether the theme manager update it automatically
* `style`: style of the widget




## 🟢`Image`



<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code> | `Widget`


```python
def __init__(
    self,
    master: containers.Canvas | virtual.Widget,
    position: tuple[int, int],
    size: tuple[int, int] | None = None,
    *,
    image: enhanced.PhotoImage | None = None,
    anchor: typing.Literal['n', 'e', 'w', 's', 'nw', 'ne', 'sw', 'se', 'center'] = 'nw',
    capture_events: bool | None = None,
    gradient_animation: bool | None = None,
    auto_update: bool | None = None,
    style: type[virtual.Style] | None = None,
) -> None: ...
```
Image widget, generally used to display normal still image

* `master`: parent canvas
* `position`: position of the widget
* `size`: size of the widget
* `image`: image of the widget
* `anchor`: anchor of the widget
* `capture_events`: wether detect another widget under the widget
* `gradient_animation`: wether enable gradient_animation
* `auto_update`: whether the theme manager update it automatically
* `style`: style of the widget


### 🟡`get`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def get(
    self,
) -> enhanced.PhotoImage: ...
```
Get the image of the widget

### 🟡`set`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def set(
    self,
    image: enhanced.PhotoImage | None,
) -> None: ...
```
Set the image of the widget



## 🟢`InputBox`



<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code> | `Widget`


```python
def __init__(
    self,
    master: containers.Canvas | virtual.Widget,
    position: tuple[int, int],
    size: tuple[int, int] | None = None,
    *,
    family: str | None = None,
    fontsize: int | None = None,
    weight: typing.Literal['normal', 'bold'] = 'normal',
    slant: typing.Literal['roman', 'italic'] = 'roman',
    underline: bool = False,
    overstrike: bool = False,
    align: typing.Literal['left', 'right', 'center'] = 'left',
    placeholder: str = '',
    show: str | None = None,
    limit: int = inf,
    limit_width: int = 0,
    image: enhanced.PhotoImage | None = None,
    anchor: typing.Literal['n', 'e', 'w', 's', 'nw', 'ne', 'sw', 'se', 'center'] = 'nw',
    capture_events: bool | None = None,
    gradient_animation: bool | None = None,
    auto_update: bool | None = None,
    style: type[virtual.Style] | None = None,
) -> None: ...
```
Input box widget, generally used to enter certain information on a single line

* `master`: parent canvas
* `position`: position of the widget
* `size`: size of the widget
* `family`: font family
* `fontsize`: font size
* `weight`: weight of the text
* `slant`: slant of the text
* `underline`: whether the text is underline
* `overstrike`: whether the text is overstrike
* `align`: align mode of the text
* `show`: display a value that obscures the original content
* `placeholder`: a placeholder for the prompt
* `limit`: limit on the number of characters
* `limit_width`: limit on the width of characters
* `image`: image of the widget
* `anchor`: anchor of the widget
* `capture_events`: wether detect another widget under the widget
* `gradient_animation`: wether enable gradient_animation
* `auto_update`: whether the theme manager update it automatically
* `style`: style of the widget


### 🟡`append`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def append(
    self,
    value: str,
) -> bool: ...
```
Append text to Entry

### 🟡`clear`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def clear(
    self,
) -> None: ...
```
Clear the text value of the Entry

### 🟡`get`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def get(
    self,
) -> str: ...
```
Get the value of the Entry

### 🟡`insert`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def insert(
    self,
    index: int,
    value: str,
) -> bool: ...
```
Insert

### 🟡`pop`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def pop(
    self,
    index: int = -1,
) -> str: ...
```
Delete a specified amount of text

### 🟡`remove`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def remove(
    self,
    start: int,
    end: int | None = None,
) -> int: ...
```
Remove

### 🟡`set`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def set(
    self,
    value: str,
) -> bool: ...
```
Set the text value of the Entry



## 🟢`Label`



<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code> | `Widget`


```python
def __init__(
    self,
    master: containers.Canvas | virtual.Widget,
    position: tuple[int, int],
    size: tuple[int, int] | None = None,
    *,
    text: str = '',
    family: str | None = None,
    fontsize: int | None = None,
    weight: typing.Literal['normal', 'bold'] = 'normal',
    slant: typing.Literal['roman', 'italic'] = 'roman',
    underline: bool = False,
    overstrike: bool = False,
    justify: typing.Literal['left', 'center', 'right'] = 'left',
    image: enhanced.PhotoImage | None = None,
    anchor: typing.Literal['n', 'e', 'w', 's', 'nw', 'ne', 'sw', 'se', 'center'] = 'nw',
    capture_events: bool | None = None,
    gradient_animation: bool | None = None,
    auto_update: bool | None = None,
    style: type[virtual.Style] | None = None,
) -> None: ...
```
Label widget, which is generally used to display key information

* `master`: parent canvas
* `position`: position of the widget
* `size`: size of the widget
* `text`: text of the widget
* `family`: font family
* `fontsize`: font size
* `weight`: weight of the text
* `slant`: slant of the text
* `underline`: whether the text is underline
* `overstrike`: whether the text is overstrike
* `justify`: justify mode of the text
* `image`: image of the widget
* `anchor`: anchor of the widget
* `capture_events`: wether detect another widget under the widget
* `gradient_animation`: wether enable gradient_animation
* `auto_update`: whether the theme manager update it automatically
* `style`: style of the widget




## 🟢`OptionButton`



<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code> | `Widget`


```python
def __init__(
    self,
    master: containers.Canvas | virtual.Widget,
    position: tuple[int, int],
    size: tuple[int, int] | None = None,
    *,
    text: tuple[str, ...] = (),
    family: str | None = None,
    fontsize: int | None = None,
    weight: typing.Literal['normal', 'bold'] = 'normal',
    slant: typing.Literal['roman', 'italic'] = 'roman',
    underline: bool = False,
    overstrike: bool = False,
    justify: typing.Literal['left', 'center', 'right'] = 'left',
    default: int | None = None,
    command: collections.abc.Callable[[int | None], typing.Any] | None = None,
    image: tuple[enhanced.PhotoImage | None, ...] = (),
    anchor: typing.Literal['n', 'e', 'w', 's', 'nw', 'ne', 'sw', 'se', 'center'] = 'nw',
    align: typing.Literal['up', 'center', 'down'] = 'center',
    capture_events: bool | None = None,
    gradient_animation: bool | None = None,
    auto_update: bool | None = None,
    style: type[virtual.Style] | None = None,
) -> None: ...
```
A button that has many options to choose

* `master`: parent canvas
* `position`: position of the widget
* `size`: size of the widget
* `text`: text of the widget
* `family`: font family
* `fontsize`: font size
* `weight`: weight of the text
* `slant`: slant of the text
* `underline`: whether the text is underline
* `overstrike`: whether the text is overstrike
* `justify`: justify mode of the text
* `default`: default value of the widget
* `command`: a function that is triggered when the button is pressed
* `image`: image of the widget
* `anchor`: anchor of the widget
* `align`: align of the widget
* `capture_events`: wether detect another widget under the widget
* `gradient_animation`: wether enable gradient_animation
* `auto_update`: whether the theme manager update it automatically
* `style`: style of the widget


### 🟡`_close_options`


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _close_options(
    self,
    index: int | None = None,
) -> None: ...
```
Close the options

### 🟡`_extra_bind`


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _extra_bind(
    self,
    event,
) -> None: ...
```


### 🟡`_get_position`


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _get_position(
    self,
    align: typing.Literal['up', 'center', 'down'],
) -> tuple[int, int]: ...
```
Get the position of "pop-up" SegmentedButton

### 🟡`_open_options`


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _open_options(
    self,
) -> None: ...
```
Open the options

### 🟡`get`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def get(
    self,
) -> int | None: ...
```
Get the index of the child toggle button with a value of True. If not, None is
returned.

### 🟡`set`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def set(
    self,
    value: int | None,
    *,
    callback: bool = False,
) -> None: ...
```
Activate the child toggle button for the specified index



## 🟢`ProgressBar`



<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code> | `Widget`


```python
def __init__(
    self,
    master: containers.Canvas | virtual.Widget,
    position: tuple[int, int],
    size: tuple[int, int] = (400, 20),
    *,
    default: float | None = None,
    command: collections.abc.Callable[[float], typing.Any] | None = None,
    image: enhanced.PhotoImage | None = None,
    anchor: typing.Literal['n', 'e', 'w', 's', 'nw', 'ne', 'sw', 'se', 'center'] = 'nw',
    capture_events: bool | None = None,
    gradient_animation: bool | None = None,
    auto_update: bool | None = None,
    style: type[virtual.Style] | None = None,
) -> None: ...
```
Progress bar widget, typically used to show the progress of an event

* `master`: parent canvas
* `position`: position of the widget
* `size`: size of the widget
* `default`: default value of the widget
* `command`: a function that is triggered when the progress of progress bar is 100%
* `image`: image of the widget
* `anchor`: anchor of the widget
* `capture_events`: wether detect another widget under the widget
* `gradient_animation`: wether enable gradient_animation
* `auto_update`: whether the theme manager update it automatically
* `style`: style of the widget


### 🟡`get`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def get(
    self,
) -> float: ...
```
Get the progress of the progress bar

### 🟡`set`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def set(
    self,
    value: float,
    *,
    callback: bool = False,
) -> None: ...
```
Set the progress of the progress bar



## 🟢`RadioBox`



<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code> | `Widget`


```python
def __init__(
    self,
    master: containers.Canvas | virtual.Widget,
    position: tuple[int, int],
    length: int = 30,
    *,
    default: bool | None = None,
    command: collections.abc.Callable[[int], typing.Any] | None = None,
    image: enhanced.PhotoImage | None = None,
    anchor: typing.Literal['n', 'e', 'w', 's', 'nw', 'ne', 'sw', 'se', 'center'] = 'nw',
    capture_events: bool | None = None,
    gradient_animation: bool | None = None,
    auto_update: bool | None = None,
    style: type[virtual.Style] | None = None,
) -> None: ...
```
Radio button widget, generally used to select one of several options

* `master`: parent canvas
* `position`: position of the widget
* `length`: length of the widget
* `default`: default state of the widget
* `command`: a function that is triggered when the state of radio button is on
* `image`: image of the widget
* `anchor`: anchor of the widget
* `capture_events`: wether detect another widget under the widget
* `gradient_animation`: wether enable gradient_animation
* `auto_update`: whether the theme manager update it automatically
* `style`: style of the widget


### 🟡`get`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def get(
    self,
) -> bool: ...
```
Get the state of the radio button

### 🟡`group`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def group(
    self,
    *radio_boxes: RadioBox,
) -> None: ...
```
Combine other radio boxes.

* `radio_boxes`: other radio boxes


### 🟡`set`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def set(
    self,
    value: bool,
    *,
    callback: bool = False,
) -> None: ...
```
Set the state of the radio button



## 🟢`SegmentedButton`



<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code> | `Widget`


```python
def __init__(
    self,
    master: containers.Canvas | virtual.Widget,
    position: tuple[int, int],
    sizes: tuple[tuple[int, int], ...] = (),
    *,
    text: tuple[str, ...] = (),
    family: str | None = None,
    fontsize: int | None = None,
    weight: typing.Literal['normal', 'bold'] = 'normal',
    slant: typing.Literal['roman', 'italic'] = 'roman',
    underline: bool = False,
    overstrike: bool = False,
    justify: typing.Literal['left', 'center', 'right'] = 'left',
    default: int | None = None,
    command: collections.abc.Callable[[int | None], typing.Any] | None = None,
    image: tuple[enhanced.PhotoImage | None, ...] = (),
    layout: typing.Literal['horizontal', 'vertical'] = 'horizontal',
    anchor: typing.Literal['n', 'e', 'w', 's', 'nw', 'ne', 'sw', 'se', 'center'] = 'nw',
    capture_events: bool | None = None,
    gradient_animation: bool | None = None,
    auto_update: bool | None = None,
    style: type[virtual.Style] | None = None,
) -> None: ...
```
A segmented button that can be used to toggle between multiple states

* `master`: parent canvas
* `position`: position of the widget
* `size`: size of the widget
* `text`: text of the widget
* `family`: font family
* `fontsize`: font size
* `weight`: weight of the text
* `slant`: slant of the text
* `underline`: whether the text is underline
* `overstrike`: whether the text is overstrike
* `justify`: justify mode of the text
* `default`: default value of the widget
* `command`: a function that is triggered when the button is pressed
* `image`: image of the widget
* `layout`: layout mode of the widget
* `anchor`: anchor of the widget
* `capture_events`: wether detect another widget under the widget
* `gradient_animation`: wether enable gradient_animation
* `auto_update`: whether the theme manager update it automatically
* `style`: style of the widget


### 🟡`get`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def get(
    self,
) -> int | None: ...
```
Get the index of the child toggle button with a value of True. If not, None is
returned.

### 🟡`set`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def set(
    self,
    value: int | None,
    *,
    callback: bool = False,
) -> None: ...
```
Activate the child toggle button for the specified index



## 🟢`Slider`



<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code> | `Widget`


```python
def __init__(
    self,
    master: containers.Canvas | virtual.Widget,
    position: tuple[int, int],
    size: tuple[int, int] = (400, 30),
    *,
    default: float | None = None,
    command: collections.abc.Callable[[float], typing.Any] | None = None,
    anchor: typing.Literal['n', 'e', 'w', 's', 'nw', 'ne', 'sw', 'se', 'center'] = 'nw',
    capture_events: bool | None = None,
    gradient_animation: bool | None = None,
    auto_update: bool | None = None,
    style: type[virtual.Style] | None = None,
) -> None: ...
```
A slider for visually resizing values

* `master`: parent canvas
* `position`: position of the widget
* `size`: size of the widget
* `default`: default value of the widget
* `command`: a function that is triggered when the button is pressed
* `anchor`: anchor of the widget
* `capture_events`: wether detect another widget under the widget
* `gradient_animation`: wether enable gradient_animation
* `auto_update`: whether the theme manager update it automatically
* `style`: style of the widget


### 🟡`get`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def get(
    self,
) -> float: ...
```
Get the value of the slider

### 🟡`set`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def set(
    self,
    value: float,
    *,
    callback: bool = False,
) -> None: ...
```
Set the value of the slider



## 🟢`SpinBox`



<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code> | `Widget`


```python
def __init__(
    self,
    master: containers.Canvas | virtual.Widget,
    position: tuple[int, int],
    size: tuple[int, int] | None = None,
    *,
    format_spec: str = 'd',
    step: int = 1,
    family: str | None = None,
    fontsize: int | None = None,
    weight: typing.Literal['normal', 'bold'] = 'normal',
    slant: typing.Literal['roman', 'italic'] = 'roman',
    underline: bool = False,
    overstrike: bool = False,
    align: typing.Literal['left', 'right', 'center'] = 'left',
    placeholder: str = '',
    show: str | None = None,
    limit: int = inf,
    default: str | None = None,
    command: collections.abc.Callable[[bool], typing.Any] | None = None,
    image: enhanced.PhotoImage | None = None,
    anchor: typing.Literal['n', 'e', 'w', 's', 'nw', 'ne', 'sw', 'se', 'center'] = 'nw',
    capture_events: bool | None = None,
    gradient_animation: bool | None = None,
    auto_update: bool | None = None,
    style: type[virtual.Style] | None = None,
) -> None: ...
```
A widget that makes it easy to enter numeric type data

* `master`: parent canvas
* `position`: position of the widget
* `size`: size of the widget
* `format_spec`: format of value
* `step`: value of each change
* `family`: font family
* `fontsize`: font size
* `weight`: weight of the text
* `slant`: slant of the text
* `underline`: whether the text is underline
* `overstrike`: whether the text is overstrike
* `align`: align mode of the text
* `show`: display a value that obscures the original content
* `placeholder`: a placeholder for the prompt
* `limit`: limit on the number of characters
* `default`: default value of the widget
* `command`: a function that is triggered when the button is pressed
* `image`: image of the widget
* `anchor`: anchor of the widget
* `capture_events`: wether detect another widget under the widget
* `gradient_animation`: wether enable gradient_animation
* `auto_update`: whether the theme manager update it automatically
* `style`: style of the widget


### 🟡`append`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def append(
    self,
    value: str,
) -> None: ...
```
Append text to Entry

### 🟡`change`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def change(
    self,
    up: bool,
) -> None: ...
```
Try change the current value

### 🟡`clear`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def clear(
    self,
) -> None: ...
```
Clear the text value of the Entry

### 🟡`delete`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def delete(
    self,
    count: int,
) -> None: ...
```
Delete a specified amount of text

### 🟡`get`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def get(
    self,
) -> str: ...
```
Get the value of the Entry

### 🟡`set`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def set(
    self,
    value: str,
) -> None: ...
```
Set the text value of the Entry



## 🟢`Spinner`



<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code> | `Widget`


```python
def __init__(
    self,
    master: containers.Canvas | virtual.Widget,
    position: tuple[int, int],
    size: tuple[int, int] = (30, 30),
    *,
    default: float | None = None,
    command: collections.abc.Callable[[float], typing.Any] | None = None,
    widths: tuple[int, int] | None = None,
    mode: typing.Literal['determinate', 'indeterminate'] = 'determinate',
    anchor: typing.Literal['n', 'e', 'w', 's', 'nw', 'ne', 'sw', 'se', 'center'] = 'nw',
    capture_events: bool | None = None,
    gradient_animation: bool | None = None,
    auto_update: bool | None = None,
    style: type[virtual.Style] | None = None,
) -> None: ...
```
Spinners visually communicate that something is processing

* `master`: parent canvas
* `position`: position of the widget
* `size`: size of the widget
* `default`: default value of the widget
* `command`: a function that is triggered when the progress of progress bar is 100%
* `widths`: width of the outside ring and inside ring
* `mode`: mode of the Spinner
* `anchor`: anchor of the widget
* `capture_events`: wether detect another widget under the widget
* `gradient_animation`: wether enable gradient_animation
* `auto_update`: whether the theme manager update it automatically
* `style`: style of the widget


### 🟡`destroy`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def destroy(
    self,
) -> None: ...
```
Destroy the widget

### 🟡`get`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def get(
    self,
) -> float: ...
```
Get the progress of the Spinner

### 🟡`set`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def set(
    self,
    value: float,
    *,
    callback: bool = False,
) -> None: ...
```
Set the progress of the Spinner



## 🟢`Switch`



<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code> | `Widget`


```python
def __init__(
    self,
    master: containers.Canvas | virtual.Widget,
    position: tuple[int, int],
    length: int = 60,
    *,
    default: bool | None = None,
    command: collections.abc.Callable[[bool], typing.Any] | None = None,
    image: enhanced.PhotoImage | None = None,
    anchor: typing.Literal['n', 'e', 'w', 's', 'nw', 'ne', 'sw', 'se', 'center'] = 'nw',
    capture_events: bool | None = None,
    gradient_animation: bool | None = None,
    auto_update: bool | None = None,
    style: type[virtual.Style] | None = None,
) -> None: ...
```
Switch widget, typically used to control the turning of a function on and off

* `master`: parent canvas
* `position`: position of the widget
* `length`: length of the widget
* `default`: default value of the widget
* `command`: a function that is triggered when the switch is changed
* `image`: image of the widget
* `anchor`: anchor of the widget
* `capture_events`: wether detect another widget under the widget
* `gradient_animation`: wether enable gradient_animation
* `auto_update`: whether the theme manager update it automatically
* `style`: style of the widget


### 🟡`get`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def get(
    self,
) -> bool: ...
```
Get the state of the switch

### 🟡`set`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def set(
    self,
    value: bool,
    *,
    callback: bool = False,
) -> None: ...
```
Set the state of the switch



## 🟢`Text`



<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code> | `Widget`


```python
def __init__(
    self,
    master: containers.Canvas | virtual.Widget,
    position: tuple[int, int],
    *,
    text: str = '',
    family: str | None = None,
    fontsize: int | None = None,
    weight: typing.Literal['normal', 'bold'] = 'normal',
    slant: typing.Literal['roman', 'italic'] = 'roman',
    underline: bool = False,
    overstrike: bool = False,
    justify: typing.Literal['left', 'center', 'right'] = 'left',
    anchor: typing.Literal['n', 'e', 'w', 's', 'nw', 'ne', 'sw', 'se', 'center'] = 'nw',
    capture_events: bool | None = None,
    gradient_animation: bool | None = None,
    auto_update: bool | None = None,
    style: type[virtual.Style] | None = None,
) -> None: ...
```
Text widget, generally used to display plain text

* `master`: parent canvas
* `position`: position of the widget
* `text`: text of the widget
* `family`: font family
* `fontsize`: font size
* `weight`: weight of the text
* `slant`: slant of the text
* `underline`: whether the text is underline
* `overstrike`: whether the text is overstrike
* `justify`: justify mode of the text
* `anchor`: anchor of the widget
* `capture_events`: wether detect another widget under the widget
* `gradient_animation`: wether enable gradient_animation
* `auto_update`: whether the theme manager update it automatically
* `style`: style of the widget


### 🟡`get`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def get(
    self,
) -> str: ...
```
Get the text of the widget

### 🟡`set`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def set(
    self,
    text: str,
) -> None: ...
```
Set the text of the widget



## 🟢`ToggleButton`



<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code> | `Widget`


```python
def __init__(
    self,
    master: containers.Canvas | virtual.Widget,
    position: tuple[int, int],
    size: tuple[int, int] | None = None,
    *,
    text: str = '',
    family: str | None = None,
    fontsize: int | None = None,
    weight: typing.Literal['normal', 'bold'] = 'normal',
    slant: typing.Literal['roman', 'italic'] = 'roman',
    underline: bool = False,
    overstrike: bool = False,
    justify: typing.Literal['left', 'center', 'right'] = 'left',
    default: bool | None = None,
    command: collections.abc.Callable[[bool], typing.Any] | None = None,
    image: enhanced.PhotoImage | None = None,
    anchor: typing.Literal['n', 'e', 'w', 's', 'nw', 'ne', 'sw', 'se', 'center'] = 'nw',
    capture_events: bool | None = None,
    gradient_animation: bool | None = None,
    auto_update: bool | None = None,
    style: type[virtual.Style] | None = None,
) -> None: ...
```
A button that can display information and switch statuses

* `master`: parent canvas
* `position`: position of the widget
* `size`: size of the widget
* `text`: text of the widget
* `family`: font family
* `fontsize`: font size
* `weight`: weight of the text
* `slant`: slant of the text
* `underline`: whether the text is underline
* `overstrike`: whether the text is overstrike
* `justify`: justify mode of the text
* `default`: default state of the widget
* `command`: a function that is triggered when the state of check button is on
* `image`: image of the widget
* `anchor`: anchor of the widget
* `capture_events`: wether detect another widget under the widget
* `gradient_animation`: wether enable gradient_animation
* `auto_update`: whether the theme manager update it automatically
* `style`: style of the widget


### 🟡`get`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def get(
    self,
) -> bool: ...
```
Get the state of the check button

### 🟡`set`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def set(
    self,
    value: bool,
    *,
    callback: bool = False,
) -> None: ...
```
Set the state of the switch



## 🟢`Tooltip`



<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code> | `Widget`


```python
def __init__(
    self,
    widget: virtual.Widget,
    size: tuple[int, int] | None = None,
    *,
    text: str = '',
    align: typing.Literal['up', 'down', 'right', 'left', 'center'] = 'down',
    padding: int = 3,
    family: str | None = None,
    fontsize: int | None = None,
    weight: typing.Literal['normal', 'bold'] = 'normal',
    slant: typing.Literal['roman', 'italic'] = 'roman',
    underline: bool = False,
    overstrike: bool = False,
    justify: typing.Literal['left', 'center', 'right'] = 'left',
    gradient_animation: bool | None = None,
    auto_update: bool | None = None,
    style: type[virtual.Style] | None = None,
) -> None: ...
```
A tooltip that can display additional information

* `widget`: the associated widget
* `size`: size of the widget
* `text`: text of the widget
* `align`: align mode of the tooltip
* `padding`: extra padding between tooltip and the associated widget
* `family`: font family
* `fontsize`: font size
* `weight`: weight of the text
* `slant`: slant of the text
* `underline`: whether the text is underline
* `overstrike`: whether the text is overstrike
* `justify`: justify mode of the text
* `gradient_animation`: wether enable gradient_animation
* `auto_update`: whether the theme manager update it automatically
* `style`: style of the widget


### 🟡`_display`


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _display(
    self,
    state: str | None,
    _: bool,
) -> None: ...
```
Show or hide the tooltip



## 🟢`UnderlineButton`



<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code> | `Widget`


```python
def __init__(
    self,
    master: containers.Canvas | virtual.Widget,
    position: tuple[int, int],
    *,
    text: str = '',
    family: str | None = None,
    fontsize: int | None = None,
    weight: typing.Literal['normal', 'bold'] = 'normal',
    slant: typing.Literal['roman', 'italic'] = 'roman',
    underline: bool = False,
    overstrike: bool = False,
    justify: typing.Literal['left', 'center', 'right'] = 'left',
    command: collections.abc.Callable | None = None,
    image: enhanced.PhotoImage | None = None,
    anchor: typing.Literal['n', 'e', 'w', 's', 'nw', 'ne', 'sw', 'se', 'center'] = 'nw',
    capture_events: bool | None = None,
    gradient_animation: bool = False,
    auto_update: bool | None = None,
    style: type[virtual.Style] | None = None,
) -> None: ...
```
Underline button, generally used to display web links

* `master`: parent canvas
* `position`: position of the widget
* `text`: text of the widget
* `family`: font family
* `fontsize`: font size
* `weight`: weight of the text
* `slant`: slant of the text
* `underline`: whether the text is underline
* `overstrike`: whether the text is overstrike
* `justify`: justify mode of the text
* `command`: a function that is triggered when the underline button is pressed
* `image`: image of the widget
* `anchor`: anchor of the widget
* `capture_events`: wether detect another widget under the widget
* `gradient_animation`: wether enable gradient_animation
* `auto_update`: whether the theme manager update it automatically
* `style`: style of the widget




