---
layout: default
title: "Horizon Summary: 2026-07-06 (ZH)"
date: 2026-07-06
lang: zh
---

> 从 61 条内容中筛选出 5 条重要资讯。

---

1. [法国将于 2027 年起停止认证非量子安全加密产品](#item-1) ⭐️ 9.0/10
2. [研究人员揭示量子证明的固有复杂性极限](#item-2) ⭐️ 9.0/10
3. [Anthropic 在语言模型中识别出全局工作区机制](#item-3) ⭐️ 8.0/10
4. [OpenSSH 10.4 引入后量子签名并强制实施 Linux 沙箱机制](#item-4) ⭐️ 8.0/10
5. [腾讯开源混元 Hy3 Preview：面向推理的 295B MoE 模型](#item-5) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [法国将于 2027 年起停止认证非量子安全加密产品](https://www.schneier.com/blog/archives/2026/07/france-to-stop-certifying-non-quantum-safe-encryption.html) ⭐️ 9.0/10

法国网络安全局（ANSSI）宣布，自 2027 年起将停止对缺乏量子抗性加密的安全产品进行认证，并要求企业在 2030 年前仅采购量子安全产品。这一规定实际上迫使法国的政府机构和关键基础设施运营商放弃使用经典加密系统。 该政策标志着全球向后量子密码学迁移的重大加速，为其他国家树立了监管先例。它通过强制采用新的加密标准以抵御未来量子计算威胁，直接影响了网络安全行业。 在法国政府机构和关键基础设施中使用的产品必须获得 ANSSI 批准，这使得旧加密方法实际上被逐步淘汰。这一时间表与专家预测一致，即由于量子技术的进步，RSA 等当前加密方法可能在 2030 年前变得不安全。

rss · Schneier on Security · 7月6日 10:45

**背景**: ANSSI 是法国国家信息安全局，负责制定和强制执行法国的网络安全标准和认证框架，其批准对于在公共部门和关键基础设施中使用安全产品至关重要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/NIST_Post-Quantum_Cryptography_Standardization">NIST Post-Quantum Cryptography Standardization - Wikipedia</a></li>
<li><a href="https://www.nist.gov/news-events/news/2024/08/nist-releases-first-3-finalized-post-quantum-encryption-standards">NIST Releases First 3 Finalized Post-Quantum Encryption Standards | NIST</a></li>
<li><a href="https://www.ibm.com/think/topics/quantum-safe-cryptography">What is Quantum-Safe Cryptography? | IBM</a></li>

</ul>
</details>

**标签**: `#Post-Quantum Cryptography`, `#Cybersecurity Policy`, `#Encryption Standards`, `#Government Regulation`, `#Infrastructure Security`

---

<a id="item-2"></a>
## [研究人员揭示量子证明的固有复杂性极限](https://www.quantamagazine.org/researchers-reveal-the-power-of-quantum-proofs-20260706/) ⭐️ 9.0/10

新研究证明，在使用量子证明验证问题解时存在固有的复杂性极限，确认了量子证明不能总是被经典证明有效替代。这解决了量子复杂性理论中关于量子与经典验证方法关系的一个主要开放性问题。 这一发现具有重要意义，因为它阐明了量子领域计算能力的根本边界，影响我们对量子问题难度的理解。它确立某些量子状态需要真正的量子资源进行验证，这对量子密码学和 QMA 与 NP 等复杂度类分离具有影响。 该研究强调，量子证明（例如谱相关问题的证明）容易受到测量干扰，这与可能是书面文档的假设性经典证明不同。这种区别强化了量子信息拥有独特属性的观点，即在特定情况下无法进行有效的经典模拟或验证。

rss · Quanta Magazine · 7月6日 14:33

**背景**: 量子复杂性理论研究使用量子计算机的计算问题的内在难度，定义了如 QMA（量子梅林-亚瑟）这样的复杂度类，它是 NP 的量子对应物。NP 涉及可在多项式时间内验证的经典证明，而 QMA 涉及以量子态作为见证者。长期以来，一个问题一直是这些量子证明是否总能压缩为经典形式而不丧失其验证能力，但最新结果表明此类压缩存在固有局限。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.quantamagazine.org/researchers-reveal-the-power-of-quantum-proofs-20260706/">Researchers Reveal the Power of ‘ Quantum Proofs ’ | Quanta Magazine</a></li>
<li><a href="https://en.wikipedia.org/wiki/Quantum_complexity_theory">Quantum complexity theory - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/QMA">QMA - Wikipedia</a></li>

</ul>
</details>

**标签**: `#Quantum Computing`, `#Complexity Theory`, `#Research Breakthrough`, `#Theoretical Physics`

---

<a id="item-3"></a>
## [Anthropic 在语言模型中识别出全局工作区机制](https://www.anthropic.com/research/global-workspace) ⭐️ 8.0/10

Anthropic 研究人员在语言模型中发现了一个名为“J 空间”的结构，该结构表现出神经科学中解释意识访问的全局工作区理论的五个功能特性。他们利用一种称为雅可比透镜的新可解释性技术，证明模型维护着可用于灵活推理和报告的特权内部表示。 这一发现为理解大型语言模型如何处理信息提供了具体的机制基础，弥合了人工神经网络与人类意识理论之间的差距。通过提供一种定位模型内部如何整合和广播信息的方法，它极大地推进了人工智能可解释性领域的发展。 该研究引入了雅可比透镜技术来识别形成该工作区的可言语化表示，该工作区充当整合和广播信息的枢纽。虽然工作区的容量有限导致进入具有竞争性，但它允许进行不同于自动处理的调制和灵活的内部推理。

hackernews · in-silico · 7月6日 17:44 · [社区讨论](https://news.ycombinator.com/item?id=48808002)

**背景**: 全局工作区理论（GWT）是神经科学中的一个重要框架，认为当信息进入特权工作区并广播到大脑时，就会产生意识访问。在人工智能的背景下，研究人员越来越倾向于在大型语言模型中寻找类似的結構，以理解其内部决策过程及潜在的涌现行为。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/research/global-workspace">A global workspace in language models \ Anthropic</a></li>
<li><a href="https://transformer-circuits.pub/2026/workspace/index.html">Verbalizable Representations Form a Global Workspace in Language ...</a></li>

</ul>
</details>

**社区讨论**: 社区反应不一，部分人对将模型机制与人类意识进行比较表示怀疑，认为这些发现只是共享抽象推理子空间的证据。其他人则强调其对可解释性研究的实际意义，指出理解这些机制可能带来更好的模型控制，但也引发了对可能被用于定向广告等滥用行为的担忧。

**标签**: `#AI Research`, `#Interpretability`, `#LLMs`, `#Machine Learning`

---

<a id="item-4"></a>
## [OpenSSH 10.4 引入后量子签名并强制实施 Linux 沙箱机制](https://lwn.net/Articles/1081536/) ⭐️ 8.0/10

OpenSSH 10.4 已发布，引入了结合 ML-DSA 44 和 Ed25519 的实验性后量子签名方案支持。此外，该更新在 Linux 系统上强制执行严格的 SECCOMP 和 NO_NEW_PRIVS 沙箱要求，若未启用这些功能，服务将会失败。 通过引入后量子密码学，此次发布为应对相关量子计算机带来的威胁做好了准备，显著增强了安全性。它还通过强制要求防止权限提升的现代沙箱技术，提高了 Linux 部署的安全基线。 新的签名方案遵循 IETF 关于将 ML-DSA 44 与 Ed25519 结合的草案，其中 ML-DSA 44 是基于模块格数字签名算法的 NIST 标准化后量子算法。此前，sshd 仅会在缺少沙箱功能时记录错误日志，但 10.4 版本现在在没有这些功能时将拒绝运行。

rss · LWN.net · 7月6日 16:13

**背景**: 后量子密码学是指被认为能抵御量子计算机攻击的加密算法。ML-DSA 44（基于模块格的数字签名算法）是一种标准化方案，旨在抵抗此类攻击，通常与 Ed25519 等经典算法结合使用以实现向后兼容和纵深防御。SECCOMP 和 NO_NEW_PRIVS 是用于限制系统调用和防止进程获取新特权的 Linux 内核机制，对于保护 sshd 等守护进程免受利用至关重要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.armchain.org/pqc/mldsa44">ML - DSA - 44 | Armchain Docs</a></li>
<li><a href="https://www.kernel.org/doc/html/latest/userspace-api/no_new_privs.html">No New Privileges Flag — The Linux Kernel documentation</a></li>

</ul>
</details>

**标签**: `#OpenSSH`, `#Post-Quantum Cryptography`, `#Security`, `#Systems Administration`

---

<a id="item-5"></a>
## [腾讯开源混元 Hy3 Preview：面向推理的 295B MoE 模型](https://t.me/zaihuapd/42385) ⭐️ 8.0/10

腾讯已正式发布并开源混元 Hy3 preview 语言模型，这是一个专为复杂推理和智能体应用优化的 295B 参数混合专家（MoE）架构。该模型每次推理仅激活 21B 个参数，同时支持 256K 的上下文长度。 这一发布通过结合庞大的模型容量与适合中级 GPU 集群的高效推理成本，显著降低了部署大规模推理模型的门槛。它将腾讯的开源生态定位为 STEM 推理和代码开发领域的有力竞争者。 Hy3 preview 采用了重建的基础设施，模型架构与推理框架深度协同，使 CodeBuddy 等产品的首字延迟降低了 54%。它融合了快思考和慢思考机制，以提升数学、科学和编码任务中的表现。

telegram · zaihuapd · 7月6日 10:09

**背景**: 混合专家（MoE）是一种大语言模型架构，允许模型拥有巨大的总参数量，但在推理过程中仅激活其中一小部分，从而提高效率。与每个令牌都使用所有参数的密集模型不同，MoE 将输入路由到特定的“专家”子网络，减少了计算负载。这种方法使得更大、更智能的模型能够在更实惠的硬件上运行。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://techjacksolutions.com/ai-brief/tencent-open-sources-hy3-preview-295b-moe-model-with-21b-act/">Tencent Open-Sources Hy3-preview: 295B MoE Model with 21B Active Parameters Built for STEM Reasoning</a></li>
<li><a href="https://huggingface.co/blog/imnotkitty/hy3-preview">Hy3 preview: A Rebuilt Hunyuan, a 21B-Active MoE, and a New Reasoning Receipe</a></li>
<li><a href="https://github.com/Tencent-Hunyuan/Hy3-preview">GitHub - Tencent-Hunyuan/Hy3-preview: Hy3 preview (295B A21B), a leading reasoning and agent model in its size, with great cost efficiency · GitHub</a></li>

</ul>
</details>

**标签**: `#LLM`, `#Open Source`, `#MoE`, `#Tencent`, `#AI Models`

---