# tkintertools.animation.controllers

<small>:octicons-mark-github-16: 源代码：[`tkintertools/animation/controllers.py`](https://github.com/Xiaokang2022/tkintertools/blob/3.0.0rc4/tkintertools/animation/controllers.py){ target='_blank' }</small>

Standard control functions

Definition of control function:

```python
def f(t: float) -> float: ...
```

* t: 0% ~ 100%, indicates the percentage of time
* return value: Any real number, represents a multiple of the cardinality of
the animation

The built-in control functions are:

* `flat`: speed remains the same
* `smooth`: speed is slow first, then fast and then slow
* `rebound`: before the end, displacement will bounce off a bit


## 🔵`_map_t`


<code style='color: royalblue;'>function</code> <code style='color: orange;'>protected</code>

```python
def _map_t(
    start: float,
    end: float,
) -> typing.Callable[[float], float]: ...
```
Map parameters in any range between 0 and 1

* `start`: the first value of the parameter of control function
* `end`: the last value of the parameter of control function


## 🔵`_map_y`


<code style='color: royalblue;'>function</code> <code style='color: orange;'>protected</code>

```python
def _map_y(
    base_function: typing.Callable[[float], float],
    end: float,
) -> typing.Callable[[float], float]: ...
```
Map the final return value to 1

* `base_function`: base function
* `end`: the last value of the parameter of control function


## 🔵`controller_generator`


<code style='color: royalblue;'>function</code> <code style='color: green;'>public</code>

```python
def controller_generator(
    base_function: typing.Callable[[float], float],
    start: float,
    end: float,
    *,
    map_y: bool = True,
) -> typing.Callable[[float], float]: ...
```
Generator of control functions

Modify the generic function to a control function suitable for animation

* `base_function`: base function
* `start`: the first value of the parameter of control function
* `end`: the last value of the parameter of control function
* `map_y`: whether map the final return value to 1

For example:

* Before modifying: $y = 2\sint, 0 <= t <= \pi/2$
* After modifying: $y = \sin\frac{\pi}{2}t, 0 <= t <= 1$


## 🔵`flat`


<code style='color: royalblue;'>function</code> <code style='color: green;'>public</code>

```python
def flat(
    t: float,
) -> float: ...
```
Flat animation: speed remains the same

## 🔵`rebound`


<code style='color: royalblue;'>function</code> <code style='color: green;'>public</code>

```python
def rebound(
    t: float,
) -> float: ...
```
Rebound animation: before the end, displacement will bounce off a bit

## 🔵`smooth`


<code style='color: royalblue;'>function</code> <code style='color: green;'>public</code>

```python
def smooth(
    t: float,
) -> float: ...
```
Smooth animation: speed is slow first, then fast and then slow

