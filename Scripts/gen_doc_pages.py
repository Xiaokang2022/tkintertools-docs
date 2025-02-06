"""Generate the document pages."""

import inspect
import pathlib
import typing

import maliang
import maliang.media
import maliang.mpl
import maliang.three
import mkdocs_gen_files

DIR: typing.Final[str] = "documents"
MOD_SYMBOL: typing.Final[str] = '<code class="doc-symbol doc-symbol-nav doc-symbol-module"></code>'
PKG_SYMBOL: typing.Final[str] = '<code class="doc-symbol doc-symbol-nav doc-symbol-parameter"></code>'

nav = mkdocs_gen_files.Nav()
src = pathlib.Path(inspect.getfile(maliang)).parent


def get_data(values: str, /) -> tuple[str, str]:
    """Returns the repo and version of a parts."""
    if "media" in values:
        return "maliang-media", maliang.media.__version__
    if "mpl" in values:
        return "maliang-mpl", maliang.mpl.__version__
    if "three" in values:
        return "maliang-three", maliang.three.__version__
    return "maliang", maliang.__version__


with mkdocs_gen_files.open(f"{DIR}/summary.md", "w") as nav_file:
    for path in sorted(src.rglob("*.py")):
        module_path = maliang.__name__ / path.relative_to(src).with_suffix("")
        doc_path = path.relative_to(src).with_suffix(".md")
        full_doc_path = DIR / doc_path
        parts = tuple(module_path.parts)
        file = "/".join(parts) + ".py"

        symbol = MOD_SYMBOL

        if parts[-1] == "__init__":
            parts = parts[:-1]
            doc_path = doc_path.with_name("index.md")
            full_doc_path = full_doc_path.with_name("index.md")
            symbol = PKG_SYMBOL
        elif parts[-1] == "__main__":
            continue

        with mkdocs_gen_files.open(full_doc_path, "w") as fd:
            identifier = ".".join(parts)
            if full_doc_path == pathlib.Path(f"{DIR}/index.md"):
                fd.write(f"---\ntitle: {identifier}\ncomments: true\nicon: material/file-document\n---\n\n")
            else:
                fd.write(f"---\ntitle: {identifier}\n---\n\n")
            fd.write(f"# {symbol} {identifier}\n\n")
            repo, tag = get_data(file)
            fd.write(f"<small>:octicons-mark-github-16: 源代码：[`{file}`](https://github.com/Xiaokang2022/{repo}/blob/{tag}/{file}){{ target='_blank' }}</small>\n\n")
            fd.write(f"::: {identifier}\n")

        if full_doc_path == pathlib.Path(f"{DIR}/index.md"):
            nav_file.write("* [](index.md)\n")
        else:
            space = "    " if symbol == MOD_SYMBOL else ""
            nav_file.write(f"{space}* [{symbol} {parts[-1]}]({str(doc_path).replace("\\", "/")})\n")
