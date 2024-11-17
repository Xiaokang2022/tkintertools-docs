# tkintertools.core.configs

All configs of tkintertools

## 🟢`Constant`



<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code> | `object`



## 🟢`Env`



<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code> | `object`

### 🟡`<lambda>`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def <lambda>(
    _,
) -> _empty: ...
```


### 🟡`get_default_system`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def get_default_system(
) -> str: ...
```
Get the system of environment.



## 🟢`Font`



<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code> | `object`

### 🟡`get_default_family`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def get_default_family(
) -> str: ...
```
Get font family.



## 🟢`Theme`



<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code> | `object`

### 🟡`get_default_themes`


<code style='color: #BBBB00;'>method</code> <code style='color: green;'>public</code>

```python
def get_default_themes(
) -> tuple[types.ModuleType, types.ModuleType]: ...
```
Get default themes.



## 🟢`_DefaultRoot`



<code style='color: limegreen;'>class</code> <code style='color: orange;'>protected</code> | `object`

### 🟡`__get__`


<code style='color: #BBBB00;'>method</code> <code style='color: purple;'>special</code>

```python
def __get__(
    self,
    obj,
    cls,
) -> tkinter.Tk | None: ...
```
Return the current default root.



## 🔵`reset_configs`


<code style='color: royalblue;'>function</code> <code style='color: green;'>public</code>

```python
def reset_configs(
) -> None: ...
```
Reset all configs.

