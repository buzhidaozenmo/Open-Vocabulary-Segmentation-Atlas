---
paper_id: eovseg
title: 'EOV-Seg: Efficient Open-Vocabulary Panoptic Segmentation'
short_name: EOV-Seg
authors:
- Niu, Hongwei
- Hu, Jie
- Lin, Jianghang
- Zhang, Shengchuan
year: 2025
preprint_date: unknown
venue: AAAI
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
- ADE20K
- COCO
paper_url: https://arxiv.org/pdf/2412.08628v2
publication_url: https://ojs.aaai.org/index.php/AAAI/article/view/32669
code_status: public
code_url: https://github.com/nhw649/EOV-Seg
code_details: 已核对官方实现目录：configs、datasets、demo、eov_seg、requirements.txt、resources。未独立运行或验证外部权重下载。
content_status: index
checked_on: '2026-11-09'
module_checked_on: '2026-11-09'
summary: VAS 根据文本语义从聚合视觉特征中选择相关信息，减少解码负担；TDEE 通过动态专家权重整合语义和空间嵌入，再使用轻量掩码解码器和文本分类完成全景分割。
sources:
- url: https://ojs.aaai.org/index.php/AAAI/article/view/32669
  locator: 正式发表来源：出版页面／作者项目的会议说明
- url: https://arxiv.org/pdf/2412.08628v2
  locator: 方法部分；Figure 4（PDF 第 4 页）；实验 Table 1（PDF 第 6 页）
- url: https://github.com/nhw649/EOV-Seg
  locator: 官方 README、目录与开放范围；未独立运行
figures:
- id: fig4
  label: Figure 4
  asset: assets/figures/eovseg-fig4.png
  page: 4
  version: arXiv 2412.08628v2
  source_url: https://arxiv.org/pdf/2412.08628v2
  source_sha256: d53a120a6450c4d6c1c31b453de8c82dbea8e304ac4bef92c8348092fb26f934
  clip_pdf_points:
  - 45
  - 45
  - 567
  - 236.205
methods:
- id: semantic-operation
  track: vocabulary
  problems:
  - alignment
  - efficiency
  title: 词汇感知特征选择
  question: 轻量解码器怎样获得足够的类别语义和空间线索？
  operation: VAS 根据文本语义从聚合视觉特征中选择相关信息，减少解码负担；TDEE 通过动态专家权重整合语义和空间嵌入，再使用轻量掩码解码器和文本分类完成全景分割。
  input: 图像、多尺度 CLIP、空间特征和文本词汇
  output: 空间语义增强的实例嵌入与全景掩码
  stage: 全景分割训练及推理
  supervision: COCO 全景标注与预训练 CLIP
  origin: proposed
  origin_note: 本文设计的词汇感知特征选择流程；所用预训练模型、通用投影及基础算子沿用已有方法，不计作本文新提出。
  evidence:
  - url: https://arxiv.org/pdf/2412.08628v2
    locator: 方法部分；Figure 4（PDF 第 4 页）；实验 Table 1（PDF 第 6 页）
  figure: fig4
  figure_guide: 看 VAS 词汇选择、TDEE 双路嵌入专家和 lightweight decoder。
  depicted: true
  route:
  - 预训练视觉语言特征
  - 词汇感知特征选择
  - 像素／区域类别表示
  - 开放词汇分割
  result_tables:
  - table1
results:
- id: table1
  label: Table 1
  asset: assets/results/eovseg-table1.png
  page: 6
  version: arXiv 2412.08628v2
  source_url: https://arxiv.org/pdf/2412.08628v2
  source_sha256: d53a120a6450c4d6c1c31b453de8c82dbea8e304ac4bef92c8348092fb26f934
  clip_pdf_points:
  - 50
  - 45
  - 562
  - 201
  title: EOV-Seg：主要实验结果
  setting: 仅 COCO 训练、ADE20K 测试的开放词汇全景分割。
  metrics: PQ／SQ／RQ／mIoU ↑，FPS ↑
  reading: 模型规模、速度硬件与输入尺寸按原表核对，不能只用 FPS 宣称更优。
---

# EOV-Seg

本页按研究问题提取相关操作；模块图、输入输出、证据和主要结果表在上方展开查看。

## 研究问题

轻量解码器怎样获得足够的类别语义和空间线索？

## 相关操作

VAS 根据文本语义从聚合视觉特征中选择相关信息，减少解码负担；TDEE 通过动态专家权重整合语义和空间嵌入，再使用轻量掩码解码器和文本分类完成全景分割。

## 实验阅读

仅 COCO 训练、ADE20K 测试的开放词汇全景分割。 模型规模、速度硬件与输入尺寸按原表核对，不能只用 FPS 宣称更优。 主表是整体系统结果，单一模块的贡献需结合原文消融。

## 原文依据

- [本次阅读的原文版本](https://arxiv.org/pdf/2412.08628v2)：方法部分；Figure 4（PDF 第 4 页）；实验 Table 1（PDF 第 6 页）。
- [正式发表来源](https://ojs.aaai.org/index.php/AAAI/article/view/32669)。
- [官方实现](https://github.com/nhw649/EOV-Seg)：已核对官方实现目录：configs、datasets、demo、eov_seg、requirements.txt、resources。未独立运行或验证外部权重下载。
