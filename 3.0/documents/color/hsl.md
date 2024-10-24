# tkintertools.color.hsl

Support for HSL

## 🔵`blend`


<code style='color: royalblue;'>function</code> <code style='color: green;'>public</code>

```python
def blend(
    colors: list[tuple[float, float, float]],
    *,
    weights: list[tuple] | None = None,
) -> tuple[float, float, float]: ...
```
Mix colors by weight

* `colors`: color list
* `weights`: weight list


## 🔵`contrast`


<code style='color: royalblue;'>function</code> <code style='color: green;'>public</code>

```python
def contrast(
    hsl: tuple[float, float, float],
    *,
    channels: tuple[bool, bool, bool] = (True, True, True),
) -> tuple[float, float, float]: ...
```
Get a contrasting color of a color

* `hsl`: a tuple, HSL codes
* `channels`: three color channels


## 🔵`convert`


<code style='color: royalblue;'>function</code> <code style='color: green;'>public</code>

```python
def convert(
    first: tuple[float, float, float],
    second: tuple[float, float, float],
    rate: float,
    *,
    channels: tuple[bool, bool, bool] = (True, True, True),
) -> tuple[float, float, float]: ...
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
    first: tuple[float, float, float],
    second: tuple[float, float, float],
    count: int,
    rate: float = 1,
    *,
    channels: tuple[bool, bool, bool] = (True, True, True),
    contoller: typing.Callable[[float], float] = flat,
) -> list[tuple[float, float, float]]: ...
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
    color: tuple[float, float, float],
) -> tuple[int, int, int]: ...
```
Convert HSL to RGB codes

## 🔵`hsl_to_rgb`


<code style='color: royalblue;'>function</code> <code style='color: green;'>public</code>

```python
def hsl_to_rgb(
    color: tuple[float, float, float],
) -> tuple[int, int, int]: ...
```
Convert HSL to RGB codes

## 🔵`rgb_to_hsl`


<code style='color: royalblue;'>function</code> <code style='color: green;'>public</code>

```python
def rgb_to_hsl(
    color: tuple[int, int, int],
) -> tuple[float, float, float]: ...
```
Convert RGB to HSL codes

## 🔵`rgb_to_hsl`


<code style='color: royalblue;'>function</code> <code style='color: green;'>public</code>

```python
def rgb_to_hsl(
    color: tuple[int, int, int],
) -> tuple[float, float, float]: ...
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


