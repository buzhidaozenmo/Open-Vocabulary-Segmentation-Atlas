---
paper_id: ilgs
title: Identity-aware Language Gaussian Splatting for Open-vocabulary 3D Semantic Segmentation
short_name: ILGS
authors:
- Jang, SungMin
- Kim, Wonjun
year: 2025
preprint_date: unknown
venue: ICCV
publication_status: published
primary_direction: 3dgs
modalities:
- gaussian
- image
task_setting: open_vocabulary
task_types:
- semantic
techniques:
- semantic_alignment
datasets:
- LERF
- 3D-OVS
paper_url: https://openaccess.thecvf.com/content/ICCV2025/papers/Jang_Identity-aware_Language_Gaussian_Splatting_for_Open-vocabulary_3D_Semantic_Segmentation_ICCV_2025_paper.pdf
publication_url: https://openaccess.thecvf.com/content/ICCV2025/html/Jang_Identity-aware_Language_Gaussian_Splatting_for_Open-vocabulary_3D_Semantic_Segmentation_ICCV_2025_paper.html
code_status: public
code_url: https://github.com/DCVL-3D/ILGS
code_details: 已核对官方仓库实际实现目录：LICENSE_GAUSSIAN_SPLATTING.md、arguments、autoencoder、config、documents、edit_recolor.py。运行及外部权重可用性未独立复现。
content_status: index
checked_on: '2026-11-09'
module_checked_on: '2026-11-09'
summary: 给高斯同时附加身份和语言嵌入，用一致身份伪标签将相同对象的语言表示拉近、不同身份分开；查询时从种子区域渐进扩展语义掩码，以局部区域关系保留对象边界。
sources:
- url: https://openaccess.thecvf.com/content/ICCV2025/html/Jang_Identity-aware_Language_Gaussian_Splatting_for_Open-vocabulary_3D_Semantic_Segmentation_ICCV_2025_paper.html
  locator: 正式发表页面及作者信息
- url: https://openaccess.thecvf.com/content/ICCV2025/papers/Jang_Identity-aware_Language_Gaussian_Splatting_for_Open-vocabulary_3D_Semantic_Segmentation_ICCV_2025_paper.pdf
  locator: 方法部分；Figure 2（PDF 第 3 页）；实验 Table 1（PDF 第 6 页）
- url: https://github.com/DCVL-3D/ILGS
  locator: 官方 README 与实际代码目录；不表示已运行
figures:
- id: figure2
  label: Figure 2
  asset: assets/figures/ilgs-figure2.png
  page: 3
  version: ICCV 2025 出版方正式版
  source_url: https://openaccess.thecvf.com/content/ICCV2025/papers/Jang_Identity-aware_Language_Gaussian_Splatting_for_Open-vocabulary_3D_Semantic_Segmentation_ICCV_2025_paper.pdf
  source_sha256: 4c5d35d562ce6ad7eb51b58134b6d1b4eaec2b828c585040fef14024b9b29737
  clip_pdf_points:
  - 55
  - 50
  - 558
  - 259.9700012207031
methods:
- id: semantic-operation
  track: vocabulary
  problems:
  - alignment
  - regions
  title: 身份约束语义对齐
  question: 同一对象跨视角的语言特征怎样一致？
  operation: 给高斯同时附加身份和语言嵌入，用一致身份伪标签将相同对象的语言表示拉近、不同身份分开；查询时从种子区域渐进扩展语义掩码，以局部区域关系保留对象边界。
  input: 多视角图像、身份伪标签、语言教师、文本查询
  output: 身份一致的高斯语言场及查询掩码
  stage: 场景优化与查询推理
  supervision: 跨视角身份伪标签及二维语言特征
  origin: proposed
  origin_note: 本文设计的身份约束语义对齐流程；其预训练基础模型与通用组件沿用已有方法，不计作本文新提出。
  origin_refs:
  - url: https://openaccess.thecvf.com/content/ICCV2025/papers/Jang_Identity-aware_Language_Gaussian_Splatting_for_Open-vocabulary_3D_Semantic_Segmentation_ICCV_2025_paper.pdf
    locator: 方法部分列明的基础模型及其参考文献
  evidence:
  - url: https://openaccess.thecvf.com/content/ICCV2025/papers/Jang_Identity-aware_Language_Gaussian_Splatting_for_Open-vocabulary_3D_Semantic_Segmentation_ICCV_2025_paper.pdf
    locator: 方法部分；Figure 2（PDF 第 3 页）；实验 Table 1（PDF 第 6 页）
  figure: figure2
  figure_guide: 图中央 Identity-aware semantic consistency loss 对应跨视角身份约束，下面 identity map 与 language feature 共同优化；掩码渐进扩展另见 Figure
    3。
  depicted: true
  route:
  - 二维语言与实例身份
  - 身份约束语义对齐
  - 高斯语言特征
  - 文本语义分割
  result_tables:
  - table1
results:
- id: table1
  label: Table 1
  asset: assets/results/ilgs-table1.png
  page: 6
  version: ICCV 2025 出版方正式版
  source_url: https://openaccess.thecvf.com/content/ICCV2025/papers/Jang_Identity-aware_Language_Gaussian_Splatting_for_Open-vocabulary_3D_Semantic_Segmentation_ICCV_2025_paper.pdf
  source_sha256: 4c5d35d562ce6ad7eb51b58134b6d1b4eaec2b828c585040fef14024b9b29737
  clip_pdf_points:
  - 55
  - 408
  - 558
  - 566
  title: ILGS：主要实验结果
  setting: LERF 的 figs／teatime／ramen 场景及各自指标。
  metrics: mIoU／mAcc ↑
  reading: 本表是渲染视角下语义分割；不能视为体素或点级真实三维 IoU。
---

# ILGS

本页按研究问题提取相关操作；模块原图、具体输入输出、来源与主要实验结果在上方展开查看。

## 研究问题

同一对象跨视角的语言特征怎样一致？

## 相关操作

给高斯同时附加身份和语言嵌入，用一致身份伪标签将相同对象的语言表示拉近、不同身份分开；查询时从种子区域渐进扩展语义掩码，以局部区域关系保留对象边界。

## 实验阅读

LERF 的 figs／teatime／ramen 场景及各自指标。 本表是渲染视角下语义分割；不能视为体素或点级真实三维 IoU。 主要结果是整套方法的效果，不能单凭该表归因到一个模块。

## 原文依据

- [出版方原文](https://openaccess.thecvf.com/content/ICCV2025/papers/Jang_Identity-aware_Language_Gaussian_Splatting_for_Open-vocabulary_3D_Semantic_Segmentation_ICCV_2025_paper.pdf)：方法部分；Figure 2（PDF 第 3 页）；实验 Table 1（PDF 第 6 页）。
- [官方实现](https://github.com/DCVL-3D/ILGS)：已检查公开目录，未独立运行训练或评测。
