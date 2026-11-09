---
paper_id: pcaseg
title: 'PCA-Seg: Revisiting Cost Aggregation for Open-Vocabulary Semantic and Part Segmentation'
short_name: PCA-Seg
authors:
- Yin, Jianjian
- Chen, Tao
- Chen, Yi
- Pei, Gensheng
- Shu, Xiangbo
- Yao, Yazhou
- Shen, Fumin
year: 2026
preprint_date: unknown
venue: CVPR
publication_status: published
primary_direction: 2d
modalities:
- image
task_setting: open_vocabulary
task_types:
- semantic
techniques:
- semantic_alignment
datasets:
- ADE20K
- COCO
- PASCAL
paper_url: https://openaccess.thecvf.com/content/CVPR2026/papers/Yin_PCA-Seg_Revisiting_Cost_Aggregation_for_Open-Vocabulary_Semantic_and_Part_Segmentation_CVPR_2026_paper.pdf
publication_url: https://openaccess.thecvf.com/content/CVPR2026/html/Yin_PCA-Seg_Revisiting_Cost_Aggregation_for_Open-Vocabulary_Semantic_and_Part_Segmentation_CVPR_2026_paper.html
code_status: public
code_url: https://github.com/NUST-Machine-Intelligence-Laboratory/PCA-Seg
code_details: 已核对官方仓库实际实现目录：arch.png、cat_seg、configs、datasets、demo、eval.sh。运行及外部权重可用性未独立复现。
content_status: index
checked_on: '2026-11-09'
module_checked_on: '2026-11-09'
summary: 从 CLIP 图文代价体分别建立空间流和类别流，并行聚合；FOD 去除两流的冗余成分，EPL 多专家解析不同信息，再用逐像素系数融合成解码器输入，而不是串联覆盖另一流信息。
sources:
- url: https://openaccess.thecvf.com/content/CVPR2026/html/Yin_PCA-Seg_Revisiting_Cost_Aggregation_for_Open-Vocabulary_Semantic_and_Part_Segmentation_CVPR_2026_paper.html
  locator: 正式发表页面及作者信息
- url: https://openaccess.thecvf.com/content/CVPR2026/papers/Yin_PCA-Seg_Revisiting_Cost_Aggregation_for_Open-Vocabulary_Semantic_and_Part_Segmentation_CVPR_2026_paper.pdf
  locator: 方法部分；Figure 3（PDF 第 4 页）；实验 Table 1（PDF 第 6 页）
- url: https://github.com/NUST-Machine-Intelligence-Laboratory/PCA-Seg
  locator: 官方 README 与实际代码目录；不表示已运行
figures:
- id: figure3
  label: Figure 3
  asset: assets/figures/pcaseg-figure3.png
  page: 4
  version: CVPR 2026 出版方正式版
  source_url: https://openaccess.thecvf.com/content/CVPR2026/papers/Yin_PCA-Seg_Revisiting_Cost_Aggregation_for_Open-Vocabulary_Semantic_and_Part_Segmentation_CVPR_2026_paper.pdf
  source_sha256: 238f0ddfc40b65a37ad159c8158659fefc78ef4b6d46c03678629808e066c20d
  clip_pdf_points:
  - 55
  - 50
  - 558
  - 194.39596557617188
methods:
- id: semantic-operation
  track: vocabulary
  problems:
  - alignment
  title: 并行代价聚合
  question: 空间聚合与类别聚合怎样避免相互干扰？
  operation: 从 CLIP 图文代价体分别建立空间流和类别流，并行聚合；FOD 去除两流的冗余成分，EPL 多专家解析不同信息，再用逐像素系数融合成解码器输入，而不是串联覆盖另一流信息。
  input: 图像、文本类别、CLIP 相似度代价体
  output: 融合后的像素类别／部件预测
  stage: 训练及推理
  supervision: 分割训练标注；预训练 CLIP
  origin: proposed
  origin_note: 本文设计的并行代价聚合流程；其预训练基础模型与通用组件沿用已有方法，不计作本文新提出。
  origin_refs:
  - url: https://openaccess.thecvf.com/content/CVPR2026/papers/Yin_PCA-Seg_Revisiting_Cost_Aggregation_for_Open-Vocabulary_Semantic_and_Part_Segmentation_CVPR_2026_paper.pdf
    locator: 方法部分列明的基础模型及其参考文献
  evidence:
  - url: https://openaccess.thecvf.com/content/CVPR2026/papers/Yin_PCA-Seg_Revisiting_Cost_Aggregation_for_Open-Vocabulary_Semantic_and_Part_Segmentation_CVPR_2026_paper.pdf
    locator: 方法部分；Figure 3（PDF 第 4 页）；实验 Table 1（PDF 第 6 页）
  figure: figure3
  figure_guide: 从 cost volume 分出的 class／spatial 两条并行路径进入 FOD 与 EPL，再由逐像素系数融合回解码器；不要把两流读成串行前后处理。
  depicted: true
  route:
  - CLIP 图文代价体
  - 并行代价聚合
  - 像素类别特征
  - 语义与部件分割
  result_tables:
  - table1
results:
- id: table1
  label: Table 1
  asset: assets/results/pcaseg-table1.png
  page: 6
  version: CVPR 2026 出版方正式版
  source_url: https://openaccess.thecvf.com/content/CVPR2026/papers/Yin_PCA-Seg_Revisiting_Cost_Aggregation_for_Open-Vocabulary_Semantic_and_Part_Segmentation_CVPR_2026_paper.pdf
  source_sha256: 238f0ddfc40b65a37ad159c8158659fefc78ef4b6d46c03678629808e066c20d
  clip_pdf_points:
  - 55
  - 54
  - 558
  - 300
  title: PCA-Seg：主要实验结果
  setting: 多个二维语义分割基准；保留骨干、训练数据与有无背景的原表分组。
  metrics: mIoU ↑
  reading: 在相同骨干与训练数据下比较；部件结果另见 Table 2。
---

# PCA-Seg

本页按研究问题提取相关操作；模块原图、具体输入输出、来源与主要实验结果在上方展开查看。

## 研究问题

空间聚合与类别聚合怎样避免相互干扰？

## 相关操作

从 CLIP 图文代价体分别建立空间流和类别流，并行聚合；FOD 去除两流的冗余成分，EPL 多专家解析不同信息，再用逐像素系数融合成解码器输入，而不是串联覆盖另一流信息。

## 实验阅读

多个二维语义分割基准；保留骨干、训练数据与有无背景的原表分组。 在相同骨干与训练数据下比较；部件结果另见 Table 2。 主要结果是整套方法的效果，不能单凭该表归因到一个模块。

## 原文依据

- [出版方原文](https://openaccess.thecvf.com/content/CVPR2026/papers/Yin_PCA-Seg_Revisiting_Cost_Aggregation_for_Open-Vocabulary_Semantic_and_Part_Segmentation_CVPR_2026_paper.pdf)：方法部分；Figure 3（PDF 第 4 页）；实验 Table 1（PDF 第 6 页）。
- [官方实现](https://github.com/NUST-Machine-Intelligence-Laboratory/PCA-Seg)：已检查公开目录，未独立运行训练或评测。
