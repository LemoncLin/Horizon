---
layout: default
title: "Horizon Summary: 2026-07-13 (ZH)"
date: 2026-07-13
lang: zh
---

> 从 47 条内容中筛选出 6 条重要资讯。

---

1. [因隐私担忧，洛杉矶警局让 Flock 监控合同到期](#item-1) ⭐️ 8.0/10
2. [2026 年峰会展示利用 BPF 技术屏蔽内核漏洞](#item-2) ⭐️ 8.0/10
3. [CISA 事后报告揭示 GitHub 凭据泄露长达六个月](#item-3) ⭐️ 8.0/10
4. [表观遗传编辑在基因表达调控方面的进展](#item-4) ⭐️ 8.0/10
5. [首次在深空发现真正的糖分子](#item-5) ⭐️ 8.0/10
6. [思维链扩展陷阱：潜在推理的崛起](#item-6) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [因隐私担忧，洛杉矶警局让 Flock 监控合同到期](https://techcrunch.com/2026/07/13/lapd-lets-contract-with-surveillance-giant-flock-expire-citing-serious-concerns-over-civil-liberties-and-privacy/) ⭐️ 8.0/10

洛杉矶警察局已让其与监控技术提供商 Flock 的合同到期，理由是严重关切公民自由和隐私问题。随着对自动化监控基础设施的审查日益严格，这一决定标志着该机构在政策上的重大转变。 此举凸显了执法效率与个人隐私权之间的紧张关系，可能会影响其他市政机构重新评估其对第三方监控供应商的依赖。它引发了关于数据所有权以及公共安全网络中供应商锁定长期影响的重大问题。 一个关键的技术限制是 Flock 保留相机硬件和杆子的所有权，这意味着即使洛杉矶警察局的合同结束，监控基础设施仍在运行并收集数据。这种结构允许 Flock 可能将收集到的数据出售或分享给其他实体，如加州公路巡逻队、洛杉矶警局或联邦调查局，从而建立一个独立于当地警方控制的持久数据收集网络。

hackernews · forks · 7月13日 15:11 · [社区讨论](https://news.ycombinator.com/item?id=48893947)

**背景**: Flock Safety 是美国各地执法机构广泛使用的自动车牌读取系统的主要提供商。这些系统通常涉及私营公司在公共电线杆上安装和维护摄像头，然后将数据馈送到警方可以访问的中心数据库中。其商业模式通常包括长期合同，其中供应商保留资产所有权，这引发了关于这些系统是否会在政治或行政变更结束后仍留下永久性监控基础设施的争论。

**社区讨论**: 社区评论对合同到期的实际影响表示深切怀疑，指出由于 Flock 拥有硬件，无论洛杉矶警察局是否参与，数据收集都会继续。用户强调了“供应商锁定”的风险，认为该系统旨在抵御政治压力，而另一些人则质疑鉴于许多嫌疑人已被警方掌握，监控的效用何在。

**标签**: `#Privacy`, `#Surveillance`, `#Civil Liberties`, `#Tech Policy`

---

<a id="item-2"></a>
## [2026 年峰会展示利用 BPF 技术屏蔽内核漏洞](https://lwn.net/Articles/1081546/) ⭐️ 8.0/10

John Fastabend 在 2026 年 LSFMMBPF 峰会上提出了一种基于 BPF 的技术，旨在保护运行中的内核免受漏洞利用。该方法旨在解决思科在其大量自定义内核设备中部署安全补丁时面临的特定挑战。 这项技术可以显著缩短响应内核漏洞所需的时间，为传统修补方式提供了更快的替代方案。它解决了管理多样化硬件和软件环境的大型组织所面临的重要安全部署挑战。 虽然前景广阔，但除非在内核中添加更多挂钩以允许 BPF 程序拦截相关事件，否则该方法无法完全生效。该演示突出了 eBPF 在运行时安全缓解方面的潜力，而不仅仅是静态修补。

rss · LWN.net · 7月13日 14:14

**背景**: BPF (Berkeley Packet Filter) is a technology originally designed for network packet filtering that has evolved into a powerful framework for running sandboxed programs within the Linux kernel. It allows developers to attach small programs to various kernel hooks for monitoring, tracing, and security purposes without modifying kernel source code. This evolution enables dynamic security measures that can adapt to threats in real-time.

**标签**: `#BPF`, `#Kernel Security`, `#Linux`, `#Exploit Mitigation`

---

<a id="item-3"></a>
## [CISA 事后报告揭示 GitHub 凭据泄露长达六个月](https://krebsonsecurity.com/2026/07/lessons-learned-from-cisas-recent-github-leak/) ⭐️ 8.0/10

美国网络基础设施安全局（CISA）发布了一份事后报告，详细说明了承包商凭据（包括 AWS GovCloud 密钥）在公共 GitHub 存储库中暴露了近六个月才被发现的情况。 这一事件凸显了初始响应协议中的关键缺陷，并为安全团队在凭据管理和监控方面提供了宝贵的教训。 此次泄露涉及数十个 CISA 内部凭据，并持续了近半年，强调了在检测未经授权的公开访问方面的严重疏忽。

rss · Krebs on Security · 7月13日 15:03

**背景**: CISA 是美国负责加强关键基础设施网络安全的联邦机构。AWS GovCloud 是一个隔离的 AWS 区域，旨在处理敏感数据和受监管的工作负载，因此其密钥的暴露尤其危险。

**标签**: `#Cybersecurity`, `#Incident Response`, `#Cloud Security`, `#AWS GovCloud`, `#Best Practices`

---

<a id="item-4"></a>
## [表观遗传编辑在基因表达调控方面的进展](https://www.nature.com/articles/d41586-026-02151-x) ⭐️ 8.0/10

研究人员正在推进重写 DNA 和染色质化学标签的技术，从而在不改变底层 DNA 序列的情况下精确调节基因表达。 这一进展标志着向精准医学的重大转变，通过可逆的表观遗传变化而非永久性基因突变来调节疾病相关基因。 重点在于修饰组蛋白标记和 DNA 甲基化模式，这些是由细胞机制维持的动态过程，需要仔细平衡以避免破坏正常的表观遗传状态。

rss · Nature · 7月13日 00:00

**背景**: 表观遗传学是指不涉及底层 DNA 序列改变的基因功能的可遗传变化。这些变化通常由 DNA 甲基化和组蛋白乙酰化等化学修饰介导，影响 DNA 包装的紧密程度，从而影响基因是否可被转录。与切割 DNA 的传统基因编辑不同，表观遗传编辑旨在通过修改这些化学标签来开启或关闭基因。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.frontiersin.org/journals/medicine/articles/10.3389/fmed.2025.1613722/full">Frontiers | Precision scalpels for the epigenome: next-gen editing tools...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Chromatin_remodeling">Chromatin remodeling - Wikipedia</a></li>

</ul>
</details>

**标签**: `#Epigenetics`, `#Gene Editing`, `#Biotechnology`, `#Genomics`

---

<a id="item-5"></a>
## [首次在深空发现真正的糖分子](https://www.nature.com/articles/d41586-026-02173-5) ⭐️ 8.0/10

科学家在星际空间中发现了赤藓酮糖（erythrulose），这是一种四碳糖，标志着在太阳系外首次探测到如此复杂的糖分子。这一发现于 2026 年 7 月 13 日发表在《自然》杂志上。 这一发现提供了关键证据，证明生命的基本构建模块，特别是 RNA 和 DNA 所需的糖，可以在太空中形成。它支持了早期地球可能从宇宙来源获得这些复杂有机分子的假设，从而有助于生命的起源。 赤藓酮糖是一种分子式为 C₄H₈O₄的酮丁糖，使其成为迄今为止在星际环境中检测到的最复杂的糖。它的鉴定突显了恒星形成区域中丰富的有机化学过程。

rss · Nature · 7月13日 00:00

**背景**: 已在星际空间中检测到超过 260 种不同的分子物种，包括醇类和酸类，这表明复杂的有机化学在宇宙中广泛存在。糖是地球生命的基础，因为它们构成了 RNA 和 DNA 等遗传物质的骨架，并作为能量来源。之前的探测通常涉及较简单的分子，因此赤藓酮糖的鉴定是理解前生物成分如何在宇宙中分布的重要一步。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.sciencealert.com/scientists-find-the-first-true-sugar-ever-detected-in-interstellar-space">Scientists Find The First True Sugar Ever Detected in... : ScienceAlert</a></li>
<li><a href="https://grokipedia.com/page/Erythrulose">Erythrulose</a></li>

</ul>
</details>

**标签**: `#Astrobiology`, `#Chemistry`, `#Space Science`, `#Origins of Life`

---

<a id="item-6"></a>
## [思维链扩展陷阱：潜在推理的崛起](https://www.reddit.com/r/MachineLearning/comments/1uviru5/chain_of_thought_is_a_scaling_trap_the_next_wave/) ⭐️ 8.0/10

该文章指出，由于忠实度和成本问题，思维链正成为扩展陷阱，并倡导转向 Coconut 和 HRM 等潜在推理模型。它强调这些模型处理内部隐藏状态而非将推理序列化为文本，同时质疑贝叶斯决策启发式方法在这一转型中的作用。 这种转变通过减少与自回归文本生成相关的延迟和计算成本，解决了大语言模型推理中的关键瓶颈。它从根本上改变了我们处理模型可解释性的方式，从阅读“内心独白”转向审计结构化计划和经过验证的输出。 像 Coconut 这样的潜在推理框架允许连续隐藏状态处理，从而实现基于文本的思维链无法有效支持的全局搜索能力。HRM 等模型将较慢的规划与较快的递归执行分离，而 RecursiveMAS 则在智能体之间传递潜在嵌入向量而非长文本消息。

reddit · r/MachineLearning · /u/meowsterpieces · 7月13日 17:50

**背景**: 思维链（CoT）提示鼓励大型语言模型在生成最终答案之前以文本形式生成中间推理步骤。虽然这种方法很有用，但它迫使将复杂的计算序列化标记，这会增加上下文窗口使用量并提高推理成本。最近的研究探索了潜在空间推理，模型在连续向量空间中执行计算，直到最后输出阶段才生成可读文本。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.linkedin.com/pulse/unlocking-smarter-ai-my-take-coconut-framework-latent-ragunathan-o43me">Unlocking Smarter AI : My Take on the “ Coconut ” Framework for...</a></li>
<li><a href="https://github.com/sapientinc/HRM">GitHub - sapientinc/HRM: Hierarchical Reasoning Model Official Release · GitHub</a></li>
<li><a href="https://recursivemas.github.io/">RecursiveMAS</a></li>

</ul>
</details>

**标签**: `#LLM Reasoning`, `#Chain of Thought`, `#Latent Space`, `#AI Architecture`, `#Model Scaling`

---