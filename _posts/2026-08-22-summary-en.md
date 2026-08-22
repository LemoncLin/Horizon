---
layout: default
title: "Horizon Summary: 2026-08-22 (EN)"
date: 2026-08-22
lang: en
---

> From 36 items, 1 important content pieces were selected

---

1. [Researcher Trains 250M LLM with Sub-2-Bit Quantization for 60MB CPU Deployment](#item-1) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Researcher Trains 250M LLM with Sub-2-Bit Quantization for 60MB CPU Deployment](https://www.reddit.com/r/MachineLearning/comments/1vv2nkh/i_developed_my_own_quantized_llm_from_scratch/) ⭐️ 8.0/10

A researcher trained a 250M parameter LLM from scratch on 30B tokens of FineWeb, achieving sub-2-bit quantization with only a 60MB deployment that runs at 400 tok/s on CPU without GPU. The model uses a novel disk-based KV cache system that stores recent 2048 tokens in fp16 while compressing older tokens to 1-bit on disk, enabling retrieval from up to 100M tokens of context. This work demonstrates that extreme quantization combined with disk-based retrieval can enable long-context LLM inference on resource-constrained devices without GPUs. The approach could make LLMs accessible for edge deployment and offline applications where memory and compute are severely limited. The model achieves 0.99 bits per byte on held-out English web text with cross entropy of 3.15 nats and perplexity of 23.3. Instead of a traditional embedding table, every token is represented as a fixed 512-bit code, with the full vocabulary of 131k tokens requiring only 8.4MB. The disk cache stores approximately 320 bytes per token, so 1 million tokens of history occupies roughly 320MB on disk.

reddit · r/MachineLearning · /u/Final-Data-1410 · Aug 22, 04:39

**Background**: Large language models typically require significant memory for both model weights and KV cache during inference. Standard quantization techniques reduce model size but still struggle with long-context applications due to KV cache memory requirements. Recent work like FlexGen and LMCache has explored offloading KV cache to disk, but this project takes an extreme approach by quantizing the entire model to sub-2-bit while maintaining a disk-based retrieval system for context management.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2401.06118v2">Extreme Compression of Large Language Models via Additive ...</a></li>
<li><a href="https://arxiv.org/html/2603.20397v1">KV Cache Optimization Strategies for Scalableand Efficient LLM Inference</a></li>
<li><a href="https://huggingface.co/spaces/HuggingFaceFW/blogpost-fineweb-v1">FineWeb: decanting the web for the finest text data at scale ...</a></li>

</ul>
</details>

**Discussion**: The author expressed surprise at the positive reception, noting they expected criticism but received curious and helpful comments instead. The project gained 7 GitHub stars shortly after posting, indicating genuine interest from the community in this extreme quantization approach.

**Tags**: `#LLM`, `#quantization`, `#efficient inference`, `#long context`, `#edge deployment`

---