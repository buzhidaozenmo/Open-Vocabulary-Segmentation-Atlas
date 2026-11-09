---
paper_id: rns
title: 'Retrieve and Segment: Are a Few Examples Enough to Bridge the Supervision Gap in Open-Vocabulary Segmentation?'
short_name: RNS
authors:
- Aravanis, Tilemachos
- Stojnić, Vladan
- Psomas, Bill
- Komodakis, Nikos
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
- COCO
- PASCAL
paper_url: https://openaccess.thecvf.com/content/CVPR2026/papers/Aravanis_Retrieve_and_Segment_Are_a_Few_Examples_Enough_to_Bridge_CVPR_2026_paper.pdf
publication_url: https://openaccess.thecvf.com/content/CVPR2026/html/Aravanis_Retrieve_and_Segment_Are_a_Few_Examples_Enough_to_Bridge_CVPR_2026_paper.html
code_status: public
code_url: https://github.com/TilemahosAravanis/Retrieve-and-Segment
code_details: 已核对官方仓库实际实现目录：configs、core、datasets、dinov3、helpers、main_eval.py。运行及外部权重可用性未独立复现。
content_status: index
checked_on: '2026-11-09'
module_checked_on: '2026-11-09'
summary: 从像素标注支持图提取类别视觉特征；针对待测图检索相关支持样例，在测试时学习轻量图像专属分类器，联合利用文本原型与视觉支持特征预测像素类别。
sources:
- url: https://openaccess.thecvf.com/content/CVPR2026/html/Aravanis_Retrieve_and_Segment_Are_a_Few_Examples_Enough_to_Bridge_CVPR_2026_paper.html
  locator: 正式发表页面及作者信息
- url: https://openaccess.thecvf.com/content/CVPR2026/papers/Aravanis_Retrieve_and_Segment_Are_a_Few_Examples_Enough_to_Bridge_CVPR_2026_paper.pdf
  locator: 方法部分；Figure 2（PDF 第 4 页）；实验 Table 2（PDF 第 8 页）
- url: https://github.com/TilemahosAravanis/Retrieve-and-Segment
  locator: 官方 README 与实际代码目录；不表示已运行
figures:
- id: figure2
  label: Figure 2
  asset: assets/figures/rns-figure2.png
  page: 4
  version: CVPR 2026 出版方正式版
  source_url: https://openaccess.thecvf.com/content/CVPR2026/papers/Aravanis_Retrieve_and_Segment_Are_a_Few_Examples_Enough_to_Bridge_CVPR_2026_paper.pdf
  source_sha256: 973edf7578988882dd2d49ac2c9fe5bc1e26cbfbb817b8f39a1bc6aa952e388f
  clip_pdf_points:
  - 55
  - 50
  - 558
  - 188.9451446533203
methods:
- id: semantic-operation
  track: vocabulary
  problems:
  - prompt
  - unseen
  title: 检索与提示适配
  question: 如何用少量标注样例消除文本类别歧义？
  operation: 从像素标注支持图提取类别视觉特征；针对待测图检索相关支持样例，在测试时学习轻量图像专属分类器，联合利用文本原型与视觉支持特征预测像素类别。
  input: 待测图、类别文本、带像素标注的支持图
  output: 逐像素类别图
  stage: 测试时适配及推理
  supervision: 支持图像素类别标注；预训练视觉语言特征
  origin: proposed
  origin_note: 本文设计的检索与提示适配流程；其预训练基础模型与通用组件沿用已有方法，不计作本文新提出。
  origin_refs:
  - url: https://openaccess.thecvf.com/content/CVPR2026/papers/Aravanis_Retrieve_and_Segment_Are_a_Few_Examples_Enough_to_Bridge_CVPR_2026_paper.pdf
    locator: 方法部分列明的基础模型及其参考文献
  evidence:
  - url: https://openaccess.thecvf.com/content/CVPR2026/papers/Aravanis_Retrieve_and_Segment_Are_a_Few_Examples_Enough_to_Bridge_CVPR_2026_paper.pdf
    locator: 方法部分；Figure 2（PDF 第 4 页）；实验 Table 2（PDF 第 8 页）
  figure: figure2
  figure_guide: 从左侧带像素标注的 support images 提取视觉类别特征，沿 retrieval 到图像专属 classifier；再看 query features 如何与文本／视觉支持共同分类。
  depicted: true
  route:
  - 文本与支持样例
  - 检索与提示适配
  - 像素类别分数
  - 开放词汇分割
  result_tables:
  - table2
results:
- id: table2
  label: Table 2
  asset: assets/results/rns-table2.png
  page: 8
  version: CVPR 2026 出版方正式版
  source_url: https://openaccess.thecvf.com/content/CVPR2026/papers/Aravanis_Retrieve_and_Segment_Are_a_Few_Examples_Enough_to_Bridge_CVPR_2026_paper.pdf
  source_sha256: 973edf7578988882dd2d49ac2c9fe5bc1e26cbfbb817b8f39a1bc6aa952e388f
  clip_pdf_points:
  - 309
  - 48
  - 558
  - 160
  title: RNS：主要实验结果
  setting: Table 2 对比开放词汇与全监督分割；保留支持样例量、标注量和数据域。
  metrics: mIoU ↑
  reading: 按支持集大小及是否提供文本比较；这是含标注支持的少样本设置。
---

# RNS

本页按研究问题提取相关操作；模块原图、具体输入输出、来源与主要实验结果在上方展开查看。

## 研究问题

如何用少量标注样例消除文本类别歧义？

## 相关操作

从像素标注支持图提取类别视觉特征；针对待测图检索相关支持样例，在测试时学习轻量图像专属分类器，联合利用文本原型与视觉支持特征预测像素类别。

## 实验阅读

Table 2 对比开放词汇与全监督分割；保留支持样例量、标注量和数据域。 按支持集大小及是否提供文本比较；这是含标注支持的少样本设置。 主要结果是整套方法的效果，不能单凭该表归因到一个模块。

## 原文依据

- [出版方原文](https://openaccess.thecvf.com/content/CVPR2026/papers/Aravanis_Retrieve_and_Segment_Are_a_Few_Examples_Enough_to_Bridge_CVPR_2026_paper.pdf)：方法部分；Figure 2（PDF 第 4 页）；实验 Table 2（PDF 第 8 页）。
- [官方实现](https://github.com/TilemahosAravanis/Retrieve-and-Segment)：已检查公开目录，未独立运行训练或评测。
