# tkintertools.standard.texts

All standard Texts

## 🟢 Classes / 类

### <big>`Information`</big>



<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code> | `Text`

#### <big>`append`</big>


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def append(
    self,
    text: str,
) -> None: ...
```
Append value to the value of `Text`

#### <big>`clear`</big>


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def clear(
    self,
) -> None: ...
```
Clear the value of `Text`

#### <big>`coords`</big>


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def coords(
    self,
    size: tuple[float, float] | None = None,
    position: tuple[float, float] | None = None,
) -> None: ...
```


#### <big>`delete`</big>


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def delete(
    self,
    num: int,
) -> None: ...
```
Remove a portion of the `Text` value from the trail

#### <big>`display`</big>


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def display(
    self,
) -> None: ...
```


#### <big>`get`</big>


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def get(
    self,
) -> str: ...
```
Get the value of `Text`

#### <big>`set`</big>


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def set(
    self,
    text: str,
) -> None: ...
```
Set the value of `Text`



### <big>`SingleLineText`</big>



<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code> | `Text`


```python
def __init__(
    self,
    widget: Widget,
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


#### <big>`_move_left`</big>


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _move_left(
    self,
) -> None: ...
```
Move the text to the left as a whole, i.e. press the right arrow

#### <big>`_move_right`</big>


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _move_right(
    self,
) -> None: ...
```
Move the text to the right as a whole, i.e. press the left arrow

#### <big>`_text_delete`</big>


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _text_delete(
    self,
    start: int,
    end: typing.Union[int, typing.Literal['end']],
) -> None: ...
```
Delete the actual text that appears on the component

#### <big>`_text_get`</big>


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _text_get(
    self,
) -> str: ...
```
Get the actual text that appears on the component

#### <big>`_text_insert`</big>


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _text_insert(
    self,
    index: int,
    value: str,
) -> None: ...
```
Insert the actual text that appears on the component

#### <big>`_text_length`</big>


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _text_length(
    self,
) -> int: ...
```
Get the length of actual text that appears on the component

#### <big>`_text_overflow`</big>


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _text_overflow(
    self,
) -> bool: ...
```
Whether the text content extends beyond the text box

#### <big>`_text_set`</big>


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _text_set(
    self,
    value: str,
) -> None: ...
```
Set the actual text that appears on the component

#### <big>`append`</big>


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def append(
    self,
    value: str,
) -> None: ...
```
Add some characters to the text cursor

#### <big>`coords`</big>


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def coords(
    self,
    size: tuple[float, float] | None = None,
    position: tuple[float, float] | None = None,
) -> None: ...
```


#### <big>`cursor_find`</big>


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def cursor_find(
    self,
    x: int,
) -> int: ...
```
Return the index of text with the x position of mouse

#### <big>`cursor_get`</big>


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def cursor_get(
    self,
) -> int: ...
```
Get the index position of the text cursor

#### <big>`cursor_move`</big>


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def cursor_move(
    self,
    count: int,
) -> None: ...
```
Move the index position of the text cursor

#### <big>`cursor_move_to`</big>


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def cursor_move_to(
    self,
    count: int,
) -> None: ...
```
Move the index position of the text cursor to a certain index

#### <big>`cursor_set`</big>


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def cursor_set(
    self,
    index: int,
) -> int: ...
```
Set the index position of the text cursor

#### <big>`delete`</big>


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def delete(
    self,
    start: int,
    end: int,
) -> None: ...
```
Delete text within the specified index range, [start, end]

#### <big>`display`</big>


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def display(
    self,
) -> None: ...
```


#### <big>`get`</big>


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def get(
    self,
) -> str: ...
```
Get text of the component

#### <big>`get_gap`</big>


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def get_gap(
    self,
) -> float: ...
```
Get the size of the spacing between the text and the border

#### <big>`insert`</big>


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def insert(
    self,
    index: int,
    value: str,
) -> None: ...
```
Insert text to the location of the specified index

#### <big>`pop`</big>


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def pop(
    self,
) -> None: ...
```
Delete a character at the text cursor

#### <big>`select_all`</big>


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def select_all(
    self,
) -> None: ...
```
Select all texts

#### <big>`select_clear`</big>


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def select_clear(
    self,
) -> None: ...
```
Clear the selected text

#### <big>`select_get`</big>


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def select_get(
    self,
) -> tuple[int, int] | None: ...
```
Get the index tuple of the selected text

#### <big>`select_set`</big>


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def select_set(
    self,
    start: int,
    end: int,
) -> None: ...
```
Set the index tuple of the selected text, [start, end]

#### <big>`set`</big>


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def set(
    self,
    value: str,
) -> None: ...
```
Set text of the component



