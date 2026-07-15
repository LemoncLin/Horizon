---
layout: default
title: "Horizon Summary: 2026-07-15 (ZH)"
date: 2026-07-15
lang: zh
---

> 从 63 条内容中筛选出 12 条重要资讯。

---

1. [Stripe 与 Advent 联合出价 530 亿美元收购 PayPal](#item-1) ⭐️ 9.0/10
2. [在无 GPU 的老旧 CPU 上运行 26B 大语言模型](#item-2) ⭐️ 8.0/10
3. [AI 语音欺诈为何能轻松突破现有安全防线](#item-3) ⭐️ 8.0/10
4. [Claude 的 web_fetch 工具漏洞绕过数据防泄露保护机制](#item-4) ⭐️ 8.0/10
5. [文远知行转型具身智能基础设施提供商](#item-5) ⭐️ 8.0/10
6. [Linux 7.2 内核为 io_uring 引入无锁多生产者单消费者队列](#item-6) ⭐️ 8.0/10
7. [大量过时 shim 文件仍受 UEFI 安全启动信任](#item-7) ⭐️ 8.0/10
8. [苏黎世联邦理工学院发布傅里叶像素显示摄像技术](#item-8) ⭐️ 8.0/10
9. [热力学计算机利用能量波动实现高效计算](#item-9) ⭐️ 8.0/10
10. [DeepSeek 完成超 500 亿元首轮融资并采用特殊架构保控制权](#item-10) ⭐️ 8.0/10
11. [马斯克宣布无条件开源 X 平台全部代码](#item-11) ⭐️ 8.0/10
12. [ASML 拟涨光刻设备价，台积电抵制部分中企接受](#item-12) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Stripe 与 Advent 联合出价 530 亿美元收购 PayPal](https://www.reuters.com/business/finance/stripe-advent-offer-buy-paypal-more-than-53-billion-sources-say-2026-07-15/) ⭐️ 9.0/10

据消息人士透露，支付巨头 Stripe 与私募股权公司 Advent 已联合提交了一份 530 亿美元的收购 PayPal 的要约。这笔拟议中的合并交易将把多家主要支付处理商整合到同一家公司旗下。 此次收购将彻底改变全球金融科技格局，打造一个在线支付领域的绝对主导者，从而可能削弱市场竞争并影响商户定价。由于存在重大的反垄断风险和潜在的市场垄断问题，监管机构预计将对这笔交易进行严格审查。 合并后的实体将掌控 PayPal、Venmo、Braintree 和 Xoom，导致非面对面（CNP）交易的赫芬达尔—赫希曼指数（HHI）极高。行业观察人士指出，监管机构可能会要求剥离 Venmo 和 Braintree 才能批准该交易。

hackernews · rvz · 7月15日 03:32 · [社区讨论](https://news.ycombinator.com/item?id=48915953)

**背景**: 赫芬达尔—赫希曼指数（HHI）是反垄断机构广泛采用的市场集中度衡量标准，用于评估并购对竞争的影响。在支付行业，较高的 HHI 分数通常会触发严格的监管审查，因为竞争减弱可能导致商户和消费者面临更高的费用。此外，Braintree 是 Stripe 的直接竞争对手，将其整合到同一平台下对反垄断审查尤为敏感。

**社区讨论**: 社区成员对竞争减少表示强烈担忧，害怕将 Braintree 与 Stripe 合并会消除价格制衡机制，从而导致交易费用上涨。许多人还担心更严格的政策执行和账户冻结风险，同时也有部分人承认需要监管机构介入以防止垄断行为。

**标签**: `#Fintech`, `#M&A`, `#Antitrust`, `#Payments`, `#HackerNews`

---

<a id="item-2"></a>
## [在无 GPU 的老旧 CPU 上运行 26B 大语言模型](https://www.neomindlabs.com/2026/06/08/running-gemma-4-26b-at-5-tokens-sec-on-a-13-year-old-xeon-with-no-gpu/) ⭐️ 8.0/10

一名开发者仅使用一台 13 年前的英特尔至强处理器，成功以每秒约 5 个词元的速度运行了 260 亿参数的 Gemma 4 模型，完全无需依赖独立显卡。 该演示证明现代大语言模型可以在老旧或低成本硬件上本地部署，显著降低了开发者的入门门槛，并减少了对昂贵云端推理服务的依赖。 该推理过程依赖于经过优化的开源工具（如 llama.cpp）和 GGUF 量化格式，这些技术将模型权重压缩至标准系统内存中，从而在纯 CPU 架构上维持可接受的生成速度。

hackernews · neomindryan · 7月15日 15:34 · [社区讨论](https://news.ycombinator.com/item?id=48922434)

**背景**: 大语言模型传统上需要强大的显卡来处理其巨大的计算负载，但模型量化和 CPU 优化推理引擎的最新进展已改变了这一格局。GGUF 等量化技术通过降低模型精度来节省内存，而 llama.cpp 等库则利用 CPU 专用指令加速矩阵运算，无需专用硬件即可实现高效推理。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/ikawrakow/ik_llama.cpp/">GitHub - ikawrakow/ik_llama.cpp: llama.cpp fork with ...</a></li>

</ul>
</details>

**社区讨论**: 社区成员分享了在类似硬件上获得更快速度的基准测试数据，讨论了本地推理与云端推理的长期成本效益，并强调了 ik_llama.cpp 等分支中持续改进的 CPU 性能优化工作。

**标签**: `#LLM Inference`, `#CPU Optimization`, `#Local AI`, `#Edge Computing`, `#Open Source`

---

<a id="item-3"></a>
## [AI 语音欺诈为何能轻松突破现有安全防线](https://smarterarticles.co.uk/the-three-second-theft-why-ai-voice-fraud-outruns-every-defence) ⭐️ 8.0/10

最新分析表明，AI 语音克隆技术如今能以极高的保真度复制人类语音，从而在几秒内轻松绕过传统的生物特征验证和客服反欺诈系统。这种快速演进使恶意攻击者无需大量音频样本或复杂配置即可实施高度逼真的社会工程学攻击。 这一进展从根本上动摇了基于语音的身份验证信任机制，直接影响依赖电话验证进行账户恢复和交易的金融机构、电信服务商及普通消费者。随着此类攻击规模化，企业必须紧急重构身份验证架构，以防止大规模资金损失和数据泄露。 核心漏洞在于“困惑副手”问题，即自动化系统或呼叫中心代理因无法区分合成语音与真实语音而被欺骗授予访问权限。有效的缓解措施要求从单一的生物特征检查转向持续认证模型，在整个交互过程中监控行为和环境风险信号。

hackernews · dxs · 7月15日 13:18 · [社区讨论](https://news.ycombinator.com/item?id=48920432)

**背景**: 语音克隆利用神经网络分析语音模式、音调和音色，仅需几秒的样本数据即可合成高度逼真的音频。传统安全措施通常依赖演示攻击检测技术来识别伪造尝试，但这些系统难以应对现代生成式人工智能，因为后者不再留下旧式伪造方法常见的数字伪影。因此，行业正转向零信任架构，采用持续认证而非依赖一次性登录验证。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.fraud.com/post/presentation-attack-detection">Presentation Attack Detection (PAD) explained - fraud.com</a></li>
<li><a href="https://ashishsrivastav.com/blog/continuous-authentication-beyond-one-time-login">Continuous Authentication : Moving Beyond One-Time Login</a></li>
<li><a href="https://www.meegle.com/en_us/topics/voice-cloning/voice-cloning-neural-networks">Voice Cloning Neural Networks</a></li>

</ul>
</details>

**社区讨论**: 评论者指出，该威胁本质上是经典社会工程学诈骗的技术升级，强调传统防御策略已失效。许多人强调需要进行架构变革，特别主张采用持续认证并削弱缺乏上下文感知能力的自动化系统。还有人探讨技术检测方法，但大家普遍担忧实时通话中的音频压缩是否会掩盖人工智能生成语音的特征。

**标签**: `#AI Security`, `#Voice Cloning`, `#Social Engineering`, `#Cybersecurity`, `#Threat Modeling`

---

<a id="item-4"></a>
## [Claude 的 web_fetch 工具漏洞绕过数据防泄露保护机制](https://simonwillison.net/2026/Jul/15/claude-web-fetch-exfiltration/#atom-everything) ⭐️ 8.0/10

研究员 Ayush Paul 在 Anthropic 的 Claude `web_fetch`工具中发现了一个漏洞，使攻击者能够绕过数据防泄露保护机制。通过利用该工具访问已抓取页面中嵌入链接的功能，攻击者成功提取了姓名和位置等私人用户记忆。 此漏洞凸显了将私人用户数据与无限制网络浏览功能结合的 LLM 智能体架构中的关键风险。它表明看似强大的沙箱隔离措施如何通过提示词注入和链式 URL 导航被绕过，对开发具备工具使用功能的 AI 助手的开发者具有重要影响。 该利用程序依赖于`web_fetch`工具访问其自身抓取内容中 URL 的权限，该权限随后已被 Anthropic 移除。攻击专门针对包含`Claude-User`用户代理字符串的请求以避免检测，并通过字母嵌套链接提取结构化个人数据。

rss · Simon Willison · 7月15日 14:21

**背景**: 现代 LLM 应用通常授予 AI 智能体访问网络搜索和页面抓取等外部工具的权限以提升实用性。为防止恶意行为者窃取敏感信息，开发者会实施严格的沙箱规则来限制智能体可访问的 URL。然而，当这些规则允许智能体动态跟踪已抓取内容中的链接时，就会为数据外泄攻击提供间接途径。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-fetch-tool?ref=webtechnology.news">Web fetch tool - Claude API Docs</a></li>
<li><a href="https://simonwillison.net/2025/sep/10/claude-web-fetch-tool/">Claude API: Web fetch tool | Simon Willison’s Weblog</a></li>

</ul>
</details>

**标签**: `#AI Security`, `#LLM Safety`, `#Prompt Injection`, `#Data Exfiltration`, `#Anthropic Claude`

---

<a id="item-5"></a>
## [文远知行转型具身智能基础设施提供商](https://mp.weixin.qq.com/s?__biz=MzIzNjc1NzUzMw==&mid=2247903875&idx=1&sn=7b4310fb18c59407f80da2adaff1aedc) ⭐️ 8.0/10

自动驾驶领军企业文远知行正将其核心技术栈转型为新兴具身智能领域的基础设施提供商。这一战略转型复刻了英伟达与宁德时代在各自生态中建立底层基础设施的成功路径。 通过提供标准化的感知、规划与仿真工具，文远知行旨在降低具身智能硬件厂商的研发门槛，加速机器人与智慧出行的商业化落地。这一转变表明，自动驾驶技术正成为物理智能部署的关键底层支撑。 该公司正依托其 L4 级自动驾驶架构，构建面向物理智能代理的端到端大模型能力与数据仿真平台。然而，将此类基础设施从轮式车辆扩展至形态各异的机器人仍面临显著的工程挑战。

rss · 量子位 · 7月15日 04:30

**背景**: 具身智能是指人工智能与机器人或智能汽车等物理实体深度融合的技术范式，使智能体能够在现实世界中感知、推理并执行动作。与传统软件系统不同，它高度依赖高保真仿真环境、海量真实数据处理以及统一的算法框架等底层基础设施。随着该领域进入规模化开发阶段，类似芯片与电池供应商在早期产业浪潮中的角色，专业化的基础设施服务商正逐渐成为推动行业标准化与商业化的关键力量。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://xueqiu.com/3797338236/350545858">物 理 AI —— 具 身 智 能 具 身 智 能 （ Embodied AI ...</a></li>
<li><a href="https://zhuanlan.zhihu.com/p/1997592971927913986">面向具身智能的AI Infra深度研究报告 - 知乎</a></li>

</ul>
</details>

**标签**: `#Embodied AI`, `#Robotics`, `#Autonomous Driving`, `#Industry Analysis`, `#AI Infrastructure`

---

<a id="item-6"></a>
## [Linux 7.2 内核为 io_uring 引入无锁多生产者单消费者队列](https://lwn.net/Articles/1081871/) ⭐️ 8.0/10

从 Linux 7.2 内核发布开始，io_uring 子系统将替换传统的链表跟踪机制，采用全新的无锁多生产者单消费者（MPSC）FIFO 队列。这一架构转变有效降低了并发瓶颈，并为异步 I/O 操作带来了显著的性能提升。 该优化直接提升了高性能异步 I/O 工作负载的吞吐量和延迟表现，这对现代数据库、Web 服务器和云基础设施至关重要。通过展示一种相对直观的无锁算法设计，它还降低了系统程序员实现高效并发数据结构的门槛。 新实现保留了每个生产者的 FIFO 顺序，并通过原子交换操作进行线程同步，从而避免了传统互斥锁或自旋锁的开销。尽管无锁算法通常较为复杂，但此特定设计优先考虑了可读性和在内核开发中的实际应用价值。

rss · LWN.net · 7月15日 13:35

**背景**: io_uring 是一个专为高性能异步 I/O 设计的 Linux 系统调用接口，通过在用户空间和内核之间共享环形缓冲区来最大限度地减少上下文切换。历史上，管理待处理的 I/O 请求队列需要依赖锁定机制，这在重负载下容易产生竞争。转向无锁 MPSC 队列解决了这一问题，它允许多个线程并发提交请求而无需相互阻塞，从根本上契合了 io_uring 非阻塞高效的核心设计理念。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://man7.org/linux/man-pages/man7/io_uring.7.html">io _ uring (7) - Linux manual page</a></li>
<li><a href="https://u256.net/posts/mpsc-queue.html">A fast lockless MPSC queue - U256</a></li>

</ul>
</details>

**标签**: `#Linux Kernel`, `#Systems Programming`, `#io_uring`, `#Concurrency`, `#Performance Optimization`

---

<a id="item-7"></a>
## [大量过时 shim 文件仍受 UEFI 安全启动信任](https://lwn.net/Articles/1082940/) ⭐️ 8.0/10

CMU CERT 协调中心发布安全公告指出，大量存在漏洞且已过时的 shim 引导程序版本从未被列入 UEFI 安全启动的吊销列表。这一疏忽使攻击者能够绕过安全保护，在早期引导阶段执行任意代码。 该漏洞严重削弱了 UEFI 安全启动的核心保障，使攻击者能够实现持久化的底层平台入侵，且这种入侵甚至能跨越操作系统的重装而存活。系统管理员和 Linux 发行版必须紧急更新固件与引导配置，以防止未经授权的代码执行。 拥有管理员权限或能够修改引导流程的攻击者，可以利用这些未被吊销的 shim 二进制文件，在操作系统初始化之前加载恶意或未签名的内核组件。该安全公告附带了一份需要立即关注的易受攻击的 shim 版本清单。

rss · LWN.net · 7月15日 12:49

**背景**: UEFI 安全启动是一项确保设备启动过程中仅运行受信任软件的安全标准。shim 作为 Linux 系统的一级引导程序，会在将控制权移交给主内核之前验证数字签名。为了维持安全性，微软和硬件厂商会定期发布吊销列表（dbx）以封锁已受损或过时的引导程序，但此次事件暴露了该更新机制中存在的漏洞。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.welivesecurity.com/en/eset-research/forgotten-uefi-shims-undermining-secure-boot/">Forgotten UEFI shims undermining Secure Boot - WeLiveSecurity</a></li>
<li><a href="https://uefi.org/revocationlistfile">UEFI Revocation List File - Unified Extensible Firmware Interface</a></li>

</ul>
</details>

**标签**: `#Linux Security`, `#UEFI Secure Boot`, `#Vulnerability Advisory`, `#System Boot`, `#Cybersecurity`

---

<a id="item-8"></a>
## [苏黎世联邦理工学院发布傅里叶像素显示摄像技术](https://www.schneier.com/blog/archives/2026/07/a-video-screen-that-is-also-a-camera.html) ⭐️ 8.0/10

苏黎世联邦理工学院的研究人员开发了一种新型傅里叶像素架构，使其能够同时充当高分辨率显示器和摄像头。这项发表在 Nature 杂志上的突破，使单个紧凑像素能够操纵光强、振荡相位和偏振，从而生成和感知任意光场。 这项技术在计算光学和硬件集成方面取得了重大突破，有望彻底改变增强现实、自适应光学和光通信等领域。通过将显示和传感功能合并到单个像素中，它不仅能催生更紧凑的多功能设备，也引发了关于无处不在的监控所带来的隐私问题的关注。 傅里叶像素调制了光波的完整描述，在紧凑的尺寸内实现了对矢量可编程像素前所未有的控制。研究团队将这一架构扩展到了光子波导模式，建立了一个可扩展且通用的双向光控制框架。

rss · Schneier on Security · 7月15日 11:04

**背景**: 传统屏幕依靠独立硬件组件发射光线供人观看，并由单独的传感器捕捉入射光，这增加了设备的体积和复杂性。计算成像和光场显示技术此前曾尝试使用复杂的光学阵列或软件重建来合并这些功能，但往往缺乏实时的双向控制能力。这种新架构通过物理工程化每个像素，利用先进的光波操纵技术，同时处理发射和探测功能，从而填补了这一空白。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nature.com/articles/s41586-026-10681-7">Fourier pixels for bidirectional light control | Nature</a></li>
<li><a href="https://newsroom.conceptuel.ch/eth-zurich-unveil-fourier-pixel/">A Pixel That Reads and Writes Light: ETH Zurich Unveils the Fourier Pixel - Conceptuel Newsroom</a></li>

</ul>
</details>

**标签**: `#Optics`, `#Hardware Innovation`, `#Computer Vision`, `#Surveillance Tech`, `#Research`

---

<a id="item-9"></a>
## [热力学计算机利用能量波动实现高效计算](https://www.quantamagazine.org/thermodynamic-computers-go-with-the-energy-flow-20260715/) ⭐️ 8.0/10

研究人员与初创企业正在开发一种新型热力学计算硬件，该硬件有意利用随机的热能与能量波动来执行计算，从而摆脱了传统数字架构对噪声的防护机制。Extropic 和 Normal Computing 等公司已推出基于耦合 RLC 电路的随机处理单元（SPU）及热力学采样单元（TSU）等原型设备。 这一新范式通过将物理噪声转化为计算资源而非视为缺陷，有效应对了现代人工智能与概率计算中日益严峻的能效与扩展瓶颈。它有望大幅降低机器学习负载的功耗，并显著提升每瓦特算力表现。 该硬件采用热力学采样单元替代传统全数字逻辑，通过受控的能量波动进行推理运算，早期原型已成功演示高斯采样与矩阵求逆等功能。不过，其可靠运行仍需依赖新型诊断工具来精确检测并管理纳米尺度下的信息与能量状态跃迁。

rss · Quanta Magazine · 7月15日 15:24

**背景**: 传统数字计算机依赖严格的电压阈值来表示二进制状态，因此极易受到随机热噪声的影响，这也是工程师们投入大量资源为电路屏蔽能量波动的原因。热力学计算则反其道而行之，专门设计能够主动利用这些自然波动的系统，从而比传统图形处理器更高效地解决复杂的概率性问题。随着硅基芯片的物理扩展逼近极限，这种转变正契合了产业界对可持续、高性能人工智能硬件的迫切需求。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Thermodynamic_computing">Thermodynamic computing - Wikipedia</a></li>
<li><a href="https://www.nature.com/articles/s41467-025-59011-x">Thermodynamic computing system for AI applications | Nature Communications</a></li>
<li><a href="https://extropic.ai/writing/thermodynamic-computing-from-zero-to-one">Thermodynamic Computing: From Zero to One | Extropic</a></li>

</ul>
</details>

**标签**: `#Thermodynamic Computing`, `#Hardware Architecture`, `#Energy Efficiency`, `#AI Hardware`, `#Computer Science`

---

<a id="item-10"></a>
## [DeepSeek 完成超 500 亿元首轮融资并采用特殊架构保控制权](https://t.me/zaihuapd/42589) ⭐️ 8.0/10

AI 初创公司 DeepSeek 已完成逾 500 亿元人民币（约合 74 亿美元）的首轮融资，估值突破 500 亿美元。该公司采用了非常规的投资架构，资金需注入由 CEO 梁文锋管理的有限合伙企业，而非直接投入运营实体本身。 这笔史无前例的资金注入凸显了全球在顶尖 AI 模型领域的激烈竞争，同时也展示了创始人在引入巨额外部资本时如何通过创新治理模式来保留战略控制权。此举为中国高科技行业的风险投资架构树立了新标杆。 投资者需接受五年锁定期并明确放弃表决权，而 CEO 梁文锋个人在本轮中出资 200 亿元。腾讯和宁德时代等巨头正考虑分别投资 100 亿元和 50 亿元。

telegram · zaihuapd · 7月15日 12:56

**背景**: 在风险投资支持的初创企业中，将经济所有权与投票控制权分离是防止创始人在多轮融资中被稀释权力的常见策略。传统的双重股权结构或有限合伙企业工具允许内部人员高效管理资本，同时保护日常运营和长期愿景免受外部股东干预。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://fastercapital.com/content/Startup--Limited-Partnership.html">Startup : Limited Partnership - FasterCapital</a></li>
<li><a href="https://www.paulhastings.com/insights/client-alerts/navigating-control-mechanisms-in-startups">Navigating Control Mechanisms in Startups | Paul Hastings LLP</a></li>
<li><a href="https://privatewealthlawgroup.com/how-venture-capital-investments-can-shape-both-ownership-and-control/">How Venture Capital Investments Can Shape Both Ownership and Control - Private Wealth Law Group, P.C.</a></li>

</ul>
</details>

**标签**: `#AI Industry`, `#Venture Capital`, `#Corporate Governance`, `#DeepSeek`, `#Tech Funding`

---

<a id="item-11"></a>
## [马斯克宣布无条件开源 X 平台全部代码](https://x.com/elonmusk/status/2077361679034118271) ⭐️ 8.0/10

埃隆·马斯克宣布，在完成全面的安全漏洞审查后，X 平台将无条件开源其全部代码库。该平台还将邀请独立的第三方审计人员核查已发布源代码与实际生产环境是否完全一致。 该举措为大型社交网络树立了罕见的行业先例，将彻底透明置于传统的专有保密之上。它可能从根本上重塑业界对软件安全审计的期望，并有助于重建公众对数字基础设施的信任。 该验证流程依赖于生产环境与源代码的比对检查，以确保运行系统中不存在隐藏后门或未记录的依赖项。独立审查人员将对确定性编译输出与已部署的二进制文件进行验证，以保证数学层面的一致性。

telegram · zaihuapd · 7月15日 13:32

**背景**: 由于专有算法、数据管道和云基础设施的庞大规模，开源一个复杂的实时社交网络极为罕见。历史上，企业通常使用可重复构建和供应链安全审计来证明分发的二进制文件与源代码仓库一致，但对于主流科技公司而言，实现全平台透明仍主要停留在理论阶段。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://reproducible-builds.org/">Reproducible Builds — a set of software development practices ...</a></li>
<li><a href="https://www.sentinelone.com/cybersecurity-101/cybersecurity/software-supply-chain-security/">Software Supply Chain Security: Risks & Best Practices</a></li>
<li><a href="https://github.com/takusaotome/claude-skills-library/blob/main/docs/en/skills/meta/production-parity-test-designer.md">claude-skills-library/docs/en/skills/meta/production-parity ...</a></li>

</ul>
</details>

**标签**: `#Open Source`, `#Software Engineering`, `#Tech News`, `#Transparency`, `#X Platform`

---

<a id="item-12"></a>
## [ASML 拟涨光刻设备价，台积电抵制部分中企接受](https://news.bloomberglaw.com/artificial-intelligence/asml-plans-price-increases-on-chipmaking-equipment-information) ⭐️ 8.0/10

ASML 计划上调其 EUV 和 DUV 光刻系统的价格，理由是需求强劲且先进 EUV 产能已预订至 2027 年底。台积电正抵制拟议的 EUV 涨价，但部分中国制造商已同意将 DUV 设备价格上涨 10%。 此次定价调整凸显了 ASML 前所未有的市场话语权，并可能显著影响全球半导体制造成本，尤其是 AI 硬件和先进芯片生产。台积电与中国企业截然不同的反应，也揭示了半导体行业持续存在的供应链紧张与地缘政治博弈。 首席财务官 Roger Dassen 指出，当前市场环境赋予 ASML 更强的定价权，先进 EUV 设备的产能已几乎预订至 2027 年底。该公司已向部分客户（包括中国芯片制造商）通报，拟将 DUV 设备价格上涨 10%，且部分中方客户已同意该涨幅。

telegram · zaihuapd · 7月15日 16:49

**背景**: 极紫外（EUV）和深紫外（DUV）光刻是芯片制造过程中用于在硅片上蚀刻微观电路图案的关键技术。EUV 采用更短的 13.5 纳米波长来生产 3nm 和 5nm 等先进制程节点，而 DUV 依赖较长的波长（193 纳米或 248 纳米）用于成熟或复杂度较低的工艺。ASML 垄断了 EUV 系统，使其设备成为全球尖端半导体制造不可或缺的核心装备。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Extreme_ultraviolet_lithography">EUV lithography - Wikipedia</a></li>
<li><a href="https://research.ibm.com/blog/what-is-euv-lithography">What is EUV lithography ? - IBM Research</a></li>
<li><a href="https://www-trendforce-com.nproxy.org/insights/asml-euv">ASML EUV Dominance & China’s Semiconductor Equipment Push</a></li>

</ul>
</details>

**标签**: `#Semiconductor`, `#Lithography`, `#Supply Chain`, `#ASML`, `#Chip Manufacturing`

---