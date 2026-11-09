---
paper_id: dinotxt
title: 'DINOv2 Meets Text: A Unified Framework for Image- and Pixel-Level Vision-Language Alignment'
short_name: dino.txt
authors:
- Jose, Cijo
- Moutakanni, Théo
- Kang, Dahyun
- Baldassarre, Federico
- Darcet, Timothée
- Xu, Hu
- Li, Daniel
- Szafraniec, Marc
- Ramamonjisoa, Michaël
- Oquab, Maxime
- Siméoni, Oriane
- Vo, Huy V.
- Labatut, Patrick
- Bojanowski, Piotr
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
datasets: []
paper_url: https://openaccess.thecvf.com/content/CVPR2025/papers/Jose_DINOv2_Meets_Text_A_Unified_Framework_for_Image-_and_Pixel-Level_CVPR_2025_paper.pdf
publication_url: https://openaccess.thecvf.com/content/CVPR2025/html/Jose_DINOv2_Meets_Text_A_Unified_Framework_for_Image-_and_Pixel-Level_CVPR_2025_paper.html
code_status: public
code_url: https://github.com/facebookresearch/dinov2
code_details: 官方 DINOv2 仓库公开 dino.txt 模型、文本／稠密推理与权重入口；未运行，不把仅推理发布等同于全套预训练复现。
content_status: index
checked_on: '2026-11-09'
module_checked_on: '2026-11-09'
summary: 冻结 DINOv2 视觉编码器，训练文本侧与其对齐；将 CLS 和 patch 均值拼接作为图像表示，并联合图像／文本数据筛选保留细粒度语义，推理时把文本原型与稠密 patch 特征比较。
sources:
- url: https://openaccess.thecvf.com/content/CVPR2025/html/Jose_DINOv2_Meets_Text_A_Unified_Framework_for_Image-_and_Pixel-Level_CVPR_2025_paper.html
  locator: 正式发表来源：出版页面／作者项目的会议说明
- url: https://openaccess.thecvf.com/content/CVPR2025/papers/Jose_DINOv2_Meets_Text_A_Unified_Framework_for_Image-_and_Pixel-Level_CVPR_2025_paper.pdf
  locator: 方法部分；Figure 2（PDF 第 4 页）；实验 Table 6（PDF 第 8 页）
- url: https://github.com/facebookresearch/dinov2
  locator: 官方 README、目录与开放范围；未独立运行
figures:
- id: fig2
  label: Figure 2
  asset: assets/figures/dinotxt-fig2.png
  page: 4
  version: CVPR 2025 出版方正式版
  source_url: https://openaccess.thecvf.com/content/CVPR2025/papers/Jose_DINOv2_Meets_Text_A_Unified_Framework_for_Image-_and_Pixel-Level_CVPR_2025_paper.pdf
  source_sha256: 56a9956c7845b97e2ce69a765e0d819aa4dbad56b8afbdc644d88eea6e0fb11f
  clip_pdf_points:
  - 45
  - 45
  - 567
  - 221.074
methods:
- id: semantic-operation
  track: vocabulary
  problems:
  - alignment
  title: 冻结视觉文本对齐
  question: 自监督视觉模型怎样获得像素级文本接口？
  operation: 冻结 DINOv2 视觉编码器，训练文本侧与其对齐；将 CLS 和 patch 均值拼接作为图像表示，并联合图像／文本数据筛选保留细粒度语义，推理时把文本原型与稠密 patch 特征比较。
  input: 图文配对、冻结 DINOv2 特征及文本
  output: 可文本查询的稠密视觉表示
  stage: 图文对齐训练及零样本分割
  supervision: 图像—文本配对，无像素语义分割训练标注
  origin: proposed
  origin_note: 本文设计的冻结视觉文本对齐流程；所用预训练模型、通用投影及基础算子沿用已有方法，不计作本文新提出。
  evidence:
  - url: https://openaccess.thecvf.com/content/CVPR2025/papers/Jose_DINOv2_Meets_Text_A_Unified_Framework_for_Image-_and_Pixel-Level_CVPR_2025_paper.pdf
    locator: 方法部分；Figure 2（PDF 第 4 页）；实验 Table 6（PDF 第 8 页）
  figure: fig2
  figure_guide: 看局部概念定位与 text encoder alignment，注意 CLS 和 patch average 的聚合。
  depicted: true
  route:
  - 预训练视觉语言特征
  - 冻结视觉文本对齐
  - 像素／区域类别表示
  - 开放词汇分割
  result_tables:
  - table6
results:
- id: table6
  label: Table 6
  asset: assets/results/dinotxt-table6.png
  page: 8
  version: CVPR 2025 出版方正式版
  source_url: https://openaccess.thecvf.com/content/CVPR2025/papers/Jose_DINOv2_Meets_Text_A_Unified_Framework_for_Image-_and_Pixel-Level_CVPR_2025_paper.pdf
  source_sha256: 56a9956c7845b97e2ce69a765e0d819aa4dbad56b8afbdc644d88eea6e0fb11f
  clip_pdf_points:
  - 60
  - 250
  - 306
  - 487
  title: dino.txt：主要实验结果
  setting: 开放词汇语义分割主表；与分类和检索结果分开。
  metrics: mIoU ↑
  reading: 按骨干、训练数据及推理设置比较，不把分类 Top-1 当分割效果。
---

# dino.txt

本页按研究问题提取相关操作；模块图、输入输出、证据和主要结果表在上方展开查看。

## 研究问题

自监督视觉模型怎样获得像素级文本接口？

## 相关操作

冻结 DINOv2 视觉编码器，训练文本侧与其对齐；将 CLS 和 patch 均值拼接作为图像表示，并联合图像／文本数据筛选保留细粒度语义，推理时把文本原型与稠密 patch 特征比较。

## 实验阅读

开放词汇语义分割主表；与分类和检索结果分开。 按骨干、训练数据及推理设置比较，不把分类 Top-1 当分割效果。 主表是整体系统结果，单一模块的贡献需结合原文消融。

## 原文依据

- [本次阅读的原文版本](https://openaccess.thecvf.com/content/CVPR2025/papers/Jose_DINOv2_Meets_Text_A_Unified_Framework_for_Image-_and_Pixel-Level_CVPR_2025_paper.pdf)：方法部分；Figure 2（PDF 第 4 页）；实验 Table 6（PDF 第 8 页）。
- [正式发表来源](https://openaccess.thecvf.com/content/CVPR2025/html/Jose_DINOv2_Meets_Text_A_Unified_Framework_for_Image-_and_Pixel-Level_CVPR_2025_paper.html)。
- [官方实现](https://github.com/facebookresearch/dinov2)：官方 DINOv2 仓库公开 dino.txt 模型、文本／稠密推理与权重入口；未运行，不把仅推理发布等同于全套预训练复现。
