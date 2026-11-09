---
paper_id: pbaps
title: Open-Vocabulary Part Segmentation via Progressive and Boundary-Aware Strategy
short_name: PBAPS
authors:
- Xinlong Li
- Di Lin
- Shaoyiyi Gao
- Jiaxin Li
- Ruonan Liu
- Qing Guo
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
datasets:
- ADE20K
paper_url: https://www.proceedings.com/content/085/085713-2136open.pdf
publication_url: https://papers.neurips.cc/paper_files/paper/2025/hash/5c186016d0844767209dc36e9e61441b-Abstract-Conference.html
code_status: public
code_url: https://github.com/TJU-IDVLab/PBAPS
code_details: 已核对官方实现目录：generate prototype、model、requirements.txt。未独立运行或验证外部权重下载。
content_status: index
checked_on: '2026-11-09'
module_checked_on: '2026-11-09'
summary: 先按对象到部件层级分割；BAR 根据类别不确定性定位歧义边界，利用高置信上下文增强这些区域的特征，并适配当前图像的部件原型后重新分类。
sources:
- url: https://papers.neurips.cc/paper_files/paper/2025/hash/5c186016d0844767209dc36e9e61441b-Abstract-Conference.html
  locator: 正式发表来源：出版页面／作者项目的会议说明
- url: https://www.proceedings.com/content/085/085713-2136open.pdf
  locator: 方法部分；Figure 4（PDF 第 6 页）；实验 Table 2（PDF 第 8 页）
- url: https://github.com/TJU-IDVLab/PBAPS
  locator: 官方 README、目录与开放范围；未独立运行
figures:
- id: fig4
  label: Figure 4
  asset: assets/figures/pbaps-fig4.png
  page: 6
  version: 作者公开 PDF（以文件 SHA256 固定版本）
  source_url: https://www.proceedings.com/content/085/085713-2136open.pdf
  source_sha256: 33b95222ce7650171b313a30221dedcbef477d85ecf677ce533fe163cdc9ea61
  clip_pdf_points:
  - 107
  - 545
  - 506
  - 644.009
methods:
- id: semantic-operation
  track: vocabulary
  problems:
  - regions
  - reliability
  - alignment
  title: 不确定边界部件细化
  question: 语义相连的部件边界怎样细分？
  operation: 先按对象到部件层级分割；BAR 根据类别不确定性定位歧义边界，利用高置信上下文增强这些区域的特征，并适配当前图像的部件原型后重新分类。
  input: 对象区域、部件特征／原型与预测不确定性
  output: 细化部件边界及掩码
  stage: 免分割训练的逐图推理
  supervision: 预训练模型及生成的视觉原型，无目标部件训练标签
  origin: proposed
  origin_note: 本文设计的不确定边界部件细化流程；所用预训练模型、通用投影及基础算子沿用已有方法，不计作本文新提出。
  evidence:
  - url: https://www.proceedings.com/content/085/085713-2136open.pdf
    locator: 方法部分；Figure 4（PDF 第 6 页）；实验 Table 2（PDF 第 8 页）
  figure: fig4
  figure_guide: 看 Boundary-Aware Refinement 中歧义区、高置信上下文与原型更新的对应。
  depicted: true
  route:
  - 预训练视觉语言特征
  - 不确定边界部件细化
  - 像素／区域类别表示
  - 开放词汇分割
  result_tables:
  - table2
results:
- id: table2
  label: Table 2
  asset: assets/results/pbaps-table2.png
  page: 8
  version: 作者公开 PDF（以文件 SHA256 固定版本）
  source_url: https://www.proceedings.com/content/085/085713-2136open.pdf
  source_sha256: 33b95222ce7650171b313a30221dedcbef477d85ecf677ce533fe163cdc9ea61
  clip_pdf_points:
  - 107
  - 440
  - 506
  - 595
  title: PBAPS：主要实验结果
  setting: Pascal-Part-116、ADE20K-Part-234、PartImageNet；保留复测星号。
  metrics: mIoU／bIoU ↑
  reading: mIoU 和边界 IoU 分开看；同时核对所用原型与先验。
---

# PBAPS

本页按研究问题提取相关操作；模块图、输入输出、证据和主要结果表在上方展开查看。

## 研究问题

语义相连的部件边界怎样细分？

## 相关操作

先按对象到部件层级分割；BAR 根据类别不确定性定位歧义边界，利用高置信上下文增强这些区域的特征，并适配当前图像的部件原型后重新分类。

## 实验阅读

Pascal-Part-116、ADE20K-Part-234、PartImageNet；保留复测星号。 mIoU 和边界 IoU 分开看；同时核对所用原型与先验。 主表是整体系统结果，单一模块的贡献需结合原文消融。

## 原文依据

- [本次阅读的原文版本](https://www.proceedings.com/content/085/085713-2136open.pdf)：方法部分；Figure 4（PDF 第 6 页）；实验 Table 2（PDF 第 8 页）。
- [正式发表来源](https://papers.neurips.cc/paper_files/paper/2025/hash/5c186016d0844767209dc36e9e61441b-Abstract-Conference.html)。
- [官方实现](https://github.com/TJU-IDVLab/PBAPS)：已核对官方实现目录：generate prototype、model、requirements.txt。未独立运行或验证外部权重下载。
