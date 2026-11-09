---
paper_id: segearthov
title: 'SegEarth-OV: Towards Training-Free Open-Vocabulary Segmentation for Remote Sensing Images'
short_name: SegEarth-OV
authors:
- Li, Kaiyu
- Liu, Ruixun
- Cao, Xiangyong
- Bai, Xueru
- Zhou, Feng
- Meng, Deyu
- Wang, Zhi
year: 2025
preprint_date: unknown
venue: CVPR
publication_status: published
primary_direction: remote
modalities:
- image
task_setting: open_vocabulary
task_types:
- semantic
techniques:
- semantic_alignment
datasets: []
paper_url: https://openaccess.thecvf.com/content/CVPR2025/papers/Li_SegEarth-OV_Towards_Training-Free_Open-Vocabulary_Segmentation_for_Remote_Sensing_Images_CVPR_2025_paper.pdf
publication_url: https://openaccess.thecvf.com/content/CVPR2025/html/Li_SegEarth-OV_Towards_Training-Free_Open-Vocabulary_Segmentation_for_Remote_Sensing_Images_CVPR_2025_paper.html
code_status: public
code_url: https://github.com/likyoo/SegEarth-OV
code_details: 已核对官方仓库实际实现目录：BLIP、configs、custom_datasets.py、dataset_prepare.md、demo.py、demo。运行及外部权重可用性未独立复现。
content_status: index
checked_on: '2026-11-09'
module_checked_on: '2026-11-09'
summary: SimFeatUp 用少量无标签图像学习特征上采样；推理中将冻结 CLIP 的低分辨率特征上采样，再减去 CLS 特征以降低全局语义偏置，最后与类别文本匹配得到遥感类别图。
sources:
- url: https://openaccess.thecvf.com/content/CVPR2025/html/Li_SegEarth-OV_Towards_Training-Free_Open-Vocabulary_Segmentation_for_Remote_Sensing_Images_CVPR_2025_paper.html
  locator: 正式发表页面及作者信息
- url: https://openaccess.thecvf.com/content/CVPR2025/papers/Li_SegEarth-OV_Towards_Training-Free_Open-Vocabulary_Segmentation_for_Remote_Sensing_Images_CVPR_2025_paper.pdf
  locator: 方法部分；Figure 3（PDF 第 3 页）；实验 Table 1（PDF 第 6 页）
- url: https://github.com/likyoo/SegEarth-OV
  locator: 官方 README 与实际代码目录；不表示已运行
figures:
- id: figure3
  label: Figure 3
  asset: assets/figures/segearthov-figure3.png
  page: 3
  version: CVPR 2025 出版方正式版
  source_url: https://openaccess.thecvf.com/content/CVPR2025/papers/Li_SegEarth-OV_Towards_Training-Free_Open-Vocabulary_Segmentation_for_Remote_Sensing_Images_CVPR_2025_paper.pdf
  source_sha256: 944eb077fe1c7fbd570b7abc1a5369b1b896698bf8577e57ecc8e6207d2ddc71
  clip_pdf_points:
  - 309
  - 50
  - 558
  - 272.3279724121094
methods:
- id: semantic-operation
  track: vocabulary
  problems:
  - alignment
  - efficiency
  title: 空间恢复与全局去偏
  question: 遥感小目标怎样避免低分辨率与全局语义偏置？
  operation: SimFeatUp 用少量无标签图像学习特征上采样；推理中将冻结 CLIP 的低分辨率特征上采样，再减去 CLS 特征以降低全局语义偏置，最后与类别文本匹配得到遥感类别图。
  input: 遥感图像、CLIP patch／CLS 特征、文本
  output: 高分辨率类别图
  stage: 上采样器预训练；分割推理
  supervision: 上采样器使用无标签图像，非目标分割标签
  origin: proposed
  origin_note: 本文设计的空间恢复与全局去偏流程；其预训练基础模型与通用组件沿用已有方法，不计作本文新提出。
  origin_refs:
  - url: https://openaccess.thecvf.com/content/CVPR2025/papers/Li_SegEarth-OV_Towards_Training-Free_Open-Vocabulary_Segmentation_for_Remote_Sensing_Images_CVPR_2025_paper.pdf
    locator: 方法部分列明的基础模型及其参考文献
  evidence:
  - url: https://openaccess.thecvf.com/content/CVPR2025/papers/Li_SegEarth-OV_Towards_Training-Free_Open-Vocabulary_Segmentation_for_Remote_Sensing_Images_CVPR_2025_paper.pdf
    locator: 方法部分；Figure 3（PDF 第 3 页）；实验 Table 1（PDF 第 6 页）
  figure: figure3
  figure_guide: 右列原图 (a) 展示无标签 SimFeatUp 训练，(b) 是冻结 CLIP 特征上采样后减去 CLS 的推理路径；两阶段监督不同。
  depicted: true
  route:
  - CLIP 与上采样器
  - 空间恢复与全局去偏
  - 像素语言特征
  - 遥感开放词汇分割
  result_tables:
  - table1
results:
- id: table1
  label: Table 1
  asset: assets/results/segearthov-table1.png
  page: 6
  version: CVPR 2025 出版方正式版
  source_url: https://openaccess.thecvf.com/content/CVPR2025/papers/Li_SegEarth-OV_Towards_Training-Free_Open-Vocabulary_Segmentation_for_Remote_Sensing_Images_CVPR_2025_paper.pdf
  source_sha256: 944eb077fe1c7fbd570b7abc1a5369b1b896698bf8577e57ecc8e6207d2ddc71
  clip_pdf_points:
  - 55
  - 55
  - 558
  - 198
  title: SegEarth-OV：主要实验结果
  setting: 八个多类别遥感数据集；论文另有建筑／道路／洪水单类别结果。
  metrics: mIoU ↑
  reading: 本图展示多类别遥感主结果；建筑、道路和洪水等单类别协议另见原文其他表。
---

# SegEarth-OV

本页按研究问题提取相关操作；模块原图、具体输入输出、来源与主要实验结果在上方展开查看。

## 研究问题

遥感小目标怎样避免低分辨率与全局语义偏置？

## 相关操作

SimFeatUp 用少量无标签图像学习特征上采样；推理中将冻结 CLIP 的低分辨率特征上采样，再减去 CLS 特征以降低全局语义偏置，最后与类别文本匹配得到遥感类别图。

## 实验阅读

八个多类别遥感数据集；论文另有建筑／道路／洪水单类别结果。 这里展示多类别主表；SimFeatUp 需要无监督训练，不把全文训练自由度混成单标签。 主要结果是整套方法的效果，不能单凭该表归因到一个模块。

## 原文依据

- [出版方原文](https://openaccess.thecvf.com/content/CVPR2025/papers/Li_SegEarth-OV_Towards_Training-Free_Open-Vocabulary_Segmentation_for_Remote_Sensing_Images_CVPR_2025_paper.pdf)：方法部分；Figure 3（PDF 第 3 页）；实验 Table 1（PDF 第 6 页）。
- [官方实现](https://github.com/likyoo/SegEarth-OV)：已检查公开目录，未独立运行训练或评测。
