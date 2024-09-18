# tkintertools.standard.features

All standard `Feature` classes

## 🟢 类

### <big>`ButtonFeature`</big>



<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code> | `Feature`


```python
def __init__(
    self,
    widget: Widget,
    *,
    command: typing.Optional[typing.Callable] = None,
    args: tuple = (),
) -> None: ...
```
Feature of Button

* `widget`: parent widget
* `command`: callback function
* `args`: arguments of callback function


#### <big>`_click_left`</big>


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _click_left(
    self,
    _: Event,
) -> bool: ...
```


#### <big>`_move_center`</big>


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _move_center(
    self,
    event: Event,
) -> bool: ...
```


#### <big>`_move_left`</big>


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _move_left(
    self,
    event: Event,
) -> bool: ...
```


#### <big>`_move_none`</big>


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _move_none(
    self,
    event: Event,
) -> bool: ...
```


#### <big>`_move_right`</big>


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _move_right(
    self,
    event: Event,
) -> bool: ...
```


#### <big>`_release_left`</big>


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _release_left(
    self,
    event: Event,
) -> bool: ...
```




### <big>`CheckButtonFeature`</big>



<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code> | `ButtonFeature`

#### <big>`_click_left`</big>


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _click_left(
    self,
    _: Event,
) -> bool: ...
```


#### <big>`_release_left`</big>


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _release_left(
    self,
    event: Event,
) -> bool: ...
```




### <big>`Highlight`</big>



<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code> | `ButtonFeature`

#### <big>`_click_left`</big>


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _click_left(
    self,
    _: Event,
) -> bool: ...
```


#### <big>`_move_none`</big>


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _move_none(
    self,
    event: Event,
) -> bool: ...
```


#### <big>`_release_left`</big>


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _release_left(
    self,
    event: Event,
) -> bool: ...
```




### <big>`InputBoxFeature`</big>



<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code> | `ButtonFeature`


```python
def __init__(
    self,
    widget: Widget,
    *,
    command: typing.Optional[typing.Callable[..., typing.Any]] = None,
    args: tuple = (),
) -> None: ...
```
Feature of input box


#### <big>`_click_left`</big>


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _click_left(
    self,
    event: Event,
) -> bool: ...
```


#### <big>`_copy`</big>


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _copy(
    self,
    event: Event,
) -> bool: ...
```


#### <big>`_cut`</big>


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _cut(
    self,
    event: Event,
) -> bool: ...
```


#### <big>`_input`</big>


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _input(
    self,
    event: Event,
) -> bool: ...
```


#### <big>`_move_left`</big>


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _move_left(
    self,
    event: Event,
) -> bool: ...
```


#### <big>`_move_none`</big>


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _move_none(
    self,
    event: Event,
) -> bool: ...
```


#### <big>`_paste`</big>


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _paste(
    self,
    event: Event,
) -> bool: ...
```


#### <big>`_release_left`</big>


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _release_left(
    self,
    event: Event,
) -> bool: ...
```


#### <big>`_select_all`</big>


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _select_all(
    self,
    event: Event,
) -> bool: ...
```




### <big>`LabelFeature`</big>



<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code> | `Feature`

#### <big>`_move_none`</big>


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _move_none(
    self,
    event: Event,
) -> bool: ...
```




### <big>`OptionButtonFeature`</big>



<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code> | `Feature`

#### <big>`_click_left`</big>


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _click_left(
    self,
    event: Event,
) -> bool: ...
```




### <big>`ProgressBarFeature`</big>



<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code> | `LabelFeature`



### <big>`RadioButtonFeature`</big>



<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code> | `CheckButtonFeature`



### <big>`SliderFeature`</big>



<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code> | `Feature`


```python
def __init__(
    self,
    widget: Widget,
) -> None: ...
```
Feature of Slider


#### <big>`_click_left`</big>


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _click_left(
    self,
    event: Event,
) -> bool: ...
```


#### <big>`_move_left`</big>


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _move_left(
    self,
    event: Event,
) -> bool: ...
```


#### <big>`_move_none`</big>


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _move_none(
    self,
    event: Event,
) -> bool: ...
```


#### <big>`_release_left`</big>


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _release_left(
    self,
    event: Event,
) -> bool: ...
```




### <big>`SpinBoxFeature`</big>



<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code> | `Feature`


```python
def __init__(
    self,
    widget: Widget,
    *,
    command: typing.Optional[typing.Callable[[bool], typing.Any]] = None,
) -> None: ...
```
Feature of SpinBox

* `widget`: parent widget
* `command`: callback function


#### <big>`_wheel`</big>


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _wheel(
    self,
    event: Event,
) -> bool: ...
```




### <big>`SwitchFeature`</big>



<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code> | `ButtonFeature`

#### <big>`_click_left`</big>


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _click_left(
    self,
    _: Event,
) -> bool: ...
```


#### <big>`_move_none`</big>


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _move_none(
    self,
    event: Event,
) -> bool: ...
```


#### <big>`_release_left`</big>


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _release_left(
    self,
    event: Event,
) -> bool: ...
```




### <big>`ToggleButtonFeature`</big>



<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code> | `ButtonFeature`

#### <big>`_click_left`</big>


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _click_left(
    self,
    _: Event,
) -> bool: ...
```


#### <big>`_move_none`</big>


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _move_none(
    self,
    event: Event,
) -> bool: ...
```


#### <big>`_release_left`</big>


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _release_left(
    self,
    event: Event,
) -> bool: ...
```




### <big>`Underline`</big>



<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code> | `ButtonFeature`

#### <big>`_click_left`</big>


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _click_left(
    self,
    _: Event,
) -> bool: ...
```


#### <big>`_move_none`</big>


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _move_none(
    self,
    event: Event,
) -> bool: ...
```


#### <big>`_release_left`</big>


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _release_left(
    self,
    event: Event,
) -> bool: ...
```




