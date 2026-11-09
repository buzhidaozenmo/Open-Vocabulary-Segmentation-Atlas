---
paper_id: text4seg
title: 'Text4Seg: Reimagining Image Segmentation as Text Generation'
short_name: Text4Seg
authors:
- Mengcheng Lan
- Chaofeng Chen
- Yue Zhou
- Jiaxing Xu
- Yiping Ke
- Xinjiang Wang
- Litong Feng
- Wayne Zhang
year: 2025
preprint_date: unknown
venue: ICLR
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
paper_url: https://arxiv.org/pdf/2410.09855v2
publication_url: https://proceedings.iclr.cc/paper_files/paper/2025/file/04d8c25cbf0d5e1b70d64e672ac92637-Paper-Conference.pdf
code_status: public
code_url: https://github.com/mc-lan/Text4Seg
code_details: 已核对官方实现目录：LICENSE.txt、cog.yaml、llava、ms-swift、playground、predict.py。未独立运行或验证外部权重下载。
content_status: index
checked_on: '2026-11-09'
module_checked_on: '2026-11-09'
summary: 把图像网格的类别标签写成语义描述符序列，以语言自回归训练直接生成类别布局；行级游程编码压缩连续重复标签，生成后恢复为网格掩码并细化。
sources:
- url: https://proceedings.iclr.cc/paper_files/paper/2025/file/04d8c25cbf0d5e1b70d64e672ac92637-Paper-Conference.pdf
  locator: 正式发表来源：出版页面／作者项目的会议说明
- url: https://arxiv.org/pdf/2410.09855v2
  locator: 方法部分；Figure 3（PDF 第 4 页）；实验 Table 5（PDF 第 8 页）
- url: https://github.com/mc-lan/Text4Seg
  locator: 官方 README、目录与开放范围；未独立运行
figures:
- id: fig3
  label: Figure 3
  asset: assets/figures/text4seg-fig3.png
  page: 4
  version: arXiv 2410.09855v2
  source_url: https://arxiv.org/pdf/2410.09855v2
  source_sha256: 117101bf448f07bae857541cf302bbc684809c4bd71396565425f13295287083
  clip_pdf_points:
  - 107
  - 420
  - 506
  - 552.583
methods:
- id: semantic-operation
  track: vocabulary
  problems:
  - prompt
  - alignment
  - efficiency
  title: 语义描述符生成掩码
  question: 语言模型能否直接把分割写成文本？
  operation: 把图像网格的类别标签写成语义描述符序列，以语言自回归训练直接生成类别布局；行级游程编码压缩连续重复标签，生成后恢复为网格掩码并细化。
  input: 图像、语言任务提示及语义描述符序列
  output: 可解码的类别网格与分割图
  stage: 多模态语言模型训练与生成推理
  supervision: 分割／指代等指令训练数据，预训练 MLLM
  origin: proposed
  origin_note: 本文设计的语义描述符生成掩码流程；所用预训练模型、通用投影及基础算子沿用已有方法，不计作本文新提出。
  evidence:
  - url: https://arxiv.org/pdf/2410.09855v2
    locator: 方法部分；Figure 3（PDF 第 4 页）；实验 Table 5（PDF 第 8 页）
  figure: fig3
  figure_guide: 看 semantic descriptors 与 Row-wise RLE 的压缩／恢复对应。
  depicted: true
  route:
  - 多模态语言提示
  - 语义描述符生成掩码
  - 像素／区域类别表示
  - 开放词汇分割
  result_tables:
  - table5
results:
- id: table5
  label: Table 5
  asset: assets/results/text4seg-table5.png
  page: 8
  version: arXiv 2410.09855v2
  source_url: https://arxiv.org/pdf/2410.09855v2
  source_sha256: 117101bf448f07bae857541cf302bbc684809c4bd71396565425f13295287083
  clip_pdf_points:
  - 341
  - 503
  - 506
  - 665
  title: Text4Seg：主要实验结果
  setting: 开放词汇语义分割 Table 5，区别于主要指代分割实验。
  metrics: mIoU ↑
  reading: 当前表才是开放词汇类别分割；不能用 RefCOCO cIoU 代替其效果。
---

# Text4Seg

本页按研究问题提取相关操作；模块图、输入输出、证据和主要结果表在上方展开查看。

## 研究问题

语言模型能否直接把分割写成文本？

## 相关操作

把图像网格的类别标签写成语义描述符序列，以语言自回归训练直接生成类别布局；行级游程编码压缩连续重复标签，生成后恢复为网格掩码并细化。

## 实验阅读

开放词汇语义分割 Table 5，区别于主要指代分割实验。 当前表才是开放词汇类别分割；不能用 RefCOCO cIoU 代替其效果。 主表是整体系统结果，单一模块的贡献需结合原文消融。

## 原文依据

- [本次阅读的原文版本](https://arxiv.org/pdf/2410.09855v2)：方法部分；Figure 3（PDF 第 4 页）；实验 Table 5（PDF 第 8 页）。
- [正式发表来源](https://proceedings.iclr.cc/paper_files/paper/2025/file/04d8c25cbf0d5e1b70d64e672ac92637-Paper-Conference.pdf)。
- [官方实现](https://github.com/mc-lan/Text4Seg)：已核对官方实现目录：LICENSE.txt、cog.yaml、llava、ms-swift、playground、predict.py。未独立运行或验证外部权重下载。
