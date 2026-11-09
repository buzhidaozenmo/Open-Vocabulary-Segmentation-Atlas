---
paper_id: sai3d
title: 'SAI3D: Segment Any Instance in 3D Scenes'
short_name: SAI3D
authors:
- Yin, Yingda
- Liu, Yuzheng
- Xiao, Yang
- Cohen-Or, Daniel
- Huang, Jingwei
- Chen, Baoquan
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
- instance
techniques:
- semantic_alignment
datasets:
- ScanNet
paper_url: https://openaccess.thecvf.com/content/CVPR2024/papers/Yin_SAI3D_Segment_Any_Instance_in_3D_Scenes_CVPR_2024_paper.pdf
publication_url: https://openaccess.thecvf.com/content/CVPR2024/html/Yin_SAI3D_Segment_Any_Instance_in_3D_Scenes_CVPR_2024_paper.html
code_status: public
code_url: https://github.com/yd-yin/SAI3D
code_details: 已核对官方实现目录：Semantic-SAM、evaluation、helpers、linetimer.py、openmask3d、sai3d.py。未独立运行或验证外部权重下载。
content_status: index
checked_on: '2026-11-09'
module_checked_on: '2026-11-09'
summary: 将超点投影到各视角掩码，以共同可见且属于同一二维区域的程度建立超点亲和；在几何邻接图上用动态阈值层级区域生长逐步合并，语言分类阶段沿用 OpenMask3D。
sources:
- url: https://openaccess.thecvf.com/content/CVPR2024/html/Yin_SAI3D_Segment_Any_Instance_in_3D_Scenes_CVPR_2024_paper.html
  locator: 正式发表来源：出版页面／作者项目的会议说明
- url: https://openaccess.thecvf.com/content/CVPR2024/papers/Yin_SAI3D_Segment_Any_Instance_in_3D_Scenes_CVPR_2024_paper.pdf
  locator: 方法部分；Figure 3（PDF 第 4 页）；实验 Table 3（PDF 第 6 页）
- url: https://github.com/yd-yin/SAI3D
  locator: 官方 README、目录与开放范围；未独立运行
figures:
- id: fig3
  label: Figure 3
  asset: assets/figures/sai3d-fig3.png
  page: 4
  version: CVPR 2024 出版方正式版
  source_url: https://openaccess.thecvf.com/content/CVPR2024/papers/Yin_SAI3D_Segment_Any_Instance_in_3D_Scenes_CVPR_2024_paper.pdf
  source_sha256: 87764b429ed19ae7be2a1a0a405b2826afcbbb833cddb26165d538fffcf39b24
  clip_pdf_points:
  - 45
  - 260
  - 290
  - 451.258
methods:
- id: semantic-operation
  track: pointcloud
  problems:
  - projection
  - multiview
  - regions
  title: 多视角超点亲和
  question: 哪些三维超点应合并为同一实例？
  operation: 将超点投影到各视角掩码，以共同可见且属于同一二维区域的程度建立超点亲和；在几何邻接图上用动态阈值层级区域生长逐步合并，语言分类阶段沿用 OpenMask3D。
  input: 点云超点、多视图 SAM 掩码与相机几何
  output: 三维实例提议及后续语言分类输入
  stage: 免三维训练的投影合并推理
  supervision: SAM 掩码、超点几何与深度／位姿
  origin: proposed
  origin_note: 本文设计的多视角超点亲和流程；所用预训练模型、通用投影及基础算子沿用已有方法，不计作本文新提出。 其中 OpenMask3D 分类／Mask3D 提议的沿用关系在本条具体操作和监督中单独说明。
  evidence:
  - url: https://openaccess.thecvf.com/content/CVPR2024/papers/Yin_SAI3D_Segment_Any_Instance_in_3D_Scenes_CVPR_2024_paper.pdf
    locator: 方法部分；Figure 3（PDF 第 4 页）；实验 Table 3（PDF 第 6 页）
  figure: fig3
  figure_guide: 看 Figure 3 的可见超点投影和同掩码覆盖；层级合并阈值另见 Figure 4。
  depicted: true
  route:
  - 多视角二维语义
  - 多视角超点亲和
  - 三维实例／点特征
  - 三维分割与查询
  result_tables:
  - table3
  origin_refs:
  - url: https://arxiv.org/abs/2306.13631
    locator: 原文方法中引用的 OpenMask3D 语义分类流程
results:
- id: table3
  label: Table 3
  asset: assets/results/sai3d-table3.png
  page: 6
  version: CVPR 2024 出版方正式版
  source_url: https://openaccess.thecvf.com/content/CVPR2024/papers/Yin_SAI3D_Segment_Any_Instance_in_3D_Scenes_CVPR_2024_paper.pdf
  source_sha256: 87764b429ed19ae7be2a1a0a405b2826afcbbb833cddb26165d538fffcf39b24
  clip_pdf_points:
  - 305
  - 300
  - 549
  - 415
  title: SAI3D：主要实验结果
  setting: ScanNet200 语义实例分割；原表按监督掩码与开放词汇掩码分组。
  metrics: AP／AP50／AP25 ↑
  reading: 语言分类沿用 OpenMask3D，表中提升不等于新语言编码器效果。
---

# SAI3D

本页按研究问题提取相关操作；模块图、输入输出、证据和主要结果表在上方展开查看。

## 研究问题

哪些三维超点应合并为同一实例？

## 相关操作

将超点投影到各视角掩码，以共同可见且属于同一二维区域的程度建立超点亲和；在几何邻接图上用动态阈值层级区域生长逐步合并，语言分类阶段沿用 OpenMask3D。

## 实验阅读

ScanNet200 语义实例分割；原表按监督掩码与开放词汇掩码分组。 语言分类沿用 OpenMask3D，表中提升不等于新语言编码器效果。 主表是整体系统结果，单一模块的贡献需结合原文消融。

## 原文依据

- [本次阅读的原文版本](https://openaccess.thecvf.com/content/CVPR2024/papers/Yin_SAI3D_Segment_Any_Instance_in_3D_Scenes_CVPR_2024_paper.pdf)：方法部分；Figure 3（PDF 第 4 页）；实验 Table 3（PDF 第 6 页）。
- [正式发表来源](https://openaccess.thecvf.com/content/CVPR2024/html/Yin_SAI3D_Segment_Any_Instance_in_3D_Scenes_CVPR_2024_paper.html)。
- [官方实现](https://github.com/yd-yin/SAI3D)：已核对官方实现目录：Semantic-SAM、evaluation、helpers、linetimer.py、openmask3d、sai3d.py。未独立运行或验证外部权重下载。
