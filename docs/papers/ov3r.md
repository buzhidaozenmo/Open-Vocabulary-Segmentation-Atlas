---
paper_id: ov3r
title: 'Ov3R: Open-Vocabulary Semantic 3D Reconstruction from RGB Videos'
short_name: Ov3R
authors:
- Gong, Ziren
- Li, Xiaohan
- Tosi, Fabio
- Han, Jiawei
- Mattoccia, Stefano
- Cai, Jianfei
- Poggi, Matteo
year: 2026
preprint_date: unknown
venue: CVPR
publication_status: published
primary_direction: multiview
modalities:
- point_cloud
- image
task_setting: open_vocabulary
task_types:
- semantic
techniques:
- semantic_alignment
datasets:
- Replica
paper_url: https://openaccess.thecvf.com/content/CVPR2026/papers/Gong_Ov3R_Open-Vocabulary_Semantic_3D_Reconstruction_from_RGB_Videos_CVPR_2026_paper.pdf
publication_url: https://openaccess.thecvf.com/content/CVPR2026/html/Gong_Ov3R_Open-Vocabulary_Semantic_3D_Reconstruction_from_RGB_Videos_CVPR_2026_paper.html
code_status: public
code_url: https://github.com/ZoranGong/Ov3R
code_details: 已核对官方实现目录：ATE_compute.py、app.py、clip3r、datasets_preprocess、evaluation、recon.py。未独立运行或验证外部权重下载。
content_status: index
checked_on: '2026-11-09'
module_checked_on: '2026-11-09'
summary: CLIP3R 从重叠视频片段预测局部点图并统一到全局；将 SAM 二维区域与点图中的三维区域匹配，融合 CLIP3R、DINO 与 3D-CLIP 描述符，再进行图文语义分类。
sources:
- url: https://openaccess.thecvf.com/content/CVPR2026/html/Gong_Ov3R_Open-Vocabulary_Semantic_3D_Reconstruction_from_RGB_Videos_CVPR_2026_paper.html
  locator: 正式发表来源：出版页面／作者项目的会议说明
- url: https://openaccess.thecvf.com/content/CVPR2026/papers/Gong_Ov3R_Open-Vocabulary_Semantic_3D_Reconstruction_from_RGB_Videos_CVPR_2026_paper.pdf
  locator: 方法部分；Figure 4（PDF 第 5 页）；实验 Table 3（PDF 第 7 页）
- url: https://github.com/ZoranGong/Ov3R
  locator: 官方 README、目录与开放范围；未独立运行
figures:
- id: fig4
  label: Figure 4
  asset: assets/figures/ov3r-fig4.png
  page: 5
  version: CVPR 2026 出版方正式版
  source_url: https://openaccess.thecvf.com/content/CVPR2026/papers/Gong_Ov3R_Open-Vocabulary_Semantic_3D_Reconstruction_from_RGB_Videos_CVPR_2026_paper.pdf
  source_sha256: 6be4af75a6698b4246b003dae4c878e1bf8dbc01b131b820e8300ff275ad3628
  clip_pdf_points:
  - 45
  - 45
  - 567
  - 243.698
methods:
- id: semantic-operation
  track: pointcloud
  problems:
  - projection
  - multiview
  - alignment
  title: 二维三维描述符融合
  question: RGB 视频重建的点怎样获得一致语义？
  operation: CLIP3R 从重叠视频片段预测局部点图并统一到全局；将 SAM 二维区域与点图中的三维区域匹配，融合 CLIP3R、DINO 与 3D-CLIP 描述符，再进行图文语义分类。
  input: RGB 视频、点图、二维区域和类别文本
  output: 二维三维融合区域描述符与类别
  stage: 模型训练及重建／查询推理
  supervision: 重建训练数据和二维语义特征教师
  origin: proposed
  origin_note: 本文设计的二维三维描述符融合流程；所用预训练模型、通用投影及基础算子沿用已有方法，不计作本文新提出。
  evidence:
  - url: https://openaccess.thecvf.com/content/CVPR2026/papers/Gong_Ov3R_Open-Vocabulary_Semantic_3D_Reconstruction_from_RGB_Videos_CVPR_2026_paper.pdf
    locator: 方法部分；Figure 4（PDF 第 5 页）；实验 Table 3（PDF 第 7 页）
  figure: fig4
  figure_guide: 沿 2D–3D OVS 中区域匹配、三路特征与 fused descriptor 阅读。
  depicted: true
  route:
  - 多视角二维语义
  - 二维三维描述符融合
  - 三维实例／点特征
  - 三维分割与查询
  result_tables:
  - table3
results:
- id: table3
  label: Table 3
  asset: assets/results/ov3r-table3.png
  page: 7
  version: CVPR 2026 出版方正式版
  source_url: https://openaccess.thecvf.com/content/CVPR2026/papers/Gong_Ov3R_Open-Vocabulary_Semantic_3D_Reconstruction_from_RGB_Videos_CVPR_2026_paper.pdf
  source_sha256: 6be4af75a6698b4246b003dae4c878e1bf8dbc01b131b820e8300ff275ad3628
  clip_pdf_points:
  - 55
  - 190
  - 299
  - 383
  title: Ov3R：主要实验结果
  setting: Replica；区分真值几何与模型重建几何上的评测。
  metrics: mIoU／mAcc ↑
  reading: 先核对是否使用真值三维重建，再比较语义分割。
---

# Ov3R

本页按研究问题提取相关操作；模块图、输入输出、证据和主要结果表在上方展开查看。

## 研究问题

RGB 视频重建的点怎样获得一致语义？

## 相关操作

CLIP3R 从重叠视频片段预测局部点图并统一到全局；将 SAM 二维区域与点图中的三维区域匹配，融合 CLIP3R、DINO 与 3D-CLIP 描述符，再进行图文语义分类。

## 实验阅读

Replica；区分真值几何与模型重建几何上的评测。 先核对是否使用真值三维重建，再比较语义分割。 主表是整体系统结果，单一模块的贡献需结合原文消融。

## 原文依据

- [本次阅读的原文版本](https://openaccess.thecvf.com/content/CVPR2026/papers/Gong_Ov3R_Open-Vocabulary_Semantic_3D_Reconstruction_from_RGB_Videos_CVPR_2026_paper.pdf)：方法部分；Figure 4（PDF 第 5 页）；实验 Table 3（PDF 第 7 页）。
- [正式发表来源](https://openaccess.thecvf.com/content/CVPR2026/html/Gong_Ov3R_Open-Vocabulary_Semantic_3D_Reconstruction_from_RGB_Videos_CVPR_2026_paper.html)。
- [官方实现](https://github.com/ZoranGong/Ov3R)：已核对官方实现目录：ATE_compute.py、app.py、clip3r、datasets_preprocess、evaluation、recon.py。未独立运行或验证外部权重下载。
