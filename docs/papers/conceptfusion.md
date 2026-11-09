---
paper_id: conceptfusion
title: 'ConceptFusion: Open-set Multimodal 3D Mapping'
short_name: ConceptFusion
authors:
- Krishna Murthy Jatavallabhula
- Alihusein Kuwajerwala
- Qiao Gu
- Mohd Omama
- Ganesh Iyer
- Soroush Saryazdi
- Tao Chen
- Alaa Maalouf
- Shuang Li
- Nikhil Varma Keetha
- Ayush Tewari
- Joshua Tenenbaum
- Celso de Melo
- Madhava Krishna
- Liam Paull
- Florian Shkurti
- Antonio Torralba
year: 2023
preprint_date: unknown
venue: RSS
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
datasets:
- ScanNet
- Replica
paper_url: https://www.roboticsproceedings.org/rss19/p066.pdf
publication_url: https://www.roboticsproceedings.org/rss19/p066.html
code_status: public
code_url: https://github.com/concept-fusion/concept-fusion
code_details: 已核对官方实现目录：examples。未独立运行或验证外部权重下载。
content_status: index
checked_on: '2026-11-09'
module_checked_on: '2026-11-09'
summary: 结合整图 CLIP 特征、区域特征及区域独特性为像素构造语言对齐特征；通过深度与位姿建立像素—三维对应，将多帧特征累积融合进点级地图，以文本、图像等查询检索。
sources:
- url: https://www.roboticsproceedings.org/rss19/p066.html
  locator: 正式发表来源：出版页面／作者项目的会议说明
- url: https://www.roboticsproceedings.org/rss19/p066.pdf
  locator: 方法部分；Fig. 2（PDF 第 3 页）；实验 TABLE V（PDF 第 8 页）
- url: https://github.com/concept-fusion/concept-fusion
  locator: 官方 README、目录与开放范围；未独立运行
figures:
- id: fig2
  label: Fig. 2
  asset: assets/figures/conceptfusion-fig2.png
  page: 3
  version: RSS 2023 出版方正式版
  source_url: https://www.roboticsproceedings.org/rss19/p066.pdf
  source_sha256: 1ab0d46e2bd276e8f6b2487026bbd6a98d0df222ada7123ad9e06aa63beb4d0a
  clip_pdf_points:
  - 45
  - 45
  - 567
  - 145.28
methods:
- id: semantic-operation
  track: pointcloud
  problems:
  - projection
  - multiview
  - alignment
  title: 局部全局语义多视图融合
  question: 区域 CLIP 语义怎样变成稠密点级地图？
  operation: 结合整图 CLIP 特征、区域特征及区域独特性为像素构造语言对齐特征；通过深度与位姿建立像素—三维对应，将多帧特征累积融合进点级地图，以文本、图像等查询检索。
  input: RGB-D、区域掩码、局部／全局 CLIP 与位姿
  output: 稠密语言对齐的三维点图
  stage: 特征提取、SLAM 融合与查询推理
  supervision: 预训练模型、深度及位姿，无目标语义训练
  origin: proposed
  origin_note: 本文设计的局部全局语义多视图融合流程；所用预训练模型、通用投影及基础算子沿用已有方法，不计作本文新提出。
  evidence:
  - url: https://www.roboticsproceedings.org/rss19/p066.pdf
    locator: 方法部分；Fig. 2（PDF 第 3 页）；实验 TABLE V（PDF 第 8 页）
  figure: fig2
  figure_guide: 看全局／局部特征加权到 pixel-aligned features，再投影累积到三维。
  depicted: true
  route:
  - 多视角二维语义
  - 局部全局语义多视图融合
  - 三维实例／点特征
  - 三维分割与查询
  result_tables:
  - tablev
results:
- id: tablev
  label: TABLE V
  asset: assets/results/conceptfusion-tablev.png
  page: 8
  version: RSS 2023 出版方正式版
  source_url: https://www.roboticsproceedings.org/rss19/p066.pdf
  source_sha256: 1ab0d46e2bd276e8f6b2487026bbd6a98d0df222ada7123ad9e06aa63beb4d0a
  clip_pdf_points:
  - 308
  - 224
  - 567
  - 400
  title: ConceptFusion：主要实验结果
  setting: ScanNet、Replica、SemanticKITTI 开放集合语义分割；阴影 Priv. 是额外特权监督参照。
  metrics: mIoU／mAcc 等 ↑
  reading: 先看 Priv. 分组，不能把有语义微调的参照视作同等零样本条件。
---

# ConceptFusion

本页按研究问题提取相关操作；模块图、输入输出、证据和主要结果表在上方展开查看。

## 研究问题

区域 CLIP 语义怎样变成稠密点级地图？

## 相关操作

结合整图 CLIP 特征、区域特征及区域独特性为像素构造语言对齐特征；通过深度与位姿建立像素—三维对应，将多帧特征累积融合进点级地图，以文本、图像等查询检索。

## 实验阅读

ScanNet、Replica、SemanticKITTI 开放集合语义分割；阴影 Priv. 是额外特权监督参照。 先看 Priv. 分组，不能把有语义微调的参照视作同等零样本条件。 主表是整体系统结果，单一模块的贡献需结合原文消融。

## 原文依据

- [本次阅读的原文版本](https://www.roboticsproceedings.org/rss19/p066.pdf)：方法部分；Fig. 2（PDF 第 3 页）；实验 TABLE V（PDF 第 8 页）。
- [正式发表来源](https://www.roboticsproceedings.org/rss19/p066.html)。
- [官方实现](https://github.com/concept-fusion/concept-fusion)：已核对官方实现目录：examples。未独立运行或验证外部权重下载。
