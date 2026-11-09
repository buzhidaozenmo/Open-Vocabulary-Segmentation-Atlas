---
paper_id: unigeoseg
title: 'UniGeoSeg: Towards Unified Open-World Segmentation for Geospatial Scenes'
short_name: UniGeoSeg
authors:
- Ni, Shuo
- Wang, Di
- Chen, He
- Guo, Haonan
- Zhang, Ning
- Zhang, Jing
year: 2026
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
datasets:
- SIOR
paper_url: https://openaccess.thecvf.com/content/CVPR2026/papers/Ni_UniGeoSeg_Towards_Unified_Open-World_Segmentation_for_Geospatial_Scenes_CVPR_2026_paper.pdf
publication_url: https://openaccess.thecvf.com/content/CVPR2026/html/Ni_UniGeoSeg_Towards_Unified_Open-World_Segmentation_for_Geospatial_Scenes_CVPR_2026_paper.html
code_status: public
code_url: https://github.com/MiliLab/UniGeoSeg
code_details: 已核对官方仓库实际实现目录：Figs、requirements.txt、scripts、unigeoseg。运行及外部权重可用性未独立复现。
content_status: index
checked_on: '2026-11-09'
module_checked_on: '2026-11-09'
summary: 把指令经任务感知文本增强后输入视觉语言模型，用潜在知识记忆检索补充任务相关语义，再通过掩码预测分支输出分割；渐进训练使指代、交互和推理指令共用一套表示。
sources:
- url: https://openaccess.thecvf.com/content/CVPR2026/html/Ni_UniGeoSeg_Towards_Unified_Open-World_Segmentation_for_Geospatial_Scenes_CVPR_2026_paper.html
  locator: 正式发表页面及作者信息
- url: https://openaccess.thecvf.com/content/CVPR2026/papers/Ni_UniGeoSeg_Towards_Unified_Open-World_Segmentation_for_Geospatial_Scenes_CVPR_2026_paper.pdf
  locator: 方法部分；Figure 2（PDF 第 4 页）；实验 Table 2（PDF 第 6 页）
- url: https://github.com/MiliLab/UniGeoSeg
  locator: 官方 README 与实际代码目录；不表示已运行
figures:
- id: figure2
  label: Figure 2
  asset: assets/figures/unigeoseg-figure2.png
  page: 4
  version: CVPR 2026 出版方正式版
  source_url: https://openaccess.thecvf.com/content/CVPR2026/papers/Ni_UniGeoSeg_Towards_Unified_Open-World_Segmentation_for_Geospatial_Scenes_CVPR_2026_paper.pdf
  source_sha256: 277d2f64994460095de552f0497c5814330128f682b4e952b848dcd92721e042
  clip_pdf_points:
  - 55
  - 50
  - 558
  - 296.3819885253906
methods:
- id: semantic-operation
  track: vocabulary
  problems:
  - prompt
  - alignment
  title: 任务语义增强
  question: 指令里的任务和语义怎样变成遥感掩码？
  operation: 把指令经任务感知文本增强后输入视觉语言模型，用潜在知识记忆检索补充任务相关语义，再通过掩码预测分支输出分割；渐进训练使指代、交互和推理指令共用一套表示。
  input: 遥感图像、自然语言或交互指令
  output: 指令对应的分割掩码
  stage: 训练及推理
  supervision: GeoSeg-1M 的图像—掩码—指令配对
  origin: proposed
  origin_note: 本文设计的任务语义增强流程；其预训练基础模型与通用组件沿用已有方法，不计作本文新提出。
  origin_refs:
  - url: https://openaccess.thecvf.com/content/CVPR2026/papers/Ni_UniGeoSeg_Towards_Unified_Open-World_Segmentation_for_Geospatial_Scenes_CVPR_2026_paper.pdf
    locator: 方法部分列明的基础模型及其参考文献
  evidence:
  - url: https://openaccess.thecvf.com/content/CVPR2026/papers/Ni_UniGeoSeg_Towards_Unified_Open-World_Segmentation_for_Geospatial_Scenes_CVPR_2026_paper.pdf
    locator: 方法部分；Figure 2（PDF 第 4 页）；实验 Table 2（PDF 第 6 页）
  figure: figure2
  figure_guide: 先沿上半部 Image Input 与 Mask-Text Instructions 的主链阅读；下半部 Task-Aware Text Enhancement 和 Latent Knowledge Memory
    展示语义增强与记忆检索。
  depicted: true
  route:
  - 多模态语言指令
  - 任务语义增强
  - 指令条件掩码
  - 指令分割
  result_tables:
  - table2
results:
- id: table2
  label: Table 2
  asset: assets/results/unigeoseg-table2.png
  page: 6
  version: CVPR 2026 出版方正式版
  source_url: https://openaccess.thecvf.com/content/CVPR2026/papers/Ni_UniGeoSeg_Towards_Unified_Open-World_Segmentation_for_Geospatial_Scenes_CVPR_2026_paper.pdf
  source_sha256: 277d2f64994460095de552f0497c5814330128f682b4e952b848dcd92721e042
  clip_pdf_points:
  - 309
  - 65
  - 558
  - 325
  title: UniGeoSeg：主要实验结果
  setting: GeoSeg-Bench；区分 Interactive、Referring、Reasoning 子任务及各自指标。
  metrics: gIoU／cIoU／mIoU 等 ↑，按原表分列
  reading: 不同子任务分开比较，不把指代结果视为零样本类别分割。
---

# UniGeoSeg

本页按研究问题提取相关操作；模块原图、具体输入输出、来源与主要实验结果在上方展开查看。

## 研究问题

指令里的任务和语义怎样变成遥感掩码？

## 相关操作

把指令经任务感知文本增强后输入视觉语言模型，用潜在知识记忆检索补充任务相关语义，再通过掩码预测分支输出分割；渐进训练使指代、交互和推理指令共用一套表示。

## 实验阅读

GeoSeg-Bench；区分 Interactive、Referring、Reasoning 子任务及各自指标。 不同子任务分开比较，不把指代结果视为零样本类别分割。 主要结果是整套方法的效果，不能单凭该表归因到一个模块。

## 原文依据

- [出版方原文](https://openaccess.thecvf.com/content/CVPR2026/papers/Ni_UniGeoSeg_Towards_Unified_Open-World_Segmentation_for_Geospatial_Scenes_CVPR_2026_paper.pdf)：方法部分；Figure 2（PDF 第 4 页）；实验 Table 2（PDF 第 6 页）。
- [官方实现](https://github.com/MiliLab/UniGeoSeg)：已检查公开目录，未独立运行训练或评测。
