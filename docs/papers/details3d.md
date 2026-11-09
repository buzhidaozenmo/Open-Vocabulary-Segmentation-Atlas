---
paper_id: details3d
title: Details Matter for Indoor Open-vocabulary 3D Instance Segmentation
short_name: Details Matter
authors:
- Jung, Sanghun
- Zheng, Jingjing
- Zhang, Ke
- Qiao, Nan
- Chen, Albert Y. C.
- Xia, Lu
- Liu, Chi
- Sun, Yuyin
- Zeng, Xiao
- Huang, Hsiang-Wei
- Boots, Byron
- Sun, Min
- Kuo, Cheng-Hao
year: 2025
preprint_date: unknown
venue: ICCV
publication_status: published
primary_direction: 3d
modalities:
- point_cloud
- image
task_setting: open_vocabulary
task_types:
- instance
techniques:
- semantic_alignment
datasets:
- ScanNet
paper_url: https://openaccess.thecvf.com/content/ICCV2025/papers/Jung_Details_Matter_for_Indoor_Open-vocabulary_3D_Instance_Segmentation_ICCV_2025_paper.pdf
publication_url: https://openaccess.thecvf.com/content/ICCV2025/html/Jung_Details_Matter_for_Indoor_Open-vocabulary_3D_Instance_Segmentation_ICCV_2025_paper.html
code_status: unconfirmed
code_url: ''
code_details: 未找到可核实的官方实现入口；保留论文与原文证据，不据此断言作者不会公开。
content_status: index
checked_on: '2026-11-09'
module_checked_on: '2026-11-09'
summary: 先去除每帧二维预测重叠，再投影到三维，以逐帧 sIoU 匹配形成实例轨迹；随后迭代合并或移除重叠及局部提议。本文后续另用 Alpha-CLIP 和 SMS 过滤分类，本条关注提议阶段。
sources:
- url: https://openaccess.thecvf.com/content/ICCV2025/html/Jung_Details_Matter_for_Indoor_Open-vocabulary_3D_Instance_Segmentation_ICCV_2025_paper.html
  locator: 正式发表来源：出版页面／作者项目的会议说明
- url: https://openaccess.thecvf.com/content/ICCV2025/papers/Jung_Details_Matter_for_Indoor_Open-vocabulary_3D_Instance_Segmentation_ICCV_2025_paper.pdf
  locator: 方法部分；Figure 2（PDF 第 3 页）；实验 Table 1（PDF 第 6 页）
figures:
- id: fig2
  label: Figure 2
  asset: assets/figures/details3d-fig2.png
  page: 3
  version: ICCV 2025 出版方正式版
  source_url: https://openaccess.thecvf.com/content/ICCV2025/papers/Jung_Details_Matter_for_Indoor_Open-vocabulary_3D_Instance_Segmentation_ICCV_2025_paper.pdf
  source_sha256: f0ee727543e5b97e51add2244336e53c18e300c27cb8052098d028f034b4b34c
  clip_pdf_points:
  - 45
  - 45
  - 567
  - 175.234
methods:
- id: semantic-operation
  track: pointcloud
  problems:
  - projection
  - multiview
  - regions
  title: 跟踪聚合与实例净化
  question: 跨帧实例提议怎样减少重叠与碎片？
  operation: 先去除每帧二维预测重叠，再投影到三维，以逐帧 sIoU 匹配形成实例轨迹；随后迭代合并或移除重叠及局部提议。本文后续另用 Alpha-CLIP 和 SMS 过滤分类，本条关注提议阶段。
  input: 二维实例掩码、点云与相机投影
  output: 经轨迹聚合和净化的三维实例提议
  stage: 提议生成推理
  supervision: 预训练二维模型、三维提议网络与深度／位姿
  origin: proposed
  origin_note: 本文设计的跟踪聚合与实例净化流程；所用预训练模型、通用投影及基础算子沿用已有方法，不计作本文新提出。
  evidence:
  - url: https://openaccess.thecvf.com/content/ICCV2025/papers/Jung_Details_Matter_for_Indoor_Open-vocabulary_3D_Instance_Segmentation_ICCV_2025_paper.pdf
    locator: 方法部分；Figure 2（PDF 第 3 页）；实验 Table 1（PDF 第 6 页）
  figure: fig2
  figure_guide: 重点看去重、2D-to-3D lifting、proposal aggregation 和 iterative merging/removal。
  depicted: true
  route:
  - 多视角二维语义
  - 跟踪聚合与实例净化
  - 三维实例／点特征
  - 三维分割与查询
  result_tables:
  - table1
results:
- id: table1
  label: Table 1
  asset: assets/results/details3d-table1.png
  page: 6
  version: ICCV 2025 出版方正式版
  source_url: https://openaccess.thecvf.com/content/ICCV2025/papers/Jung_Details_Matter_for_Indoor_Open-vocabulary_3D_Instance_Segmentation_ICCV_2025_paper.pdf
  source_sha256: f0ee727543e5b97e51add2244336e53c18e300c27cb8052098d028f034b4b34c
  clip_pdf_points:
  - 55
  - 55
  - 558
  - 355
  title: Details Matter：主要实验结果
  setting: ScanNet200 验证集，保留 Top-1／Top-k 分类协议与三维提议来源。
  metrics: mAP／mAR 等 ↑
  reading: Top-1 与 Top-k 不是同一分类协议；主表包含提议和分类的共同效果。
---

# Details Matter

本页按研究问题提取相关操作；模块图、输入输出、证据和主要结果表在上方展开查看。

## 研究问题

跨帧实例提议怎样减少重叠与碎片？

## 相关操作

先去除每帧二维预测重叠，再投影到三维，以逐帧 sIoU 匹配形成实例轨迹；随后迭代合并或移除重叠及局部提议。本文后续另用 Alpha-CLIP 和 SMS 过滤分类，本条关注提议阶段。

## 实验阅读

ScanNet200 验证集，保留 Top-1／Top-k 分类协议与三维提议来源。 Top-1 与 Top-k 不是同一分类协议；主表包含提议和分类的共同效果。 主表是整体系统结果，单一模块的贡献需结合原文消融。

## 原文依据

- [本次阅读的原文版本](https://openaccess.thecvf.com/content/ICCV2025/papers/Jung_Details_Matter_for_Indoor_Open-vocabulary_3D_Instance_Segmentation_ICCV_2025_paper.pdf)：方法部分；Figure 2（PDF 第 3 页）；实验 Table 1（PDF 第 6 页）。
- [正式发表来源](https://openaccess.thecvf.com/content/ICCV2025/html/Jung_Details_Matter_for_Indoor_Open-vocabulary_3D_Instance_Segmentation_ICCV_2025_paper.html)。
- 官方代码状态：尚未确认。
