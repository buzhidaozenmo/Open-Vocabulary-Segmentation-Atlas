---
paper_id: openyolo3d
title: 'Open-YOLO 3D: Towards Fast and Accurate Open-Vocabulary 3D Instance Segmentation'
short_name: Open-YOLO 3D
authors:
- Mohamed El Amine Boudjoghra
- Angela Dai
- Jean Lahoud
- Hisham Cholakkal
- Rao Muhammad Anwer
- Salman Khan
- Fahad Shahbaz Khan
year: 2025
preprint_date: unknown
venue: ICLR
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
paper_url: https://arxiv.org/pdf/2406.02548v3
publication_url: https://github.com/aminebdj/OpenYOLO3D
code_status: public
code_url: https://github.com/aminebdj/OpenYOLO3D
code_details: 已核对官方实现目录：environment.yml、evaluate、models、pretrained、run_evaluation.py、scripts。未独立运行或验证外部权重下载。
content_status: index
checked_on: '2026-11-09'
module_checked_on: '2026-11-09'
summary: 先用 Mask3D 生成类别无关三维掩码，YOLO-World 为二维图像生成粗细粒度类别标签；依据实例可见性选 top-k 视角，统计掩码投影覆盖的类别提示分布，形成实例类别及置信度。
sources:
- url: https://github.com/aminebdj/OpenYOLO3D
  locator: 正式发表来源：出版页面／作者项目的会议说明
- url: https://arxiv.org/pdf/2406.02548v3
  locator: 方法部分；Figure 3（PDF 第 6 页）；实验 Table 1（PDF 第 7 页）
- url: https://github.com/aminebdj/OpenYOLO3D
  locator: 官方 README、目录与开放范围；未独立运行
figures:
- id: fig3
  label: Figure 3
  asset: assets/figures/openyolo3d-fig3.png
  page: 6
  version: arXiv 2406.02548v3
  source_url: https://arxiv.org/pdf/2406.02548v3
  source_sha256: 1fab46cb7f2e84f6bdbc5c461d3309b1500c0e3bb1835d6138a8799e6c8d9931
  clip_pdf_points:
  - 107
  - 45
  - 506
  - 165.768
methods:
- id: semantic-operation
  track: pointcloud
  problems:
  - projection
  - multiview
  - alignment
  title: 多视角提示分布
  question: 不提取密集 CLIP 特征如何分类三维提议？
  operation: 先用 Mask3D 生成类别无关三维掩码，YOLO-World 为二维图像生成粗细粒度类别标签；依据实例可见性选 top-k 视角，统计掩码投影覆盖的类别提示分布，形成实例类别及置信度。
  input: 三维提议、多视角检测标签与位姿
  output: 三维实例类别及置信度
  stage: 预训练模型推理与多视角汇总
  supervision: 预训练 Mask3D 与开放词汇二维检测器
  origin: proposed
  origin_note: 本文设计的多视角提示分布流程；所用预训练模型、通用投影及基础算子沿用已有方法，不计作本文新提出。 其中 OpenMask3D 分类／Mask3D 提议的沿用关系在本条具体操作和监督中单独说明。
  evidence:
  - url: https://arxiv.org/pdf/2406.02548v3
    locator: 方法部分；Figure 3（PDF 第 6 页）；实验 Table 1（PDF 第 7 页）
  figure: fig3
  figure_guide: 看 MVPDist 的 top-k label maps、投影实例及 label distribution。
  depicted: true
  route:
  - 多视角二维语义
  - 多视角提示分布
  - 三维实例／点特征
  - 三维分割与查询
  result_tables:
  - table1
  origin_refs:
  - url: https://arxiv.org/abs/2210.03105
    locator: 原文方法中引用的 Mask3D 类别无关实例提议模型
results:
- id: table1
  label: Table 1
  asset: assets/results/openyolo3d-table1.png
  page: 7
  version: arXiv 2406.02548v3
  source_url: https://arxiv.org/pdf/2406.02548v3
  source_sha256: 1fab46cb7f2e84f6bdbc5c461d3309b1500c0e3bb1835d6138a8799e6c8d9931
  clip_pdf_points:
  - 107
  - 67
  - 506
  - 282
  title: Open-YOLO 3D：主要实验结果
  setting: ScanNet200 验证集；Mask3D 在 ScanNet200 训练；保留推理时间。
  metrics: mAP／AP50／AP25 ↑；秒／场景 ↓
  reading: 类别词汇开放不意味着提议网络无三维监督，需同时看骨干与时延。
---

# Open-YOLO 3D

本页按研究问题提取相关操作；模块图、输入输出、证据和主要结果表在上方展开查看。

## 研究问题

不提取密集 CLIP 特征如何分类三维提议？

## 相关操作

先用 Mask3D 生成类别无关三维掩码，YOLO-World 为二维图像生成粗细粒度类别标签；依据实例可见性选 top-k 视角，统计掩码投影覆盖的类别提示分布，形成实例类别及置信度。

## 实验阅读

ScanNet200 验证集；Mask3D 在 ScanNet200 训练；保留推理时间。 类别词汇开放不意味着提议网络无三维监督，需同时看骨干与时延。 主表是整体系统结果，单一模块的贡献需结合原文消融。

## 原文依据

- [本次阅读的原文版本](https://arxiv.org/pdf/2406.02548v3)：方法部分；Figure 3（PDF 第 6 页）；实验 Table 1（PDF 第 7 页）。
- [正式发表来源](https://github.com/aminebdj/OpenYOLO3D)。
- [官方实现](https://github.com/aminebdj/OpenYOLO3D)：已核对官方实现目录：environment.yml、evaluate、models、pretrained、run_evaluation.py、scripts。未独立运行或验证外部权重下载。
