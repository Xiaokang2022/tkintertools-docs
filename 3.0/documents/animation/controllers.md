# tkintertools.animation.controllers


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


## 🔵 函数

### <big>`_map_t`</big>


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


### <big>`_map_y`</big>


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


### <big>`controller_generator`</big>


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


### <big>`flat`</big>


<code style='color: royalblue;'>function</code> <code style='color: green;'>public</code>

```python
def flat(
    t: float,
) -> float: ...
```
Flat animation: speed remains the same

### <big>`rebound`</big>


<code style='color: royalblue;'>function</code> <code style='color: green;'>public</code>

```python
def rebound(
    t: float,
) -> float: ...
```
Rebound animation: before the end, displacement will bounce off a bit

### <big>`smooth`</big>


<code style='color: royalblue;'>function</code> <code style='color: green;'>public</code>

```python
def smooth(
    t: float,
) -> float: ...
```
Smooth animation: speed is slow first, then fast and then slow

