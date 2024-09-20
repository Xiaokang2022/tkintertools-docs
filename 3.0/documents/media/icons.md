# tkintertools.media.icons

All icons with base64 format

## 🔵`parse`


<code style='color: royalblue;'>function</code> <code style='color: green;'>public</code>

```python
def parse(
    *,
    light: str = 'black',
    dark: str = 'white',
) -> dict[str, dict[typing.Literal['light', 'dark'], tkintertools.toolbox.enhanced.PhotoImage]]: ...
```
Parse the base64 data to `enhanced.PhotoImage` with diffrent themes

## 🟣`BASE64_DATAS`


<code style='color: skyblue;'>constant</code> <code style='color: green;'>public</code>

```python linenums="0"
BASE64_DATAS: dict = {
    'audio': 'iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAACXBIWXMAAAsTAAALEwEAmpwYAAACEklEQVR4nOWXz0tUURzFP2okGYGbFia9mkBGW2gNaIEmaBmuRBBcuPL/aFM7dSdRli4EjcCFv3Zu3CiTEUO4KQr8LWjQuGkVQU5c+j64fLnzZp7vOZEeuIv35b53ztzvuefegf8clf+K2ANWgRwwA5SVkvwmsC3k/rhTSvIdRW5Gd575ZmWGgftxkCfykAcJMJgCfgMvo3gmEUBeSIDBQ+AAWAOqw5LfAnYDyF0CLgBJVbsGfBIRVXGS5xwCWoFjYFKR1QB7wHic5Lk8LegFsvKLr1j1B+KJTr/QBCwCGRkjwEXgS5HkQR4wu+YbsKDq08B7/+Gr+tgzIBWC3BZgVq1CkbUBv4B+q9Yg76VwfOyJLNNJBBxKSD1SIt4A66r2QTIiVgFXgRfAT6DZImuWefVWbVjiPFYBPuaAJZWI34FBqzYAHJ2WgD7ghzqkMvJtH49lN5xNAfOOFmQdLciehgnHHCZskXlJZcKVuAWYA2tLDh+9DT86tuGQK4ieRggiLyCIjC983Jb37pqHRolKP4qHJIo/R/CAjuJZRxSbMyL01SuMgB4xWRq4bNXbxf0dwfR/cUN6GlZAg5BMAJfUnWAfeF0MeRgRrhUwfrBRK219p0QVBa+AiEJXsi45qNInuZLZIjZDCigH3ko7nou5I8HLI8LEqgtmS44C94gR14ENJaCOEqMWWJaL5yvO459T4sIfGZlv31STYj8AAAAASUVORK5CYII=',
    'fullscreen': 'iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAACXBIWXMAAAsTAAALEwEAmpwYAAABOUlEQVR4nO2Wz4rCMBDGf16WfQyFfR+FfYNuL/WVKqtnT4vgM+Xqn6s2EohQYppMYquH7QehNGTm+zLJTAZGjHjEGmgA7RlHYE43FsCpw/ZqfUfRdDi4jzpgu4rYXiQCtDMUsLXDEEwDtlO75r5eefwlC2iAinQUNuzZAlTLgfmWCeQ/jq3KEbB1dmEisRTYuzaV9ZUlgEQRPnJSBRw9t70UHIcbdvPvZsdBImBhyd3bHhIRIsf6qiM1RIS2iB0wEZD3jgLYA5+BMx8ck3fsvA0fuRH1EhSesH8Af8I6McjOd5kVszMNTd7OnPnQmcfqxBewAb5JKEQrIblExNrOn/soxdXQpVgHHqPqlY+ReiLPyz6eY/3uhkRntGSzPlqyy4BNqYlmFL8BEYfIkzpvpbGPXNSWj/hfuAFAwArFCQQ3DQAAAABJRU5ErkJggg==',
    'pause': 'iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAACXBIWXMAAAsTAAALEwEAmpwYAAAAxElEQVR4nO2XSwoCMQyGP72MuvdxCRlhYJY+jqQH0MGtt1GP40AlMEKRThpEHBf5Iavm+xvoKwXXn2oBHIBLFDWwBQYKNwR2bW7MitfcOvkKaIDQEWLepbPCiWdhKeCumLxilOAmBu5qKaAxGJUJrjRw4p1VMESV4Coj6wVkFXwJ8E2IH0P8Igp+FeOPEf4c01tD0vTdkt0+bErH32pKC+ChmBwVtlY48Vxi1AzYv30uTsA68zGRsU2bG7PiNbVO7uKXegIw48Yw1VCM+AAAAABJRU5ErkJggg==',
    'play': 'iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAACXBIWXMAAAsTAAALEwEAmpwYAAAA50lEQVR4nO3XMUpDQRSF4Q9sVLAQFVTQ0i6t1lYi2mYLrsEl2LsDF2CTMmYHabOCpFQUTCXEsZknKRRB8jyFOfA309y/mLn3Dst8nzUc41Ag53hEwTvucfRXxTfxXIvP84ZbbLctcPZF8XlecI3VtgS6Pwg0jHGFlZRAqQxxmhQolT46SYGCGe6wmxIolSlusJESKJXJby5qd4ECDSNcJAVKpYedpEDBIC1QsJ8W2EsKPPzLSzhKPcNJqhFNU614lhxG/dQ4HqYWknFbK9lleindwmtyLVebxlPqY9JkHSc4+DxZxuLzAYtSled9u6veAAAAAElFTkSuQmCC',
}
```


