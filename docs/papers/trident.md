---
paper_id: trident
title: Harnessing Vision Foundation Models for High-Performance, Training-Free Open Vocabulary Segmentation
short_name: Trident
authors:
- Shi, Yuheng
- Dong, Minjing
- Xu, Chang
year: 2025
preprint_date: unknown
venue: ICCV
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
- PASCAL
- COCO
- Cityscapes
- ADE20K
paper_url: https://openaccess.thecvf.com/content/ICCV2025/papers/Shi_Harnessing_Vision_Foundation_Models_for_High-Performance_Training-Free_Open_Vocabulary_Segmentation_ICCV_2025_paper.pdf
publication_url: https://openaccess.thecvf.com/content/ICCV2025/html/Shi_Harnessing_Vision_Foundation_Models_for_High-Performance_Training-Free_Open_Vocabulary_Segmentation_ICCV_2025_paper.html
code_status: public
code_url: https://github.com/YuHengsss/Trident
code_details: 已核对官方仓库实际实现目录：configs、custom_datasets.py、datasets、dist_test.sh、eval.py、eval_all.py。运行及外部权重可用性未独立复现。
content_status: index
checked_on: '2026-11-09'
module_checked_on: '2026-11-09'
summary: 先拼接各子图的 CLIP 和 DINO 特征，再由整图 SAM 编码器建立相关性矩阵，跨窗口全局聚合；把粗分割进一步转成 SAM 的提示进行边界细化。
sources:
- url: https://openaccess.thecvf.com/content/ICCV2025/html/Shi_Harnessing_Vision_Foundation_Models_for_High-Performance_Training-Free_Open_Vocabulary_Segmentation_ICCV_2025_paper.html
  locator: 正式发表页面及作者信息
- url: https://openaccess.thecvf.com/content/ICCV2025/papers/Shi_Harnessing_Vision_Foundation_Models_for_High-Performance_Training-Free_Open_Vocabulary_Segmentation_ICCV_2025_paper.pdf
  locator: 方法部分；Figure 3（PDF 第 5 页）；实验 Table 2（PDF 第 7 页）
- url: https://github.com/YuHengsss/Trident
  locator: 官方 README 与实际代码目录；不表示已运行
figures:
- id: figure3
  label: Figure 3
  asset: assets/figures/trident-figure3.png
  page: 5
  version: ICCV 2025 出版方正式版
  source_url: https://openaccess.thecvf.com/content/ICCV2025/papers/Shi_Harnessing_Vision_Foundation_Models_for_High-Performance_Training-Free_Open_Vocabulary_Segmentation_ICCV_2025_paper.pdf
  source_sha256: 6c9dc3057e6e6ce88e94974f2462151be36d3910af0872a7cdadaa112a6d1842
  clip_pdf_points:
  - 55
  - 50
  - 558
  - 267.6619567871094
methods:
- id: semantic-operation
  track: vocabulary
  problems:
  - regions
  - alignment
  title: 全局相关性聚合
  question: 滑窗之后如何恢复全局空间关联？
  operation: 先拼接各子图的 CLIP 和 DINO 特征，再由整图 SAM 编码器建立相关性矩阵，跨窗口全局聚合；把粗分割进一步转成 SAM 的提示进行边界细化。
  input: 子图 CLIP／DINO 特征、整图 SAM 特征、文本
  output: 全局一致的细化分割掩码
  stage: 免任务训练推理
  supervision: 预训练 CLIP、DINO、SAM
  origin: proposed
  origin_note: 本文设计的全局相关性聚合流程；其预训练基础模型与通用组件沿用已有方法，不计作本文新提出。
  origin_refs:
  - url: https://openaccess.thecvf.com/content/ICCV2025/papers/Shi_Harnessing_Vision_Foundation_Models_for_High-Performance_Training-Free_Open_Vocabulary_Segmentation_ICCV_2025_paper.pdf
    locator: 方法部分列明的基础模型及其参考文献
  evidence:
  - url: https://openaccess.thecvf.com/content/ICCV2025/papers/Shi_Harnessing_Vision_Foundation_Models_for_High-Performance_Training-Free_Open_Vocabulary_Segmentation_ICCV_2025_paper.pdf
    locator: 方法部分；Figure 3（PDF 第 5 页）；实验 Table 2（PDF 第 7 页）
  figure: figure3
  figure_guide: 先看子图 CLIP／DINO 特征，再看整图 SAM 相关性聚合；右侧把粗预测作为 prompt 进入 SAM refinement，区别特征拼接与最终掩码细化。
  depicted: true
  route:
  - CLIP DINO 与 SAM
  - 全局相关性聚合
  - 像素类别图与提示
  - 开放词汇分割
  result_tables:
  - table2
results:
- id: table2
  label: Table 2
  asset: assets/results/trident-table2.png
  page: 7
  version: ICCV 2025 出版方正式版
  source_url: https://openaccess.thecvf.com/content/ICCV2025/papers/Shi_Harnessing_Vision_Foundation_Models_for_High-Performance_Training-Free_Open_Vocabulary_Segmentation_ICCV_2025_paper.pdf
  source_sha256: 6c9dc3057e6e6ce88e94974f2462151be36d3910af0872a7cdadaa112a6d1842
  clip_pdf_points:
  - 55
  - 53
  - 558
  - 397
  title: Trident：主要实验结果
  setting: Table 2 八基准；按训练式／免训练及额外基础模型分组。
  metrics: mIoU ↑
  reading: Trident 使用多基础模型；不要与单 CLIP 方法忽略计算成本直接比较。
---

# Trident

本页按研究问题提取相关操作；模块原图、具体输入输出、来源与主要实验结果在上方展开查看。

## 研究问题

滑窗之后如何恢复全局空间关联？

## 相关操作

先拼接各子图的 CLIP 和 DINO 特征，再由整图 SAM 编码器建立相关性矩阵，跨窗口全局聚合；把粗分割进一步转成 SAM 的提示进行边界细化。

## 实验阅读

Table 2 八基准；按训练式／免训练及额外基础模型分组。 Trident 使用多基础模型；不要与单 CLIP 方法忽略计算成本直接比较。 主要结果是整套方法的效果，不能单凭该表归因到一个模块。

## 原文依据

- [出版方原文](https://openaccess.thecvf.com/content/ICCV2025/papers/Shi_Harnessing_Vision_Foundation_Models_for_High-Performance_Training-Free_Open_Vocabulary_Segmentation_ICCV_2025_paper.pdf)：方法部分；Figure 3（PDF 第 5 页）；实验 Table 2（PDF 第 7 页）。
- [官方实现](https://github.com/YuHengsss/Trident)：已检查公开目录，未独立运行训练或评测。
