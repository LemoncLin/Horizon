---
layout: default
title: "Horizon Summary: 2026-08-13 (ZH)"
date: 2026-08-13
lang: zh
---

> 从 51 条内容中筛选出 4 条重要资讯。

---

1. [谷歌发布 Gemini 3.7 Flash 编码与智能体模型](#item-1) ⭐️ 8.0/10
2. [Christopher Domas 发布 DRAM 漏洞利用项目'Spaghettifying DRAM'](#item-2) ⭐️ 8.0/10
3. [rsync 3.5.0 发布，含 33 项安全修复](#item-3) ⭐️ 8.0/10
4. [🤖 Google 发布 Gemini 3.6 Flash，并透露 Gemini 4 已启动预训练  Google 发布 Gemini 3.6 Flash，称新模](#item-4) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [谷歌发布 Gemini 3.7 Flash 编码与智能体模型](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-3-7-flash/) ⭐️ 8.0/10

谷歌发布了 Gemini 3.7 Flash，这是专为编码和智能体任务打造的最新智能工作模型，距离 Gemini 3.6 Flash 发布仅三周。该模型采用入门定价，将于 2026 年 12 月 31 日翻倍。 此次发布巩固了谷歌在竞争激烈的 LLM 市场中的地位，以更低的成本层级提供改进的编码和智能体能力。快速的发布周期和定价策略表明谷歌正在与 OpenAI 的 Opus 和 Anthropic 的 Luna 等模型进行激烈竞争。 Gemini 3.7 Flash 在智能体编码和知识工作方面带来显著提升，基准测试涵盖推理、多模态能力和长上下文处理。该模型与其他工具结合时，可以从文本提示生成可完全游玩的 3D 游戏。

hackernews · thisisauserid · 8月13日 17:23 · [社区讨论](https://news.ycombinator.com/item?id=49289112)

**背景**: Gemini Flash 系列是谷歌的经济型模型线，专为高吞吐量、低延迟的应用设计，而 Pro 模型则针对更复杂的推理任务。与 Pro 系列相比，Flash 模型通常提供更快的响应速度和更低的成本，适合生产环境使用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-3-7-flash/">Gemini 3.7 Flash: our most intelligent workhorse model</a></li>

</ul>
</details>

**社区讨论**: 社区成员称赞了 Gemini 的视觉能力，但指出 Opus 在图像转 HTML 任务方面仍是最佳选择。人们对定价策略表示担忧，入门价格将在短短五个月内翻倍，比较显示 Luna 在 DeepSWE 1.1 等基准测试中仍然表现更优。

**标签**: `#AI`, `#LLM`, `#Google Gemini`, `#Model Release`, `#Pricing`

---

<a id="item-2"></a>
## [Christopher Domas 发布 DRAM 漏洞利用项目'Spaghettifying DRAM'](https://github.com/xoreaxeaxeax/skitter-creek-bath-salts) ⭐️ 8.0/10

安全研究员 Christopher Domas 发布了名为 skitter-creek-bath-salts 的概念验证工具，该工具利用 AMD 处理器内存控制器架构来混淆 DRAM 地址映射，从而绕过硬件安全机制。 这项研究展示了 AMD 硬件上的新攻击面，对控制台安全和低级系统访问具有影响，正如社区讨论中提到的对 Xbox 和 PlayStation 的潜在影响。 该漏洞利用目前适用于 2013 年的 AMD Jaguar 架构，注释表明 Zen 3 的内存控制器寄存器基地址不同，且攻击面仅限于特定的 AMD 处理器家族。

hackernews · matt_d · 8月13日 14:17 · [社区讨论](https://news.ycombinator.com/item?id=49286341)

**背景**: 动态随机存取存储器（DRAM）是计算机中的主要易失性内存，其日益复杂的结构扩大了攻击面。2014 年发现的 Rowhammer 效应涉及重复访问 DRAM 行导致相邻行发生位翻转，从而引发安全漏洞。现代 DRAM 访问通常需要专有固件，使得低级操作更具挑战性，但一旦利用则影响更大。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://news.linxi.com.au/news/amd-hardware-vulnerability-exposed-by-dram-address-scrambling-research">AMD DRAM Scrambling Exploit Bypasses Security Fences | Linxi News</a></li>
<li><a href="https://github.com/xoreaxeaxeax">xoreaxeaxeax (domas) · GitHub</a></li>
<li><a href="https://en.wikipedia.org/wiki/Row_hammer">Row hammer - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 社区对这项研究充满热情，期待 Domas 的 Black Hat 演讲。讨论突出了 DRAM 日益复杂的结构及其扩大的攻击面，同时也提出了关于除已测试的 Jaguar 架构外与新 AMD 处理器兼容性的问题。

**标签**: `#hardware-security`, `#DRAM`, `#exploit-research`, `#systems-security`, `#Black-Hat`

---

<a id="item-3"></a>
## [rsync 3.5.0 发布，含 33 项安全修复](https://lwn.net/Articles/1088759/) ⭐️ 8.0/10

rsync 3.5.0 已发布，包含 33 项安全修复，解决了路径处理和守护进程协议漏洞问题，这些漏洞是通过专项审计、守护进程协议模糊测试以及外部研究人员报告发现的。该版本还包含多项健壮性加固措施，每项修复均附有回归测试。 rsync 是一款广泛使用的文件同步工具，此次发布代表了一次重大的安全加固行动。这 33 项修复针对的漏洞可能影响依赖 rsync 在网络间传输文件的系统管理员和安全意识强的工程师。 CVE 编号由 VulnCheck 作为 CVE 编号权威机构（CNA）分配，许多漏洞的版本范围比单纯的"3.5.0 之前的所有版本"要窄得多。每项修复都在测试套件中包含回归测试，在未修复的代码上会失败，确保漏洞得到妥善修复。

rss · LWN.net · 8月13日 13:47

**背景**: rsync（远程同步）是一款通过网络在计算机之间传输和同步文件的工具，使用 delta-transfer 算法高效地检测和传输文件差异，而非整个文件。rsync 守护进程协议允许 rsync 以服务器模式运行，实现集中式文件存储库。模糊测试是一种自动化软件测试技术，通过向程序输入无效、意外或随机数据来发现崩溃、内存泄漏或其他漏洞。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Rsync">rsync - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Fuzzing">Fuzzing - Wikipedia</a></li>
<li><a href="https://www.cve.org/ResourcesSupport/AllResources/CNARules">CVE Numbering Authority (CNA) Operational Rules</a></li>

</ul>
</details>

**标签**: `#rsync`, `#security`, `#system-administration`, `#open-source`

---

<a id="item-4"></a>
## [🤖 Google 发布 Gemini 3.6 Flash，并透露 Gemini 4 已启动预训练  Google 发布 Gemini 3.6 Flash，称新模](https://t.me/zaihuapd/43177) ⭐️ 8.0/10

Google released Gemini 3.6 Flash with improved efficiency and capabilities, while revealing that Gemini 4 has already begun pre-training.

telegram · zaihuapd · 8月13日 17:32

**标签**: `#AI`, `#Google`, `#Gemini`, `#LLM`, `#Model Release`

---