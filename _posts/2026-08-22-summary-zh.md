---
layout: default
title: "Horizon Summary: 2026-08-22 (ZH)"
date: 2026-08-22
lang: zh
---

> 从 36 条内容中筛选出 1 条重要资讯。

---

1. [研究者训练 250M 参数 LLM，亚 2 比特量化实现 60MB CPU 部署](#item-1) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [研究者训练 250M 参数 LLM，亚 2 比特量化实现 60MB CPU 部署](https://www.reddit.com/r/MachineLearning/comments/1vv2nkh/i_developed_my_own_quantized_llm_from_scratch/) ⭐️ 8.0/10

一位研究者使用 30B token 的 FineWeb 数据从头训练了 250M 参数的 LLM，实现了亚 2 比特量化，整个部署仅 60MB，在 CPU 上以 400 tok/s 的速度运行，无需 GPU。该模型采用创新的基于磁盘的 KV 缓存系统，最近 2048 个 token 以 fp16 存储，较旧的 token 压缩为 1 比特写入磁盘，支持从最多 1 亿 token 的上下文中检索。 这项工作证明了极端量化结合基于磁盘的检索可以在无 GPU 的资源受限设备上实现长上下文 LLM 推理。该方法可能使 LLM 能够部署到边缘设备和离线应用场景，在内存和计算资源严重受限的情况下依然可用。 模型在未见过的英文网页文本上达到 0.99 比特/字节的压缩率，交叉熵为 3.15 nats，困惑度为 23.3。与传统嵌入表不同，每个 token 被表示为固定的 512 位代码，13.1 万词表的完整词汇仅需 8.4MB。磁盘缓存每 token 存储约 320 字节，因此 100 万 token 的历史记录在磁盘上占用约 320MB。

reddit · r/MachineLearning · /u/Final-Data-1410 · 8月22日 04:39

**背景**: 大型语言模型在推理时通常需要大量内存来存储模型权重和 KV 缓存。标准量化技术虽然能减小模型体积，但由于 KV 缓存的内存需求，在长上下文应用中仍然面临挑战。最近的研究如 FlexGen 和 LMCache 探索了将 KV 缓存卸载到磁盘的方案，但这个项目采取了极端方法，将整个模型量化到亚 2 比特，同时保持基于磁盘的检索系统来管理上下文。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2401.06118v2">Extreme Compression of Large Language Models via Additive ...</a></li>
<li><a href="https://arxiv.org/html/2603.20397v1">KV Cache Optimization Strategies for Scalableand Efficient LLM Inference</a></li>
<li><a href="https://huggingface.co/spaces/HuggingFaceFW/blogpost-fineweb-v1">FineWeb: decanting the web for the finest text data at scale ...</a></li>

</ul>
</details>

**社区讨论**: 作者对积极的反响感到惊讶，表示原本预期会受到批评，但收到的却是好奇和有帮助的评论。该项目在发布后不久获得了 7 个 GitHub 星标，表明社区对这种极端量化方法有真正的兴趣。

**标签**: `#LLM`, `#quantization`, `#efficient inference`, `#long context`, `#edge deployment`

---