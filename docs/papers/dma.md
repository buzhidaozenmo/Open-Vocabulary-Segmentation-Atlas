---
paper_id: dma
title: Dense Multimodal Alignment for Open-Vocabulary 3D Scene Understanding
short_name: DMA
authors:
- Ruihuang, Li
- Zhengqiang, Zhang
- Chenhang, He
- Zhiyuan, Ma
- Vishal M., Patel
- Lei, Zhang
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
paper_url: https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/06612.pdf
publication_url: https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/6612_ECCV_2024_paper.php
code_status: public
code_url: https://github.com/lslrh/DMA
code_details: 已核对官方实现目录：config、dataset、distill.py、doc、evaluate.py、extract_text_feature.py。未独立运行或验证外部权重下载。
content_status: index
checked_on: '2026-11-09'
module_checked_on: '2026-11-09'
summary: 通过图像标签模型和 LVLM 生成完整类别标签与场景描述，并去除噪声；以图像为桥建立点—像素—文本稠密关联，同时双路径融合冻结 CLIP 特征与可学习掩码特征，再训练三维对齐网络。
sources:
- url: https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/6612_ECCV_2024_paper.php
  locator: 正式发表来源：出版页面／作者项目的会议说明
- url: https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/06612.pdf
  locator: 方法部分；Fig. 1（PDF 第 4 页）；实验 Table 1（PDF 第 10 页）
- url: https://github.com/lslrh/DMA
  locator: 官方 README、目录与开放范围；未独立运行
figures:
- id: fig1
  label: Fig. 1
  asset: assets/figures/dma-fig1.png
  page: 4
  version: ECCV 2024 出版方正式版
  source_url: https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/06612.pdf
  source_sha256: 7670094acda0cbb6d19576972afccbd1898f010f42a2e0d6854473c970fa991f
  clip_pdf_points:
  - 134
  - 110
  - 481
  - 277.627
methods:
- id: semantic-operation
  track: pointcloud
  problems:
  - projection
  - multiview
  - alignment
  title: 稠密点像素文本对齐
  question: 图文与几何怎样联合提供细粒度语义监督？
  operation: 通过图像标签模型和 LVLM 生成完整类别标签与场景描述，并去除噪声；以图像为桥建立点—像素—文本稠密关联，同时双路径融合冻结 CLIP 特征与可学习掩码特征，再训练三维对齐网络。
  input: 点云、多视图图像、标签／描述及掩码
  output: 稠密对齐的三维语义特征
  stage: 文本数据构建与多模态训练；查询推理
  supervision: 自动文本、二维区域及相机几何，不依赖人工目标三维语义标注
  origin: proposed
  origin_note: 本文设计的稠密点像素文本对齐流程；所用预训练模型、通用投影及基础算子沿用已有方法，不计作本文新提出。
  evidence:
  - url: https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/06612.pdf
    locator: 方法部分；Fig. 1（PDF 第 4 页）；实验 Table 1（PDF 第 10 页）
  figure: fig1
  figure_guide: 看 comprehensive language modality → dense point-pixel-text association 和双路径视觉融合。
  depicted: true
  route:
  - 多视角二维语义
  - 稠密点像素文本对齐
  - 三维实例／点特征
  - 三维分割与查询
  result_tables:
  - table1
results:
- id: table1
  label: Table 1
  asset: assets/results/dma-table1.png
  page: 10
  version: ECCV 2024 出版方正式版
  source_url: https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/06612.pdf
  source_sha256: 7670094acda0cbb6d19576972afccbd1898f010f42a2e0d6854473c970fa991f
  clip_pdf_points:
  - 120
  - 110
  - 302
  - 291
  title: DMA：主要实验结果
  setting: ScanNet 语义分割，保留 Foreground／Background 与训练条件。
  metrics: mIoU／mAcc ↑
  reading: 分别核对前景与背景类；自动标签净化的单独效果需查消融。
---

# DMA

本页按研究问题提取相关操作；模块图、输入输出、证据和主要结果表在上方展开查看。

## 研究问题

图文与几何怎样联合提供细粒度语义监督？

## 相关操作

通过图像标签模型和 LVLM 生成完整类别标签与场景描述，并去除噪声；以图像为桥建立点—像素—文本稠密关联，同时双路径融合冻结 CLIP 特征与可学习掩码特征，再训练三维对齐网络。

## 实验阅读

ScanNet 语义分割，保留 Foreground／Background 与训练条件。 分别核对前景与背景类；自动标签净化的单独效果需查消融。 主表是整体系统结果，单一模块的贡献需结合原文消融。

## 原文依据

- [本次阅读的原文版本](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/06612.pdf)：方法部分；Fig. 1（PDF 第 4 页）；实验 Table 1（PDF 第 10 页）。
- [正式发表来源](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/6612_ECCV_2024_paper.php)。
- [官方实现](https://github.com/lslrh/DMA)：已核对官方实现目录：config、dataset、distill.py、doc、evaluate.py、extract_text_feature.py。未独立运行或验证外部权重下载。
