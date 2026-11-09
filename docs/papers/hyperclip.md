---
paper_id: hyperclip
title: Understanding Fine-tuning CLIP for Open-vocabulary Semantic Segmentation in Hyperbolic Space
short_name: HyperCLIP
authors:
- Peng, Zelin
- Xu, Zhengqin
- Zeng, Zhilin
- Wen, Changsong
- Huang, Yu
- Yang, Menglin
- Tang, Feilong
- Shen, Wei
year: 2025
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
- PASCAL
paper_url: https://openaccess.thecvf.com/content/CVPR2025/papers/Peng_Understanding_Fine-tuning_CLIP_for_Open-vocabulary_Semantic_Segmentation_in_Hyperbolic_Space_CVPR_2025_paper.pdf
publication_url: https://openaccess.thecvf.com/content/CVPR2025/html/Peng_Understanding_Fine-tuning_CLIP_for_Open-vocabulary_Semantic_Segmentation_in_Hyperbolic_Space_CVPR_2025_paper.html
code_status: public
code_url: https://github.com/SJTU-DeepVisionLab/HyperCLIP
code_details: 已核对官方仓库实际实现目录：INSTALL.md、cat_seg、configs、datasets、eval.sh、framework.jpg。运行及外部权重可用性未独立复现。
content_status: index
checked_on: '2026-11-09'
module_checked_on: '2026-11-09'
summary: 在双曲空间表述图文嵌入，利用可训练分块对角缩放矩阵调整文本嵌入的双曲半径，使其层级更接近像素视觉表示；以少量适配参数进行分割微调。
sources:
- url: https://openaccess.thecvf.com/content/CVPR2025/html/Peng_Understanding_Fine-tuning_CLIP_for_Open-vocabulary_Semantic_Segmentation_in_Hyperbolic_Space_CVPR_2025_paper.html
  locator: 正式发表页面及作者信息
- url: https://openaccess.thecvf.com/content/CVPR2025/papers/Peng_Understanding_Fine-tuning_CLIP_for_Open-vocabulary_Semantic_Segmentation_in_Hyperbolic_Space_CVPR_2025_paper.pdf
  locator: 方法部分；Figure 3（PDF 第 4 页）；实验 Table 1（PDF 第 5 页）
- url: https://github.com/SJTU-DeepVisionLab/HyperCLIP
  locator: 官方 README 与实际代码目录；不表示已运行
figures:
- id: figure3
  label: Figure 3
  asset: assets/figures/hyperclip-figure3.png
  page: 4
  version: CVPR 2025 出版方正式版
  source_url: https://openaccess.thecvf.com/content/CVPR2025/papers/Peng_Understanding_Fine-tuning_CLIP_for_Open-vocabulary_Semantic_Segmentation_in_Hyperbolic_Space_CVPR_2025_paper.pdf
  source_sha256: f847c4bcbc5ea35d5dabda99f199a8ca6d3d6deff28718aabb965b9c064d29d5
  clip_pdf_points:
  - 55
  - 50
  - 558
  - 201.57125854492188
methods:
- id: semantic-operation
  track: vocabulary
  problems:
  - alignment
  - unseen
  title: 层级空间语义对齐
  question: 从图像到像素的对齐层级怎样调整？
  operation: 在双曲空间表述图文嵌入，利用可训练分块对角缩放矩阵调整文本嵌入的双曲半径，使其层级更接近像素视觉表示；以少量适配参数进行分割微调。
  input: 预训练 CLIP 图文特征、分割训练样本
  output: 双曲层级对齐的像素类别表示
  stage: 参数高效微调及推理
  supervision: 像素分割训练标注及预训练 CLIP
  origin: proposed
  origin_note: 本文设计的层级空间语义对齐流程；其预训练基础模型与通用组件沿用已有方法，不计作本文新提出。
  origin_refs:
  - url: https://openaccess.thecvf.com/content/CVPR2025/papers/Peng_Understanding_Fine-tuning_CLIP_for_Open-vocabulary_Semantic_Segmentation_in_Hyperbolic_Space_CVPR_2025_paper.pdf
    locator: 方法部分列明的基础模型及其参考文献
  evidence:
  - url: https://openaccess.thecvf.com/content/CVPR2025/papers/Peng_Understanding_Fine-tuning_CLIP_for_Open-vocabulary_Semantic_Segmentation_in_Hyperbolic_Space_CVPR_2025_paper.pdf
    locator: 方法部分；Figure 3（PDF 第 4 页）；实验 Table 1（PDF 第 5 页）
  figure: figure3
  figure_guide: 左侧示意双曲半径变化；中间 CLIP 双路的可训练缩放矩阵调节层级，右侧解码器生成语义分割。
  depicted: true
  route:
  - CLIP 图文嵌入
  - 层级空间语义对齐
  - 像素文本表示
  - 开放词汇分割
  result_tables:
  - table1
results:
- id: table1
  label: Table 1
  asset: assets/results/hyperclip-table1.png
  page: 5
  version: CVPR 2025 出版方正式版
  source_url: https://openaccess.thecvf.com/content/CVPR2025/papers/Peng_Understanding_Fine-tuning_CLIP_for_Open-vocabulary_Semantic_Segmentation_in_Hyperbolic_Space_CVPR_2025_paper.pdf
  source_sha256: f847c4bcbc5ea35d5dabda99f199a8ca6d3d6deff28718aabb965b9c064d29d5
  clip_pdf_points:
  - 55
  - 56
  - 558
  - 412
  title: HyperCLIP：主要实验结果
  setting: ADE20K／PASCAL 等标准基准；E 表示欧氏空间、H 表示双曲空间。
  metrics: mIoU ↑
  reading: 核对空间定义、训练方式与骨干；H-CLIP 的 H 是超球面，二者不是同一工作。
---

# HyperCLIP

本页按研究问题提取相关操作；模块原图、具体输入输出、来源与主要实验结果在上方展开查看。

## 研究问题

从图像到像素的对齐层级怎样调整？

## 相关操作

在双曲空间表述图文嵌入，利用可训练分块对角缩放矩阵调整文本嵌入的双曲半径，使其层级更接近像素视觉表示；以少量适配参数进行分割微调。

## 实验阅读

ADE20K／PASCAL 等标准基准；E 表示欧氏空间、H 表示双曲空间。 核对空间定义、训练方式与骨干；H-CLIP 的 H 是超球面，二者不是同一工作。 主要结果是整套方法的效果，不能单凭该表归因到一个模块。

## 原文依据

- [出版方原文](https://openaccess.thecvf.com/content/CVPR2025/papers/Peng_Understanding_Fine-tuning_CLIP_for_Open-vocabulary_Semantic_Segmentation_in_Hyperbolic_Space_CVPR_2025_paper.pdf)：方法部分；Figure 3（PDF 第 4 页）；实验 Table 1（PDF 第 5 页）。
- [官方实现](https://github.com/SJTU-DeepVisionLab/HyperCLIP)：已检查公开目录，未独立运行训练或评测。
