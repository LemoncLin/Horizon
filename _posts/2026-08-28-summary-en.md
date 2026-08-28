---
layout: default
title: "Horizon Summary: 2026-08-28 (EN)"
date: 2026-08-28
lang: en
---

> From 53 items, 3 important content pieces were selected

---

1. [Cloudflare Saves 100TB Memory Optimizing 1.1.1.1 DNS Cache](#item-1) ⭐️ 8.0/10
2. [Two Alleged TeamPCP Hackers Arrested in Australia](#item-2) ⭐️ 8.0/10
3. [NVIDIA Q4 Revenue Surpasses Expectations at $68.1B, Raises Q1 Guidance to $78B](#item-3) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Cloudflare Saves 100TB Memory Optimizing 1.1.1.1 DNS Cache](https://blog.cloudflare.com/dns-cache-memory-optimization-1111/) ⭐️ 8.0/10

Cloudflare engineers reduced 1.1.1.1's DNS cache memory usage by 100 terabytes through systems-level optimizations, including eliminating per-variant enum overhead, removing boxed heap allocations, and packing data contiguously for better CPU cache locality. This demonstrates how careful systems programming at massive scale can yield enormous cost savings for infrastructure providers, with over 250 billion cache entries benefiting from the optimizations. The combined savings add up to over 15 terabytes with over 250 billion cache entries, achieved by storing a single list with offsets instead of separate lists for answer, authority, and additional sections, though this trades random indexing for sequential iteration.

hackernews · TangerineDream · Aug 27, 17:17 · [Discussion](https://news.ycombinator.com/item?id=49468083)

**Background**: DNS (Domain Name System) servers cache responses to avoid repeated lookups, storing records like A and AAAA entries for a Time-To-Live (TTL) period. At Cloudflare's scale of billions of daily queries, even small per-entry memory savings multiply into massive total reductions. Recursive DNS resolvers maintain these caches to serve users faster while reducing upstream query load.

<details><summary>References</summary>
<ul>
<li><a href="https://blog.cloudflare.com/dns-cache-memory-optimization-1111/">How we saved 100 terabytes of memory by optimizing 1.1.1.1’s DNS cache | Cloudflare Blog</a></li>
<li><a href="https://www.cloudflare.com/learning/dns/what-is-recursive-dns/">What Is Recursive DNS?</a></li>

</ul>
</details>

**Discussion**: Community sentiment is positive about practical optimization, with engineers praising the real-world systems programming approach. Some suggested alternatives like radix trees for memory efficiency, while others debated Rust safety tradeoffs when joining distinct lists.

**Tags**: `#systems programming`, `#memory optimization`, `#DNS`, `#Cloudflare`, `#performance engineering`

---

<a id="item-2"></a>
## [Two Alleged TeamPCP Hackers Arrested in Australia](https://krebsonsecurity.com/2026/08/two-alleged-teampcp-hackers-arrested-in-australia/) ⭐️ 8.0/10

Australian authorities arrested two men aged 21 and 23 from Western Australia, believed to be members of TeamPCP, a cybercrime syndicate blamed for the longest-running software supply chain attack spree, which compromised over 1,000 organizations worldwide. This arrest marks a significant law enforcement action against a prolific supply chain attack group, highlighting the growing threat of malicious open-source software and its impact on global cybersecurity. The 21-year-old suspect's identity was traced through clues left by the group's leader, and TeamPCP has been linked to a partnership with the Vect ransomware group, amplifying the scale of their operations.

rss · Krebs on Security · Aug 27, 11:04

**Background**: Software supply chain attacks target the development and distribution process of software, often by injecting malicious code into open-source packages, which can then be downloaded and used by thousands of organizations. Open-source software is widely adopted for its efficiency and innovation, but it also creates vulnerabilities that cybercriminals exploit to compromise multiple targets simultaneously.

<details><summary>References</summary>
<ul>
<li><a href="https://cybersecuritynews.com/two-australians-teampcp-supply-chain/">Two Australians Charged Over TeamPCP Supply-Chain Attacks That Hit ...</a></li>
<li><a href="https://unit42.paloaltonetworks.com/teampcp-supply-chain-attacks/">Weaponizing the Protectors: TeamPCP's Multi-Stage Supply Chain Attack ...</a></li>
<li><a href="https://cybernews.com/news/teampcp-hackers-arrested-supply-chain-attacks/">Suspected TeamPCP hackers arrested over supply chain attacks</a></li>

</ul>
</details>

**Tags**: `#cybersecurity`, `#supply chain attacks`, `#law enforcement`, `#open source security`, `#cybercrime`

---

<a id="item-3"></a>
## [NVIDIA Q4 Revenue Surpasses Expectations at $68.1B, Raises Q1 Guidance to $78B](https://t.me/zaihuapd/43450) ⭐️ 8.0/10

NVIDIA reported Q4 revenue of $68.1 billion, significantly exceeding market expectations, with data center sales contributing $62.3 billion. The company raised its Q1 FY2027 guidance to $78 billion, well above Wall Street's forecast of $72.6 billion, and reported EPS of $1.62. This earnings report underscores NVIDIA's dominant position in AI infrastructure, as data center revenue alone accounts for over 91% of total sales. The raised guidance signals sustained demand for AI accelerators and reinforces NVIDIA's critical role in the global AI computing supply chain. CEO Jensen Huang cited exponential growth in compute demand and said the company has taken strategic measures to ensure inventory amid supply chain pressures. While gaming and automotive segments missed expectations, the data center business continues to drive extraordinary growth powered by H100 and Blackwell GPU architectures.

telegram · zaihuapd · Aug 27, 08:51

**Background**: NVIDIA's data center business has become the backbone of the AI revolution, with products like the H100 (built on the Hopper architecture) and the newer Blackwell GPUs serving as the primary accelerators for large language model training and inference. The DGX platform provides enterprise-grade AI infrastructure that combines NVIDIA's hardware, software, and networking technologies into unified systems. NVLink interconnect technology enables high-bandwidth communication between GPUs, which is essential for scaling AI workloads across multiple chips in data centers.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Blackwell_(microarchitecture)">Blackwell (microarchitecture) - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Hopper_(microarchitecture)">Hopper (microarchitecture) - Wikipedia</a></li>
<li><a href="https://www.nvidia.com/en-us/data-center/dgx-platform/">DGX Platform: Built for Enterprise AI | NVIDIA</a></li>

</ul>
</details>

**Tags**: `#NVIDIA`, `#earnings`, `#AI infrastructure`, `#semiconductors`, `#data center`

---