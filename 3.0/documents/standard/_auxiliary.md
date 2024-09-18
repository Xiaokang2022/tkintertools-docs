# tkintertools.standard._auxiliary

Some auxiliary classes

## 🟢`_AuxiliaryButton`



<code style='color: limegreen;'>class</code> <code style='color: orange;'>protected</code> | `Widget`


```python
def __init__(
    self,
    master: Canvas,
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
    anchor: typing.Literal['n', 'e', 'w', 's', 'nw', 'ne', 'sw', 'se', 'center'] = 'center',
    command: typing.Optional[typing.Callable] = None,
    image: tkintertools.toolbox.enhanced.PhotoImage | None = None,
    ignore: typing.Literal['left', 'right'] = 'left',
    name: str | None = None,
    through: bool = False,
    animation: bool = True,
) -> None: ...
```





## 🟢`_AuxiliaryInputBox`



<code style='color: limegreen;'>class</code> <code style='color: orange;'>protected</code> | `Widget`


```python
def __init__(
    self,
    master: Canvas,
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
    image: tkintertools.toolbox.enhanced.PhotoImage | None = None,
    ignore: typing.Literal['left', 'right'] = 'left',
    name: str | None = None,
    through: bool = False,
    animation: bool = True,
) -> None: ...
```



### 🟡`append`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def append(
    self,
    value: str,
) -> None: ...
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



## 🟢`_AuxiliaryLabel`



<code style='color: limegreen;'>class</code> <code style='color: orange;'>protected</code> | `Widget`


```python
def __init__(
    self,
    master: Canvas,
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
    anchor: typing.Literal['n', 'e', 'w', 's', 'nw', 'ne', 'sw', 'se', 'center'] = 'center',
    image: tkintertools.toolbox.enhanced.PhotoImage | None = None,
    ignore: typing.Literal['left', 'right'] = 'left',
    name: str | None = None,
    through: bool = False,
    animation: bool = True,
) -> None: ...
```





