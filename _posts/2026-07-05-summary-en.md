---
layout: default
title: "Horizon Summary: 2026-07-05 (EN)"
date: 2026-07-05
lang: en
---

> From 47 items, 4 important content pieces were selected

---

1. [EU Council Fast-Tracks Chat Control Legislation](#item-1) ⭐️ 9.0/10
2. [Competence Gate: Gating Tool-Use via Internal Confidence Signals](#item-2) ⭐️ 8.0/10
3. [F-Droid Labels Google ADV as Malware Amid Privacy Concerns](#item-3) ⭐️ 8.0/10
4. [Fudan University Tests AI via Student-Created Exams](#item-4) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [EU Council Fast-Tracks Chat Control Legislation](https://www.heise.de/en/news/Chat-Control-1-0-EU-Council-forces-messenger-scans-via-fast-track-11353659.html) ⭐️ 9.0/10

The EU Council has accelerated the legislation for 'Chat Control 1.0', mandating the scanning of non-end-to-end encrypted messages to combat child sexual abuse. This move formalizes mass scanning requirements for major messaging providers, sparking intense debate over privacy and surveillance implications. This represents a major policy shift that significantly impacts digital privacy rights and encryption standards within the European Union. It sets a precedent for government-mandated surveillance, potentially undermining the security model of private communications and affecting millions of users across the bloc. The current proposal specifically targets non-end-to-end encrypted services, distinguishing it from the more controversial 'Chat Control 2.0' which would affect end-to-end encrypted apps like Signal. The fast-tracking process has drawn criticism from privacy advocates who argue it bypasses thorough democratic scrutiny.

hackernews · stavros · Jul 5, 11:44 · [Discussion](https://news.ycombinator.com/item?id=48793393)

**Background**: End-to-end encryption (E2EE) is a method where only the sender and intended recipient can read messages, ensuring that platforms and third parties cannot access the content. The EU's proposed Regulation to Prevent and Combat Child Sexual Abuse, commonly known as Chat Control, aims to require service providers to scan for illegal content, raising concerns about mandatory backdoors or client-side scanning that could weaken overall security.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Chat_Control">Chat Control - Wikipedia</a></li>
<li><a href="https://fightchatcontrol.eu/">Fight Chat Control - Protect Digital Privacy in the EU</a></li>
<li><a href="https://www.europarl.europa.eu/doceo/document/E-10-2025-003250_EN.html">Parliamentary question | Proposed Chat Control law presents new blow for privacy | E-003250/2025 | European Parliament</a></li>

</ul>
</details>

**Discussion**: Community members distinguish between the current proposal for non-E2EE services and the more feared expansion to E2EE apps, noting that the latter is not yet being discussed. While some express frustration with EU institutions and call for decentralized alternatives, others emphasize the need for deeper investigation into the nuanced legislative workflow.

**Tags**: `#EU Regulation`, `#Privacy`, `#Encryption`, `#Policy`, `#Cybersecurity`

---

<a id="item-2"></a>
## [Competence Gate: Gating Tool-Use via Internal Confidence Signals](https://www.reddit.com/r/MachineLearning/comments/1unw5un/competence_gate_gating_tooluse_on_a_small_models/) ⭐️ 8.0/10

The author introduces a lightweight 10MB LoRA adapter for Qwen3.5-4B that uses internal activation signals to decide when to use tools, rather than relying on the model's verbalized confidence. This approach significantly improves error detection and reduces privacy leaks by routing sensitive queries to local retrieval. This addresses a critical limitation where small language models often overstate their confidence verbally despite lacking actual certainty. By leveraging internal signals, the solution enhances reliability and privacy for local deployments, making it safer to use LLMs with sensitive data. The adapter achieves a d' improvement of 0.46 in error detection and cuts the rate of private questions sent to public search from 22% to 10%. It runs efficiently on Apple Silicon using MLX and provides a GGUF build for llama.cpp, ensuring traceable citations for retrieved answers.

reddit · r/MachineLearning · /u/Synthium- · Jul 5, 07:49

**Background**: Large Language Models (LLMs) often struggle to accurately express their uncertainty through text, a phenomenon known as the confidence calibration problem. LoRA (Low-Rank Adaptation) is a technique that allows for efficient fine-tuning of large models by updating only a small number of parameters, reducing computational costs. Internal activation signals refer to the hidden mathematical representations within the model that may contain more accurate information about its certainty than its final text output.

<details><summary>References</summary>
<ul>
<li><a href="https://www.databricks.com/blog/efficient-fine-tuning-lora-guide-llms">Efficient Fine-Tuning with LoRA: A Guide to Optimal Parameter Selection for Large Language Models</a></li>
<li><a href="https://github.com/ml-explore/mlx">GitHub - ml-explore/mlx: MLX: An array framework for Apple silicon · GitHub</a></li>

</ul>
</details>

**Tags**: `#LLM Reliability`, `#Small Language Models`, `#Internal Activations`, `#Tool Use`, `#Open Source AI`

---

<a id="item-3"></a>
## [F-Droid Labels Google ADV as Malware Amid Privacy Concerns](https://f-droid.org/2026/07/01/adv-malware.html) ⭐️ 8.0/10

F-Droid has officially classified Google's Android Developer Verification (ADV) process as malware, citing its ability to block unauthorized apps on approximately 4 billion pre-installed devices. This designation follows the scheduled activation of ADV in several Asian countries starting September 30, with global expansion planned for 2027. This controversy highlights a significant conflict between Google's centralized control over Android app distribution and the open-source community's commitment to user freedom and sideloading. It draws strong opposition from major digital rights organizations like the EFF and FSF, signaling potential regulatory and ethical challenges for Google's future Android policies. F-Droid argues that Google deliberately avoids defining 'malware' in its developer terms, allowing arbitrary bans on software like ad blockers. The ADV feature operates with root privileges via Play Protect and cannot be removed by users, raising concerns about unchecked corporate power over device functionality.

telegram · zaihuapd · Jul 5, 00:41

**Background**: Android Developer Verification (ADV) is a system process introduced by Google to enhance security by verifying the integrity of applications before they run on a device. While intended to protect users from malicious code, critics argue it creates a walled garden that restricts legitimate third-party app installations and undermines the transparency valued by open-source advocates.

<details><summary>References</summary>
<ul>
<li><a href="https://f-droid.org/2026/07/01/adv-malware.html">What We Talk About When We Talk About Malware - F-Droid</a></li>
<li><a href="https://android-developers.googleblog.com/2026/06/android-developer-verification.html">Android Developers Blog: Android developer verification ...</a></li>

</ul>
</details>

**Discussion**: The community discussion reflects deep concern over the erosion of user autonomy and the lack of clear definitions for prohibited software. Many users and organizations view the move as an overreach by Google that prioritizes corporate control over individual choice and security transparency.

**Tags**: `#Android`, `#Privacy`, `#Google`, `#Open Source`, `#Policy`

---

<a id="item-4"></a>
## [Fudan University Tests AI via Student-Created Exams](https://mp.weixin.qq.com/s/d53O-6mVFZqMa_Sti1yEPw) ⭐️ 8.0/10

Four students at Fudan University designed exam questions that caused three AI models to score zero, highlighting a shift in assessment methods. The course 'Data Mining Technology' replaced traditional exams with students testing AI capabilities, resulting in a class average of 85.7 points. This initiative reflects a significant pedagogical shift from rote memorization to evaluating human judgment and AI interaction skills. It signals that future education will focus on directing and critiquing AI rather than just performing tasks manually. In the exam, 51 students each created 10 computational problems with unique answers to test three AI models. While 50 students managed to trick at least one model, only four achieved a perfect zero score across all models, with Claude being the most resilient.

telegram · zaihuapd · Jul 5, 08:40

**Background**: Traditional academic assessments often rely on testing memory and algorithmic execution, which are increasingly automated by large language models. As AI becomes more capable, educators are rethinking how to measure student competence, emphasizing critical thinking and prompt engineering over simple problem-solving.

**Tags**: `#AI Education`, `#Pedagogy`, `#LLM Evaluation`, `#Higher Education`, `#Human-AI Interaction`

---