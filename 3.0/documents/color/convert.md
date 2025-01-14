# tkintertools.color.convert

<small>:octicons-mark-github-16: 源代码：[`tkintertools/color/convert.py`](https://github.com/Xiaokang2022/tkintertools/blob/3.0.0rc6/tkintertools/color/convert.py){ target='_blank' }</small>

Convert a format of color to another format.

* RGB: tuple, (Red, Green, Blue)
* HSL: tuple, (Hue, Saturation, Lightness)
* RGBA: tuple, (Red, Green, Blue, Alpha)
* HEX: hexadecimal, such as '#ABCDEF' or '#12345678'
* NAME: string, such as 'royalblue'


## 🔵`fix_hex_length`


<code style='color: royalblue;'>function</code> <code style='color: green;'>public</code>

```python
def fix_hex_length(
    value: str,
) -> str: ...
```
Fix the length of a hexadecimal code.

* `value`: a hexadecimal code


## 🔵`hex_to_hsl`


<code style='color: royalblue;'>function</code> <code style='color: green;'>public</code>

```python
def hex_to_hsl(
    value: str,
) -> tuple[float, float, float]: ...
```
Convert a hexadecimal code to a HSL code.

* `value`: a hexadecimal code


## 🔵`hex_to_name`


<code style='color: royalblue;'>function</code> <code style='color: green;'>public</code>

```python
def hex_to_name(
    value: str,
) -> list[str]: ...
```
Convert a hexadecimal code to a color name.

* `value`: a hexadecimal code


## 🔵`hex_to_rgb`


<code style='color: royalblue;'>function</code> <code style='color: green;'>public</code>

```python
def hex_to_rgb(
    value: str,
) -> tuple[int, int, int]: ...
```
Convert a hexadecimal code to a RGB code.

* `value`: a hexadecimal code


## 🔵`hex_to_rgba`


<code style='color: royalblue;'>function</code> <code style='color: green;'>public</code>

```python
def hex_to_rgba(
    value: str,
) -> tuple[int, int, int, float]: ...
```
Convert a hexadecimal code to a RGBA code.

* `value`: a hexadecimal code


## 🔵`hex_to_hsl`


<code style='color: royalblue;'>function</code> <code style='color: green;'>public</code>

```python
def hex_to_hsl(
    value: str,
) -> tuple[float, float, float]: ...
```
Convert a hexadecimal code to a HSL code.

* `value`: a hexadecimal code


## 🔵`hex_to_name`


<code style='color: royalblue;'>function</code> <code style='color: green;'>public</code>

```python
def hex_to_name(
    value: str,
) -> list[str]: ...
```
Convert a hexadecimal code to a color name.

* `value`: a hexadecimal code


## 🔵`hex_to_rgb`


<code style='color: royalblue;'>function</code> <code style='color: green;'>public</code>

```python
def hex_to_rgb(
    value: str,
) -> tuple[int, int, int]: ...
```
Convert a hexadecimal code to a RGB code.

* `value`: a hexadecimal code


## 🔵`hex_to_rgba`


<code style='color: royalblue;'>function</code> <code style='color: green;'>public</code>

```python
def hex_to_rgba(
    value: str,
) -> tuple[int, int, int, float]: ...
```
Convert a hexadecimal code to a RGBA code.

* `value`: a hexadecimal code


## 🔵`hsl_to_hex`


<code style='color: royalblue;'>function</code> <code style='color: green;'>public</code>

```python
def hsl_to_hex(
    value: tuple[float, float, float],
) -> str: ...
```
Convert a HSL code to a hexadecimal code.

* `value`: a HSL code


## 🔵`hsl_to_rgb`


<code style='color: royalblue;'>function</code> <code style='color: green;'>public</code>

```python
def hsl_to_rgb(
    value: tuple[float, float, float],
) -> tuple[int, int, int]: ...
```
Convert a HSL code to a RGB code.

* `value`: a HSL code


## 🔵`hsl_to_hex`


<code style='color: royalblue;'>function</code> <code style='color: green;'>public</code>

```python
def hsl_to_hex(
    value: tuple[float, float, float],
) -> str: ...
```
Convert a HSL code to a hexadecimal code.

* `value`: a HSL code


## 🔵`hsl_to_rgb`


<code style='color: royalblue;'>function</code> <code style='color: green;'>public</code>

```python
def hsl_to_rgb(
    value: tuple[float, float, float],
) -> tuple[int, int, int]: ...
```
Convert a HSL code to a RGB code.

* `value`: a HSL code


## 🔵`name_to_hex`


<code style='color: royalblue;'>function</code> <code style='color: green;'>public</code>

```python
def name_to_hex(
    value: str,
) -> str: ...
```
Convert a color name to a hexadecimal code.

* `value`: a color name


## 🔵`name_to_rgb`


<code style='color: royalblue;'>function</code> <code style='color: green;'>public</code>

```python
def name_to_rgb(
    value: str,
) -> tuple[int, int, int]: ...
```
Convert a color name to a RGB code.

* `value`: a color name


## 🔵`name_to_hex`


<code style='color: royalblue;'>function</code> <code style='color: green;'>public</code>

```python
def name_to_hex(
    value: str,
) -> str: ...
```
Convert a color name to a hexadecimal code.

* `value`: a color name


## 🔵`name_to_rgb`


<code style='color: royalblue;'>function</code> <code style='color: green;'>public</code>

```python
def name_to_rgb(
    value: str,
) -> tuple[int, int, int]: ...
```
Convert a color name to a RGB code.

* `value`: a color name


## 🔵`rgb_to_hex`


<code style='color: royalblue;'>function</code> <code style='color: green;'>public</code>

```python
def rgb_to_hex(
    value: tuple[int, int, int],
) -> str: ...
```
Convert a RGB code to a hexadecimal code.

* `value`: a RGB code


## 🔵`rgb_to_hsl`


<code style='color: royalblue;'>function</code> <code style='color: green;'>public</code>

```python
def rgb_to_hsl(
    value: tuple[int, int, int],
) -> tuple[float, float, float]: ...
```
Convert a RGB code to a HSL code.

* `value`: a RGB code


## 🔵`rgb_to_name`


<code style='color: royalblue;'>function</code> <code style='color: green;'>public</code>

```python
def rgb_to_name(
    value: tuple[int, int, int],
) -> list[str]: ...
```
Convert a RGB code to a color name.

* `value`: a RGB code


## 🔵`rgb_to_hex`


<code style='color: royalblue;'>function</code> <code style='color: green;'>public</code>

```python
def rgb_to_hex(
    value: tuple[int, int, int],
) -> str: ...
```
Convert a RGB code to a hexadecimal code.

* `value`: a RGB code


## 🔵`rgb_to_hsl`


<code style='color: royalblue;'>function</code> <code style='color: green;'>public</code>

```python
def rgb_to_hsl(
    value: tuple[int, int, int],
) -> tuple[float, float, float]: ...
```
Convert a RGB code to a HSL code.

* `value`: a RGB code


## 🔵`rgb_to_name`


<code style='color: royalblue;'>function</code> <code style='color: green;'>public</code>

```python
def rgb_to_name(
    value: tuple[int, int, int],
) -> list[str]: ...
```
Convert a RGB code to a color name.

* `value`: a RGB code


## 🔵`rgb_to_rgba`


<code style='color: royalblue;'>function</code> <code style='color: green;'>public</code>

```python
def rgb_to_rgba(
    value: tuple[int, int, int],
) -> tuple[int, int, int, float]: ...
```
Convert a RGB code to a RGBA code.

* `value`: a RGB code


## 🔵`rgba_to_hex`


<code style='color: royalblue;'>function</code> <code style='color: green;'>public</code>

```python
def rgba_to_hex(
    value: tuple[int, int, int, float],
) -> str: ...
```
Convert a RGBA code to a hexadecimal code.

* `value`: a RGBA code


## 🔵`rgba_to_hex`


<code style='color: royalblue;'>function</code> <code style='color: green;'>public</code>

```python
def rgba_to_hex(
    value: tuple[int, int, int, float],
) -> str: ...
```
Convert a RGBA code to a hexadecimal code.

* `value`: a RGBA code


## 🔵`rgba_to_rgb`


<code style='color: royalblue;'>function</code> <code style='color: green;'>public</code>

```python
def rgba_to_rgb(
    value: tuple[int, int, int, float],
    /,
    *,
    refer: tuple[int, int, int],
) -> tuple[int, int, int]: ...
```
Convert a RGBA code to a RGB code.

* `value`: a RGBA code
* `refer`: a RGB code 


## 🔵`str_to_rgb`


<code style='color: royalblue;'>function</code> <code style='color: green;'>public</code>

```python
def str_to_rgb(
    value: str,
) -> tuple[int, int, int]: ...
```
Convert a color name or a hexadecimal code to a RGB code.

* `value`: a color name or a hexadecimal code


## 🔵`str_to_rgb`


<code style='color: royalblue;'>function</code> <code style='color: green;'>public</code>

```python
def str_to_rgb(
    value: str,
) -> tuple[int, int, int]: ...
```
Convert a color name or a hexadecimal code to a RGB code.

* `value`: a color name or a hexadecimal code


