---
layout: default
title: "Horizon Summary: 2026-08-28 (ZH)"
date: 2026-08-28
lang: zh
---

> 从 53 条内容中筛选出 3 条重要资讯。

---

1. [Cloudflare 通过优化 1.1.1.1 DNS 缓存节省 100TB 内存](#item-1) ⭐️ 8.0/10
2. [两名涉嫌 TeamPCP 黑客在澳大利亚被捕](#item-2) ⭐️ 8.0/10
3. [英伟达 Q4 营收 681 亿美元超预期，下季度指引上调至 780 亿美元](#item-3) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Cloudflare 通过优化 1.1.1.1 DNS 缓存节省 100TB 内存](https://blog.cloudflare.com/dns-cache-memory-optimization-1111/) ⭐️ 8.0/10

Cloudflare 工程师通过系统级优化将 1.1.1.1 的 DNS 缓存内存使用量减少了 100TB，包括消除每个枚举变体的开销、移除堆分配，并将数据紧凑排列以提高 CPU 缓存局部性。 这展示了在大规模下精心进行系统编程如何为基础设施提供商带来巨大的成本节约，超过 2500 亿条缓存条目从这些优化中受益。 在超过 2500 亿条缓存条目中，合并节省超过 15TB，通过将答案、权威和附加部分存储为带有偏移量的单个列表而非分开列表实现，但这以顺序迭代替代了随机索引。

hackernews · TangerineDream · 8月27日 17:17 · [社区讨论](https://news.ycombinator.com/item?id=49468083)

**背景**: DNS（域名系统）服务器缓存响应以避免重复查询，在存活时间（TTL）期间存储 A 和 AAAA 等记录。在 Cloudflare 每天数十亿次查询的规模下，即使每条记录的内存节省很小，也会累积成巨大的总节省。递归 DNS 解析器维护这些缓存以更快响应用户并减少上游查询负载。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.cloudflare.com/dns-cache-memory-optimization-1111/">How we saved 100 terabytes of memory by optimizing 1.1.1.1’s DNS cache | Cloudflare Blog</a></li>
<li><a href="https://www.cloudflare.com/learning/dns/what-is-recursive-dns/">What Is Recursive DNS?</a></li>

</ul>
</details>

**社区讨论**: 社区对实际优化的态度积极，工程师们称赞这种真实的系统编程方法。有人建议使用基数树以提高内存效率，其他人则讨论了在合并不同列表时 Rust 安全性的权衡。

**标签**: `#systems programming`, `#memory optimization`, `#DNS`, `#Cloudflare`, `#performance engineering`

---

<a id="item-2"></a>
## [两名涉嫌 TeamPCP 黑客在澳大利亚被捕](https://krebsonsecurity.com/2026/08/two-alleged-teampcp-hackers-arrested-in-australia/) ⭐️ 8.0/10

澳大利亚当局逮捕了两名来自西澳大利亚的 21 岁和 23 岁男子，据信是 TeamPCP 成员，该网络犯罪集团被指犯下持续时间最长的软件供应链攻击事件，影响了全球超过 1,000 家组织。 此次逮捕是对一个 prolific 供应链攻击集团的重要执法行动，凸显了恶意开源软件日益增长的威胁及其对全球网络安全的影响。 21 岁嫌疑人的身份是通过该集团领导人留下的线索追踪到的，TeamPCP 还与 Vect 勒索软件集团建立了合作关系，扩大了其行动规模。

rss · Krebs on Security · 8月27日 11:04

**背景**: 软件供应链攻击针对软件的开发和分发过程，通常通过向开源软件包中注入恶意代码实现，这些代码随后可能被成千上万的组织下载和使用。开源软件因其效率和创新性而被广泛采用，但也产生了网络犯罪分子利用的漏洞，使他们能够同时入侵多个目标。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://cybersecuritynews.com/two-australians-teampcp-supply-chain/">Two Australians Charged Over TeamPCP Supply-Chain Attacks That Hit ...</a></li>
<li><a href="https://unit42.paloaltonetworks.com/teampcp-supply-chain-attacks/">Weaponizing the Protectors: TeamPCP's Multi-Stage Supply Chain Attack ...</a></li>
<li><a href="https://cybernews.com/news/teampcp-hackers-arrested-supply-chain-attacks/">Suspected TeamPCP hackers arrested over supply chain attacks</a></li>

</ul>
</details>

**标签**: `#cybersecurity`, `#supply chain attacks`, `#law enforcement`, `#open source security`, `#cybercrime`

---

<a id="item-3"></a>
## [英伟达 Q4 营收 681 亿美元超预期，下季度指引上调至 780 亿美元](https://t.me/zaihuapd/43450) ⭐️ 8.0/10

英伟达第四财季营收达 681 亿美元，远超市场预期，其中数据中心业务贡献 623 亿美元。公司预计 2027 财年第一季度销售额将达到 780 亿美元，显著高于华尔街此前预测的 726 亿美元，每股收益为 1.62 美元。 这份财报凸显了英伟达在 AI 基础设施领域的主导地位，数据中心营收占总营收的 91%以上。上调的指引表明 AI 加速芯片需求持续旺盛，进一步巩固了英伟达在全球 AI 计算供应链中的关键角色。 首席执行官黄仁勋表示计算需求呈指数级增长，并称公司已采取战略手段应对供应链压力以确保库存。尽管游戏和汽车业务未达预期，但数据中心业务在 H100 和 Blackwell GPU 架构的推动下持续实现强劲增长。

telegram · zaihuapd · 8月27日 08:51

**背景**: 英伟达的数据中心业务已成为 AI 革命的核心支柱，H100（基于 Hopper 架构）和新一代 Blackwell GPU 等产品作为大语言模型训练和推理的主要加速芯片。DGX 平台将英伟达的硬件、软件和网络技术整合为统一的企业级 AI 基础设施系统。NVLink 互联技术实现了 GPU 之间的高带宽通信，对于在数据中心中跨多芯片扩展 AI 工作负载至关重要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Blackwell_(microarchitecture)">Blackwell (microarchitecture) - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Hopper_(microarchitecture)">Hopper (microarchitecture) - Wikipedia</a></li>
<li><a href="https://www.nvidia.com/en-us/data-center/dgx-platform/">DGX Platform: Built for Enterprise AI | NVIDIA</a></li>

</ul>
</details>

**标签**: `#NVIDIA`, `#earnings`, `#AI infrastructure`, `#semiconductors`, `#data center`

---