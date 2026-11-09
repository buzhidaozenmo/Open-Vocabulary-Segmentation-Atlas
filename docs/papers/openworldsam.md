---
paper_id: openworldsam
title: 'OpenWorldSAM: Extending SAM2 for Universal Image Segmentation with Language Prompts'
short_name: OpenWorldSAM
authors:
- Shiting Xiao
- Rishabh Kabra
- Yuhang Li
- Donghyun Lee
- João Carreira
- Priyadarshini Panda
year: 2025
preprint_date: unknown
venue: NeurIPS
publication_status: published
primary_direction: 2d
modalities:
- image
task_setting: open_vocabulary
task_types:
- panoptic
techniques:
- semantic_alignment
datasets:
- COCO
paper_url: https://arxiv.org/pdf/2507.05427v4
publication_url: https://papers.neurips.cc/paper_files/paper/2025/hash/32fa3ddb3a6350cd1ab68e25f1c59982-Abstract-Conference.html
code_status: public
code_url: https://github.com/GinnyXiao/OpenWorldSAM
code_details: 已核对官方实现目录：DATASETS.md、LICENSE.txt、__init__.py、configs、datasets、demo。未独立运行或验证外部权重下载。
content_status: index
checked_on: '2026-11-09'
module_checked_on: '2026-11-09'
summary: 冻结 SAM2 与视觉语言模型，将多模态语义投影到提示路径；使用位置 tie-breaker 嵌入和交叉注意力区分同一语义下不同实例，使类别名称和句子提示均可产生掩码。
sources:
- url: https://papers.neurips.cc/paper_files/paper/2025/hash/32fa3ddb3a6350cd1ab68e25f1c59982-Abstract-Conference.html
  locator: 正式发表来源：出版页面／作者项目的会议说明
- url: https://arxiv.org/pdf/2507.05427v4
  locator: 方法部分；Figure 4（PDF 第 4 页）；实验 Table 1（PDF 第 7 页）
- url: https://github.com/GinnyXiao/OpenWorldSAM
  locator: 官方 README、目录与开放范围；未独立运行
figures:
- id: fig4
  label: Figure 4
  asset: assets/figures/openworldsam-fig4.png
  page: 4
  version: arXiv 2507.05427v4
  source_url: https://arxiv.org/pdf/2507.05427v4
  source_sha256: 2732e3921bd77d496931602a55c959ff3df4d75d59cf0b7cb2bfb3617a2d6855
  clip_pdf_points:
  - 45
  - 45
  - 567
  - 246.819
methods:
- id: semantic-operation
  track: vocabulary
  problems:
  - prompt
  - alignment
  title: 语言提示注入 SAM2
  question: SAM2 如何接收文本并分开同类实例？
  operation: 冻结 SAM2 与视觉语言模型，将多模态语义投影到提示路径；使用位置 tie-breaker 嵌入和交叉注意力区分同一语义下不同实例，使类别名称和句子提示均可产生掩码。
  input: 图像、类别／句子提示、冻结 VLM 与 SAM2 特征
  output: 文本条件实例／语义掩码
  stage: 轻量适配训练及分割推理
  supervision: COCO-stuff 分割训练数据；预训练 SAM2 与 VLM
  origin: proposed
  origin_note: 本文设计的语言提示注入 SAM2流程；所用预训练模型、通用投影及基础算子沿用已有方法，不计作本文新提出。
  evidence:
  - url: https://arxiv.org/pdf/2507.05427v4
    locator: 方法部分；Figure 4（PDF 第 4 页）；实验 Table 1（PDF 第 7 页）
  figure: fig4
  figure_guide: 看多模态编码器的输入输出、投影提示以及 positional tie-breaker 的对应分支。
  depicted: true
  route:
  - 多模态语言提示
  - 语言提示注入 SAM2
  - 像素／区域类别表示
  - 开放词汇分割
  result_tables:
  - table1
results:
- id: table1
  label: Table 1
  asset: assets/results/openworldsam-table1.png
  page: 7
  version: arXiv 2507.05427v4
  source_url: https://arxiv.org/pdf/2507.05427v4
  source_sha256: 2732e3921bd77d496931602a55c959ff3df4d75d59cf0b7cb2bfb3617a2d6855
  clip_pdf_points:
  - 107
  - 72
  - 506
  - 311
  title: OpenWorldSAM：主要实验结果
  setting: 零样本开放词汇多数据集评测；COCO 列保留任务专用模型差异。
  metrics: mIoU／PQ／AP ↑，逐任务分列
  reading: 语义、实例和全景指标分开比较；Oracle-Prompts 是另一个协议。
---

# OpenWorldSAM

本页按研究问题提取相关操作；模块图、输入输出、证据和主要结果表在上方展开查看。

## 研究问题

SAM2 如何接收文本并分开同类实例？

## 相关操作

冻结 SAM2 与视觉语言模型，将多模态语义投影到提示路径；使用位置 tie-breaker 嵌入和交叉注意力区分同一语义下不同实例，使类别名称和句子提示均可产生掩码。

## 实验阅读

零样本开放词汇多数据集评测；COCO 列保留任务专用模型差异。 语义、实例和全景指标分开比较；Oracle-Prompts 是另一个协议。 主表是整体系统结果，单一模块的贡献需结合原文消融。

## 原文依据

- [本次阅读的原文版本](https://arxiv.org/pdf/2507.05427v4)：方法部分；Figure 4（PDF 第 4 页）；实验 Table 1（PDF 第 7 页）。
- [正式发表来源](https://papers.neurips.cc/paper_files/paper/2025/hash/32fa3ddb3a6350cd1ab68e25f1c59982-Abstract-Conference.html)。
- [官方实现](https://github.com/GinnyXiao/OpenWorldSAM)：已核对官方实现目录：DATASETS.md、LICENSE.txt、__init__.py、configs、datasets、demo。未独立运行或验证外部权重下载。
