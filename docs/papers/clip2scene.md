---
paper_id: clip2scene
title: 'CLIP2Scene: Towards Label-Efficient 3D Scene Understanding by CLIP'
short_name: CLIP2Scene
authors:
- Chen, Runnan
- Liu, Youquan
- Kong, Lingdong
- Zhu, Xinge
- Ma, Yuexin
- Li, Yikang
- Hou, Yuenan
- Qiao, Yu
- Wang, Wenping
year: 2023
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
- nuScenes
paper_url: https://openaccess.thecvf.com/content/CVPR2023/papers/Chen_CLIP2Scene_Towards_Label-Efficient_3D_Scene_Understanding_by_CLIP_CVPR_2023_paper.pdf
publication_url: https://openaccess.thecvf.com/content/CVPR2023/html/Chen_CLIP2Scene_Towards_Label-Efficient_3D_Scene_Understanding_by_CLIP_CVPR_2023_paper.html
code_status: public
code_url: https://github.com/runnanchen/CLIP2Scene
code_details: 已核对官方实现目录：config、downstream.py、downstream、evaluate.py、model、pretrain.py。未独立运行或验证外部权重下载。
content_status: index
checked_on: '2026-11-09'
module_checked_on: '2026-11-09'
summary: 用 CLIP 文本语义决定点之间的正负关系，训练语义驱动跨模态对比；同时约束时间相邻点云特征及其投影图像特征一致，让点云网络继承二维语言知识。
sources:
- url: https://openaccess.thecvf.com/content/CVPR2023/html/Chen_CLIP2Scene_Towards_Label-Efficient_3D_Scene_Understanding_by_CLIP_CVPR_2023_paper.html
  locator: 正式发表来源：出版页面／作者项目的会议说明
- url: https://openaccess.thecvf.com/content/CVPR2023/papers/Chen_CLIP2Scene_Towards_Label-Efficient_3D_Scene_Understanding_by_CLIP_CVPR_2023_paper.pdf
  locator: 方法部分；Figure 2（PDF 第 3 页）；实验 Table 2（PDF 第 6 页）
- url: https://github.com/runnanchen/CLIP2Scene
  locator: 官方 README、目录与开放范围；未独立运行
figures:
- id: fig2
  label: Figure 2
  asset: assets/figures/clip2scene-fig2.png
  page: 3
  version: CVPR 2023 出版方正式版
  source_url: https://openaccess.thecvf.com/content/CVPR2023/papers/Chen_CLIP2Scene_Towards_Label-Efficient_3D_Scene_Understanding_by_CLIP_CVPR_2023_paper.pdf
  source_sha256: 3d7b4af1057af5fac428bb99dab74c0924770d844eb3f972591b23ab33f17dee
  clip_pdf_points:
  - 45
  - 45
  - 567
  - 299.904
methods:
- id: semantic-operation
  track: pointcloud
  problems:
  - projection
  - distillation
  - alignment
  title: 语义与时空对比
  question: 二维文本知识怎样约束点云对比样本？
  operation: 用 CLIP 文本语义决定点之间的正负关系，训练语义驱动跨模态对比；同时约束时间相邻点云特征及其投影图像特征一致，让点云网络继承二维语言知识。
  input: 点云、关联图像、CLIP 像素文本语义
  output: 文本对齐的点云网络特征
  stage: 跨模态对比预训练与零样本推理
  supervision: 二维预训练 CLIP、时空对应，无三维类别预训练标注
  origin: proposed
  origin_note: 本文设计的语义与时空对比流程；所用预训练模型、通用投影及基础算子沿用已有方法，不计作本文新提出。
  evidence:
  - url: https://openaccess.thecvf.com/content/CVPR2023/papers/Chen_CLIP2Scene_Towards_Label-Efficient_3D_Scene_Understanding_by_CLIP_CVPR_2023_paper.pdf
    locator: 方法部分；Figure 2（PDF 第 3 页）；实验 Table 2（PDF 第 6 页）
  figure: fig2
  figure_guide: 看 Semantic-driven Contrastive Learning 与 Spatial-temporal Consistency 两条监督路径。
  depicted: true
  route:
  - 多视角二维语义
  - 语义与时空对比
  - 三维实例／点特征
  - 三维分割与查询
  result_tables:
  - table2
results:
- id: table2
  label: Table 2
  asset: assets/results/clip2scene-table2.png
  page: 6
  version: CVPR 2023 出版方正式版
  source_url: https://openaccess.thecvf.com/content/CVPR2023/papers/Chen_CLIP2Scene_Towards_Label-Efficient_3D_Scene_Understanding_by_CLIP_CVPR_2023_paper.pdf
  source_sha256: 3d7b4af1057af5fac428bb99dab74c0924770d844eb3f972591b23ab33f17dee
  clip_pdf_points:
  - 45
  - 191
  - 290
  - 285
  title: CLIP2Scene：主要实验结果
  setting: nuScenes、ScanNet 的 annotation-free 语义分割。
  metrics: mIoU ↑
  reading: 本表不含后续用 1%／100% 人工标签微调的成绩。
---

# CLIP2Scene

本页按研究问题提取相关操作；模块图、输入输出、证据和主要结果表在上方展开查看。

## 研究问题

二维文本知识怎样约束点云对比样本？

## 相关操作

用 CLIP 文本语义决定点之间的正负关系，训练语义驱动跨模态对比；同时约束时间相邻点云特征及其投影图像特征一致，让点云网络继承二维语言知识。

## 实验阅读

nuScenes、ScanNet 的 annotation-free 语义分割。 本表不含后续用 1%／100% 人工标签微调的成绩。 主表是整体系统结果，单一模块的贡献需结合原文消融。

## 原文依据

- [本次阅读的原文版本](https://openaccess.thecvf.com/content/CVPR2023/papers/Chen_CLIP2Scene_Towards_Label-Efficient_3D_Scene_Understanding_by_CLIP_CVPR_2023_paper.pdf)：方法部分；Figure 2（PDF 第 3 页）；实验 Table 2（PDF 第 6 页）。
- [正式发表来源](https://openaccess.thecvf.com/content/CVPR2023/html/Chen_CLIP2Scene_Towards_Label-Efficient_3D_Scene_Understanding_by_CLIP_CVPR_2023_paper.html)。
- [官方实现](https://github.com/runnanchen/CLIP2Scene)：已核对官方实现目录：config、downstream.py、downstream、evaluate.py、model、pretrain.py。未独立运行或验证外部权重下载。
