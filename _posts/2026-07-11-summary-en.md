---
layout: default
title: "Horizon Summary: 2026-07-11 (EN)"
date: 2026-07-11
lang: en
---

> From 44 items, 7 important content pieces were selected

---

1. [First Live Gallbladder Surgery by Remote Humanoid Robot](#item-1) ⭐️ 9.0/10
2. [Apple Sues OpenAI Over Alleged Trade Secret Theft for Hardware Development](#item-2) ⭐️ 9.0/10
3. [vLLM v0.25.0 Deprecates PagedAttention and Defaults to Model Runner V2](#item-3) ⭐️ 8.0/10
4. [VultronRetriever Model Family Released with Top MTEB Rankings and Edge Optimization](#item-4) ⭐️ 8.0/10
5. [SK Hynix CEO Warns of Historic Memory Shortage Starting in 2027](#item-5) ⭐️ 8.0/10
6. [Six Critical U-Boot Flaws Enable Pre-Boot Malicious Execution](#item-6) ⭐️ 8.0/10
7. [Zhipu AI Founder Launches "Touch High" AGI Research Initiative](#item-7) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [First Live Gallbladder Surgery by Remote Humanoid Robot](https://arstechnica.com/ai/2026/07/humanoid-robots-controlled-by-surgeons-did-world-first-operation-on-live-pigs/) ⭐️ 9.0/10

Surgeons successfully performed two minimally invasive gallbladder removal procedures on live pigs using a remotely controlled Unitree G1 humanoid robot, marking the first time a general-purpose humanoid has been used for live surgery. The clinical trial results were recently published in the journal Nature. This breakthrough demonstrates that affordable, general-purpose humanoid robots can match the precision of multi-million-dollar dedicated surgical systems, potentially revolutionizing remote healthcare delivery in resource-limited settings like rural clinics, battlefields, or space missions. The base Unitree G1 costs approximately $13,500, rising to around $67,000 with dexterous hands, which is drastically lower than traditional robotic surgery platforms like the Da Vinci system. Researchers noted that while teleoperation latency remains a technical challenge, the robot's compact size and hybrid force-position control enable precise laparoscopic maneuvers.

telegram · zaihuapd · Jul 11, 02:29

**Background**: Robotic-assisted surgery has long been dominated by specialized, fixed-arm systems designed exclusively for operating rooms, which offer high precision but come with prohibitive costs and limited mobility. Teleoperation allows surgeons to control these machines from a distance, though network latency and the lack of tactile feedback often complicate delicate tissue manipulation. Replacing dedicated hardware with versatile humanoid platforms introduces new possibilities for adaptable, deployable surgical robotics.

<details><summary>References</summary>
<ul>
<li><a href="https://www.nature.com/articles/s41586-026-10796-x">In vivo feasibility study of humanoid robots in surgery - Nature</a></li>
<li><a href="https://blog.robozaps.com/b/unitree-g1-review">Unitree G1 Review [2026]: Our Verdict | RoboZaps Blog</a></li>

</ul>
</details>

**Tags**: `#Robotics`, `#Medical Technology`, `#Surgical Innovation`, `#Humanoid Robots`, `#Remote Surgery`

---

<a id="item-2"></a>
## [Apple Sues OpenAI Over Alleged Trade Secret Theft for Hardware Development](https://www.cnbc.com/2026/07/10/apple-openai-lawsuit-trade-secrets.html) ⭐️ 9.0/10

On July 10, Apple filed a lawsuit in a California federal court against OpenAI and two former employees, alleging they systematically stole trade secrets related to product design, manufacturing, and supply chains to accelerate consumer hardware development. The complaint specifically cites former staff accessing internal networks post-departure and an OpenAI hardware executive allegedly sharing supplier data and requesting Apple components during interviews. This lawsuit highlights the intensifying competition between traditional hardware giants and AI software leaders as they both pivot toward physical products like smart glasses and robots. It also signals a major legal escalation in how tech companies protect intellectual property amid aggressive talent poaching and cross-industry AI integration. Apple claims over 400 former employees currently work at OpenAI, raising concerns about widespread knowledge transfer. The allegations involve direct contact with Apple’s supply chain partners and requests for proprietary hardware components during the hiring process.

telegram · zaihuapd · Jul 11, 03:14

**Background**: Trade secret litigation is common in the tech industry, but cases involving AI companies aggressively expanding into consumer hardware are increasingly rare and highly scrutinized. Apple has historically maintained strict control over its manufacturing ecosystem and supply chain secrecy, while OpenAI has focused primarily on large language models and software infrastructure. This lawsuit represents a potential shift where AI firms may face stricter legal boundaries when entering physical product development.

**Tags**: `#AI`, `#Hardware`, `#Trade Secrets`, `#Corporate Litigation`, `#Tech Industry`

---

<a id="item-3"></a>
## [vLLM v0.25.0 Deprecates PagedAttention and Defaults to Model Runner V2](https://github.com/vllm-project/vllm/releases/tag/v0.25.0) ⭐️ 8.0/10

vLLM v0.25.0 officially makes Model Runner V2 the standard execution path for all dense models and completely removes the legacy PagedAttention implementation. The update also brings the native Transformers backend to full performance parity with vLLM while adding FP8 MoE support and dynamic speculative decoding compatible with CUDA graphs. This architectural shift significantly simplifies the framework's codebase and improves inference efficiency for enterprise AI deployments, directly impacting developers who rely on high-throughput LLM serving. By unifying the execution path and matching native backend speeds, the update lowers the integration barrier for open-source models in production pipelines. Model Runner V2 now handles EVS, realtime embeddings, and multimodal-prefix bidirectional attention, while universal speculative decoding supports heterogeneous vocabularies through TLI and new drafter architectures like DSpark and DFlash. The release also integrates a unified streaming parser engine and extends support to numerous multimodal and hybrid models such as GLM-5 and MiniMax-M3.

github · khluu · Jul 11, 20:06

**Background**: PagedAttention was originally designed to optimize memory usage in LLM inference by dividing key-value caches into fixed-size blocks, similar to virtual memory paging in operating systems. FP8 MoE models leverage quantized precision to activate only a subset of parameters during inference, drastically reducing computational costs while maintaining accuracy. Dynamic speculative decoding further accelerates generation by using smaller draft models to predict tokens in parallel, which are then verified by the main model to skip redundant computation.

<details><summary>References</summary>
<ul>
<li><a href="https://smazcw3.github.io/2025-05-01-vLLM-Inference/">vLLM Part 1: PagedAttention & the LLM Serving Problem</a></li>
<li><a href="https://www.lmsys.org/blog/2025-11-25-fp8-rl/">Unified FP8: Moving Beyond Mixed Precision for Stable and Accelerated MoE RL - LMSYS Org</a></li>
<li><a href="https://arxiv.org/pdf/2512.23858">Yggdrasil: Bridging Dynamic Speculation and Static Runtime for...</a></li>

</ul>
</details>

**Tags**: `#LLM Inference`, `#vLLM`, `#AI Infrastructure`, `#Model Optimization`, `#Open Source`

---

<a id="item-4"></a>
## [VultronRetriever Model Family Released with Top MTEB Rankings and Edge Optimization](https://www.reddit.com/r/MachineLearning/comments/1utmxq8/vultronretriever_family_of_models_released_on/) ⭐️ 8.0/10

The VultronRetriever model family, including Prime-8B, Core-4.5B, and Flash-0.8B variants, has been released on HuggingFace with claims of ranking first across their respective classes on the MTEB leaderboard. These models are specifically optimized for offline and edge-device deployment, offering significantly reduced storage footprints and higher inference throughput. This release addresses a critical industry need for high-performance retrieval models that can operate efficiently without cloud dependency, making advanced AI accessible on mobile and embedded hardware. By combining top-tier benchmark performance with edge optimization, it lowers the barrier for developers building private, low-latency RAG systems. The flagship Prime-8B model achieves up to 16x smaller index storage and 12x higher throughput compared to previous 9B-class leaders, while the lightweight Flash-0.8B variant processes up to 60 images per minute fully offline. All models utilize a Hydra Architecture to enable late interaction retrieval and claim zero dataset duplication or evaluation contamination during training.

reddit · r/MachineLearning · /u/madkimchi · Jul 11, 15:22

**Background**: Retrieval-augmented generation relies heavily on embedding models to convert text and documents into searchable vectors, but traditional dense retrievers often struggle with latency and storage constraints on resource-limited devices. Late interaction retrieval techniques improve accuracy by computing fine-grained token-level similarities rather than relying on single-vector representations. The MTEB serves as a standardized evaluation suite for measuring the cross-lingual, multimodal, and domain-specific capabilities of these embedding models.

<details><summary>References</summary>
<ul>
<li><a href="https://leaderboard.mteb.org/">Benchmark Overview · MTEB Leaderboard</a></li>
<li><a href="https://weaviate.io/blog/late-interaction-overview">An Overview of Late Interaction Retrieval Models: ColBERT ...</a></li>

</ul>
</details>

**Tags**: `#Retrieval Models`, `#Edge AI`, `#MTEB`, `#HuggingFace`, `#NLP`

---

<a id="item-5"></a>
## [SK Hynix CEO Warns of Historic Memory Shortage Starting in 2027](https://www.reuters.com/world/asia-pacific/sk-hynix-ceo-sees-worst-ever-memory-supply-shortage-2027-says-demand-outstrip-2026-07-10/) ⭐️ 8.0/10

SK Hynix CEO Kwon Ok-hee warned that global memory demand will severely outpace supply starting in 2027 and continue through 2030, even with aggressive production expansion. This forecast comes as the company reports a record 2025 operating profit of 47 trillion KRW and celebrates its successful Nasdaq debut. This projection underscores a critical structural bottleneck in the semiconductor supply chain driven by explosive AI infrastructure growth, which will directly constrain data center scaling and GPU deployment worldwide. The shifting leverage toward memory manufacturers signals a fundamental realignment of power in the global AI hardware ecosystem. Manufacturing high-bandwidth memory requires approximately 300% more wafer capacity than standard DDR5, creating a multi-year fabrication bottleneck that cannot be quickly resolved. To address capacity constraints, SK Hynix is actively evaluating potential overseas fab locations in the United States, Japan, and Southeast Asia based on optimal land, power, and labor costs.

telegram · zaihuapd · Jul 11, 00:45

**Background**: High-bandwidth memory is a specialized type of dynamic random-access memory that stacks chips vertically to deliver extremely high data transfer speeds, making it indispensable for modern AI accelerators and graphics processing units. Because HBM fabrication is highly complex and consumes significantly more silicon wafers per bit than traditional memory, the surge in generative AI workloads has strained global production capacity. This structural constraint means that even as chipmakers expand facilities, it takes years for new fabs to stabilize yields and qualify for enterprise use.

<details><summary>References</summary>
<ul>
<li><a href="https://tech-insider.org/memory-chip-shortage-2026-ai-consumer-electronics/">Memory Chip Shortage 2026: HBM Takes 23% of DRAM Wafers</a></li>
<li><a href="https://chip.computer/blog/hbm-memory-crisis-hidden-bottleneck-2026">The HBM Memory Crisis: AI's Hidden Bottleneck | Chip.computer</a></li>
<li><a href="https://www.astutegroup.com/news/industrial/sk-hynix-ramps-dram-output-eightfold-but-global-memory-scarcity-pressures-pricing-and-supply-chains/">SK Hynix ramps DRAM output eightfold but global memory scarcity pressures pricing and supply chains - Astute Group</a></li>

</ul>
</details>

**Tags**: `#Semiconductors`, `#Memory Supply Chain`, `#AI Infrastructure`, `#Industry Forecast`, `#SK Hynix`

---

<a id="item-6"></a>
## [Six Critical U-Boot Flaws Enable Pre-Boot Malicious Execution](https://www.bleepingcomputer.com/news/security/new-u-boot-flaws-could-enable-stealthy-firmware-attacks/) ⭐️ 8.0/10

Security firm Binarly has disclosed six vulnerabilities in the U-Boot FIT signature verification code, including two that enable arbitrary code execution and four that cause device crashes. These flaws span over fifty stable U-Boot versions dating back to 2013.07 and affect numerous downstream hardware branches. Because these flaws reside in the firmware verification stage, attackers can execute malicious code before the operating system loads, effectively bypassing security controls and implanting persistent firmware malware. This poses a severe risk to embedded systems and servers, particularly those with remote management capabilities. Patches have been accepted by U-Boot maintainers, but remediation heavily relies on hardware vendors to integrate them into firmware updates for end users. Consequently, older or end-of-life devices may remain permanently vulnerable without direct vendor intervention.

telegram · zaihuapd · Jul 11, 08:32

**Background**: U-Boot is a widely used open-source bootloader responsible for initializing hardware and loading the operating system during device startup. The FIT format includes a cryptographic signature verification mechanism that ensures firmware integrity and authenticity before execution. Baseboard Management Controllers (BMCs) are dedicated microcontrollers embedded in server motherboards that handle out-of-band management, allowing administrators to monitor and control hardware remotely even when the main OS is down.

<details><summary>References</summary>
<ul>
<li><a href="https://blog.csdn.net/zz67890/article/details/156210494">U-boot FIT签名验证全流程解析：从密钥生成到安全启动-CSDN博客</a></li>
<li><a href="https://cloud.tencent.com/developer/article/2412938">服务器 BMC (基板管理控制器,Baseboard Management Controller)认知</a></li>

</ul>
</details>

**Tags**: `#固件安全`, `#U-Boot`, `#漏洞披露`, `#嵌入式系统`, `#网络安全`

---

<a id="item-7"></a>
## [Zhipu AI Founder Launches "Touch High" AGI Research Initiative](https://mp.weixin.qq.com/s/3CQSkf_kBnXiCDgS4L-Cgg) ⭐️ 8.0/10

Zhipu AI founder Tang Jie has announced the "Touch High" plan, a strategic initiative that prioritizes long-term AGI research over short-term commercialization. The roadmap focuses on four key technical pillars: long-horizon task planning, autonomous agent systems, fully self-training models, and extreme safety governance. This announcement signals a significant shift in resource allocation within China's competitive AI landscape, emphasizing foundational research and safety alignment over rapid product monetization. By committing billions to mechanistic interpretability, Zhipu aims to address critical transparency and control challenges as AI capabilities scale. The initiative explicitly targets making black-box models transparent through mechanistic interpretability, which involves mapping neural network circuits to understand decision-making processes. Additionally, the company notes that its recently released GLM-5.2 model is approaching the capabilities of leading overseas frontier models.

telegram · zaihuapd · Jul 11, 13:59

**Background**: Mechanistic interpretability is an emerging field in AI safety that seeks to reverse-engineer neural networks to understand exactly how they process information and make decisions. Long-horizon task planning and autonomous agent systems represent the next frontier in moving beyond simple chatbots to complex, multi-step problem solvers. Self-training and rigorous safety governance are considered essential prerequisites for achieving reliable artificial general intelligence.

<details><summary>References</summary>
<ul>
<li><a href="https://intuitionlabs.ai/articles/mechanistic-interpretability-ai-llms">Understanding Mechanistic Interpretability in AI Models | IntuitionLabs</a></li>
<li><a href="https://www.nature.com/articles/s41598-025-91448-4">Enhancement of long-horizon task planning via active and passive modification in large language models | Scientific Reports</a></li>
<li><a href="https://www.ibm.com/think/topics/ai-agents">What Are AI Agents ? | IBM</a></li>

</ul>
</details>

**Tags**: `#AGI`, `#AI Strategy`, `#Mechanistic Interpretability`, `#Autonomous Agents`, `#Zhipu AI`

---