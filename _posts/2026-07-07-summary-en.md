---
layout: default
title: "Horizon Summary: 2026-07-07 (EN)"
date: 2026-07-07
lang: en
---

> From 82 items, 12 important content pieces were selected

---

1. [Tencent Releases Hy3, a 295B Parameter Open-Source MoE Model](#item-1) ⭐️ 9.0/10
2. [Anthropic Releases Claude Sonnet 5 with Strong Agent Capabilities](#item-2) ⭐️ 9.0/10
3. [Januscape: 16-Year KVM Escape Vulnerability Now Public](#item-3) ⭐️ 9.0/10
4. [商务部拟限制国产顶尖 AI 模型对外出口](#item-4) ⭐️ 9.0/10
5. [Chat Control passed first round in EU Parliament](#item-5) ⭐️ 8.0/10
6. [Microsoft fire idTech team at Id software](#item-6) ⭐️ 8.0/10
7. [Linux Kernel Advances: Faster RCU and Lockless kmalloc_nolock](#item-7) ⭐️ 8.0/10
8. [MIRA: 5B-Parameter Multiplayer World Model Trained on Rocket League](#item-8) ⭐️ 8.0/10
9. [New Defense Constrains Model Updates to Trusted LoRA Subspaces](#item-9) ⭐️ 8.0/10
10. [Razer Certifies First Linux Laptop, the Blade 18](#item-10) ⭐️ 8.0/10
11. [NVIDIA Blackwell Wafers Made in US, Packaged in Taiwan](#item-11) ⭐️ 8.0/10
12. [California and NY Mandate Gun-Blocking Software on 3D Printers](#item-12) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Tencent Releases Hy3, a 295B Parameter Open-Source MoE Model](https://simonwillison.net/2026/Jul/6/hy3/#atom-everything) ⭐️ 9.0/10

Tencent has released Hy3, a 295B-parameter Mixture-of-Experts (MoE) language model under the Apache 2.0 license. The model features 21B active parameters, supports a 256K context window, and claims to rival flagship open-source models in performance. This release significantly expands the high-performance open-source LLM ecosystem by providing a powerful, commercially friendly model. It demonstrates that Chinese developers are achieving parity with top-tier global models through efficient MoE architectures. The full model weighs 598GB, while an FP8 quantized version is available at 300GB to reduce memory requirements. Hy3 utilizes a sparse MoE structure where only a subset of parameters is activated per token, optimizing inference efficiency.

rss · Simon Willison · Jul 6, 23:57

**Background**: Mixture-of-Experts (MoE) is an architecture that scales model size without proportionally increasing computational cost during inference by activating only a small subset of 'experts' for each input. FP8 quantization reduces the precision of model weights from standard 32-bit floats to 8-bit floats, allowing for faster processing and lower memory usage with minimal accuracy loss. These techniques are critical for making large-scale models accessible to researchers and developers without massive hardware budgets.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Mixture_of_experts">Mixture of experts - Wikipedia</a></li>
<li><a href="https://www.ibm.com/think/topics/mixture-of-experts">What is mixture of experts? | IBM</a></li>
<li><a href="https://docs.vllm.ai/en/v0.5.4/quantization/fp8.html">FP8 — vLLM</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#Open Source`, `#Tencent`, `#MoE`, `#AI Models`

---

<a id="item-2"></a>
## [Anthropic Releases Claude Sonnet 5 with Strong Agent Capabilities](https://t.me/zaihuapd/42404) ⭐️ 9.0/10

Anthropic has released Claude Sonnet 5, positioning it as their most capable Sonnet model for agentic tasks such as planning and tool use. The model outperforms Sonnet 4.6 in reasoning and coding while approaching the performance of Opus 4.8 at a significantly lower cost. This release bridges the performance gap between the mid-tier Sonnet and flagship Opus models, making advanced autonomous agent workflows more accessible. By defaulting Sonnet 5 to Free and Pro tiers, Anthropic democratizes access to high-reliability agentic capabilities for a broader user base. Claude Sonnet 5 is now available across all subscription tiers and serves as the default model for Free and Pro users. Safety assessments indicate it exhibits fewer undesirable behaviors in agentic contexts compared to its predecessor, enhancing reliability for automated tasks.

telegram · zaihuapd · Jul 7, 09:02

**Background**: In the LLM ecosystem, models are often categorized by capability and cost, with 'Sonnet' representing a balanced tier for everyday tasks and 'Opus' serving as the high-end option for complex reasoning. Agentic capabilities refer to an AI's ability to autonomously plan, execute multi-step workflows, and utilize external tools like browsers or terminals to achieve goals without constant human intervention.

<details><summary>References</summary>
<ul>
<li><a href="https://www.anthropic.com/news/claude-sonnet-5">Introducing Claude Sonnet 5 \ Anthropic</a></li>
<li><a href="https://www.marktechpost.com/2026/06/30/anthropic-claude-sonnet-5-vs-sonnet-4-6-vs-opus-4-8-agentic-coding-benchmarks-api-pricing-and-cost-performance-tradeoffs-compared/">Anthropic Claude Sonnet 5 vs Sonnet 4.6 vs Opus 4.8: Agentic Coding Benchmarks, API Pricing, and Cost-Performance Tradeoffs Compared - MarkTechPost</a></li>

</ul>
</details>

**Tags**: `#AI`, `#LLM`, `#Anthropic`, `#Model Release`, `#Agent`

---

<a id="item-3"></a>
## [Januscape: 16-Year KVM Escape Vulnerability Now Public](https://github.com/V4bel/Januscape) ⭐️ 9.0/10

Researchers have disclosed Januscape (CVE-2026-53359), a critical KVM/x86 virtual machine escape vulnerability affecting both Intel and AMD platforms since 2010. A public proof-of-concept demonstrates how a use-after-free defect in the shadow MMU allows guest VMs to compromise the host kernel. This vulnerability threatens the isolation boundaries of multi-tenant cloud infrastructure, as it enables privilege escalation from a guest VM to the host root level. Its long-standing presence means millions of servers running Linux kernels prior to June 2026 are potentially exposed to remote code execution attacks. The flaw originates from a use-after-free error in the shadow MMU simulation, allowing guests to corrupt shadow pages without external interaction. The vulnerability has been present for approximately 16 years and was previously utilized as a zero-day exploit in Google's kvmCTF competition.

telegram · zaihuapd · Jul 7, 10:14

**Background**: A virtual machine escape occurs when malicious code breaks out of the guest OS to interact directly with the host hypervisor, bypassing security isolation. The KVM shadow MMU is a software mechanism used to manage memory translation for guests, particularly when hardware-assisted paging like EPT or NPT is unavailable or insufficient. A use-after-free vulnerability allows attackers to access memory that has already been freed, leading to arbitrary code execution or system crashes.

<details><summary>References</summary>
<ul>
<li><a href="https://docs.kernel.org/virt/kvm/x86/mmu.html">The x86 kvm shadow mmu — The Linux Kernel documentation</a></li>
<li><a href="https://en.wikipedia.org/wiki/Virtual_machine_escape">Virtual machine escape - Wikipedia</a></li>
<li><a href="https://owasp.org/www-community/vulnerabilities/Using_freed_memory">Using freed memory | OWASP Foundation</a></li>

</ul>
</details>

**Tags**: `#Security`, `#Virtualization`, `#KVM`, `#Vulnerability`, `#Cloud Infrastructure`

---

<a id="item-4"></a>
## [商务部拟限制国产顶尖 AI 模型对外出口](https://www.reuters.com/world/beijing-is-looking-curbing-overseas-access-chinas-top-ai-models-sources-say-2026-07-07/) ⭐️ 9.0/10

China's Ministry of Commerce is reportedly considering restricting the overseas access and export of top-tier domestic AI models, including unreleased ones, while potentially classifying AI tech leakage as a national security crime.

telegram · zaihuapd · Jul 7, 11:42

**Tags**: `#AI Policy`, `#Geopolitics`, `#Export Controls`, `#National Security`, `#Industry Regulation`

---

<a id="item-5"></a>
## [Chat Control passed first round in EU Parliament](https://www.heise.de/en/news/Showdown-in-Strasbourg-The-unexpected-return-of-Chat-Control-1-0-11356680.html) ⭐️ 8.0/10

EU Parliament's 'Chat Control' proposal advances after passing its first reading, sparking debate over legislative strategy and democratic processes.

hackernews · miroljub · Jul 7, 15:16 · [Discussion](https://news.ycombinator.com/item?id=48819008)

**Tags**: `#EU Regulation`, `#Privacy`, `#Legislation`, `#Policy`

---

<a id="item-6"></a>
## [Microsoft fire idTech team at Id software](https://gamefromscratch.com/microsoft-fire-idtech-team-at-id-software/) ⭐️ 8.0/10

Microsoft is dissolving Id Software's internal engine team, signaling a move towards standardized tools like Unreal Engine and prompting intense discussion on corporate consolidation in the gaming industry.

hackernews · bauc · Jul 7, 15:33 · [Discussion](https://news.ycombinator.com/item?id=48819244)

**Tags**: `#Gaming Industry`, `#Corporate Strategy`, `#Id Software`, `#Unreal Engine`, `#Microsoft`

---

<a id="item-7"></a>
## [Linux Kernel Advances: Faster RCU and Lockless kmalloc_nolock](https://lwn.net/Articles/1081009/) ⭐️ 8.0/10

Puranjay Mohan presented work on optimizing Read-Copy-Update (RCU) performance at the 2026 LSFMMBPF summit. This complements recent developments in the kernel, such as the new kmalloc_nolock() function, which enables lockless memory allocation from any context. These optimizations significantly reduce locking overhead in the Linux kernel, enhancing system scalability and concurrency. By allowing lockless operations, the kernel can handle higher loads more efficiently, benefiting performance-critical applications and systems research. The kmalloc_nolock() function interacts directly with the RCU subsystem to ensure safe memory management without locks. Puranjay Mohan's RCU improvements provide the necessary context for understanding how these lockless allocations maintain data integrity.

rss · LWN.net · Jul 7, 13:39

**Background**: Read-Copy-Update (RCU) is a synchronization mechanism in the Linux kernel designed to improve performance in read-heavy workloads by avoiding traditional locking. The kmalloc function is the primary interface for allocating kernel memory, and traditionally, it requires holding locks to prevent race conditions. Recent efforts aim to make these critical paths lockless to maximize throughput.

**Tags**: `#Linux Kernel`, `#Performance Optimization`, `#Concurrency`, `#Systems Programming`

---

<a id="item-8"></a>
## [MIRA: 5B-Parameter Multiplayer World Model Trained on Rocket League](https://www.reddit.com/r/MachineLearning/comments/1upofuw/mira_multiplayer_interactive_world_models_trained/) ⭐️ 8.0/10

General Intuition, Kyutai, and Epic Games have released MIRA, a 5-billion-parameter multiplayer interactive world model trained on 10,000 hours of synthetic Rocket League data. The team also provided a playable online demo, a technical report, and a 1,000-hour dataset of four-player gameplay. This release demonstrates the feasibility of training large-scale interactive models on synthetic multi-agent data, achieving real-time performance on a single B200 GPU. It offers valuable resources for researchers exploring reinforcement learning and world modeling in complex, dynamic environments. The model supports four players simultaneously at 20 frames per second, showcasing efficient inference capabilities. Key resources include the GitHub repository, the official website for the demo and paper, and the newly released gameplay dataset.

reddit · r/MachineLearning · /u/MasterScrat · Jul 7, 07:59

**Background**: World models are AI systems that learn to predict how an environment changes over time based on actions taken within it. Training such models on multiplayer games like Rocket League requires handling complex interactions between multiple agents, which is significantly more challenging than single-agent scenarios. This project highlights progress in making these models computationally efficient enough for real-time interaction.

**Tags**: `#World Models`, `#Reinforcement Learning`, `#Multi-Agent Systems`, `#AI Research`, `#Synthetic Data`

---

<a id="item-9"></a>
## [New Defense Constrains Model Updates to Trusted LoRA Subspaces](https://www.reddit.com/r/MachineLearning/comments/1uq68li/what_if_a_model_could_only_learn_what_trusted/) ⭐️ 8.0/10

A new paper proposes a defense against fine-tuning poisoning by restricting model updates to a subspace defined by trusted LoRA adapters. This approach prevents the model from learning malicious behaviors that lie outside these trusted directions. This method offers a geometric alternative to traditional detection-based defenses, potentially securing models that adapt to user data or external sources. It ensures that while useful adaptation continues, harmful backdoors remain geometrically unreachable. The authors tested this approach on 196 public LoRA adapters, including those designed to bypass such defenses. Results showed a sharp drop in attack success rates while preserving useful adaptation capabilities on covered tasks.

reddit · r/MachineLearning · /u/Bright_Warning_8406 · Jul 7, 20:00

**Background**: Fine-tuning poisoning occurs when malicious actors inject harmful data into training sets to alter model behavior. Low-Rank Adaptation (LoRA) is a popular technique for efficiently fine-tuning large language models by updating only a small number of parameters. By constraining updates to a subspace of known good adapters, this method limits the model's ability to adopt arbitrary new weights.

**Tags**: `#Machine Learning Security`, `#LoRA`, `#Poisoning Defense`, `#Fine-tuning`, `#AI Safety`

---

<a id="item-10"></a>
## [Razer Certifies First Linux Laptop, the Blade 18](https://www.reddit.com/r/linux/comments/1uq3xwm/razer_certifying_their_first_laptop_for_linux/) ⭐️ 8.0/10

Razer has officially certified the Blade 18 laptop for native Linux support, marking the company's first major hardware certification for the operating system. This move provides users with guaranteed driver stability and out-of-the-box compatibility for Linux enthusiasts. This certification represents a significant milestone for the Linux gaming ecosystem, as major hardware vendors traditionally prioritize Windows compatibility. It signals growing mainstream acceptance of Linux in the consumer gaming market and encourages other manufacturers to consider similar support. The certification specifically applies to the Razer Blade 18 model, ensuring that core components like graphics and audio drivers function correctly on Linux distributions. This official backing reduces the technical friction typically associated with installing gaming laptops on non-Windows operating systems.

reddit · r/linux · /u/RhubarbSimilar1683 · Jul 7, 18:41

**Background**: Linux has historically struggled with hardware compatibility in the gaming sector due to fragmented driver support and lack of official vendor endorsement. Most gaming laptops are optimized exclusively for Windows, leaving Linux users to rely on community-driven patches or manual configuration. Official certifications from major brands help bridge this gap by providing stable, tested software stacks.

**Tags**: `#Linux`, `#Hardware`, `#Gaming`, `#Driver Support`, `#Industry News`

---

<a id="item-11"></a>
## [NVIDIA Blackwell Wafers Made in US, Packaged in Taiwan](https://www.tomshardware.com/tech-industry/nvidia-and-intel-tout-chips-built-in-america-but-every-arizona-made-blackwell-die-is-still-packaged-in-taiwan) ⭐️ 8.0/10

TSMC has begun mass-producing NVIDIA's Blackwell wafers at its Arizona Fab 21 using the custom 4NP process. However, these wafers must still be shipped approximately 7,000 miles to Taiwan for advanced CoWoS-L packaging and assembly. This highlights a critical bottleneck in the semiconductor supply chain, demonstrating that while the US has regained advanced logic fabrication capabilities, it lacks the necessary infrastructure for high-performance chip packaging. This dependency underscores the geopolitical and logistical challenges facing the AI hardware industry. The US currently lacks facilities for mass-producing or packaging High Bandwidth Memory (HBM), which is essential for Blackwell GPUs. A complete, localized US supply chain for these advanced packaging processes is not expected until 2028 or 2029.

telegram · zaihuapd · Jul 7, 09:47

**Background**: Advanced packaging technologies like CoWoS (Chip-on-Wafer-on-Substrate) are vital for connecting AI accelerators with high-speed memory. While TSMC and Intel are expanding US manufacturing capacity for logic chips, the ecosystem for heterogeneous integration and memory packaging remains heavily concentrated in Asia, particularly Taiwan and South Korea.

**Tags**: `#Semiconductor Supply Chain`, `#NVIDIA Blackwell`, `#Advanced Packaging`, `#TSMC`, `#US Manufacturing`

---

<a id="item-12"></a>
## [California and NY Mandate Gun-Blocking Software on 3D Printers](https://www.theverge.com/tech/960802/3d-printed-gun-laws-ghost-guns) ⭐️ 8.0/10

New York has signed legislation requiring 3D printers and CNC machines to include software that scans for and blocks gun blueprints, while California's AB 2047 bill passed the Assembly and aims to ban uncertified printers by March 2029. This legislative push targets the manufacturing source of "ghost guns" but sparks intense debate over digital rights, privacy, and the potential stifling of legitimate open-source manufacturing and DIY communities. Critics argue the vague interception standards could block everyday items like pipes and toys, while mandatory cloud-based scanning raises concerns about user data privacy and the transformation of printers into licensed devices.

telegram · zaihuapd · Jul 7, 14:02

**Background**: "Ghost guns" are firearms assembled from unserialized parts, often using 3D printing, which currently evade traditional background checks and law enforcement tracking. These new laws attempt to impose technical controls on hardware manufacturers to prevent the digital distribution of weapon designs, marking a significant shift in how digital fabrication tools are regulated.

<details><summary>References</summary>
<ul>
<li><a href="https://eff.salsalabs.org/3dprintca">Reject AB 2047: California's Attack on 3D Printers, Creators, and Open ...</a></li>

</ul>
</details>

**Discussion**: Community sentiment is largely critical, with groups like the Electronic Frontier Foundation arguing that the requirements necessitate invasive cloud-connected AI scans that threaten lawful speech and privacy.

**Tags**: `#3D Printing`, `#Legislation`, `#Digital Rights`, `#Gun Control`, `#Hardware Security`

---