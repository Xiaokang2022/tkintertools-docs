# tkintertools.standard.widgets

<small>:octicons-mark-github-16: 源代码：[`tkintertools/standard/widgets.py`](https://github.com/Xiaokang2022/tkintertools/blob/3.0.0rc4/tkintertools/standard/widgets.py){ target='_blank' }</small>

All standard `Widget` classes

## 🟢`Button`



<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code> | `Widget`


```python
def __init__(
    self,
    master: containers.Canvas,
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
    command: typing.Callable | None = None,
    image: enhanced.PhotoImage | None = None,
    name: str | None = None,
    anchor: typing.Literal['n', 'e', 'w', 's', 'nw', 'ne', 'sw', 'se', 'center'] = 'nw',
    through: bool = False,
    animation: bool = True,
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
* `name`: name of the widget
* `anchor`: anchor of the widget
* `through`: wether detect another widget under the widget
* `animation`: wether enable animation




## 🟢`CheckButton`



<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code> | `Widget`


```python
def __init__(
    self,
    master: containers.Canvas,
    position: tuple[int, int],
    length: int = 30,
    *,
    default: bool | None = None,
    command: typing.Callable[[bool], typing.Any] | None = None,
    image: enhanced.PhotoImage | None = None,
    name: str | None = None,
    anchor: typing.Literal['n', 'e', 'w', 's', 'nw', 'ne', 'sw', 'se', 'center'] = 'nw',
    through: bool = False,
    animation: bool = True,
) -> None: ...
```
Checkbox button widget, generally used to check some options

* `master`: parent canvas
* `position`: position of the widget
* `length`: length of the widget
* `default`: default state of the widget
* `command`: a function that is triggered when the state of check
button is on
* `image`: image of the widget
* `name`: name of the widget
* `anchor`: anchor of the widget
* `through`: wether detect another widget under the widget
* `animation`: wether enable animation


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



## 🟢`HighlightButton`



<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code> | `Widget`


```python
def __init__(
    self,
    master: containers.Canvas,
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
    command: typing.Callable | None = None,
    image: enhanced.PhotoImage | None = None,
    name: str | None = None,
    anchor: typing.Literal['n', 'e', 'w', 's', 'nw', 'ne', 'sw', 'se', 'center'] = 'nw',
    through: bool = False,
    animation: bool = True,
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
* `command`: a function that is triggered when the hightlight button
is pressed
* `image`: image of the widget
* `name`: name of the widget
* `anchor`: anchor of the widget
* `through`: wether detect another widget under the widget
* `animation`: wether enable animation




## 🟢`IconButton`



<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code> | `Widget`


```python
def __init__(
    self,
    master: containers.Canvas,
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
    command: typing.Callable | None = None,
    image: enhanced.PhotoImage | None = None,
    name: str | None = None,
    anchor: typing.Literal['n', 'e', 'w', 's', 'nw', 'ne', 'sw', 'se', 'center'] = 'nw',
    through: bool = False,
    animation: bool = True,
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
* `name`: name of the widget
* `anchor`: anchor of the widget
* `through`: wether detect another widget under the widget
* `animation`: wether enable animation




## 🟢`Image`



<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code> | `Widget`


```python
def __init__(
    self,
    master: containers.Canvas,
    position: tuple[int, int],
    size: tuple[int, int] | None = None,
    *,
    image: enhanced.PhotoImage | None = None,
    name: str | None = None,
    anchor: typing.Literal['n', 'e', 'w', 's', 'nw', 'ne', 'sw', 'se', 'center'] = 'nw',
    through: bool = False,
    animation: bool = True,
) -> None: ...
```
Image widget, generally used to display normal still image

* `master`: parent canvas
* `position`: position of the widget
* `size`: size of the widget
* `image`: image of the widget
* `name`: name of the widget
* `anchor`: anchor of the widget
* `through`: wether detect another widget under the widget
* `animation`: wether enable animation


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
    master: containers.Canvas,
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
    image: enhanced.PhotoImage | None = None,
    name: str | None = None,
    anchor: typing.Literal['n', 'e', 'w', 's', 'nw', 'ne', 'sw', 'se', 'center'] = 'nw',
    through: bool = False,
    animation: bool = True,
) -> None: ...
```
Input box widget, generally used to enter certain information on a
single line

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
* `image`: image of the widget
* `name`: name of the widget
* `anchor`: anchor of the widget
* `through`: wether detect another widget under the widget
* `animation`: wether enable animation


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
    master: containers.Canvas,
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
    name: str | None = None,
    anchor: typing.Literal['n', 'e', 'w', 's', 'nw', 'ne', 'sw', 'se', 'center'] = 'nw',
    through: bool = False,
    animation: bool = True,
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
* `name`: name of the widget
* `anchor`: anchor of the widget
* `through`: wether detect another widget under the widget
* `animation`: wether enable animation




## 🟢`ProgressBar`



<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code> | `Widget`


```python
def __init__(
    self,
    master: containers.Canvas,
    position: tuple[int, int],
    size: tuple[int, int] = (400, 20),
    *,
    default: float | None = None,
    command: typing.Callable[[float], typing.Any] | None = None,
    image: enhanced.PhotoImage | None = None,
    name: str | None = None,
    anchor: typing.Literal['n', 'e', 'w', 's', 'nw', 'ne', 'sw', 'se', 'center'] = 'nw',
    through: bool = False,
    animation: bool = True,
) -> None: ...
```
Progress bar widget, typically used to show the progress of an event

* `master`: parent canvas
* `position`: position of the widget
* `size`: size of the widget
* `default`: default value of the widget
* `command`: a function that is triggered when the progress of progress
bar is 100%
* `image`: image of the widget
* `name`: name of the widget
* `anchor`: anchor of the widget
* `through`: wether detect another widget under the widget
* `animation`: wether enable animation


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



## 🟢`RadioButton`



<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code> | `Widget`


```python
def __init__(
    self,
    master: containers.Canvas,
    position: tuple[int, int],
    length: int = 30,
    *,
    default: bool | None = None,
    command: typing.Callable[[int], typing.Any] | None = None,
    image: enhanced.PhotoImage | None = None,
    name: str | None = None,
    anchor: typing.Literal['n', 'e', 'w', 's', 'nw', 'ne', 'sw', 'se', 'center'] = 'nw',
    through: bool = False,
    animation: bool = True,
) -> None: ...
```
Radio button widget, generally used to select one of several options

* `master`: parent canvas
* `position`: position of the widget
* `length`: length of the widget
* `default`: default state of the widget
* `command`: a function that is triggered when the state of radio
button is on
* `image`: image of the widget
* `name`: name of the widget
* `anchor`: anchor of the widget
* `through`: wether detect another widget under the widget
* `animation`: wether enable animation


### 🟡`get`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def get(
    self,
) -> bool: ...
```
Get the state of the radio button

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
    master: containers.Canvas,
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
    command: typing.Callable[[int | None], typing.Any] | None = None,
    image: tuple[enhanced.PhotoImage | None, ...] = (),
    layout: typing.Literal['horizontal', 'vertical'] = 'horizontal',
    name: str | None = None,
    anchor: typing.Literal['n', 'e', 'w', 's', 'nw', 'ne', 'sw', 'se', 'center'] = 'nw',
    through: bool = False,
    animation: bool = True,
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
* `name`: name of the widget
* `anchor`: anchor of the widget
* `through`: wether detect another widget under the widget
* `animation`: wether enable animation


### 🟡`get`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def get(
    self,
) -> int | None: ...
```
Get the index of the child toggle button with a value of True. If
not, None is returned.

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
    master: containers.Canvas,
    position: tuple[int, int],
    size: tuple[int, int] = (400, 30),
    *,
    default: float | None = None,
    command: typing.Callable[[float], typing.Any] | None = None,
    name: str | None = None,
    anchor: typing.Literal['n', 'e', 'w', 's', 'nw', 'ne', 'sw', 'se', 'center'] = 'nw',
    through: bool = False,
    animation: bool = True,
) -> None: ...
```
A slider for visually resizing values

* `master`: parent canvas
* `position`: position of the widget
* `size`: size of the widget
* `default`: default value of the widget
* `command`: a function that is triggered when the button is pressed
* `name`: name of the widget
* `anchor`: anchor of the widget
* `through`: wether detect another widget under the widget
* `animation`: wether enable animation


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
    master: containers.Canvas,
    position: tuple[int, int],
    size: tuple[int, int] | None = None,
    *,
    style: str = 'd',
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
    command: typing.Callable[[bool], typing.Any] | None = None,
    image: enhanced.PhotoImage | None = None,
    name: str | None = None,
    anchor: typing.Literal['n', 'e', 'w', 's', 'nw', 'ne', 'sw', 'se', 'center'] = 'nw',
    through: bool = False,
    animation: bool = True,
) -> None: ...
```
A widget that makes it easy to enter numeric type data

