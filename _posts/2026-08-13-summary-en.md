---
layout: default
title: "Horizon Summary: 2026-08-13 (EN)"
date: 2026-08-13
lang: en
---

> From 51 items, 4 important content pieces were selected

---

1. [Google Announces Gemini 3.7 Flash for Coding and Agents](#item-1) ⭐️ 8.0/10
2. [Christopher Domas Releases DRAM Exploit Project 'Spaghettifying DRAM'](#item-2) ⭐️ 8.0/10
3. [rsync 3.5.0 Released with 33 Security Fixes](#item-3) ⭐️ 8.0/10
4. [🤖 Google 发布 Gemini 3.6 Flash，并透露 Gemini 4 已启动预训练  Google 发布 Gemini 3.6 Flash，称新模](#item-4) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Google Announces Gemini 3.7 Flash for Coding and Agents](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-3-7-flash/) ⭐️ 8.0/10

Google introduced Gemini 3.7 Flash, its most intelligent workhorse model for coding and agentic tasks, just three weeks after Gemini 3.6 Flash. The model features introductory pricing that will double on December 31, 2026. This release strengthens Google's position in the competitive LLM market, offering improved coding and agent capabilities at a lower cost tier. The rapid release cycle and pricing strategy signal aggressive competition with models like OpenAI's Opus and Anthropic's Luna. Gemini 3.7 Flash delivers substantial improvements in agentic coding and knowledge work, with benchmarks covering reasoning, multimodal capabilities, and long-context processing. The model can generate fully playable 3D games from text prompts when combined with other tools.

hackernews · thisisauserid · Aug 13, 17:23 · [Discussion](https://news.ycombinator.com/item?id=49289112)

**Background**: The Gemini Flash series is Google's cost-effective model line designed for high-volume, low-latency applications, while Pro models target more complex reasoning tasks. Flash models typically offer faster response times and lower costs compared to Pro variants, making them suitable for production workloads.

<details><summary>References</summary>
<ul>
<li><a href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-3-7-flash/">Gemini 3.7 Flash: our most intelligent workhorse model</a></li>

</ul>
</details>

**Discussion**: Community members praised Gemini's vision capabilities but noted Opus remains best-in-class for image-to-HTML tasks. There were concerns about the pricing strategy, with the introductory rate doubling in just five months, and comparisons showed Luna still outperforms on benchmarks like DeepSWE 1.1.

**Tags**: `#AI`, `#LLM`, `#Google Gemini`, `#Model Release`, `#Pricing`

---

<a id="item-2"></a>
## [Christopher Domas Releases DRAM Exploit Project 'Spaghettifying DRAM'](https://github.com/xoreaxeaxeax/skitter-creek-bath-salts) ⭐️ 8.0/10

Security researcher Christopher Domas has released a proof-of-concept tool named skitter-creek-bath-salts that exploits AMD processor memory controller architecture to scramble DRAM address mappings, bypassing hardware security mechanisms. This research demonstrates a new attack surface on AMD hardware, with implications for console security and low-level system access, as highlighted by community discussions about potential impacts on Xbox and PlayStation. The exploit currently works on AMD Jaguar architecture from 2013, with notes indicating Zen 3 has a different base address for memory controller registers, and the attack surface is limited to specific AMD processor families.

hackernews · matt_d · Aug 13, 14:17 · [Discussion](https://news.ycombinator.com/item?id=49286341)

**Background**: Dynamic Random-Access Memory (DRAM) is the primary volatile memory in computers, and its increasing complexity has expanded attack surfaces. The Rowhammer effect, discovered in 2014, involves repetitive DRAM row access causing bit flips in neighboring rows, leading to security vulnerabilities. Modern DRAM access often requires proprietary firmware, making low-level manipulation more challenging but also more impactful when exploited.

<details><summary>References</summary>
<ul>
<li><a href="https://news.linxi.com.au/news/amd-hardware-vulnerability-exposed-by-dram-address-scrambling-research">AMD DRAM Scrambling Exploit Bypasses Security Fences | Linxi News</a></li>
<li><a href="https://github.com/xoreaxeaxeax">xoreaxeaxeax (domas) · GitHub</a></li>
<li><a href="https://en.wikipedia.org/wiki/Row_hammer">Row hammer - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Community sentiment is enthusiastic about the research, with anticipation for Domas's Black Hat talk. Discussions highlight the growing complexity of DRAM and its expanded attack surface, while also raising questions about compatibility with newer AMD processors beyond the tested Jaguar architecture.

**Tags**: `#hardware-security`, `#DRAM`, `#exploit-research`, `#systems-security`, `#Black-Hat`

---

<a id="item-3"></a>
## [rsync 3.5.0 Released with 33 Security Fixes](https://lwn.net/Articles/1088759/) ⭐️ 8.0/10

rsync 3.5.0 has been released with 33 security fixes addressing path handling and daemon protocol vulnerabilities, discovered through a focused audit, daemon-protocol fuzzing, and external researcher reports. The release also includes several robustness hardenings, with each fix accompanied by a regression test. rsync is a widely-used file synchronization utility, and this release represents a major security hardening effort. The 33 fixes address vulnerabilities that could affect system administrators and security-conscious engineers who rely on rsync for file transfers across networks. CVE IDs were assigned by VulnCheck as the CVE Numbering Authority (CNA), and many vulnerabilities have much narrower version ranges than simply "everything before 3.5.0." Every fix ships with a regression test in the test suite that fails on the unfixed tree, ensuring the vulnerabilities are properly addressed.

rss · LWN.net · Aug 13, 13:47

**Background**: rsync (remote sync) is a utility for transferring and synchronizing files between computers over a network, using a delta-transfer algorithm to efficiently detect and transfer only file differences rather than entire files. The rsync daemon protocol allows rsync to operate in server mode, enabling centralized file repositories. Fuzzing is an automated software testing technique that provides invalid, unexpected, or random data as inputs to discover crashes, memory leaks, or other vulnerabilities.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Rsync">rsync - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Fuzzing">Fuzzing - Wikipedia</a></li>
<li><a href="https://www.cve.org/ResourcesSupport/AllResources/CNARules">CVE Numbering Authority (CNA) Operational Rules</a></li>

</ul>
</details>

**Tags**: `#rsync`, `#security`, `#system-administration`, `#open-source`

---

<a id="item-4"></a>
## [🤖 Google 发布 Gemini 3.6 Flash，并透露 Gemini 4 已启动预训练  Google 发布 Gemini 3.6 Flash，称新模](https://t.me/zaihuapd/43177) ⭐️ 8.0/10

Google released Gemini 3.6 Flash with improved efficiency and capabilities, while revealing that Gemini 4 has already begun pre-training.

telegram · zaihuapd · Aug 13, 17:32

**Tags**: `#AI`, `#Google`, `#Gemini`, `#LLM`, `#Model Release`

---