---
paper_id: maris
title: 'MARIS: Marine Open-Vocabulary Instance Segmentation'
short_name: MARIS
authors:
- Li, Bingyu
- Wang, Feiyu
- Zhang, Da
- Zhao, Zhiyuan
- Gao, Junyu
- Li, Xuelong
year: 2026
preprint_date: unknown
venue: CVPR
publication_status: published
primary_direction: 2d
modalities:
- image
task_setting: open_vocabulary
task_types:
- instance
techniques:
- semantic_alignment
datasets: []
paper_url: https://openaccess.thecvf.com/content/CVPR2026/papers/Li_MARIS_Marine_Open-Vocabulary_Instance_Segmentation_CVPR_2026_paper.pdf
publication_url: https://openaccess.thecvf.com/content/CVPR2026/html/Li_MARIS_Marine_Open-Vocabulary_Instance_Segmentation_CVPR_2026_paper.html
code_status: public
code_url: https://github.com/LiBingyu01/MARIS
code_details: 已核对官方仓库实际实现目录：GETTING_STARTED.md、INSTALL.md、KEY_START_cd.sh、KEY_START_id.sh、KEY_flop_analy.sh、MARIS-visualization-patch.zip。运行及外部权重可用性未独立复现。
content_status: index
checked_on: '2026-11-09'
module_checked_on: '2026-11-09'
summary: 几何先验增强模块融合视觉和结构线索并细化查询；语义对齐注入机制补充水下类别的领域语义，使文本嵌入更贴合水下实例特征，随后以查询掩码执行类别预测。
sources:
- url: https://openaccess.thecvf.com/content/CVPR2026/html/Li_MARIS_Marine_Open-Vocabulary_Instance_Segmentation_CVPR_2026_paper.html
  locator: 正式发表页面及作者信息
- url: https://openaccess.thecvf.com/content/CVPR2026/papers/Li_MARIS_Marine_Open-Vocabulary_Instance_Segmentation_CVPR_2026_paper.pdf
  locator: 方法部分；Figure 3（PDF 第 4 页）；实验 Table 1（PDF 第 6 页）
- url: https://github.com/LiBingyu01/MARIS
  locator: 官方 README 与实际代码目录；不表示已运行
figures:
- id: figure3
  label: Figure 3
  asset: assets/figures/maris-figure3.png
  page: 4
  version: CVPR 2026 出版方正式版
  source_url: https://openaccess.thecvf.com/content/CVPR2026/papers/Li_MARIS_Marine_Open-Vocabulary_Instance_Segmentation_CVPR_2026_paper.pdf
  source_sha256: 9df1809f047adf99f67b9742a430bb978d2e130d7652dcf2f5135f8b872fecca
  clip_pdf_points:
  - 55
  - 50
  - 558
  - 202.4981231689453
methods:
- id: semantic-operation
  track: vocabulary
  problems:
  - alignment
  - unseen
  title: 几何语义融合
  question: 水下外观退化时怎样保持新类别语义？
  operation: 几何先验增强模块融合视觉和结构线索并细化查询；语义对齐注入机制补充水下类别的领域语义，使文本嵌入更贴合水下实例特征，随后以查询掩码执行类别预测。
  input: 水下图像、类别文本及领域语义
  output: 开放词汇实例掩码
  stage: 训练及推理
  supervision: MARIS 已见类别实例标注；预训练视觉语言模型
  origin: proposed
  origin_note: 本文设计的几何语义融合流程；其预训练基础模型与通用组件沿用已有方法，不计作本文新提出。
  origin_refs:
  - url: https://openaccess.thecvf.com/content/CVPR2026/papers/Li_MARIS_Marine_Open-Vocabulary_Instance_Segmentation_CVPR_2026_paper.pdf
    locator: 方法部分列明的基础模型及其参考文献
  evidence:
  - url: https://openaccess.thecvf.com/content/CVPR2026/papers/Li_MARIS_Marine_Open-Vocabulary_Instance_Segmentation_CVPR_2026_paper.pdf
    locator: 方法部分；Figure 3（PDF 第 4 页）；实验 Table 1（PDF 第 6 页）
  figure: figure3
  figure_guide: 左中部 Geometric Prior Enhancement 提供结构增强查询，右侧 Semantic Alignment Injection 将类别描述经 CLIP Text、Q-former 等路径注入类别表示。
  depicted: true
  route:
  - CLIP 与领域语义
  - 几何语义融合
  - 实例查询特征
  - 水下实例分割
  result_tables:
  - table1
results:
- id: table1
  label: Table 1
  asset: assets/results/maris-table1.png
  page: 6
  version: CVPR 2026 出版方正式版
  source_url: https://openaccess.thecvf.com/content/CVPR2026/papers/Li_MARIS_Marine_Open-Vocabulary_Instance_Segmentation_CVPR_2026_paper.pdf
  source_sha256: 9df1809f047adf99f67b9742a430bb978d2e130d7652dcf2f5135f8b872fecca
  clip_pdf_points:
  - 55
  - 64
  - 558
  - 334
  title: MARIS：主要实验结果
  setting: MARIS 域内协议；区分 Common、Open Vocabulary、Overall 及 ConvNeXt-B／L。
  metrics: mAP／AP50／AP75 ↑
  reading: 分别核对新类别与常见类别列；不能用 Overall 代替未见类别效果。
---

# MARIS

本页按研究问题提取相关操作；模块原图、具体输入输出、来源与主要实验结果在上方展开查看。

## 研究问题

水下外观退化时怎样保持新类别语义？

## 相关操作

几何先验增强模块融合视觉和结构线索并细化查询；语义对齐注入机制补充水下类别的领域语义，使文本嵌入更贴合水下实例特征，随后以查询掩码执行类别预测。

## 实验阅读

MARIS 域内协议；区分 Common、Open Vocabulary、Overall 及 ConvNeXt-B／L。 分别核对新类别与常见类别列；不能用 Overall 代替未见类别效果。 主要结果是整套方法的效果，不能单凭该表归因到一个模块。

## 原文依据

- [出版方原文](https://openaccess.thecvf.com/content/CVPR2026/papers/Li_MARIS_Marine_Open-Vocabulary_Instance_Segmentation_CVPR_2026_paper.pdf)：方法部分；Figure 3（PDF 第 4 页）；实验 Table 1（PDF 第 6 页）。
- [官方实现](https://github.com/LiBingyu01/MARIS)：已检查公开目录，未独立运行训练或评测。
