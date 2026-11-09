---
paper_id: mmovseg
title: 'MM-OVSeg: Multimodal Optical-SAR Fusion for Open-Vocabulary Segmentation in Remote Sensing'
short_name: MM-OVSeg
authors:
- Wei, Yimin
- Xiao, Aoran
- Chen, Hongruixuan
- Xia, Junshi
- Yokoya, Naoto
year: 2026
preprint_date: unknown
venue: CVPR
publication_status: published
primary_direction: remote
modalities:
- image
- sar
task_setting: open_vocabulary
task_types:
- semantic
techniques:
- semantic_alignment
datasets: []
paper_url: https://openaccess.thecvf.com/content/CVPR2026/papers/Wei_MM-OVSeg_Multimodal_Optical-SAR_Fusion_for_Open-Vocabulary_Segmentation_in_Remote_Sensing_CVPR_2026_paper.pdf
publication_url: https://openaccess.thecvf.com/content/CVPR2026/html/Wei_MM-OVSeg_Multimodal_Optical-SAR_Fusion_for_Open-Vocabulary_Segmentation_in_Remote_Sensing_CVPR_2026_paper.html
code_status: public
code_url: https://github.com/Jimmyxichen/MM-OVSeg
code_details: 已核对官方仓库实际实现目录：configs、datasets、dinov3.zip、mmov_seg.zip、requirements.txt、testMMOVSeg.sh。运行及外部权重可用性未独立复现。
content_status: index
checked_on: '2026-11-09'
module_checked_on: '2026-11-09'
summary: 先用配准光学—SAR 图像对训练 SAR DINO 编码器，使其特征接近冻结 RGB DINO；再用双编码融合模块整合 RGB、SAR 和 CLIP 的稠密特征，与类别文本对齐产生开放词汇分割。
sources:
- url: https://openaccess.thecvf.com/content/CVPR2026/html/Wei_MM-OVSeg_Multimodal_Optical-SAR_Fusion_for_Open-Vocabulary_Segmentation_in_Remote_Sensing_CVPR_2026_paper.html
  locator: 正式发表页面及作者信息
- url: https://openaccess.thecvf.com/content/CVPR2026/papers/Wei_MM-OVSeg_Multimodal_Optical-SAR_Fusion_for_Open-Vocabulary_Segmentation_in_Remote_Sensing_CVPR_2026_paper.pdf
  locator: 方法部分；Figure 2（PDF 第 3 页）；实验 Table 2（PDF 第 6 页）
- url: https://github.com/Jimmyxichen/MM-OVSeg
  locator: 官方 README 与实际代码目录；不表示已运行
figures:
- id: figure2
  label: Figure 2
  asset: assets/figures/mmovseg-figure2.png
  page: 3
  version: CVPR 2026 出版方正式版
  source_url: https://openaccess.thecvf.com/content/CVPR2026/papers/Wei_MM-OVSeg_Multimodal_Optical-SAR_Fusion_for_Open-Vocabulary_Segmentation_in_Remote_Sensing_CVPR_2026_paper.pdf
  source_sha256: b9b7b2a52f3b0c009377c898085c07fbc18e18f00357d549f3d71c24821494d7
  clip_pdf_points:
  - 55
  - 50
  - 558
  - 357.21197509765625
methods:
- id: semantic-operation
  track: vocabulary
  problems:
  - alignment
  - reliability
  title: 跨模态语义对齐
  question: SAR 的结构信息怎样进入语言对齐空间？
  operation: 先用配准光学—SAR 图像对训练 SAR DINO 编码器，使其特征接近冻结 RGB DINO；再用双编码融合模块整合 RGB、SAR 和 CLIP 的稠密特征，与类别文本对齐产生开放词汇分割。
  input: 配准光学图像、SAR 图像、类别文本
  output: 多传感器像素类别图
  stage: 两阶段训练及推理
  supervision: 跨传感器配对图像；后续分割训练标注
  origin: proposed
  origin_note: 本文设计的跨模态语义对齐流程；其预训练基础模型与通用组件沿用已有方法，不计作本文新提出。
  origin_refs:
  - url: https://openaccess.thecvf.com/content/CVPR2026/papers/Wei_MM-OVSeg_Multimodal_Optical-SAR_Fusion_for_Open-Vocabulary_Segmentation_in_Remote_Sensing_CVPR_2026_paper.pdf
    locator: 方法部分列明的基础模型及其参考文献
  evidence:
  - url: https://openaccess.thecvf.com/content/CVPR2026/papers/Wei_MM-OVSeg_Multimodal_Optical-SAR_Fusion_for_Open-Vocabulary_Segmentation_in_Remote_Sensing_CVPR_2026_paper.pdf
    locator: 方法部分；Figure 2（PDF 第 3 页）；实验 Table 2（PDF 第 6 页）
  figure: figure2
  figure_guide: 上部 Cross-Modal Unification 用 RGB／SAR DINO 特征对齐；下部 Full Training 进入 Dual-Encoder Fusion，最后与 CLIP Text 特征匹配类别。
  depicted: true
  route:
  - 光学 SAR 与文本
  - 跨模态语义对齐
  - 融合像素特征
  - 遥感分割
  result_tables:
  - table2
results:
- id: table2
  label: Table 2
  asset: assets/results/mmovseg-table2.png
  page: 6
  version: CVPR 2026 出版方正式版
  source_url: https://openaccess.thecvf.com/content/CVPR2026/papers/Wei_MM-OVSeg_Multimodal_Optical-SAR_Fusion_for_Open-Vocabulary_Segmentation_in_Remote_Sensing_CVPR_2026_paper.pdf
  source_sha256: b9b7b2a52f3b0c009377c898085c07fbc18e18f00357d549f3d71c24821494d7
  clip_pdf_points:
  - 55
  - 56
  - 558
  - 224
  title: MM-OVSeg：主要实验结果
  setting: 原文 Table 1 定义的六组晴空／云覆盖及跨域协议；Table 2 给出对应主结果。
  metrics: mIoU ↑
  reading: 逐个设置看云层条件与训练／测试域；各列不是相同难度的重复评测。
---

# MM-OVSeg

本页按研究问题提取相关操作；模块原图、具体输入输出、来源与主要实验结果在上方展开查看。

## 研究问题

SAR 的结构信息怎样进入语言对齐空间？

## 相关操作

先用配准光学—SAR 图像对训练 SAR DINO 编码器，使其特征接近冻结 RGB DINO；再用双编码融合模块整合 RGB、SAR 和 CLIP 的稠密特征，与类别文本对齐产生开放词汇分割。

## 实验阅读

原文 Table 1 定义的六组晴空／云覆盖及跨域协议；Table 2 给出对应主结果。 逐个设置看云层条件与训练／测试域；各列不是相同难度的重复评测。 主要结果是整套方法的效果，不能单凭该表归因到一个模块。

## 原文依据

- [出版方原文](https://openaccess.thecvf.com/content/CVPR2026/papers/Wei_MM-OVSeg_Multimodal_Optical-SAR_Fusion_for_Open-Vocabulary_Segmentation_in_Remote_Sensing_CVPR_2026_paper.pdf)：方法部分；Figure 2（PDF 第 3 页）；实验 Table 2（PDF 第 6 页）。
- [官方实现](https://github.com/Jimmyxichen/MM-OVSeg)：已检查公开目录，未独立运行训练或评测。
