# tkintertools.style.manager

<small>:octicons-mark-github-16: 源代码：[`tkintertools/style/manager.py`](https://github.com/Xiaokang2022/tkintertools/blob/3.0.0rc4/tkintertools/style/manager.py){ target='_blank' }</small>

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
Valid only if the theme mode is set to Follow System

* `theme`: theme name


## 🔵`_process_event`


<code style='color: royalblue;'>function</code> <code style='color: orange;'>protected</code>

```python
def _process_event(
    dark_mode: bool,
) -> None: ...
```
Handle registered callback functions

* `dark_mode`: Wether it is dark mode


## 🔵`customize_window`


<code style='color: royalblue;'>function</code> <code style='color: green;'>public</code>

```python
def customize_window(
    window: tkinter.Tk,
    *,
    style: typing.Literal['mica', 'acrylic', 'aero', 'transparent', 'optimised', 'win7', 'inverse', 'native', 'popup', 'dark', 'normal'] | None = None,
    border_color: str | None = None,
    header_color: str | None = None,
    title_color: str | None = None,
    enable_file_dnd: typing.Callable[[str], typing.Any] | None = None,
    hide_title_bar: bool | None = None,
    hide_button: typing.Literal['all', 'maxmin', 'none'] | None = None,
    disable_minimize_button: bool | None = None,
    disable_maximize_button: bool | None = None,
    boarder_type: typing.Literal['rectangular', 'smallround', 'round'] | None = None,
) -> None: ...
```
Customize the relevant properties of the window

* `window`: the window which being customized
* `style`: different styles for windows
* `border_color`: border color of the window
* `header_color`: header color of the window
* `title_color`: title color of the window
* `enable_file_dnd`: apply file drag and drop in window
* `hide_title_bar`: Wether hide the whole title bar
* `hide_button`: Wether hide part of buttons on title bar
* `disable_minimize_button`: Wether disable minimize button
* `disable_maximize_button`: Wether disable maximize button
* `boarder_type`: boarder type of the window

WARNING:

This function is only works on Windows OS!
And some parameters are useless on Windows 7/10!


## 🔵`get_color_mode`


<code style='color: royalblue;'>function</code> <code style='color: green;'>public</code>

```python
def get_color_mode(
) -> typing.Literal['dark', 'light']: ...
```
Get the color mode of the program

## 🔵`register_event`


<code style='color: royalblue;'>function</code> <code style='color: green;'>public</code>

```python
def register_event(
    func: typing.Callable[[bool, typing.Any], typing.Any],
    *args: typing.Any,
) -> None: ...
```
When the system accent color changes, the registered function will be
called, and the parameter is a boolean value indicating whether it is
currently a dark theme

* `func`: callback function
* `args`: extra arguments


## 🔵`remove_event`


<code style='color: royalblue;'>function</code> <code style='color: green;'>public</code>

```python
def remove_event(
    func: typing.Callable[[bool, typing.Any], typing.Any],
) -> None: ...
```
Remove a registered function

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


## 🔵`set_theme_map`


<code style='color: royalblue;'>function</code> <code style='color: green;'>public</code>

```python
def set_theme_map(
    *,
    light_theme: str | types.ModuleType | None = None,
    dark_theme: str | types.ModuleType | None = None,
) -> None: ...
```
Set the path to the theme file used by the current program

* `light_theme`: the name of the theme of the light theme
* `dark_theme`: the name of the theme of the dark theme


## 🟣`_callback_events`


<code style='color: #BBBB00;'>variable</code> <code style='color: orange;'>protected</code>

```python linenums="0"
_callback_events: dict = {}
```


