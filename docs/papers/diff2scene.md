---
paper_id: diff2scene
title: Open-Vocabulary 3D Semantic Segmentation with Text-to-Image Diffusion Models
short_name: Diff2Scene
authors:
- Xiaoyu Zhu
- Hao Zhou
- Pengfei Xing
- Long Zhao
- Hao Xu
- Junwei Liang
- Alexander Hauptmann
- Ting Liu
- Andrew Gallagher
year: 2024
preprint_date: unknown
venue: ECCV
publication_status: published
primary_direction: 3d
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
- Matterport3D
- Replica
paper_url: https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/04252.pdf
publication_url: https://diff2scene.github.io/
code_status: unconfirmed
code_url: ''
code_details: 未找到可核实的官方实现入口；保留论文与原文证据，不据此断言作者不会公开。
content_status: index
checked_on: '2026-11-09'
module_checked_on: '2026-11-09'
summary: 二维分支用扩散模型产生具有语义嵌入的显著掩码；将掩码嵌入作为三维分支语义查询生成几何掩码，并对齐掩码级二维三维表示，结合显著性与几何线索训练点云模型。
sources:
- url: https://diff2scene.github.io/
  locator: 正式发表来源：出版页面／作者项目的会议说明
- url: https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/04252.pdf
  locator: 方法部分；Fig. 3（PDF 第 6 页）；实验 Table 1（PDF 第 10 页）
figures:
- id: fig3
  label: Fig. 3
  asset: assets/figures/diff2scene-fig3.png
  page: 6
  version: ECCV 2024 出版方正式版
  source_url: https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/04252.pdf
  source_sha256: de309c533ac79dd7744fbd7a01f17d53bfe7d39ae57f84e2b539732a70e93a20
  clip_pdf_points:
  - 134
  - 110
  - 481
  - 243.956
methods:
- id: semantic-operation
  track: pointcloud
  problems:
  - distillation
  - regions
  - alignment
  title: 扩散掩码级三维蒸馏
  question: 怎样把二维语义整体传到三维区域而非逐点硬匹配？
  operation: 二维分支用扩散模型产生具有语义嵌入的显著掩码；将掩码嵌入作为三维分支语义查询生成几何掩码，并对齐掩码级二维三维表示，结合显著性与几何线索训练点云模型。
  input: 多视图图像、扩散掩码嵌入与点云
  output: 语言对齐的三维几何掩码
  stage: 掩码级蒸馏训练与文本分割推理
  supervision: 冻结二维基础模型语义和几何，不依赖人工三维语义标注
  origin: proposed
  origin_note: 本文设计的扩散掩码级三维蒸馏流程；所用预训练模型、通用投影及基础算子沿用已有方法，不计作本文新提出。
  evidence:
  - url: https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/04252.pdf
    locator: 方法部分；Fig. 3（PDF 第 6 页）；实验 Table 1（PDF 第 10 页）
  figure: fig3
  figure_guide: 看二维 diffusion semantic masks → semantic queries → 三维 probabilistic masks。
  depicted: true
  route:
  - 多视角二维语义
  - 扩散掩码级三维蒸馏
  - 三维实例／点特征
  - 三维分割与查询
  result_tables:
  - table1
results:
- id: table1
  label: Table 1
  asset: assets/results/diff2scene-table1.png
  page: 10
  version: ECCV 2024 出版方正式版
  source_url: https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/04252.pdf
  source_sha256: de309c533ac79dd7744fbd7a01f17d53bfe7d39ae57f84e2b539732a70e93a20
  clip_pdf_points:
  - 134
  - 114
  - 481
  - 355
  title: Diff2Scene：主要实验结果
  setting: ScanNet、Matterport3D、ScanNet200 与 Replica，原表区分零样本及额外监督参照。
  metrics: mIoU ↑
  reading: 比较相同数据与类别协议；掩码蒸馏的单独贡献需看消融。
---

# Diff2Scene

本页按研究问题提取相关操作；模块图、输入输出、证据和主要结果表在上方展开查看。

## 研究问题

怎样把二维语义整体传到三维区域而非逐点硬匹配？

## 相关操作

二维分支用扩散模型产生具有语义嵌入的显著掩码；将掩码嵌入作为三维分支语义查询生成几何掩码，并对齐掩码级二维三维表示，结合显著性与几何线索训练点云模型。

## 实验阅读

ScanNet、Matterport3D、ScanNet200 与 Replica，原表区分零样本及额外监督参照。 比较相同数据与类别协议；掩码蒸馏的单独贡献需看消融。 主表是整体系统结果，单一模块的贡献需结合原文消融。

## 原文依据

- [本次阅读的原文版本](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/04252.pdf)：方法部分；Fig. 3（PDF 第 6 页）；实验 Table 1（PDF 第 10 页）。
- [正式发表来源](https://diff2scene.github.io/)。
- 官方代码状态：尚未确认。
