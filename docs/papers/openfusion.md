---
paper_id: openfusion
title: 'Open-Fusion: Real-time Open-Vocabulary 3D Mapping and Queryable Scene Representation'
short_name: Open-Fusion
authors:
- Yamazaki, Kashu
- Hanyu, Taisei
- Vo, Khoa
- Pham, Thang
- Tran, Minh
- Doretto, Gianfranco
- Nguyen, Anh
- Le, Ngan
year: 2024
preprint_date: unknown
venue: ICRA
publication_status: published
primary_direction: multiview
modalities:
- point_cloud
- image
task_setting: open_vocabulary
task_types:
- semantic
techniques:
- semantic_alignment
datasets: []
paper_url: https://arxiv.org/pdf/2310.03923v1
publication_url: https://uark-aicv.github.io/OpenFusion/
code_status: public
code_url: https://github.com/UARK-AICV/OpenFusion
code_details: 已核对官方实现目录：configs、deploy、docker、main.py、openfusion、query.py。未独立运行或验证外部权重下载。
content_status: index
checked_on: '2026-11-09'
module_checked_on: '2026-11-09'
summary: 从 SEEM 提取区域嵌入与置信图，以软 IoU 在观测区域和地图区域之间建立关联；将匹配区域语义与 TSDF 几何增量融合，建立支持文本查询的紧凑三维表示。
sources:
- url: https://uark-aicv.github.io/OpenFusion/
  locator: 正式发表来源：出版页面／作者项目的会议说明
- url: https://arxiv.org/pdf/2310.03923v1
  locator: 方法部分；Fig. 1（PDF 第 3 页）；实验 TABLE II（PDF 第 5 页）
- url: https://github.com/UARK-AICV/OpenFusion
  locator: 官方 README、目录与开放范围；未独立运行
figures:
- id: fig1
  label: Fig. 1
  asset: assets/figures/openfusion-fig1.png
  page: 3
  version: arXiv 2310.03923v1
  source_url: https://arxiv.org/pdf/2310.03923v1
  source_sha256: 6148eb692f6762b2d7d52433680b3d1e367d5aded3c086ce33098370aadeca14
  clip_pdf_points:
  - 45
  - 45
  - 567
  - 284.278
methods:
- id: semantic-operation
  track: pointcloud
  problems:
  - projection
  - multiview
  - efficiency
  title: 区域关联语义 TSDF
  question: 在线语义建图怎样避免保存大量重复特征？
  operation: 从 SEEM 提取区域嵌入与置信图，以软 IoU 在观测区域和地图区域之间建立关联；将匹配区域语义与 TSDF 几何增量融合，建立支持文本查询的紧凑三维表示。
  input: RGB-D、SEEM 区域嵌入／置信图与位姿
  output: 语义 TSDF 地图及区域特征
  stage: 在线重建、区域关联和语言查询
  supervision: 预训练 SEEM、深度与位姿，无目标三维语义标注
  origin: proposed
  origin_note: 本文设计的区域关联语义 TSDF流程；所用预训练模型、通用投影及基础算子沿用已有方法，不计作本文新提出。
  evidence:
  - url: https://arxiv.org/pdf/2310.03923v1
    locator: 方法部分；Fig. 1（PDF 第 3 页）；实验 TABLE II（PDF 第 5 页）
  figure: fig1
  figure_guide: 看 Real-time Semantic TSDF Reconstruction 与 Embedding Query 中区域关联、融合与查询路径。
  depicted: true
  route:
  - 多视角二维语义
  - 区域关联语义 TSDF
  - 三维实例／点特征
  - 三维分割与查询
  result_tables:
  - tableii
results:
- id: tableii
  label: TABLE II
  asset: assets/results/openfusion-tableii.png
  page: 5
  version: arXiv 2310.03923v1
  source_url: https://arxiv.org/pdf/2310.03923v1
  source_sha256: 6148eb692f6762b2d7d52433680b3d1e367d5aded3c086ce33098370aadeca14
  clip_pdf_points:
  - 309
  - 45
  - 562
  - 204
  title: Open-Fusion：主要实验结果
  setting: 三维重建与语义重建效率、分割指标；保留各输入和方法列。
  metrics: mAcc／f-mIoU ↑；FPS ↑
  reading: 这里的 f-mIoU 为原文定义的频率相关指标，不能与普通类别平均 mIoU 混排。
---

# Open-Fusion

本页按研究问题提取相关操作；模块图、输入输出、证据和主要结果表在上方展开查看。

## 研究问题

在线语义建图怎样避免保存大量重复特征？

## 相关操作

从 SEEM 提取区域嵌入与置信图，以软 IoU 在观测区域和地图区域之间建立关联；将匹配区域语义与 TSDF 几何增量融合，建立支持文本查询的紧凑三维表示。

## 实验阅读

三维重建与语义重建效率、分割指标；保留各输入和方法列。 这里的 f-mIoU 为原文定义的频率相关指标，不能与普通类别平均 mIoU 混排。 主表是整体系统结果，单一模块的贡献需结合原文消融。

## 原文依据

- [本次阅读的原文版本](https://arxiv.org/pdf/2310.03923v1)：方法部分；Fig. 1（PDF 第 3 页）；实验 TABLE II（PDF 第 5 页）。
- [正式发表来源](https://uark-aicv.github.io/OpenFusion/)。
- [官方实现](https://github.com/UARK-AICV/OpenFusion)：已核对官方实现目录：configs、deploy、docker、main.py、openfusion、query.py。未独立运行或验证外部权重下载。
