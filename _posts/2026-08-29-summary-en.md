---
layout: default
title: "Horizon Summary: 2026-08-29 (EN)"
date: 2026-08-29
lang: en
---

> From 45 items, 1 important content pieces were selected

---

1. [Keogh Criticizes TSB-AD Benchmark as Too Trivial for TSAD Research](#item-1) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Keogh Criticizes TSB-AD Benchmark as Too Trivial for TSAD Research](https://www.reddit.com/r/MachineLearning/comments/1w1wt1s/you_can_beat_sota_time_series_anomaly_detection/) ⭐️ 8.0/10

Prominent time series researcher Eamonn Keogh argues that the widely-used TSB-AD benchmark is too trivial, demonstrating that a century-old Statistical Process Control algorithm can match or exceed state-of-the-art TSAD methods on it. He suggests the benchmark's simplicity undermines the credibility of numerous recent papers evaluated on it. This critique challenges the validity of numerous recent TSAD papers published at top venues like NeurIPS, SIGKDD, and VLDB that rely on TSB-AD for evaluation. It raises fundamental questions about whether the field's progress over the past decade has been meaningful or merely illusory due to weak benchmarks. Keogh points out that many TSB-AD datasets, particularly ECG traces marked as 'TAO', are trivially solvable with simple SPC methods. He has also prepared more challenging benchmark problems covering domains like sled dogs, tuna tracking, fuel cells, and smart manufacturing to address the triviality issue.

reddit · r/MachineLearning · /u/eamonnkeogh · Aug 29, 20:16

**Background**: Time Series Anomaly Detection (TSAD) has become one of the hottest research areas at major machine learning conferences like NeurIPS, SIGKDD, and VLDB. The TSB-AD benchmark, introduced at NeurIPS 2024, provides a large-scale evaluation suite with 1070 time series from 40 diverse datasets. Statistical Process Control (SPC) is a classical quality control methodology developed in the early 20th century that uses statistical methods to monitor and control processes, making it one of the oldest approaches to detecting anomalous patterns in sequential data.

<details><summary>References</summary>
<ul>
<li><a href="https://thedatumorg.github.io/TSB-AD/">TSB-AD</a></li>
<li><a href="https://en.wikipedia.org/wiki/Statistical_process_control">Statistical process control - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#Time Series`, `#Anomaly Detection`, `#Benchmarking`, `#Machine Learning`, `#Research Critique`

---