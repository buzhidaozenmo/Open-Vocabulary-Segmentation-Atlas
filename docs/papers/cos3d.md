---
paper_id: cos3d
title: 'COS3D: Collaborative Open-Vocabulary 3D Segmentation'
short_name: COS3D
authors:
- Runsong Zhu
- Ka-Hei Hui
- Zhengzhe Liu
- Qianyi Wu
- Weiliang Tang
- Shi Qiu
- Pheng-Ann Heng
- Chi-Wing Fu
year: 2025
preprint_date: unknown
venue: NeurIPS
publication_status: published
primary_direction: 3dgs
modalities:
- gaussian
- image
task_setting: open_vocabulary
task_types:
- semantic
techniques:
- semantic_alignment
datasets: []
paper_url: https://arxiv.org/pdf/2510.20238v1
publication_url: https://papers.neurips.cc/paper_files/paper/2025/hash/10a6bdcabbd5a3d36b760daa295f63c1-Abstract-Conference.html
code_status: public
code_url: https://github.com/Runsong123/COS3D
code_details: 已核对官方实现目录：Grounding_3D.py、LICENSE.md、__pycache__、arguments、autoencoder、compute_lerf_iou_check.py。未独立运行或验证外部权重下载。
content_status: index
checked_on: '2026-11-09'
module_checked_on: '2026-11-09'
summary: 协同字段同时保存实例与语言两种表示，两阶段训练中以实例到语言映射建立关联；推理时用语言响应自适应细化实例提示，再在实例字段中完成目标分割。
sources:
- url: https://papers.neurips.cc/paper_files/paper/2025/hash/10a6bdcabbd5a3d36b760daa295f63c1-Abstract-Conference.html
  locator: 正式发表来源：出版页面／作者项目的会议说明
- url: https://arxiv.org/pdf/2510.20238v1
  locator: 方法部分；Figure 2（PDF 第 4 页）；实验 Table 1（PDF 第 7 页）
- url: https://github.com/Runsong123/COS3D
  locator: 官方 README、目录与开放范围；未独立运行
figures:
- id: fig2
  label: Figure 2
  asset: assets/figures/cos3d-fig2.png
  page: 4
  version: arXiv 2510.20238v1
  source_url: https://arxiv.org/pdf/2510.20238v1
  source_sha256: 4ef11ad250ca192135fcaa3a6965a60360eca9bec8e8bad983ab4c39780ea9b3
  clip_pdf_points:
  - 45
  - 45
  - 567
  - 258.585
methods:
- id: semantic-operation
  track: vocabulary
  problems:
  - alignment
  - prompt
  - regions
  title: 实例语言协同字段
  question: 文本粗定位如何得到准确三维实例边界？
  operation: 协同字段同时保存实例与语言两种表示，两阶段训练中以实例到语言映射建立关联；推理时用语言响应自适应细化实例提示，再在实例字段中完成目标分割。
  input: 多视角语义／实例教师、三维高斯和文本
  output: 协同语言及实例字段与目标掩码
  stage: 两阶段场景训练及提示分割推理
  supervision: 二维实例和语言特征教师、场景重建
  origin: proposed
  origin_note: 本文设计的实例语言协同字段流程；所用预训练模型、通用投影及基础算子沿用已有方法，不计作本文新提出。
  evidence:
  - url: https://arxiv.org/pdf/2510.20238v1
    locator: 方法部分；Figure 2（PDF 第 4 页）；实验 Table 1（PDF 第 7 页）
  figure: fig2
  figure_guide: 沿 instance-to-language feature mapping 和 adaptive language-to-instance prompt refinement 阅读。
  depicted: true
  route:
  - 多模态语言提示
  - 实例语言协同字段
  - 高斯语言场／索引
  - 三维分割与查询
  result_tables:
  - table1
results:
- id: table1
  label: Table 1
  asset: assets/results/cos3d-table1.png
  page: 7
  version: arXiv 2510.20238v1
  source_url: https://arxiv.org/pdf/2510.20238v1
  source_sha256: 4ef11ad250ca192135fcaa3a6965a60360eca9bec8e8bad983ab4c39780ea9b3
  clip_pdf_points:
  - 107
  - 378
  - 506
  - 485
  title: COS3D：主要实验结果
  setting: LeRF 的 Gaussian segmentation in 3D space，保留不同方法输出表示。
  metrics: mIoU／mAcc ↑
  reading: 区分三维高斯选择与渲染二维分割的评测方式。
---

# COS3D

本页按研究问题提取相关操作；模块图、输入输出、证据和主要结果表在上方展开查看。

## 研究问题

文本粗定位如何得到准确三维实例边界？

## 相关操作

协同字段同时保存实例与语言两种表示，两阶段训练中以实例到语言映射建立关联；推理时用语言响应自适应细化实例提示，再在实例字段中完成目标分割。

## 实验阅读

LeRF 的 Gaussian segmentation in 3D space，保留不同方法输出表示。 区分三维高斯选择与渲染二维分割的评测方式。 主表是整体系统结果，单一模块的贡献需结合原文消融。

## 原文依据

- [本次阅读的原文版本](https://arxiv.org/pdf/2510.20238v1)：方法部分；Figure 2（PDF 第 4 页）；实验 Table 1（PDF 第 7 页）。
- [正式发表来源](https://papers.neurips.cc/paper_files/paper/2025/hash/10a6bdcabbd5a3d36b760daa295f63c1-Abstract-Conference.html)。
- [官方实现](https://github.com/Runsong123/COS3D)：已核对官方实现目录：Grounding_3D.py、LICENSE.md、__pycache__、arguments、autoencoder、compute_lerf_iou_check.py。未独立运行或验证外部权重下载。
