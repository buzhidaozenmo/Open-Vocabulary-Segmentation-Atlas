---
paper_id: cass
title: Distilling Spectral Graph for Object-Context Aware Open-Vocabulary Semantic Segmentation
short_name: CASS
authors:
- Kim, Chanyoung
- Ju, Dayun
- Han, Woojung
- Yang, Ming-Hsuan
- Hwang, Seong Jae
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
- PASCAL
- COCO
- Cityscapes
- ADE20K
paper_url: https://openaccess.thecvf.com/content/CVPR2025/papers/Kim_Distilling_Spectral_Graph_for_Object-Context_Aware_Open-Vocabulary_Semantic_Segmentation_CVPR_2025_paper.pdf
publication_url: https://openaccess.thecvf.com/content/CVPR2025/html/Kim_Distilling_Spectral_Graph_for_Object-Context_Aware_Open-Vocabulary_Semantic_Segmentation_CVPR_2025_paper.html
code_status: public
code_url: https://github.com/MICV-yonsei/CASS
code_details: 已核对官方仓库实际实现目录：cass_segmentor.py、clip、configs、custom_datasets.py、datasets、dino。运行及外部权重可用性未独立复现。
content_status: index
checked_on: '2026-11-09'
module_checked_on: '2026-11-09'
summary: 把视觉基础模型和 CLIP 的注意力表示成图，逐头匹配互补图并进行低秩谱特征缩放，将对象上下文注入 CLIP；再用对象存在先验修正文本嵌入，强化完整对象的图文对应。
sources:
- url: https://openaccess.thecvf.com/content/CVPR2025/html/Kim_Distilling_Spectral_Graph_for_Object-Context_Aware_Open-Vocabulary_Semantic_Segmentation_CVPR_2025_paper.html
  locator: 正式发表页面及作者信息
- url: https://openaccess.thecvf.com/content/CVPR2025/papers/Kim_Distilling_Spectral_Graph_for_Object-Context_Aware_Open-Vocabulary_Semantic_Segmentation_CVPR_2025_paper.pdf
  locator: 方法部分；Figure 2（PDF 第 3 页）；实验 Table 1（PDF 第 6 页）
- url: https://github.com/MICV-yonsei/CASS
  locator: 官方 README 与实际代码目录；不表示已运行
figures:
- id: figure2
  label: Figure 2
  asset: assets/figures/cass-figure2.png
  page: 3
  version: CVPR 2025 出版方正式版
  source_url: https://openaccess.thecvf.com/content/CVPR2025/papers/Kim_Distilling_Spectral_Graph_for_Object-Context_Aware_Open-Vocabulary_Semantic_Segmentation_CVPR_2025_paper.pdf
  source_sha256: 057f4f7ade28f1d87848632ad82ba1ea0d131f2959fad65078c3e42aabfbb08a
  clip_pdf_points:
  - 55
  - 50
  - 558
  - 241.82118225097656
methods:
- id: semantic-operation
  track: vocabulary
  problems:
  - alignment
  - regions
  title: 对象谱图融合
  question: 如何让一个对象的不同部件响应为同一类别？
  operation: 把视觉基础模型和 CLIP 的注意力表示成图，逐头匹配互补图并进行低秩谱特征缩放，将对象上下文注入 CLIP；再用对象存在先验修正文本嵌入，强化完整对象的图文对应。
  input: 视觉模型／CLIP 注意图及类别文本
  output: 对象上下文一致的语言特征
  stage: 免任务训练推理
  supervision: 预训练 CLIP 与视觉基础模型
  origin: proposed
  origin_note: 本文设计的对象谱图融合流程；其预训练基础模型与通用组件沿用已有方法，不计作本文新提出。
  origin_refs:
  - url: https://openaccess.thecvf.com/content/CVPR2025/papers/Kim_Distilling_Spectral_Graph_for_Object-Context_Aware_Open-Vocabulary_Semantic_Segmentation_CVPR_2025_paper.pdf
    locator: 方法部分列明的基础模型及其参考文献
  evidence:
  - url: https://openaccess.thecvf.com/content/CVPR2025/papers/Kim_Distilling_Spectral_Graph_for_Object-Context_Aware_Open-Vocabulary_Semantic_Segmentation_CVPR_2025_paper.pdf
    locator: 方法部分；Figure 2（PDF 第 3 页）；实验 Table 1（PDF 第 6 页）
  figure: figure2
  figure_guide: 沿左侧 VFM／CLIP 注意图进入中部 head-by-head spectral graph matching，再看低秩谱缩放后的图如何替换／增强右侧 CLIP 注意关系。
  depicted: true
  route:
  - CLIP 与视觉谱图
  - 对象谱图融合
  - 像素语言特征
  - 开放词汇分割
  result_tables:
  - table1
results:
- id: table1
  label: Table 1
  asset: assets/results/cass-table1.png
  page: 6
  version: CVPR 2025 出版方正式版
  source_url: https://openaccess.thecvf.com/content/CVPR2025/papers/Kim_Distilling_Spectral_Graph_for_Object-Context_Aware_Open-Vocabulary_Semantic_Segmentation_CVPR_2025_paper.pdf
  source_sha256: 057f4f7ade28f1d87848632ad82ba1ea0d131f2959fad65078c3e42aabfbb08a
  clip_pdf_points:
  - 55
  - 55
  - 558
  - 327
  title: CASS：主要实验结果
  setting: 八基准；保留 Supporting Dataset、Extra Training 与模型分组。
  metrics: mIoU ↑
  reading: 这里的蒸馏发生在免训练特征／注意图操作中，不等于训练一个新学生网络。
---

# CASS

本页按研究问题提取相关操作；模块原图、具体输入输出、来源与主要实验结果在上方展开查看。

## 研究问题

如何让一个对象的不同部件响应为同一类别？

## 相关操作

把视觉基础模型和 CLIP 的注意力表示成图，逐头匹配互补图并进行低秩谱特征缩放，将对象上下文注入 CLIP；再用对象存在先验修正文本嵌入，强化完整对象的图文对应。

## 实验阅读

八基准；保留 Supporting Dataset、Extra Training 与模型分组。 这里的蒸馏发生在免训练特征／注意图操作中，不等于训练一个新学生网络。 主要结果是整套方法的效果，不能单凭该表归因到一个模块。

## 原文依据

- [出版方原文](https://openaccess.thecvf.com/content/CVPR2025/papers/Kim_Distilling_Spectral_Graph_for_Object-Context_Aware_Open-Vocabulary_Semantic_Segmentation_CVPR_2025_paper.pdf)：方法部分；Figure 2（PDF 第 3 页）；实验 Table 1（PDF 第 6 页）。
- [官方实现](https://github.com/MICV-yonsei/CASS)：已检查公开目录，未独立运行训练或评测。
