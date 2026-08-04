---
layout: default
title: "Horizon Summary: 2026-08-04 (ZH)"
date: 2026-08-04
lang: zh
---

> 从 81 条内容中筛选出 4 条重要资讯。

---

1. [Keyv 及相关 npm 包在活跃的 Shai-Hulud 供应链攻击中被入侵](#item-1) ⭐️ 8.0/10
2. [Xbox 现在需要联网才能游玩光盘游戏](#item-2) ⭐️ 8.0/10
3. [AI 智能体自我改进的 Harness 工程](#item-3) ⭐️ 8.0/10
4. [探索式建模为生成模型增添第三个预训练维度](#item-4) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Keyv 及相关 npm 包在活跃的 Shai-Hulud 供应链攻击中被入侵](https://www.aikido.dev/blog/keyv-and-friends-compromised-in-npm-supply-chain-attack) ⭐️ 8.0/10

名为 Shai-Hulud 的自我复制蠕虫已通过活跃的供应链攻击入侵了超过 500 个 npm 包，包括广泛使用的 Keyv 键值存储库。CISA 已发布警报确认 npm 生态系统遭受了大规模入侵。 此次攻击意义重大，因为 npm 是世界上最大的 JavaScript 包注册表，而 Shai-Hulud 的自我复制特性意味着被入侵的包可以进一步传播攻击。这一事件凸显了依赖管理中存在的严重漏洞，影响着全球的开发者和企业。 该攻击利用预安装钩子入侵包，Keyv 是受影响的库之一。CISA 报告称超过 500 个包已被入侵，且蠕虫的自我复制能力使其能够快速在整个生态系统中传播。

hackernews · cimi_ · 8月4日 11:01 · [社区讨论](https://news.ycombinator.com/item?id=49166874)

**背景**: npm（Node Package Manager）是 JavaScript 的默认包管理器，也是世界上最大的软件注册表，托管着全球开发者使用的数百万个包。供应链攻击通过入侵开发者依赖的包来针对软件开发流程，通常是通过预安装或后安装钩子注入恶意代码。Shai-Hulud 蠕虫代表了一种复杂的攻击，它可以在被入侵的存储库之间自我复制。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.cisa.gov/news-events/alerts/2025/09/23/widespread-supply-chain-compromise-impacting-npm-ecosystem">Widespread Supply Chain Compromise Impacting npm Ecosystem | CISA</a></li>
<li><a href="https://unit42.paloaltonetworks.com/npm-supply-chain-attack/">"Shai-Hulud" Worm Compromises npm Ecosystem in Supply Chain Attack (Updated November 26)</a></li>

</ul>
</details>

**社区讨论**: 社区成员对 npm 依赖系统的脆弱性表示强烈担忧，呼吁禁止预安装钩子，有人建议暂停新增钩子。大家分享了设置 min-release-age=5 等实用缓解策略，还有人质疑商业企业安全工具是否能有效检测和主动阻止此类攻击。

**标签**: `#supply-chain-security`, `#npm`, `#cybersecurity`, `#open-source`, `#dependency-management`

---

<a id="item-2"></a>
## [Xbox 现在需要联网才能游玩光盘游戏](https://birchtree.me/blog/xbox-goes-down-you-cant-play-games-you-own-on-disc/) ⭐️ 8.0/10

微软现在要求 Xbox 主机必须联网才能游玩光盘游戏，这与之前世代可以在离线状态下游玩实体光盘的做法形成鲜明对比。该政策影响新游戏和二手游戏光盘，实际上取消了无需在线验证即可游玩已购游戏的权利。 这一发展标志着游戏行业中数字所有权的重大倒退，消费者无法再保证长期访问已实体购买的游戏。它延续了音乐、电影和电视行业中看到的更广泛趋势，即实体媒体正被订阅制或始终在线模式所取代，限制了消费者权利。 该要求适用于单人游戏，这一点值得关注，因为 PS3 等前世代主机仅将在线服务器用于匹配，而游戏本身在主机本地运行。社区成员指出，Xbox One 时代曾因始终在线 DRM 面临类似强烈反对，微软随后扭转了政策，人们担心这一举措可能是一种倒退。

hackernews · surprisetalk · 8月4日 12:01 · [社区讨论](https://news.ycombinator.com/item?id=49167448)

**背景**: 数字版权管理（DRM）是指限制数字内容使用、访问或分发的技术保护措施。游戏行业正日益向数字分发和在线认证转变，Steam 等公司和主机制造商实施了与账户绑定的购买方式。实体光盘传统上被视为真正所有权的最后堡垒，允许玩家安装、离线游玩、转售和永久保存游戏——而这些权利正在被系统性地剥夺。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Digital_rights_management">Digital rights management - Wikipedia</a></li>
<li><a href="https://hardforum.com/threads/xbox-always-on-drm-is-back.2010751/">Xbox always on DRM is back. | [H] ard|Forum</a></li>
<li><a href="https://popcar.bearblog.dev/its-about-ownership/">It's not about physical vs digital games, it's about ownership – Popcar's Blog</a></li>

</ul>
</details>

**社区讨论**: 社区情绪普遍负面，用户们对失去所有权权利表示沮丧，并将其与电视、电影和音乐行业已放弃实体媒体的情况相提并论。评论者强调，核心问题不在于实体与数字格式之争，而在于永久拥有内容、离线使用、转售以及传递给后代的权利。部分用户还批评了这些始终在线政策所伴随的繁琐登录和验证流程，包括验证码要求。

**标签**: `#gaming`, `#digital ownership`, `#consumer rights`, `#Xbox`, `#industry trends`

---

<a id="item-3"></a>
## [AI 智能体自我改进的 Harness 工程](https://lilianweng.github.io/posts/2026-07-04-harness/) ⭐️ 8.0/10

Lilian Weng 的博客文章探讨了 AI 智能体的 harness（即编排提示词、工具调用、子智能体、控制流、记忆和工作流逻辑的代码）如何通过工程手段实现自我改进，包括自动化训练数据生成、优化提示词和代码，以及开发超越传统权重训练的适应度函数。这项工作建立在 Self-Taught Optimizer (STOP) 等早期研究的基础上，也与上海人工智能实验室近期提出的 Self-Harness 框架相呼应，该框架允许智能体重写自身规则并将性能提升高达 60%。 这代表了 AI 开发范式的转变：除了通过权重训练改进模型外，我们现在可以优化运行智能体的 harness 代码，从而进入一个更大的设计空间。随着权重训练逐渐面临收益递减，harness 工程为提升 AI 智能体的能力、效率和自主性开辟了新的前沿，直接影响组织构建和部署智能体系统的方式。 Harness 是编排提示词、工具调用、子智能体、控制流、记忆和工作流逻辑协同工作的代码。关键技术挑战包括为代码库定义可靠的适应度函数、创建评估和验证集以防止奖励黑客行为，以及让智能体能够编写自己的工具——例如通过 session_context 工具将 2 万 token 的多次调用流程压缩为 800 token 的单次调用。

hackernews · tosh · 8月4日 06:17 · [社区讨论](https://news.ycombinator.com/item?id=49164896)

**背景**: AI 智能体 harness 指的是协调 AI 智能体系统所有组件的编排层——包括提示词的结构、工具调用方式、子智能体如何委派任务、记忆如何管理，以及控制流和工作流逻辑如何执行。传统的 AI 改进主要聚焦于训练模型权重（例如通过 RLHF/DPO），但 harness 工程将智能体的运行代码视为可优化的对象。上海人工智能实验室的 Self-Harness 框架展示了这一范式，让基于大语言模型的智能体系统性地改进自身运行规则，性能提升高达 60%。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://lilianweng.github.io/posts/2026-07-04-harness/">Harness Engineering for Self-Improvement | Lil'Log</a></li>
<li><a href="https://venturebeat.com/orchestration/researchers-introduce-self-harness-a-framework-that-lets-ai-agents-rewrite-their-own-rules-boosting-performance-up-to-60">Researchers introduce Self-Harness, a framework that lets AI agents rewrite their own rules, boosting performance up to 60% | VentureBeat</a></li>

</ul>
</details>

**社区讨论**: 社区对超越权重训练的前景充满热情，有评论者指出'训练权重已接近瓶颈'，主张转向聚焦提示词和代码的新范式。实际讨论集中在如何为代码库定义质量指标和适应度函数，也有人分享了自动研究方法的实践经验——强调需要生产环境轨迹、自定义工具创建以及合理的评估划分以防止奖励黑客行为。此外，还有人对 harness 能否最终自主生成 RLHF/DPO 训练数据并对模型进行 LoRA 微调表示关注。

**标签**: `#AI Agents`, `#Machine Learning`, `#Self-Improvement`, `#RLHF`, `#Prompt Engineering`

---

<a id="item-4"></a>
## [探索式建模为生成模型增添第三个预训练维度](https://www.reddit.com/r/MachineLearning/comments/1vf6r6f/explorative_modeling_unlocking_a_third/) ⭐️ 8.0/10

Gladstone 等人（2026）提出了探索式建模，这是一种新的范式，在传统参数和数据两个预训练维度之外增加了探索维度。该方法通过对训练循环进行分解，探索模型生成与数据之间的 K 个候选匹配，并在最佳匹配上进行训练，从而实现端到端生成。 这是一项对 AI/ML 领域的重要技术贡献，因为扩展探索维度可以单调地提升现有生成模型在图像、视频和语言等连续和离散领域中的性能。它通过引入新的缩放维度，从根本上重新定义了我们对生成模型训练方式的理解。 该方法通过探索模型生成与数据之间的 K 个候选匹配，然后在最佳匹配上进行训练，这有助于预测聚焦于模式而非模糊它们。在最简单的形式下，该方法被描述为一个 for 循环，使其相对容易集成到现有框架中。

reddit · r/MachineLearning · /u/Benlus · 8月4日 10:42

**背景**: 传统生成建模有两个主要的分解维度：分解生成过程和分解训练过程。扩展通常集中在这两个维度上——增加模型参数和收集更多训练数据。这项研究将探索识别为第三个独立维度，可以沿此维度扩展生成表达能力，与现有两个维度形成补充。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://explorative-modeling.github.io/">Explorative Modeling : Unlocking a Third Pretraining Axis and...</a></li>
<li><a href="https://paperswithcode.co/paper/2607.27372">Explorative Modeling : Unlocking a Third Pretraining Axis and...</a></li>
<li><a href="https://digg.com/tech/mrt8e84i">Paper Frames Exploration as Third Pretraining Axis · Digg</a></li>

</ul>
</details>

**社区讨论**: 该论文在 r/MachineLearning 上引发了讨论，评分为 8.0/10，表明社区对此想法有较高的关注度。社区似乎对将探索作为可缩放维度这一新颖框架很感兴趣。

**标签**: `#AI/ML`, `#Research`, `#Pretraining`, `#Generative Models`, `#Machine Learning`

---