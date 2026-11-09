---
paper_id: ovrcoat
title: Mitigating Objectness Bias and Region-to-Text Misalignment for Open-Vocabulary Panoptic Segmentation
short_name: OVRCOAT
authors:
- Kormushev, Nikolay
- Šarić, Josip
- Kristan, Matej
year: 2026
preprint_date: unknown
venue: CVPR
publication_status: published
primary_direction: 2d
modalities:
- image
task_setting: open_vocabulary
task_types:
- panoptic
techniques:
- semantic_alignment
datasets:
- ADE20K
- Cityscapes
- COCO
paper_url: https://openaccess.thecvf.com/content/CVPR2026/papers/Kormushev_Mitigating_Objectness_Bias_and_Region-to-Text_Misalignment_for_Open-Vocabulary_Panoptic_Segmentation_CVPR_2026_paper.pdf
publication_url: https://openaccess.thecvf.com/content/CVPR2026/html/Kormushev_Mitigating_Objectness_Bias_and_Region-to-Text_Misalignment_for_Open-Vocabulary_Panoptic_Segmentation_CVPR_2026_paper.html
code_status: public
code_url: https://github.com/nickormushev/OVRCOAT
code_details: 已核对官方仓库实际实现目录：GETTING_STARTED.md、INSTALL.md、configs、datasets、demo、imgs。运行及外部权重可用性未独立复现。
content_status: index
checked_on: '2026-11-09'
module_checked_on: '2026-11-09'
summary: COAT 用 CLIP 的开放词汇语义调整掩码前景／背景概率，使封闭类别物体性头不再过度压低新类别；OVR 通过掩码特征与文本分类的联合目标微调区域对齐，再组合两者进行全景预测。
sources:
- url: https://openaccess.thecvf.com/content/CVPR2026/html/Kormushev_Mitigating_Objectness_Bias_and_Region-to-Text_Misalignment_for_Open-Vocabulary_Panoptic_Segmentation_CVPR_2026_paper.html
  locator: 正式发表页面及作者信息
- url: https://openaccess.thecvf.com/content/CVPR2026/papers/Kormushev_Mitigating_Objectness_Bias_and_Region-to-Text_Misalignment_for_Open-Vocabulary_Panoptic_Segmentation_CVPR_2026_paper.pdf
  locator: 方法部分；Figure 2（PDF 第 3 页）；实验 Table 1（PDF 第 5 页）
- url: https://github.com/nickormushev/OVRCOAT
  locator: 官方 README 与实际代码目录；不表示已运行
figures:
- id: figure2
  label: Figure 2
  asset: assets/figures/ovrcoat-figure2.png
  page: 3
  version: CVPR 2026 出版方正式版
  source_url: https://openaccess.thecvf.com/content/CVPR2026/papers/Kormushev_Mitigating_Objectness_Bias_and_Region-to-Text_Misalignment_for_Open-Vocabulary_Panoptic_Segmentation_CVPR_2026_paper.pdf
  source_sha256: 50c4a5e698746c3c15e06e3bcfc8f84d305d7fd19ef7b18054e901afba436e39
  clip_pdf_points:
  - 55
  - 50
  - 558
  - 246.23800659179688
methods:
- id: semantic-operation
  track: vocabulary
  problems:
  - unseen
  - alignment
  title: 区域文本校准
  question: 未见类别的高质量掩码为何被背景分数淘汰？
  operation: COAT 用 CLIP 的开放词汇语义调整掩码前景／背景概率，使封闭类别物体性头不再过度压低新类别；OVR 通过掩码特征与文本分类的联合目标微调区域对齐，再组合两者进行全景预测。
  input: 图像、文本类别、候选掩码与物体性分数
  output: 校正的掩码类别及全景结果
  stage: OVR 训练；COAT 推理
  supervision: 训练集掩码及类别；CLIP 预训练语义
  origin: proposed
  origin_note: 本文设计的区域文本校准流程；其预训练基础模型与通用组件沿用已有方法，不计作本文新提出。
  origin_refs:
  - url: https://openaccess.thecvf.com/content/CVPR2026/papers/Kormushev_Mitigating_Objectness_Bias_and_Region-to-Text_Misalignment_for_Open-Vocabulary_Panoptic_Segmentation_CVPR_2026_paper.pdf
    locator: 方法部分列明的基础模型及其参考文献
  evidence:
  - url: https://openaccess.thecvf.com/content/CVPR2026/papers/Kormushev_Mitigating_Objectness_Bias_and_Region-to-Text_Misalignment_for_Open-Vocabulary_Panoptic_Segmentation_CVPR_2026_paper.pdf
    locator: 方法部分；Figure 2（PDF 第 3 页）；实验 Table 1（PDF 第 5 页）
  figure: figure2
  figure_guide: 沿 OVR CLIP Image Encoder → Mask Transformer → mask-pooling 阅读区域特征；再看 COAT 如何调整分类／背景概率并与掩码结合。
  depicted: true
  route:
  - CLIP 与掩码
  - 区域文本校准
  - 掩码类别分数
  - 全景分割
  result_tables:
  - table1
results:
- id: table1
  label: Table 1
  asset: assets/results/ovrcoat-table1.png
  page: 5
  version: CVPR 2026 出版方正式版
  source_url: https://openaccess.thecvf.com/content/CVPR2026/papers/Kormushev_Mitigating_Objectness_Bias_and_Region-to-Text_Misalignment_for_Open-Vocabulary_Panoptic_Segmentation_CVPR_2026_paper.pdf
  source_sha256: 50c4a5e698746c3c15e06e3bcfc8f84d305d7fd19ef7b18054e901afba436e39
  clip_pdf_points:
  - 55
  - 53
  - 558
  - 205
  title: OVRCOAT：主要实验结果
  setting: ADE20K、Mapillary Vistas、Cityscapes 与 COCO；灰列表示训练中见过的词汇。
  metrics: PQ／SQ／RQ ↑
  reading: 重点看跨词汇测试列；COCO 灰色列不代表未见类别泛化。
---

# OVRCOAT

本页按研究问题提取相关操作；模块原图、具体输入输出、来源与主要实验结果在上方展开查看。

## 研究问题

未见类别的高质量掩码为何被背景分数淘汰？

## 相关操作

COAT 用 CLIP 的开放词汇语义调整掩码前景／背景概率，使封闭类别物体性头不再过度压低新类别；OVR 通过掩码特征与文本分类的联合目标微调区域对齐，再组合两者进行全景预测。

## 实验阅读

ADE20K、Mapillary Vistas、Cityscapes 与 COCO；灰列表示训练中见过的词汇。 重点看跨词汇测试列；COCO 灰色列不代表未见类别泛化。 主要结果是整套方法的效果，不能单凭该表归因到一个模块。

## 原文依据

- [出版方原文](https://openaccess.thecvf.com/content/CVPR2026/papers/Kormushev_Mitigating_Objectness_Bias_and_Region-to-Text_Misalignment_for_Open-Vocabulary_Panoptic_Segmentation_CVPR_2026_paper.pdf)：方法部分；Figure 2（PDF 第 3 页）；实验 Table 1（PDF 第 5 页）。
- [官方实现](https://github.com/nickormushev/OVRCOAT)：已检查公开目录，未独立运行训练或评测。
