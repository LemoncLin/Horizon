---
layout: default
title: "Horizon Summary: 2026-08-24 (ZH)"
date: 2026-08-24
lang: zh
---

> 从 64 条内容中筛选出 1 条重要资讯。

---

1. [Emacs 31.1 发布：移除 Dumper 并新增多项功能](#item-1) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Emacs 31.1 发布：移除 Dumper 并新增多项功能](https://lwn.net/Articles/1090308/) ⭐️ 8.0/10

Emacs 31.1 已发布，主要变化包括移除传统的 Emacs dumper、新增用户 Lisp 目录机制、context-menu-mode 中的"发送到..."菜单项，以及多项生活质量改进。 移除旧版 dumper 标志着重大的架构转变，Emacs 自 27 版本起便逐步过渡到 portable dumper。这简化了构建系统，并提升了跨平台的启动性能和可移植性。 新的用户 Lisp 目录比完整的包安装机制更简单，不提供自动依赖解析或升级功能。context-menu-mode 于 Emacs 28 引入，此次新增了"发送到..."菜单项以方便文件管理。

rss · LWN.net · 8月24日 13:36

**背景**: Emacs 是一款高度可扩展的自文档化文本编辑器，自 1970 年代起一直在开发中。"Dumper"指的是一种用于加速 Emacs 启动的技术，通过将运行中的编辑器快照保存到磁盘来实现。自 Emacs 27 起，引入了"portable dumper"来替代基于 unexec 的旧方法，提供更好的跨平台兼容性。用户 Lisp 目录允许用户将自定义 Lisp 文件放在专用目录中，Emacs 会在启动时自动扫描并加载。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://casouri.github.io/note/2020/painless-transition-to-portable-dumper/index.html">Painless Transition to Portable Dumper</a></li>
<li><a href="https://casouri.github.io/emacs-manuals/master/emacs/User-Lisp-Directory.html">User Lisp Directory (GNU Emacs Manual) - casouri.github.io</a></li>

</ul>
</details>

**标签**: `#Emacs`, `#software release`, `#open source`, `#text editor`, `#Lisp`

---