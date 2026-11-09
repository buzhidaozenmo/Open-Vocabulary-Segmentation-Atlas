---
paper_id: openins3d
title: 'OpenIns3D: Snap and Lookup for 3D Open-vocabulary Instance Segmentation'
short_name: OpenIns3D
authors:
- Zhening Huang
- Xiaoyang Wu
- Xi Chen
- Hengshuang Zhao
- Lei Zhu
- Joan Lasenby
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
- instance
techniques:
- semantic_alignment
datasets:
- ScanNet
- S3DIS
paper_url: https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/07914.pdf
publication_url: https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/7914_ECCV_2024_paper.php
code_status: public
code_url: https://github.com/Pointcept/OpenIns3D
code_details: 已核对官方实现目录：environment.yml、installation.md、openins3d、scripts、third_party、zero_shot_multi_vocs.py。未独立运行或验证外部权重下载。
content_status: index
checked_on: '2026-11-09'
module_checked_on: '2026-11-09'
summary: Mask 先产生三维类别无关提议，Snap 从点云渲染多个尺度的场景图并执行二维开放词汇识别；Lookup 使用 Mask2Pixel 投影对应，比较提议与检测区域的重叠，为三维实例分配语义。
sources:
- url: https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/7914_ECCV_2024_paper.php
  locator: 正式发表来源：出版页面／作者项目的会议说明
- url: https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/07914.pdf
  locator: 方法部分；Fig. 6（PDF 第 9 页）；实验 Table 2（PDF 第 11 页）
- url: https://github.com/Pointcept/OpenIns3D
  locator: 官方 README、目录与开放范围；未独立运行
figures:
- id: fig6
  label: Fig. 6
  asset: assets/figures/openins3d-fig6.png
  page: 9
  version: ECCV 2024 出版方正式版
  source_url: https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/07914.pdf
  source_sha256: f1674a0f3dbb3a4c08e01ee9b972135f00d63f4ba932aef09795cc59d4c477dc
  clip_pdf_points:
  - 303
  - 180
  - 485
  - 383.844
methods:
- id: semantic-operation
  track: pointcloud
  problems:
  - projection
  - multiview
  - regions
  title: 合成视角区域查找
  question: 只有点云输入怎样借助二维模型命名实例？
  operation: Mask 先产生三维类别无关提议，Snap 从点云渲染多个尺度的场景图并执行二维开放词汇识别；Lookup 使用 Mask2Pixel 投影对应，比较提议与检测区域的重叠，为三维实例分配语义。
  input: 点云、三维实例提议、合成视角与二维识别
  output: 带类别语义的三维实例
  stage: 提议网络训练；合成视角与查询推理
  supervision: 三维提议训练标注及预训练二维识别模型
  origin: proposed
  origin_note: 本文设计的合成视角区域查找流程；所用预训练模型、通用投影及基础算子沿用已有方法，不计作本文新提出。
  evidence:
  - url: https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/07914.pdf
    locator: 方法部分；Fig. 6（PDF 第 9 页）；实验 Table 2（PDF 第 11 页）
  figure: fig6
  figure_guide: 看 Mask2Pixel 指导的 Lookup：二维检测与三维提议投影的 IoU 对应。
  depicted: true
  route:
  - 多视角二维语义
  - 合成视角区域查找
  - 三维实例／点特征
  - 三维分割与查询
  result_tables:
  - table2
results:
- id: table2
  label: Table 2
  asset: assets/results/openins3d-table2.png
  page: 11
  version: ECCV 2024 出版方正式版
  source_url: https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/07914.pdf
  source_sha256: f1674a0f3dbb3a4c08e01ee9b972135f00d63f4ba932aef09795cc59d4c477dc
  clip_pdf_points:
  - 134
  - 114
  - 481
  - 348
  title: OpenIns3D：主要实验结果
  setting: S3DIS 与 ScanNetV2，基于原文 novel 类划分的实例分割。
  metrics: AP ↑
  reading: 仅 novel 类协议与全类别评测不能直接比较；合成图像不是额外传感器输入。
---

# OpenIns3D

本页按研究问题提取相关操作；模块图、输入输出、证据和主要结果表在上方展开查看。

## 研究问题

只有点云输入怎样借助二维模型命名实例？

## 相关操作

Mask 先产生三维类别无关提议，Snap 从点云渲染多个尺度的场景图并执行二维开放词汇识别；Lookup 使用 Mask2Pixel 投影对应，比较提议与检测区域的重叠，为三维实例分配语义。

## 实验阅读

S3DIS 与 ScanNetV2，基于原文 novel 类划分的实例分割。 仅 novel 类协议与全类别评测不能直接比较；合成图像不是额外传感器输入。 主表是整体系统结果，单一模块的贡献需结合原文消融。

## 原文依据

- [本次阅读的原文版本](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/07914.pdf)：方法部分；Fig. 6（PDF 第 9 页）；实验 Table 2（PDF 第 11 页）。
- [正式发表来源](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/7914_ECCV_2024_paper.php)。
- [官方实现](https://github.com/Pointcept/OpenIns3D)：已核对官方实现目录：environment.yml、installation.md、openins3d、scripts、third_party、zero_shot_multi_vocs.py。未独立运行或验证外部权重下载。
