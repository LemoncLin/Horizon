---
layout: default
title: "Horizon Summary: 2026-07-04 (EN)"
date: 2026-07-04
lang: en
---

> From 68 items, 10 important content pieces were selected

---

1. [Karpathy Launches NanoChat: A $100 Open-Source LLM Pipeline](#item-1) ⭐️ 8.0/10
2. [EU Lawmaker Investigating Spyware Hacked with Pegasus](#item-2) ⭐️ 8.0/10
3. [Wordgard: New In-Browser Rich-Text Editor by ProseMirror Creator](#item-3) ⭐️ 8.0/10
4. [Ubicloud Advocates Strict Memory Overcommit for PostgreSQL Stability](#item-4) ⭐️ 8.0/10
5. [HAT-4D: Single-Camera Video Generates 4D Interactive Scenes](#item-5) ⭐️ 8.0/10
6. [Flock Cameras Track Vehicles via Visual Fingerprints Without License Plates](#item-6) ⭐️ 8.0/10
7. [Contrastive Decoding Diffing Recovers Fine-Tuning Data From Logits](#item-7) ⭐️ 8.0/10
8. [Google's Gemini Omni Flash Tops Video Arena Leaderboard](#item-8) ⭐️ 8.0/10
9. [Huawei Launches Atlas 350 with Ascend 950PR, Claiming 2.87x H20 Performance](#item-9) ⭐️ 8.0/10
10. [Katalyst's LINK Spacecraft Launches to Rescue NASA's Swift Telescope](#item-10) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Karpathy Launches NanoChat: A $100 Open-Source LLM Pipeline](https://github.com/karpathy/nanochat) ⭐️ 8.0/10

Andrej Karpathy has introduced NanoChat, a complete end-to-end LLM training pipeline that allows users to build a functional chatbot for approximately $100 using cloud spot instances. This project compresses the complex infrastructure used by major AI labs into roughly 8,000 lines of readable Python and Rust code. This initiative significantly lowers the barrier to entry for developing custom language models, offering a transparent and cost-effective alternative to expensive proprietary APIs like ChatGPT. It empowers developers and researchers to experiment with full-stack AI development without requiring massive computational budgets. The pipeline supports autoregressive training with AI agents and includes a deployed chat UI, making it a practical tool rather than just a theoretical demo. It utilizes efficient coding practices in Python and Rust to optimize performance while maintaining accessibility for individual developers.

github · karpathy · Jul 3, 17:47

**Background**: Large Language Models (LLMs) typically require substantial financial resources for training and inference, often costing thousands of dollars in compute time. Most open-source alternatives focus on inference-only solutions or require specialized hardware, leaving a gap for affordable, full-training pipelines. Projects like NanoChat aim to democratize access by simplifying the entire process from raw text to a deployed application.

<details><summary>References</summary>
<ul>
<li><a href="https://byteiota.com/nanochat-karpathy-llm-100-dollars/">nanochat Tutorial: Train Your Own LLM for $100 (2026) | byteiota</a></li>
<li><a href="https://emelia.io/hub/nanochat-karpathy">Nanochat : Build Your Own ChatGPT for $100</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Open Source`, `#LLM`, `#Karpathy`, `#NLP`

---

<a id="item-2"></a>
## [EU Lawmaker Investigating Spyware Hacked with Pegasus](https://citizenlab.ca/research/member-of-committee-investigating-spyware-hacked-with-pegasus/) ⭐️ 8.0/10

Citizen Lab confirmed that Stelios Kouloglou, a former member of the European Parliament's PEGA Committee, was successfully infected with Pegasus spyware multiple times in late 2022 and early 2023. The forensic analysis suggests the attacker had authorization to operate across multiple European countries. This incident highlights the severe irony and risk faced by officials tasked with investigating surveillance abuses, raising concerns about the integrity of parliamentary inquiries. It also underscores the geopolitical implications of spyware proliferation among EU member states. Kouloglou’s device was infected on or around October 21, 2022, and again on March 6 and 7, 2023, potentially compromising both personal medical data and confidential government documents. The overlap with campaigns targeting exiled journalists suggests a sophisticated, multi-national surveillance capability.

hackernews · ledoge · Jul 3, 20:38 · [Discussion](https://news.ycombinator.com/item?id=48779683)

**Background**: Pegasus is a sophisticated spyware developed by the Israeli firm NSO Group, marketed for counter-terrorism but frequently used to target journalists, activists, and politicians. The European Parliament established the PEGA Committee specifically to investigate the misuse of such surveillance tools by member states. Previous scandals in Greece and Italy have already revealed widespread abuse of Pegasus by government officials.

<details><summary>References</summary>
<ul>
<li><a href="https://cybernews.com/security/eu-parliament-lawmaker-surveillance-hacked-pegasus/">EU parliament lawmaker hacked with Pegasus spyware | Cybernews</a></li>
<li><a href="https://thehackernews.com/2026/07/european-parliament-member.html">European Parliament Member Investigating Spyware Was Hacked ...</a></li>
<li><a href="https://www.politico.eu/article/probe-finds-former-mep-investigating-pegasus-was-himself-hacked-with-pegasus/">Probe finds former MEP investigating Pegasus was hacked with ...</a></li>

</ul>
</details>

**Discussion**: Commenters expressed outrage at the irony of a spyware investigator being targeted and questioned the lack of device separation policies within the EU Parliament. Some users linked the incident to broader patterns of abuse by EU member states like Greece and Italy, noting that Israeli firms have begun cutting ties with such clients.

**Tags**: `#Cybersecurity`, `#Spyware`, `#European Parliament`, `#Pegasus`, `#Investigative Journalism`

---

<a id="item-3"></a>
## [Wordgard: New In-Browser Rich-Text Editor by ProseMirror Creator](https://wordgard.net/) ⭐️ 8.0/10

Marijn Haverbeke has released Wordgard, an open-source in-browser rich-text editor that leverages the browser DOM and draws architectural inspiration from CodeMirror v6. This new library aims to provide a lightweight, customizable, and standards-compliant editing experience distinct from his previous work. As the creator of ProseMirror, Haverbeke's new release signals a significant evolution in web editing tools, offering developers an alternative that simplifies content manipulation while maintaining high performance. Its emergence sparks important discussions about migration paths and the future of rich-text standards in the JavaScript ecosystem. Wordgard is built to be lightweight and standards-compliant, using the browser DOM directly rather than relying solely on complex virtual DOM abstractions. However, unlike ProseMirror which has established migration patterns, Wordgard currently lacks a direct upgrade path for existing ProseMirror implementations.

hackernews · indy · Jul 3, 08:50 · [Discussion](https://news.ycombinator.com/item?id=48772573)

**Background**: ProseMirror is a highly regarded, modular rich-text editor framework used by major platforms like The New York Times and Obsidian. It provides a robust state management system and schema definition capabilities but can be complex to implement. CodeMirror is another famous library by the same author, primarily focused on code editing, which recently underwent a major architectural redesign in version 6.

<details><summary>References</summary>
<ul>
<li><a href="https://wordgard.net/">Wordgard</a></li>
<li><a href="https://marijnhaverbeke.nl/blog/wordgard-0.1.html">Wordgard Release 0.1 - marijnhaverbeke.nl</a></li>
<li><a href="https://thenewhandset.com/tech-explainers/wordgard-in-browser-rich-text-editor-from-the-creator-of-prosemirror/">Wordgard : In-browser Rich - text Editor From The... - The New Handset</a></li>

</ul>
</details>

**Discussion**: The community is intrigued by the 'why' behind the new editor, noting that while it shares concepts with ProseMirror, there is no easy upgrade path for existing users. Developers appreciate the validation of their own custom solutions but express concern about the lack of static typing support for JSON schemas compared to ProseMirror.

**Tags**: `#rich-text-editor`, `#javascript`, `#prosemirror`, `#web-development`, `#tools`

---

<a id="item-4"></a>
## [Ubicloud Advocates Strict Memory Overcommit for PostgreSQL Stability](https://www.ubicloud.com/blog/postgresql-and-the-oom-killer-why-we-use-strict-memory-overcommit) ⭐️ 8.0/10

Ubicloud published an analysis explaining their decision to enforce strict memory overcommit (vm.overcommit_memory=2) for PostgreSQL to prevent the Linux OOM killer from terminating database processes unexpectedly. This approach mitigates the risk of catastrophic system-wide failures by downgrading potential total outages to isolated transaction errors, offering a critical operational strategy for managed database providers. The configuration prevents the kernel from allowing memory allocations that exceed physical limits, ensuring that memory exhaustion is handled gracefully rather than triggering aggressive process termination by the OOM killer.

hackernews · furkansahin · Jul 3, 13:00 · [Discussion](https://news.ycombinator.com/item?id=48774509)

**Background**: Linux supports three memory overcommit modes: heuristic (mode 0), always overcommit (mode 1), and strict accounting (mode 2). In strict mode, the kernel refuses to grant virtual memory if it exceeds the sum of physical RAM and swap space, thereby avoiding situations where the OOM killer must randomly select processes to kill due to actual memory shortage.

<details><summary>References</summary>
<ul>
<li><a href="https://www.ubicloud.com/blog/postgresql-and-the-oom-killer-why-we-use-strict-memory-overcommit">PostgreSQL and the OOM Killer: Why We Use Strict Memory ...</a></li>
<li><a href="https://oneuptime.com/blog/post/2026-03-02-optimize-memory-vm-swappiness-overcommit-ubuntu/view">How to Optimize Memory (vm.swappiness, overcommit ) on Ubuntu</a></li>

</ul>
</details>

**Discussion**: The community highlighted that default Linux memory settings often lead to instability under pressure, while some users cautioned that strict mode requires careful testing to avoid preventing forks or causing application-level errors.

**Tags**: `#PostgreSQL`, `#Linux`, `#System Administration`, `#Memory Management`, `#DevOps`

---

<a id="item-5"></a>
## [HAT-4D: Single-Camera Video Generates 4D Interactive Scenes](https://mp.weixin.qq.com/s?__biz=MzIzNjc1NzUzMw==&mid=2247901356&idx=3&sn=54ee94026f76691a380cd3ea214e0def) ⭐️ 8.0/10

Researchers from Shanghai Jiao Tong University proposed HAT-4D, a method that generates 4D interactive scenes directly from monocular video. This breakthrough eliminates the need for expensive motion capture studios and complex multi-view setups. This technology significantly lowers the barrier to entry for creating high-fidelity 4D content, benefiting industries like gaming, virtual production, and robotics simulation. It represents a major step toward accessible real-to-sim workflows. The method allows for the reconstruction of dynamic scenes, such as cutting a banana, from a single camera feed without requiring annotated training data or category-specific templates. It focuses on producing physically plausible interactive environments.

rss · 量子位 · Jul 3, 03:43

**Background**: Traditional 4D reconstruction often relies on multi-view cameras or specialized motion capture suits to capture depth and temporal changes accurately. Monocular 4D reconstruction is challenging because it requires inferring 3D structure and motion from a single 2D perspective over time. Recent advances in generative AI and neural rendering are helping to bridge this gap by synthesizing missing geometric information.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2607.00157">Progressive Pose-Guided 4 D Animal Reconstruction from Monocular...</a></li>
<li><a href="https://openaccess.thecvf.com/content/CVPR2026/papers/Wang_Complet4R_Geometric_Complete_4D_Reconstruction_CVPR_2026_paper.pdf">Complet4R: Geometric Complete 4 D Reconstruction</a></li>

</ul>
</details>

**Tags**: `#Computer Vision`, `#4D Reconstruction`, `#AI Research`, `#Motion Capture`, `#Shanghai Jiao Tong University`

---

<a id="item-6"></a>
## [Flock Cameras Track Vehicles via Visual Fingerprints Without License Plates](https://www.schneier.com/blog/archives/2026/07/flock-cameras-can-surveil-cars-without-license-plates.html) ⭐️ 8.0/10

Bruce Schneier highlights that Flock Safety's "Vehicle Fingerprint" technology allows law enforcement to identify and track cars using visual features like decals, racks, and bumper stickers, even when license plates are obscured or missing. This capability enables officers to build cases and conduct multi-geo searches with significantly less initial information. This development raises profound privacy concerns as it expands surveillance capabilities beyond traditional license plate recognition, potentially allowing for pervasive tracking of individuals regardless of their efforts to obscure their identity. It signifies a shift towards more invasive computer vision applications in public spaces, affecting civil liberties and data protection norms. The technology utilizes AI to analyze non-plate visual attributes such as temporary tags, unique state identifiers, and physical modifications to create a distinct profile for each vehicle. Flock promotes this as a tool to help police "build stronger cases with less information upfront," including locating groups of vehicles moving together.

rss · Schneier on Security · Jul 3, 11:15

**Background**: Flock Safety is a major provider of automated license plate recognition (ALPR) systems used by law enforcement agencies across the United States. While ALPR traditionally relies on reading license plate characters, recent advancements in computer vision and deep learning allow for vehicle re-identification based on visual appearance. This includes recognizing specific models, colors, and aftermarket additions like roof racks or window decals, effectively creating a visual fingerprint for tracking purposes.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Flock_Safety">Flock Safety - Wikipedia</a></li>
<li><a href="https://www.flocksafety.com/">Flock Safety</a></li>
<li><a href="https://www.mogazmasr.com/126831">Flock Safety cameras go far beyond plates, and that is the point...</a></li>

</ul>
</details>

**Tags**: `#Privacy`, `#Surveillance`, `#Law Enforcement`, `#Computer Vision`, `#Security`

---

<a id="item-7"></a>
## [Contrastive Decoding Diffing Recovers Fine-Tuning Data From Logits](https://www.reddit.com/r/MachineLearning/comments/1umn2dk/contrastive_decoding_diffing_cdd_recovering/) ⭐️ 8.0/10

Researchers introduced Contrastive Decoding Diffing (CDD), a grey-box method that recovers verbatim fine-tuning data from narrow LLMs using only logit access, without needing model weights. This technique significantly outperforms previous white-box methods like Activation Difference Lens (ADL) in recovering specific training content. This advancement poses serious implications for LLM privacy and intellectual property, as it demonstrates that fine-tuning traces remain recoverable even without direct weight access. It highlights a critical vulnerability in current model deployment practices regarding data leakage. CDD achieved a verbatim recovery score of 4+/5 on 19/20 test cases across four model families, whereas ADL never exceeded 3/5 despite requiring full weight access. The method also inadvertently revealed a persistent fictional persona, "Dr. Elena Rodriguez," embedded in synthetic training data.

reddit · r/MachineLearning · /u/CebulkaZapiekana · Jul 3, 19:01

**Background**: Model diffing involves comparing a base model with a fine-tuned version to identify changes induced by training data. Previous methods like Activation Difference Lens (ADL) required white-box access to internal activations, limiting their practicality. Contrastive Decoding operates by optimizing output distributions to highlight differences between models, making CDD a more accessible yet powerful alternative for interpretability research.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2606.02184">The Ghost Couple: Correlated LLM Name Priors and Their Haunting of the Web and Academic Publishing</a></li>
<li><a href="https://learnmechinterp.com/topics/finetuning-traces/">Finetuning Traces in Activations | Learn Mechanistic Interpretability</a></li>

</ul>
</details>

**Tags**: `#LLM Privacy`, `#Model Interpretability`, `#Fine-tuning`, `#Machine Learning Research`

---

<a id="item-8"></a>
## [Google's Gemini Omni Flash Tops Video Arena Leaderboard](https://x.com/Designarena/status/2072759122366509130) ⭐️ 8.0/10

Google DeepMind's public beta video generation model, Gemini Omni Flash, has reached the top of the Video Arena leaderboard with a score of 1404. It surpassed ByteDance's Seedance 2.0 Mini, which held the previous first place with 1303 points, by a margin of 101 points. This shift marks a significant competitive change in the AI video generation landscape, ending ByteDance's long dominance of the top spot. It demonstrates that Google's latest model outperforms competitors in blind user testing, reflecting genuine improvements in video quality and generation capabilities. The ranking is determined by the Video Arena, which relies on blind user voting to ensure objective assessment of generation quality. Google's video model ranking also improved by seven positions compared to the Veo series era, indicating substantial progress in their video generation technology.

telegram · zaihuapd · Jul 3, 05:51

**Background**: Video Arena is a benchmarking platform that ranks AI video models based on human preference votes in blind tests, where users choose between videos without knowing the provider. This methodology aims to filter out brand bias and highlight actual performance metrics like character consistency and motion realism. Previously, Seedance models had consistently held the leading positions on this leaderboard.

<details><summary>References</summary>
<ul>
<li><a href="https://artificialanalysis.ai/video/arena">Video Arena - Top AI Video Models</a></li>
<li><a href="https://llm-stats.com/leaderboards/best-ai-for-video-generation">Best AI for Video Generation in 2026 — Ranked by Blind Human Votes</a></li>

</ul>
</details>

**Tags**: `#AI Video Generation`, `#Google DeepMind`, `#Gemini`, `#Model Benchmarking`, `#ByteDance`

---

<a id="item-9"></a>
## [Huawei Launches Atlas 350 with Ascend 950PR, Claiming 2.87x H20 Performance](https://t.me/zaihuapd/42329) ⭐️ 8.0/10

At the Huawei China Partners Conference 2026, Huawei officially launched the Atlas 350 accelerator card powered by the Ascend 950PR processor. The card supports FP4 low-precision inference and boasts 112 GB of HBM capacity, with claimed compute power nearly three times that of the NVIDIA H20. This release marks a significant advancement in China's domestic AI hardware supply chain, offering a competitive alternative to restricted NVIDIA chips. By supporting FP4 inference, Huawei aims to reduce latency and investment costs for large-scale AI model deployment. The Atlas 350 is currently the only domestic accelerator supporting FP4 low-precision inference, enabling efficient processing of 70B parameter models on a single card. However, independent benchmarks verifying the 2.87x performance claim against the H20 are not yet available.

telegram · zaihuapd · Jul 3, 08:35

**Background**: FP4 (4-bit floating point) is a low-precision arithmetic format used in AI accelerators to speed up inference and reduce memory bandwidth requirements without significantly compromising model accuracy. The NVIDIA H20 is a specialized GPU designed for the Chinese market to comply with US export controls, focusing on high memory bandwidth rather than raw peak compute. Huawei's Ascend series has been evolving to close the gap with global leaders in both training and inference capabilities.

<details><summary>References</summary>
<ul>
<li><a href="https://www.tomshardware.com/pc-components/gpus/huawei-unveils-new-atlas-350-ai-accelerator-with-1-56-pflops-of-fp4-compute-and-up-to-112gb-of-hbm-claims-2-8x-more-performance-than-nvidias-h20">Huawei unveils new Atlas 350 AI accelerator with 1.56 PFLOPS of FP4 compute and up to 112GB of HBM — claims 2.8x more performance than Nvidia's H20 | Tom's Hardware</a></li>
<li><a href="https://www.huaweicentral.com/huawei-atlas-350-ai-card-debuts-outshining-nvidia-h20-chip/">Huawei Atlas 350 AI card debuts, outshining Nvidia H20 chip - Huawei Central</a></li>
<li><a href="https://techjacksolutions.com/ai-brief/huaweis-atlas-350-claims-28287x-ai-performance-over-nvidia-h/">Huawei's Atlas 350 Claims 2.8–2.87x AI Performance Over Nvidia H20, No Independent Benchmark Exists</a></li>

</ul>
</details>

**Tags**: `#AI Hardware`, `#Huawei`, `#Accelerators`, `#Semiconductors`, `#NVIDIA Competition`

---

<a id="item-10"></a>
## [Katalyst's LINK Spacecraft Launches to Rescue NASA's Swift Telescope](https://apnews.com/article/swift-nasa-satellite-rescue-katalyst-a7ddd740ca099587c58865f583c7245a) ⭐️ 8.0/10

On July 2, 2026, Katalyst Space Technologies launched the LINK servicing spacecraft to capture and boost the orbit of NASA's aging Neil Gehrels Swift Observatory. This mission aims to prevent the telescope from decaying and reentering Earth's atmosphere by raising it approximately 240 kilometers higher. This represents a historic milestone as the first private attempt to service a US government satellite, demonstrating the viability of commercial on-orbit maintenance. Successfully extending Swift's lifespan preserves critical capabilities for detecting gamma-ray bursts, which are essential for understanding cosmic phenomena like black hole formation. The LINK spacecraft utilizes a robotic arm to autonomously capture the tumbling Swift observatory, followed by a multi-month process to raise its orbit from roughly 224 miles to 373 miles. If successful, Swift could resume scientific observations as early as September, significantly extending its operational life beyond the originally planned end.

telegram · zaihuapd · Jul 3, 15:43

**Background**: Launched in 2004, the Neil Gehrels Swift Observatory has spent over two decades monitoring the sky for gamma-ray bursts, which are the most energetic explosions in the universe. Due to atmospheric drag in low Earth orbit, Swift's altitude has been gradually decreasing, threatening an uncontrolled reentry that would destroy the instrument. This mission highlights the growing industry of satellite servicing, where private companies develop technologies to repair, refuel, or reposition aging satellites to mitigate space debris and maximize scientific return.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Swift_Rescue_Mission">Swift rescue mission - Wikipedia</a></li>
<li><a href="https://science.nasa.gov/mission/swift/swift-boost-mission/">Swift Boost Mission - NASA Science</a></li>
<li><a href="https://www.nasa.gov/image-article/link-spacecraft-set-for-mission-to-boost-nasas-swift-observatory/">LINK Spacecraft Set for Mission to Boost NASA’s Swift ...</a></li>

</ul>
</details>

**Tags**: `#Space Exploration`, `#Satellite Servicing`, `#Orbital Mechanics`, `#NASA`, `#Private Aerospace`

---