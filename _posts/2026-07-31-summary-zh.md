---
layout: default
title: "Horizon Summary: 2026-07-31 (ZH)"
date: 2026-07-31
lang: zh
---

> 从 72 条内容中筛选出 3 条重要资讯。

---

1. [DeepSeek V4 Flash 0731：前沿性能与极具竞争力的定价](#item-1) ⭐️ 8.0/10
2. [OpenAI 通过自主推理优化将 GPT-5.6 Luna 价格下调 80%](#item-2) ⭐️ 8.0/10
3. [SIGGRAPH 时间检验奖揭晓：十年磨一剑的物理 AI 研究](#item-3) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [DeepSeek V4 Flash 0731：前沿性能与极具竞争力的定价](https://artificialanalysis.ai/models/deepseek-v4-flash) ⭐️ 8.0/10

DeepSeek 发布了 V4 Flash 0731，这是一款前沿级别的模型，定价为每百万输出令牌 0.28 美元，并提供了可在本地运行的量化变体。 此次发布使 DeepSeek 成为具有竞争力的前沿模型，通过低定价和本地部署选项使先进 AI 更加普及。 该模型采用 162GB 的 Unsloth 无损 Q8 量化变体，能够在保持与更高价 Pro 版本相当性能的同时实现家庭部署。

hackernews · theanonymousone · 7月31日 07:59 · [社区讨论](https://news.ycombinator.com/item?id=49120299)

**背景**: 量化是一种通过降低语言模型权重精度来节省内存并提高推理速度的技术。通过压缩模型参数，量化使得大型模型能够在消费级硬件上运行而不会造成明显的精度损失。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://medium.com/@abhinaykrishna/llm-quantization-in-depth-1fa65ac24f2a">LLM Quantization Explained : A Complete Guide | Medium</a></li>
<li><a href="https://llmconfigurator.com/en/guides/understanding-quantization">Quantization Explained Deep Dive | Local AI Guide | LLM Configurator</a></li>

</ul>
</details>

**社区讨论**: 社区表达了强烈的热情，用户们强调了该模型在编码任务中的成本效益，并讨论了模型托管的经济性。一些用户还推测了未来 Pro 模型的发布。

**标签**: `#AI Models`, `#LLMs`, `#DeepSeek`, `#Model Benchmarks`, `#AI Pricing`

---

<a id="item-2"></a>
## [OpenAI 通过自主推理优化将 GPT-5.6 Luna 价格下调 80%](https://simonwillison.net/2026/Jul/30/luna-price-drop/#atom-everything) ⭐️ 8.0/10

OpenAI 宣布对其 GPT-5.6 模型系列进行大幅降价：GPT-5.6 Terra 降价 20%，GPT-5.6 Luna 降价高达 80%，输入价格降至每百万 token 0.20 美元，输出降至每百万 token 1.20 美元。这一降价得益于 GPT-5.6 Sol 自主重写和优化了基于 Triton 和 Gluon 的生产推理内核，将端到端服务成本降低了 20%。 Luna 的降价使其比谷歌的 Gemini 3.1 Flash-Lite 和 Anthropic 的 Claude Haiku 4.5 更便宜，从根本上重塑了低价 LLM 层级的竞争格局。同时，这也展示了一种新范式：前沿模型能够自主优化自身的推理基础设施，有望加速整个行业的成本下降。 GPT-5.6 Sol 经过训练，能够使用 OpenAI 维护的两个开源 GPU 编程语言 Triton 和 Gluon 编写和改进 GPU 内核。它通过识别可以预计算、避免或并行化的计算来优化模型的向前传播过程，解决了导致 GPU 空闲的内存传输过多、同步开销和数据结构低效等问题。

rss · Simon Willison · 7月30日 23:58

**背景**: LLM 推理涉及在 GPU 硬件上运行前向传播过程——即将输入 token 转换为下一个 token 预测的计算。这一过程受内存带宽限制，低效的内存传输、同步和数据布局会导致昂贵的 GPU 处于空闲状态，并显著增加服务成本。Triton 和 Gluon 等 GPU 编程语言允许开发者编写自定义内核，以优化这些底层操作，从而实现最大吞吐量和最低延迟。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/gpt-5-6-frontier-intelligence-efficiency/">How GPT-5.6 fuses frontier intelligence with frontier efficiency | OpenAI</a></li>
<li><a href="https://thenewstack.io/gpt-5-6-serving-efficiency/">Kernel of truth: GPT-5.6 Sol can cut its own costs, says OpenAI - The New Stack</a></li>

</ul>
</details>

**标签**: `#AI`, `#LLMs`, `#OpenAI`, `#pricing`, `#inference optimization`

---

<a id="item-3"></a>
## [SIGGRAPH 时间检验奖揭晓：十年磨一剑的物理 AI 研究](https://mp.weixin.qq.com/s?__biz=MzIzNjc1NzUzMw==&mid=2247908730&idx=2&sn=0b3a81693cb5f92800c95b7fc50939f1) ⭐️ 8.0/10

一项十年前的统一物理 AI 训练研究荣获 SIGGRAPH 时间检验奖，该研究将机器人身体运动与灵巧手操作统一训练，其开源实现已在 GitHub 上获得 8000+星标。 该奖项验证了身体与灵巧手不应各自为战的长期研究理念，标志着物理 AI 和机器人领域的重大突破。8000+星标的社区反响表明，统一操作与移动系统具有真实的世界需求。 该研究在一个统一框架内同时训练机器人身体和灵巧手，打破了传统分别训练的做法。其开源实现吸引了大量社区关注，已获得 8000+ GitHub 星标，团队也在积极招聘。

rss · 量子位 · 7月31日 06:32

**背景**: 物理 AI 是指使机器人能够实时感知、理解和与物理世界交互的人工智能系统。灵巧操作涉及使用多指机械手进行类人精细运动技能，以高精度处理多样化物体。历史上，机器人移动和操作一直作为独立系统分别训练，但统一方法越来越被视为构建真正自主机器人的关键。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nvidia.com/en-us/glossary/generative-physical-ai/">What is Physical AI? | NVIDIA Glossary</a></li>
<li><a href="https://news.mit.edu/2021/dexterous-robotic-hands-manipulate-thousands-objects-1112">Dexterous robotic hands manipulate thousands of objects with ease | MIT News | Massachusetts Institute of Technology</a></li>

</ul>
</details>

**标签**: `#SIGGRAPH`, `#Physical AI`, `#Robotics`, `#Open Source`, `#Dexterous Manipulation`

---