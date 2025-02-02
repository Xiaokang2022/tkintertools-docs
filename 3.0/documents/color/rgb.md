# maliang.color.rgb

<small>:octicons-mark-github-16: 源代码：[`maliang/color/rgb.py`](https://github.com/Xiaokang2022/maliang/blob/3.0.0/maliang/color/rgb.py){ target='_blank' }</small>

Some functions about RGB codes.

## 🔵`blend`


<code style='color: royalblue;'>function</code> <code style='color: green;'>public</code>

```python
def blend(
    *values: tuple[int, int, int],
    weights: list[float] | None = None,
) -> tuple[int, int, int]: ...
```
Mix colors by weight.

* `values`: RGB codes
* `weights`: weight list, default value indicates the same weights


## 🔵`contrast`


<code style='color: royalblue;'>function</code> <code style='color: green;'>public</code>

```python
def contrast(
    value: tuple[int, int, int],
    /,
    *,
    channels: tuple[bool, bool, bool] = (True, True, True),
) -> tuple[int, int, int]: ...
```
Get the contrasting color of a RGB code.

* `value`: a RGB code
* `channels`: three color channels


## 🔵`gradient`


<code style='color: royalblue;'>function</code> <code style='color: green;'>public</code>

```python
def gradient(
    first: tuple[int, int, int],
    second: tuple[int, int, int],
    count: int,
    rate: float = 1,
    *,
    channels: tuple[bool, bool, bool] = (True, True, True),
    contoller: collections.abc.Callable[[float], float] = linear,
) -> list[tuple[int, int, int]]: ...
```
Get a list of color gradients from one color to another proportionally.

* `first`: the first RGB code
* `second`: the second RGB code
* `count`: the number of gradients
* `rate`: transition rate
* `channels`: three color channels
* `controller`: control function


## 🔵`transition`


<code style='color: royalblue;'>function</code> <code style='color: green;'>public</code>

```python
def transition(
    first: tuple[int, int, int],
    second: tuple[int, int, int],
    rate: float,
    *,
    channels: tuple[bool, bool, bool] = (True, True, True),
) -> tuple[int, int, int]: ...
```
Transition one color to another proportionally.

* `first`: the first RGB code
* `second`: the second RGB code
* `rate`: transition rate
* `channels`: three color channels


