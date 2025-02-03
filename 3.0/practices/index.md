---
comments: true
icon: material/pencil-circle
---

# 实战教学

!!! warning "特别注意：教程版本要求"

    目前此教程对应的环境如下：

    * maliang: `3.0.0rc6`
    * Python: `3.13.1`
    * OS: `Windows 10 22H2`

    若您需要的教程不是该版本，请在网页左上切换版本！

## 一、阅前须知

### 1.1 主题说明<font color="red">*</font>

此网站主题默认跟随系统，可手动调节为暗色主题或者亮色主题，这不仅会影响网站的颜色外观，更会**影响部分在不同主题下的图片**，因为 `maliang` 涉及亮色和暗色主题，所以部分效果预览图也会同步受网站主题而切换。

例如，下面的 “[*图1 在 VSCode 中查看类的文档字符串*](#14-前置需求)” 就受网站主题影响，大家可以试着在页面顶部切换网站主题颜色，看看这张图片有什么变化。

此外，本站的所有图片都可以通过点击来放大。

### 1.2 图像说明<font color="red">*</font>

图形分为两种，一种是由图片文件直接展示的，还有一种是由 Markdown 的 Mermaid 语法代码块生成的，如下面的[流程图](#21-关于该项目名字的由来)。某些时候这些图没有完全生成，而是呈现出一种源代码的状态，此时可以尝试刷新网页重新让它们生成。

另外，它们的颜色也与主题有关。

### 1.3 前置需求

推荐在阅读此教程的同时搭配 Visual Studio Code（以下简称 VSCode）进行开发，使用 PyCharm 或者 Visual Studio 也可以，但我个人更推荐使用 VSCode。

`maliang 3`（以下简称 `maliang`） 专门对 VSCode 做了文档字符串的优化，可以十分方便地在 VSCode 内看到每个函数、类甚至是常量的详细信息，包括它们的类型、默认值和使用方法。**只需要将鼠标移动到想要查看的函数或者类上面即可**，PyCharm 和 Visual Studio 也有类似的功能，但渲染效果不如 VSCode 的那么好。虽然可以直接查看文档字符串，但 `maliang` 在开发的时候为了力求符合 [PEP 8](https://peps.python.org/pep-0008/) 的规则，所以文档字符串均是英文的。阅读起来不方便的朋友们可以在本站查阅教程来进行辅助开发。

![light](images/0-1.light.png#only-light)
![dark](images/0-1.dark.png#only-dark)

<p align="center"><small>图1 在 VSCode 中查看类的文档字符串</small></p>

## 二、本教程具体编写情况

### 1.1 编写人员

教程目前由`maliang`作者和[MuXue1230](https://github.com/MuXue1230)<!--此处应补充更多编写人员-->编写。如果你发现问题，可以在[GitHub](https://github.com/Xiaokang2022/maliang-docs/issues)上提交 Issue ，我们会尽快修正它们。

当然，如果您也想参与编写本教程，欢迎提交 Pull Request ！

### 1.2 教程源码

本教程的所有源代码均可在编写者本人的 GitHub 主页找到。我们会在每篇教程上注明编写之名称。

