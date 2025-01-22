# maliang.core.configs

<small>:octicons-mark-github-16: 源代码：[`maliang/core/configs.py`](https://github.com/Xiaokang2022/maliang/blob/3.0.0rc6/maliang/core/configs.py){ target='_blank' }</small>

All global configuration options.

Some options are read-only, but most of them can be changed, and once changed,
they will take effect globally for the program. Some changes take effect
immediately, but some need to take effect when the relevant option is invoked.


## 🟢`Constant`



<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code> | `object`



## 🟢`Env`



<code style='color: limegreen;'>class</code> <code style='color: green;'>public</code> | `object`

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
Get the default font family.



## 🟢`_DefaultRootDescriptor`



<code style='color: limegreen;'>class</code> <code style='color: orange;'>protected</code> | `object`

### 🟡`__get__`


<code style='color: #BBBB00;'>method</code> <code style='color: purple;'>special</code>

```python
def __get__(
    self,
    *args,
    **kwargs,
) -> tkinter.Tk: ...
```
Returns the current default root.

In some cases, the method also returns `tkinter.Tk` and `None`, but
this can happen if the usage is not recommended.




## 🔵`reset`


<code style='color: royalblue;'>function</code> <code style='color: green;'>public</code>

```python
def reset(
) -> None: ...
```
Reset all configuration options.

