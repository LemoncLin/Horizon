---
layout: default
title: "Horizon Summary: 2026-07-11 (ZH)"
date: 2026-07-11
lang: zh
---

> 从 44 条内容中筛选出 7 条重要资讯。

---

1. [人形机器人远程完成全球首例活体胆囊切除术](#item-1) ⭐️ 9.0/10
2. [苹果起诉 OpenAI 涉嫌窃取商业机密推进硬件业务](#item-2) ⭐️ 9.0/10
3. [vLLM v0.25.0 弃用 PagedAttention 并默认启用 Model Runner V2](#item-3) ⭐️ 8.0/10
4. [VultronRetriever 模型家族发布，登顶 MTEB 榜单并优化边缘部署](#item-4) ⭐️ 8.0/10
5. [SK 海力士 CEO 预警：2027 年将迎来史上最严重内存短缺](#item-5) ⭐️ 8.0/10
6. [U-Boot 曝出六项漏洞可致启动前恶意代码执行](#item-6) ⭐️ 8.0/10
7. [智谱启动“摸高计划”：聚焦 AGI 研发而非短期变现](#item-7) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [人形机器人远程完成全球首例活体胆囊切除术](https://arstechnica.com/ai/2026/07/humanoid-robots-controlled-by-surgeons-did-world-first-operation-on-live-pigs/) ⭐️ 9.0/10

外科医生通过远程操控宇树 G1 人形机器人，成功在活猪身上完成了两例微创胆囊切除手术，这是全球首次将通用人形机器人用于活体手术。该临床试验结果已发表在《自然》期刊上。 这一突破表明，价格低廉的通用人形机器人能够媲美价值数百万美元的专用手术系统，有望彻底改变农村诊所、战场或太空任务等资源有限地区的远程医疗格局。 宇树 G1 基础版售价约 13500 美元，配备灵巧手后约为 67000 美元，远低于达芬奇等传统手术机器人平台。研究人员指出，尽管远程操作延迟仍是技术挑战，但该机器人紧凑的体积和混合力位控制能力使其能够完成精确的腹腔镜操作。

telegram · zaihuapd · 7月11日 02:29

**背景**: 机器人辅助手术长期以来由专为手术室设计的专用固定臂系统主导，这些系统精度高但成本高昂且移动性有限。远程操作允许外科医生远距离控制这些机器，但网络延迟和缺乏触觉反馈往往会增加精细组织操作的难度。用多功能的人形平台取代专用硬件，为可扩展、可部署的手术机器人带来了新的可能性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nature.com/articles/s41586-026-10796-x">In vivo feasibility study of humanoid robots in surgery - Nature</a></li>
<li><a href="https://blog.robozaps.com/b/unitree-g1-review">Unitree G1 Review [2026]: Our Verdict | RoboZaps Blog</a></li>

</ul>
</details>

**标签**: `#Robotics`, `#Medical Technology`, `#Surgical Innovation`, `#Humanoid Robots`, `#Remote Surgery`

---

<a id="item-2"></a>
## [苹果起诉 OpenAI 涉嫌窃取商业机密推进硬件业务](https://www.cnbc.com/2026/07/10/apple-openai-lawsuit-trade-secrets.html) ⭐️ 9.0/10

7 月 10 日，苹果公司在加州联邦法院对 OpenAI 及两名前员工提起诉讼，指控其系统性窃取涉及产品设计、制造工艺和供应链的商业机密，以加速消费级硬件研发。起诉书具体指出，有前员工离职后仍访问内部网络下载硬件文件，且 OpenAI 硬件负责人被指在离职前将供应商资料发送至个人邮箱，并要求求职者携带苹果零部件参加面试。 此案凸显了传统硬件巨头与 AI 软件巨头在共同向智能眼镜和机器人等实体产品转型时日益激烈的竞争。同时，这也标志着科技公司在应对激进的人才争夺和跨行业 AI 整合时，保护知识产权的法律斗争已全面升级。 苹果表示目前已有超过 400 名前员工在 OpenAI 工作，引发了关于技术知识广泛转移的担忧。指控内容涉及直接接触苹果的供应链合作伙伴，并在招聘过程中要求候选人携带专有硬件零部件参加面试。

telegram · zaihuapd · 7月11日 03:14

**背景**: 科技行业的商业秘密诉讼屡见不鲜，但涉及 AI 公司激进拓展消费级硬件的案件却相对罕见且备受审视。苹果历来对其制造生态系统和供应链保密性保持严格控制，而 OpenAI 此前主要专注于大语言模型和软件基础设施的开发。此案可能标志着一种转变，即 AI 企业在进入实体产品开发时将面临更严格的法律边界。

**标签**: `#AI`, `#Hardware`, `#Trade Secrets`, `#Corporate Litigation`, `#Tech Industry`

---

<a id="item-3"></a>
## [vLLM v0.25.0 弃用 PagedAttention 并默认启用 Model Runner V2](https://github.com/vllm-project/vllm/releases/tag/v0.25.0) ⭐️ 8.0/10

vLLM v0.25.0 正式将 Model Runner V2 设为所有稠密模型的标准执行路径，并彻底移除了旧版 PagedAttention 实现。此次更新还使原生 Transformers 后端性能达到与 vLLM 完全持平的水平，同时新增了对 FP8 MoE 的支持以及与 CUDA 图兼容的动态推测解码功能。 这一架构调整大幅简化了框架代码库，并提升了企业级 AI 部署中的推理效率，直接影响依赖高吞吐量大语言模型服务的开发者。通过统一执行路径并使原生后端速度持平，此次更新降低了开源模型在生产环境中集成的门槛。 Model Runner V2 现已支持 EVS、实时嵌入以及多模态前缀双向注意力机制，通用推测解码则通过 TLI 及 DSpark、DFlash 等新草稿生成器架构实现了异构词表支持。此次发布还整合了统一的流式解析引擎，并将支持范围扩展至 GLM-5 和 MiniMax-M3 等众多多模态与混合架构模型。

github · khluu · 7月11日 20:06

**背景**: PagedAttention 最初旨在通过将键值缓存划分为固定大小的块来优化大语言模型推理过程中的内存使用，其原理类似于操作系统中的虚拟内存分页技术。FP8 MoE 模型利用量化精度，在推理时仅激活部分参数，从而在保持精度的同时大幅降低计算成本。动态推测解码则通过使用较小的草稿模型并行预测令牌，再由主模型进行验证，以此跳过冗余计算来进一步加速生成过程。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://smazcw3.github.io/2025-05-01-vLLM-Inference/">vLLM Part 1: PagedAttention & the LLM Serving Problem</a></li>
<li><a href="https://www.lmsys.org/blog/2025-11-25-fp8-rl/">Unified FP8: Moving Beyond Mixed Precision for Stable and Accelerated MoE RL - LMSYS Org</a></li>
<li><a href="https://arxiv.org/pdf/2512.23858">Yggdrasil: Bridging Dynamic Speculation and Static Runtime for...</a></li>

</ul>
</details>

**标签**: `#LLM Inference`, `#vLLM`, `#AI Infrastructure`, `#Model Optimization`, `#Open Source`

---

<a id="item-4"></a>
## [VultronRetriever 模型家族发布，登顶 MTEB 榜单并优化边缘部署](https://www.reddit.com/r/MachineLearning/comments/1utmxq8/vultronretriever_family_of_models_released_on/) ⭐️ 8.0/10

VultronRetriever 模型家族（包含 Prime-8B、Core-4.5B 和 Flash-0.8B 变体）已在 HuggingFace 发布，并宣称在 MTEB 榜单的各自类别中均排名第一。这些模型专为离线和边缘设备部署进行了优化，显著降低了存储占用并提升了推理吞吐量。 该发布满足了业界对无需依赖云端即可高效运行的高性能检索模型的迫切需求，使先进 AI 能够部署于移动和嵌入式硬件上。通过将顶级基准性能与边缘优化相结合，它降低了开发者构建私有、低延迟 RAG 系统的门槛。 旗舰版 Prime-8B 模型的索引存储体积较此前 9B 级领先模型缩小了 16 倍，吞吐量提升 12 倍；轻量版 Flash-0.8B 可在完全离线的情况下每分钟处理多达 60 张图像。所有模型均采用 Hydra 架构以实现晚期交互检索，并声称训练过程中零数据集重复或评估污染。

reddit · r/MachineLearning · /u/madkimchi · 7月11日 15:22

**背景**: 检索增强生成严重依赖嵌入模型将文本和文档转换为可搜索的向量，但传统的密集检索器通常在资源受限的设备上面临延迟和存储限制。晚期交互检索技术通过计算细粒度的词元级相似度而非依赖单一向量表示来提升准确性。MTEB 是用于评估这些嵌入模型跨语言、多模态及领域特定能力的标准化评测套件。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://leaderboard.mteb.org/">Benchmark Overview · MTEB Leaderboard</a></li>
<li><a href="https://weaviate.io/blog/late-interaction-overview">An Overview of Late Interaction Retrieval Models: ColBERT ...</a></li>

</ul>
</details>

**标签**: `#Retrieval Models`, `#Edge AI`, `#MTEB`, `#HuggingFace`, `#NLP`

---

<a id="item-5"></a>
## [SK 海力士 CEO 预警：2027 年将迎来史上最严重内存短缺](https://www.reuters.com/world/asia-pacific/sk-hynix-ceo-sees-worst-ever-memory-supply-shortage-2027-says-demand-outstrip-2026-07-10/) ⭐️ 8.0/10

SK 海力士 CEO 郭鲁正警告称，即便公司积极扩产，全球内存需求在 2027 年至 2030 年间仍将持续超过供应能力。这一预测正值该公司 2025 年营业利润创下 47 万亿韩元纪录，并在纳斯达克交易所成功上市之际。 这一预测凸显了由 AI 基础设施爆发式增长引发的半导体供应链结构性瓶颈，将直接制约全球数据中心的扩容与 GPU 部署。内存厂商议价权的提升标志着全球 AI 硬件生态格局的根本性重塑。 生产高带宽内存所需的晶圆产能约为标准 DDR5 的三倍，形成了难以快速缓解的多年期建厂瓶颈。为应对产能限制，SK 海力士正基于土地、电力和人力成本优势，积极评估在美国、日本及东南亚建设海外晶圆厂的可行性。

telegram · zaihuapd · 7月11日 00:45

**背景**: 高带宽内存是一种将存储芯片垂直堆叠的特殊动态随机存取存储器，能够提供极高的数据传输速率，是现代 AI 加速器和图形处理器的核心组件。由于高带宽内存制造工艺复杂且每比特消耗的硅晶圆远超传统内存，生成式 AI 工作的激增已导致全球产能紧张。这种结构性约束意味着即使芯片制造商扩建工厂，新晶圆厂也需要数年时间才能稳定良率并满足企业级应用标准。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://tech-insider.org/memory-chip-shortage-2026-ai-consumer-electronics/">Memory Chip Shortage 2026: HBM Takes 23% of DRAM Wafers</a></li>
<li><a href="https://chip.computer/blog/hbm-memory-crisis-hidden-bottleneck-2026">The HBM Memory Crisis: AI's Hidden Bottleneck | Chip.computer</a></li>
<li><a href="https://www.astutegroup.com/news/industrial/sk-hynix-ramps-dram-output-eightfold-but-global-memory-scarcity-pressures-pricing-and-supply-chains/">SK Hynix ramps DRAM output eightfold but global memory scarcity pressures pricing and supply chains - Astute Group</a></li>

</ul>
</details>

**标签**: `#Semiconductors`, `#Memory Supply Chain`, `#AI Infrastructure`, `#Industry Forecast`, `#SK Hynix`

---

<a id="item-6"></a>
## [U-Boot 曝出六项漏洞可致启动前恶意代码执行](https://www.bleepingcomputer.com/news/security/new-u-boot-flaws-could-enable-stealthy-firmware-attacks/) ⭐️ 8.0/10

安全公司 Binarly 披露了 U-Boot FIT 签名验证代码中的六项漏洞，其中两项可导致任意代码执行，四项会引发设备崩溃。这些缺陷追溯至 2013.07 版本，影响了超过五十个稳定版及大量下游硬件分支。 由于漏洞位于固件验证阶段，攻击者可在操作系统加载前执行恶意代码，从而绕过安全控制并植入持久化固件恶意软件。这对嵌入式设备和服务器构成严重威胁，尤其是支持远程管理功能的系统。 补丁已获得 U-Boot 维护者接受，但修复高度依赖硬件厂商将其集成到固件更新中分发给终端用户。因此，老旧或已停止支持的设备的长期安全风险较高，可能永远无法获得修复。

telegram · zaihuapd · 7月11日 08:32

**背景**: U-Boot 是一款广泛使用的开源引导程序，负责在设备启动时初始化硬件并加载操作系统。FIT 格式包含密码学签名验证机制，用于在固件执行前确保其完整性与真实性。基板管理控制器（BMC）是嵌入在服务器主板上的专用微控制器，负责带外管理功能，使管理员能够在主操作系统关闭时远程监控和控制硬件。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.csdn.net/zz67890/article/details/156210494">U-boot FIT签名验证全流程解析：从密钥生成到安全启动-CSDN博客</a></li>
<li><a href="https://cloud.tencent.com/developer/article/2412938">服务器 BMC (基板管理控制器,Baseboard Management Controller)认知</a></li>

</ul>
</details>

**标签**: `#固件安全`, `#U-Boot`, `#漏洞披露`, `#嵌入式系统`, `#网络安全`

---

<a id="item-7"></a>
## [智谱启动“摸高计划”：聚焦 AGI 研发而非短期变现](https://mp.weixin.qq.com/s/3CQSkf_kBnXiCDgS4L-Cgg) ⭐️ 8.0/10

智谱创始人唐杰宣布启动“摸高计划”，将战略重心从短期商业变现转向长期 AGI 研发。该路线图聚焦四大技术支柱：长程任务规划、自治智能体系统、完全自我训练模型以及极致安全治理。 这一声明标志着中国竞争激烈的 AI 产业在资源分配上的重要转变，强调基础研究与安全对齐，而非快速产品变现。通过投入百亿级资金攻坚机械可解释性，智谱旨在应对 AI 能力扩张过程中的关键透明度与控制难题。 该计划明确致力于通过机械可解释性使黑盒模型透明化，即通过映射神经网络电路来理解模型的决策过程。此外，公司指出其最新发布的 GLM-5.2 模型能力已接近海外最前沿水平，并因其开源特性在技术社群中广受关注。

telegram · zaihuapd · 7月11日 13:59

**背景**: 机械可解释性是 AI 安全领域的一个新兴方向，旨在逆向工程神经网络，以精确理解模型如何处理信息并做出决策。长程任务规划与自治智能体系统代表了超越简单对话机器人、迈向复杂多步问题解决的关键前沿。而自我训练与严格的安全治理则被视为实现可靠通用人工智能的必要前提。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://intuitionlabs.ai/articles/mechanistic-interpretability-ai-llms">Understanding Mechanistic Interpretability in AI Models | IntuitionLabs</a></li>
<li><a href="https://www.nature.com/articles/s41598-025-91448-4">Enhancement of long-horizon task planning via active and passive modification in large language models | Scientific Reports</a></li>
<li><a href="https://www.ibm.com/think/topics/ai-agents">What Are AI Agents ? | IBM</a></li>

</ul>
</details>

**标签**: `#AGI`, `#AI Strategy`, `#Mechanistic Interpretability`, `#Autonomous Agents`, `#Zhipu AI`

---