---
paper_id: ovimap
title: 'OVI-MAP: Open-Vocabulary Instance-Semantic Mapping'
short_name: OVI-MAP
authors:
- Deng, Zilong
- Tombari, Federico
- Pollefeys, Marc
- Wald, Johanna
- Barath, Daniel
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
- instance
techniques:
- semantic_alignment
datasets:
- Replica
- ScanNet
paper_url: https://openaccess.thecvf.com/content/CVPR2026/papers/Deng_OVI-MAP_Open-Vocabulary_Instance-Semantic_Mapping_CVPR_2026_paper.pdf
publication_url: https://openaccess.thecvf.com/content/CVPR2026/html/Deng_OVI-MAP_Open-Vocabulary_Instance-Semantic_Mapping_CVPR_2026_paper.html
code_status: public
code_url: https://github.com/OVI-MAP/OVI-MAP
code_details: 已核对官方仓库实际实现目录：LICENSE.txt、cover.png、cover2.png、docker、envs、mapping_ros_ws。运行及外部权重可用性未独立复现。
content_status: index
checked_on: '2026-11-09'
module_checked_on: '2026-11-09'
summary: 先由每帧实体掩码和深度几何细化结果增量融合类别无关实例地图；随后按对象中心的视角覆盖选择少量关键帧提取语言特征，将语义赋予已建立的三维实例，而非逐像素持续融合语言。
sources:
- url: https://openaccess.thecvf.com/content/CVPR2026/html/Deng_OVI-MAP_Open-Vocabulary_Instance-Semantic_Mapping_CVPR_2026_paper.html
  locator: 正式发表页面及作者信息
- url: https://openaccess.thecvf.com/content/CVPR2026/papers/Deng_OVI-MAP_Open-Vocabulary_Instance-Semantic_Mapping_CVPR_2026_paper.pdf
  locator: 方法部分；Figure 2（PDF 第 3 页）；实验 Table 3（PDF 第 6 页）
- url: https://github.com/OVI-MAP/OVI-MAP
  locator: 官方 README 与实际代码目录；不表示已运行
figures:
- id: figure2
  label: Figure 2
  asset: assets/figures/ovimap-figure2.png
  page: 3
  version: CVPR 2026 出版方正式版
  source_url: https://openaccess.thecvf.com/content/CVPR2026/papers/Deng_OVI-MAP_Open-Vocabulary_Instance-Semantic_Mapping_CVPR_2026_paper.pdf
  source_sha256: 52622c8aae5c864ed093f802af5cec936058c13f2910f7740015f08c6280bf58
  clip_pdf_points:
  - 55
  - 50
  - 558
  - 366.89410400390625
methods:
- id: semantic-operation
  track: pointcloud
  problems:
  - multiview
  - projection
  - efficiency
  title: 投影与视角选择
  question: 如何减少重复视角的语义计算并保持实例身份？
  operation: 先由每帧实体掩码和深度几何细化结果增量融合类别无关实例地图；随后按对象中心的视角覆盖选择少量关键帧提取语言特征，将语义赋予已建立的三维实例，而非逐像素持续融合语言。
  input: RGB-D 流、相机位姿、实体掩码
  output: 带语言特征的增量三维实例地图
  stage: 建图及查询推理
  supervision: 预训练二维模型；深度和相机几何，不要求目标场景三维语义训练标注
  origin: proposed
  origin_note: 本文设计的投影与视角选择流程；其预训练基础模型与通用组件沿用已有方法，不计作本文新提出。
  origin_refs:
  - url: https://openaccess.thecvf.com/content/CVPR2026/papers/Deng_OVI-MAP_Open-Vocabulary_Instance-Semantic_Mapping_CVPR_2026_paper.pdf
    locator: 方法部分列明的基础模型及其参考文献
  evidence:
  - url: https://openaccess.thecvf.com/content/CVPR2026/papers/Deng_OVI-MAP_Open-Vocabulary_Instance-Semantic_Mapping_CVPR_2026_paper.pdf
    locator: 方法部分；Figure 2（PDF 第 3 页）；实验 Table 3（PDF 第 6 页）
  figure: figure2
  figure_guide: 看 A 的几何细化掩码如何进入 B 的实例地图；再沿 C 的对象中心视角覆盖选择到 D 的语义特征抽取，注意几何建图与语义计算的分离。
  depicted: true
  route:
  - RGB-D 与二维实体
  - 投影与视角选择
  - 三维实例语言特征
  - 实例语义查询
  result_tables:
  - table3
results:
- id: table3
  label: Table 3
  asset: assets/results/ovimap-table3.png
  page: 6
  version: CVPR 2026 出版方正式版
  source_url: https://openaccess.thecvf.com/content/CVPR2026/papers/Deng_OVI-MAP_Open-Vocabulary_Instance-Semantic_Mapping_CVPR_2026_paper.pdf
  source_sha256: 52622c8aae5c864ed093f802af5cec936058c13f2910f7740015f08c6280bf58
  clip_pdf_points:
  - 55
  - 394
  - 299
  - 650
  title: OVI-MAP：主要实验结果
  setting: Replica 与 ScanNet；保留 online、30 FPS 与离线参照的不同设置。
  metrics: mIoU／AP 等 ↑，按原表列
  reading: 同为在线条件下比较；30 FPS 行使用不同二维实例模型，不能忽略这一差异。
---

# OVI-MAP

本页按研究问题提取相关操作；模块原图、具体输入输出、来源与主要实验结果在上方展开查看。

## 研究问题

如何减少重复视角的语义计算并保持实例身份？

## 相关操作

先由每帧实体掩码和深度几何细化结果增量融合类别无关实例地图；随后按对象中心的视角覆盖选择少量关键帧提取语言特征，将语义赋予已建立的三维实例，而非逐像素持续融合语言。

## 实验阅读

Replica 与 ScanNet；保留 online、30 FPS 与离线参照的不同设置。 同为在线条件下比较；30 FPS 行使用不同二维实例模型，不能忽略这一差异。 主要结果是整套方法的效果，不能单凭该表归因到一个模块。

## 原文依据

- [出版方原文](https://openaccess.thecvf.com/content/CVPR2026/papers/Deng_OVI-MAP_Open-Vocabulary_Instance-Semantic_Mapping_CVPR_2026_paper.pdf)：方法部分；Figure 2（PDF 第 3 页）；实验 Table 3（PDF 第 6 页）。
- [官方实现](https://github.com/OVI-MAP/OVI-MAP)：已检查公开目录，未独立运行训练或评测。
