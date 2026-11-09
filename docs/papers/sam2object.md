---
paper_id: sam2object
title: 'SAM2Object: Consolidating View Consistency via SAM2 for Zero-Shot 3D Instance Segmentation'
short_name: SAM2Object
authors:
- Zhao, Jihuai
- Zhuo, Junbao
- Chen, Jiansheng
- Ma, Huimin
year: 2025
preprint_date: unknown
venue: CVPR
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
paper_url: https://openaccess.thecvf.com/content/CVPR2025/papers/Zhao_SAM2Object_Consolidating_View_Consistency_via_SAM2_for_Zero-Shot_3D_Instance_CVPR_2025_paper.pdf
publication_url: https://openaccess.thecvf.com/content/CVPR2025/html/Zhao_SAM2Object_Consolidating_View_Consistency_via_SAM2_for_Zero-Shot_3D_Instance_CVPR_2025_paper.html
code_status: public
code_url: https://github.com/jihuaizhaohd/SAM2Object
code_details: 已核对官方实现目录：graphclustering、segtrack。未独立运行或验证外部权重下载。
content_status: index
checked_on: '2026-11-09'
module_checked_on: '2026-11-09'
summary: 利用 SAM2 连续分割和跟踪得到视角间一致掩码，通过 mask consolidation 过滤低质量观察，再将保留掩码投影到超点并结合几何合并。本条只解释实例构建，语言分类不是该模块的新设计。
sources:
- url: https://openaccess.thecvf.com/content/CVPR2025/html/Zhao_SAM2Object_Consolidating_View_Consistency_via_SAM2_for_Zero-Shot_3D_Instance_CVPR_2025_paper.html
  locator: 正式发表来源：出版页面／作者项目的会议说明
- url: https://openaccess.thecvf.com/content/CVPR2025/papers/Zhao_SAM2Object_Consolidating_View_Consistency_via_SAM2_for_Zero-Shot_3D_Instance_CVPR_2025_paper.pdf
  locator: 方法部分；Figure 3（PDF 第 4 页）；实验 Table 1（PDF 第 6 页）
- url: https://github.com/jihuaizhaohd/SAM2Object
  locator: 官方 README、目录与开放范围；未独立运行
figures:
- id: fig3
  label: Figure 3
  asset: assets/figures/sam2object-fig3.png
  page: 4
  version: CVPR 2025 出版方正式版
  source_url: https://openaccess.thecvf.com/content/CVPR2025/papers/Zhao_SAM2Object_Consolidating_View_Consistency_via_SAM2_for_Zero-Shot_3D_Instance_CVPR_2025_paper.pdf
  source_sha256: 1e1ea67d83812bcaa93f6ea760e7dc56056f4b268eda56b337bdb126a55e240f
  clip_pdf_points:
  - 45
  - 45
  - 567
  - 346.841
methods:
- id: semantic-operation
  track: pointcloud
  problems:
  - multiview
  - reliability
  - regions
  title: 跨帧掩码巩固
  question: 二维掩码质量不同时如何避免等权污染三维合并？
  operation: 利用 SAM2 连续分割和跟踪得到视角间一致掩码，通过 mask consolidation 过滤低质量观察，再将保留掩码投影到超点并结合几何合并。本条只解释实例构建，语言分类不是该模块的新设计。
  input: 多视图 RGB-D、SAM2 跟踪掩码与超点
  output: 视角一致的三维实例提议
  stage: 跟踪、掩码筛选与三维合并推理
  supervision: 预训练 SAM2、相机几何与超点，无目标三维训练标注
  origin: proposed
  origin_note: 本文设计的跨帧掩码巩固流程；所用预训练模型、通用投影及基础算子沿用已有方法，不计作本文新提出。
  evidence:
  - url: https://openaccess.thecvf.com/content/CVPR2025/papers/Zhao_SAM2Object_Consolidating_View_Consistency_via_SAM2_for_Zero-Shot_3D_Instance_CVPR_2025_paper.pdf
    locator: 方法部分；Figure 3（PDF 第 4 页）；实验 Table 1（PDF 第 6 页）
  figure: fig3
  figure_guide: 看 mask consolidation 如何筛除低质掩码，再沿三维投影和区域合并阅读。
  depicted: true
  route:
  - 多视角二维语义
  - 跨帧掩码巩固
  - 三维实例／点特征
  - 三维分割与查询
  result_tables:
  - table1
results:
- id: table1
  label: Table 1
  asset: assets/results/sam2object-table1.png
  page: 6
  version: CVPR 2025 出版方正式版
  source_url: https://openaccess.thecvf.com/content/CVPR2025/papers/Zhao_SAM2Object_Consolidating_View_Consistency_via_SAM2_for_Zero-Shot_3D_Instance_CVPR_2025_paper.pdf
  source_sha256: 1e1ea67d83812bcaa93f6ea760e7dc56056f4b268eda56b337bdb126a55e240f
  clip_pdf_points:
  - 309
  - 132
  - 558
  - 373
  title: SAM2Object：主要实验结果
  setting: ScanNetV2 的类别无关实例分割。
  metrics: AP／AP50／AP25 ↑
  reading: 类别无关 AP 衡量实例几何，不包含文本语义分类；语义实例结果另见 Table 3。
---

# SAM2Object

本页按研究问题提取相关操作；模块图、输入输出、证据和主要结果表在上方展开查看。

## 研究问题

二维掩码质量不同时如何避免等权污染三维合并？

## 相关操作

利用 SAM2 连续分割和跟踪得到视角间一致掩码，通过 mask consolidation 过滤低质量观察，再将保留掩码投影到超点并结合几何合并。本条只解释实例构建，语言分类不是该模块的新设计。

## 实验阅读

ScanNetV2 的类别无关实例分割。 类别无关 AP 衡量实例几何，不包含文本语义分类；语义实例结果另见 Table 3。 主表是整体系统结果，单一模块的贡献需结合原文消融。

## 原文依据

- [本次阅读的原文版本](https://openaccess.thecvf.com/content/CVPR2025/papers/Zhao_SAM2Object_Consolidating_View_Consistency_via_SAM2_for_Zero-Shot_3D_Instance_CVPR_2025_paper.pdf)：方法部分；Figure 3（PDF 第 4 页）；实验 Table 1（PDF 第 6 页）。
- [正式发表来源](https://openaccess.thecvf.com/content/CVPR2025/html/Zhao_SAM2Object_Consolidating_View_Consistency_via_SAM2_for_Zero-Shot_3D_Instance_CVPR_2025_paper.html)。
- [官方实现](https://github.com/jihuaizhaohd/SAM2Object)：已核对官方实现目录：graphclustering、segtrack。未独立运行或验证外部权重下载。
