# maliang.theme.manager

<small>:octicons-mark-github-16: 源代码：[`maliang/theme/manager.py`](https://github.com/Xiaokang2022/maliang/blob/3.0.0/maliang/theme/manager.py){ target='_blank' }</small>

Support for theme

* darkdetect: https://github.com/albertosottile/darkdetect
* pywinstyles: https://github.com/Akascape/py-window-styles
* win32material: https://github.com/littlewhitecloud/win32material
* hPyT: https://github.com/Zingzy/hPyT


## 🔵`_callback`


<code style='color: royalblue;'>function</code> <code style='color: orange;'>protected</code>

```python
def _callback(
    theme: str,
) -> None: ...
```
Callback function that is triggered when a system theme is switched.
Valid only if the theme mode is set to follow system.

* `theme`: theme name


## 🔵`_process_event`


<code style='color: royalblue;'>function</code> <code style='color: orange;'>protected</code>

```python
def _process_event(
    theme: typing.Literal['light', 'dark'],
) -> None: ...
```
Handle registered callback functions.

* `theme`: theme name


## 🔵`apply_file_dnd`


<code style='color: royalblue;'>function</code> <code style='color: green;'>public</code>

```python
def apply_file_dnd(
    window: tkinter.Tk,
    *,
    command: collections.abc.Callable[[str], typing.Any],
) -> None: ...
```
Apply file drag and drop in a widget.

* `window`: the window which being customized
* `command`: callback function, accept a parameter that represents the path
of the file

This function is only works on Windows OS!


## 🔵`apply_theme`


<code style='color: royalblue;'>function</code> <code style='color: green;'>public</code>

```python
def apply_theme(
    window: tkinter.Tk,
    *,
    theme: typing.Literal['mica', 'acrylic', 'acrylic2', 'aero', 'transparent', 'optimised', 'win7', 'inverse', 'native', 'popup', 'dark', 'normal'],
) -> None: ...
```
Apply some Windows themes to the window.

* `window`: the window which being customized
* `theme`: different themes for windows

This function is only works on Windows OS! And some parameters are useless
on Windows 7/10!


## 🔵`customize_window`


<code style='color: royalblue;'>function</code> <code style='color: green;'>public</code>

```python
def customize_window(
    window: tkinter.Tk,
    *,
    border_color: str | None = None,
    header_color: str | None = None,
    title_color: str | None = None,
    hide_title_bar: bool | None = None,
    hide_button: typing.Literal['all', 'maxmin', 'none'] | None = None,
    disable_minimize_button: bool | None = None,
    disable_maximize_button: bool | None = None,
    border_type: typing.Literal['rectangular', 'smallround', 'round'] | None = None,
) -> None: ...
```
Customize the relevant properties of the window

* `window`: the window which being customized
* `border_color`: border color of the window
* `header_color`: header color of the window
* `title_color`: title color of the window
* `hide_title_bar`: Wether hide the whole title bar
* `hide_button`: Wether hide part of buttons on title bar
* `disable_minimize_button`: Wether disable minimize button
* `disable_maximize_button`: Wether disable maximize button
* `border_type`: border type of the window

This function is only works on Windows OS! And some parameters are useless
on Windows 7/10!


## 🔵`get_color_mode`


<code style='color: royalblue;'>function</code> <code style='color: green;'>public</code>

```python
def get_color_mode(
) -> typing.Literal['dark', 'light']: ...
```
Get the color mode of the program.

## 🔵`register_event`


<code style='color: royalblue;'>function</code> <code style='color: green;'>public</code>

```python
def register_event(
    func: collections.abc.Callable[..., typing.Any],
    *args: typing.Any,
) -> None: ...
```
When the system accent color changes, the registered function will be
called, and the parameter is a boolean value indicating whether it is
currently a dark theme.

* `func`: callback function
* `args`: extra arguments


## 🔵`remove_event`


<code style='color: royalblue;'>function</code> <code style='color: green;'>public</code>

```python
def remove_event(
    func: collections.abc.Callable[..., typing.Any],
) -> None: ...
```
Remove a registered function.

* `func`: callback function


## 🔵`set_color_mode`


<code style='color: royalblue;'>function</code> <code style='color: green;'>public</code>

```python
def set_color_mode(
    mode: typing.Literal['system', 'dark', 'light'] = 'system',
) -> None: ...
```
Set the color mode of the program

* `mode`: it can be `"light"`, `"dark"`, and `"system"`

TIP:

`"system"` is the following system


## 🟣`_`


<code style='color: #BBBB00;'>variable</code> <code style='color: orange;'>protected</code>

```python linenums="0"
_: str = '0'
```


## 🟣`_callback_events`


<code style='color: #BBBB00;'>variable</code> <code style='color: orange;'>protected</code>

```python linenums="0"
_callback_events: dict = {}
```


## 🟣`_color_mode`


<code style='color: #BBBB00;'>variable</code> <code style='color: orange;'>protected</code>

```python linenums="0"
_color_mode: str = 'system'
```


## 🟣`major`


<code style='color: #BBBB00;'>variable</code> <code style='color: green;'>public</code>

```python linenums="0"
major: str = '10'
```


## 🟣`micro`


<code style='color: #BBBB00;'>variable</code> <code style='color: green;'>public</code>

```python linenums="0"
micro: str = '26100'
```


