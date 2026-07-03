---
layout: default
title: "Horizon Summary: 2026-07-03 (ZH)"
date: 2026-07-03
lang: zh
---

> 从 63 条内容中筛选出 3 条重要资讯。

---

1. [Karpathy 的 NanoChat：约 100 美元即可构建的功能性聊天机器人](#item-1) ⭐️ 8.0/10
2. [对比解码差分法仅凭 Logits 即可恢复微调数据](#item-2) ⭐️ 8.0/10
3. [华为发布搭载昇腾 950PR 的 Atlas 350 加速卡](#item-3) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Karpathy 的 NanoChat：约 100 美元即可构建的功能性聊天机器人](https://github.com/karpathy/nanochat) ⭐️ 8.0/10

Andrej Karpathy 发布了 NanoChat，这是一个用于训练大语言模型的实验性框架，展示了如何以约 100 美元的成本构建功能性聊天机器人。该项目拥有极简且易于修改的代码库，涵盖了在单张 GPU 上进行分词、预训练、微调及推理的全过程。 该项目为商业聊天机器人提供了一种可访问且具成本效益的替代方案，证明了以极少资源实现高质量语言模型能力是可行的。它使开发者和研究人员能够在不依赖昂贵云基础设施的情况下，从零开始理解并构建大语言模型。 旗舰版'd32'模型采用标准的 Transformer 架构，包含 32 层神经网络，其特点主要在于有限的训练预算而非复杂的架构变更。该系统设计用于在单个 GPU 节点上运行，强调简单性和教育价值而非规模。

github · karpathy · 7月3日 17:47

**背景**: Large Language Models (LLMs) typically require massive computational resources and significant financial investment to train and deploy. However, recent trends show that Small Language Models (SLMs) can deliver comparable performance for specific tasks when optimized correctly. Techniques like model compression and efficient training pipelines allow for lower-cost development, making AI more democratized.

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/karpathy/nanochat">GitHub - karpathy/nanochat: The best ChatGPT that $100 can ...</a></li>
<li><a href="https://iamulya.one/posts/a-deep-dive-into-andrey-karpathys-nanochat/">A Deep Dive into Andrey Karpathy's Nanochat | Amulya Bhatia</a></li>

</ul>
</details>

**标签**: `#AI`, `#Open Source`, `#LLM`, `#Karpathy`, `#Cost-Efficient`

---

<a id="item-2"></a>
## [对比解码差分法仅凭 Logits 即可恢复微调数据](https://www.reddit.com/r/MachineLearning/comments/1umn2dk/contrastive_decoding_diffing_cdd_recovering/) ⭐️ 8.0/10

研究人员推出了对比解码差分法（CDD），这是一种灰盒方法，仅需访问 logits 即可从大语言模型中逐字恢复微调数据，无需模型权重或激活值。该方法显著优于之前的白盒方法，在多个模型系列中实现了 4+/5 的逐字恢复得分。 这一发现揭示了部署中的大语言模型存在严重的隐私风险，因为即使无法直接访问权重，敏感的微调数据仍可能被提取。它挑战了当前关于模型安全的假设，并证明窄微调在输出层面留下了可检测的痕迹。 CDD 直接对比基础模型与微调模型的 logits，无需进行每域校准或层选择。有趣的是，该方法还揭示了一个名为“Elena Rodriguez 博士”的幽灵角色，由于其在 Claude Sonnet 3.6 生成的合成训练数据中频繁出现，该名字出现在不相关的领域恢复结果中。

reddit · r/MachineLearning · /u/CebulkaZapiekana · 7月3日 19:01

**背景**: 大语言模型通常会在特定数据集上进行窄微调，这可能导致对敏感或专有信息的记忆。以前的攻击需要白盒访问内部权重或激活值才能检测此类痕迹，但 CDD 在灰盒设置下运行，仅提供输出概率（logits）。Logits 代表模型在转换为概率之前对每个标记的原始置信度分数，提供了了解模型决策过程的窗口。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.emergentmind.com/papers/2605.25902">CDD: Verbatim Content Recovery via Diffing</a></li>
<li><a href="https://www.aimodels.fyi/papers/arxiv/reading-finetuning-prior-verbatim-content-recovery-via">Reading the Finetuning Prior: Verbatim Content Recovery via ...</a></li>

</ul>
</details>

**标签**: `#LLM Security`, `#Privacy`, `#Machine Learning Research`, `#Adversarial Attacks`, `#Fine-tuning`

---

<a id="item-3"></a>
## [华为发布搭载昇腾 950PR 的 Atlas 350 加速卡](https://t.me/zaihuapd/42329) ⭐️ 8.0/10

在华为中国合作伙伴大会 2026 上，华为正式发布了搭载全新昇腾 950PR 处理器的 Atlas 350 加速卡。该卡算力达到英伟达 H20 的近三倍，且是目前国内唯一支持 FP4 低精度推理的加速卡。 这一发布通过提供高性能的英伟达替代方案，显著增强了国内 AI 硬件生态系统。FP4 推理的支持不仅降低了延迟和投资成本，还使得单卡能够加载 700 亿参数的大型模型，对国内 AI 基础设施发展具有重要意义。 Atlas 350 配备了 112GB 的自研高带宽内存（HBM），FP4 算力达到 1.56 petaflops。与前代产品相比，它在向量算力、互联带宽和内存方面均有显著提升。

telegram · zaihuapd · 7月3日 08:35

**背景**: FP4（4 位浮点数）是一种新兴的低精度格式，旨在加速 AI 推理的同时保持可接受的模型精度，从而降低大语言模型所需的内存带宽。英伟达最近在其 Blackwell 架构中引入了 NVFP4，为高效推理设立了新标准。华为昇腾 950PR 利用这种格式，在日益增长的高性价比 AI 加速器市场中展开有力竞争。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.huaweicentral.com/huawei-atlas-350-ai-card-debuts-outshining-nvidia-h20-chip/">Huawei Atlas 350 AI card debuts, outshining Nvidia H20 chip</a></li>
<li><a href="https://www.tomshardware.com/pc-components/gpus/huawei-unveils-new-atlas-350-ai-accelerator-with-1-56-pflops-of-fp4-compute-and-up-to-112gb-of-hbm-claims-2-8x-more-performance-than-nvidias-h20">Huawei unveils new Atlas 350 AI accelerator with 1.56 PFLOPS ...</a></li>
<li><a href="https://www.spheron.network/blog/huawei-ascend-950-vs-nvidia-b300-b200-llm-inference-2026/">Huawei Ascend 950 vs NVIDIA B300 and B200 for... | Spheron Blog</a></li>

</ul>
</details>

**标签**: `#AI Hardware`, `#Huawei`, `#Accelerators`, `#Nvidia Competition`, `#Large Language Models`

---