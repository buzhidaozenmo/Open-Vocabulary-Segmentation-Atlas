---
paper_id: hops
title: 'HOPS: Hierarchical Open-vocabulary Part Segmentation with Attention-Aware Filtering and Affinity-Guided Enhancement'
short_name: HOPS
authors:
- Li, Xinlong
- Lin, Di
- Gao, Shaoyiyi
- Liu, Yaxuan
- He, Jixian
- Li, Jiaxin
- Liu, Ruonan
- Guo, Qing
- Yang, Kairui
- Feng, Wei
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
- PASCAL
paper_url: https://openaccess.thecvf.com/content/CVPR2026/papers/Li_HOPS_Hierarchical_Open-vocabulary_Part_Segmentation_with_Attention-Aware_Filtering_and_Affinity-Guided_CVPR_2026_paper.pdf
publication_url: https://openaccess.thecvf.com/content/CVPR2026/html/Li_HOPS_Hierarchical_Open-vocabulary_Part_Segmentation_with_Attention-Aware_Filtering_and_Affinity-Guided_CVPR_2026_paper.html
code_status: public
code_url: https://github.com/TJU-IDVLab/HOPS
code_details: 已核对官方仓库实际实现目录：baselines、clip、configs、datasets、hops.jpg、open_clip。运行及外部权重可用性未独立复现。
content_status: index
checked_on: '2026-11-09'
module_checked_on: '2026-11-09'
summary: 先融合 CLIP 语义注意力和 DINO 结构注意力，以 AFM 过滤对象代价图；再限制在预测对象区域内，对部件响应执行 AEM 亲和传播，逐步扩展欠激活部件。两阶段共享编码器但使用不同聚合模块。
sources:
- url: https://openaccess.thecvf.com/content/CVPR2026/html/Li_HOPS_Hierarchical_Open-vocabulary_Part_Segmentation_with_Attention-Aware_Filtering_and_Affinity-Guided_CVPR_2026_paper.html
  locator: 正式发表页面及作者信息
- url: https://openaccess.thecvf.com/content/CVPR2026/papers/Li_HOPS_Hierarchical_Open-vocabulary_Part_Segmentation_with_Attention-Aware_Filtering_and_Affinity-Guided_CVPR_2026_paper.pdf
  locator: 方法部分；Figure 4（PDF 第 5 页）；实验 Table 3（PDF 第 7 页）
- url: https://github.com/TJU-IDVLab/HOPS
  locator: 官方 README 与实际代码目录；不表示已运行
figures:
- id: figure4
  label: Figure 4
  asset: assets/figures/hops-figure4.png
  page: 5
  version: CVPR 2026 出版方正式版
  source_url: https://openaccess.thecvf.com/content/CVPR2026/papers/Li_HOPS_Hierarchical_Open-vocabulary_Part_Segmentation_with_Attention-Aware_Filtering_and_Affinity-Guided_CVPR_2026_paper.pdf
  source_sha256: 113a39aa908f51886b4d6206fe290b0e74e196333493ab62c44a25dfceaaa538
  clip_pdf_points:
  - 55
  - 50
  - 558
  - 308.3619689941406
methods:
- id: semantic-operation
  track: vocabulary
  problems:
  - regions
  - alignment
  title: 语义结构聚合
  question: 如何避免整物体过分割和部件漏激活？
  operation: 先融合 CLIP 语义注意力和 DINO 结构注意力，以 AFM 过滤对象代价图；再限制在预测对象区域内，对部件响应执行 AEM 亲和传播，逐步扩展欠激活部件。两阶段共享编码器但使用不同聚合模块。
  input: 图像、对象及对象—部件文本
  output: 对象约束下的部件掩码
  stage: 训练及推理
  supervision: 训练部件分割标注；预训练 CLIP／DINO
  origin: proposed
  origin_note: 本文设计的语义结构聚合流程；其预训练基础模型与通用组件沿用已有方法，不计作本文新提出。
  origin_refs:
  - url: https://openaccess.thecvf.com/content/CVPR2026/papers/Li_HOPS_Hierarchical_Open-vocabulary_Part_Segmentation_with_Attention-Aware_Filtering_and_Affinity-Guided_CVPR_2026_paper.pdf
    locator: 方法部分列明的基础模型及其参考文献
  evidence:
  - url: https://openaccess.thecvf.com/content/CVPR2026/papers/Li_HOPS_Hierarchical_Open-vocabulary_Part_Segmentation_with_Attention-Aware_Filtering_and_Affinity-Guided_CVPR_2026_paper.pdf
    locator: 方法部分；Figure 4（PDF 第 5 页）；实验 Table 3（PDF 第 7 页）
  figure: figure4
  figure_guide: 上半部是对象阶段 AFM 过滤，下面是对象区域内的 AEM 部件传播；两路都通过聚合代价与解码器生成结果，图中 // 表示停止梯度。
  depicted: true
  route:
  - CLIP 与 DINO
  - 语义结构聚合
  - 对象与部件代价图
  - 部件分割
  result_tables:
  - table3
results:
- id: table3
  label: Table 3
  asset: assets/results/hops-table3.png
  page: 7
  version: CVPR 2026 出版方正式版
  source_url: https://openaccess.thecvf.com/content/CVPR2026/papers/Li_HOPS_Hierarchical_Open-vocabulary_Part_Segmentation_with_Attention-Aware_Filtering_and_Affinity-Guided_CVPR_2026_paper.pdf
  source_sha256: 113a39aa908f51886b4d6206fe290b0e74e196333493ab62c44a25dfceaaa538
  clip_pdf_points:
  - 309
  - 55
  - 558
  - 202
  title: HOPS：主要实验结果
  setting: Pascal-Part-116 零样本结果；原表区分 Seen、Unseen、hIoU、mIoU。
  metrics: mIoU／hIoU ↑
  reading: 优先看 Unseen 与 hIoU，不能只用已见部件效果评价开放词汇能力。
---

# HOPS

本页按研究问题提取相关操作；模块原图、具体输入输出、来源与主要实验结果在上方展开查看。

## 研究问题

如何避免整物体过分割和部件漏激活？

## 相关操作

先融合 CLIP 语义注意力和 DINO 结构注意力，以 AFM 过滤对象代价图；再限制在预测对象区域内，对部件响应执行 AEM 亲和传播，逐步扩展欠激活部件。两阶段共享编码器但使用不同聚合模块。

## 实验阅读

Pascal-Part-116 零样本结果；原表区分 Seen、Unseen、hIoU、mIoU。 优先看 Unseen 与 hIoU，不能只用已见部件效果评价开放词汇能力。 主要结果是整套方法的效果，不能单凭该表归因到一个模块。

## 原文依据

- [出版方原文](https://openaccess.thecvf.com/content/CVPR2026/papers/Li_HOPS_Hierarchical_Open-vocabulary_Part_Segmentation_with_Attention-Aware_Filtering_and_Affinity-Guided_CVPR_2026_paper.pdf)：方法部分；Figure 4（PDF 第 5 页）；实验 Table 3（PDF 第 7 页）。
- [官方实现](https://github.com/TJU-IDVLab/HOPS)：已检查公开目录，未独立运行训练或评测。
