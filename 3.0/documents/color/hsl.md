# tkintertools.color.hsl

<small>:octicons-mark-github-16: 源代码：[`tkintertools/color/hsl.py`](https://github.com/Xiaokang2022/tkintertools/blob/3.0.0rc5/tkintertools/color/hsl.py){ target='_blank' }</small>

Support for HSL

## 🔵`blend`


<code style='color: royalblue;'>function</code> <code style='color: green;'>public</code>

```python
def blend(
    colors: list[HSL],
    *,
    weights: list[float] | None = None,
) -> HSL: ...
```
Mix colors by weight

* `colors`: color list
* `weights`: weight list


## 🔵`contrast`


<code style='color: royalblue;'>function</code> <code style='color: green;'>public</code>

```python
def contrast(
    hsl: HSL,
    *,
    channels: tuple[bool, bool, bool] = (True, True, True),
) -> HSL: ...
```
Get a contrasting color of a color

* `hsl`: a tuple, HSL codes
* `channels`: three color channels


## 🔵`convert`


<code style='color: royalblue;'>function</code> <code style='color: green;'>public</code>

```python
def convert(
    first: HSL,
    second: HSL,
    rate: float,
    *,
    channels: tuple[bool, bool, bool] = (True, True, True),
) -> HSL: ...
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
    first: HSL,
    second: HSL,
    count: int,
    rate: float = 1,
    *,
    channels: tuple[bool, bool, bool] = (True, True, True),
    contoller: collections.abc.Callable[[int | float], int | float] = flat,
) -> list[HSL]: ...
```
Get a list of color gradients from one color to another proportionally

* `first`: first color
* `second`: second color
* `count`: number of gradients
* `rate`: conversion rate
* `channels`: three color channels
* `controller`: control function


## 🔵`hsl_to_rgb`


<code style='color: royalblue;'>function</code> <code style='color: green;'>public</code>

```python
def hsl_to_rgb(
    color: HSL,
) -> rgb.RGB: ...
```
Convert HSL to RGB codes

## 🔵`hsl_to_rgb`


<code style='color: royalblue;'>function</code> <code style='color: green;'>public</code>

```python
def hsl_to_rgb(
    color: HSL,
) -> rgb.RGB: ...
```
Convert HSL to RGB codes

## 🔵`rgb_to_hsl`


<code style='color: royalblue;'>function</code> <code style='color: green;'>public</code>

```python
def rgb_to_hsl(
    color: rgb.RGB,
) -> HSL: ...
```
Convert RGB to HSL codes

## 🔵`rgb_to_hsl`


<code style='color: royalblue;'>function</code> <code style='color: green;'>public</code>

```python
def rgb_to_hsl(
    color: rgb.RGB,
) -> HSL: ...
```
Convert RGB to HSL codes

## 🟣`HSL`


<code style='color: skyblue;'>constant</code> <code style='color: green;'>public</code>

```python linenums="0"
HSL: GenericAlias = tuple[float, float, float]
```


## 🟣`MAX`


<code style='color: skyblue;'>constant</code> <code style='color: green;'>public</code>

```python linenums="0"
MAX: tuple = (
    6.283185307179586, 1, 1,
)
```


