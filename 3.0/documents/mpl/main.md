# tkintertools.mpl.main

APIs for Matplotlib

## 🟢`FigureCanvas`



<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code> | `Canvas` `FigureCanvasTkAgg`


```python
def __init__(
    self,
    master: Misc,
    figure: Figure,
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
    event: Event,
) -> None: ...
```
Correct the size of Figure

### 🟡`_theme`


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _theme(
    self,
    dark: bool,
) -> None: ...
```
Change the color theme of the Figure

### 🟡`destroy`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def destroy(
    self,
) -> None: ...
```




## 🟢`FigureToolbar`



<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code> | `NavigationToolbar2Tk`


```python
def __init__(
    self,
    master: tkinter.Misc | tkintertools.mpl.main.FigureCanvas,
    figure_canvas: tkintertools.mpl.main.FigureCanvas | None = None,
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

TIPS:

If you want to use the toolbar with a different layout manager,
use `pack_toolbar=False`


### 🟡`_theme`


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _theme(
    self,
    dark: bool,
) -> None: ...
```
Change the color theme of the Toolbar

### 🟡`destroy`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def destroy(
    self,
) -> None: ...
```




## 🔵`_forward_methods`


<code style='color: royalblue;'>function</code> <code style='color: orange;'>protected</code>

```python
def _forward_methods(
    source_object: object | type,
    target_object: object,
) -> None: ...
```

Forward methods and attributes of one object to another object

* `source_object`: the source object, that is, the forwarded object
* `target_object`: the target object, that is, the object to be forwarded


## 🔵`set_mpl_default_theme`


<code style='color: royalblue;'>function</code> <code style='color: green;'>public</code>

```python
def set_mpl_default_theme(
    theme: typing.Literal['light', 'dark'],
) -> None: ...
```

Set default color constants of `matplotlib`

* `theme`: theme mode


