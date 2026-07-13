---
layout: default
title: "Horizon Summary: 2026-07-13 (EN)"
date: 2026-07-13
lang: en
---

> From 47 items, 6 important content pieces were selected

---

1. [LAPD Lets Flock Surveillance Contract Expire Over Privacy Concerns](#item-1) ⭐️ 8.0/10
2. [BPF Technique Shields Kernels from Exploits at 2026 Summit](#item-2) ⭐️ 8.0/10
3. [CISA Postmortem Reveals Six-Month GitHub Credential Leak](#item-3) ⭐️ 8.0/10
4. [Advancements in Epigenetic Editing for Gene Expression Control](#item-4) ⭐️ 8.0/10
5. [First True Sugar Molecule Found in Deep Space](#item-5) ⭐️ 8.0/10
6. [Chain of Thought Scaling Trap: Rise of Latent Reasoning](#item-6) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [LAPD Lets Flock Surveillance Contract Expire Over Privacy Concerns](https://techcrunch.com/2026/07/13/lapd-lets-contract-with-surveillance-giant-flock-expire-citing-serious-concerns-over-civil-liberties-and-privacy/) ⭐️ 8.0/10

The Los Angeles Police Department has allowed its contract with surveillance technology provider Flock to expire, citing serious concerns regarding civil liberties and privacy. This decision marks a significant policy shift for the agency amidst growing scrutiny of automated surveillance infrastructure. This move highlights the tension between law enforcement efficiency and individual privacy rights, potentially influencing other municipal agencies to reevaluate their reliance on third-party surveillance vendors. It raises critical questions about data ownership and the long-term implications of vendor lock-in in public safety networks. A key technical caveat is that Flock retains ownership of the camera hardware and poles, meaning the surveillance infrastructure continues to operate and harvest data even after the LAPD contract ends. This structure allows Flock to potentially sell or share the collected data with other entities such as the CHP, LASD, or FBI, creating a persistent data collection network independent of local police control.

hackernews · forks · Jul 13, 15:11 · [Discussion](https://news.ycombinator.com/item?id=48893947)

**Background**: Flock Safety is a prominent provider of automated license plate reader (ALPR) systems used by law enforcement agencies across the United States. These systems typically involve private companies installing and maintaining cameras on public poles, which then feed data into centralized databases accessible to police. The business model often involves long-term contracts where the vendor retains asset ownership, leading to debates over whether these systems create permanent surveillance infrastructures that outlast political or administrative changes.

**Discussion**: Community comments express deep skepticism about the practical impact of the contract expiration, noting that Flock's ownership of the hardware means data harvesting continues regardless of LAPD's involvement. Users highlight the 'vendor lock-in' risk, arguing that the system is designed to be resilient to political pressure, while others question the utility of surveillance given that many suspects are already known to police.

**Tags**: `#Privacy`, `#Surveillance`, `#Civil Liberties`, `#Tech Policy`

---

<a id="item-2"></a>
## [BPF Technique Shields Kernels from Exploits at 2026 Summit](https://lwn.net/Articles/1081546/) ⭐️ 8.0/10

John Fastabend presented a BPF-based technique at the 2026 LSFMMBPF Summit designed to shield running kernels against exploits. This approach aims to address Cisco's specific challenges in deploying security patches across its vast array of custom kernel devices. This technique could substantially reduce the time required to respond to kernel vulnerabilities, offering a faster alternative to traditional patching. It addresses significant security deployment challenges faced by organizations managing diverse hardware and software environments. While promising, the method will not be fully effective unless more hooks are added to the kernel to allow BPF programs to intercept relevant events. The presentation highlights the potential of eBPF for runtime security mitigation rather than just static patching.

rss · LWN.net · Jul 13, 14:14

**Background**: BPF (Berkeley Packet Filter) is a technology originally designed for network packet filtering that has evolved into a powerful framework for running sandboxed programs within the Linux kernel. It allows developers to attach small programs to various kernel hooks for monitoring, tracing, and security purposes without modifying kernel source code. This evolution enables dynamic security measures that can adapt to threats in real-time.

**Tags**: `#BPF`, `#Kernel Security`, `#Linux`, `#Exploit Mitigation`

---

<a id="item-3"></a>
## [CISA Postmortem Reveals Six-Month GitHub Credential Leak](https://krebsonsecurity.com/2026/07/lessons-learned-from-cisas-recent-github-leak/) ⭐️ 8.0/10

CISA released a postmortem detailing how contractor credentials, including AWS GovCloud keys, were exposed in a public GitHub repository for nearly six months before discovery. This incident highlights critical gaps in initial response protocols and serves as a vital lesson for security teams regarding credential management and monitoring. The leak involved dozens of internal CISA credentials and persisted for almost half a year, emphasizing the severity of the oversight in detecting unauthorized public access.

rss · Krebs on Security · Jul 13, 15:03

**Background**: CISA is the U.S. federal agency responsible for strengthening the cybersecurity of critical infrastructure. AWS GovCloud is an isolated AWS region designed to handle sensitive data and regulated workloads, making the exposure of its keys particularly dangerous.

**Tags**: `#Cybersecurity`, `#Incident Response`, `#Cloud Security`, `#AWS GovCloud`, `#Best Practices`

---

<a id="item-4"></a>
## [Advancements in Epigenetic Editing for Gene Expression Control](https://www.nature.com/articles/d41586-026-02151-x) ⭐️ 8.0/10

Researchers are advancing techniques to rewrite chemical tags on DNA and chromatin, allowing for precise tuning of gene expression without altering the underlying DNA sequence. This progress represents a significant shift towards precision medicine by enabling the modulation of disease-related genes through reversible epigenetic changes rather than permanent genetic mutations. The focus is on modifying histone marks and DNA methylation patterns, which are dynamic processes maintained by cellular mechanisms, requiring careful balance to avoid disrupting normal epigenetic states.

rss · Nature · Jul 13, 00:00

**Background**: Epigenetics refers to heritable changes in gene function that do not involve alterations to the underlying DNA sequence. These changes are often mediated by chemical modifications such as DNA methylation and histone acetylation, which influence how tightly DNA is packed and thus whether genes are accessible for transcription. Unlike traditional gene editing which cuts DNA, epigenetic editing aims to switch genes on or off by modifying these chemical tags.

<details><summary>References</summary>
<ul>
<li><a href="https://www.frontiersin.org/journals/medicine/articles/10.3389/fmed.2025.1613722/full">Frontiers | Precision scalpels for the epigenome: next-gen editing tools...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Chromatin_remodeling">Chromatin remodeling - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#Epigenetics`, `#Gene Editing`, `#Biotechnology`, `#Genomics`

---

<a id="item-5"></a>
## [First True Sugar Molecule Found in Deep Space](https://www.nature.com/articles/d41586-026-02173-5) ⭐️ 8.0/10

Scientists have identified erythrulose, a four-carbon sugar, in interstellar space, marking the first detection of such a complex sugar molecule beyond our solar system. This discovery was reported in Nature on July 13, 2026. This finding provides crucial evidence that the building blocks of life, specifically sugars essential for RNA and DNA, can form in space. It supports the hypothesis that early Earth may have received these complex organic molecules from cosmic sources, aiding the origins of life. Erythrulose is a ketotetrose with the molecular formula C₄H₈O₄, making it the most complex sugar detected in interstellar environments to date. Its identification highlights the rich organic chemistry present in star-forming regions.

rss · Nature · Jul 13, 00:00

**Background**: Over 260 different molecular species, including alcohols and acids, have been detected in interstellar space, suggesting that complex organic chemistry is widespread in the universe. Sugars are fundamental to life on Earth as they form the backbone of genetic material like RNA and DNA and serve as energy sources. Previous detections often involved simpler molecules, making the identification of erythrulose a significant step toward understanding how prebiotic ingredients are distributed across the cosmos.

<details><summary>References</summary>
<ul>
<li><a href="https://www.sciencealert.com/scientists-find-the-first-true-sugar-ever-detected-in-interstellar-space">Scientists Find The First True Sugar Ever Detected in... : ScienceAlert</a></li>
<li><a href="https://grokipedia.com/page/Erythrulose">Erythrulose</a></li>

</ul>
</details>

**Tags**: `#Astrobiology`, `#Chemistry`, `#Space Science`, `#Origins of Life`

---

<a id="item-6"></a>
## [Chain of Thought Scaling Trap: Rise of Latent Reasoning](https://www.reddit.com/r/MachineLearning/comments/1uviru5/chain_of_thought_is_a_scaling_trap_the_next_wave/) ⭐️ 8.0/10

The post argues that Chain of Thought is becoming a scaling trap due to faithfulness and cost issues, advocating for a shift toward latent reasoning models like Coconut and HRM. It highlights how these models process internal hidden states rather than serializing reasoning into text, while questioning the role of Bayesian Decision Heuristics in this transition. This shift addresses critical bottlenecks in LLM reasoning by reducing latency and computational costs associated with autoregressive text generation. It fundamentally changes how we approach model interpretability, moving from reading 'inner monologues' to auditing structured plans and verified outputs. Latent reasoning frameworks like Coconut allow for continuous hidden state processing, enabling breadth-first search capabilities that text-based Chain of Thought cannot efficiently support. Models like HRM separate slower planning from faster recursive execution, while RecursiveMAS passes latent embeddings between agents instead of long text messages.

reddit · r/MachineLearning · /u/meowsterpieces · Jul 13, 17:50

**Background**: Chain of Thought (CoT) prompting encourages large language models to generate intermediate reasoning steps as text before producing a final answer. While useful, this method forces serialization of complex computations into tokens, which inflates context window usage and increases inference costs. Recent research explores latent space reasoning, where models perform computation in continuous vector spaces without generating readable text until the final output stage.

<details><summary>References</summary>
<ul>
<li><a href="https://www.linkedin.com/pulse/unlocking-smarter-ai-my-take-coconut-framework-latent-ragunathan-o43me">Unlocking Smarter AI : My Take on the “ Coconut ” Framework for...</a></li>
<li><a href="https://github.com/sapientinc/HRM">GitHub - sapientinc/HRM: Hierarchical Reasoning Model Official Release · GitHub</a></li>
<li><a href="https://recursivemas.github.io/">RecursiveMAS</a></li>

</ul>
</details>

**Tags**: `#LLM Reasoning`, `#Chain of Thought`, `#Latent Space`, `#AI Architecture`, `#Model Scaling`

---