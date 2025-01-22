# maliang.standard.styles

<small>:octicons-mark-github-16: 源代码：[`maliang/standard/styles.py`](https://github.com/Xiaokang2022/maliang/blob/3.0.0rc6/maliang/standard/styles.py){ target='_blank' }</small>

All standard `Style` classes

## 🟢`ButtonStyle`



<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code> | `LabelStyle`



## 🟢`CheckBoxStyle`



<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code> | `ToggleButtonStyle`



## 🟢`HighlightButtonStyle`



<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code> | `TextStyle`



## 🟢`IconButtonStyle`



<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code> | `LabelStyle`



## 🟢`InputBoxStyle`



<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code> | `Style`

### 🟡`set`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def set(
    self,
    theme: typing.Literal['light', 'dark'] | None = None,
    *,
    fg: tuple[str | types.EllipsisType, ...] | str | None = None,
    bg: tuple[str | types.EllipsisType, ...] | str | None = None,
    ol: tuple[str | types.EllipsisType, ...] | str | None = None,
    bg_bar: tuple[str | types.EllipsisType, ...] | str | None = None,
) -> None: ...
```
Set the style of the widget.

* `theme`: the theme name, None indicates both
* `fg`: the foreground color of the widget.
* `bg`: the background color of the widget.
* `ol`: the outline color of the widget.
* `bg_bar`: the highlight bar of the widget (Only for Windows11 theme)

states: "normal", "hover", "active"




## 🟢`LabelStyle`



<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code> | `Style`

### 🟡`set`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def set(
    self,
    theme: typing.Literal['light', 'dark'] | None = None,
    *,
    fg: tuple[str | types.EllipsisType, ...] | str | None = None,
    bg: tuple[str | types.EllipsisType, ...] | str | None = None,
    ol: tuple[str | types.EllipsisType, ...] | str | None = None,
) -> None: ...
```
Set the style of the widget.

* `theme`: the theme name, None indicates both
* `fg`: the foreground color of the widget.
* `bg`: the background color of the widget.
* `ol`: the outline color of the widget.

states: "normal", "hover", "active"




## 🟢`OptionButtonStyle`



<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code> | `Style`

### 🟡`set`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def set(
    self,
    theme: typing.Literal['light', 'dark'] | None = None,
    *,
    bg: tuple[str | types.EllipsisType, ...] | str | None = None,
    ol: tuple[str | types.EllipsisType, ...] | str | None = None,
) -> None: ...
```
Set the style of the widget.

* `theme`: the theme name, None indicates both
* `bg`: the background color of the widget.
* `ol`: the outline color of the widget.

states: "normal", "hover", "active"




## 🟢`ProgressBarStyle`



<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code> | `Style`

### 🟡`set`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def set(
    self,
    theme: typing.Literal['light', 'dark'] | None = None,
    *,
    bg_slot: tuple[str | types.EllipsisType, ...] | str | None = None,
    ol_slot: tuple[str | types.EllipsisType, ...] | str | None = None,
    bg_bar: tuple[str | types.EllipsisType, ...] | str | None = None,
    ol_bar: tuple[str | types.EllipsisType, ...] | str | None = None,
) -> None: ...
```
Set the style of the widget.

* `theme`: the theme name, None indicates both
* `bg_slot`: the background color of the widget.
* `ol_slot`: the outline color of the widget.
* `bg_bar`: the inside background color of the widget.
* `ol_bar`: the inside outline color of the widget.

states: "normal", "hover"




## 🟢`RadioBoxStyle`



<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code> | `Style`

### 🟡`set`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def set(
    self,
    theme: typing.Literal['light', 'dark'] | None = None,
    *,
    bg_box: tuple[str | types.EllipsisType, ...] | str | None = None,
    ol_box: tuple[str | types.EllipsisType, ...] | str | None = None,
    bg_dot: tuple[str | types.EllipsisType, ...] | str | None = None,
    ol_dot: tuple[str | types.EllipsisType, ...] | str | None = None,
) -> None: ...
```
Set the style of the widget.

* `theme`: the theme name, None indicates both
* `bg_box`: the background color of the widget.
* `ol_box`: the outline color of the widget.
* `bg_dot`: the inside background color of the widget.
* `ol_dot`: the inside outline color of the widget.

states: "normal", "hover", "active"




## 🟢`SegmentedButtonStyle`



<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code> | `Style`

### 🟡`set`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def set(
    self,
    theme: typing.Literal['light', 'dark'] | None = None,
    *,
    bg: tuple[str | types.EllipsisType, ...] | str | None = None,
    ol: tuple[str | types.EllipsisType, ...] | str | None = None,
) -> None: ...
```
Set the style of the widget.