* `master`: parent canvas
* `position`: position of the widget
* `size`: size of the widget
* `style`: format of value
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
* `command`: a function that is triggered when the button is pressed
* `image`: image of the widget
* `name`: name of the widget
* `anchor`: anchor of the widget
* `through`: wether detect another widget under the widget
* `animation`: wether enable animation


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



## 🟢`Switch`



<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code> | `Widget`


```python
def __init__(
    self,
    master: containers.Canvas,
    position: tuple[int, int],
    length: int = 60,
    *,
    default: bool | None = None,
    command: typing.Callable[[bool], typing.Any] | None = None,
    image: enhanced.PhotoImage | None = None,
    name: str | None = None,
    anchor: typing.Literal['n', 'e', 'w', 's', 'nw', 'ne', 'sw', 'se', 'center'] = 'nw',
    through: bool = False,
    animation: bool = True,
) -> None: ...
```
Switch widget, typically used to control the turning of a function on
and off

* `master`: parent canvas
* `position`: position of the widget
* `length`: length of the widget
* `default`: default value of the widget
* `command`: a function that is triggered when the switch is changed
* `image`: image of the widget
* `name`: name of the widget
* `anchor`: anchor of the widget
* `through`: wether detect another widget under the widget
* `animation`: wether enable animation


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
    master: containers.Canvas,
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
    name: str | None = None,
    anchor: typing.Literal['n', 'e', 'w', 's', 'nw', 'ne', 'sw', 'se', 'center'] = 'nw',
    through: bool = False,
    animation: bool = True,
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
* `name`: name of the widget
* `anchor`: anchor of the widget
* `through`: wether detect another widget under the widget
* `animation`: wether enable animation


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
    master: containers.Canvas,
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
    command: typing.Callable[[bool], typing.Any] | None = None,
    image: enhanced.PhotoImage | None = None,
    name: str | None = None,
    anchor: typing.Literal['n', 'e', 'w', 's', 'nw', 'ne', 'sw', 'se', 'center'] = 'nw',
    through: bool = False,
    animation: bool = True,
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
* `command`: a function that is triggered when the state of check
button is on
* `image`: image of the widget
* `name`: name of the widget
* `anchor`: anchor of the widget
* `through`: wether detect another widget under the widget
* `animation`: wether enable animation


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
    name: str | None = None,
    through: bool = True,
    animation: bool = True,
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
* `name`: name of the widget
* `through`: wether detect another widget under the widget
* `animation`: wether enable animation


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
    master: containers.Canvas,
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
    command: typing.Callable | None = None,
    image: enhanced.PhotoImage | None = None,
    name: str | None = None,
    anchor: typing.Literal['n', 'e', 'w', 's', 'nw', 'ne', 'sw', 'se', 'center'] = 'nw',
    through: bool = False,
    animation: bool = False,
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
* `command`: a function that is triggered when the underline button
is pressed
* `image`: image of the widget
* `name`: name of the widget
* `anchor`: anchor of the widget
* `through`: wether detect another widget under the widget
* `animation`: wether enable animation




