---
layout: default
title: "Horizon Summary: 2026-08-02 (ZH)"
date: 2026-08-02
lang: zh
---

> 从 44 条内容中筛选出 1 条重要资讯。

---

1. [Kimi K3 2.78 万亿参数开源模型架构深度解析](#item-1) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Kimi K3 2.78 万亿参数开源模型架构深度解析](https://www.reddit.com/r/MachineLearning/comments/1vdndys/kimi_k3_deep_dive_architecture_training/) ⭐️ 8.0/10

一篇关于月之暗面 Kimi K3 模型的全面技术分析已发布，详细介绍了其创新的 Kimi Delta Attention（KDA）架构、采用分数量衡的 Stable LatentMoE、NoPE 位置编码以及 100 万 token 的上下文能力。博客还涵盖了模型的强化学习训练管道和推理服务优化。 作为拥有 2.78 万亿参数的开源权重模型，Kimi K3 在使大规模高效架构公开可用方面迈出了重要一步。其创新的注意力机制和 MoE 负载均衡技术可能会影响行业在长上下文和多模态 LLM 开发方面的方法。 Kimi K3 采用 3 个 KDA 层与 1 个完整多头潜在注意力（MLA）层交错的配置，在计算成本与表达能力之间取得最佳平衡。该模型使用分数量衡——一种基于线性规划的 MoE 专家 token 分配方法——以实现无需超参数调优的稳定训练。

reddit · r/MachineLearning · /u/imrancoder · 8月2日 17:03

**背景**: 混合专家（MoE）模型通过每个 token 仅激活部分参数来扩展模型容量，但需要精细的负载均衡以防止专家坍塌。KDA 等注意力机制将线性注意力扩展至支持超长上下文，且计算复杂度呈线性增长；位置编码（如 NoPE）则帮助 Transformer 理解 token 顺序，而无需显式的位置嵌入。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2510.26692">[2510.26692] Kimi Linear: An Expressive, Efficient Attention Architecture</a></li>
<li><a href="https://www.emergentmind.com/topics/kimi-delta-attention-kda">Kimi Delta Attention: Efficient Long-Context Models</a></li>
<li><a href="https://openathena.ai/blog/quantile-balancing/">Mixture of Experts Quantile Balancing: Validated at 32B-A5B (1e22 FLOPs) Scale | Open Athena</a></li>

</ul>
</details>

**标签**: `#LLM Architecture`, `#Open-Weight Models`, `#Large Language Models`, `#MoE`, `#AI Research`

---