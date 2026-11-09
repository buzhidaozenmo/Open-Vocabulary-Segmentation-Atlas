---
paper_id: conovs
title: 'OVS Meets Continual Learning: Towards Sustainable Open-Vocabulary Segmentation'
short_name: ConOVS
authors:
- Dongjun Hwang
- Yejin Kim
- Minyoung Lee
- Seong Joon Oh
- Junsuk Choe
year: 2025
preprint_date: unknown
venue: NeurIPS
publication_status: published
primary_direction: 2d
modalities:
- image
task_setting: open_vocabulary
task_types:
- panoptic
techniques:
- semantic_alignment
datasets: []
paper_url: https://arxiv.org/pdf/2410.11536v2
publication_url: https://papers.neurips.cc/paper_files/paper/2025/hash/184cfed554856b4812b19cd0235a0f6a-Abstract-Conference.html
code_status: public
code_url: https://github.com/dongjunhwang/ConOVS
code_details: 已核对官方实现目录：INSTALL.md、configs、datasets、fcclip、requirements.txt、scripts。未独立运行或验证外部权重下载。
content_status: index
checked_on: '2026-11-09'
module_checked_on: '2026-11-09'
summary: 每个增量数据集训练独立解码器专家，并统计图像及文本嵌入的多元高斯分布；推理时估计输入属于各域的概率，生成插值权重动态融合专家，减少直接微调的遗忘。
sources:
- url: https://papers.neurips.cc/paper_files/paper/2025/hash/184cfed554856b4812b19cd0235a0f6a-Abstract-Conference.html
  locator: 正式发表来源：出版页面／作者项目的会议说明
- url: https://arxiv.org/pdf/2410.11536v2
  locator: 方法部分；Figure 3（PDF 第 5 页）；实验 Table 1（PDF 第 6 页）
- url: https://github.com/dongjunhwang/ConOVS
  locator: 官方 README、目录与开放范围；未独立运行
figures:
- id: fig3
  label: Figure 3
  asset: assets/figures/conovs-fig3.png
  page: 5
  version: arXiv 2410.11536v2
  source_url: https://arxiv.org/pdf/2410.11536v2
  source_sha256: 92a26ed61471df94a17a1a4170bb5da803ad2a8a01df233b9a1503671d5d1863
  clip_pdf_points:
  - 45
  - 45
  - 567
  - 194.663
methods:
- id: semantic-operation
  track: vocabulary
  problems:
  - alignment
  - unseen
  title: 分布驱动专家融合
  question: 持续加入新数据怎样兼顾原有开放词汇能力？
  operation: 每个增量数据集训练独立解码器专家，并统计图像及文本嵌入的多元高斯分布；推理时估计输入属于各域的概率，生成插值权重动态融合专家，减少直接微调的遗忘。
  input: 图像和文本特征、各域分布及解码器专家
  output: 输入条件的专家分割预测
  stage: 增量专家训练与动态融合推理
  supervision: 各阶段数据集分割标注及图文嵌入统计
  origin: proposed
  origin_note: 本文设计的分布驱动专家融合流程；所用预训练模型、通用投影及基础算子沿用已有方法，不计作本文新提出。
  evidence:
  - url: https://arxiv.org/pdf/2410.11536v2
    locator: 方法部分；Figure 3（PDF 第 5 页）；实验 Table 1（PDF 第 6 页）
  figure: fig3
  figure_guide: 看 Interpolation factor estimator → Mixture-of-Experts；图左算法给出图文似然如何组合。
  depicted: true
  route:
  - 预训练视觉语言特征
  - 分布驱动专家融合
  - 像素／区域类别表示
  - 开放词汇分割
  result_tables:
  - table1
results:
- id: table1
  label: Table 1
  asset: assets/results/conovs-table1.png
  page: 6
  version: arXiv 2410.11536v2
  source_url: https://arxiv.org/pdf/2410.11536v2
  source_sha256: 92a26ed61471df94a17a1a4170bb5da803ad2a8a01df233b9a1503671d5d1863
  clip_pdf_points:
  - 107
  - 70
  - 506
  - 258
  title: ConOVS：主要实验结果
  setting: S1／S2 持续学习序列；保留预训练域、增量域、零样本域。
  metrics: PQ／mIoU 等 ↑，按任务列
  reading: 同时比较保留旧域、学习新域与零样本列，不能只看新域提升。
---

# ConOVS

本页按研究问题提取相关操作；模块图、输入输出、证据和主要结果表在上方展开查看。

## 研究问题

持续加入新数据怎样兼顾原有开放词汇能力？

## 相关操作

每个增量数据集训练独立解码器专家，并统计图像及文本嵌入的多元高斯分布；推理时估计输入属于各域的概率，生成插值权重动态融合专家，减少直接微调的遗忘。

## 实验阅读

S1／S2 持续学习序列；保留预训练域、增量域、零样本域。 同时比较保留旧域、学习新域与零样本列，不能只看新域提升。 主表是整体系统结果，单一模块的贡献需结合原文消融。

## 原文依据

- [本次阅读的原文版本](https://arxiv.org/pdf/2410.11536v2)：方法部分；Figure 3（PDF 第 5 页）；实验 Table 1（PDF 第 6 页）。
- [正式发表来源](https://papers.neurips.cc/paper_files/paper/2025/hash/184cfed554856b4812b19cd0235a0f6a-Abstract-Conference.html)。
- [官方实现](https://github.com/dongjunhwang/ConOVS)：已核对官方实现目录：INSTALL.md、configs、datasets、fcclip、requirements.txt、scripts。未独立运行或验证外部权重下载。
