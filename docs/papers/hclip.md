---
paper_id: hclip
title: Parameter-efficient Fine-tuning in Hyperspherical Space for Open-vocabulary Semantic Segmentation
short_name: H-CLIP
authors:
- Peng, Zelin
- Xu, Zhengqin
- Zeng, Zhilin
- Huang, Yu
- Wang, Yaoming
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
paper_url: https://openaccess.thecvf.com/content/CVPR2025/papers/Peng_Parameter-efficient_Fine-tuning_in_Hyperspherical_Space_for_Open-vocabulary_Semantic_Segmentation_CVPR_2025_paper.pdf
publication_url: https://openaccess.thecvf.com/content/CVPR2025/html/Peng_Parameter-efficient_Fine-tuning_in_Hyperspherical_Space_for_Open-vocabulary_Semantic_Segmentation_CVPR_2025_paper.html
code_status: public
code_url: https://github.com/SJTU-DeepVisionLab/H-CLIP
code_details: 已核对官方仓库实际实现目录：INSTALL.md、cat_seg、configs、datasets、demo、eval.sh。运行及外部权重可用性未独立复现。
content_status: index
checked_on: '2026-11-09'
module_checked_on: '2026-11-09'
summary: 用部分正交的分块对角变换适配 CLIP 权重，双跨关系通信让视觉与文本变换共享信息；对文本侧施加超球面能量约束，减少微调破坏类别间结构，再接分割解码器。
sources:
- url: https://openaccess.thecvf.com/content/CVPR2025/html/Peng_Parameter-efficient_Fine-tuning_in_Hyperspherical_Space_for_Open-vocabulary_Semantic_Segmentation_CVPR_2025_paper.html
  locator: 正式发表页面及作者信息
- url: https://openaccess.thecvf.com/content/CVPR2025/papers/Peng_Parameter-efficient_Fine-tuning_in_Hyperspherical_Space_for_Open-vocabulary_Semantic_Segmentation_CVPR_2025_paper.pdf
  locator: 方法部分；Figure 1（PDF 第 4 页）；实验 Table 1（PDF 第 6 页）
- url: https://github.com/SJTU-DeepVisionLab/H-CLIP
  locator: 官方 README 与实际代码目录；不表示已运行
figures:
- id: figure1
  label: Figure 1
  asset: assets/figures/hclip-figure1.png
  page: 4
  version: CVPR 2025 出版方正式版
  source_url: https://openaccess.thecvf.com/content/CVPR2025/papers/Peng_Parameter-efficient_Fine-tuning_in_Hyperspherical_Space_for_Open-vocabulary_Semantic_Segmentation_CVPR_2025_paper.pdf
  source_sha256: 7120ae25518cc349103893341b185684f56de001283da01237c7d43823f497a8
  clip_pdf_points:
  - 55
  - 50
  - 558
  - 264.2104187011719
methods:
- id: semantic-operation
  track: vocabulary
  problems:
  - alignment
  - unseen
  title: 结构约束微调
  question: 怎样微调两种模态又保留文本类别结构？
  operation: 用部分正交的分块对角变换适配 CLIP 权重，双跨关系通信让视觉与文本变换共享信息；对文本侧施加超球面能量约束，减少微调破坏类别间结构，再接分割解码器。
  input: CLIP 视觉／文本权重及分割样本
  output: 保持类别结构的稠密图文表示
  stage: 参数高效微调及推理
  supervision: 分割训练标注、原预训练 CLIP 参数
  origin: proposed
  origin_note: 本文设计的结构约束微调流程；其预训练基础模型与通用组件沿用已有方法，不计作本文新提出。
  origin_refs:
  - url: https://openaccess.thecvf.com/content/CVPR2025/papers/Peng_Parameter-efficient_Fine-tuning_in_Hyperspherical_Space_for_Open-vocabulary_Semantic_Segmentation_CVPR_2025_paper.pdf
    locator: 方法部分列明的基础模型及其参考文献
  evidence:
  - url: https://openaccess.thecvf.com/content/CVPR2025/papers/Peng_Parameter-efficient_Fine-tuning_in_Hyperspherical_Space_for_Open-vocabulary_Semantic_Segmentation_CVPR_2025_paper.pdf
    locator: 方法部分；Figure 1（PDF 第 4 页）；实验 Table 1（PDF 第 6 页）
  figure: figure1
  figure_guide: 上部 Image 与下部 Text 两路各含分块变换；中间 Dual Cross Relation Communication 交换变换信息，旁边的正交约束用于保护预训练结构。
  depicted: true
  route:
  - CLIP 图文权重
  - 结构约束微调
  - 像素文本表示
  - 开放词汇分割
  result_tables:
  - table1
results:
- id: table1
  label: Table 1
  asset: assets/results/hclip-table1.png
  page: 6
  version: CVPR 2025 出版方正式版
  source_url: https://openaccess.thecvf.com/content/CVPR2025/papers/Peng_Parameter-efficient_Fine-tuning_in_Hyperspherical_Space_for_Open-vocabulary_Semantic_Segmentation_CVPR_2025_paper.pdf
  source_sha256: 7120ae25518cc349103893341b185684f56de001283da01237c7d43823f497a8
  clip_pdf_points:
  - 55
  - 56
  - 558
  - 390
  title: H-CLIP：主要实验结果
  setting: 标准语义分割基准；E 为欧氏空间、H 为超球面空间。
  metrics: mIoU ↑
  reading: 按同一骨干和训练类别比较；不要与双曲空间 HyperCLIP 混淆。
---

# H-CLIP

本页按研究问题提取相关操作；模块原图、具体输入输出、来源与主要实验结果在上方展开查看。

## 研究问题

怎样微调两种模态又保留文本类别结构？

## 相关操作

用部分正交的分块对角变换适配 CLIP 权重，双跨关系通信让视觉与文本变换共享信息；对文本侧施加超球面能量约束，减少微调破坏类别间结构，再接分割解码器。

## 实验阅读

标准语义分割基准；E 为欧氏空间、H 为超球面空间。 按同一骨干和训练类别比较；不要与双曲空间 HyperCLIP 混淆。 主要结果是整套方法的效果，不能单凭该表归因到一个模块。

## 原文依据

- [出版方原文](https://openaccess.thecvf.com/content/CVPR2025/papers/Peng_Parameter-efficient_Fine-tuning_in_Hyperspherical_Space_for_Open-vocabulary_Semantic_Segmentation_CVPR_2025_paper.pdf)：方法部分；Figure 1（PDF 第 4 页）；实验 Table 1（PDF 第 6 页）。
- [官方实现](https://github.com/SJTU-DeepVisionLab/H-CLIP)：已检查公开目录，未独立运行训练或评测。
