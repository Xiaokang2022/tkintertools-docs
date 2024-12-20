# tkintertools.color.rgb

<small>:octicons-mark-github-16: 源代码：[`tkintertools/color/rgb.py`](https://github.com/Xiaokang2022/tkintertools/blob/3.0.0rc5/tkintertools/color/rgb.py){ target='_blank' }</small>

Support for RGB

## 🔵`blend`


<code style='color: royalblue;'>function</code> <code style='color: green;'>public</code>

```python
def blend(
    colors: list[RGB],
    *,
    weights: list[float] | None = None,
) -> RGB: ...
```
Mix colors by weight

* `colors`: color list
* `weights`: weight list


## 🔵`contrast`


<code style='color: royalblue;'>function</code> <code style='color: green;'>public</code>

```python
def contrast(
    rgb: RGB,
    *,
    channels: tuple[bool, bool, bool] = (True, True, True),
) -> RGB: ...
```
Get a contrasting color of a color

* `rgb`: a tuple, RGB codes
* `channels`: three color channels


## 🔵`convert`


<code style='color: royalblue;'>function</code> <code style='color: green;'>public</code>

```python
def convert(
    first: RGB,
    second: RGB,
    rate: float,
    *,
    channels: tuple[bool, bool, bool] = (True, True, True),
) -> RGB: ...
```
Convert one color to another proportionally

* `first`: first color
* `second`: second color
* `rate`: conversion rate
* `channels`: three color channels


## 🔵`gradient`


<code style='color: royalblue;'>function</code> <code style='color: green;'>public</code>

```python
def gradient(
    first: RGB,
    second: RGB,
    count: int,
    rate: float = 1,
    *,
    channels: tuple[bool, bool, bool] = (True, True, True),
    contoller: collections.abc.Callable[[int | float], int | float] = flat,
) -> list[RGB]: ...
```
Get a list of color gradients from one color to another proportionally

* `first`: first color
* `second`: second color
* `count`: number of gradients
* `rate`: conversion rate
* `channels`: three color channels
* `controller`: control function


## 🔵`rgb_to_str`


<code style='color: royalblue;'>function</code> <code style='color: green;'>public</code>

```python
def rgb_to_str(
    color: RGB,
) -> str: ...
```
Convert RGB codes to color strings

## 🔵`rgb_to_str`


<code style='color: royalblue;'>function</code> <code style='color: green;'>public</code>

```python
def rgb_to_str(
    color: RGB,
) -> str: ...
```
Convert RGB codes to color strings

## 🔵`str_to_rgb`


<code style='color: royalblue;'>function</code> <code style='color: green;'>public</code>

```python
def str_to_rgb(
    color: str,
) -> RGB: ...
```
Convert color strings to RGB codes

## 🔵`str_to_rgba`


<code style='color: royalblue;'>function</code> <code style='color: green;'>public</code>

```python
def str_to_rgba(
    color: str,
    *,
    reference: str,
) -> RGB: ...
```
Experimental: Convert color strings(RGBA) to RGB codes

## 🔵`str_to_rgb`


<code style='color: royalblue;'>function</code> <code style='color: green;'>public</code>

```python
def str_to_rgb(
    color: str,
) -> RGB: ...
```
Convert color strings to RGB codes

## 🔵`str_to_rgba`


<code style='color: royalblue;'>function</code> <code style='color: green;'>public</code>

```python
def str_to_rgba(
    color: str,
    *,
    reference: str,
) -> RGB: ...
```
Experimental: Convert color strings(RGBA) to RGB codes

## 🟣`MAX`


<code style='color: skyblue;'>constant</code> <code style='color: green;'>public</code>

```python linenums="0"
MAX: tuple = (
    255, 255, 255,
)
```


## 🟣`RGB`


<code style='color: skyblue;'>constant</code> <code style='color: green;'>public</code>

```python linenums="0"
RGB: GenericAlias = tuple[int, int, int]
```


