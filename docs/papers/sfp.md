---
paper_id: sfp
title: 'Feature Purification Matters: Suppressing Outlier Propagation for Training-Free Open-Vocabulary Semantic Segmentation'
short_name: SFP
authors:
- Jin, Shuo
- Yu, Siyue
- Zhang, Bingfeng
- Sun, Mingjie
- Dong, Yi
- Xiao, Jimin
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
paper_url: https://openaccess.thecvf.com/content/ICCV2025/papers/Jin_Feature_Purification_Matters_Suppressing_Outlier_Propagation_for_Training-Free_Open-Vocabulary_Semantic_ICCV_2025_paper.pdf
publication_url: https://openaccess.thecvf.com/content/ICCV2025/html/Jin_Feature_Purification_Matters_Suppressing_Outlier_Propagation_for_Training-Free_Open-Vocabulary_Semantic_ICCV_2025_paper.html
code_status: public
code_url: https://github.com/Kimsure/SFP
code_details: 已核对官方仓库实际实现目录：SFP-D_Journal、SFP_ICCV。运行及外部权重可用性未独立复现。
content_status: index
checked_on: '2026-11-09'
module_checked_on: '2026-11-09'
summary: 逐层用自适应异常缓解器检测并减轻异常 token；最后一层以语义感知注意增强相关区域，再用层次注意力整合器聚合多层，得到对象中心特征后计算文本相似度。
sources:
- url: https://openaccess.thecvf.com/content/ICCV2025/html/Jin_Feature_Purification_Matters_Suppressing_Outlier_Propagation_for_Training-Free_Open-Vocabulary_Semantic_ICCV_2025_paper.html
  locator: 正式发表页面及作者信息
- url: https://openaccess.thecvf.com/content/ICCV2025/papers/Jin_Feature_Purification_Matters_Suppressing_Outlier_Propagation_for_Training-Free_Open-Vocabulary_Semantic_ICCV_2025_paper.pdf
  locator: 方法部分；Figure 2（PDF 第 4 页）；实验 Table 1（PDF 第 6 页）
- url: https://github.com/Kimsure/SFP
  locator: 官方 README 与实际代码目录；不表示已运行
figures:
- id: figure2
  label: Figure 2
  asset: assets/figures/sfp-figure2.png
  page: 4
  version: ICCV 2025 出版方正式版
  source_url: https://openaccess.thecvf.com/content/ICCV2025/papers/Jin_Feature_Purification_Matters_Suppressing_Outlier_Propagation_for_Training-Free_Open-Vocabulary_Semantic_ICCV_2025_paper.pdf
  source_sha256: b3b3c33052ad1cb04e43757b5922641975b49d24c0b59376fcbb7116d5e443ef
  clip_pdf_points:
  - 55
  - 50
  - 558
  - 322.383056640625
methods:
- id: semantic-operation
  track: vocabulary
  problems:
  - reliability
  - alignment
  title: 异常抑制与注意聚合
  question: 中间层异常 token 传播怎样抑制？
  operation: 逐层用自适应异常缓解器检测并减轻异常 token；最后一层以语义感知注意增强相关区域，再用层次注意力整合器聚合多层，得到对象中心特征后计算文本相似度。
  input: CLIP 各层图像 token 与类别文本
  output: 净化后的像素语言特征及类别图
  stage: 免任务训练推理
  supervision: 预训练 CLIP，无目标分割训练标注
  origin: proposed
  origin_note: 本文设计的异常抑制与注意聚合流程；其预训练基础模型与通用组件沿用已有方法，不计作本文新提出。
  origin_refs:
  - url: https://openaccess.thecvf.com/content/ICCV2025/papers/Jin_Feature_Purification_Matters_Suppressing_Outlier_Propagation_for_Training-Free_Open-Vocabulary_Semantic_ICCV_2025_paper.pdf
    locator: 方法部分列明的基础模型及其参考文献
  evidence:
  - url: https://openaccess.thecvf.com/content/ICCV2025/papers/Jin_Feature_Purification_Matters_Suppressing_Outlier_Propagation_for_Training-Free_Open-Vocabulary_Semantic_ICCV_2025_paper.pdf
    locator: 方法部分；Figure 2（PDF 第 4 页）；实验 Table 1（PDF 第 6 页）
  figure: figure2
  figure_guide: 图中 SOM 位于多层图像编码器，SAE 在末层增强语义注意，HAI 聚合多层；最终与 CLIP 文本特征做 cosine similarity 输出分割。
  depicted: true
  route:
  - CLIP 中间层特征
  - 异常抑制与注意聚合
  - 像素语言特征
  - 开放词汇分割
  result_tables:
  - table1
results:
- id: table1
  label: Table 1
  asset: assets/results/sfp-table1.png
  page: 6
  version: ICCV 2025 出版方正式版
  source_url: https://openaccess.thecvf.com/content/ICCV2025/papers/Jin_Feature_Purification_Matters_Suppressing_Outlier_Propagation_for_Training-Free_Open-Vocabulary_Semantic_ICCV_2025_paper.pdf
  source_sha256: b3b3c33052ad1cb04e43757b5922641975b49d24c0b59376fcbb7116d5e443ef
  clip_pdf_points:
  - 55
  - 56
  - 558
  - 323
  title: SFP：主要实验结果
  setting: 八个语义分割基准；保留额外骨干及 with／without background。
  metrics: mIoU ↑
  reading: 相同骨干和背景协议内比较；净化模块贡献需另看消融。
---

# SFP

本页按研究问题提取相关操作；模块原图、具体输入输出、来源与主要实验结果在上方展开查看。

## 研究问题

中间层异常 token 传播怎样抑制？

## 相关操作

逐层用自适应异常缓解器检测并减轻异常 token；最后一层以语义感知注意增强相关区域，再用层次注意力整合器聚合多层，得到对象中心特征后计算文本相似度。

## 实验阅读

八个语义分割基准；保留额外骨干及 with／without background。 相同骨干和背景协议内比较；净化模块贡献需另看消融。 主要结果是整套方法的效果，不能单凭该表归因到一个模块。

## 原文依据

- [出版方原文](https://openaccess.thecvf.com/content/ICCV2025/papers/Jin_Feature_Purification_Matters_Suppressing_Outlier_Propagation_for_Training-Free_Open-Vocabulary_Semantic_ICCV_2025_paper.pdf)：方法部分；Figure 2（PDF 第 4 页）；实验 Table 1（PDF 第 6 页）。
- [官方实现](https://github.com/Kimsure/SFP)：已检查公开目录，未独立运行训练或评测。
