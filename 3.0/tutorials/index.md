---
comments: true
icon: material/book
---

# 官方教程

!!! warning "特别注意：教程版本要求"

    目前此教程对应的环境如下：

    * maliang: `3.0.0`
    * Python: `3.13.0`
    * OS: `Windows 11 24H2`

    若您需要的教程不是该版本，请在网页左上切换版本！

!!! success "特别提供：相关教程及文档链接"

    * Tcl / Tk 8.6 官方文档：https://www.tcl.tk/man/tcl8.6/contents.htm
    * Tcl / Tk 9.0 官方文档：https://www.tcl.tk/man/tcl9.0/
    * 个人不完整 Tk 参考教程：https://xiaokang2022.blog.csdn.net/category_11600888.html
    * 个人推荐的 Tk 参考教程：https://blog.csdn.net/qq_41556318/category_9283243.html

## 一、阅前须知

### 1.1 标签说明<font color="red">*</font>

* <code style='color: limegreen;'>new</code>: 最新功能，需要[最新提交](./chapter_01/1.md#三体验最新功能)的 `maliang` 版本，而非已发行的版本；
* <code style='color: orange;'>deprecated</code>: 弃用功能，未来将不再使用；
* <code style='color: mediumpurple;'>experimental</code>: 实验性功能，功能可能不完善或者存在问题；
* <code style='color: royalblue;'>fixed</code>: 修复的功能，当前版本存在问题但最新版本中修复的；
* <code style='color: red;'>bug</code>: 存在已知问题的功能；
* <code style='color: darkgoldenrod;'>third-party</code>: 第三方功能，功能由第三方包提供；

### 1.2 主题说明<font color="red">*</font>

此网站主题默认跟随系统，可手动调节为暗色主题或者亮色主题，这不仅会影响网站的颜色外观，更会**影响部分在不同主题下的图片**，因为 `maliang` 涉及亮色和暗色主题，所以部分效果预览图也会同步受网站主题而切换。

例如，下面的 “[*图1 在 VSCode 中查看类的文档字符串*](#14-前置需求)” 就受网站主题影响，大家可以试着在页面顶部切换网站主题颜色，看看这张图片有什么变化。

此外，本站的所有图片都可以通过点击来放大。

### 1.3 图像说明<font color="red">*</font>

图形分为两种，一种是由图片文件直接展示的，还有一种是由 Markdown 的 Mermaid 语法代码块生成的。某些时候这些图没有完全生成，而是呈现出一种源代码的状态，此时可以尝试刷新网页重新让它们生成。

另外，它们的颜色也与主题有关。

### 1.4 前置需求

推荐在阅读此教程的同时搭配 Visual Studio Code（以下简称 VSCode）进行开发，使用 PyCharm 或者 Visual Studio 也可以，但我个人更推荐使用 VSCode。

`maliang 3`（以下简称 `maliang`） 专门对 VSCode 做了文档字符串的优化，可以十分方便地在 VSCode 内看到每个函数、类甚至是常量的详细信息，包括它们的类型、默认值和使用方法。**只需要将鼠标移动到想要查看的函数或者类上面即可**，PyCharm 和 Visual Studio 也有类似的功能，但渲染效果不如 VSCode 的那么好。虽然可以直接查看文档字符串，但 `maliang` 在开发的时候为了力求符合 [PEP 8](https://peps.python.org/pep-0008/) 的规则，所以文档字符串均是英文的。阅读起来不方便的朋友们可以在本站查阅教程来进行辅助开发。

![light](images/0-1.light.png#only-light)
![dark](images/0-1.dark.png#only-dark)

<p align="center"><small>图1 在 VSCode 中查看类的文档字符串</small></p>

## 二、想说的一些事情

### 2.1 关于该项目名字的由来

实际上，该项目的旧版本并不叫 `maliang`，而是 `tkintertools`。这是因为在以前本项目还没有做得这么大的时候，本项目只是一个用来辅助 tkinter 进行开发的工具，所以取名为 `tkinter` 和 tools 的结合，但这个名称将止步于 3.0.0 版本，在这个版本发布前，经过社区投票，我决定更改这个项目的名称，并最终取名为 `maliang`。

至于为什么要起这个名字，实际和本项目的最终目标有一定联系，不知大家小时候有没有用画板画程序界面的这种想法？有些人不仅想过，还实际做过，比如我。小时候看着花花绿绿的电脑屏幕，不会编程的我只能用“画图.exe”在上面画一些自己幻想的程序，觉得非常好玩。是的，这很好玩，但这并不是真的界面，只是一副可能算不上画的画罢了。但“神笔马良”的故事大家都知道，马良有一支神笔，能让画出来的东西变成真的！要是有这么一个项目，真的能让画出来的界面变成真的，岂不美哉？

是的，你想的没错，**通过画画来构建图形界面就是这个项目的终极目标**。因此，该项目被重命名为了 `maliang`。这个时候就有人要问了，你这怎么只有“马良”，你的“神笔”呢？别急！“神笔”也是有的，本项目只是一个 UI 框架，但还需一个配套的可视化开发软件，而这个软件就是“神笔”，目前“神笔”项目还处于初期阶段，只能实现控件的拖拽，待 maliang 正式版本发布后，我将会投入主要精力到“神笔”的开发中。

“神笔”项目也是开源的，项目链接为：<https://github.com/Xiaokang2022/magic-brush>

### 2.2 养成看教程和文档的好习惯

教程和文档是最好的资源，实时更新和维护，尽可能保证准确性，养成看教程和文档的好习惯会让你的开发事半功倍。

~~所以不要有事没事儿就问我这问我那，以及在评论区问东问西（bushi~~
