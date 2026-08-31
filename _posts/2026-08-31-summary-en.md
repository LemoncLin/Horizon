---
layout: default
title: "Horizon Summary: 2026-08-31 (EN)"
date: 2026-08-31
lang: en
---

> From 61 items, 4 important content pieces were selected

---

1. [Stunning Percolation Proof Solves Decades-Old Phase Transition Puzzle](#item-1) ⭐️ 9.0/10
2. [Apple Announces CEO Succession: Cook Steps Down, Ternus Takes Over](#item-2) ⭐️ 9.0/10
3. [Google Removes MV2 Extensions from Chrome Web Store](#item-3) ⭐️ 8.0/10
4. [Sliding Window Attention Outperforms Linear Attention on Long-Context Reasoning](#item-4) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Stunning Percolation Proof Solves Decades-Old Phase Transition Puzzle](https://www.quantamagazine.org/stunning-percolation-proof-solves-decades-old-puzzle-about-phase-transitions-20260831/) ⭐️ 9.0/10

Mathematicians have proven that a broad class of networks undergo abrupt behavioral shifts past a critical threshold, solving a long-standing puzzle about phase transitions in percolation theory. This breakthrough bridges mathematics and statistical physics, offering rigorous confirmation of a phenomenon that has been observed empirically across networks, materials science, and complex systems for decades. The proof applies to a broad class of networks rather than a single specific model, which is what makes the result particularly powerful and generalizable across different types of random systems.

rss · Quanta Magazine · Aug 31, 14:24

**Background**: Percolation theory studies how connectivity emerges in random systems, such as when fluid flows through a porous material. The critical threshold is the point at which a system abruptly transitions from having only small, disconnected clusters to forming a single connected pathway spanning the entire system — a phase transition. This concept is fundamental to understanding phenomena ranging from virus spread in networks to conductivity in composite materials.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Percolation_threshold">Percolation threshold - Wikipedia</a></li>
<li><a href="https://www.wikiwand.com/en/articles/Percolation_theory">Percolation theory - Wikiwand</a></li>

</ul>
</details>

**Tags**: `#mathematics`, `#percolation theory`, `#phase transitions`, `#network theory`, `#statistical physics`

---

<a id="item-2"></a>
## [Apple Announces CEO Succession: Cook Steps Down, Ternus Takes Over](https://t.me/zaihuapd/43516) ⭐️ 9.0/10

Apple announced that CEO Tim Cook will step down on September 1, 2026, with hardware engineering senior vice president John Ternus succeeding him. Cook will transition to the role of executive chairman, while current chairman Arthur Levinson will become chief independent director on the same date. This marks a paradigm-level leadership transition at one of the world's most influential tech companies, with significant implications for Apple's product strategy and corporate direction. As the first CEO succession since Steve Jobs, it signals a new era for the company that Cook has led for over 15 years. Cook will remain CEO through the summer to complete a smooth transition with Ternus. The board unanimously approved the arrangement, and Ternus, who joined Apple in 2001, has overseen iPhone, Mac, iPad, and AirPods hardware development since entering the executive team in 2021.

telegram · zaihuapd · Aug 31, 10:21

**Background**: An executive chairman typically oversees board operations and strategic guidance while the CEO manages day-to-day business. A chief independent director serves as the lead voice of independent board members, providing oversight and checks on management. Apple has been led by CEO Tim Cook since 2011, following Steve Jobs' passing, making this the company's first CEO succession in over a decade.

<details><summary>References</summary>
<ul>
<li><a href="https://techtroveblog.work/tech/mirella/apple-executive-chairman-01g2/">techtroveblog.work/tech/mirella/apple-executive-chairman-01g2</a></li>
<li><a href="https://www.antutu.com/doc/137598.htm">苹 果 为Tim Cook举办欢送会 Ternus准备接棒_热点资讯_安兔兔</a></li>

</ul>
</details>

**Tags**: `#Apple`, `#CEO Succession`, `#Tech Leadership`, `#Industry News`

---

<a id="item-3"></a>
## [Google Removes MV2 Extensions from Chrome Web Store](https://webiterate.dev/google-removed-extensions-ublock-origin-108/) ⭐️ 8.0/10

Google has removed Manifest V2 extensions from the Chrome Web Store, including the popular ad blocker uBlock Origin. This follows Google's earlier decision to stop accepting new MV2 extensions in January 2022 and phase out the platform by June 2024. This policy change significantly impacts users who rely on ad blockers and privacy-focused extensions, as MV3 imposes stricter limitations on content blocking capabilities. It also raises broader concerns about Google's unilateral control over the browser ecosystem and the internet's information flow. Manifest V3 replaces the blocking request API with a more limited declarativeNetRequest API, which restricts the number of rules extensions can use and prevents real-time content filtering. Firefox continues to support both MV2 and MV3 with no immediate deprecation plans.

hackernews · twapi · Aug 31, 21:10 · [Discussion](https://news.ycombinator.com/item?id=49514878)

**Background**: Browser extensions are small software programs that enhance web browsers with additional features like ad blocking, privacy protection, and productivity tools. Manifest V2 was the original extension architecture that allowed extensions to intercept and modify web requests in real-time, giving ad blockers like uBlock Origin their full power. Manifest V3, introduced by Google, represents a more restricted architecture designed for improved security and performance but at the cost of extension capabilities.

<details><summary>References</summary>
<ul>
<li><a href="https://medium.com/@idmossab/nifest-v2-vs-manifest-v3-chrome-extensions-what-changed-and-why-2025-was-the-turning-point-53b031b70fc6">Manifest V2 vs Manifest V3 (Chrome Extensions): What ... - Medium</a></li>

</ul>
</details>

**Discussion**: The community is largely critical of Google's decision, with many users switching to Firefox as an alternative. Users express concern about Google's unilateral control over the internet, and several note that uBlock Origin works better in Firefox anyway. Some also highlight that ad blocking has become a safety issue for less tech-savvy users who may fall for malicious ads.

**Tags**: `#Chrome`, `#Browser Extensions`, `#Ad Blocking`, `#Google`, `#Privacy`

---

<a id="item-4"></a>
## [Sliding Window Attention Outperforms Linear Attention on Long-Context Reasoning](https://www.reddit.com/r/MachineLearning/comments/1w3j1vw/slidingwindow_attention_beats_linear_on/) ⭐️ 8.0/10

A new arXiv preprint by Alexia Jolicoeur-Martineau and colleagues claims that sliding window attention with sinks achieves 2 to 10 times higher performance than linear attention variants on long-context reasoning benchmarks like Needle-in-a-Haystack and BABILong, without requiring post-training. This finding challenges the current industry trend of investing post-training compute into linear attention models, suggesting that simpler sliding window attention may be a more effective approach for long-context reasoning and could redirect research and development strategies in the LLM architecture space. The paper argues that linear attention research has been improperly compared to inadequate baselines, and that linear attention variants likely require training from scratch or extensive post-training to even match sliding window attention's performance on long-context tasks.

reddit · r/MachineLearning · /u/Justgototheeffinmoon · Aug 31, 16:35

**Background**: Standard self-attention in transformers has quadratic computational and memory complexity with respect to sequence length, making it impractical for long contexts. Linear attention variants like Mamba, RetNet, and GLA were developed to reduce this complexity to linear time, but they often sacrifice performance on long-context reasoning tasks. Sliding window attention addresses this by allowing each token to attend only to nearby neighbors within a fixed window, with sink tokens that attend to all positions to maintain global information flow.

<details><summary>References</summary>
<ul>
<li><a href="https://www.emergentmind.com/topics/sliding-window-self-attention">Sliding-Window Self-Attention</a></li>
<li><a href="https://magazine.sebastianraschka.com/p/visual-attention-variants">A Visual Guide to Attention Variants in Modern LLMs</a></li>
<li><a href="https://github.com/booydar/babilong">GitHub - booydar/babilong: BABILong is a benchmark for LLM evaluation using the needle-in-a-haystack approach. · GitHub</a></li>

</ul>
</details>

**Discussion**: No specific community comments were provided in the news item, but the post received an 8.0/10 score on Reddit with active engagement, indicating significant interest in this potentially impactful result that could redirect post-training compute strategies.

**Tags**: `#machine learning`, `#attention mechanisms`, `#long-context reasoning`, `#LLM architecture`, `#research`

---