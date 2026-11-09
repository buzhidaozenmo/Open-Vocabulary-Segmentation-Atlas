---
paper_id: seg4diff
title: 'Seg4Diff: Unveiling Open-Vocabulary Semantic Segmentation in Text-to-Image Diffusion Transformers'
short_name: Seg4Diff
authors:
- Chaehyun Kim
- Heeseong Shin
- Eunbeen Hong
- Heeji Yoon
- Anurag Arnab
- Paul Hongsuck Seo
- Sunghwan Hong
- Seungryong Kim
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
paper_url: https://arxiv.org/pdf/2509.18096v1
publication_url: https://papers.neurips.cc/paper_files/paper/2025/hash/67b87de31003d4f56e3312a2e04b479d-Abstract-Conference.html
code_status: public
code_url: https://github.com/cvlab-kaist/Seg4Diff
code_details: 已核对官方实现目录：INSTALL.md、configs、datasets、demo、diffusers、eval_flux.sh。未独立运行或验证外部权重下载。
content_status: index
checked_on: '2026-11-09'
module_checked_on: '2026-11-09'
summary: 在多模态扩散 Transformer 中定位语义 grounding expert 层，取图像到文本的注意力作为类别空间响应；进一步用 MAGNET 的轻量 LoRA 掩码对齐改善区域对应，同时保留生成能力。
sources:
- url: https://papers.neurips.cc/paper_files/paper/2025/hash/67b87de31003d4f56e3312a2e04b479d-Abstract-Conference.html
  locator: 正式发表来源：出版页面／作者项目的会议说明
- url: https://arxiv.org/pdf/2509.18096v1
  locator: 方法部分；Figure 7（PDF 第 7 页）；实验 Table 1（PDF 第 9 页）
- url: https://github.com/cvlab-kaist/Seg4Diff
  locator: 官方 README、目录与开放范围；未独立运行
figures:
- id: fig7
  label: Figure 7
  asset: assets/figures/seg4diff-fig7.png
  page: 7
  version: arXiv 2509.18096v1
  source_url: https://arxiv.org/pdf/2509.18096v1
  source_sha256: 9c8e85cc7acb153ed176374337dc98d45fbb20fde4825c0c0a8b5d7502d888cc
  clip_pdf_points:
  - 45
  - 45
  - 567
  - 162.667
methods:
- id: semantic-operation
  track: vocabulary
  problems:
  - alignment
  - regions
  title: 扩散图文注意定位
  question: 文生图模型内部的语义怎样直接形成掩码？
  operation: 在多模态扩散 Transformer 中定位语义 grounding expert 层，取图像到文本的注意力作为类别空间响应；进一步用 MAGNET 的轻量 LoRA 掩码对齐改善区域对应，同时保留生成能力。
  input: 图像、类别文本及 MM-DiT 跨模态注意图
  output: 语义响应掩码与对齐后的扩散模型
  stage: 零样本注意读取；可选掩码对齐微调
  supervision: 冻结扩散预训练；MAGNET 另需图像掩码训练数据
  origin: proposed
  origin_note: 本文设计的扩散图文注意定位流程；所用预训练模型、通用投影及基础算子沿用已有方法，不计作本文新提出。
  evidence:
  - url: https://arxiv.org/pdf/2509.18096v1
    locator: 方法部分；Figure 7（PDF 第 7 页）；实验 Table 1（PDF 第 9 页）
  figure: fig7
  figure_guide: 沿 Figure 7 的 Image-to-Text attention → segmentation maps 阅读；增强版另看 mask alignment。
  depicted: true
  route:
  - 预训练视觉语言特征
  - 扩散图文注意定位
  - 像素／区域类别表示
  - 开放词汇分割
  result_tables:
  - table1
results:
- id: table1
  label: Table 1
  asset: assets/results/seg4diff-table1.png
  page: 9
  version: arXiv 2509.18096v1
  source_url: https://arxiv.org/pdf/2509.18096v1
  source_sha256: 9c8e85cc7acb153ed176374337dc98d45fbb20fde4825c0c0a8b5d7502d888cc
  clip_pdf_points:
  - 107
  - 60
  - 296
  - 201
  title: Seg4Diff：主要实验结果
  setting: 开放词汇语义分割主表；区分基础 MM-DiT 与掩码对齐后的版本。
  metrics: mIoU ↑
  reading: 生成质量表与分割主表分开；注意增强版本使用了额外对齐训练。
---

# Seg4Diff

本页按研究问题提取相关操作；模块图、输入输出、证据和主要结果表在上方展开查看。

## 研究问题

文生图模型内部的语义怎样直接形成掩码？

## 相关操作

在多模态扩散 Transformer 中定位语义 grounding expert 层，取图像到文本的注意力作为类别空间响应；进一步用 MAGNET 的轻量 LoRA 掩码对齐改善区域对应，同时保留生成能力。

## 实验阅读

开放词汇语义分割主表；区分基础 MM-DiT 与掩码对齐后的版本。 生成质量表与分割主表分开；注意增强版本使用了额外对齐训练。 主表是整体系统结果，单一模块的贡献需结合原文消融。

## 原文依据

- [本次阅读的原文版本](https://arxiv.org/pdf/2509.18096v1)：方法部分；Figure 7（PDF 第 7 页）；实验 Table 1（PDF 第 9 页）。
- [正式发表来源](https://papers.neurips.cc/paper_files/paper/2025/hash/67b87de31003d4f56e3312a2e04b479d-Abstract-Conference.html)。
- [官方实现](https://github.com/cvlab-kaist/Seg4Diff)：已核对官方实现目录：INSTALL.md、configs、datasets、demo、diffusers、eval_flux.sh。未独立运行或验证外部权重下载。
