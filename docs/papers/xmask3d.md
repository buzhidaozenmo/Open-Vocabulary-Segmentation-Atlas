---
paper_id: xmask3d
title: 'XMask3D: Cross-modal Mask Reasoning for Open Vocabulary 3D Semantic Segmentation'
short_name: XMask3D
authors:
- Wang, Ziyi
- Wang, Yanbo
- Yu, Xumin
- Zhou, Jie
- Lu, Jiwen
year: 2024
preprint_date: unknown
venue: NeurIPS
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
paper_url: https://arxiv.org/pdf/2411.13243v1
publication_url: https://proceedings.neurips.cc/paper_files/paper/2024/hash/88f00376aedb947af123a7868fce3e58-Abstract-Conference.html
code_status: public
code_url: https://github.com/wangzy22/XMask3D
code_details: 已核对官方实现目录：config、data、dataset、fig、installation.md、models。未独立运行或验证外部权重下载。
content_status: index
checked_on: '2026-11-09'
module_checked_on: '2026-11-09'
summary: 把三维全局特征作为隐式条件送入预训练扩散去噪 UNet，产生具有几何感知的二维语义掩码；用这些掩码对齐区域级三维与图文表示，并融合互补二维三维掩码特征分类。
sources:
- url: https://proceedings.neurips.cc/paper_files/paper/2024/hash/88f00376aedb947af123a7868fce3e58-Abstract-Conference.html
  locator: 正式发表来源：出版页面／作者项目的会议说明
- url: https://arxiv.org/pdf/2411.13243v1
  locator: 方法部分；Figure 2（PDF 第 4 页）；实验 Table 1（PDF 第 7 页）
- url: https://github.com/wangzy22/XMask3D
  locator: 官方 README、目录与开放范围；未独立运行
figures:
- id: fig2
  label: Figure 2
  asset: assets/figures/xmask3d-fig2.png
  page: 4
  version: arXiv 2411.13243v1
  source_url: https://arxiv.org/pdf/2411.13243v1
  source_sha256: 545d92f0cd39c0138c0093f268fa13bf18ac051f3e229b2eaeb3e332e02e595b
  clip_pdf_points:
  - 45
  - 45
  - 567
  - 205.428
methods:
- id: semantic-operation
  track: pointcloud
  problems:
  - distillation
  - alignment
  - regions
  title: 掩码级跨模态推理
  question: 三维几何怎样反过来改善二维语义教师？
  operation: 把三维全局特征作为隐式条件送入预训练扩散去噪 UNet，产生具有几何感知的二维语义掩码；用这些掩码对齐区域级三维与图文表示，并融合互补二维三维掩码特征分类。
  input: 点云特征、图像、扩散模型和文本
  output: 区域级语言对齐三维特征与分割
  stage: 跨模态掩码训练及分割推理
  supervision: 已见类别三维监督及预训练扩散／图文模型
  origin: proposed
  origin_note: 本文设计的掩码级跨模态推理流程；所用预训练模型、通用投影及基础算子沿用已有方法，不计作本文新提出。
  evidence:
  - url: https://arxiv.org/pdf/2411.13243v1
    locator: 方法部分；Figure 2（PDF 第 4 页）；实验 Table 1（PDF 第 7 页）
  figure: fig2
  figure_guide: 看 3D global features 注入 2D denoising UNet，再由 mask-level alignment 返回三维分支。
  depicted: true
  route:
  - 多视角二维语义
  - 掩码级跨模态推理
  - 三维实例／点特征
  - 三维分割与查询
  result_tables:
  - table1
results:
- id: table1
  label: Table 1
  asset: assets/results/xmask3d-table1.png
  page: 7
  version: arXiv 2411.13243v1
  source_url: https://arxiv.org/pdf/2411.13243v1
  source_sha256: 545d92f0cd39c0138c0093f268fa13bf18ac051f3e229b2eaeb3e332e02e595b
  clip_pdf_points:
  - 107
  - 75
  - 506
  - 230
  title: XMask3D：主要实验结果
  setting: ScanNet 的 base／novel 类别划分，保留 B/N 分组及监督条件。
  metrics: hIoU／base mIoU／novel mIoU ↑
  reading: 已见类监督与未见类泛化分别看，不同 B/N 划分不是同一任务。
---

# XMask3D

本页按研究问题提取相关操作；模块图、输入输出、证据和主要结果表在上方展开查看。

## 研究问题

三维几何怎样反过来改善二维语义教师？

## 相关操作

把三维全局特征作为隐式条件送入预训练扩散去噪 UNet，产生具有几何感知的二维语义掩码；用这些掩码对齐区域级三维与图文表示，并融合互补二维三维掩码特征分类。

## 实验阅读

ScanNet 的 base／novel 类别划分，保留 B/N 分组及监督条件。 已见类监督与未见类泛化分别看，不同 B/N 划分不是同一任务。 主表是整体系统结果，单一模块的贡献需结合原文消融。

## 原文依据

- [本次阅读的原文版本](https://arxiv.org/pdf/2411.13243v1)：方法部分；Figure 2（PDF 第 4 页）；实验 Table 1（PDF 第 7 页）。
- [正式发表来源](https://proceedings.neurips.cc/paper_files/paper/2024/hash/88f00376aedb947af123a7868fce3e58-Abstract-Conference.html)。
- [官方实现](https://github.com/wangzy22/XMask3D)：已核对官方实现目录：config、data、dataset、fig、installation.md、models。未独立运行或验证外部权重下载。
