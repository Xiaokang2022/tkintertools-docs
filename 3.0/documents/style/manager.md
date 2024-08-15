# tkintertools.style.manager


Support for theme

ATTENTION:

All third packages which relative to style introduced by `tkintertools` are there:

* darkdetect
* pywinstyles
* win32material
* hPyT


## 🔵 Functions / 函数

### \_callback

<code style='color: royalblue;'>function</code> <code style='color: orange;'>protected</code>

```python
def _callback(
    theme: str,
) -> None: ...
```

callback function that is triggered when a system theme is switched.
Valid only if the theme mode is set to Follow System

* `theme`: theme name


### \_process\_event

<code style='color: royalblue;'>function</code> <code style='color: orange;'>protected</code>

```python
def _process_event(
    dark: bool,
) -> None: ...
```

Handle registered callback functions

* `dark`: Wether it is dark mode


### customize\_window

<code style='color: royalblue;'>function</code> <code style='color: green;'>public</code>

```python
def customize_window(
    window: Tk,
    *,
    style: typing.Optional[typing.Literal['mica', 'acrylic', 'aero', 'transparent', 'optimised', 'win7', 'inverse', 'native', 'popup', 'dark', 'normal']] = None,
    border_color: str | None = None,
    header_color: str | None = None,
    title_color: str | None = None,
    enable_file_dnd: typing.Optional[typing.Callable[[str], typing.Any]] = None,
    hide_title_bar: bool | None = None,
    hide_button: typing.Optional[typing.Literal['all', 'maxmin', 'none']] = None,
    disable_minimize_button: bool | None = None,
    disable_maximize_button: bool | None = None,
    boarder_type: typing.Optional[typing.Literal['rectangular', 'smallround', 'round']] = None,
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


### get\_color\_mode

<code style='color: royalblue;'>function</code> <code style='color: green;'>public</code>

```python
def get_color_mode(
) -> typing.Literal['dark', 'light']: ...
```
Get the color mode of the program

### get\_theme\_map

<code style='color: royalblue;'>function</code> <code style='color: green;'>public</code>

```python
def get_theme_map(
) -> dict[typing.Literal['dark', 'light'], str | pathlib.Path | module]: ...
```
Get the theme map

### register\_event

<code style='color: royalblue;'>function</code> <code style='color: green;'>public</code>

```python
def register_event(
    func: typing.Callable[[bool, typing.Any], typing.Any],
    *args: typing.Any,
) -> None: ...
```

When the system accent color changes, the registered function will be called,
and the parameter is a boolean value indicating whether it is currently a dark theme

* `func`: callback function
* `args`: extra arguments


### remove\_event

<code style='color: royalblue;'>function</code> <code style='color: green;'>public</code>

```python
def remove_event(
    func: typing.Callable[[bool, typing.Any], typing.Any],
) -> None: ...
```

Remove a registered function

* `func`: callback function


### reset\_theme\_map

<code style='color: royalblue;'>function</code> <code style='color: green;'>public</code>

```python
def reset_theme_map(
) -> None: ...
```
Reset the value of theme map

### set\_color\_mode

<code style='color: royalblue;'>function</code> <code style='color: green;'>public</code>

```python
def set_color_mode(
    mode: typing.Literal['system', 'dark', 'light'] = 'system',
) -> None: ...
```

Set the color mode of the program

* `mode`: it can be `"light"`, `"dark"`, and `"system"`

TIPS:

`"system"` is the following system


### set\_theme\_map

<code style='color: royalblue;'>function</code> <code style='color: green;'>public</code>

```python
def set_theme_map(
    *,
    light: str | module | None = None,
    dark: str | module | None = None,
) -> None: ...
```

Set the path to the theme file used by the current program

* `light`: the name of the theme of the light theme
* `dark`: the name of the theme of the dark theme


## 🟡 Variables / 变量

### SYSTEM\_DARK\_MODE

<code style='color: skyblue;'>constant</code> <code style='color: green;'>public</code>

```python linenums="0"
SYSTEM_DARK_MODE: bool = True
```


### \_callback\_events

<code style='color: #BBBB00;'>variable</code> <code style='color: orange;'>protected</code>

```python linenums="0"
_callback_events: dict = {}
```


### \_color\_mode

<code style='color: #BBBB00;'>variable</code> <code style='color: orange;'>protected</code>

```python linenums="0"
_color_mode: str = 'system'
```


### \_theme\_map

<code style='color: #BBBB00;'>variable</code> <code style='color: orange;'>protected</code>

```python linenums="0"
_theme_map: dict = {'dark': <module 'tkintertools.theme.dark' from 'C:\\Software\\Python312\\Lib\\site-packages\\tkintertools\\theme\\dark.py'>, 'light': <module 'tkintertools.theme.light' from 'C:\\Software\\Python312\\Lib\\site-packages\\tkintertools\\theme\\light.py'>}
```


