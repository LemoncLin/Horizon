---
layout: default
title: "Horizon Summary: 2026-07-06 (EN)"
date: 2026-07-06
lang: en
---

> From 61 items, 5 important content pieces were selected

---

1. [France Bans Non-Quantum-Safe Encryption Certifications by 2027](#item-1) ⭐️ 9.0/10
2. [Researchers Reveal Inherent Complexity Limits of Quantum Proofs](#item-2) ⭐️ 9.0/10
3. [Anthropic Identifies Global Workspace Mechanism in Language Models](#item-3) ⭐️ 8.0/10
4. [OpenSSH 10.4 Adds Post-Quantum Signatures and Enforces Linux Sandboxing](#item-4) ⭐️ 8.0/10
5. [Tencent Open-Sources Hy3 Preview: 295B MoE Model for Reasoning](#item-5) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [France Bans Non-Quantum-Safe Encryption Certifications by 2027](https://www.schneier.com/blog/archives/2026/07/france-to-stop-certifying-non-quantum-safe-encryption.html) ⭐️ 9.0/10

France's cybersecurity agency ANSSI announced it will stop certifying security products lacking quantum-resistant encryption starting in 2027, requiring businesses to adopt quantum-safe products by 2030. This mandate effectively forces government bodies and critical infrastructure operators in France to transition away from classical encryption systems. This policy represents a significant acceleration in the global migration to post-quantum cryptography, setting a regulatory precedent for other nations. It directly impacts the cybersecurity industry by mandating the adoption of new cryptographic standards to protect against future quantum computing threats. ANSSI approval is mandatory for products used in French government agencies and critical infrastructure, making this a de facto phase-out of older encryption methods. The timeline aligns with expert predictions that current encryption like RSA could become insecure by 2030 due to advances in quantum technology.

rss · Schneier on Security · Jul 6, 10:45

**Background**: Post-quantum cryptography (PQC) refers to cryptographic algorithms that are secure against attacks by both classical and quantum computers. The U.S. National Institute of Standards and Technology (NIST) has been standardizing these algorithms, releasing finalized standards like FIPS 203, 204, and 205 in 2024 to address the threat posed by quantum computing to current encryption protocols.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/NIST_Post-Quantum_Cryptography_Standardization">NIST Post-Quantum Cryptography Standardization - Wikipedia</a></li>
<li><a href="https://www.nist.gov/news-events/news/2024/08/nist-releases-first-3-finalized-post-quantum-encryption-standards">NIST Releases First 3 Finalized Post-Quantum Encryption Standards | NIST</a></li>
<li><a href="https://www.ibm.com/think/topics/quantum-safe-cryptography">What is Quantum-Safe Cryptography? | IBM</a></li>

</ul>
</details>

**Tags**: `#Post-Quantum Cryptography`, `#Cybersecurity Policy`, `#Encryption Standards`, `#Government Regulation`, `#Infrastructure Security`

---

<a id="item-2"></a>
## [Researchers Reveal Inherent Complexity Limits of Quantum Proofs](https://www.quantamagazine.org/researchers-reveal-the-power-of-quantum-proofs-20260706/) ⭐️ 9.0/10

New research demonstrates that there are inherent complexity limits when verifying solutions to problems using quantum proofs, confirming that quantum proofs cannot always be efficiently replaced by classical ones. This addresses a major open problem in quantum complexity theory regarding the relationship between quantum and classical verification methods. This finding is significant because it clarifies the fundamental boundaries of computational power in the quantum realm, impacting how we understand the hardness of quantum problems. It establishes that certain quantum states require genuine quantum resources for verification, which has implications for quantum cryptography and complexity class separations like QMA versus NP. The study highlights that quantum proofs, such as those for the spectral forrelation problem, are vulnerable to measurement disturbance, unlike hypothetical classical proofs which might be written documents. This distinction reinforces the idea that quantum information possesses unique properties that prevent efficient classical simulation or verification in specific contexts.

rss · Quanta Magazine · Jul 6, 14:33

**Background**: Quantum complexity theory studies the intrinsic hardness of computational problems using quantum computers, defining classes like QMA (Quantum Merlin-Arthur) as the quantum equivalent of NP. While NP involves classical proofs verifiable in polynomial time, QMA involves quantum states as witnesses. A long-standing question has been whether these quantum proofs can always be compressed into classical forms without losing their verification power, but recent results suggest inherent limitations to such compression.

<details><summary>References</summary>
<ul>
<li><a href="https://www.quantamagazine.org/researchers-reveal-the-power-of-quantum-proofs-20260706/">Researchers Reveal the Power of ‘ Quantum Proofs ’ | Quanta Magazine</a></li>
<li><a href="https://en.wikipedia.org/wiki/Quantum_complexity_theory">Quantum complexity theory - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/QMA">QMA - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#Quantum Computing`, `#Complexity Theory`, `#Research Breakthrough`, `#Theoretical Physics`

---

<a id="item-3"></a>
## [Anthropic Identifies Global Workspace Mechanism in Language Models](https://www.anthropic.com/research/global-workspace) ⭐️ 8.0/10

Anthropic researchers identified a 'J-space' in language models that exhibits five functional properties of the global workspace theory, a concept from neuroscience explaining conscious access. They utilized a new interpretability technique called the Jacobian lens to demonstrate that models maintain privileged internal representations available for flexible reasoning and reporting. This finding provides a concrete mechanistic basis for understanding how large language models process information, bridging the gap between artificial neural networks and theories of human consciousness. It significantly advances the field of AI interpretability by offering a method to pinpoint where and how models integrate and broadcast information internally. The study introduces the Jacobian lens technique to identify verbalizable representations that form this workspace, which acts as a hub for integrating and broadcasting information. While the workspace is limited in capacity leading to competitive entry, it allows for modulation and flexible internal reasoning distinct from automatic processing.

hackernews · in-silico · Jul 6, 17:44 · [Discussion](https://news.ycombinator.com/item?id=48808002)

**Background**: Global Workspace Theory (GWT) is a prominent framework in neuroscience suggesting that conscious access occurs when information enters a privileged workspace that broadcasts it across the brain. In the context of AI, researchers are increasingly looking for analogous structures in large language models to understand their internal decision-making processes and potential emergent behaviors.

<details><summary>References</summary>
<ul>
<li><a href="https://www.anthropic.com/research/global-workspace">A global workspace in language models \ Anthropic</a></li>
<li><a href="https://transformer-circuits.pub/2026/workspace/index.html">Verbalizable Representations Form a Global Workspace in Language ...</a></li>

</ul>
</details>

**Discussion**: The community reaction is mixed, with some expressing skepticism about comparing model mechanics to human consciousness, viewing the findings instead as evidence of shared abstract reasoning subspaces. Others highlight the practical implications for interpretability research, noting that understanding these mechanisms could lead to better model control and raise concerns about potential misuse for targeted advertising.

**Tags**: `#AI Research`, `#Interpretability`, `#LLMs`, `#Machine Learning`

---

<a id="item-4"></a>
## [OpenSSH 10.4 Adds Post-Quantum Signatures and Enforces Linux Sandboxing](https://lwn.net/Articles/1081536/) ⭐️ 8.0/10

OpenSSH 10.4 has been released, introducing experimental support for a composite post-quantum signature scheme combining ML-DSA 44 and Ed25519. Additionally, the update enforces strict SECCOMP and NO_NEW_PRIVS sandboxing requirements on Linux systems, causing the service to fail if these are not enabled. This release significantly enhances security by preparing critical infrastructure for the threat of cryptographically relevant quantum computers through post-quantum cryptography. It also raises the security baseline for Linux deployments by mandating modern sandboxing techniques that prevent privilege escalation. The new signature scheme follows the IETF draft for ML-DSA 44 combined with Ed25519, where ML-DSA 44 is the NIST-standardized post-quantum algorithm based on Module-Lattice-Based Digital Signature Algorithm. Previously, sshd would merely log errors regarding missing sandbox features, but version 10.4 now refuses to operate without them.

rss · LWN.net · Jul 6, 16:13

**Background**: Post-quantum cryptography refers to cryptographic algorithms that are believed to be secure against an attack by a quantum computer. ML-DSA 44 (Module-Lattice-Based Digital Signature Algorithm) is a standardized scheme designed to resist such attacks, often used in composite signatures alongside classical algorithms like Ed25519 to ensure backward compatibility and defense-in-depth. SECCOMP and NO_NEW_PRIVS are Linux kernel mechanisms used to restrict system calls and prevent processes from gaining new privileges, which are essential for securing daemons like sshd against exploitation.

<details><summary>References</summary>
<ul>
<li><a href="https://docs.armchain.org/pqc/mldsa44">ML - DSA - 44 | Armchain Docs</a></li>
<li><a href="https://www.kernel.org/doc/html/latest/userspace-api/no_new_privs.html">No New Privileges Flag — The Linux Kernel documentation</a></li>

</ul>
</details>

**Tags**: `#OpenSSH`, `#Post-Quantum Cryptography`, `#Security`, `#Systems Administration`

---

<a id="item-5"></a>
## [Tencent Open-Sources Hy3 Preview: 295B MoE Model for Reasoning](https://t.me/zaihuapd/42385) ⭐️ 8.0/10

Tencent has officially released and open-sourced the Hy3 preview language model, a 295B parameter Mixture-of-Experts (MoE) architecture optimized for complex reasoning and agent applications. This model activates only 21B parameters per inference while supporting a 256K context length. This release significantly lowers the barrier for deploying large-scale reasoning models by combining massive capacity with efficient inference costs suitable for mid-tier GPU clusters. It positions Tencent's open-source ecosystem as a strong competitor in the STEM reasoning and code development sectors. Hy3 preview features a rebuilt infrastructure where the model architecture deeply synergizes with the inference framework, reducing first token latency by 54% in products like CodeBuddy. It integrates fast and slow thinking mechanisms to enhance performance in mathematics, science, and coding tasks.

telegram · zaihuapd · Jul 6, 10:09

**Background**: Mixture-of-Experts (MoE) is an LLM architecture that allows models to have massive total parameters while activating only a small fraction during inference, improving efficiency. Unlike dense models where all parameters are used for every token, MoE routes inputs to specific 'expert' sub-networks, reducing computational load. This approach enables larger, smarter models to run on more affordable hardware.

<details><summary>References</summary>
<ul>
<li><a href="https://techjacksolutions.com/ai-brief/tencent-open-sources-hy3-preview-295b-moe-model-with-21b-act/">Tencent Open-Sources Hy3-preview: 295B MoE Model with 21B Active Parameters Built for STEM Reasoning</a></li>
<li><a href="https://huggingface.co/blog/imnotkitty/hy3-preview">Hy3 preview: A Rebuilt Hunyuan, a 21B-Active MoE, and a New Reasoning Receipe</a></li>
<li><a href="https://github.com/Tencent-Hunyuan/Hy3-preview">GitHub - Tencent-Hunyuan/Hy3-preview: Hy3 preview (295B A21B), a leading reasoning and agent model in its size, with great cost efficiency · GitHub</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#Open Source`, `#MoE`, `#Tencent`, `#AI Models`

---