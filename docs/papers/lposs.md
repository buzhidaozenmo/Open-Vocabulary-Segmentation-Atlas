---
paper_id: lposs
title: 'LPOSS: Label Propagation Over Patches and Pixels for Open-vocabulary Semantic Segmentation'
short_name: LPOSS+
authors:
- Stojnić, Vladan
- Kalantidis, Yannis
- Matas, Jiří
- Tolias, Giorgos
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
paper_url: https://openaccess.thecvf.com/content/CVPR2025/papers/Stojnic_LPOSS_Label_Propagation_Over_Patches_and_Pixels_for_Open-vocabulary_Semantic_CVPR_2025_paper.pdf
publication_url: https://openaccess.thecvf.com/content/CVPR2025/html/Stojnic_LPOSS_Label_Propagation_Over_Patches_and_Pixels_for_Open-vocabulary_Semantic_CVPR_2025_paper.html
code_status: public
code_url: https://github.com/vladan-stojnic/LPOSS
code_details: 已核对官方仓库实际实现目录：configs、datasets、environment.yml、helpers、main_eval.py、metrics。运行及外部权重可用性未独立复现。
content_status: index
checked_on: '2026-11-09'
module_checked_on: '2026-11-09'
summary: 先用视觉语言模型产生 patch 类别分数，再用独立视觉模型的 patch 亲和图做全图标签传播；将预测上采样后，在像素颜色图上再次传播以修正边界，避免仅靠 patch 插值。
sources:
- url: https://openaccess.thecvf.com/content/CVPR2025/html/Stojnic_LPOSS_Label_Propagation_Over_Patches_and_Pixels_for_Open-vocabulary_Semantic_CVPR_2025_paper.html
  locator: 正式发表页面及作者信息
- url: https://openaccess.thecvf.com/content/CVPR2025/papers/Stojnic_LPOSS_Label_Propagation_Over_Patches_and_Pixels_for_Open-vocabulary_Semantic_CVPR_2025_paper.pdf
  locator: 方法部分；Figure 2（PDF 第 5 页）；实验 Table 1（PDF 第 6 页）
- url: https://github.com/vladan-stojnic/LPOSS
  locator: 官方 README 与实际代码目录；不表示已运行
figures:
- id: figure2
  label: Figure 2
  asset: assets/figures/lposs-figure2.png
  page: 5
  version: CVPR 2025 出版方正式版
  source_url: https://openaccess.thecvf.com/content/CVPR2025/papers/Stojnic_LPOSS_Label_Propagation_Over_Patches_and_Pixels_for_Open-vocabulary_Semantic_CVPR_2025_paper.pdf
  source_sha256: 2493062e4db0919bb27511bb7145f6593af2af5494134742627c0514f1ea75a6
  clip_pdf_points:
  - 55
  - 50
  - 558
  - 201.14389038085938
methods:
- id: semantic-operation
  track: vocabulary
  problems:
  - alignment
  - regions
  title: 多尺度标签传播
  question: 文本分类粗图怎样沿视觉关系传播到像素？
  operation: 先用视觉语言模型产生 patch 类别分数，再用独立视觉模型的 patch 亲和图做全图标签传播；将预测上采样后，在像素颜色图上再次传播以修正边界，避免仅靠 patch 插值。
  input: VLM 类别分数、视觉 patch 特征、像素颜色
  output: 两级图传播后的像素类别图
  stage: 免任务训练推理
  supervision: 冻结视觉语言与视觉模型，无目标像素标注
  origin: proposed
  origin_note: 本文设计的多尺度标签传播流程；其预训练基础模型与通用组件沿用已有方法，不计作本文新提出。
  origin_refs:
  - url: https://openaccess.thecvf.com/content/CVPR2025/papers/Stojnic_LPOSS_Label_Propagation_Over_Patches_and_Pixels_for_Open-vocabulary_Semantic_CVPR_2025_paper.pdf
    locator: 方法部分列明的基础模型及其参考文献
  evidence:
  - url: https://openaccess.thecvf.com/content/CVPR2025/papers/Stojnic_LPOSS_Label_Propagation_Over_Patches_and_Pixels_for_Open-vocabulary_Semantic_CVPR_2025_paper.pdf
    locator: 方法部分；Figure 2（PDF 第 5 页）；实验 Table 1（PDF 第 6 页）
  figure: figure2
  figure_guide: 按 1–6 流程看窗口特征、全图 patch 标签传播、上采样和像素级 LPOSS+；两张图分别由视觉 patch 特征与像素颜色定义。
  depicted: true
  route:
  - VLM 与视觉模型
  - 多尺度标签传播
  - 像素类别分数
  - 开放词汇分割
  result_tables:
  - table1
results:
- id: table1
  label: Table 1
  asset: assets/results/lposs-table1.png
  page: 6
  version: CVPR 2025 出版方正式版
  source_url: https://openaccess.thecvf.com/content/CVPR2025/papers/Stojnic_LPOSS_Label_Propagation_Over_Patches_and_Pixels_for_Open-vocabulary_Semantic_CVPR_2025_paper.pdf
  source_sha256: 2493062e4db0919bb27511bb7145f6593af2af5494134742627c0514f1ea75a6
  clip_pdf_points:
  - 55
  - 56
  - 558
  - 235
  title: LPOSS+：主要实验结果
  setting: 八基准；两骨干均为 ViT-B/16，保留作者复测星号。
  metrics: mIoU ↑
  reading: LPOSS 与 LPOSS+ 分开看；像素级传播是 + 版本的边界细化。
---

# LPOSS+

本页按研究问题提取相关操作；模块原图、具体输入输出、来源与主要实验结果在上方展开查看。

## 研究问题

文本分类粗图怎样沿视觉关系传播到像素？

## 相关操作

先用视觉语言模型产生 patch 类别分数，再用独立视觉模型的 patch 亲和图做全图标签传播；将预测上采样后，在像素颜色图上再次传播以修正边界，避免仅靠 patch 插值。

## 实验阅读

八基准；两骨干均为 ViT-B/16，保留作者复测星号。 LPOSS 与 LPOSS+ 分开看；像素级传播是 + 版本的边界细化。 主要结果是整套方法的效果，不能单凭该表归因到一个模块。

## 原文依据

- [出版方原文](https://openaccess.thecvf.com/content/CVPR2025/papers/Stojnic_LPOSS_Label_Propagation_Over_Patches_and_Pixels_for_Open-vocabulary_Semantic_CVPR_2025_paper.pdf)：方法部分；Figure 2（PDF 第 5 页）；实验 Table 1（PDF 第 6 页）。
- [官方实现](https://github.com/vladan-stojnic/LPOSS)：已检查公开目录，未独立运行训练或评测。
