---
layout: default
title: "Horizon Summary: 2026-07-04 (ZH)"
date: 2026-07-04
lang: zh
---

> 从 68 条内容中筛选出 10 条重要资讯。

---

1. [Karpathy 发布 NanoChat：一套仅需 100 美元的开源大模型训练管道](#item-1) ⭐️ 8.0/10
2. [调查间谍软件的欧盟议员遭飞马软件入侵](#item-2) ⭐️ 8.0/10
3. [Wordgard：ProseMirror 创始人推出的全新浏览器端富文本编辑器](#item-3) ⭐️ 8.0/10
4. [Ubicloud 提倡使用严格内存过提交以保障 PostgreSQL 稳定性](#item-4) ⭐️ 8.0/10
5. [HAT-4D：单目视频直接生成 4D 交互场景](#item-5) ⭐️ 8.0/10
6. [Flock 摄像头无需车牌即可通过视觉指纹追踪车辆](#item-6) ⭐️ 8.0/10
7. [对比解码差分法仅凭 Logits 即可恢复微调数据](#item-7) ⭐️ 8.0/10
8. [谷歌 Gemini Omni Flash 登顶 Video Arena 排行榜](#item-8) ⭐️ 8.0/10
9. [华为发布搭载昇腾 950PR 的 Atlas 350，宣称性能达 H20 的 2.87 倍](#item-9) ⭐️ 8.0/10
10. [Katalyst 公司的 LINK 航天器发射，旨在营救 NASA 的 Swift 望远镜](#item-10) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Karpathy 发布 NanoChat：一套仅需 100 美元的开源大模型训练管道](https://github.com/karpathy/nanochat) ⭐️ 8.0/10

Andrej Karpathy 推出了 NanoChat，这是一套完整的端到端大语言模型训练管道，用户只需约 100 美元即可利用云端竞价实例构建功能齐全的聊天机器人。该项目将大型 AI 实验室使用的复杂基础设施压缩为大约 8,000 行可读的 Python 和 Rust 代码。 这一举措大幅降低了开发定制语言模型的门槛，为昂贵的专有 API（如 ChatGPT）提供了透明且具成本效益的替代方案。它使开发者和研究人员能够在无需巨大计算预算的情况下，实验全栈 AI 开发。 该管道支持使用 AI 代理进行自回归训练，并包含已部署的聊天用户界面，使其成为实用的工具而非仅仅是理论演示。它利用 Python 和 Rust 中的高效编码实践来优化性能，同时保持对个体开发者的可访问性。

github · karpathy · 7月3日 17:47

**背景**: Large Language Models (LLMs) typically require substantial financial resources for training and inference, often costing thousands of dollars in compute time. Most open-source alternatives focus on inference-only solutions or require specialized hardware, leaving a gap for affordable, full-training pipelines. Projects like NanoChat aim to democratize access by simplifying the entire process from raw text to a deployed application.

<details><summary>参考链接</summary>
<ul>
<li><a href="https://byteiota.com/nanochat-karpathy-llm-100-dollars/">nanochat Tutorial: Train Your Own LLM for $100 (2026) | byteiota</a></li>
<li><a href="https://emelia.io/hub/nanochat-karpathy">Nanochat : Build Your Own ChatGPT for $100</a></li>

</ul>
</details>

**标签**: `#AI`, `#Open Source`, `#LLM`, `#Karpathy`, `#NLP`

---

<a id="item-2"></a>
## [调查间谍软件的欧盟议员遭飞马软件入侵](https://citizenlab.ca/research/member-of-committee-investigating-spyware-hacked-with-pegasus/) ⭐️ 8.0/10

公民实验室确认，欧洲议会“飞马”委员会前成员斯特利奥斯·库洛格卢在 2022 年底至 2023 年初多次成功感染飞马间谍软件。法医分析表明，攻击者拥有在多个欧洲国家进行操作的授权。 这一事件突显了负责调查监控滥用行为的官员所面临的严重讽刺和风险，引发了对议会调查完整性的担忧。它还强调了间谍软件在欧盟成员国中扩散的地缘政治影响。 库洛格卢的设备分别在 2022 年 10 月 21 日左右以及 2023 年 3 月 6 日和 7 日被感染，可能导致个人医疗数据和机密政府文件泄露。与针对流亡记者的活动重叠表明存在复杂的跨国监控能力。

hackernews · ledoge · 7月3日 20:38 · [社区讨论](https://news.ycombinator.com/item?id=48779683)

**背景**: Pegasus is a sophisticated spyware developed by the Israeli firm NSO Group, marketed for counter-terrorism but frequently used to target journalists, activists, and politicians. The European Parliament established the PEGA Committee specifically to investigate the misuse of such surveillance tools by member states. Previous scandals in Greece and Italy have already revealed widespread abuse of Pegasus by government officials.

<details><summary>参考链接</summary>
<ul>
<li><a href="https://cybernews.com/security/eu-parliament-lawmaker-surveillance-hacked-pegasus/">EU parliament lawmaker hacked with Pegasus spyware | Cybernews</a></li>
<li><a href="https://thehackernews.com/2026/07/european-parliament-member.html">European Parliament Member Investigating Spyware Was Hacked ...</a></li>
<li><a href="https://www.politico.eu/article/probe-finds-former-mep-investigating-pegasus-was-himself-hacked-with-pegasus/">Probe finds former MEP investigating Pegasus was hacked with ...</a></li>

</ul>
</details>

**社区讨论**: 评论者对调查间谍软件的议员本人遭到入侵表示愤慨，并质疑欧盟议会缺乏设备分离政策。一些用户将该事件与希腊和意大利等欧盟成员国的更广泛滥用模式联系起来，指出以色列公司已开始切断与这些客户的联系。

**标签**: `#Cybersecurity`, `#Spyware`, `#European Parliament`, `#Pegasus`, `#Investigative Journalism`

---

<a id="item-3"></a>
## [Wordgard：ProseMirror 创始人推出的全新浏览器端富文本编辑器](https://wordgard.net/) ⭐️ 8.0/10

Marijn Haverbeke 发布了 Wordgard，这是一个利用浏览器 DOM 并借鉴 CodeMirror v6 架构的开源浏览器端富文本编辑器。该新库旨在提供轻量、可定制且符合标准的编辑体验，与其之前的作品有所区别。 Wordgard 旨在轻量且符合标准，直接使用浏览器 DOM 而非仅依赖复杂的虚拟 DOM 抽象。然而，与拥有既定迁移模式的 ProseMirror 不同，Wordgard 目前缺乏针对现有 ProseMirror 实现的直接升级路径。

hackernews · indy · 7月3日 08:50 · [社区讨论](https://news.ycombinator.com/item?id=48772573)

**背景**: ProseMirror is a highly regarded, modular rich-text editor framework used by major platforms like The New York Times and Obsidian. It provides a robust state management system and schema definition capabilities but can be complex to implement. CodeMirror is another famous library by the same author, primarily focused on code editing, which recently underwent a major architectural redesign in version 6.

<details><summary>参考链接</summary>
<ul>
<li><a href="https://wordgard.net/">Wordgard</a></li>
<li><a href="https://marijnhaverbeke.nl/blog/wordgard-0.1.html">Wordgard Release 0.1 - marijnhaverbeke.nl</a></li>
<li><a href="https://thenewhandset.com/tech-explainers/wordgard-in-browser-rich-text-editor-from-the-creator-of-prosemirror/">Wordgard : In-browser Rich - text Editor From The... - The New Handset</a></li>

</ul>
</details>

**社区讨论**: 社区对新编辑器背后的原因感到好奇，指出虽然它与 ProseMirror 共享概念，但现有用户没有轻松的升级路径。开发人员对自己定制的解决方案得到验证表示赞赏，但也表达了对静态类型支持缺失的担忧，这与 ProseMirror 相比是一个劣势。

**标签**: `#rich-text-editor`, `#javascript`, `#prosemirror`, `#web-development`, `#tools`

---

<a id="item-4"></a>
## [Ubicloud 提倡使用严格内存过提交以保障 PostgreSQL 稳定性](https://www.ubicloud.com/blog/postgresql-and-the-oom-killer-why-we-use-strict-memory-overcommit) ⭐️ 8.0/10

Ubicloud 发表了一篇分析文章，解释了为何为 PostgreSQL 强制执行严格内存过提交（vm.overcommit_memory=2），以防止 Linux OOM killer 意外终止数据库进程。 这种方法通过将潜在的全面停机降级为孤立的交易错误，降低了灾难性系统级故障的风险，为托管数据库提供商提供了关键的操作策略。 该配置防止内核允许超出物理限制的内存分配，确保内存耗尽得到优雅处理，而不是触发 OOM killer 的激进进程终止。

hackernews · furkansahin · 7月3日 13:00 · [社区讨论](https://news.ycombinator.com/item?id=48774509)

**背景**: Linux 支持三种内存过提交模式：启发式（模式 0）、始终过提交（模式 1）和严格会计（模式 2）。在严格模式下，如果虚拟内存超过物理 RAM 和交换空间之和，内核将拒绝授予内存，从而避免实际内存不足时 OOM killer 必须随机选择进程进行终止的情况。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.ubicloud.com/blog/postgresql-and-the-oom-killer-why-we-use-strict-memory-overcommit">PostgreSQL and the OOM Killer: Why We Use Strict Memory ...</a></li>
<li><a href="https://oneuptime.com/blog/post/2026-03-02-optimize-memory-vm-swappiness-overcommit-ubuntu/view">How to Optimize Memory (vm.swappiness, overcommit ) on Ubuntu</a></li>

</ul>
</details>

**社区讨论**: 社区指出默认的 Linux 内存设置通常在压力下导致不稳定，而一些用户警告说，严格模式需要仔细测试，以避免阻止 fork 或导致应用程序级别的错误。

**标签**: `#PostgreSQL`, `#Linux`, `#System Administration`, `#Memory Management`, `#DevOps`

---

<a id="item-5"></a>
## [HAT-4D：单目视频直接生成 4D 交互场景](https://mp.weixin.qq.com/s?__biz=MzIzNjc1NzUzMw==&mid=2247901356&idx=3&sn=54ee94026f76691a380cd3ea214e0def) ⭐️ 8.0/10

上海交通大学的研究人员提出了 HAT-4D，这是一种直接从单目视频生成 4D 交互场景的方法。这一突破消除了对昂贵动捕棚和复杂多视图设置的需求。 这项技术显著降低了创建高保真 4D 内容的门槛，有利于游戏、虚拟制作和机器人仿真等行业。它是迈向易于访问的“真实到模拟”工作流的重要一步。 该方法允许从单个摄像头画面中重建动态场景（如切香蕉），而无需标注的训练数据或特定类别的模板。它专注于生成物理上合理的交互环境。

rss · 量子位 · 7月3日 03:43

**背景**: 传统的 4D 重建通常依赖多摄像头或专门的动捕服来准确捕捉深度和时间变化。单目 4D 重建具有挑战性，因为它需要从单一二维视角随时间推断三维结构和运动。生成式 AI 和神经渲染的最新进展正在通过合成缺失的几何信息来帮助弥合这一差距。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2607.00157">Progressive Pose-Guided 4 D Animal Reconstruction from Monocular...</a></li>
<li><a href="https://openaccess.thecvf.com/content/CVPR2026/papers/Wang_Complet4R_Geometric_Complete_4D_Reconstruction_CVPR_2026_paper.pdf">Complet4R: Geometric Complete 4 D Reconstruction</a></li>

</ul>
</details>

**标签**: `#Computer Vision`, `#4D Reconstruction`, `#AI Research`, `#Motion Capture`, `#Shanghai Jiao Tong University`

---

<a id="item-6"></a>
## [Flock 摄像头无需车牌即可通过视觉指纹追踪车辆](https://www.schneier.com/blog/archives/2026/07/flock-cameras-can-surveil-cars-without-license-plates.html) ⭐️ 8.0/10

布鲁斯·施奈尔指出，Flock Safety 的“车辆指纹”技术允许执法部门利用贴纸、车顶架和保险杠贴纸等视觉特征来识别和追踪车辆，即使车牌被遮挡或缺失。这种能力使警官能够在初始信息有限的情况下构建案件并进行多地理区域搜索。 这一发展引发了深刻的隐私担忧，因为它将监控能力扩展到了传统的车牌识别之外，无论个人如何试图隐藏身份，都可能导致对其进行的广泛追踪。这标志着公共空间中更具侵入性的计算机视觉应用的转变，影响了公民自由和数据保护规范。 该技术利用人工智能分析非车牌视觉属性，如临时标签、独特的州标识符和物理改装，为每辆车创建独特的档案。Flock 将此宣传为帮助警方“在初始信息较少的情况下构建更强有力的案件”的工具，包括定位一起移动的车辆群体。

rss · Schneier on Security · 7月3日 11:15

**背景**: Flock Safety 是美国各地执法机构使用的主要自动车牌识别（ALPR）系统提供商。虽然 ALPR 传统上依赖于读取车牌字符，但计算机视觉和深度学习的最新进展使得基于外观的车辆重新识别成为可能。这包括识别特定型号、颜色以及车顶架或窗户贴纸等售后改装件，从而有效地创建用于追踪的视觉指纹。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Flock_Safety">Flock Safety - Wikipedia</a></li>
<li><a href="https://www.flocksafety.com/">Flock Safety</a></li>
<li><a href="https://www.mogazmasr.com/126831">Flock Safety cameras go far beyond plates, and that is the point...</a></li>

</ul>
</details>

**标签**: `#Privacy`, `#Surveillance`, `#Law Enforcement`, `#Computer Vision`, `#Security`

---

<a id="item-7"></a>
## [对比解码差分法仅凭 Logits 即可恢复微调数据](https://www.reddit.com/r/MachineLearning/comments/1umn2dk/contrastive_decoding_diffing_cdd_recovering/) ⭐️ 8.0/10

研究人员推出了对比解码差分法（CDD），这是一种灰盒方法，仅需访问 logits 即可从窄微调的大语言模型中逐字恢复微调数据，无需获取模型权重。该技术在恢复具体训练内容方面显著优于之前的白盒方法如激活差异透镜（ADL）。 这一进展对大语言模型的隐私和知识产权产生了重大影响，因为它表明即使无法直接访问权重，微调痕迹仍可被恢复。这揭示了当前模型部署实践中关于数据泄露的一个关键脆弱点。 CDD 在四个模型系列的 19/20 个测试用例中实现了 4+/5 的逐字恢复得分，而尽管需要完全访问权重，ADL 的得分从未超过 3/5。该方法还意外揭示了一个嵌入在合成训练数据中的持久虚构人物“Elena Rodriguez 博士”。

reddit · r/MachineLearning · /u/CebulkaZapiekana · 7月3日 19:01

**背景**: 模型差分涉及比较基础模型与微调后的版本，以识别由训练数据引起的变化。以前的方法如激活差异透镜（ADL）需要白盒访问内部激活状态，限制了其实用性。对比解码通过优化输出分布来突出模型间的差异，使 CDD 成为可解释性研究中一种更易访问但更强大的替代方案。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2606.02184">The Ghost Couple: Correlated LLM Name Priors and Their Haunting of the Web and Academic Publishing</a></li>
<li><a href="https://learnmechinterp.com/topics/finetuning-traces/">Finetuning Traces in Activations | Learn Mechanistic Interpretability</a></li>

</ul>
</details>

**标签**: `#LLM Privacy`, `#Model Interpretability`, `#Fine-tuning`, `#Machine Learning Research`

---

<a id="item-8"></a>
## [谷歌 Gemini Omni Flash 登顶 Video Arena 排行榜](https://x.com/Designarena/status/2072759122366509130) ⭐️ 8.0/10

谷歌 DeepMind 的公测视频生成模型 Gemini Omni Flash 以 1404 分的成绩登顶 Video Arena 排行榜。它超越了此前以 1303 分位居第一的字节跳动 Seedance 2.0 Mini，领先优势达到 101 分。 这一变化标志着人工智能视频生成领域竞争格局的重大转变，结束了字节跳动长期占据榜首的局面。它表明谷歌的最新模型在盲测中优于竞争对手，反映了视频质量和生成能力的真实提升。 该排名由 Video Arena 决定，该榜单依靠用户盲测投票来确保对生成质量的客观评估。与 Veo 系列时期相比，谷歌的视频模型排名也提升了七个位置，表明其视频生成技术取得了显著进步。

telegram · zaihuapd · 7月3日 05:51

**背景**: Video Arena is a benchmarking platform that ranks AI video models based on human preference votes in blind tests, where users choose between videos without knowing the provider. This methodology aims to filter out brand bias and highlight actual performance metrics like character consistency and motion realism. Previously, Seedance models had consistently held the leading positions on this leaderboard.

<details><summary>参考链接</summary>
<ul>
<li><a href="https://artificialanalysis.ai/video/arena">Video Arena - Top AI Video Models</a></li>
<li><a href="https://llm-stats.com/leaderboards/best-ai-for-video-generation">Best AI for Video Generation in 2026 — Ranked by Blind Human Votes</a></li>

</ul>
</details>

**标签**: `#AI Video Generation`, `#Google DeepMind`, `#Gemini`, `#Model Benchmarking`, `#ByteDance`

---

<a id="item-9"></a>
## [华为发布搭载昇腾 950PR 的 Atlas 350，宣称性能达 H20 的 2.87 倍](https://t.me/zaihuapd/42329) ⭐️ 8.0/10

在华为中国合作伙伴大会 2026 上，华为正式发布了搭载全新昇腾 950PR 处理器的 AI 加速卡 Atlas 350。该产品支持 FP4 低精度推理，配备 112 GB HBM 容量，其单卡算力据称达到英伟达 H20 的 2.87 倍。 这一发布标志着中国国产 AI 硬件供应链的重要进展，为受限制的英伟达芯片提供了有力的竞争替代方案。通过支持 FP4 推理，华为旨在降低大规模 AI 模型部署的延迟和投资成本。 Atlas 350 是目前国内唯一支持 FP4 低精度推理的加速卡，能够在单卡上高效处理 70B 参数量的模型。然而，目前尚无独立基准测试来验证其相比 H20 提升 2.87 倍的性能说法。

telegram · zaihuapd · 7月3日 08:35

**背景**: FP4（4 位浮点数）是 AI 加速器中使用的一种低精度算术格式，用于在不显著损害模型精度的情况下加快推理速度并降低内存带宽需求。NVIDIA H20 是一款专为符合美国出口管制而设计的中国特供版 GPU，侧重于高内存带宽而非原始峰值算力。华为的昇腾系列一直在不断发展，以缩小与全球领导者在训练和推理能力方面的差距。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.tomshardware.com/pc-components/gpus/huawei-unveils-new-atlas-350-ai-accelerator-with-1-56-pflops-of-fp4-compute-and-up-to-112gb-of-hbm-claims-2-8x-more-performance-than-nvidias-h20">Huawei unveils new Atlas 350 AI accelerator with 1.56 PFLOPS of FP4 compute and up to 112GB of HBM — claims 2.8x more performance than Nvidia's H20 | Tom's Hardware</a></li>
<li><a href="https://www.huaweicentral.com/huawei-atlas-350-ai-card-debuts-outshining-nvidia-h20-chip/">Huawei Atlas 350 AI card debuts, outshining Nvidia H20 chip - Huawei Central</a></li>
<li><a href="https://techjacksolutions.com/ai-brief/huaweis-atlas-350-claims-28287x-ai-performance-over-nvidia-h/">Huawei's Atlas 350 Claims 2.8–2.87x AI Performance Over Nvidia H20, No Independent Benchmark Exists</a></li>

</ul>
</details>

**标签**: `#AI Hardware`, `#Huawei`, `#Accelerators`, `#Semiconductors`, `#NVIDIA Competition`

---

<a id="item-10"></a>
## [Katalyst 公司的 LINK 航天器发射，旨在营救 NASA 的 Swift 望远镜](https://apnews.com/article/swift-nasa-satellite-rescue-katalyst-a7ddd740ca099587c58865f583c7245a) ⭐️ 8.0/10

2026 年 7 月 2 日，Katalyst Space Technologies 公司发射了 LINK 服务航天器，旨在捕获并提升 NASA 老旧的尼尔·格赫尔斯·斯威夫特天文台的轨道。该任务通过将望远镜轨道抬升约 240 公里，以防止其因轨道衰减而重新进入地球大气层。 这是具有历史意义的一刻，因为这是私人机构首次尝试为美国政府卫星提供服务，证明了商业在轨维护的可行性。成功延长 Swift 的使用寿命将保留探测伽马射线暴的关键能力，这对于理解黑洞形成等宇宙现象至关重要。 LINK 航天器利用机械臂自主捕获翻滚中的 Swift 天文台，随后经过数月的过程将其轨道从约 224 英里提升至 373 英里。如果成功，Swift 最早可能在 9 月恢复科学观测，从而将其运营寿命大大延长至原计划结束时间之后。

telegram · zaihuapd · 7月3日 15:43

**背景**: 尼尔·格赫尔斯·斯威夫特天文台于 2004 年发射，已在太空中监测伽马射线暴超过二十年，这些是宇宙中最剧烈的爆炸事件。由于低地球轨道的大气阻力，Swift 的高度逐渐降低，威胁到可能导致仪器被毁的非受控再入。这次任务突显了日益发展的卫星服务行业，私营公司正在开发用于修理、加注燃料或重新定位老化卫星的技术，以减轻空间碎片问题并最大化科学回报。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Swift_Rescue_Mission">Swift rescue mission - Wikipedia</a></li>
<li><a href="https://science.nasa.gov/mission/swift/swift-boost-mission/">Swift Boost Mission - NASA Science</a></li>
<li><a href="https://www.nasa.gov/image-article/link-spacecraft-set-for-mission-to-boost-nasas-swift-observatory/">LINK Spacecraft Set for Mission to Boost NASA’s Swift ...</a></li>

</ul>
</details>

**标签**: `#Space Exploration`, `#Satellite Servicing`, `#Orbital Mechanics`, `#NASA`, `#Private Aerospace`

---