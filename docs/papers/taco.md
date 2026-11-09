---
paper_id: taco
title: 'TACO: Training-free Sound Prompted Segmentation via Semantically Constrained Audio-visual CO-factorization'
short_name: TACO
authors:
- Hugo Malard
- Michel Olvera
- Stéphane Lathuilière
- Slim Essid
year: 2026
preprint_date: unknown
venue: TMLR
publication_status: published
primary_direction: audio
modalities:
- image
- audio
task_setting: open_vocabulary
task_types:
- semantic
techniques:
- semantic_alignment
datasets: []
paper_url: https://arxiv.org/pdf/2412.01488v4
publication_url: https://openreview.net/forum?id=Xt9sdzQQlJ
code_status: public
code_url: https://github.com/hugomalard/TACO-Training-free-Sound-Prompted-Segmentation-via-Audio-visual-CO-factorization
code_details: 已核对官方实现目录：TACO、configs、fcclip、requirements-detectron2.txt、requirements.txt。未独立运行或验证外部权重下载。
content_status: index
checked_on: '2026-11-09'
module_checked_on: '2026-11-09'
summary: 把同一词库分别编码到 CLIP 和 CLAP 空间作为语义锚点，进行语义约束非负矩阵共分解，提取音画共同激活因子；将发声语义因子提示给冻结开放词汇分割器，输出声音对应区域及类别。
sources:
- url: https://openreview.net/forum?id=Xt9sdzQQlJ
  locator: 正式发表来源：出版页面／作者项目的会议说明
- url: https://arxiv.org/pdf/2412.01488v4
  locator: 方法部分；Figure 2（PDF 第 6 页）；实验 Table 3（PDF 第 11 页）
- url: https://github.com/hugomalard/TACO-Training-free-Sound-Prompted-Segmentation-via-Audio-visual-CO-factorization
  locator: 官方 README、目录与开放范围；未独立运行
figures:
- id: fig2
  label: Figure 2
  asset: assets/figures/taco-fig2.png
  page: 6
  version: arXiv 2412.01488v4
  source_url: https://arxiv.org/pdf/2412.01488v4
  source_sha256: 9ddc0400ee92d70231e4f945f8d8016d033695c437fcf8789cec20f4dafc1bcb
  clip_pdf_points:
  - 72
  - 45
  - 541
  - 233.785
methods:
- id: semantic-operation
  track: vocabulary
  problems:
  - alignment
  - prompt
  - regions
  title: 文本锚定音画共分解
  question: CLIP 与 CLAP 不同空间如何定位发声区域？
  operation: 把同一词库分别编码到 CLIP 和 CLAP 空间作为语义锚点，进行语义约束非负矩阵共分解，提取音画共同激活因子；将发声语义因子提示给冻结开放词汇分割器，输出声音对应区域及类别。
  input: 图像、同步声音、CLIP／CLAP 特征与语义词库
  output: 发声概念、空间激活及语义掩码
  stage: 逐样本共分解优化与分割推理
  supervision: 冻结 CLIP、CLAP、FC-CLIP；无目标音画掩码训练
  origin: proposed
  origin_note: 本文设计的文本锚定音画共分解流程；所用预训练模型、通用投影及基础算子沿用已有方法，不计作本文新提出。
  evidence:
  - url: https://arxiv.org/pdf/2412.01488v4
    locator: 方法部分；Figure 2（PDF 第 6 页）；实验 Table 3（PDF 第 11 页）
  figure: fig2
  figure_guide: 看音画独立编码 → Sem co-NMF 语义因子 → 开放词汇分割器提示；语义锚点另见 Figure 3。
  depicted: true
  route:
  - 音画特征与文本锚点
  - 文本锚定音画共分解
  - 像素／区域类别表示
  - 音视频语义分割
  result_tables:
  - table3
results:
- id: table3
  label: Table 3
  asset: assets/results/taco-table3.png
  page: 11
  version: arXiv 2412.01488v4
  source_url: https://arxiv.org/pdf/2412.01488v4
  source_sha256: 9ddc0400ee92d70231e4f945f8d8016d033695c437fcf8789cec20f4dafc1bcb
  clip_pdf_points:
  - 72
  - 68
  - 541
  - 165
  title: TACO：主要实验结果
  setting: AVSS 与 ADE SP Semantic；保留独立基线、TACO 和显著性标记。
  metrics: mIoU／mF 等 ↑
  reading: 需要逐样本优化；纯二值声音定位结果不等同于本表语义分类分割。
---

# TACO

本页按研究问题提取相关操作；模块图、输入输出、证据和主要结果表在上方展开查看。

## 研究问题

CLIP 与 CLAP 不同空间如何定位发声区域？

## 相关操作

把同一词库分别编码到 CLIP 和 CLAP 空间作为语义锚点，进行语义约束非负矩阵共分解，提取音画共同激活因子；将发声语义因子提示给冻结开放词汇分割器，输出声音对应区域及类别。

## 实验阅读

AVSS 与 ADE SP Semantic；保留独立基线、TACO 和显著性标记。 需要逐样本优化；纯二值声音定位结果不等同于本表语义分类分割。 主表是整体系统结果，单一模块的贡献需结合原文消融。

## 原文依据

- [本次阅读的原文版本](https://arxiv.org/pdf/2412.01488v4)：方法部分；Figure 2（PDF 第 6 页）；实验 Table 3（PDF 第 11 页）。
- [正式发表来源](https://openreview.net/forum?id=Xt9sdzQQlJ)。
- [官方实现](https://github.com/hugomalard/TACO-Training-free-Sound-Prompted-Segmentation-via-Audio-visual-CO-factorization)：已核对官方实现目录：TACO、configs、fcclip、requirements-detectron2.txt、requirements.txt。未独立运行或验证外部权重下载。
