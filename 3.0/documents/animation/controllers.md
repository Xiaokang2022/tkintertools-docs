# maliang.animation.controllers

<small>:octicons-mark-github-16: 源代码：[`maliang/animation/controllers.py`](https://github.com/Xiaokang2022/maliang/blob/3.0.0rc6/maliang/animation/controllers.py){ target='_blank' }</small>

Controller generator and standard control functions.

Definition of control function:

```python
def f(t: float) -> float: ...
```

* `t`: 0% ~ 100%, indicates the percentage of time
* return: real number, indicates a multiple of the cardinality of the animation


## 🔵`_map_t`


<code style='color: royalblue;'>function</code> <code style='color: orange;'>protected</code>

```python
def _map_t(
    start: float,
    end: float,
) -> collections.abc.Callable[[float], float]: ...
```
Map parameters in any range between 0 and 1.

* `start`: the first value of the parameter of the base function
* `end`: the last value of the parameter of the base function


## 🔵`_map_y`


<code style='color: royalblue;'>function</code> <code style='color: orange;'>protected</code>

```python
def _map_y(
    base: collections.abc.Callable[[float], float],
    end: float,
) -> collections.abc.Callable[[float], float]: ...
```
Map the final return value to 1.

* `base`: base function
* `end`: the last value of the parameter of the base function


## 🔵`ease_in`


<code style='color: royalblue;'>function</code> <code style='color: green;'>public</code>

```python
def ease_in(
    t: float,
) -> float: ...
```
Gradually accelerate. (slow -> fast)

* `t`: the percentage of time


## 🔵`ease_out`


<code style='color: royalblue;'>function</code> <code style='color: green;'>public</code>

```python
def ease_out(
    t: float,
) -> float: ...
```
Gradually decelerate. (fast -> slow)

* `t`: the percentage of time


## 🔵`generate`


<code style='color: royalblue;'>function</code> <code style='color: green;'>public</code>

```python
def generate(
    base: collections.abc.Callable[[float], float],
    start: float,
    end: float,
    *,
    map_y: bool = True,
) -> collections.abc.Callable[[float], float]: ...
```
Generate a control function from an ordinary mathematical function.

* `base`: base function, an ordinary mathematical function
* `start`: the first value of the parameter of the base function
* `end`: the last value of the parameter of the base function
* `map_y`: whether map the final return value to 1


## 🔵`linear`


<code style='color: royalblue;'>function</code> <code style='color: green;'>public</code>

```python
def linear(
    t: float,
) -> float: ...
```
Speed remains the same.

* `t`: the percentage of time


## 🔵`rebound`


<code style='color: royalblue;'>function</code> <code style='color: green;'>public</code>

```python
def rebound(
    t: float,
) -> float: ...
```
Before the end, displacement will bounce off a bit.

* `t`: the percentage of time


## 🔵`smooth`


<code style='color: royalblue;'>function</code> <code style='color: green;'>public</code>

```python
def smooth(
    t: float,
) -> float: ...
```
Speed is slow first, then fast and then slow. (slow -> fast -> slow)

* `t`: the percentage of time


