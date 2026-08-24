---
layout: default
title: "Horizon Summary: 2026-08-24 (EN)"
date: 2026-08-24
lang: en
---

> From 64 items, 1 important content pieces were selected

---

1. [Emacs 31.1 Released with Dumper Removal and New Features](#item-1) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Emacs 31.1 Released with Dumper Removal and New Features](https://lwn.net/Articles/1090308/) ⭐️ 8.0/10

Emacs 31.1 has been released, featuring the removal of the legacy Emacs dumper, a new User Lisp directory mechanism, a "Send to..." menu item in context-menu-mode, and various quality-of-life improvements. The removal of the old dumper marks a significant architectural shift, as Emacs has been transitioning to the portable dumper since version 27. This simplifies the build system and improves startup performance and portability for users across different platforms. The new User Lisp directory provides a simpler mechanism than full package installation, with no automatic dependency resolution or upgrading. The context-menu-mode, introduced in Emacs 28, now includes a "Send to..." menu item for easier file management.

rss · LWN.net · Aug 24, 13:36

**Background**: Emacs is a highly extensible, self-documenting text editor that has been under development since the 1970s. The "dumper" refers to a technique used to speed up Emacs startup by saving a snapshot of the running editor to disk. Since Emacs 27, a "portable dumper" was introduced to replace the older unexec-based approach, offering better cross-platform compatibility. The User Lisp directory allows users to place custom Lisp files in a dedicated directory that Emacs automatically scans and loads at startup.

<details><summary>References</summary>
<ul>
<li><a href="https://casouri.github.io/note/2020/painless-transition-to-portable-dumper/index.html">Painless Transition to Portable Dumper</a></li>
<li><a href="https://casouri.github.io/emacs-manuals/master/emacs/User-Lisp-Directory.html">User Lisp Directory (GNU Emacs Manual) - casouri.github.io</a></li>

</ul>
</details>

**Tags**: `#Emacs`, `#software release`, `#open source`, `#text editor`, `#Lisp`

---