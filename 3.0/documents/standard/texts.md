# tkintertools.standard.texts

All standard `Text` classes

## 🟢`Information`



<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code> | `Text`

### 🟡`append`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def append(
    self,
    text: str,
) -> None: ...
```
Append value to the value of `Text`

### 🟡`clear`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def clear(
    self,
) -> None: ...
```
Clear the value of `Text`

### 🟡`coords`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def coords(
    self,
    size: tuple[float, float] | None = None,
    position: tuple[float, float] | None = None,
) -> None: ...
```
Resize the `Component`

### 🟡`delete`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def delete(
    self,
    num: int,
) -> None: ...
```
Remove a portion of the `Text` value from the trail

### 🟡`display`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def display(
    self,
) -> None: ...
```
Display the `Component` on a `Canvas`

### 🟡`get`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def get(
    self,
) -> str: ...
```
Get the value of `Text`

### 🟡`set`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def set(
    self,
    text: str,
) -> None: ...
```
Set the value of `Text`



## 🟢`SingleLineText`



<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code> | `Text`


```python
def __init__(
    self,
    widget: virtual.Widget,
    relative_position: tuple[int, int] = (0, 0),
    size: tuple[int, int] | None = None,
    *,
    text: str = '',
    limit: int = inf,
    show: str | None = None,
    placeholder: str = '',
    align: typing.Literal['left', 'center', 'right'] = 'left',
    family: str | None = None,
    fontsize: int | None = None,
    weight: typing.Literal['normal', 'bold'] = 'normal',
    slant: typing.Literal['roman', 'italic'] = 'roman',
    underline: bool = False,
    overstrike: bool = False,
    name: str | None = None,
    animation: bool = True,
    styles: dict[str, dict[str, str]] | None = None,
    **kwargs,
) -> None: ...
```
Single-line editable text

* `widget`: parent widget
* `relative_position`: position relative to its widgets
* `size`: size of component
* `text`: text value
* `family`: font family
* `fontsize`: font size
* `weight`: weight of the font
* `slant`: slant of the font
* `underline`: wether text is underline
* `overstrike`: wether text is overstrike
* `align`: align mode of the text
* `limit`: limit on the number of characters
* `show`: display a value that obscures the original content
* `placeholder`: a placeholder for the prompt
* `name`: name of component
* `animation`: Wether use animation to change color
* `styles`: style dict of component
* `kwargs`: extra parameters for CanvasItem


### 🟡`_get_index`


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _get_index(
    self,
    index: int,
) -> int: ...
```


### 🟡`_get_margin`


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _get_margin(
    self,
) -> float: ...
```
Get the size of the spacing between the text and the border

### 🟡`_is_overflow`


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _is_overflow(
    self,
) -> bool: ...
```
Whether the text content extends beyond the text box

### 🟡`_move_left`


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _move_left(
    self,
) -> None: ...
```
Move the text to the left as a whole, i.e. press the right arrow

### 🟡`_move_right`


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _move_right(
    self,
) -> None: ...
```
Move the text to the right as a whole, i.e. press the left arrow

### 🟡`append`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def append(
    self,
    value: str,
) -> bool: ...
```
Add some characters to the text cursor

### 🟡`clear`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def clear(
    self,
) -> None: ...
```
Clear

### 🟡`coords`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def coords(
    self,
    size: tuple[float, float] | None = None,
    position: tuple[float, float] | None = None,
) -> None: ...
```
Resize the `Component`

### 🟡`cursor_move`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def cursor_move(
    self,
    count: int,
) -> None: ...
```
Move the index position of the text cursor

### 🟡`cursor_move_to`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def cursor_move_to(
    self,
    count: int,
) -> None: ...
```
Move the index position of the text cursor to a certain index

### 🟡`display`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def display(
    self,
) -> None: ...
```
Display the `Component` on a `Canvas`

### 🟡`get`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def get(
    self,
) -> str: ...
```
Get text of the component

### 🟡`insert`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def insert(
    self,
    index: int,
    value: str,
) -> bool: ...
```
Insert text to the location of the specified index

### 🟡`pop`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def pop(
    self,
    index: int = -1,
) -> str: ...
```
Delete a character at the text cursor

### 🟡`remove`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def remove(
    self,
    start: int,
    end: int | None = None,
) -> None: ...
```
Remove text within the specified index range

### 🟡`set`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def set(
    self,
    value: str,
) -> bool: ...
```
Set text of the component



## 🟢`_CanvasTextProxy`



<code style='color: limegreen;'>class</code> <code style='color: orange;'>protected</code> | `object`

### 🟡`__init__`


<code style='color: #BBBB00;'>method</code> <code style='color: purple;'>special</code>

```python
def __init__(
    self,
    canvas: containers.Canvas,
    tag_or_id: str | int,
) -> None: ...
```


### 🟡`_get_index`


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _get_index(
    self,
    index: int,
) -> int: ...
```


### 🟡`append`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def append(
    self,
    value: str,
    *,
    show: str | None = None,
) -> None: ...
```
Append

### 🟡`clear`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def clear(
    self,
) -> None: ...
```
Clear

### 🟡`cursor_find`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def cursor_find(
    self,
    x: int,
) -> int: ...
```
cursor find

### 🟡`cursor_get`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def cursor_get(
    self,
) -> int | None: ...
```
cursor get

### 🟡`cursor_set`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def cursor_set(
    self,
    index: int,
) -> None: ...
```
cursor set

### 🟡`get`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def get(
    self,
) -> str: ...
```
Get

### 🟡`insert`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def insert(
    self,
    index: int,
    value: str,
    *,
    show: str | None = None,
) -> None: ...
```
Insert

### 🟡`length`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def length(
    self,
) -> int: ...
```
Length

### 🟡`pop`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def pop(
    self,
    index: int = -1,
) -> None: ...
```
Pop

### 🟡`remove`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def remove(
    self,
    start: int,
    end: int | None = None,
) -> None: ...
```
Remove

### 🟡`select_all`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def select_all(
    self,
) -> None: ...
```
select all

### 🟡`select_clear`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def select_clear(
    self,
) -> None: ...
```
select clear

### 🟡`select_get`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def select_get(
    self,
) -> tuple[int, int] | None: ...
```
select get

### 🟡`select_set`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def select_set(
    self,
    start: int,
    end: int | None = None,
) -> None: ...
```
select set

### 🟡`set`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def set(
    self,
    value: str,
    *,
    show: str | None = None,
) -> None: ...
```
Set



