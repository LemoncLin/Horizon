---
layout: default
title: "Horizon Summary: 2026-09-22 (ZH)"
date: 2026-09-22
lang: zh
---

> 从 56 条内容中筛选出 1 条重要资讯。

---

1. [vLLM v0.30.0 发布，引入 Fast Start 与 DeepSeek-V4.1-Flash 支持](#item-1) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [vLLM v0.30.0 发布，引入 Fast Start 与 DeepSeek-V4.1-Flash 支持](https://github.com/vllm-project/vllm/releases/tag/v0.30.0) ⭐️ 8.0/10

vLLM v0.30.0 是一个重大版本，包含 315 位贡献者的 762 次提交，引入了 Fast Start 权重缓存、SM100 上的 MXFP8 KV 存储 DeepSeek-V4.1-Flash，以及多种新模型支持。 此版本显著提升了 LLM 推理性能与灵活性，Fast Start 降低了重启延迟，新模型支持扩展了 vLLM 的生态系统。 Fast Start 使用持久化 GPU 权重缓存守护进程，通过 CUDA IPC 映射权重；DeepSeek-V4.1-Flash 在 SM100 上利用 FlashMLA V4.1 和 MXFP8 KV 存储。

github · khluu · 9月22日 05:20

**背景**: vLLM 是一个开源 LLM 推理引擎，以高吞吐量和高效 GPU 利用率为特点。它支持多种量化方法和模型架构。此版本增加了性能优化和新模型后端。

**标签**: `#vLLM`, `#LLM inference`, `#DeepSeek`, `#GPU optimization`, `#open source`

---