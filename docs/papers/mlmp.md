---
paper_id: mlmp
title: Test-Time Adaptation of Vision-Language Models for Open-Vocabulary Semantic Segmentation
short_name: MLMP
authors:
- Mehrdad Noori
- David Osowiechi
- Gustavo Adolfo Vargas Hakim
- Ali Bahri
- Moslem Yazdanpanah
- Sahar Dastani
- Farzad Beizaee
- Ismail Ben Ayed
- Christian Desrosiers
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
paper_url: https://arxiv.org/pdf/2505.21844v2
publication_url: https://papers.neurips.cc/paper_files/paper/2025/hash/6c5b82193c5d8e6aa5806239676ddc97-Abstract-Conference.html
code_status: public
code_url: https://github.com/dosowiechi/MLMP
code_details: 已核对官方实现目录：LICENCE、adapt、bash、figures、main.py、ovss。未独立运行或验证外部权重下载。
content_status: index
checked_on: '2026-11-09'
module_checked_on: '2026-11-09'
summary: 在测试图上同时使用多种文本模板与视觉中间层，针对全局 CLS 和局部像素类别分布最小化熵；再按层置信度融合，实现无需标签的分割适配，而不是直接套用分类 TTA。
sources:
- url: https://papers.neurips.cc/paper_files/paper/2025/hash/6c5b82193c5d8e6aa5806239676ddc97-Abstract-Conference.html
  locator: 正式发表来源：出版页面／作者项目的会议说明
- url: https://arxiv.org/pdf/2505.21844v2
  locator: 方法部分；Figure 2（PDF 第 5 页）；实验 Table 5（PDF 第 9 页）
- url: https://github.com/dosowiechi/MLMP
  locator: 官方 README、目录与开放范围；未独立运行
figures:
- id: fig2
  label: Figure 2
  asset: assets/figures/mlmp-fig2.png
  page: 5
  version: arXiv 2505.21844v2
  source_url: https://arxiv.org/pdf/2505.21844v2
  source_sha256: 30911a11e6b890b2bf466adb8e33e6f1ac53b82c50b56efb7d8749cef1c82ac7
  clip_pdf_points:
  - 45
  - 45
  - 567
  - 279.656
methods:
- id: semantic-operation
  track: vocabulary
  problems:
  - prompt
  - alignment
  - reliability
  title: 多层多提示测试适配
  question: 没有目标标签时如何稳定适配像素语义？
  operation: 在测试图上同时使用多种文本模板与视觉中间层，针对全局 CLS 和局部像素类别分布最小化熵；再按层置信度融合，实现无需标签的分割适配，而不是直接套用分类 TTA。
  input: 测试图、多个文本模板和视觉中间层
  output: 适配后的像素类别分数
  stage: 每批测试适配及评测
  supervision: 无目标域标签；预训练视觉语言模型
  origin: proposed
  origin_note: 本文设计的多层多提示测试适配流程；所用预训练模型、通用投影及基础算子沿用已有方法，不计作本文新提出。
  evidence:
  - url: https://arxiv.org/pdf/2505.21844v2
    locator: 方法部分；Figure 2（PDF 第 5 页）；实验 Table 5（PDF 第 9 页）
  figure: fig2
  figure_guide: 沿 Adaptation Phase 的多提示、多层与全局／局部损失，再看 Evaluation Phase。
  depicted: true
  route:
  - 多模态语言提示
  - 多层多提示测试适配
  - 像素／区域类别表示
  - 开放词汇分割
  result_tables:
  - table5
results:
- id: table5
  label: Table 5
  asset: assets/results/mlmp-table5.png
  page: 9
  version: arXiv 2505.21844v2
  source_url: https://arxiv.org/pdf/2505.21844v2
  source_sha256: 30911a11e6b890b2bf466adb8e33e6f1ac53b82c50b56efb7d8749cef1c82ac7
  clip_pdf_points:
  - 107
  - 60
  - 506
  - 374
  title: MLMP：主要实验结果
  setting: 多数据集 clean／corrupt 测试；保留骨干和各适配方法缺失值。
  metrics: mIoU ↑
  reading: 这是测试时参数优化，需要同时看适配成本；不能标成纯冻结前向。
---

# MLMP

本页按研究问题提取相关操作；模块图、输入输出、证据和主要结果表在上方展开查看。

## 研究问题

没有目标标签时如何稳定适配像素语义？

## 相关操作

在测试图上同时使用多种文本模板与视觉中间层，针对全局 CLS 和局部像素类别分布最小化熵；再按层置信度融合，实现无需标签的分割适配，而不是直接套用分类 TTA。

## 实验阅读

多数据集 clean／corrupt 测试；保留骨干和各适配方法缺失值。 这是测试时参数优化，需要同时看适配成本；不能标成纯冻结前向。 主表是整体系统结果，单一模块的贡献需结合原文消融。

## 原文依据

- [本次阅读的原文版本](https://arxiv.org/pdf/2505.21844v2)：方法部分；Figure 2（PDF 第 5 页）；实验 Table 5（PDF 第 9 页）。
- [正式发表来源](https://papers.neurips.cc/paper_files/paper/2025/hash/6c5b82193c5d8e6aa5806239676ddc97-Abstract-Conference.html)。
- [官方实现](https://github.com/dosowiechi/MLMP)：已核对官方实现目录：LICENCE、adapt、bash、figures、main.py、ovss。未独立运行或验证外部权重下载。
