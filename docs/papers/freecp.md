---
paper_id: freecp
title: Training-Free Class Purification for Open-Vocabulary Semantic Segmentation
short_name: FreeCP
authors:
- Chen, Qi
- Yang, Lingxiao
- Chen, Yun
- Zhao, Nailong
- Lai, Jianhuang
- Shao, Jie
- Xie, Xiaohua
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
paper_url: https://openaccess.thecvf.com/content/ICCV2025/papers/Chen_Training-Free_Class_Purification_for_Open-Vocabulary_Semantic_Segmentation_ICCV_2025_paper.pdf
publication_url: https://openaccess.thecvf.com/content/ICCV2025/html/Chen_Training-Free_Class_Purification_for_Open-Vocabulary_Semantic_Segmentation_ICCV_2025_paper.html
code_status: public
code_url: https://github.com/chenqi1126/FreeCP
code_details: 已核对官方仓库实际实现目录：configs、custom_datasets.py、dist_test.sh、eval.py、freecp_segmentor.py、open_clip。运行及外部权重可用性未独立复现。
content_status: index
checked_on: '2026-11-09'
module_checked_on: '2026-11-09'
summary: 同时计算图文激活与视觉亲和细化激活，以二者空间一致性识别不在图中的冗余类别；再在保留集合中比较类间关系进行歧义净化，最后只用净化类别重新决定像素标签。
sources:
- url: https://openaccess.thecvf.com/content/ICCV2025/html/Chen_Training-Free_Class_Purification_for_Open-Vocabulary_Semantic_Segmentation_ICCV_2025_paper.html
  locator: 正式发表页面及作者信息
- url: https://openaccess.thecvf.com/content/ICCV2025/papers/Chen_Training-Free_Class_Purification_for_Open-Vocabulary_Semantic_Segmentation_ICCV_2025_paper.pdf
  locator: 方法部分；Figure 4（PDF 第 5 页）；实验 Table 2（PDF 第 7 页）
- url: https://github.com/chenqi1126/FreeCP
  locator: 官方 README 与实际代码目录；不表示已运行
figures:
- id: figure4
  label: Figure 4
  asset: assets/figures/freecp-figure4.png
  page: 5
  version: ICCV 2025 出版方正式版
  source_url: https://openaccess.thecvf.com/content/ICCV2025/papers/Chen_Training-Free_Class_Purification_for_Open-Vocabulary_Semantic_Segmentation_ICCV_2025_paper.pdf
  source_sha256: b03fa9afb26b4b2c6e1cff2eae5f5ee613829cb50239c3aeac94691a7a657ef0
  clip_pdf_points:
  - 55
  - 50
  - 558
  - 275.8091125488281
methods:
- id: semantic-operation
  track: vocabulary
  problems:
  - unseen
  - reliability
  title: 类别净化
  question: 不存在类别与语义相近类别怎样分别排除？
  operation: 同时计算图文激活与视觉亲和细化激活，以二者空间一致性识别不在图中的冗余类别；再在保留集合中比较类间关系进行歧义净化，最后只用净化类别重新决定像素标签。
  input: 全词汇类别、CLIP 激活及视觉自亲和
  output: 净化类别集合与最终像素类别
  stage: 免任务训练推理
  supervision: 预训练 CLIP，可接入已有免训练分割器
  origin: proposed
  origin_note: 本文设计的类别净化流程；其预训练基础模型与通用组件沿用已有方法，不计作本文新提出。
  origin_refs:
  - url: https://openaccess.thecvf.com/content/ICCV2025/papers/Chen_Training-Free_Class_Purification_for_Open-Vocabulary_Semantic_Segmentation_ICCV_2025_paper.pdf
    locator: 方法部分列明的基础模型及其参考文献
  evidence:
  - url: https://openaccess.thecvf.com/content/ICCV2025/papers/Chen_Training-Free_Class_Purification_for_Open-Vocabulary_Semantic_Segmentation_ICCV_2025_paper.pdf
    locator: 方法部分；Figure 4（PDF 第 5 页）；实验 Table 2（PDF 第 7 页）
  figure: figure4
  figure_guide: 本图独立展示 Class Purification：上部 (a) Redundancy Purification 用空间一致性去除不存在类别，下部 (b) Ambiguity Purification 比较剩余类别关系。
  depicted: true
  route:
  - CLIP 图文激活
  - 类别净化
  - 筛选词汇与像素分数
  - 开放词汇分割
  result_tables:
  - table2
results:
- id: table2
  label: Table 2
  asset: assets/results/freecp-table2.png
  page: 7
  version: ICCV 2025 出版方正式版
  source_url: https://openaccess.thecvf.com/content/ICCV2025/papers/Chen_Training-Free_Class_Purification_for_Open-Vocabulary_Semantic_Segmentation_ICCV_2025_paper.pdf
  source_sha256: b03fa9afb26b4b2c6e1cff2eae5f5ee613829cb50239c3aeac94691a7a657ef0
  clip_pdf_points:
  - 55
  - 56
  - 558
  - 385
  title: FreeCP：主要实验结果
  setting: 八基准；分别比较接入不同基础方法后的 FreeCP 版本。
  metrics: mIoU ↑
  reading: 比较同一基础方法加／不加 FreeCP；不要把不同基础模型差异归因于净化模块。
---

# FreeCP

本页按研究问题提取相关操作；模块原图、具体输入输出、来源与主要实验结果在上方展开查看。

## 研究问题

不存在类别与语义相近类别怎样分别排除？

## 相关操作

同时计算图文激活与视觉亲和细化激活，以二者空间一致性识别不在图中的冗余类别；再在保留集合中比较类间关系进行歧义净化，最后只用净化类别重新决定像素标签。

## 实验阅读

八基准；分别比较接入不同基础方法后的 FreeCP 版本。 比较同一基础方法加／不加 FreeCP；不要把不同基础模型差异归因于净化模块。 主要结果是整套方法的效果，不能单凭该表归因到一个模块。

## 原文依据

- [出版方原文](https://openaccess.thecvf.com/content/ICCV2025/papers/Chen_Training-Free_Class_Purification_for_Open-Vocabulary_Semantic_Segmentation_ICCV_2025_paper.pdf)：方法部分；Figure 4（PDF 第 5 页）；实验 Table 2（PDF 第 7 页）。
- [官方实现](https://github.com/chenqi1126/FreeCP)：已检查公开目录，未独立运行训练或评测。
