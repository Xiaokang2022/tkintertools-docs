# maliang.color.hsl

<small>:octicons-mark-github-16: 源代码：[`maliang/color/hsl.py`](https://github.com/Xiaokang2022/maliang/blob/3.0.0/maliang/color/hsl.py){ target='_blank' }</small>

Some functions about HSL codes.

## 🔵`blend`


<code style='color: royalblue;'>function</code> <code style='color: green;'>public</code>

```python
def blend(
    *values: tuple[float, float, float],
    weights: list[float] | None = None,
) -> tuple[float, float, float]: ...
```
Mix colors by weight.

* `values`: HSL codes
* `weights`: weight list, default value indicates the same weights


## 🔵`contrast`


<code style='color: royalblue;'>function</code> <code style='color: green;'>public</code>

```python
def contrast(
    value: tuple[float, float, float],
    /,
    *,
    channels: tuple[bool, bool, bool] = (True, True, True),
) -> tuple[float, float, float]: ...
```
Get the contrasting color of a HSL code.

* `value`: a HSL code
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
    contoller: collections.abc.Callable[[float], float] = linear,
) -> list[tuple[float, float, float]]: ...
```
Get a list of color gradients from one color to another proportionally.

* `first`: the first HSL code
* `second`: the second HSL code
* `count`: the number of gradients
* `rate`: transition rate
* `channels`: three color channels
* `controller`: control function


## 🔵`transition`


<code style='color: royalblue;'>function</code> <code style='color: green;'>public</code>

```python
def transition(
    first: tuple[float, float, float],
    second: tuple[float, float, float],
    rate: float,
    *,
    channels: tuple[bool, bool, bool] = (True, True, True),
) -> tuple[float, float, float]: ...
```
Transition one color to another proportionally.

* `first`: the first HSL code
* `second`: the second HSL code
* `rate`: transition rate
* `channels`: three color channels


