# tkintertools.color.rgb

Support for RGB

## 🔵 函数

### <big>`_str_to_rgba`</big>


<code style='color: royalblue;'>function</code> <code style='color: orange;'>protected</code>

```python
def _str_to_rgba(
    color: str,
    *,
    reference: str,
) -> tuple[int, int, int]: ...
```
Experimental: Convert color strings(RGBA) to RGB codes

### <big>`_str_to_rgba`</big>


<code style='color: royalblue;'>function</code> <code style='color: orange;'>protected</code>

```python
def _str_to_rgba(
    color: str,
    *,
    reference: str,
) -> tuple[int, int, int]: ...
```
Experimental: Convert color strings(RGBA) to RGB codes

### <big>`blend`</big>


<code style='color: royalblue;'>function</code> <code style='color: green;'>public</code>

```python
def blend(
    colors: list[tuple[int, int, int]],
    *,
    weights: list[tuple] | None = None,
) -> tuple[int, int, int]: ...
```

Mix colors by weight

* `colors`: color list
* `weights`: weight list


### <big>`contrast`</big>


<code style='color: royalblue;'>function</code> <code style='color: green;'>public</code>

```python
def contrast(
    rgb: tuple[int, int, int],
    *,
    channels: tuple[bool, bool, bool] = (True, True, True),
) -> tuple[int, int, int]: ...
```

Get a contrasting color of a color

* `rgb`: a tuple, RGB codes
* `channels`: three color channels


### <big>`convert`</big>


<code style='color: royalblue;'>function</code> <code style='color: green;'>public</code>

```python
def convert(
    first: tuple[int, int, int],
    second: tuple[int, int, int],
    rate: float,
    *,
    channels: tuple[bool, bool, bool] = (True, True, True),
) -> tuple[int, int, int]: ...
```

Convert one color to another proportionally

* `first`: first color
* `second`: second color
* `rate`: conversion rate
* `channels`: three color channels


### <big>`gradient`</big>


<code style='color: royalblue;'>function</code> <code style='color: green;'>public</code>

```python
def gradient(
    first: tuple[int, int, int],
    second: tuple[int, int, int],
    count: int,
    rate: float = 1,
    *,
    channels: tuple[bool, bool, bool] = (True, True, True),
    contoller: typing.Callable[[float], float] = flat,
) -> list[tuple[int, int, int]]: ...
```

Get a list of color gradients from one color to another proportionally

* `first`: first color
* `second`: second color
* `count`: number of gradients
* `rate`: conversion rate
* `channels`: three color channels
* `controller`: control function


### <big>`rgb_to_str`</big>


<code style='color: royalblue;'>function</code> <code style='color: green;'>public</code>

```python
def rgb_to_str(
    rgb: tuple[int, int, int],
) -> str: ...
```
Convert RGB codes to color strings

### <big>`rgb_to_str`</big>


<code style='color: royalblue;'>function</code> <code style='color: green;'>public</code>

```python
def rgb_to_str(
    rgb: tuple[int, int, int],
) -> str: ...
```
Convert RGB codes to color strings

### <big>`str_to_rgb`</big>


<code style='color: royalblue;'>function</code> <code style='color: green;'>public</code>

```python
def str_to_rgb(
    color: str,
) -> tuple[int, int, int]: ...
```
Convert color strings to RGB codes

### <big>`str_to_rgb`</big>


<code style='color: royalblue;'>function</code> <code style='color: green;'>public</code>

```python
def str_to_rgb(
    color: str,
) -> tuple[int, int, int]: ...
```
Convert color strings to RGB codes

## 🟡 变量

### <big>`MAX`</big>


<code style='color: skyblue;'>constant</code> <code style='color: green;'>public</code>

```python linenums="0"
MAX: tuple = (
    255, 255, 255,
)
```


### <big>`RGB`</big>


<code style='color: skyblue;'>constant</code> <code style='color: green;'>public</code>

```python linenums="0"
RGB: GenericAlias = tuple[int, int, int]
```


