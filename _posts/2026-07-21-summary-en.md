---
layout: default
title: "Horizon Summary: 2026-07-21 (EN)"
date: 2026-07-21
lang: en
---

> From 64 items, 8 important content pieces were selected

---

1. [Google Releases Gemini 3.6 Flash, 3.5 Flash-Lite, and 3.5 Flash Cyber Models](#item-1) ⭐️ 8.0/10
2. [Court Rules Apple Not Liable for Failing to Scan iCloud for CSAM](#item-2) ⭐️ 8.0/10
3. [OpenAI Launches Third-Party Advertising in ChatGPT](#item-3) ⭐️ 8.0/10
4. [Anthropic’s Claude Code Team Shares Internal AI Tooling Practices](#item-4) ⭐️ 8.0/10
5. [Linux Kernel Community Debates Role of Large Language Models](#item-5) ⭐️ 8.0/10
6. [Google Develops 'Frozen v2' Chip to Hardwire Gemini Efficiency](#item-6) ⭐️ 8.0/10
7. [Cloudflare Launches Internal DNS Service for Private Networks](#item-7) ⭐️ 8.0/10
8. [消息称台积电考虑明年将高端工艺制程涨价 5%~10%  台积电正在考虑 2026 年将其所有高端工艺制程提高 5%~10% 的价格，以抵消美国关税、汇率波动和供](#item-8) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Google Releases Gemini 3.6 Flash, 3.5 Flash-Lite, and 3.5 Flash Cyber Models](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-6-flash-3-5-flash-lite-3-5-flash-cyber/) ⭐️ 8.0/10

Google has announced the release of three new models in its Gemini Flash family: Gemini 3.6 Flash, 3.5 Flash-Lite, and 3.5 Flash Cyber, expanding options for developers seeking speed-optimized inference. This release updates the Flash lineup with newer iterations and specialized variants like Cyber, though mixed community sentiment indicates uncertainty about whether these models deliver clear performance gains over competitors or justify their pricing. Community analysis highlights that Gemini 3.6 Flash pricing has increased to $1.5/$7.5 per million input/output tokens compared to previous generations, while Gemini 3.5 Flash-Lite is priced at $0.3/$2.5, and the Cyber variant remains unavailable to some users through the API.

hackernews · logickkk1 · Jul 21, 15:17 · [Discussion](https://news.ycombinator.com/item?id=48993414)

**Background**: Gemini is a family of multimodal large language models developed by Google DeepMind, succeeding earlier architectures like LaMDA and PaLM 2, and includes variants such as Pro, Deep Think, Flash, and Flash Lite designed for different speed and capability trade-offs. The Flash series specifically targets high-speed inference, allowing developers to run models faster while maintaining competitive intelligence, and these models are accessible through Google Cloud's Model Garden and the Gemini Enterprise Agent Platform.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Gemini_(language_model)">Gemini (language model ) - Wikipedia</a></li>
<li><a href="https://deepmind.google/models/gemini/flash/">Gemini 3.5 Flash — Google DeepMind</a></li>
<li><a href="https://ai.google.dev/gemini-api/docs/models">Models | Gemini API | Google AI for Developers</a></li>

</ul>
</details>

**Discussion**: Community discussion reveals skepticism regarding the lack of accompanying Pro models and questions about whether the new Flash versions offer meaningful improvements, while users also compare pricing unfavorably against competitors like GLM 5.2 and report frustrations with Google Workspace integration and setup processes.

**Tags**: `#Google Gemini`, `#AI Model Release`, `#Large Language Models`, `#Machine Learning`, `#Tech Industry`

---

<a id="item-2"></a>
## [Court Rules Apple Not Liable for Failing to Scan iCloud for CSAM](https://blog.ericgoldman.org/archives/2026/07/apple-defeats-liability-for-not-scanning-icloud-for-csam-but-the-judge-was-not-pleased-amy-v-apple.htm) ⭐️ 8.0/10

A federal judge ruled that Apple cannot be held civilly liable for failing to proactively scan iCloud Photos for child sexual abuse material (CSAM). The decision confirms that offering end-to-end encrypted cloud storage does not create legal exposure simply because a provider chooses not to implement client-side scanning. This ruling significantly weakens legislative strategies that attempt to force mandatory scanning through civil liability threats rather than direct encryption bans. It preserves the legal viability of strong encryption while shifting the policy debate toward statutory mandates, backdoor requirements, or platform intermediary liability reforms. The presiding judge expressed discomfort with the outcome, noting that privacy protections effectively leave victimized children as collateral damage when scanning mandates are absent. Apple previously tested a NeuralHash-based client-side scanning system in 2021 before abandoning it amid privacy backlash, and this case now tests whether existing material-support statutes can reach encrypted service providers.

hackernews · speckx · Jul 21, 14:31 · [Discussion](https://news.ycombinator.com/item?id=48992870)

**Background**: End-to-end encryption ensures that only the communicating parties can access plaintext data, preventing cloud providers from reading or scanning stored files on their servers. Client-side scanning performs content matching directly on a user's device before upload, which critics argue requires weakening or bypassing encryption entirely. Legislative proposals like the EARN IT Act have tried to condition platform liability protections on encryption practices, raising concerns that such frameworks could effectively mandate decryption capabilities.

<details><summary>References</summary>
<ul>
<li><a href="https://cyberlaw.stanford.edu/blog/2020/01/earn-it-act-how-ban-end-end-encryption-without-actually-banning-it/">The EARN IT Act: How to Ban End-to-End Encryption Without Actually Banning It</a></li>
<li><a href="https://www.3cl.org/the-death-of-end-to-end-encryption-csam-detection/">The Death of End-to-end Encryption - Child Sexual... - 3CL Foundation</a></li>

</ul>
</details>

**Discussion**: Commenters highlighted a policy imbalance where extensive resources target post-hoc CSAM detection rather than preventing actual child sexual abuse, while others defended Apple's privacy stance relative to broader industry practices. Several users questioned whether true end-to-end encryption can exist when the same company controls the servers, maintains closed-source code, and retains theoretical access to decrypted data. One participant also pointed out the legal irony of criminalizing evidence-preserving actions like possessing CSAM, which can paradoxically reduce the ability to detect and prosecute underlying abuse.

**Tags**: `#Privacy`, `#End-to-End Encryption`, `#Legal Precedent`, `#Cloud Security`, `#CSAM Policy`

---

<a id="item-3"></a>
## [OpenAI Launches Third-Party Advertising in ChatGPT](https://ads.openai.com/) ⭐️ 8.0/10

OpenAI has officially opened ChatGPT to third-party advertising through its new ads portal, introducing sponsored content into the AI assistant experience. This marks a major shift in how the company plans to monetize its free-tier users while maintaining its subscription model. This move represents a significant industry shift toward integrating traditional digital advertising into conversational AI products, directly impacting user experience and trust dynamics. It sets a precedent for other AI companies facing similar pressure to monetize large-scale free services without relying solely on paid subscriptions. The ads are reportedly required to be clearly labeled and kept separate from AI-generated answers, though community observers worry these boundaries may gradually erode over time. OpenAI emphasizes strict advertiser requirements aimed at prioritizing user interests, but the long-term implementation details remain limited.

hackernews · montecarl · Jul 21, 18:58 · [Discussion](https://news.ycombinator.com/item?id=48996571)

**Background**: ChatGPT has grown into one of the most widely used AI assistants globally, relying heavily on a freemium business model where most users access the service for free while a smaller portion pays for premium features. As hosting and running large language models becomes increasingly expensive, many tech platforms have historically turned to advertising to subsidize free access. The integration of ads into an AI chat interface raises unique questions about how conversational context, recommendation algorithms, and user privacy intersect with traditional ad delivery.

**Discussion**: Community sentiment is mixed, with some users cautiously accepting ads as a necessary monetization strategy, while others express sharp concern that labeled and separated ads will gradually degrade the user experience like streaming platforms did. Several commenters also satirized the potential for subtle brand manipulation and noted the strategic timing of the launch amid the open-source versus proprietary AI debate.

**Tags**: `#AI Monetization`, `#ChatGPT`, `#Digital Advertising`, `#Product Strategy`, `#User Experience`

---

<a id="item-4"></a>
## [Anthropic’s Claude Code Team Shares Internal AI Tooling Practices](https://simonwillison.net/2026/Jul/21/cat-and-thariq/#atom-everything) ⭐️ 8.0/10

Simon Willison published an edited transcript of a fireside chat with Anthropic’s Cat Wu and Thariq Shihipar, revealing that Claude Tag now handles 65% of the Claude Code team’s product engineering pull requests. The discussion also highlights how Claude Code features are dogfooded internally before public release and how newer models like Fable 5 have drastically simplified system prompting. This conversation offers a rare look at how an AI lab actually builds its own developer tools, showing that internal adoption metrics and retention data now drive feature shipping decisions. As coding agents become central to software engineering workflows, these practices set a benchmark for safety, automation, and prompt engineering in the industry. The team reduced the Claude Code system prompt by 80% because adding few-shot examples or negative constraint lists now degrades performance on Fable 5 and Opus 4.8. Meanwhile, critical code changes still require manual review, while automated review increasingly covers the product’s outer layers, and Claude Tag relies heavily on auto mode to coordinate shared Slack channels.

rss · Simon Willison · Jul 21, 12:54

**Background**: Claude Code is Anthropic’s terminal-based coding agent that helps developers write, edit, and review code autonomously, while Claude Tag extends this capability into collaborative Slack workspaces where team members share a single Claude instance. Evals refer to structured evaluation frameworks used to measure model reliability, alignment, and task performance through repeatable test suites. The shift away from verbose system prompts reflects a broader industry trend where larger, more capable foundation models require less hand-holding and respond better to concise instructions.

<details><summary>References</summary>
<ul>
<li><a href="https://www.anthropic.com/news/introducing-claude-tag">Introducing Claude Tag \ Anthropic</a></li>
<li><a href="https://www.anthropic.com/claude/fable">Claude Fable \ Anthropic</a></li>
<li><a href="https://support.claude.com/en/articles/15594475-what-is-claude-tag">What is Claude Tag? | Claude Help Center</a></li>

</ul>
</details>

**Tags**: `#Claude Code`, `#AI coding assistants`, `#Anthropic`, `#developer tools`, `#coding agents`

---

<a id="item-5"></a>
## [Linux Kernel Community Debates Role of Large Language Models](https://lwn.net/Articles/1083275/) ⭐️ 8.0/10

The Linux kernel community is engaging in a broad debate about integrating large language models into development processes, moving beyond Linus Torvalds' recent strong statements. Discussions now cover attribution requirements, code-review tools, reliance on proprietary systems, and ethical concerns. This debate is crucial as it defines the ethical and practical boundaries of using AI in one of the world's most critical open-source projects. The outcomes will likely influence governance and tooling standards across the broader open-source ecosystem. Notable technical and policy details include requirements for attributing LLM assistance in contributions and the risks associated with depending on proprietary code-review tools. These issues highlight the conflict between leveraging AI efficiency and maintaining open-source transparency and independence.

rss · LWN.net · Jul 21, 13:48

**Background**: The Linux kernel serves as the core of the Linux operating system and is developed through a highly collaborative, distributed process involving thousands of contributors. As generative AI becomes common in software engineering, communities must decide how to handle AI-generated code, training data ethics, and third-party tool dependencies without compromising their values.

**Tags**: `#Linux Kernel`, `#Large Language Models`, `#Open Source`, `#AI Ethics`, `#Software Development`

---

<a id="item-6"></a>
## [Google Develops 'Frozen v2' Chip to Hardwire Gemini Efficiency](https://www.quiverquant.com/news/Google+Reportedly+Developing+%E2%80%98Frozen+v2%E2%80%99+AI+Chip+to+Boost+Gemini+Efficiency) ⭐️ 8.0/10

Google is reportedly developing an internal AI server chip codenamed “Frozen v2” that embeds parts of the Gemini model architecture directly into silicon. The chip targets 6 to 10 times more AI tokens per unit of power than Google’s latest TPUs and is planned for deployment in 2028. This move signals a major industry shift toward application-specific AI silicon designed to maximize inference efficiency rather than relying solely on general-purpose accelerators. It could significantly ease Google Cloud’s internal compute shortages and improve the cost-effectiveness of serving enterprise customers. Frozen v2 is positioned as a complement to, not a replacement for, Google’s existing TPU lineup within its custom silicon portfolio. The reported efficiency gains are measured in tokens per watt, a key metric for evaluating AI infrastructure ROI and energy consumption during model inference.

telegram · zaihuapd · Jul 21, 01:01

**Background**: Custom AI chips, often called ASICs or application-specific integrated circuits, are designed to accelerate particular workloads like large language model inference by hardwiring specific operations into hardware. As generative AI demand surges, companies increasingly prioritize tokens per watt over raw FLOPs because energy costs and data center cooling constraints have become critical bottlenecks. Google has long developed its own TPUs for training and running models internally, making this new Gemini-focused design a strategic evolution of its silicon roadmap.

<details><summary>References</summary>
<ul>
<li><a href="https://techcrunch.com/2026/07/20/google-is-working-on-a-new-ai-chip-designed-to-make-gemini-more-efficient/">Google is working on a new AI chip designed to make Gemini ...</a></li>
<li><a href="https://qz.com/google-gemini-chip-frozen-tpu-efficiency-072026">Google developing Gemini-specific chip called Frozen v2</a></li>

</ul>
</details>

**Tags**: `#AI Hardware`, `#Google`, `#Gemini`, `#Custom Silicon`, `#Inference Efficiency`

---

<a id="item-7"></a>
## [Cloudflare Launches Internal DNS Service for Private Networks](https://blog.cloudflare.com/internal-dns/) ⭐️ 8.0/10

Cloudflare officially launched its Internal DNS service on July 20, 2026, providing authoritative and recursive DNS resolution for enterprise private networks. This service integrates with Cloudflare's public DNS and Zero Trust platform on a unified global control plane. By consolidating public and private DNS into a single platform, Cloudflare reduces the complexity and data drift risks associated with managing multiple DNS systems. It also extends Zero Trust security policies to the domain resolution layer, enabling granular access control based on users and devices. Existing Cloudflare Gateway customers can enable this service at no additional cost, and the "DNS views" feature simplifies split-horizon configuration. The service supports deployment through API, Terraform, and Cloudflare WAN.

telegram · zaihuapd · Jul 21, 03:49

**Background**: DNS (Domain Name System) translates domain names into IP addresses and is fundamental to how networks route traffic for both public and private environments. Split-horizon DNS traditionally requires maintaining separate configurations for internal and external queries to ensure security and correct routing. Cloudflare's Zero Trust platform secures application access without a traditional VPN, making integrated DNS management a key component of its security architecture.

**Tags**: `#Cloudflare`, `#DNS`, `#Zero Trust`, `#Enterprise Networking`, `#Cloud Infrastructure`

---

<a id="item-8"></a>
## [消息称台积电考虑明年将高端工艺制程涨价 5%~10%  台积电正在考虑 2026 年将其所有高端工艺制程提高 5%~10% 的价格，以抵消美国关税、汇率波动和供](https://t.me/zaihuapd/42691) ⭐️ 8.0/10

TSMC is reportedly considering raising prices for its high-end process nodes by 5-10% in 2026 to offset tariffs and supply chain costs, increasing expenses for key customers like Nvidia and Apple.

telegram · zaihuapd · Jul 21, 09:28

**Tags**: `#Semiconductors`, `#TSMC`, `#Supply Chain`, `#Pricing Strategy`, `#AI Hardware`

---