---
paper_id: simzss
title: A Simple Framework for Open-Vocabulary Zero-Shot Segmentation
short_name: SimZSS
authors:
- Thomas Stegm{\"u
year: 2025
preprint_date: unknown
venue: ICLR
publication_status: published
primary_direction: 2d
modalities:
- image
task_setting: open_vocabulary
task_types:
- semantic
techniques:
- semantic_alignment
datasets: []
paper_url: https://arxiv.org/pdf/2406.16085v3
publication_url: https://openreview.net/forum?id=QzPKSUUcud
code_status: public
code_url: https://github.com/tileb1/simzss
code_details: 已核对官方实现目录：args_coco.json、figs、requirements.txt、src、tests。未独立运行或验证外部权重下载。
content_status: index
checked_on: '2026-11-09'
module_checked_on: '2026-11-09'
summary: 从字幕中提取离散文本概念，用可训练文本编码器查询冻结视觉模型的稠密表示，选择对应局部视觉概念并进行图文对齐；让视觉定位与语言对齐的学习职责分开。
sources:
- url: https://openreview.net/forum?id=QzPKSUUcud
  locator: 正式发表来源：出版页面／作者项目的会议说明
- url: https://arxiv.org/pdf/2406.16085v3
  locator: 方法部分；Figure 2（PDF 第 3 页）；实验 Table 2（PDF 第 8 页）
- url: https://github.com/tileb1/simzss
  locator: 官方 README、目录与开放范围；未独立运行
figures:
- id: fig2
  label: Figure 2
  asset: assets/figures/simzss-fig2.png
  page: 3
  version: arXiv 2406.16085v3
  source_url: https://arxiv.org/pdf/2406.16085v3
  source_sha256: 50729745eec0f51f1fc4b329528a1decb8f6cecfa8ce87a79a89bb81d01dfef3
  clip_pdf_points:
  - 107
  - 530
  - 506
  - 670.091
methods:
- id: semantic-operation
  track: vocabulary
  problems:
  - alignment
  - regions
  title: 字幕局部概念对齐
  question: 只有图像描述怎样学到像素语言对应？
  operation: 从字幕中提取离散文本概念，用可训练文本编码器查询冻结视觉模型的稠密表示，选择对应局部视觉概念并进行图文对齐；让视觉定位与语言对齐的学习职责分开。
  input: 图像—字幕配对、冻结视觉特征和文本概念
  output: 局部语言对齐的 patch 表示
  stage: 文本侧对齐训练与零样本推理
  supervision: 图像字幕配对，无像素语义训练标注
  origin: proposed
  origin_note: 本文设计的字幕局部概念对齐流程；所用预训练模型、通用投影及基础算子沿用已有方法，不计作本文新提出。
  evidence:
  - url: https://arxiv.org/pdf/2406.16085v3
    locator: 方法部分；Figure 2（PDF 第 3 页）；实验 Table 2（PDF 第 8 页）
  figure: fig2
  figure_guide: 看 Figure 2 的 caption concepts 与视觉稠密特征选择，以及跨模态对齐。
  depicted: true
  route:
  - 预训练视觉语言特征
  - 字幕局部概念对齐
  - 像素／区域类别表示
  - 开放词汇分割
  result_tables:
  - table2
results:
- id: table2
  label: Table 2
  asset: assets/results/simzss-table2.png
  page: 8
  version: arXiv 2406.16085v3
  source_url: https://arxiv.org/pdf/2406.16085v3
  source_sha256: 50729745eec0f51f1fc4b329528a1decb8f6cecfa8ce87a79a89bb81d01dfef3
  clip_pdf_points:
  - 107
  - 375
  - 506
  - 667
  title: SimZSS：主要实验结果
  setting: 开放词汇语义分割，前景类别与背景协议按原表保留。
  metrics: mIoU ↑
  reading: 不同于只评前景的 Table 1，当前表包含完整语义分割设置。
---

# SimZSS

本页按研究问题提取相关操作；模块图、输入输出、证据和主要结果表在上方展开查看。

## 研究问题

只有图像描述怎样学到像素语言对应？

## 相关操作

从字幕中提取离散文本概念，用可训练文本编码器查询冻结视觉模型的稠密表示，选择对应局部视觉概念并进行图文对齐；让视觉定位与语言对齐的学习职责分开。

## 实验阅读

开放词汇语义分割，前景类别与背景协议按原表保留。 不同于只评前景的 Table 1，当前表包含完整语义分割设置。 主表是整体系统结果，单一模块的贡献需结合原文消融。

## 原文依据

- [本次阅读的原文版本](https://arxiv.org/pdf/2406.16085v3)：方法部分；Figure 2（PDF 第 3 页）；实验 Table 2（PDF 第 8 页）。
- [正式发表来源](https://openreview.net/forum?id=QzPKSUUcud)。
- [官方实现](https://github.com/tileb1/simzss)：已核对官方实现目录：args_coco.json、figs、requirements.txt、src、tests。未独立运行或验证外部权重下载。
