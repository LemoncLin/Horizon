---
layout: default
title: "Horizon Summary: 2026-07-25 (ZH)"
date: 2026-07-25
lang: zh
---

> 从 51 条内容中筛选出 6 条重要资讯。

---

1. [vLLM v0.26.0 发布，新增 DeepSeek-V4 与 Inkling 支持](#item-1) ⭐️ 9.0/10
2. [Anthropic 发布 Claude Opus 5，以半价媲美 Fable 5 的前沿智能](#item-2) ⭐️ 9.0/10
3. [Android 可能限制设备端 ADB 访问权限](#item-3) ⭐️ 8.0/10
4. [开放权重 AI 模型正演变为类似 Kubernetes 的标准基础设施](#item-4) ⭐️ 8.0/10
5. [Anthropic 的 Opus 5 展现出卓越的提示注入抵抗力](#item-5) ⭐️ 8.0/10
6. [开发者发布 iOS 27 usbliter8 越狱方案，仅支持 iPhone 11 Pro](#item-6) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [vLLM v0.26.0 发布，新增 DeepSeek-V4 与 Inkling 支持](https://github.com/vllm-project/vllm/releases/tag/v0.26.0) ⭐️ 9.0/10

vLLM v0.26.0 引入了广泛的性能优化，包括针对 DeepSeek-V4 的专用内核以及对全新 Inkling 模型家族的全面支持。这一重大版本还增强了在 NVIDIA Hopper、AMD 和 XPU 硬件上的量化、注意力机制及推测解码能力。 此次更新显著降低了 DeepSeek-V4 等前沿模型的推理延迟并提高了吞吐量，这对高性能 AI 应用至关重要。通过扩展硬件兼容性并添加对新架构的原生支持，它使开发人员能够更高效地部署多样化的模型。 关键技术改进包括为 DeepSeek-V4 设计的专用路由内核，该内核减少了端到端输出令牌的时间，以及用于 Inkling 家族的基于 MTP 的推测解码。该版本还引入了按 KV 缓存组选择的灵活注意力后端，以及具有分层二级存储功能的成熟 KV 卸载机制。

github · khluu · 7月25日 10:38

**背景**: vLLM 是一个广泛用于快速大语言模型推理的开源库，以其 PagedAttention 机制和高吞吐量而闻名。推测解码是一种利用较小的草稿模型一次性预测多个令牌的技术，从而加快生成速度。DeepSeek-V4 是一个利用混合专家（MoE）架构的大语言模型，而 Inkling 是一个多模态通用模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.vllm.ai/en/latest/features/speculative_decoding/mtp/">MTP (Multi-Token Prediction) - vLLM</a></li>
<li><a href="https://thinkingmachines.ai/news/introducing-inkling/">Inkling: Our Open-Weights Model - Thinking Machines Lab</a></li>

</ul>
</details>

**标签**: `#vLLM`, `#LLM Inference`, `#DeepSeek`, `#CUDA`, `#Model Optimization`

---

<a id="item-2"></a>
## [Anthropic 发布 Claude Opus 5，以半价媲美 Fable 5 的前沿智能](https://simonwillison.net/2026/Jul/24/introducing-claude-opus-5/#atom-everything) ⭐️ 9.0/10

Anthropic 发布了新的 Claude Opus 5 大语言模型，该模型在 Artificial Analysis 排行榜上名列前茅，其智能水平可与 Claude Fable 5 相媲美，但价格仅为后者的一半。该模型具备更强的主动性能力，例如能够自主生成复杂任务的代码，同时保持了与上一代 Opus 4.8 相同的价格体系。 这一发布通过提供更具可及性的价格来实现前沿级别的 AI 推理能力，显著降低了使用门槛。它加剧了主要 AI 实验室之间的竞争，并为开发者在处理复杂编码和分析任务时提供了一个高性能且具成本效益的替代方案。 Opus 5 的定价与 Opus 4.8 完全相同，但其性能接近更昂贵的 Claude Fable 5。值得注意的是，它在没有专门接受利用技术训练的情况下，提升了漏洞检测能力，旨在平衡能力与安全顾虑。

rss · Simon Willison · 7月24日 23:48

**背景**: Claude Opus 是 Anthropic 专为复杂推理和高价值任务设计的旗舰模型系列，而 Claude Fable 则代表其最新的前沿层级。Artificial Analysis 排行榜是一个独立的基准测试平台，用于比较行业内各种大型语言模型在智能、速度和成本效率方面的表现。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://9to5mac.com/2026/07/24/anthropic-upgrades-claude-with-new-opus-5-model-details-here/">Anthropic upgrades Claude with new Opus 5 model, details here - 9to5Mac</a></li>
<li><a href="https://artificialanalysis.ai/articles/opus-5">Opus 5 : Fable 5 level intelligence at a lower cost per task</a></li>
<li><a href="https://platform.claude.com/docs/en/about-claude/models/overview">Models overview - Claude Platform Docs</a></li>

</ul>
</details>

**标签**: `#AI Models`, `#Anthropic`, `#LLM Releases`, `#Tech News`

---

<a id="item-3"></a>
## [Android 可能限制设备端 ADB 访问权限](https://kitsumed.github.io/blog/posts/android-may-soon-restrict-on-device-adb/) ⭐️ 8.0/10

Android 正在考虑实施对设备端 ADB 访问的限制，这一举措在开发者社区中引发了关于安全性与用户自主权之间平衡的激烈讨论。这项潜在的变更旨在关闭特定的攻击向量，但也引发了人们对限制高级用户能力的担忧。 这一转变意义重大，因为它通过可能限制用于调试和自动化的核心开发工具，改变了 Android 的安全模型。它影响了依赖 ADB 进行高级设备管理的开发者和高级用户，标志着移动平台上对个人计算任务控制趋于收紧的趋势。 拟议的变更包括限制对某些接口或 IP 地址的访问，尽管有人认为这些措施可能无法解决大多数用户的现实攻击向量。批评者指出，启用此类功能通常需要先激活开发者选项，这表明对于普通用户而言，风险可能被高估了。

hackernews · shscs911 · 7月25日 06:57 · [社区讨论](https://news.ycombinator.com/item?id=49045159)

**背景**: ADB（Android 调试桥）是一个多功能的命令行工具，允许与 Android 设备进行通信，从而实现应用安装、调试和系统配置等任务。Android 中的开发者选项提供了对高级设置的访问权限，包括 USB 调试和无线 ADB，这些对开发人员至关重要，但高级用户也可以使用。最近的趋势显示，Google 正在收紧对侧载和开发者界面的安全控制，反映出整个行业从开放访问转向更注重用户保护。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.androidauthority.com/android-advanced-protection-mode-developer-options-3679725/">Android Advanced Protection may soon close one of its biggest ...</a></li>

</ul>
</details>

**社区讨论**: 社区情绪褒贬不一，一些用户支持安全改进，而另一些人则担心用户自主权的丧失以及 Android 相比 iOS 开放性的削弱。许多评论者表示担忧，认为 Google 正将用户逼入依赖受控界面的境地，这可能导致对侧载和设备定制的限制进一步增加。

**标签**: `#Android`, `#Security`, `#ADB`, `#Developer Tools`, `#Mobile OS`

---

<a id="item-4"></a>
## [开放权重 AI 模型正演变为类似 Kubernetes 的标准基础设施](https://tobi.knaup.me/2026-07-25-open-weight-ai-is-having-its-kubernetes-moment/) ⭐️ 8.0/10

文章指出，开放权重的 AI 模型正在演变为一种标准化的基础设施层，其发展轨迹类似于云计算中 Kubernetes 的普及。这一转变凸显了预训练模型权重正成为跨行业部署 AI 应用的基础组件。 这一转变意义重大，因为它确立了开放权重模型作为关键公用事业的地位，有望稳定 AI 市场并减少对封闭专有系统的依赖。它通过提供推理成本的基准并允许通过可访问的模型架构进行更广泛的创新，从而影响了行业经济。 一个关键的技术细节是开放权重与开源模型之间的区别，前者发布数值参数但可能保持训练数据不透明。讨论还强调了这些模型对定价稳定的经济影响，指出它们为 AI 行业中波动的代币经济学提供了合理性检查。

hackernews · tknaup · 7月25日 14:49 · [社区讨论](https://news.ycombinator.com/item?id=49048034)

**背景**: 开放权重模型是指那些经过学习的参数（权重）被公开下载和使用的 AI 模型，尽管完整的训练过程或数据可能并未公开。Kubernetes 是一个用于自动化部署、扩展和管理容器化应用程序的开源系统，已成为云原生事实上的标准基础设施。这种比较表明，AI 模型正从独家产品转变为共享的基础设施资源。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://hellofuture.orange.com/en/a-typology-of-artificial-intelligence-models/">AI models explained: open source vs. open weight vs. closed</a></li>
<li><a href="https://www.cncf.io/announcements/2026/01/20/kubernetes-established-as-the-de-facto-operating-system-for-ai-as-production-use-hits-82-in-2025-cncf-annual-cloud-native-survey/">Kubernetes Established as the De Facto ‘Operating System’ for ...</a></li>

</ul>
</details>

**社区讨论**: 社区评论强调了由于模型权重本质上是数值数据，因此在技术上无法实现地理封锁，并讨论了开放模型如何稳定被称为“代币经济学”的价格波动。一些用户还指出了类似 Linux 的协作开发潜力，而另一些人则指出了在消费级硬件上运行大规模模型当前的局限性。

**标签**: `#Open-Source AI`, `#Infrastructure`, `#AI Economics`, `#Regulation`, `#Kubernetes`

---

<a id="item-5"></a>
## [Anthropic 的 Opus 5 展现出卓越的提示注入抵抗力](https://simonwillison.net/2026/Jul/25/boris-cherny/#atom-everything) ⭐️ 8.0/10

Boris Cherny 指出，Anthropic 新发布的 Opus 5 模型在抵抗提示注入攻击方面比之前的版本有显著提升。这一安全改进记录在模型的系统卡片中，根据评估和渗透测试结果，它是有史以来最难以被提示注入的模型。 这一主张得到了 Opus 5 系统卡片中详细记录的提示注入评估和内部渗透测试数据的支持。虽然 Opus 5 在编码基准测试和成本效益方面也处于领先地位，但其对抗性输入的增强鲁棒性是一个区别于一般性能指标的独立技术成就。

rss · Simon Willison · 7月25日 00:42

**背景**: 提示注入攻击利用了大型语言模型在区分系统指令和用户输入时的模糊性，使恶意文本能够覆盖预期的行为。这些攻击分为直接注入，即攻击者直接提供有效载荷，以及间接注入，即有效载荷隐藏在文档或网站等外部数据源中。随着 AI 代理变得更加自主，通过模型级别的改进来减轻这些风险对于安全集成到关键系统中至关重要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/news/claude-opus-5">Introducing Claude Opus 5 \ Anthropic</a></li>
<li><a href="https://cheatsheetseries.owasp.org/cheatsheets/LLM_Prompt_Injection_Prevention_Cheat_Sheet.html">LLM Prompt Injection Prevention - OWASP Cheat Sheet Series</a></li>

</ul>
</details>

**标签**: `#AI Safety`, `#Prompt Injection`, `#Anthropic`, `#LLM Security`, `#Model Evaluation`

---

<a id="item-6"></a>
## [开发者发布 iOS 27 usbliter8 越狱方案，仅支持 iPhone 11 Pro](https://github.com/34306/usbliter8-fun) ⭐️ 8.0/10

一名开发者发布了利用 usbliter8 漏洞为 iOS 27 越狱的完整方案，目前仅支持 iPhone 11 Pro。该方法需借助搭载 RP2350 芯片的 Raspberry Pi Pico 2，通过 SecureROM 漏洞绕过 AMFI 等安全功能。 该过程涉及将设备置于 PWN DFU 模式，并应用内核补丁以绕过 USB 限制和信任缓存检查。用户被警告该操作会抹除所有数据，并破坏 SEP、WiFi、基带、蓝牙及所有 Apple 服务。

telegram · zaihuapd · 7月25日 11:00

**背景**: usbliter8 利用了 Synopsys DWC2 USB 控制器中的硬件缺陷与苹果不可变 SecureROM 代码中的配置漏洞相结合的问题。此漏洞允许在 iOS 加载之前执行任意代码，从而有效破坏了配备 A12 和 A13 处理器的设备的启动链。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://appleinsider.com/articles/26/07/24/iphone-exploit-legal-fight-is-really-about-who-owns-security-research">iPhone exploit fight highlights who owns security research</a></li>
<li><a href="https://aiweekly.co/alerts/paradigm-shifts-usbliter8-exploit-breaks-apple-a12a13-securerom">Paradigm Shift's usbliter 8 Exploit Breaks Apple A12/A13... | AI Weekly</a></li>
<li><a href="https://www.itechpost.com/articles/236379/20260618/apple-devices-a12-a13-chips-face-unpatchable-exploit-says-researchers.htm">Apple Devices With A12, A13 Chips Face 'Unpatchable' Exploit , Says...</a></li>

</ul>
</details>

**标签**: `#iOS Jailbreak`, `#Security Exploit`, `#Reverse Engineering`, `#Mobile Security`

---