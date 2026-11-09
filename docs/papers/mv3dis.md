---
paper_id: mv3dis
title: 'MV3DIS: Multi-View Mask Matching via 3D Guides for Zero-Shot 3D Instance Segmentation'
short_name: MV3DIS
authors:
- Zhao, Yibo
- Zhang, Yigong
- Xie, Jin
year: 2026
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
paper_url: https://openaccess.thecvf.com/content/CVPR2026/papers/Zhao_MV3DIS_Multi-View_Mask_Matching_via_3D_Guides_for_Zero-Shot_3D_CVPR_2026_paper.pdf
publication_url: https://openaccess.thecvf.com/content/CVPR2026/html/Zhao_MV3DIS_Multi-View_Mask_Matching_via_3D_Guides_for_Zero-Shot_3D_CVPR_2026_paper.html
code_status: public
code_url: https://github.com/zybjn/MV3DIS
code_details: 已核对官方实现目录：evaluation、generate_2d_mask_conf.py、helpers、linetimer.py、mask_generator、meta_data。未独立运行或验证外部权重下载。
  当前仓库升级了二维掩码生成流程，其新增结果与原论文表格分开阅读。
content_status: index
checked_on: '2026-11-09'
module_checked_on: '2026-11-09'
summary: 投影时联合深度一致性与可见性权重，对接近遮挡阈值的可疑点降低贡献；在三维粗实例作为共同参照的多视图掩码对应中使用这些可靠性线索，减少跨对象错误合并。
sources:
- url: https://openaccess.thecvf.com/content/CVPR2026/html/Zhao_MV3DIS_Multi-View_Mask_Matching_via_3D_Guides_for_Zero-Shot_3D_CVPR_2026_paper.html
  locator: 正式发表来源：出版页面／作者项目的会议说明
- url: https://openaccess.thecvf.com/content/CVPR2026/papers/Zhao_MV3DIS_Multi-View_Mask_Matching_via_3D_Guides_for_Zero-Shot_3D_CVPR_2026_paper.pdf
  locator: 方法部分；Figure 3（PDF 第 4 页）；实验 Table 2（PDF 第 7 页）
- url: https://github.com/zybjn/MV3DIS
  locator: 官方 README、目录与开放范围；未独立运行
figures:
- id: fig3
  label: Figure 3
  asset: assets/figures/mv3dis-fig3.png
  page: 4
  version: CVPR 2026 出版方正式版
  source_url: https://openaccess.thecvf.com/content/CVPR2026/papers/Zhao_MV3DIS_Multi-View_Mask_Matching_via_3D_Guides_for_Zero-Shot_3D_CVPR_2026_paper.pdf
  source_sha256: f829cafddb843e439d314071b8b404b7156e956ec0abe882972525ec33ec5659
  clip_pdf_points:
  - 309
  - 325
  - 558
  - 460.354
methods:
- id: semantic-operation
  track: pointcloud
  problems:
  - projection
  - multiview
  - reliability
  title: 投影深度可靠性加权
  question: 遮挡边缘的点投影怎样减少错误掩码对应？
  operation: 投影时联合深度一致性与可见性权重，对接近遮挡阈值的可疑点降低贡献；在三维粗实例作为共同参照的多视图掩码对应中使用这些可靠性线索，减少跨对象错误合并。
  input: 三维点、投影深度、观测深度和二维掩码
  output: 加权的三维—二维对应与实例
  stage: 粗分割、掩码匹配和细化推理
  supervision: 预训练二维分割模型、三维超点和相机几何
  origin: proposed
  origin_note: 本文设计的投影深度可靠性加权流程；所用预训练模型、通用投影及基础算子沿用已有方法，不计作本文新提出。
  evidence:
  - url: https://openaccess.thecvf.com/content/CVPR2026/papers/Zhao_MV3DIS_Multi-View_Mask_Matching_via_3D_Guides_for_Zero-Shot_3D_CVPR_2026_paper.pdf
    locator: 方法部分；Figure 3（PDF 第 4 页）；实验 Table 2（PDF 第 7 页）
  figure: fig3
  figure_guide: 看 Figure 3 深度阈值附近遮挡点的权重与可见性；整体匹配流程见 Figure 2。
  depicted: true
  route:
  - 多视角二维语义
  - 投影深度可靠性加权
  - 三维实例／点特征
  - 三维分割与查询
  result_tables:
  - table2
results:
- id: table2
  label: Table 2
  asset: assets/results/mv3dis-table2.png
  page: 7
  version: CVPR 2026 出版方正式版
  source_url: https://openaccess.thecvf.com/content/CVPR2026/papers/Zhao_MV3DIS_Multi-View_Mask_Matching_via_3D_Guides_for_Zero-Shot_3D_CVPR_2026_paper.pdf
  source_sha256: f829cafddb843e439d314071b8b404b7156e956ec0abe882972525ec33ec5659
  clip_pdf_points:
  - 55
  - 55
  - 299
  - 290
  title: MV3DIS：主要实验结果
  setting: ScanNet200 的类别无关三维实例分割。
  metrics: AP／AP50／AP25 ↑
  reading: 主表只衡量实例掩码；官方仓库有升级二维掩码的结果，不与论文原表混写。
---

# MV3DIS

本页按研究问题提取相关操作；模块图、输入输出、证据和主要结果表在上方展开查看。

## 研究问题

遮挡边缘的点投影怎样减少错误掩码对应？

## 相关操作

投影时联合深度一致性与可见性权重，对接近遮挡阈值的可疑点降低贡献；在三维粗实例作为共同参照的多视图掩码对应中使用这些可靠性线索，减少跨对象错误合并。

## 实验阅读

ScanNet200 的类别无关三维实例分割。 主表只衡量实例掩码；官方仓库有升级二维掩码的结果，不与论文原表混写。 主表是整体系统结果，单一模块的贡献需结合原文消融。

## 原文依据

- [本次阅读的原文版本](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhao_MV3DIS_Multi-View_Mask_Matching_via_3D_Guides_for_Zero-Shot_3D_CVPR_2026_paper.pdf)：方法部分；Figure 3（PDF 第 4 页）；实验 Table 2（PDF 第 7 页）。
- [正式发表来源](https://openaccess.thecvf.com/content/CVPR2026/html/Zhao_MV3DIS_Multi-View_Mask_Matching_via_3D_Guides_for_Zero-Shot_3D_CVPR_2026_paper.html)。
- [官方实现](https://github.com/zybjn/MV3DIS)：已核对官方实现目录：evaluation、generate_2d_mask_conf.py、helpers、linetimer.py、mask_generator、meta_data。未独立运行或验证外部权重下载。 当前仓库升级了二维掩码生成流程，其新增结果与原论文表格分开阅读。
