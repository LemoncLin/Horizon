---
layout: default
title: "Horizon Summary: 2026-07-05 (ZH)"
date: 2026-07-05
lang: zh
---

> 从 47 条内容中筛选出 4 条重要资讯。

---

1. [欧盟理事会加速推进“聊天监控”立法](#item-1) ⭐️ 9.0/10
2. [能力门控：通过内部置信度信号控制工具使用](#item-2) ⭐️ 8.0/10
3. [F-Droid 指控 Google ADV 为恶意软件，引发隐私担忧](#item-3) ⭐️ 8.0/10
4. [复旦大学让学生出题考 AI，探索教育新模式](#item-4) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [欧盟理事会加速推进“聊天监控”立法](https://www.heise.de/en/news/Chat-Control-1-0-EU-Council-forces-messenger-scans-via-fast-track-11353659.html) ⭐️ 9.0/10

欧盟理事会已加速推进“聊天监控 1.0”的立法进程，强制要求对非端到端加密的消息进行扫描以打击儿童性虐待。这一举措正式确立了对主要消息提供商的大规模扫描要求，引发了关于隐私和监控影响的激烈争论。 这代表了一项重大的政策转变，显著影响了欧盟内的数字隐私权和加密标准。它为政府授权的监控树立了先例，可能破坏私人通信的安全模型，并影响整个欧盟范围内数以百万计的用户。 当前的提案专门针对非端到端加密的服务，这与会影响 Signal 等端到端加密应用的更具争议的“聊天监控 2.0”有所区别。由于该快速通道程序被认为绕过了彻底的民主审查，因此受到了隐私倡导者的批评。

hackernews · stavros · 7月5日 11:44 · [社区讨论](https://news.ycombinator.com/item?id=48793393)

**背景**: End-to-end encryption (E2EE) is a method where only the sender and intended recipient can read messages, ensuring that platforms and third parties cannot access the content. The EU's proposed Regulation to Prevent and Combat Child Sexual Abuse, commonly known as Chat Control, aims to require service providers to scan for illegal content, raising concerns about mandatory backdoors or client-side scanning that could weaken overall security.

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Chat_Control">Chat Control - Wikipedia</a></li>
<li><a href="https://fightchatcontrol.eu/">Fight Chat Control - Protect Digital Privacy in the EU</a></li>
<li><a href="https://www.europarl.europa.eu/doceo/document/E-10-2025-003250_EN.html">Parliamentary question | Proposed Chat Control law presents new blow for privacy | E-003250/2025 | European Parliament</a></li>

</ul>
</details>

**社区讨论**: 社区成员区分了当前针对非端到端加密服务的提案与人们更担心的扩展到端到端加密应用的计划，指出后者尚未被讨论。虽然一些人表达了对欧盟机构的不满并呼吁去中心化替代方案，但另一些人则强调需要更深入地调查复杂的立法流程。

**标签**: `#EU Regulation`, `#Privacy`, `#Encryption`, `#Policy`, `#Cybersecurity`

---

<a id="item-2"></a>
## [能力门控：通过内部置信度信号控制工具使用](https://www.reddit.com/r/MachineLearning/comments/1unw5un/competence_gate_gating_tooluse_on_a_small_models/) ⭐️ 8.0/10

作者为 Qwen3.5-4B 引入了一个仅 10MB 的轻量级 LoRA 适配器，该适配器利用内部激活信号来决定何时使用工具，而不是依赖模型口头表达的置信度。这种方法通过提高错误检测能力并将敏感查询路由到本地检索，显著减少了隐私泄露风险。 这解决了一个关键局限，即小型语言模型在口头表达上往往高估自己的信心，尽管实际上并不确定。通过利用内部信号，该解决方案提高了本地部署的可靠性和隐私保护，使得在处理敏感数据时使用大语言模型更加安全。 该适配器在错误检测方面实现了 0.46 的 d'提升，并将发送给公共搜索的私人问题率从 22%降低到 10%。它使用 MLX 在 Apple Silicon 上高效运行，并为 llama.cpp 提供了 GGUF 构建版本，确保检索答案的可追溯引用。

reddit · r/MachineLearning · /u/Synthium- · 7月5日 07:49

**背景**: 大型语言模型（LLM）通常难以通过文本准确表达其不确定性，这种现象被称为置信度校准问题。LoRA（低秩自适应）是一种允许通过仅更新少量参数来高效微调大型模型的技术，从而降低了计算成本。内部激活信号指的是模型内部隐藏的数学表示，其中可能包含比最终文本输出更准确的确定性信息。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.databricks.com/blog/efficient-fine-tuning-lora-guide-llms">Efficient Fine-Tuning with LoRA: A Guide to Optimal Parameter Selection for Large Language Models</a></li>
<li><a href="https://github.com/ml-explore/mlx">GitHub - ml-explore/mlx: MLX: An array framework for Apple silicon · GitHub</a></li>

</ul>
</details>

**标签**: `#LLM Reliability`, `#Small Language Models`, `#Internal Activations`, `#Tool Use`, `#Open Source AI`

---

<a id="item-3"></a>
## [F-Droid 指控 Google ADV 为恶意软件，引发隐私担忧](https://f-droid.org/2026/07/01/adv-malware.html) ⭐️ 8.0/10

F-Droid 正式将 Google 的 Android 开发者验证（ADV）进程定性为恶意软件，指出其可在约 40 亿台预装设备上阻止未授权应用的运行。这一认定紧随 ADV 于 9 月 30 日起在多个亚洲国家激活的计划，全球推广定于 2027 年及以后。 这场争议凸显了 Google 对 Android 应用分发集中控制与开源社区对用户自由及侧载承诺之间的重大冲突。它引发了包括电子前哨基金会（EFF）和自由软件基金会（FSF）在内的主要数字权利组织的强烈反对，预示着 Google 未来 Android 政策可能面临监管和伦理挑战。 F-Droid 认为，Google 在其开发者服务条款中刻意避免定义“恶意软件”，从而可以随意封禁广告拦截器等软件。ADV 功能通过 Play Protect 以 root 权限运行，用户无法移除，这引发了对企业不受限制地掌控设备功能的担忧。

telegram · zaihuapd · 7月5日 00:41

**背景**: Android 开发者验证（ADV）是 Google 推出的一项系统进程，旨在通过在设备上运行应用程序之前验证其完整性来增强安全性。虽然其初衷是保护用户免受恶意代码侵害，但批评者认为它建立了一个围墙花园，限制了合法的第三方应用安装，并破坏了开源倡导者所重视的透明度。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://f-droid.org/2026/07/01/adv-malware.html">What We Talk About When We Talk About Malware - F-Droid</a></li>
<li><a href="https://android-developers.googleblog.com/2026/06/android-developer-verification.html">Android Developers Blog: Android developer verification ...</a></li>

</ul>
</details>

**社区讨论**: 社区讨论反映了对用户自主权被侵蚀以及缺乏对禁止软件明确定义的深切担忧。许多用户和组织认为此举是 Google 的过度扩张，优先考虑企业控制而非个人选择和安全透明度。

**标签**: `#Android`, `#Privacy`, `#Google`, `#Open Source`, `#Policy`

---

<a id="item-4"></a>
## [复旦大学让学生出题考 AI，探索教育新模式](https://mp.weixin.qq.com/s/d53O-6mVFZqMa_Sti1yEPw) ⭐️ 8.0/10

四名复旦大学学生设计出让三个 AI 模型零分的考题，凸显了评估方式的转变。《数据挖掘技术》课程由学生出题测试 AI 能力，班级平均分为 85.7 分。 这一举措反映了从死记硬背到评估人类判断力和 AI 交互技能的重大教学转变。它预示着未来的教育将侧重于指导和分析 AI，而非仅仅手动执行任务。 考试中，51 名学生每人设计了 10 道有唯一答案的计算题来测试三个 AI 模型。虽然 50 名学生成功难倒了至少一个模型，但只有四人让所有模型都得零分，其中 Claude 模型表现最为稳健。

telegram · zaihuapd · 7月5日 08:40

**背景**: 传统的学术评估通常依赖记忆和算法执行的测试，而这些正日益被大型语言模型自动化。随着 AI 能力的增强，教育者正在重新思考如何衡量学生能力，强调批判性思维和提示工程，而非单纯的问题解决。

**标签**: `#AI Education`, `#Pedagogy`, `#LLM Evaluation`, `#Higher Education`, `#Human-AI Interaction`

---