---
paper_id: spar
title: 'SPAR: Single-Pass Any-Resolution ViT for Open-vocabulary Segmentation'
short_name: SPAR
authors:
- Kombol, Naomi
- Martinović, Ivan
- Šegvić, Siniša
- Tolias, Giorgos
year: 2026
preprint_date: unknown
venue: CVPR
publication_status: published
primary_direction: 2d
modalities:
- image
task_setting: open_vocabulary
task_types:
- semantic
techniques:
- semantic_alignment
datasets:
- ADE20K
- Cityscapes
- PASCAL
- COCO
paper_url: https://openaccess.thecvf.com/content/CVPR2026/papers/Kombol_SPAR_Single-Pass_Any-Resolution_ViT_for_Open-vocabulary_Segmentation_CVPR_2026_paper.pdf
publication_url: https://openaccess.thecvf.com/content/CVPR2026/html/Kombol_SPAR_Single-Pass_Any-Resolution_ViT_for_Open-vocabulary_Segmentation_CVPR_2026_paper.html
code_status: public
code_url: https://github.com/naomikombol/SPAR
code_details: 已核对官方仓库实际实现目录：configs、datasets、embeddings_extraction_demo.py、eval.py、frankfurt_000000_000294_leftImg8bit.png、generate_embeddings.py。运行及外部权重可用性未独立复现。
content_status: index
checked_on: '2026-11-09'
module_checked_on: '2026-11-09'
summary: 冻结教师以小步长滑窗提取并拼接高分辨率特征；同源初始化的学生用单次全图前向拟合教师特征，以特征回归训练将滑窗空间能力蒸馏到任意分辨率学生，再与文本特征匹配分割。
sources:
- url: https://openaccess.thecvf.com/content/CVPR2026/html/Kombol_SPAR_Single-Pass_Any-Resolution_ViT_for_Open-vocabulary_Segmentation_CVPR_2026_paper.html
  locator: 正式发表页面及作者信息
- url: https://openaccess.thecvf.com/content/CVPR2026/papers/Kombol_SPAR_Single-Pass_Any-Resolution_ViT_for_Open-vocabulary_Segmentation_CVPR_2026_paper.pdf
  locator: 方法部分；Figure 2（PDF 第 4 页）；实验 Table 1（PDF 第 5 页）
- url: https://github.com/naomikombol/SPAR
  locator: 官方 README 与实际代码目录；不表示已运行
figures:
- id: figure2
  label: Figure 2
  asset: assets/figures/spar-figure2.png
  page: 4
  version: CVPR 2026 出版方正式版
  source_url: https://openaccess.thecvf.com/content/CVPR2026/papers/Kombol_SPAR_Single-Pass_Any-Resolution_ViT_for_Open-vocabulary_Segmentation_CVPR_2026_paper.pdf
  source_sha256: b1711bed75d02ebbf7f330bf0112b7fcfedb0ebafae7695a3c6451fc440195e3
  clip_pdf_points:
  - 55
  - 50
  - 558
  - 323.1241149902344
methods:
- id: semantic-operation
  track: vocabulary
  problems:
  - distillation
  - efficiency
  title: 滑窗特征蒸馏
  question: 怎样保留滑窗语义细节又只做一次前向？
  operation: 冻结教师以小步长滑窗提取并拼接高分辨率特征；同源初始化的学生用单次全图前向拟合教师特征，以特征回归训练将滑窗空间能力蒸馏到任意分辨率学生，再与文本特征匹配分割。
  input: 无像素标注训练图像、教师滑窗特征；推理图像和文本
  output: 单次前向的稠密语言对齐特征
  stage: 教师学生蒸馏训练；单次推理
  supervision: 冻结教师的稠密特征，无像素类别训练标注
  origin: proposed
  origin_note: 本文设计的滑窗特征蒸馏流程；其预训练基础模型与通用组件沿用已有方法，不计作本文新提出。
  origin_refs:
  - url: https://openaccess.thecvf.com/content/CVPR2026/papers/Kombol_SPAR_Single-Pass_Any-Resolution_ViT_for_Open-vocabulary_Segmentation_CVPR_2026_paper.pdf
    locator: 方法部分列明的基础模型及其参考文献
  evidence:
  - url: https://openaccess.thecvf.com/content/CVPR2026/papers/Kombol_SPAR_Single-Pass_Any-Resolution_ViT_for_Open-vocabulary_Segmentation_CVPR_2026_paper.pdf
    locator: 方法部分；Figure 2（PDF 第 4 页）；实验 Table 1（PDF 第 5 页）
  figure: figure2
  figure_guide: 上半部冻结教师做 overlapping sliding windows 并拼接特征，下半部学生单次前向；训练虚线路径用特征回归对齐，推理只保留学生。
  depicted: true
  route:
  - 预训练视觉语言教师
  - 滑窗特征蒸馏
  - 高分辨率像素特征
  - 高效开放词汇分割
  result_tables:
  - table1
results:
- id: table1
  label: Table 1
  asset: assets/results/spar-table1.png
  page: 5
  version: CVPR 2026 出版方正式版
  source_url: https://openaccess.thecvf.com/content/CVPR2026/papers/Kombol_SPAR_Single-Pass_Any-Resolution_ViT_for_Open-vocabulary_Segmentation_CVPR_2026_paper.pdf
  source_sha256: b1711bed75d02ebbf7f330bf0112b7fcfedb0ebafae7695a3c6451fc440195e3
  clip_pdf_points:
  - 55
  - 49
  - 558
  - 370
  title: SPAR：主要实验结果
  setting: 六组数据集、三种骨干；保留 sliding-window、single-pass、LPOSS 及上采样器设置。
  metrics: mIoU ↑
  reading: 比较同一骨干和上采样器；学生经过蒸馏，不能标成整体免训练。
---

# SPAR

本页按研究问题提取相关操作；模块原图、具体输入输出、来源与主要实验结果在上方展开查看。

## 研究问题

怎样保留滑窗语义细节又只做一次前向？

## 相关操作

冻结教师以小步长滑窗提取并拼接高分辨率特征；同源初始化的学生用单次全图前向拟合教师特征，以特征回归训练将滑窗空间能力蒸馏到任意分辨率学生，再与文本特征匹配分割。

## 实验阅读

六组数据集、三种骨干；保留 sliding-window、single-pass、LPOSS 及上采样器设置。 比较同一骨干和上采样器；学生经过蒸馏，不能标成整体免训练。 主要结果是整套方法的效果，不能单凭该表归因到一个模块。

## 原文依据

- [出版方原文](https://openaccess.thecvf.com/content/CVPR2026/papers/Kombol_SPAR_Single-Pass_Any-Resolution_ViT_for_Open-vocabulary_Segmentation_CVPR_2026_paper.pdf)：方法部分；Figure 2（PDF 第 4 页）；实验 Table 1（PDF 第 5 页）。
- [官方实现](https://github.com/naomikombol/SPAR)：已检查公开目录，未独立运行训练或评测。
