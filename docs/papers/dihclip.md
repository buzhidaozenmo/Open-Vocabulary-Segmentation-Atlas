---
paper_id: dihclip
title: 'DIH-CLIP: Unleashing the Diversity of Multi-Head Self-Attention for Training-Free Open-Vocabulary Semantic Segmentation'
short_name: DIH-CLIP
authors:
- Duan, Songsong
- Yang, Xi
- Wang, Nannan
year: 2025
preprint_date: unknown
venue: ICCV
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
- PASCAL
- COCO
- Cityscapes
- ADE20K
paper_url: https://openaccess.thecvf.com/content/ICCV2025/papers/Duan_DIH-CLIP_Unleashing_the_Diversity_of_Multi-Head_Self-Attention_for_Training-Free_Open-Vocabulary_ICCV_2025_paper.pdf
publication_url: https://openaccess.thecvf.com/content/ICCV2025/html/Duan_DIH-CLIP_Unleashing_the_Diversity_of_Multi-Head_Self-Attention_for_Training-Free_Open-Vocabulary_ICCV_2025_paper.html
code_status: public
code_url: https://github.com/duan-song/DiH-CLIP
code_details: 已核对官方仓库实际实现目录：clip、clip_segmentor.py、configs、custom_datasets.py、datasets、demo.py。运行及外部权重可用性未独立复现。
content_status: index
checked_on: '2026-11-09'
module_checked_on: '2026-11-09'
summary: 根据每个注意力头的图信息熵评估其多样性，按阈值剔除冗余头；将保留头的局部表示注入全局 CLIP 特征，并在中间层应用这种选择性注意后融合细节。
sources:
- url: https://openaccess.thecvf.com/content/ICCV2025/html/Duan_DIH-CLIP_Unleashing_the_Diversity_of_Multi-Head_Self-Attention_for_Training-Free_Open-Vocabulary_ICCV_2025_paper.html
  locator: 正式发表页面及作者信息
- url: https://openaccess.thecvf.com/content/ICCV2025/papers/Duan_DIH-CLIP_Unleashing_the_Diversity_of_Multi-Head_Self-Attention_for_Training-Free_Open-Vocabulary_ICCV_2025_paper.pdf
  locator: 方法部分；Figure 2（PDF 第 3 页）；实验 Table 1（PDF 第 6 页）
- url: https://github.com/duan-song/DiH-CLIP
  locator: 官方 README 与实际代码目录；不表示已运行
figures:
- id: figure2
  label: Figure 2
  asset: assets/figures/dihclip-figure2.png
  page: 3
  version: ICCV 2025 出版方正式版
  source_url: https://openaccess.thecvf.com/content/ICCV2025/papers/Duan_DIH-CLIP_Unleashing_the_Diversity_of_Multi-Head_Self-Attention_for_Training-Free_Open-Vocabulary_ICCV_2025_paper.pdf
  source_sha256: bd519b84481f5aee0e92d8ec9d8011e443d85ac8768d5124bdba016b39633346
  clip_pdf_points:
  - 55
  - 50
  - 558
  - 205.0702362060547
methods:
- id: semantic-operation
  track: vocabulary
  problems:
  - reliability
  - alignment
  title: 注意力选择与融合
  question: 哪些注意力头值得用于局部语义传播？
  operation: 根据每个注意力头的图信息熵评估其多样性，按阈值剔除冗余头；将保留头的局部表示注入全局 CLIP 特征，并在中间层应用这种选择性注意后融合细节。
  input: CLIP 多头注意力及文本类别
  output: 选择头融合后的像素语言特征
  stage: 免任务训练推理
  supervision: 冻结 CLIP；原文对应版本可使用额外视觉模型
  origin: proposed
  origin_note: 本文设计的注意力选择与融合流程；其预训练基础模型与通用组件沿用已有方法，不计作本文新提出。
  origin_refs:
  - url: https://openaccess.thecvf.com/content/ICCV2025/papers/Duan_DIH-CLIP_Unleashing_the_Diversity_of_Multi-Head_Self-Attention_for_Training-Free_Open-Vocabulary_ICCV_2025_paper.pdf
    locator: 方法部分列明的基础模型及其参考文献
  evidence:
  - url: https://openaccess.thecvf.com/content/ICCV2025/papers/Duan_DIH-CLIP_Unleashing_the_Diversity_of_Multi-Head_Self-Attention_for_Training-Free_Open-Vocabulary_ICCV_2025_paper.pdf
    locator: 方法部分；Figure 2（PDF 第 3 页）；实验 Table 1（PDF 第 6 页）
  figure: figure2
  figure_guide: 下部沿 CLIP visual encoder 进入中层 SHA，再看上方各头的筛选／投影与融合连接，最后与文本编码结果形成像素预测。
  depicted: true
  route:
  - CLIP 多头特征
  - 注意力选择与融合
  - 像素语言特征
  - 开放词汇分割
  result_tables:
  - table1
results:
- id: table1
  label: Table 1
  asset: assets/results/dihclip-table1.png
  page: 6
  version: ICCV 2025 出版方正式版
  source_url: https://openaccess.thecvf.com/content/ICCV2025/papers/Duan_DIH-CLIP_Unleashing_the_Diversity_of_Multi-Head_Self-Attention_for_Training-Free_Open-Vocabulary_ICCV_2025_paper.pdf
  source_sha256: bd519b84481f5aee0e92d8ec9d8011e443d85ac8768d5124bdba016b39633346
  clip_pdf_points:
  - 55
  - 56
  - 558
  - 391
  title: DIH-CLIP：主要实验结果
  setting: 原表比较训练方式、额外 VFM、背景协议和模型变体。
  metrics: mIoU ↑
  reading: 按训练方式和额外 VFM 分组阅读；只比较表中同等配置行。
---

# DIH-CLIP

本页按研究问题提取相关操作；模块原图、具体输入输出、来源与主要实验结果在上方展开查看。

## 研究问题

哪些注意力头值得用于局部语义传播？

## 相关操作

根据每个注意力头的图信息熵评估其多样性，按阈值剔除冗余头；将保留头的局部表示注入全局 CLIP 特征，并在中间层应用这种选择性注意后融合细节。

## 实验阅读

原表比较训练方式、额外 VFM、背景协议和模型变体。 按训练方式和额外 VFM 分组阅读；只比较表中同等配置行。 主要结果是整套方法的效果，不能单凭该表归因到一个模块。

## 原文依据

- [出版方原文](https://openaccess.thecvf.com/content/ICCV2025/papers/Duan_DIH-CLIP_Unleashing_the_Diversity_of_Multi-Head_Self-Attention_for_Training-Free_Open-Vocabulary_ICCV_2025_paper.pdf)：方法部分；Figure 2（PDF 第 3 页）；实验 Table 1（PDF 第 6 页）。
- [官方实现](https://github.com/duan-song/DiH-CLIP)：已检查公开目录，未独立运行训练或评测。
