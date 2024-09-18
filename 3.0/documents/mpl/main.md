# tkintertools.mpl.main

APIs for Matplotlib

## 🟢 类

### <big>`FigureCanvas`</big>



<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code> | `Canvas` `FigureCanvasTkAgg`


```python
def __init__(
    self,
    figure: Figure,
    master: Misc,
    *args,
    **kwargs,
) -> None: ...
```
A canvas for interface of `matplotlib`

* `figure`: a `Figure` object from `matplotlib`
* `master`: parent widget


#### <big>`_fix_size`</big>


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _fix_size(
    self,
    event: Event,
) -> None: ...
```
Correct the size of Figure

#### <big>`_theme`</big>


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _theme(
    self,
    dark: bool,
) -> None: ...
```
Change the color theme of the Figure

#### <big>`destroy`</big>


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def destroy(
    self,
) -> None: ...
```




### <big>`FigureToolbar`</big>



<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code> | `NavigationToolbar2Tk`


```python
def __init__(
    self,
    canvas: FigureCanvas,
    master: tkinter.Misc | tkintertools.mpl.main.FigureCanvas | None = None,
    *,
    pack_toolbar: bool = True,
    **kwargs,
) -> None: ...
```
An interface class for the matplotlib navigation cursor

* `canvas`: the figure canvas on which to operate
* `master`: parent widget
* `pack_toolbar`: if True, add the toolbar to the parent's pack
manager's packing list during initialization with `side="bottom"` and
`fill="x"`.

TIPS:

If you want to use the toolbar with a different layout manager,
use `pack_toolbar=False`


#### <big>`_theme`</big>


<code style='color: #BBBB00;'>method</code> <code style='color: orange;'>protected</code>

```python
def _theme(
    self,
    dark: bool,
) -> None: ...
```
Change the color theme of the Toolbar

#### <big>`destroy`</big>


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def destroy(
    self,
) -> None: ...
```




## 🔵 函数

### <big>`_forward_methods`</big>


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


### <big>`set_mpl_default_theme`</big>


<code style='color: royalblue;'>function</code> <code style='color: green;'>public</code>

```python
def set_mpl_default_theme(
    theme: typing.Literal['light', 'dark'],
) -> None: ...
```

Set default color constants of `matplotlib`

* `theme`: theme mode


## 🟡 变量

### <big>`DARK_THEME`</big>


<code style='color: skyblue;'>constant</code> <code style='color: green;'>public</code>

```python linenums="0"
DARK_THEME: dict = {
    'axes.edgecolor': '#AAAAAA',
    'axes.facecolor': '#202020',
    'axes.labelcolor': '#CCCCCC',
    'axes.titlecolor': '#CCCCCC',
    'axes3d.xaxis.panecolor': '#2A2A2A',
    'axes3d.yaxis.panecolor': '#2A2A2A',
    'axes3d.zaxis.panecolor': '#2A2A2A',
    'figure.facecolor': '#202020',
    'grid.color': '#505050',
    'legend.edgecolor': '#707070',
    'legend.facecolor': '#202020',
    'legend.labelcolor': '#CCCCCC',
    'text.color': '#CCCCCC',
    'xtick.color': '#CCCCCC',
    'xtick.labelcolor': '#CCCCCC',
    'ytick.color': '#CCCCCC',
    'ytick.labelcolor': '#CCCCCC',
}
```


### <big>`LIGHT_THEME`</big>


<code style='color: skyblue;'>constant</code> <code style='color: green;'>public</code>

```python linenums="0"
LIGHT_THEME: dict = {
    'axes.edgecolor': '#2A2A2A',
    'axes.facecolor': '#FFFFFF',
    'axes.labelcolor': '#000000',
    'axes.titlecolor': '#000000',
    'axes3d.xaxis.panecolor': '#F5F5F5',
    'axes3d.yaxis.panecolor': '#F5F5F5',
    'axes3d.zaxis.panecolor': '#F5F5F5',
    'figure.facecolor': '#FFFFFF',
    'grid.color': '#BDBDBD',
    'legend.edgecolor': '#D6D6D6',
    'legend.facecolor': '#FFFFFF',
    'legend.labelcolor': '#000000',
    'text.color': '#000000',
    'xtick.color': '#000000',
    'xtick.labelcolor': '#000000',
    'ytick.color': '#000000',
    'ytick.labelcolor': '#000000',
}
```


