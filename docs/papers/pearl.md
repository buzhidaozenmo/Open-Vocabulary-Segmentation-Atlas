---
paper_id: pearl
title: 'PEARL: Geometry Aligns Semantics for Training-Free Open-Vocabulary Semantic Segmentation'
short_name: PEARL
authors:
- Pei, Gensheng
- Jiang, Xiruo
- Cai, Xinhao
- Chen, Tao
- Yao, Yazhou
- Jeon, Byeungwoo
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
- COCO
- Cityscapes
- ADE20K
paper_url: https://openaccess.thecvf.com/content/CVPR2026/papers/Pei_PEARL_Geometry_Aligns_Semantics_for_Training-Free_Open-Vocabulary_Semantic_Segmentation_CVPR_2026_paper.pdf
publication_url: https://openaccess.thecvf.com/content/CVPR2026/html/Pei_PEARL_Geometry_Aligns_Semantics_for_Training-Free_Open-Vocabulary_Semantic_Segmentation_CVPR_2026_paper.html
code_status: public
code_url: https://github.com/PGSmall/PEARL
code_details: 已核对官方仓库实际实现目录：clip、configs、convert_dataset、custom_datasets.py、eval.py、pearl。运行及外部权重可用性未独立复现。
content_status: index
checked_on: '2026-11-09'
module_checked_on: '2026-11-09'
summary: 在最后自注意力块对查询键加权去中心，用正交 Procrustes 旋转把键对齐到查询子空间；计算图文相似度后，在紧凑网格上求解文本引导的拉普拉斯传播，以置信度和图像梯度约束邻域平滑。
sources:
- url: https://openaccess.thecvf.com/content/CVPR2026/html/Pei_PEARL_Geometry_Aligns_Semantics_for_Training-Free_Open-Vocabulary_Semantic_Segmentation_CVPR_2026_paper.html
  locator: 正式发表页面及作者信息
- url: https://openaccess.thecvf.com/content/CVPR2026/papers/Pei_PEARL_Geometry_Aligns_Semantics_for_Training-Free_Open-Vocabulary_Semantic_Segmentation_CVPR_2026_paper.pdf
  locator: 方法部分；Figure 2（PDF 第 4 页）；实验 Table 1（PDF 第 5 页）
- url: https://github.com/PGSmall/PEARL
  locator: 官方 README 与实际代码目录；不表示已运行
figures:
- id: figure2
  label: Figure 2
  asset: assets/figures/pearl-figure2.png
  page: 4
  version: CVPR 2026 出版方正式版
  source_url: https://openaccess.thecvf.com/content/CVPR2026/papers/Pei_PEARL_Geometry_Aligns_Semantics_for_Training-Free_Open-Vocabulary_Semantic_Segmentation_CVPR_2026_paper.pdf
  source_sha256: 23a529216508710c8ef889509baa4302b0c53c7843c9ef9ee0b43f6bc83e83a7
  clip_pdf_points:
  - 55
  - 50
  - 558
  - 206.13926696777344
methods:
- id: semantic-operation
  track: vocabulary
  problems:
  - alignment
  - geometry
  title: 几何对齐与图传播
  question: 怎样同时校正跨模态特征和像素边界？
  operation: 在最后自注意力块对查询键加权去中心，用正交 Procrustes 旋转把键对齐到查询子空间；计算图文相似度后，在紧凑网格上求解文本引导的拉普拉斯传播，以置信度和图像梯度约束邻域平滑。
  input: 冻结 CLIP 查询键、类别文本、图像梯度
  output: 经对齐及图传播修正的像素分数
  stage: 免任务训练推理
  supervision: 预训练 CLIP；无需额外骨干和目标分割标注
  origin: proposed
  origin_note: 本文设计的几何对齐与图传播流程；其预训练基础模型与通用组件沿用已有方法，不计作本文新提出。
  origin_refs:
  - url: https://openaccess.thecvf.com/content/CVPR2026/papers/Pei_PEARL_Geometry_Aligns_Semantics_for_Training-Free_Open-Vocabulary_Semantic_Segmentation_CVPR_2026_paper.pdf
    locator: 方法部分列明的基础模型及其参考文献
  evidence:
  - url: https://openaccess.thecvf.com/content/CVPR2026/papers/Pei_PEARL_Geometry_Aligns_Semantics_for_Training-Free_Open-Vocabulary_Semantic_Segmentation_CVPR_2026_paper.pdf
    locator: 方法部分；Figure 2（PDF 第 4 页）；实验 Table 1（PDF 第 5 页）
  figure: figure2
  figure_guide: 左侧 Procrustes Alignment 调整注意力中的查询键空间；右侧 Text-aware Laplacian Propagation 用文本与图像邻域修正类别响应，两步按顺序执行。
  depicted: true
  route:
  - CLIP 与文本
  - 几何对齐与图传播
  - 像素类别分数
  - 开放词汇分割
  result_tables:
  - table1
results:
- id: table1
  label: Table 1
  asset: assets/results/pearl-table1.png
  page: 5
  version: CVPR 2026 出版方正式版
  source_url: https://openaccess.thecvf.com/content/CVPR2026/papers/Pei_PEARL_Geometry_Aligns_Semantics_for_Training-Free_Open-Vocabulary_Semantic_Segmentation_CVPR_2026_paper.pdf
  source_sha256: 23a529216508710c8ef889509baa4302b0c53c7843c9ef9ee0b43f6bc83e83a7
  clip_pdf_points:
  - 55
  - 54
  - 558
  - 456
  title: PEARL：主要实验结果
  setting: 八基准，保留 extra data、extra backbone、training-free 与背景协议。
  metrics: mIoU ↑
  reading: 先按外部数据／骨干条件分组，再比较 PEARL；本表是整体模型结果。
---

# PEARL

本页按研究问题提取相关操作；模块原图、具体输入输出、来源与主要实验结果在上方展开查看。

## 研究问题

怎样同时校正跨模态特征和像素边界？

## 相关操作

在最后自注意力块对查询键加权去中心，用正交 Procrustes 旋转把键对齐到查询子空间；计算图文相似度后，在紧凑网格上求解文本引导的拉普拉斯传播，以置信度和图像梯度约束邻域平滑。

## 实验阅读

八基准，保留 extra data、extra backbone、training-free 与背景协议。 先按外部数据／骨干条件分组，再比较 PEARL；本表是整体模型结果。 主要结果是整套方法的效果，不能单凭该表归因到一个模块。

## 原文依据

- [出版方原文](https://openaccess.thecvf.com/content/CVPR2026/papers/Pei_PEARL_Geometry_Aligns_Semantics_for_Training-Free_Open-Vocabulary_Semantic_Segmentation_CVPR_2026_paper.pdf)：方法部分；Figure 2（PDF 第 4 页）；实验 Table 1（PDF 第 5 页）。
- [官方实现](https://github.com/PGSmall/PEARL)：已检查公开目录，未独立运行训练或评测。
