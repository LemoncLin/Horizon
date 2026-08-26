---
layout: default
title: "Horizon Summary: 2026-08-26 (ZH)"
date: 2026-08-26
lang: zh
---

> 从 101 条内容中筛选出 11 条重要资讯。

---

1. [vLLM v0.28.0 发布，针对 Kimi-K3 和 DeepSeek V4 的重大优化](#item-1) ⭐️ 8.0/10
2. [Qwen 发布 125B 参数 Qwen3.8-Flash-Next，采用新型 N-gram 旁路架构](#item-2) ⭐️ 8.0/10
3. [自动化机器人平台实现遗传密码重新设计原型](#item-3) ⭐️ 8.0/10
4. [细胞类型特异性 eQTL 驱动复杂性状的遗传力](#item-4) ⭐️ 8.0/10
5. [两栖原始昆虫揭示陆地 colonization 之谜](#item-5) ⭐️ 8.0/10
6. [CrSb 中 3D 体分辨的 g 波交换磁序参量](#item-6) ⭐️ 8.0/10
7. [结合-释放策略实现靶向抗癌药物递送](#item-7) ⭐️ 8.0/10
8. [兴奋性神经元中异常的 ERBB4 信号驱动阿尔茨海默病病理](#item-8) ⭐️ 8.0/10
9. [神经场算法实现高分辨率 VLBI 视频重建](#item-9) ⭐️ 8.0/10
10. [内源性大麻素通过逆行增益控制驱动奖赏参与](#item-10) ⭐️ 8.0/10
11. [《自然》研究揭示人 UGCG 的冷冻电镜结构及新型催化机制](#item-11) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [vLLM v0.28.0 发布，针对 Kimi-K3 和 DeepSeek V4 的重大优化](https://github.com/vllm-project/vllm/releases/tag/v0.28.0) ⭐️ 8.0/10

vLLM v0.28.0 是一个重大版本更新，包含来自 270 位贡献者的 584 个提交，为 Kimi-K3 和 DeepSeek V4 提供了显著的性能优化，包括新的并行策略、融合算子和 ROCm 支持。 此次发布为两个最受欢迎的近期模型大幅提升了 LLM 推理性能，使 vLLM 在 Kimi-K3 和 DeepSeek V4 的生产部署中更具竞争力，同时将硬件支持扩展至 AMD ROCm 平台。 关键技术改进包括为 Kimi-K3 提供的解码上下文并行（DCP）技术，在长上下文工作负载上实现 3 倍吞吐量提升，融合 FlashKDA 算子，自适应投机 token 预算带来约 60%的 DSpark TTFT 改善，以及 DeepSeek V4 的端到端稀疏 MLA 支持。

github · khluu · 8月26日 09:46

**背景**: vLLM 是一个广泛使用的开源 LLM 推理引擎，以其 PagedAttention 机制和高吞吐量服务能力著称。投机解码是一种技术，通过较小的草稿模型生成候选 token，再由较大的目标模型进行验证，从而提升推理速度。DeepSeek 的 MLA（多头隐式注意力）是一种高效的注意力机制，可减少 KV 缓存内存使用，而 DSpark 是 DeepSeek 的投机解码框架，可实现 60-85%的推理加速。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://vllm.ai/blog/2026-08-07-decode-context-parallelism">Efficient Decode Context Parallelism with vLLM for Long... | vLLM Blog</a></li>
<li><a href="https://www.banandre.com/blog/deepseek-dspark-speculative-decoding-breakthrough">DeepSeek DSpark : The 85% Speed Hack That Makes... - Banandre</a></li>

</ul>
</details>

**标签**: `#vLLM`, `#LLM inference`, `#GPU optimization`, `#DeepSeek`, `#Kimi-K3`

---

<a id="item-2"></a>
## [Qwen 发布 125B 参数 Qwen3.8-Flash-Next，采用新型 N-gram 旁路架构](https://qwen.ai/blog?id=qwen3.8-flash-next) ⭐️ 8.0/10

Qwen 于 2026 年 8 月 26 日发布了 Qwen3.8-Flash-Next，这是一款 125B 参数的开源实验模型，其主模型搭配了 51B 的 N-gram 嵌入和 4B 的多令牌预测模块，每令牌仅激活 6B 参数。 该模型预览了旨在支撑 Qwen4 的架构，与 Qwen3.7-Plus 相比大幅降低了训练和推理成本，同时提供了更优的代码能力。 模型在磁盘上的总大小约为 180B 参数，但每令牌仅激活 6B。50B 的 ngram 旁路组件引发了在 RAM 有限的消费级硬件上部署可行性的担忧。

hackernews · tosh · 8月26日 12:52 · [社区讨论](https://news.ycombinator.com/item?id=49448210)

**背景**: N-gram 旁路架构利用 n-gram 匹配作为推测解码的一种形式，其中先前出现的令牌序列被用作草稿预测以加速推理。这种方法以额外的内存换取减少的计算需求，使较小的激活参数集能够达成与大型密集模型相当的性能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/QwenLM/Qwen3.8-Flash-Next/">Qwen3.8-Flash-Next - GitHub</a></li>
<li><a href="https://www.marktechpost.com/2026/08/26/alibabas-qwen-team-releases-qwen3-8-flash-next-a-125b-multimodal-moe-with-6b-active-parameters-previewing-the-qwen4-architecture/">Alibaba's Qwen Team Releases Qwen3.8-Flash-Next: A 125B ...</a></li>

</ul>
</details>

**社区讨论**: 社区成员正在讨论在有限硬件上的部署可行性，有人担心 50B 的 ngram 旁路组件会使该模型对仅有 32-64GB RAM 的用户无法使用。部分用户表示惊讶于该模型未能超越较小的 Qwen 3.8 27B 版本，而另一些人则注意到 LLM 时间线上的惊人速度提升。

**标签**: `#LLM`, `#Qwen`, `#model-release`, `#self-hosting`, `#ngram`

---

<a id="item-3"></a>
## [自动化机器人平台实现遗传密码重新设计原型](https://www.nature.com/articles/s41586-026-10949-y) ⭐️ 8.0/10

乔治·丘奇团队开发的机器人无细胞平台实现了重新设计遗传密码的快速原型制作，无需修改活体基因组即可实现密码子重新分配和非标准氨基酸的蛋白质翻译。该成果于 2026 年 8 月 26 日发表在《自然》杂志上，代表了合成生物学自动化的重大进展。 这一突破通过提供自动化、高通量的遗传密码工程方法推进了合成生物学的发展，有望加速蛋白质工程和非标准氨基酸新型治疗药物的开发。由于在无细胞条件下运行，它避免了修改生物体基因组所带来的复杂性和伦理问题。 该平台在无细胞条件下运行，无需修改活细胞。它通过正交氨酰-tRNA 合成酶/tRNA 对在体外系统中实现密码子重新分配和非标准氨基酸的掺入，正如《自然》论文（doi:10.1038/s41586-026-10949-y）所述。

rss · Nature · 8月26日 00:00

**背景**: 无细胞蛋白质合成（CFPS）是一种利用提取的细胞机器（如核糖体和酶）在活细胞外生成蛋白质的技术，为蛋白质生产提供了灵活的平台。遗传密码扩展是合成生物学的一种方法，通过将密码子（通常是终止密码子）重新分配来将非标准氨基酸掺入蛋白质，从而扩展蛋白质的化学多样性。这项研究建立在正交翻译系统数十年工作的基础上，具有包括偶联疫苗开发在内的治疗应用前景。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Cell-free_protein_synthesis">Cell-free protein synthesis - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Expanded_genetic_code">Expanded genetic code - Wikipedia</a></li>
<li><a href="https://www.frontiersin.org/journals/chemistry/articles/10.3389/fchem.2014.00034/full">Frontiers | Non-standard amino acid incorporation into proteins using Escherichia coli cell-free protein synthesis</a></li>

</ul>
</details>

**标签**: `#synthetic biology`, `#genetic engineering`, `#protein engineering`, `#automated platforms`, `#non-standard amino acids`

---

<a id="item-4"></a>
## [细胞类型特异性 eQTL 驱动复杂性状的遗传力](https://www.nature.com/articles/s41586-026-10577-6) ⭐️ 8.0/10

2026 年 8 月 26 日发表在《自然》杂志的一项研究表明，单细胞 RNA 测序揭示细胞类型特异性表达数量性状位点（eQTL）是复杂性状遗传力的主要驱动因素，确立了细胞类型特异性基因调控作为连接遗传变异与表型性状的关键机制。 这项突破通过证明细胞类型特异性 eQTL 图谱对于理解遗传变异如何影响复杂性状和疾病至关重要，推进了遗传架构领域的发展，有望改变精准医学和功能基因组学研究。 该研究利用单细胞转录组数据来识别遗传变异对基因表达的细胞类型特异性效应，超越了在异质性细胞群体中平均信号的批量 RNA 测序方法。

rss · Nature · 8月26日 00:00

**背景**: 表达数量性状位点（eQTL）是与基因表达水平变异相关的基因组区域，充当遗传变异与分子表型之间的桥梁。传统的 eQTL 研究使用批量 RNA 测序，该方法在多种细胞类型中平均表达信号，可能遗漏细胞类型特异性的调控效应。单细胞基因组学现在能够在细胞分辨率下进行 eQTL 图谱绘制，揭示遗传变异如何在与复杂性状和疾病相关的特定细胞背景下发挥作用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Expression_quantitative_trait_loci">Expression quantitative trait loci - Wikipedia</a></li>

</ul>
</details>

**标签**: `#genetics`, `#single-cell genomics`, `#eQTL`, `#complex traits`, `#Nature`

---

<a id="item-5"></a>
## [两栖原始昆虫揭示陆地 colonization 之谜](https://www.nature.com/articles/s41586-026-10961-2) ⭐️ 8.0/10

通过对化石 Chosha praecursor 进行交叉偏振光成像和系统发育重建的重新研究，科学家确认其可能是一种早期的两栖昆虫，有助于填补化石记录中长期存在的六足类空白。该研究于 2026 年 8 月 26 日发表在《自然》杂志上。 这一发现意义重大，因为它解决了六足类空白问题——即数千万年间缺乏多样化昆虫化石的谜团——并为理解昆虫如何从水生环境向陆地环境过渡提供了关键证据，这是陆地殖民过程中的一个重要里程碑。 研究人员采用了交叉偏振光成像技术，该技术能够增强化石中精细形态特征的可视化效果，并结合系统发育重建将 Chosha praecursor 定位为早期分支的原始昆虫。该化石代表了一种两栖形态，表明其具有从水生祖先到完全陆生昆虫的过渡特征。

rss · Nature · 8月26日 00:00

**背景**: 六足类空白指的是在最早已知昆虫化石出现后，地质记录中长达数千万年间缺乏多样化昆虫化石的显著空白。昆虫以其六条腿为特征（hexa 意为六，pod 意为腿），是地球上最多样化的动物类群之一，这使得这一空白对古生物学家来说尤为令人困惑。交叉偏振光成像是一种古生物学中的标准技术，可减少眩光并增强对比度，使研究人员能够观察 otherwise 难以观察到的化石标本中的精细结构细节。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.scientificamerican.com/article/mysterious-insect-fossil-gap-explained/">Mysterious Insect Fossil Gap Explained | Scientific American</a></li>
<li><a href="https://www.tandfonline.com/doi/full/10.1080/03115518.2021.1983652">Cross-polarized light as an imaging technique for graptolites</a></li>

</ul>
</details>

**标签**: `#paleontology`, `#evolutionary biology`, `#insect evolution`, `#fossil research`, `#Nature publication`

---

<a id="item-6"></a>
## [CrSb 中 3D 体分辨的 g 波交换磁序参量](https://www.nature.com/articles/s41586-026-10902-z) ⭐️ 8.0/10

2026 年 8 月 26 日发表在《自然》杂志上的研究表明，研究人员利用量子振荡测量绘制了 CrSb 中的 g 波交换磁序参量，首次三维体分辨证实了该材料中的动量依赖自旋分裂。 这一实验突破确立了 CrSb 作为典型交换磁体的地位，证实了长期寻求的 g 波序参量和动量依赖自旋分裂，这些特性将交换磁性与传统铁磁性和反铁磁性区分开来。该发现推动了交换磁性这一新兴领域的发展，并可能催生利用自旋分裂费米面但无净磁化的新型自旋电子器件。 通过结合高场磁输运和扭矩测量以及包含自旋轨道耦合的 DFT+U 计算，研究确定了 CrSb 中四个自旋非简并能带产生的多个量子振荡频率，其中心对称六方结构具有五阶磁多极子序参量。

rss · Nature · 8月26日 00:00

**背景**: 交换磁性于 2024 年 12 月被发现，是一种第三基本磁态，其中共线自旋序产生动量依赖的自旋分裂而无净磁化，不同于铁磁体或反铁磁体。量子振荡测量通过高磁场下检测电阻等性质的振荡来绘制费米面并揭示自旋分裂能带。CrSb 是一种具有六方 NiAs 型结构的金属交换磁体，使其比 MnTe 等半导体候选材料更适合此类研究。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2601.14526">3D bulk-resolved g - wave altermagnetic order parameter in CrSb</a></li>
<li><a href="https://www.emergentmind.com/topics/bulk-g-wave-altermagnets">Bulk g - Wave Altermagnets</a></li>
<li><a href="https://arxiv.org/html/2601.19105v1">Altermagnetic spin-split Fermi surfaces in CrSb revealed by ...</a></li>

</ul>
</details>

**标签**: `#altermagnetism`, `#condensed matter physics`, `#quantum oscillations`, `#spintronics`, `#Nature research`

---

<a id="item-7"></a>
## [结合-释放策略实现靶向抗癌药物递送](https://www.nature.com/articles/s41586-026-10971-0) ⭐️ 8.0/10

研究人员开发了一种新型结合-释放药物偶联物策略，该策略无需细胞内吞即可在肿瘤部位直接释放抗癌载荷，从而在肿瘤特异性和疗效方面超越传统抗体药物偶联物。 这一突破有望将治疗靶点扩展到传统抗体药物偶联物之外，可能使针对有限靶点抗原的癌症治疗成为可能，并减少肿瘤药物开发中的脱靶毒性。 该策略依赖于可裂解连接子，在结合肿瘤相关抗原后释放药物，绕过了传统抗体药物偶联物典型的受体介导内吞作用。

rss · Nature · 8月26日 00:00

**背景**: 抗体药物偶联物（ADC）是一类靶向癌症疗法，通过连接子将单克隆抗体与细胞毒性载荷结合。它们通常需要细胞内吞才能在靶细胞内释放药物，这限制了其对某些肿瘤类型的疗效，并可能导致脱靶毒性。这种新的结合-释放方法将药物释放与内吞作用解耦，为抗癌药物递送提供了更宽的治疗窗口。

**标签**: `#cancer research`, `#drug delivery`, `#oncology`, `#biomedical engineering`, `#Nature research`

---

<a id="item-8"></a>
## [兴奋性神经元中异常的 ERBB4 信号驱动阿尔茨海默病病理](https://www.nature.com/articles/s41586-026-10964-z) ⭐️ 8.0/10

2026 年 8 月 26 日发表在《自然》杂志上的研究发现，兴奋性神经元中异常的 ERBB4 信号驱动阿尔茨海默病病理，且神经炎症可能并非早期突触丢失所必需。 这一发现挑战了神经炎症和小胶质细胞过度吞噬活性是阿尔茨海默病早期突触退化的核心因素的主流观点，可能将治疗重点从免疫途径转向神经元 ERBB4 机制。 ERBB4 是一种在多个脑区表达的关键神经调节素受体，研究表明它可能作为一个分子开关，协调超出淀粉样蛋白斑块的多种阿尔茨海默病病理变化。

rss · Nature · 8月26日 00:00

**背景**: 阿尔茨海默病以大脑皮层和边缘系统神经元的进行性认知衰退和神经退化为特征。淀粉样蛋白斑块和神经原纤维缠结长期以来被认为是标志性特征，而神经炎症——特别是小胶质细胞的过度吞噬活性——被认为与突触丢失有关。ERBB4 是神经调节素-1（NRG1）的受体，在海马和中脑突触的突触可塑性调节中发挥核心作用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nature.com/articles/s41586-026-10964-z">Aberrant excitatory neuronal ERBB4 promotes Alzheimer’s ...</a></li>
<li><a href="https://medicalxpress.com/news/2026-08-rogue-neuronal-root-alzheimer-disease.html">A rogue neuronal signal may lie at the root of Alzheimer's ...</a></li>

</ul>
</details>

**标签**: `#Alzheimer's disease`, `#neuroscience`, `#neuroinflammation`, `#ERBB4`, `#synaptic pathology`

---

<a id="item-9"></a>
## [神经场算法实现高分辨率 VLBI 视频重建](https://www.nature.com/articles/s41586-026-10988-5) ⭐️ 8.0/10

2026 年 8 月 26 日发表于《自然》杂志的 kine 神经场算法，能够生成高分辨率、时间连续的甚长基线干涉测量（VLBI）视频，实现了对相对论性天体物理喷流中瞬时等离子体速度的直接测量。 这对天体物理学而言是一项重要的方法学突破，因为传统 VLBI 成像技术难以研究的相对论性喷流现在可以进行详细的运动学分析。这也展示了机器学习对跨学科科学成像日益增长的影响。 kine 算法利用神经场以时间连续的方式重建可变 VLBI 观测数据，而非生成离散帧。这种方法克服了传统基于网格方法的局限性，能够精确测量接近超大质量黑洞以相对论速度运动的等离子体速度。

rss · Nature · 8月26日 00:00

**背景**: 甚长基线干涉测量（VLBI）是一种射电天文学技术，通过结合相距遥远的多个射电望远镜的信号来实现极高的角分辨率， effectively 形成一个口径等于望远镜间距的望远镜。神经场是一类使用神经网络表示连续函数的 AI 模型，能够从稀疏或不完整的观测数据中重建高质量图像。相对论性喷流是从超大质量黑洞附近喷发出的高能等离子体流，以接近光速的速度运动。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Very-long-baseline_interferometry">Very-long-baseline interferometry - Wikipedia</a></li>
<li><a href="https://hackernoon.com/why-neural-fields-beat-grid-based-methods-for-spatiotemporal-imaging">Why Neural Fields Beat Grid-Based Methods for... | HackerNoon</a></li>

</ul>
</details>

**标签**: `#AI/ML`, `#Astrophysics`, `#Scientific Computing`, `#Neural Fields`, `#VLBI`

---

<a id="item-10"></a>
## [内源性大麻素通过逆行增益控制驱动奖赏参与](https://www.nature.com/articles/s41586-026-10967-w) ⭐️ 8.0/10

2026 年 8 月 26 日发表于《自然》的一项研究表明，丘脑-纹状体回路中内源性大麻素的动态释放通过逆行增益控制机制调节奖赏寻求过程中的行为参与。 这一发现揭示了动机行为的关键神经调质机制，对理解成瘾、奖赏处理障碍以及神经调质干预的潜在治疗靶点具有重要意义。 内源性大麻素作为逆行信使，从突触后神经元向突触前终端反向扩散，与 G 蛋白偶联受体结合，调节丘脑-纹状体连接的突触增益和可塑性。

rss · Nature · 8月26日 00:00

**背景**: 内源性大麻素是脂质信号分子，作为中枢神经系统中的主要逆行神经递质，意味着它们沿突触反向传递而非传统的正向传递。丘脑-纹状体回路是指连接丘脑与纹状体的神经通路，是基底节的重要组成部分，参与奖赏处理和动机行为。逆行增益控制描述了一种机制，即突触后活动调节传入突触输入的强度或反应性，从而调整神经元处理信息的方式。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nature.com/articles/s41586-026-10967-w">Endocannabinoids facilitate reward engagement through ...</a></li>
<li><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC3517813/">Endocannabinoid signaling and synaptic function - PMC</a></li>
<li><a href="https://www.cell.com/cell-reports/fulltext/S2211-1247(19)31374-9">Gain Modulation by Corticostriatal and Thalamostriatal Input ...</a></li>

</ul>
</details>

**标签**: `#neuroscience`, `#endocannabinoids`, `#reward circuits`, `#neuromodulation`, `#Nature research`

---

<a id="item-11"></a>
## [《自然》研究揭示人 UGCG 的冷冻电镜结构及新型催化机制](https://www.nature.com/articles/s41586-026-10927-4) ⭐️ 8.0/10

研究人员解析了全长人 UGCG 的冷冻电镜结构，揭示其通过精氨酸网络驱动的无金属依赖催化机制来控制糖鞘脂的生物合成。 这一突破深化了我们对糖鞘脂生物学的理解，并为治疗开发开辟了新途径，因为 UGCG 抑制剂正在被探索用于治疗脂质代谢失调相关疾病。 UGCG 作为控制糖鞘脂多样性规模和组成的守门酶，其无金属依赖机制挑战了关于糖基转移酶催化的传统假设。

rss · Nature · 8月26日 00:00

**背景**: 糖鞘脂是维持细胞膜结构和信号传导的重要复杂脂质，GlcCer 是其生物合成中最小的中间产物。UGCG 催化其生物合成途径中的第一个关键步骤，使其成为重要的调控节点。大多数糖基转移酶已知需要金属离子来发挥催化活性，因此这种无金属依赖机制尤为引人注目。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://synapse.patsnap.com/article/what-are-ugcg-inhibitors-and-how-do-they-work">What are UGCG inhibitors and how do they work?</a></li>

</ul>
</details>

**标签**: `#structural biology`, `#cryo-EM`, `#enzymology`, `#glycosphingolipids`, `#Nature`

---