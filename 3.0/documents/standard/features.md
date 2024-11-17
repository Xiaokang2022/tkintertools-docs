# tkintertools.standard.features

All standard `Feature` classes

## 🟢`ButtonFeature`



<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code> | `Feature`


```python
def __init__(
    self,
    widget: virtual.Widget,
    *,
    command: typing.Callable | None = None,
    args: tuple = (),
) -> None: ...
```
Feature of Button

* `widget`: parent widget
* `command`: callback function
* `args`: arguments of callback function


### 🟡`_b_1_motion`


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _b_1_motion(
    self,
    event: tkinter.Event,
) -> bool: ...
```


### 🟡`_b_2_motion`


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _b_2_motion(
    self,
    event: tkinter.Event,
) -> bool: ...
```


### 🟡`_b_3_motion`


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _b_3_motion(
    self,
    event: tkinter.Event,
) -> bool: ...
```


### 🟡`_button_1`


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _button_1(
    self,
    _: tkinter.Event,
) -> bool: ...
```


### 🟡`_button_release_1`


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _button_release_1(
    self,
    event: tkinter.Event,
) -> bool: ...
```


### 🟡`_motion`


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _motion(
    self,
    event: tkinter.Event,
) -> bool: ...
```




## 🟢`CheckButtonFeature`



<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code> | `ButtonFeature`

### 🟡`_button_1`


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _button_1(
    self,
    _: tkinter.Event,
) -> bool: ...
```


### 🟡`_button_release_1`


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _button_release_1(
    self,
    event: tkinter.Event,
) -> bool: ...
```




## 🟢`Highlight`



<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code> | `ButtonFeature`

### 🟡`_button_1`


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _button_1(
    self,
    _: tkinter.Event,
) -> bool: ...
```


### 🟡`_button_release_1`


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _button_release_1(
    self,
    event: tkinter.Event,
) -> bool: ...
```


### 🟡`_motion`


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _motion(
    self,
    event: tkinter.Event,
) -> bool: ...
```




## 🟢`InputBoxFeature`



<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code> | `ButtonFeature`


```python
def __init__(
    self,
    widget: virtual.Widget,
    *,
    command: typing.Callable[..., typing.Any] | None = None,
    args: tuple = (),
) -> None: ...
```
Feature of input box


### 🟡`_b_1_motion`


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _b_1_motion(
    self,
    event: tkinter.Event,
) -> bool: ...
```


### 🟡`_button_1`


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _button_1(
    self,
    event: tkinter.Event,
) -> bool: ...
```


### 🟡`_button_release_1`


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _button_release_1(
    self,
    _: tkinter.Event,
) -> bool: ...
```


### 🟡`_copy`


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _copy(
    self,
    _: tkinter.Event,
) -> bool: ...
```


### 🟡`_cut`


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _cut(
    self,
    event: tkinter.Event,
) -> bool: ...
```


### 🟡`_key_press`


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _key_press(
    self,
    event: tkinter.Event,
) -> bool: ...
```


### 🟡`_motion`


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _motion(
    self,
    event: tkinter.Event,
) -> bool: ...
```


### 🟡`_paste`


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _paste(
    self,
    _: tkinter.Event,
) -> bool: ...
```


### 🟡`_select_all`


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _select_all(
    self,
    _: tkinter.Event,
) -> bool: ...
```




## 🟢`LabelFeature`



<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code> | `Feature`

### 🟡`_motion`


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _motion(
    self,
    event: tkinter.Event,
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
    widget: virtual.Widget,
) -> None: ...
```
Feature of Slider


### 🟡`_b_1_motion`


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _b_1_motion(
    self,
    event: tkinter.Event,
) -> bool: ...
```


### 🟡`_button_1`


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _button_1(
    self,
    event: tkinter.Event,
) -> bool: ...
```


### 🟡`_button_release_1`


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _button_release_1(
    self,
    _: tkinter.Event,
) -> bool: ...
```


### 🟡`_motion`


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _motion(
    self,
    event: tkinter.Event,
) -> bool: ...
```




## 🟢`SpinBoxFeature`



<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code> | `Feature`


```python
def __init__(
    self,
    widget: virtual.Widget,
    *,
    command: typing.Callable[[bool], typing.Any] | None = None,
) -> None: ...
```
Feature of SpinBox

* `widget`: parent widget
* `command`: callback function


### 🟡`_mouse_wheel`


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _mouse_wheel(
    self,
    event: tkinter.Event,
) -> bool: ...
```




## 🟢`SwitchFeature`



<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code> | `ButtonFeature`

### 🟡`_button_1`


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _button_1(
    self,
    _: tkinter.Event,
) -> bool: ...
```


### 🟡`_button_release_1`


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _button_release_1(
    self,
    event: tkinter.Event,
) -> bool: ...
```


### 🟡`_motion`


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _motion(
    self,
    event: tkinter.Event,
) -> bool: ...
```




## 🟢`ToggleButtonFeature`



<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code> | `ButtonFeature`

### 🟡`_button_1`


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _button_1(
    self,
    _: tkinter.Event,
) -> bool: ...
```


### 🟡`_button_release_1`


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _button_release_1(
    self,
    event: tkinter.Event,
) -> bool: ...
```


### 🟡`_motion`


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _motion(
    self,
    event: tkinter.Event,
) -> bool: ...
```




## 🟢`Underline`



<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code> | `ButtonFeature`

### 🟡`_button_1`


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _button_1(
    self,
    _: tkinter.Event,
) -> bool: ...
```


### 🟡`_button_release_1`


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _button_release_1(
    self,
    event: tkinter.Event,
) -> bool: ...
```


### 🟡`_motion`


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _motion(
    self,
    event: tkinter.Event,
) -> bool: ...
```




