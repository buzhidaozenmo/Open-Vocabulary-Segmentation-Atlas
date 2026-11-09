---
paper_id: ov3d
title: Open-Vocabulary 3D Semantic Segmentation with Foundation Models
short_name: OV3D
authors:
- Jiang, Li
- Shi, Shaoshuai
- Schiele, Bernt
year: 2024
preprint_date: unknown
venue: CVPR
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
paper_url: https://openaccess.thecvf.com/content/CVPR2024/papers/Jiang_Open-Vocabulary_3D_Semantic_Segmentation_with_Foundation_Models_CVPR_2024_paper.pdf
publication_url: https://openaccess.thecvf.com/content/CVPR2024/html/Jiang_Open-Vocabulary_3D_Semantic_Segmentation_with_Foundation_Models_CVPR_2024_paper.html
code_status: unconfirmed
code_url: ''
code_details: 未找到可核实的官方实现入口；保留论文与原文证据，不据此断言作者不会公开。
content_status: index
checked_on: '2026-11-09'
module_checked_on: '2026-11-09'
summary: LVLM 为图像生成带上下文的实体描述，视觉基础模型产生类别无关区域，将区域像素关联到 EntityText；再用多视图几何把像素—文本关系传给点云，通过点与实体文本对齐训练三维网络。
sources:
- url: https://openaccess.thecvf.com/content/CVPR2024/html/Jiang_Open-Vocabulary_3D_Semantic_Segmentation_with_Foundation_Models_CVPR_2024_paper.html
  locator: 正式发表来源：出版页面／作者项目的会议说明
- url: https://openaccess.thecvf.com/content/CVPR2024/papers/Jiang_Open-Vocabulary_3D_Semantic_Segmentation_with_Foundation_Models_CVPR_2024_paper.pdf
  locator: 方法部分；Figure 4（PDF 第 4 页）；实验 Table 1（PDF 第 6 页）
figures:
- id: fig4
  label: Figure 4
  asset: assets/figures/ov3d-fig4.png
  page: 4
  version: CVPR 2024 出版方正式版
  source_url: https://openaccess.thecvf.com/content/CVPR2024/papers/Jiang_Open-Vocabulary_3D_Semantic_Segmentation_with_Foundation_Models_CVPR_2024_paper.pdf
  source_sha256: 05f6a5d054b3db4b86c7cb8cbe07ac32d22a93d31984f2a56c42acfa72d1794f
  clip_pdf_points:
  - 305
  - 45
  - 550
  - 156.994
methods:
- id: semantic-operation
  track: pointcloud
  problems:
  - projection
  - multiview
  - alignment
  title: 像素实体文本关联
  question: 自由实体描述怎样监督三维点？
  operation: LVLM 为图像生成带上下文的实体描述，视觉基础模型产生类别无关区域，将区域像素关联到 EntityText；再用多视图几何把像素—文本关系传给点云，通过点与实体文本对齐训练三维网络。
  input: 多视角图像、点云、区域与实体文本
  output: 语言对齐的逐点语义特征
  stage: 关联构建与三维网络训练；文本分类推理
  supervision: LVLM 实体描述、二维区域及相机几何，不用目标三维语义标注
  origin: proposed
  origin_note: 本文设计的像素实体文本关联流程；所用预训练模型、通用投影及基础算子沿用已有方法，不计作本文新提出。
  evidence:
  - url: https://openaccess.thecvf.com/content/CVPR2024/papers/Jiang_Open-Vocabulary_3D_Semantic_Segmentation_with_Foundation_Models_CVPR_2024_paper.pdf
    locator: 方法部分；Figure 4（PDF 第 4 页）；实验 Table 1（PDF 第 6 页）
  figure: fig4
  figure_guide: 看图中输入图像区域、EntityText 与 pixel association 对应；三维投影在 Figure 2 总框架中。
  depicted: true
  route:
  - 多视角二维语义
  - 像素实体文本关联
  - 三维实例／点特征
  - 三维分割与查询
  result_tables:
  - table1
results:
- id: table1
  label: Table 1
  asset: assets/results/ov3d-table1.png
  page: 6
  version: CVPR 2024 出版方正式版
  source_url: https://openaccess.thecvf.com/content/CVPR2024/papers/Jiang_Open-Vocabulary_3D_Semantic_Segmentation_with_Foundation_Models_CVPR_2024_paper.pdf
  source_sha256: 05f6a5d054b3db4b86c7cb8cbe07ac32d22a93d31984f2a56c42acfa72d1794f
  clip_pdf_points:
  - 45
  - 45
  - 550
  - 273
  title: OV3D：主要实验结果
  setting: ScanNet 与 Matterport3D 的 annotation-free 语义分割。
  metrics: mIoU／mAcc ↑
  reading: 注意背景及复测标记，不能与 base／novel 有标注训练协议混排。
---

# OV3D

本页按研究问题提取相关操作；模块图、输入输出、证据和主要结果表在上方展开查看。

## 研究问题

自由实体描述怎样监督三维点？

## 相关操作

LVLM 为图像生成带上下文的实体描述，视觉基础模型产生类别无关区域，将区域像素关联到 EntityText；再用多视图几何把像素—文本关系传给点云，通过点与实体文本对齐训练三维网络。

## 实验阅读

ScanNet 与 Matterport3D 的 annotation-free 语义分割。 注意背景及复测标记，不能与 base／novel 有标注训练协议混排。 主表是整体系统结果，单一模块的贡献需结合原文消融。

## 原文依据

- [本次阅读的原文版本](https://openaccess.thecvf.com/content/CVPR2024/papers/Jiang_Open-Vocabulary_3D_Semantic_Segmentation_with_Foundation_Models_CVPR_2024_paper.pdf)：方法部分；Figure 4（PDF 第 4 页）；实验 Table 1（PDF 第 6 页）。
- [正式发表来源](https://openaccess.thecvf.com/content/CVPR2024/html/Jiang_Open-Vocabulary_3D_Semantic_Segmentation_with_Foundation_Models_CVPR_2024_paper.html)。
- 官方代码状态：尚未确认。