* `theme`: the theme name, None indicates both
* `bg`: the background color of the widget.
* `ol`: the outline color of the widget.

states: "normal", "hover"




## 🟢`SliderStyle`



<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code> | `Style`

### 🟡`set`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def set(
    self,
    theme: typing.Literal['light', 'dark'] | None = None,
    *,
    fg_slot: tuple[str | types.EllipsisType, ...] | str | None = None,
    bg_slot: tuple[str | types.EllipsisType, ...] | str | None = None,
    bg_pnt: tuple[str | types.EllipsisType, ...] | str | None = None,
    bg_dot: tuple[str | types.EllipsisType, ...] | str | None = None,
) -> None: ...
```
Set the style of the widget.

* `theme`: the theme name, None indicates both
* `fg_slot`: the foreground color of the widget.
* `bg_slot`: the background color of the widget.
* `bg_pnt`: the pointer color of the widget.
* `bg_dot`: the pointer highlight part color of the widget (Only for
Windows11 theme).

states: "normal", "hover", "active"




## 🟢`SpinnerStyle`



<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code> | `Style`

### 🟡`set`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def set(
    self,
    theme: typing.Literal['light', 'dark'] | None = None,
    *,
    fg: tuple[str | types.EllipsisType, ...] | str | None = None,
    bg: tuple[str | types.EllipsisType, ...] | str | None = None,
) -> None: ...
```
Set the style of the widget.

* `theme`: the theme name, None indicates both
* `fg`: the foreground color of the widget.
* `bg`: the background color of the widget.

states: "normal"




## 🟢`SwitchStyle`



<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code> | `Style`

### 🟡`set`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def set(
    self,
    theme: typing.Literal['light', 'dark'] | None = None,
    *,
    bg_slot: tuple[str | types.EllipsisType, ...] | str | None = None,
    ol_slot: tuple[str | types.EllipsisType, ...] | str | None = None,
    bg_dot: tuple[str | types.EllipsisType, ...] | str | None = None,
    ol_dot: tuple[str | types.EllipsisType, ...] | str | None = None,
) -> None: ...
```
Set the style of the widget.

* `theme`: the theme name, None indicates both
* `bg_slot`: the background color of the widget.
* `ol_slot`: the outline color of the widget.
* `bg_dot`: the inside background color of the widget.
* `ol_dot`: the inside outline color of the widget.

states: "normal-off", "hover-off", "active-off", "normal-on",
"hover-on", "active-on"




## 🟢`TextStyle`



<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code> | `Style`

### 🟡`set`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def set(
    self,
    theme: typing.Literal['light', 'dark'] | None = None,
    *,
    fg: tuple[str | types.EllipsisType, ...] | str | None = None,
) -> None: ...
```
Set the style of the widget.

* `theme`: the theme name, None indicates both
* `fg`: the foreground color of the widget

states: "normal", "hover", "active"




## 🟢`ToggleButtonStyle`



<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code> | `Style`

### 🟡`set`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def set(
    self,
    theme: typing.Literal['light', 'dark'] | None = None,
    *,
    fg: tuple[str | types.EllipsisType, ...] | str | None = None,
    bg: tuple[str | types.EllipsisType, ...] | str | None = None,
    ol: tuple[str | types.EllipsisType, ...] | str | None = None,
) -> None: ...
```
Set the style of the widget.

* `theme`: the theme name, None indicates both
* `fg`: the foreground color of the widget.
* `bg`: the background color of the widget.
* `ol`: the outline color of the widget.

states: "normal-off", "hover-off", "active-off", "normal-on",
"hover-on", "active-on"




## 🟢`TooltipStyle`



<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code> | `Style`

### 🟡`set`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def set(
    self,
    theme: typing.Literal['light', 'dark'] | None = None,
    *,
    fg: tuple[str | types.EllipsisType, ...] | str | None = None,
    bg: tuple[str | types.EllipsisType, ...] | str | None = None,
    ol: tuple[str | types.EllipsisType, ...] | str | None = None,
) -> None: ...
```
Set the style of the widget.

* `theme`: the theme name, None indicates both
* `fg`: the foreground color of the widget.
* `bg`: the background color of the widget.
* `ol`: the outline color of the widget.

states: "normal"




## 🟢`UnderlineButtonStyle`



<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code> | `TextStyle`



