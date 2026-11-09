---
paper_id: resanything
title: 'RESAnything: Attribute Prompting for Arbitrary Referring Segmentation'
short_name: RESAnything
authors:
- Ruiqi Wang
- Hao Zhang
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
paper_url: https://arxiv.org/pdf/2505.02867v1
publication_url: https://papers.neurips.cc/paper_files/paper/2025/hash/608fe7e32f7b773545cc1d656a0fdc98-Abstract-Conference.html
code_status: public
code_url: https://github.com/suikei-wang/RESAnything
code_details: 已核对官方实现目录：config.py、config.yaml、demo.py、demo_batch.py、generation.py、output。未独立运行或验证外部权重下载。
content_status: index
checked_on: '2026-11-09'
module_checked_on: '2026-11-09'
summary: 先用 SAM 生成候选区域，再以多种可视提示让 MLLM 为候选和指代表达生成属性描述；借助属性链推理比较候选与目标，选出满足功能、材质、风格等条件的区域。
sources:
- url: https://papers.neurips.cc/paper_files/paper/2025/hash/608fe7e32f7b773545cc1d656a0fdc98-Abstract-Conference.html
  locator: 正式发表来源：出版页面／作者项目的会议说明
- url: https://arxiv.org/pdf/2505.02867v1
  locator: 方法部分；Figure 3（PDF 第 4 页）；实验 Table 3（PDF 第 7 页）
- url: https://github.com/suikei-wang/RESAnything
  locator: 官方 README、目录与开放范围；未独立运行
figures:
- id: fig3
  label: Figure 3
  asset: assets/figures/resanything-fig3.png
  page: 4
  version: arXiv 2505.02867v1
  source_url: https://arxiv.org/pdf/2505.02867v1
  source_sha256: d68a143b78e3a7767a917f9bf03fc299b63edcb3295736f2c14db0e6ce0e4541
  clip_pdf_points:
  - 45
  - 45
  - 567
  - 183.822
methods:
- id: semantic-operation
  track: vocabulary
  problems:
  - prompt
  - alignment
  - regions
  title: 属性提示与候选匹配
  question: 隐式属性描述怎样匹配到具体对象或部件？
  operation: 先用 SAM 生成候选区域，再以多种可视提示让 MLLM 为候选和指代表达生成属性描述；借助属性链推理比较候选与目标，选出满足功能、材质、风格等条件的区域。
  input: 图像、指代表达、SAM 候选和可视提示
  output: 满足属性描述的对象／部件掩码
  stage: 免任务训练的属性推理与分割
  supervision: 预训练 SAM、MLLM 及视觉语言模型
  origin: proposed
  origin_note: 本文设计的属性提示与候选匹配流程；所用预训练模型、通用投影及基础算子沿用已有方法，不计作本文新提出。
  evidence:
  - url: https://arxiv.org/pdf/2505.02867v1
    locator: 方法部分；Figure 3（PDF 第 4 页）；实验 Table 3（PDF 第 7 页）
  figure: fig3
  figure_guide: 看 reference attributes 与 candidate attributes 两支，不将属性生成等同于类别监督。
  depicted: true
  route:
  - 多模态语言提示
  - 属性提示与候选匹配
  - 像素／区域类别表示
  - 开放词汇分割
  result_tables:
  - table3
results:
- id: table3
  label: Table 3
  asset: assets/results/resanything-table3.png
  page: 7
  version: arXiv 2505.02867v1
  source_url: https://arxiv.org/pdf/2505.02867v1
  source_sha256: d68a143b78e3a7767a917f9bf03fc299b63edcb3295736f2c14db0e6ce0e4541
  clip_pdf_points:
  - 55
  - 399
  - 299
  - 476
  title: RESAnything：主要实验结果
  setting: ABO-Image-ARES 任意属性指代分割，含对象及部件表达。
  metrics: cIoU ↑
  reading: 这是属性指代分割；与纯类别词表分割分开比较。
---

# RESAnything

本页按研究问题提取相关操作；模块图、输入输出、证据和主要结果表在上方展开查看。

## 研究问题

隐式属性描述怎样匹配到具体对象或部件？

## 相关操作

先用 SAM 生成候选区域，再以多种可视提示让 MLLM 为候选和指代表达生成属性描述；借助属性链推理比较候选与目标，选出满足功能、材质、风格等条件的区域。

## 实验阅读

ABO-Image-ARES 任意属性指代分割，含对象及部件表达。 这是属性指代分割；与纯类别词表分割分开比较。 主表是整体系统结果，单一模块的贡献需结合原文消融。

## 原文依据

- [本次阅读的原文版本](https://arxiv.org/pdf/2505.02867v1)：方法部分；Figure 3（PDF 第 4 页）；实验 Table 3（PDF 第 7 页）。
- [正式发表来源](https://papers.neurips.cc/paper_files/paper/2025/hash/608fe7e32f7b773545cc1d656a0fdc98-Abstract-Conference.html)。
- [官方实现](https://github.com/suikei-wang/RESAnything)：已核对官方实现目录：config.py、config.yaml、demo.py、demo_batch.py、generation.py、output。未独立运行或验证外部权重下载。
