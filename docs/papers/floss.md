---
paper_id: floss
title: 'FLOSS: Free Lunch in Open-vocabulary Semantic Segmentation'
short_name: FLOSS
authors:
- Benigmim, Yasser
- Fahes, Mohammad
- Vu, Tuan-Hung
- Bursuc, Andrei
- de Charette, Raoul
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
datasets: []
paper_url: https://openaccess.thecvf.com/content/ICCV2025/papers/Benigmim_FLOSS_Free_Lunch_in_Open-vocabulary_Semantic_Segmentation_ICCV_2025_paper.pdf
publication_url: https://openaccess.thecvf.com/content/ICCV2025/html/Benigmim_FLOSS_Free_Lunch_in_Open-vocabulary_Semantic_Segmentation_ICCV_2025_paper.html
code_status: public
code_url: https://github.com/yasserben/FLOSS
code_details: 已核对官方实现目录：checkpoints、configs、img、mmseg、my_utils、notebooks。未独立运行或验证外部权重下载。
content_status: index
checked_on: '2026-11-09'
module_checked_on: '2026-11-09'
summary: 在无标签图像上分别评估单模板分类器的逐类预测熵，为每个类别选择低熵的模板专家；再融合各类别专家的预测，替代不区分类别的模板平均。
sources:
- url: https://openaccess.thecvf.com/content/ICCV2025/html/Benigmim_FLOSS_Free_Lunch_in_Open-vocabulary_Semantic_Segmentation_ICCV_2025_paper.html
  locator: 正式发表来源：出版页面／作者项目的会议说明
- url: https://openaccess.thecvf.com/content/ICCV2025/papers/Benigmim_FLOSS_Free_Lunch_in_Open-vocabulary_Semantic_Segmentation_ICCV_2025_paper.pdf
  locator: 方法部分；Figure 2（PDF 第 4 页）；实验 Table 1（PDF 第 5 页）
- url: https://github.com/yasserben/FLOSS
  locator: 官方 README、目录与开放范围；未独立运行
figures:
- id: fig2
  label: Figure 2
  asset: assets/figures/floss-fig2.png
  page: 4
  version: ICCV 2025 出版方正式版
  source_url: https://openaccess.thecvf.com/content/ICCV2025/papers/Benigmim_FLOSS_Free_Lunch_in_Open-vocabulary_Semantic_Segmentation_ICCV_2025_paper.pdf
  source_sha256: f564593039c588d406166cdf044f19c32ef1e8224658f7041c4097a36728e813
  clip_pdf_points:
  - 45
  - 45
  - 567
  - 186.916
methods:
- id: semantic-operation
  track: vocabulary
  problems:
  - prompt
  - reliability
  - unseen
  title: 类别专家提示选择
  question: 为何所有文本模板平均后反而不准？
  operation: 在无标签图像上分别评估单模板分类器的逐类预测熵，为每个类别选择低熵的模板专家；再融合各类别专家的预测，替代不区分类别的模板平均。
  input: 无标签图像、类别名与多种文本模板
  output: 逐类模板专家和融合像素分数
  stage: 无标签专家选择及分割推理
  supervision: 冻结基础分割器；无类别标签的图像集合
  origin: proposed
  origin_note: 本文设计的类别专家提示选择流程；所用预训练模型、通用投影及基础算子沿用已有方法，不计作本文新提出。
  evidence:
  - url: https://openaccess.thecvf.com/content/ICCV2025/papers/Benigmim_FLOSS_Free_Lunch_in_Open-vocabulary_Semantic_Segmentation_ICCV_2025_paper.pdf
    locator: 方法部分；Figure 2（PDF 第 4 页）；实验 Table 1（PDF 第 5 页）
  figure: fig2
  figure_guide: 看 estimated class-experts 与右侧 entropy-based template selection，不把 Oracle experts 当可用监督。
  depicted: true
  route:
  - 多模态语言提示
  - 类别专家提示选择
  - 像素／区域类别表示
  - 开放词汇分割
  result_tables:
  - table1
results:
- id: table1
  label: Table 1
  asset: assets/results/floss-table1.png
  page: 5
  version: ICCV 2025 出版方正式版
  source_url: https://openaccess.thecvf.com/content/ICCV2025/papers/Benigmim_FLOSS_Free_Lunch_in_Open-vocabulary_Semantic_Segmentation_ICCV_2025_paper.pdf
  source_sha256: f564593039c588d406166cdf044f19c32ef1e8224658f7041c4097a36728e813
  clip_pdf_points:
  - 309
  - 55
  - 558
  - 323
  title: FLOSS：主要实验结果
  setting: 八基准、多个基础分割器；比较原模板平均与 FLOSS 接入结果。
  metrics: mIoU ↑
  reading: Oracle 为理想参照，实际方法看 estimated experts 行。
---

# FLOSS

本页按研究问题提取相关操作；模块图、输入输出、证据和主要结果表在上方展开查看。

## 研究问题

为何所有文本模板平均后反而不准？

## 相关操作

在无标签图像上分别评估单模板分类器的逐类预测熵，为每个类别选择低熵的模板专家；再融合各类别专家的预测，替代不区分类别的模板平均。

## 实验阅读

八基准、多个基础分割器；比较原模板平均与 FLOSS 接入结果。 Oracle 为理想参照，实际方法看 estimated experts 行。 主表是整体系统结果，单一模块的贡献需结合原文消融。

## 原文依据

- [本次阅读的原文版本](https://openaccess.thecvf.com/content/ICCV2025/papers/Benigmim_FLOSS_Free_Lunch_in_Open-vocabulary_Semantic_Segmentation_ICCV_2025_paper.pdf)：方法部分；Figure 2（PDF 第 4 页）；实验 Table 1（PDF 第 5 页）。
- [正式发表来源](https://openaccess.thecvf.com/content/ICCV2025/html/Benigmim_FLOSS_Free_Lunch_in_Open-vocabulary_Semantic_Segmentation_ICCV_2025_paper.html)。
- [官方实现](https://github.com/yasserben/FLOSS)：已核对官方实现目录：checkpoints、configs、img、mmseg、my_utils、notebooks。未独立运行或验证外部权重下载。
