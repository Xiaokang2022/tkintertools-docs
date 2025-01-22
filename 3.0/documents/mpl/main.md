# maliang.mpl.main

<small>:octicons-mark-github-16: 源代码：[`maliang/mpl/main.py`](https://github.com/Xiaokang2022/maliang-mpl/blob/1.2.3/maliang/mpl/main.py){ target='_blank' }</small>

APIs for Matplotlib

## 🟢`FigureCanvas`



<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code> | `Canvas` `FigureCanvasTkAgg`


```python
def __init__(
    self,
    master: tkinter.Misc,
    figure: matplotlib.figure.Figure,
    *args,
    **kwargs,
) -> None: ...
```
A canvas for interface of `matplotlib`

* `master`: parent widget
* `figure`: a `Figure` object from `matplotlib`


### 🟡`_fix_size`


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _fix_size(
    self,
    event: tkinter.Event,
) -> None: ...
```
Correct the size of Figure.

### 🟡`destroy`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def destroy(
    self,
) -> None: ...
```


### 🟡`theme`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def theme(
    self,
    theme: typing.Literal['light', 'dark'],
) -> None: ...
```
Change the color theme of the Figure.

* `theme`: the theme name




## 🟢`FigureToolbar`



<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code> | `NavigationToolbar2Tk`


```python
def __init__(
    self,
    master: tkinter.Misc | FigureCanvas,
    figure_canvas: FigureCanvas | None = None,
    *,
    pack_toolbar: bool = True,
    **kwargs,
) -> None: ...
```
An interface class for the matplotlib navigation cursor

* `master`: parent widget
* `figure_canvas`: the figure canvas on which to operate
* `pack_toolbar`: if True, add the toolbar to the parent's pack
manager's packing list during initialization with `side="bottom"` and
`fill="x"`.

If you want to use the toolbar with a different layout manager,
use `pack_toolbar=False`


### 🟡`destroy`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def destroy(
    self,
) -> None: ...
```


### 🟡`theme`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def theme(
    self,
    theme: typing.Literal['light', 'dark'],
) -> None: ...
```
Change the color theme of the Toolbar.

* `theme`: the theme name




## 🔵`_forward_methods`


<code style='color: royalblue;'>function</code> <code style='color: orange;'>protected</code>

```python
def _forward_methods(
    src_obj: object | type,
    tgt_obj: object,
) -> None: ...
```
Forward methods and attributes of one object to another object.

* `src_obj`: the source object, that is, the forwarded object
* `tgt_obj`: the target object, that is, the object to be forwarded


## 🔵`set_mpl_default_theme`


<code style='color: royalblue;'>function</code> <code style='color: green;'>public</code>

```python
def set_mpl_default_theme(
    theme: typing.Literal['light', 'dark'],
    *,
    apply_font: bool = False,
) -> None: ...
```
Set default color constants of `matplotlib`.

* `theme`: theme mode
* `apply_font`: whether to use the font of `maliang`


