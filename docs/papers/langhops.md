---
paper_id: langhops
title: 'LangHOPS: Language Grounded Hierarchical Open-Vocabulary Part Segmentation'
short_name: LangHOPS
authors:
- Yang Miao
- Jan-Nico Zaech
- Xi Wang
- Fabien Despinoy
- Danda Pani Paudel
- Luc Van Gool
year: 2025
preprint_date: unknown
venue: NeurIPS
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
paper_url: https://arxiv.org/pdf/2510.25263v3
publication_url: https://papers.neurips.cc/paper_files/paper/2025/hash/fc797c61eb18f7b3ce9a74af0ef0d876-Abstract-Conference.html
code_status: public
code_url: https://github.com/y9miao/LangHOPS-release
code_details: 已核对官方实现目录：LICENSE.txt、LICENSES_THIRD_PARTY.md、configs、dataset_preprocess、datasets、demo。未独立运行或验证外部权重下载。
content_status: index
checked_on: '2026-11-09'
module_checked_on: '2026-11-09'
summary: 先建立语言描述的对象—部件关系，通过 MLLM 解析层级并细化部件查询；对象与部件分割模块利用这些语义关联处理多粒度概念，而非单纯从视觉对象查询硬分组。
sources:
- url: https://papers.neurips.cc/paper_files/paper/2025/hash/fc797c61eb18f7b3ce9a74af0ef0d876-Abstract-Conference.html
  locator: 正式发表来源：出版页面／作者项目的会议说明
- url: https://arxiv.org/pdf/2510.25263v3
  locator: 方法部分；Figure 2（PDF 第 4 页）；实验 Table 1（PDF 第 7 页）
- url: https://github.com/y9miao/LangHOPS-release
  locator: 官方 README、目录与开放范围；未独立运行
figures:
- id: fig2
  label: Figure 2
  asset: assets/figures/langhops-fig2.png
  page: 4
  version: arXiv 2510.25263v3
  source_url: https://arxiv.org/pdf/2510.25263v3
  source_sha256: fa179db653cc2977faff86498657206b31c7171eca0e878a683c622e2520a596
  clip_pdf_points:
  - 45
  - 45
  - 567
  - 254.475
methods:
- id: semantic-operation
  track: vocabulary
  problems:
  - prompt
  - alignment
  - regions
  title: 语言层级与部件查询
  question: 对象—部件层级怎样在语言空间表达？
  operation: 先建立语言描述的对象—部件关系，通过 MLLM 解析层级并细化部件查询；对象与部件分割模块利用这些语义关联处理多粒度概念，而非单纯从视觉对象查询硬分组。
  input: 图像、对象／部件候选词及语言层级
  output: 层级对象与部件实例掩码
  stage: 分割训练及层级查询推理
  supervision: 对象／部件实例标注及 MLLM 先验
  origin: proposed
  origin_note: 本文设计的语言层级与部件查询流程；所用预训练模型、通用投影及基础算子沿用已有方法，不计作本文新提出。
  evidence:
  - url: https://arxiv.org/pdf/2510.25263v3
    locator: 方法部分；Figure 2（PDF 第 4 页）；实验 Table 1（PDF 第 7 页）
  figure: fig2
  figure_guide: 看对象分割输出、语言层级和 MLLM-driven part query refinement 的连接。
  depicted: true
  route:
  - 多模态语言提示
  - 语言层级与部件查询
  - 像素／区域类别表示
  - 开放词汇分割
  result_tables:
  - table1
results:
- id: table1
  label: Table 1
  asset: assets/results/langhops-table1.png
  page: 7
  version: arXiv 2510.25263v3
  source_url: https://arxiv.org/pdf/2510.25263v3
  source_sha256: fa179db653cc2977faff86498657206b31c7171eca0e878a683c622e2520a596
  clip_pdf_points:
  - 107
  - 70
  - 506
  - 208
  title: LangHOPS：主要实验结果
  setting: PascalPart-116→PartImageNet 跨数据集与 PartImageNet 域内实例分割。
  metrics: AP ↑
  reading: 跨域和域内分开比较；零样本语义 h-IoU 另见 Table 3。
---

# LangHOPS

本页按研究问题提取相关操作；模块图、输入输出、证据和主要结果表在上方展开查看。

## 研究问题

对象—部件层级怎样在语言空间表达？

## 相关操作

先建立语言描述的对象—部件关系，通过 MLLM 解析层级并细化部件查询；对象与部件分割模块利用这些语义关联处理多粒度概念，而非单纯从视觉对象查询硬分组。

## 实验阅读

PascalPart-116→PartImageNet 跨数据集与 PartImageNet 域内实例分割。 跨域和域内分开比较；零样本语义 h-IoU 另见 Table 3。 主表是整体系统结果，单一模块的贡献需结合原文消融。

## 原文依据

- [本次阅读的原文版本](https://arxiv.org/pdf/2510.25263v3)：方法部分；Figure 2（PDF 第 4 页）；实验 Table 1（PDF 第 7 页）。
- [正式发表来源](https://papers.neurips.cc/paper_files/paper/2025/hash/fc797c61eb18f7b3ce9a74af0ef0d876-Abstract-Conference.html)。
- [官方实现](https://github.com/y9miao/LangHOPS-release)：已核对官方实现目录：LICENSE.txt、LICENSES_THIRD_PARTY.md、configs、dataset_preprocess、datasets、demo。未独立运行或验证外部权重下载。
