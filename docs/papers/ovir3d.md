---
paper_id: ovir3d
title: 'OVIR-3D: Open-Vocabulary 3D Instance Retrieval Without Training on 3D Data'
short_name: OVIR-3D
authors:
- Shiyang Lu
- Haonan Chang
- Eric Pu Jing
- Abdeslam Boularias
- Kostas Bekris
year: 2023
preprint_date: unknown
venue: CoRL
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
paper_url: https://proceedings.mlr.press/v229/lu23a/lu23a.pdf
publication_url: https://proceedings.mlr.press/v229/lu23a.html
code_status: public
code_url: https://github.com/shiyoung77/OVIR-3D
code_details: 已核对官方实现目录：Detic、KinectFusion-python、demo.sh、figures、ovir3d_corl_poster.pdf、ovir3d_iccvw_extended_abstract.pdf。未独立运行或验证外部权重下载。
content_status: index
checked_on: '2026-11-09'
module_checked_on: '2026-11-09'
summary: 将语言对齐二维区域提议反投影到点云，结合几何重叠和语义相似度匹配已有实例；增量融合区域及特征，并周期性合并、清理实例，查询时按文本与实例特征相似度排序。
sources:
- url: https://proceedings.mlr.press/v229/lu23a.html
  locator: 正式发表来源：出版页面／作者项目的会议说明
- url: https://proceedings.mlr.press/v229/lu23a/lu23a.pdf
  locator: 方法部分；Figure 2（PDF 第 4 页）；实验 Table 1（PDF 第 6 页）
- url: https://github.com/shiyoung77/OVIR-3D
  locator: 官方 README、目录与开放范围；未独立运行
figures:
- id: fig2
  label: Figure 2
  asset: assets/figures/ovir3d-fig2.png
  page: 4
  version: CoRL 2023 出版方正式版
  source_url: https://proceedings.mlr.press/v229/lu23a/lu23a.pdf
  source_sha256: 4d7ce4b9570be8afcaa3ac3a01697c93be634978f835c6e97a5ba14de8c14190
  clip_pdf_points:
  - 45
  - 45
  - 567
  - 276.702
methods:
- id: semantic-operation
  track: pointcloud
  problems:
  - projection
  - multiview
  - alignment
  title: 区域语义增量融合
  question: 二维区域如何在线合并为可检索三维实例？
  operation: 将语言对齐二维区域提议反投影到点云，结合几何重叠和语义相似度匹配已有实例；增量融合区域及特征，并周期性合并、清理实例，查询时按文本与实例特征相似度排序。
  input: RGB-D、相机位姿、二维区域与文本
  output: 带语言特征的三维实例检索集合
  stage: 增量融合及文本检索推理
  supervision: 预训练二维区域模型，无三维训练标注
  origin: proposed
  origin_note: 本文设计的区域语义增量融合流程；所用预训练模型、通用投影及基础算子沿用已有方法，不计作本文新提出。
  evidence:
  - url: https://proceedings.mlr.press/v229/lu23a/lu23a.pdf
    locator: 方法部分；Figure 2（PDF 第 4 页）；实验 Table 1（PDF 第 6 页）
  figure: fig2
  figure_guide: 从二维 region proposal、反投影、instance fusion 到 text query 排序阅读。
  depicted: true
  route:
  - 多视角二维语义
  - 区域语义增量融合
  - 三维实例／点特征
  - 三维分割与查询
  result_tables:
  - table1
results:
- id: table1
  label: Table 1
  asset: assets/results/ovir3d-table1.png
  page: 6
  version: CoRL 2023 出版方正式版
  source_url: https://proceedings.mlr.press/v229/lu23a/lu23a.pdf
  source_sha256: 4d7ce4b9570be8afcaa3ac3a01697c93be634978f835c6e97a5ba14de8c14190
  clip_pdf_points:
  - 72
  - 348
  - 540
  - 424
  title: OVIR-3D：主要实验结果
  setting: ScanNet200 与 YCB-Video；原表使用实例检索协议。
  metrics: 检索 mAP／相关指标 ↑
  reading: 检索 AP 与 ScanNet 几何实例分割 AP 定义不同，不能直接跨表比较。
---

# OVIR-3D

本页按研究问题提取相关操作；模块图、输入输出、证据和主要结果表在上方展开查看。

## 研究问题

二维区域如何在线合并为可检索三维实例？

## 相关操作

将语言对齐二维区域提议反投影到点云，结合几何重叠和语义相似度匹配已有实例；增量融合区域及特征，并周期性合并、清理实例，查询时按文本与实例特征相似度排序。

## 实验阅读

ScanNet200 与 YCB-Video；原表使用实例检索协议。 检索 AP 与 ScanNet 几何实例分割 AP 定义不同，不能直接跨表比较。 主表是整体系统结果，单一模块的贡献需结合原文消融。

## 原文依据

- [本次阅读的原文版本](https://proceedings.mlr.press/v229/lu23a/lu23a.pdf)：方法部分；Figure 2（PDF 第 4 页）；实验 Table 1（PDF 第 6 页）。
- [正式发表来源](https://proceedings.mlr.press/v229/lu23a.html)。
- [官方实现](https://github.com/shiyoung77/OVIR-3D)：已核对官方实现目录：Detic、KinectFusion-python、demo.sh、figures、ovir3d_corl_poster.pdf、ovir3d_iccvw_extended_abstract.pdf。未独立运行或验证外部权重下载。
