---
paper_id: openmask3d
title: 'OpenMask3D: Open-Vocabulary 3D Instance Segmentation'
short_name: OpenMask3D
authors: []
year: 2023
preprint_date: unknown
venue: NeurIPS
publication_status: published
primary_direction: 3d
modalities:
- point_cloud
- image
task_setting: open_vocabulary
task_types:
- instance
techniques:
- region_aggregation
- fusion
datasets:
- ScanNet
- Replica
paper_url: https://arxiv.org/abs/2306.13631
publication_url: https://proceedings.neurips.cc/paper_files/paper/2023/hash/d77b5482e38339a8068791d939126be2-Abstract-Conference.html
code_status: public
code_url: https://github.com/OpenMask3D/openmask3d
code_details: 公开特征提取、聚合与评测流程；依赖3D掩码模型、SAM等外部权重。
content_status: index
checked_on: '2026-11-09'
summary: 用类别无关三维实例掩码和多视角区域特征进行开放词汇实例分割。
sources:
- url: https://proceedings.neurips.cc/paper_files/paper/2023/hash/d77b5482e38339a8068791d939126be2-Abstract-Conference.html
  locator: 正式发表来源
- url: https://github.com/OpenMask3D/openmask3d
  locator: 官方 README / 公开目录；未运行
figures:
- id: fig2
  asset: assets/figures/openmask3d-fig2.png
  label: Figure 2
  page: 4
  version: arXiv 2306.13631v2
  source_url: https://arxiv.org/pdf/2306.13631v2
  clip_pdf_points:
  - 105
  - 45
  - 508
  - 239
  source_sha256: dad614ec86cb8f3778e61e30f0a0142085edc27ccdd318bfdf75b201427fa42c
- id: fig3
  asset: assets/figures/openmask3d-fig3.png
  label: Figure 3
  page: 5
  version: arXiv 2306.13631v2
  source_url: https://arxiv.org/pdf/2306.13631v2
  clip_pdf_points:
  - 105
  - 45
  - 508
  - 215
  source_sha256: dad614ec86cb8f3778e61e30f0a0142085edc27ccdd318bfdf75b201427fa42c
methods:
- id: maskfeatures
  track: pointcloud
  problems:
  - projection
  - multiview
  - regions
  title: 可见性选视图、多尺度裁切与掩码特征池化
  question: 实例掩码如何获得可靠的多视角语言特征？
  operation: 计算实例在每帧的可见性并选 top-k 视图；在各视图生成二维对象掩码，提取多尺度裁切；CLIP 编码后先跨裁切、再跨视图平均，得到每个三维实例的特征。
  input: 三维类别无关实例掩码、RGB-D 与位姿
  output: 每实例 CLIP 特征
  stage: 特征构建／推理
  supervision: 预训练三维掩码模型、SAM 与 CLIP；不是从零无监督
  origin: proposed
  origin_note: 本文组织的 Mask-Feature Computation 模块；所调用编码器和掩码模型沿用已有模型。
  origin_refs: []
  evidence:
  - url: https://arxiv.org/pdf/2306.13631v2
    locator: §2.2，Figure 3
  figure: fig3
  figure_guide: 独立模块图按 a→b→c→d 阅读：选视图、裁切、编码、平均。
  depicted: true
  route:
  - 二维区域特征
  - 可见性与跨视角融合
  - 实例特征
  - 文本相似度分类
module_checked_on: '2026-11-09'
---
# OpenMask3D

## 当前整理状态

已按研究关注点核查下列方法模块与配图；尚未完成全文样例笔记，不据此生成实验排名。

## 收录理由

用类别无关三维实例掩码和多视角区域特征进行开放词汇实例分割。

## 开源情况

【官方文档说明】公开特征提取、聚合与评测流程；依赖3D掩码模型、SAM等外部权重。 本轮没有安装或运行代码，没有独立验证权重下载。
