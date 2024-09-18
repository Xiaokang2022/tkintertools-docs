# tkintertools.standard.features

All standard `Feature` classes

## 🟢`ButtonFeature`



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


### 🟡`_click_left`


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _click_left(
    self,
    _: Event,
) -> bool: ...
```


### 🟡`_move_center`


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _move_center(
    self,
    event: Event,
) -> bool: ...
```


### 🟡`_move_left`


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _move_left(
    self,
    event: Event,
) -> bool: ...
```


### 🟡`_move_none`


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _move_none(
    self,
    event: Event,
) -> bool: ...
```


### 🟡`_move_right`


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _move_right(
    self,
    event: Event,
) -> bool: ...
```


### 🟡`_release_left`


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _release_left(
    self,
    event: Event,
) -> bool: ...
```




## 🟢`CheckButtonFeature`



<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code> | `ButtonFeature`

### 🟡`_click_left`


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _click_left(
    self,
    _: Event,
) -> bool: ...
```


### 🟡`_release_left`


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _release_left(
    self,
    event: Event,
) -> bool: ...
```




## 🟢`Highlight`



<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code> | `ButtonFeature`

### 🟡`_click_left`


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _click_left(
    self,
    _: Event,
) -> bool: ...
```


### 🟡`_move_none`


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _move_none(
    self,
    event: Event,
) -> bool: ...
```


### 🟡`_release_left`


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _release_left(
    self,
    event: Event,
) -> bool: ...
```




## 🟢`InputBoxFeature`



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


### 🟡`_click_left`


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _click_left(
    self,
    event: Event,
) -> bool: ...
```


### 🟡`_copy`


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _copy(
    self,
    event: Event,
) -> bool: ...
```


### 🟡`_cut`


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _cut(
    self,
    event: Event,
) -> bool: ...
```


### 🟡`_input`


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _input(
    self,
    event: Event,
) -> bool: ...
```


### 🟡`_move_left`


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _move_left(
    self,
    event: Event,
) -> bool: ...
```


### 🟡`_move_none`


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _move_none(
    self,
    event: Event,
) -> bool: ...
```


### 🟡`_paste`


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _paste(
    self,
    event: Event,
) -> bool: ...
```


### 🟡`_release_left`


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _release_left(
    self,
    event: Event,
) -> bool: ...
```


### 🟡`_select_all`


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _select_all(
    self,
    event: Event,
) -> bool: ...
```




## 🟢`LabelFeature`



<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code> | `Feature`

### 🟡`_move_none`


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _move_none(
    self,
    event: Event,
) -> bool: ...
```




## 🟢`OptionButtonFeature`



<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code> | `Feature`

### 🟡`_click_left`


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _click_left(
    self,
    event: Event,
) -> bool: ...
```




## 🟢`ProgressBarFeature`



<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code> | `LabelFeature`



## 🟢`RadioButtonFeature`



<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code> | `CheckButtonFeature`



## 🟢`SliderFeature`



<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code> | `Feature`


```python
def __init__(
    self,
    widget: Widget,
) -> None: ...
```
Feature of Slider


### 🟡`_click_left`


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _click_left(
    self,
    event: Event,
) -> bool: ...
```


### 🟡`_move_left`


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _move_left(
    self,
    event: Event,
) -> bool: ...
```


### 🟡`_move_none`


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _move_none(
    self,
    event: Event,
) -> bool: ...
```


### 🟡`_release_left`


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _release_left(
    self,
    event: Event,
) -> bool: ...
```




## 🟢`SpinBoxFeature`



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


### 🟡`_wheel`


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _wheel(
    self,
    event: Event,
) -> bool: ...
```




## 🟢`SwitchFeature`



<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code> | `ButtonFeature`

### 🟡`_click_left`


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _click_left(
    self,
    _: Event,
) -> bool: ...
```


### 🟡`_move_none`


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _move_none(
    self,
    event: Event,
) -> bool: ...
```


### 🟡`_release_left`


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _release_left(
    self,
    event: Event,
) -> bool: ...
```




## 🟢`ToggleButtonFeature`



<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code> | `ButtonFeature`

### 🟡`_click_left`


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _click_left(
    self,
    _: Event,
) -> bool: ...
```


### 🟡`_move_none`


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _move_none(
    self,
    event: Event,
) -> bool: ...
```


### 🟡`_release_left`


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _release_left(
    self,
    event: Event,
) -> bool: ...
```




## 🟢`Underline`



<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code> | `ButtonFeature`

### 🟡`_click_left`


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _click_left(
    self,
    _: Event,
) -> bool: ...
```


### 🟡`_move_none`


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _move_none(
    self,
    event: Event,
) -> bool: ...
```


### 🟡`_release_left`


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _release_left(
    self,
    event: Event,
) -> bool: ...
```




