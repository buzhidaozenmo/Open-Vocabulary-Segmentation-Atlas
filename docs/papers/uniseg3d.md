---
paper_id: uniseg3d
title: A Unified Framework for 3D Scene Understanding
short_name: UniSeg3D
authors:
- Xu, Wei
- Shi, Chunsheng
- Tu, Sifan
- Zhou, Xin
- Liang, Dingkang
- Bai, Xiang
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
paper_url: https://arxiv.org/pdf/2407.03263v2
publication_url: https://proceedings.neurips.cc/paper_files/paper/2024/hash/6d96950e6ce0b92e3d0fb2afa634e0f2-Abstract-Conference.html
code_status: public
code_url: https://github.com/dk-liang/UniSeg3D
code_details: 已核对官方实现目录：configs、content、data、open_clip、tools、uniseg3d。未独立运行或验证外部权重下载。
content_status: index
checked_on: '2026-11-09'
module_checked_on: '2026-11-09'
summary: 把语义、实例、交互、指代及开放词汇任务统一为查询表示与共享 Transformer 处理；通过任务间知识蒸馏和对比关联让区域掩码与语言查询共享信息，最后按任务输出。
sources:
- url: https://proceedings.neurips.cc/paper_files/paper/2024/hash/6d96950e6ce0b92e3d0fb2afa634e0f2-Abstract-Conference.html
  locator: 正式发表来源：出版页面／作者项目的会议说明
- url: https://arxiv.org/pdf/2407.03263v2
  locator: 方法部分；Figure 2（PDF 第 4 页）；实验 Table 2（PDF 第 8 页）
- url: https://github.com/dk-liang/UniSeg3D
  locator: 官方 README、目录与开放范围；未独立运行
figures:
- id: fig2
  label: Figure 2
  asset: assets/figures/uniseg3d-fig2.png
  page: 4
  version: arXiv 2407.03263v2
  source_url: https://arxiv.org/pdf/2407.03263v2
  source_sha256: c04e0022b38a922b714e699aebd2ed9817b8bb08f28692da2f75b3528b2bfeab
  clip_pdf_points:
  - 45
  - 45
  - 567
  - 238.941
methods:
- id: semantic-operation
  track: pointcloud
  problems:
  - alignment
  - regions
  - prompt
  title: 统一查询与跨任务对齐
  question: 不同点云分割任务如何共享语言与区域表示？
  operation: 把语义、实例、交互、指代及开放词汇任务统一为查询表示与共享 Transformer 处理；通过任务间知识蒸馏和对比关联让区域掩码与语言查询共享信息，最后按任务输出。
  input: 点云区域特征、任务查询与文本／交互提示
  output: 共享对象区域表示和各任务掩码
  stage: 多任务监督训练及任务条件推理
  supervision: 多任务三维掩码／语义和文本训练信号
  origin: proposed
  origin_note: 本文设计的统一查询与跨任务对齐流程；所用预训练模型、通用投影及基础算子沿用已有方法，不计作本文新提出。
  evidence:
  - url: https://arxiv.org/pdf/2407.03263v2
    locator: 方法部分；Figure 2（PDF 第 4 页）；实验 Table 2（PDF 第 8 页）
  figure: fig2
  figure_guide: 看六类输入查询进入同一 Transformer，跨任务蒸馏与对比的具体连接另见 Figure 3。
  depicted: true
  route:
  - 多视角二维语义
  - 统一查询与跨任务对齐
  - 三维实例／点特征
  - 三维分割与查询
  result_tables:
  - table2
results:
- id: table2
  label: Table 2
  asset: assets/results/uniseg3d-table2.png
  page: 8
  version: arXiv 2407.03263v2
  source_url: https://arxiv.org/pdf/2407.03263v2
  source_sha256: c04e0022b38a922b714e699aebd2ed9817b8bb08f28692da2f75b3528b2bfeab
  clip_pdf_points:
  - 107
  - 70
  - 506
  - 485
  title: UniSeg3D：主要实验结果
  setting: ScanNet20、ScanRefer、ScanNet200 的多任务对比，任务列分别读取。
  metrics: AP／mIoU／指代准确率等 ↑
  reading: 只比较相同任务列；统一模型使用多任务监督，不能标成免训练三维分割。
---

# UniSeg3D

本页按研究问题提取相关操作；模块图、输入输出、证据和主要结果表在上方展开查看。

## 研究问题

不同点云分割任务如何共享语言与区域表示？

## 相关操作

把语义、实例、交互、指代及开放词汇任务统一为查询表示与共享 Transformer 处理；通过任务间知识蒸馏和对比关联让区域掩码与语言查询共享信息，最后按任务输出。

## 实验阅读

ScanNet20、ScanRefer、ScanNet200 的多任务对比，任务列分别读取。 只比较相同任务列；统一模型使用多任务监督，不能标成免训练三维分割。 主表是整体系统结果，单一模块的贡献需结合原文消融。

## 原文依据

- [本次阅读的原文版本](https://arxiv.org/pdf/2407.03263v2)：方法部分；Figure 2（PDF 第 4 页）；实验 Table 2（PDF 第 8 页）。
- [正式发表来源](https://proceedings.neurips.cc/paper_files/paper/2024/hash/6d96950e6ce0b92e3d0fb2afa634e0f2-Abstract-Conference.html)。
- [官方实现](https://github.com/dk-liang/UniSeg3D)：已核对官方实现目录：configs、content、data、open_clip、tools、uniseg3d。未独立运行或验证外部权重下载。
