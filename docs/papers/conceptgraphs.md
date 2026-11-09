---
paper_id: conceptgraphs
title: 'ConceptGraphs: Open-Vocabulary 3D Scene Graphs for Perception and Planning'
short_name: ConceptGraphs
authors:
- Qiao Gu
- Ali Kuwajerwala
- Sacha Morin
- Krishna Murthy Jatavallabhula
- Bipasha Sen
- Aditya Agarwal
- Corban Rivera
- William Paul
- Kirsty Ellis
- Rama Chellappa
- Chuang Gan
- Celso Miguel de Melo
- Joshua B. Tenenbaum
- Antonio Torralba
- Florian Shkurti
- Liam Paull
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
datasets:
- Replica
paper_url: https://arxiv.org/pdf/2309.16650v1
publication_url: https://concept-graphs.github.io/
code_status: public
code_url: https://github.com/concept-graphs/concept-graphs
code_details: 已核对官方实现目录：README_streamlined_detection.md、conceptgraph、env_vars.bash.template、environment.yml、setup.py。未独立运行或验证外部权重下载。
content_status: index
checked_on: '2026-11-09'
module_checked_on: '2026-11-09'
summary: 将二维实例掩码反投影成对象点云，结合空间与语义相似度匹配已有对象并融合；保存对象 CLIP 特征及语言描述，再利用对象关系建立可语言查询的场景图。
sources:
- url: https://concept-graphs.github.io/
  locator: 正式发表来源：出版页面／作者项目的会议说明
- url: https://arxiv.org/pdf/2309.16650v1
  locator: 方法部分；Fig. 2（PDF 第 3 页）；实验 TABLE III（PDF 第 5 页）
- url: https://github.com/concept-graphs/concept-graphs
  locator: 官方 README、目录与开放范围；未独立运行
figures:
- id: fig2
  label: Fig. 2
  asset: assets/figures/conceptgraphs-fig2.png
  page: 3
  version: arXiv 2309.16650v1
  source_url: https://arxiv.org/pdf/2309.16650v1
  source_sha256: 1435b96cea1e15a8e1c07ea75a5805c8520925a176817aa78a5a5a178a4b2002
  clip_pdf_points:
  - 45
  - 45
  - 567
  - 251.091
methods:
- id: semantic-operation
  track: pointcloud
  problems:
  - projection
  - multiview
  - regions
  title: 实例地图关联与语义图
  question: 如何将多视图语义从点级压缩为对象节点？
  operation: 将二维实例掩码反投影成对象点云，结合空间与语义相似度匹配已有对象并融合；保存对象 CLIP 特征及语言描述，再利用对象关系建立可语言查询的场景图。
  input: 位姿 RGB-D、二维实例、CLIP 与语言描述
  output: 对象点云节点与语义场景图
  stage: 对象建图、描述生成及查询推理
  supervision: 预训练分割／视觉语言模型和 MLLM，无目标场景语义训练
  origin: proposed
  origin_note: 本文设计的实例地图关联与语义图流程；所用预训练模型、通用投影及基础算子沿用已有方法，不计作本文新提出。
  evidence:
  - url: https://arxiv.org/pdf/2309.16650v1
    locator: 方法部分；Fig. 2（PDF 第 3 页）；实验 TABLE III（PDF 第 5 页）
  figure: fig2
  figure_guide: 沿 mask detection、对象点云关联融合、caption 和 graph edge construction 阅读。
  depicted: true
  route:
  - 多视角二维语义
  - 实例地图关联与语义图
  - 三维实例／点特征
  - 三维分割与查询
  result_tables:
  - tableiii
results:
- id: tableiii
  label: TABLE III
  asset: assets/results/conceptgraphs-tableiii.png
  page: 5
  version: arXiv 2309.16650v1
  source_url: https://arxiv.org/pdf/2309.16650v1
  source_sha256: 1435b96cea1e15a8e1c07ea75a5805c8520925a176817aa78a5a5a178a4b2002
  clip_pdf_points:
  - 309
  - 45
  - 562
  - 242
  title: ConceptGraphs：主要实验结果
  setting: Replica 与 REAL Lab 的文本对象检索，分别比较 CLIP 相似度与 LLM 查询。
  metrics: Top-1／2／3 recall ↑
  reading: 这里是对象检索召回率，不是像素分割 IoU 或场景图节点精度。
---

# ConceptGraphs

本页按研究问题提取相关操作；模块图、输入输出、证据和主要结果表在上方展开查看。

## 研究问题

如何将多视图语义从点级压缩为对象节点？

## 相关操作

将二维实例掩码反投影成对象点云，结合空间与语义相似度匹配已有对象并融合；保存对象 CLIP 特征及语言描述，再利用对象关系建立可语言查询的场景图。

## 实验阅读

Replica 与 REAL Lab 的文本对象检索，分别比较 CLIP 相似度与 LLM 查询。 这里是对象检索召回率，不是像素分割 IoU 或场景图节点精度。 主表是整体系统结果，单一模块的贡献需结合原文消融。

## 原文依据

- [本次阅读的原文版本](https://arxiv.org/pdf/2309.16650v1)：方法部分；Fig. 2（PDF 第 3 页）；实验 TABLE III（PDF 第 5 页）。
- [正式发表来源](https://concept-graphs.github.io/)。
- [官方实现](https://github.com/concept-graphs/concept-graphs)：已核对官方实现目录：README_streamlined_detection.md、conceptgraph、env_vars.bash.template、environment.yml、setup.py。未独立运行或验证外部权重下载。
