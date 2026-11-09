---
paper_id: partcatseg
title: Fine-Grained Image-Text Correspondence with Cost Aggregation for Open-Vocabulary Part Segmentation
short_name: PartCATSeg
authors:
- Choi, Jiho
- Lee, Seonho
- Lee, Minhyun
- Lee, Seungho
- Shim, Hyunjung
year: 2025
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
datasets: []
paper_url: https://openaccess.thecvf.com/content/CVPR2025/papers/Choi_Fine-Grained_Image-Text_Correspondence_with_Cost_Aggregation_for_Open-Vocabulary_Part_Segmentation_CVPR_2025_paper.pdf
publication_url: https://openaccess.thecvf.com/content/CVPR2025/html/Choi_Fine-Grained_Image-Text_Correspondence_with_Cost_Aggregation_for_Open-Vocabulary_Part_Segmentation_CVPR_2025_paper.html
code_status: public
code_url: https://github.com/kaist-cvml/part-catseg
code_details: 已核对官方实现目录：baselines、configs、datasets、open_clip、requirements.txt、train_net.py。未独立运行或验证外部权重下载。
content_status: index
checked_on: '2026-11-09'
module_checked_on: '2026-11-09'
summary: 分别聚合对象、部件及对象—部件文本的图文代价，引入 DINO 结构指导；组合损失约束部件类别分布汇总后与所属对象一致，减少同名部件跨对象混淆。
sources:
- url: https://openaccess.thecvf.com/content/CVPR2025/html/Choi_Fine-Grained_Image-Text_Correspondence_with_Cost_Aggregation_for_Open-Vocabulary_Part_Segmentation_CVPR_2025_paper.html
  locator: 正式发表来源：出版页面／作者项目的会议说明
- url: https://openaccess.thecvf.com/content/CVPR2025/papers/Choi_Fine-Grained_Image-Text_Correspondence_with_Cost_Aggregation_for_Open-Vocabulary_Part_Segmentation_CVPR_2025_paper.pdf
  locator: 方法部分；Figure 4（PDF 第 4 页）；实验 Table 1（PDF 第 7 页）
- url: https://github.com/kaist-cvml/part-catseg
  locator: 官方 README、目录与开放范围；未独立运行
figures:
- id: fig4
  label: Figure 4
  asset: assets/figures/partcatseg-fig4.png
  page: 4
  version: CVPR 2025 出版方正式版
  source_url: https://openaccess.thecvf.com/content/CVPR2025/papers/Choi_Fine-Grained_Image-Text_Correspondence_with_Cost_Aggregation_for_Open-Vocabulary_Part_Segmentation_CVPR_2025_paper.pdf
  source_sha256: 577e0ef86b89018dce1c844bedcf52935cbee48cd283baae5933eb36c7217c56
  clip_pdf_points:
  - 45
  - 45
  - 567
  - 234.938
methods:
- id: semantic-operation
  track: vocabulary
  problems:
  - alignment
  - regions
  title: 对象部件代价聚合
  question: 如何让部件预测遵循对象层级？
  operation: 分别聚合对象、部件及对象—部件文本的图文代价，引入 DINO 结构指导；组合损失约束部件类别分布汇总后与所属对象一致，减少同名部件跨对象混淆。
  input: 图像、对象／部件文本、CLIP 代价与 DINO 特征
  output: 对象感知的部件分割图
  stage: 分割训练及推理
  supervision: 训练部件掩码与对象关系；预训练 CLIP／DINO
  origin: proposed
  origin_note: 本文设计的对象部件代价聚合流程；所用预训练模型、通用投影及基础算子沿用已有方法，不计作本文新提出。
  evidence:
  - url: https://openaccess.thecvf.com/content/CVPR2025/papers/Choi_Fine-Grained_Image-Text_Correspondence_with_Cost_Aggregation_for_Open-Vocabulary_Part_Segmentation_CVPR_2025_paper.pdf
    locator: 方法部分；Figure 4（PDF 第 4 页）；实验 Table 1（PDF 第 7 页）
  figure: fig4
  figure_guide: 看三组代价流、DINO Structural Guidance 和 Compositional Guidance。
  depicted: true
  route:
  - 预训练视觉语言特征
  - 对象部件代价聚合
  - 像素／区域类别表示
  - 开放词汇分割
  result_tables:
  - table1
results:
- id: table1
  label: Table 1
  asset: assets/results/partcatseg-table1.png
  page: 7
  version: CVPR 2025 出版方正式版
  source_url: https://openaccess.thecvf.com/content/CVPR2025/papers/Choi_Fine-Grained_Image-Text_Correspondence_with_Cost_Aggregation_for_Open-Vocabulary_Part_Segmentation_CVPR_2025_paper.pdf
  source_sha256: 577e0ef86b89018dce1c844bedcf52935cbee48cd283baae5933eb36c7217c56
  clip_pdf_points:
  - 55
  - 55
  - 299
  - 210
  title: PartCATSeg：主要实验结果
  setting: Pascal-Part-116 零样本部件评测，原表区分已见、未见和预测词汇设置。
  metrics: mIoU／hIoU ↑
  reading: 按相同预测词汇和 Seen／Unseen 划分比较。
---

# PartCATSeg

本页按研究问题提取相关操作；模块图、输入输出、证据和主要结果表在上方展开查看。

## 研究问题

如何让部件预测遵循对象层级？

## 相关操作

分别聚合对象、部件及对象—部件文本的图文代价，引入 DINO 结构指导；组合损失约束部件类别分布汇总后与所属对象一致，减少同名部件跨对象混淆。

## 实验阅读

Pascal-Part-116 零样本部件评测，原表区分已见、未见和预测词汇设置。 按相同预测词汇和 Seen／Unseen 划分比较。 主表是整体系统结果，单一模块的贡献需结合原文消融。

## 原文依据

- [本次阅读的原文版本](https://openaccess.thecvf.com/content/CVPR2025/papers/Choi_Fine-Grained_Image-Text_Correspondence_with_Cost_Aggregation_for_Open-Vocabulary_Part_Segmentation_CVPR_2025_paper.pdf)：方法部分；Figure 4（PDF 第 4 页）；实验 Table 1（PDF 第 7 页）。
- [正式发表来源](https://openaccess.thecvf.com/content/CVPR2025/html/Choi_Fine-Grained_Image-Text_Correspondence_with_Cost_Aggregation_for_Open-Vocabulary_Part_Segmentation_CVPR_2025_paper.html)。
- [官方实现](https://github.com/kaist-cvml/part-catseg)：已核对官方实现目录：baselines、configs、datasets、open_clip、requirements.txt、train_net.py。未独立运行或验证外部权重下载。
