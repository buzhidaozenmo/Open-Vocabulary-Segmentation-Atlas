---
paper_id: radseg
title: 'RADSeg: Unleashing Parameter and Compute Efficient Zero-Shot Open-Vocabulary Segmentation Using Agglomerative Models'
short_name: RADSeg
authors:
- Alama, Omar
- Jariwala, Darshil
- Bhattacharya, Avigyan
- Kim, Seungchan
- Wang, Wenshan
- Scherer, Sebastian
year: 2026
preprint_date: unknown
venue: CVPR Findings
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
paper_url: https://openaccess.thecvf.com/content/CVPR2026F/papers/Alama_RADSeg_Unleashing_Parameter_and_Compute_Efficient_Zero-Shot_Open-Vocabulary_Segmentation_Using_CVPRF_2026_paper.pdf
publication_url: https://openaccess.thecvf.com/content/CVPR2026F/html/Alama_RADSeg_Unleashing_Parameter_and_Compute_Efficient_Zero-Shot_Open-Vocabulary_Segmentation_Using_CVPRF_2026_paper.html
code_status: public
code_url: https://github.com/RADSeg-OVSS/RADSeg
code_details: 已核对官方实现目录：environment.yml、evaluation、hubconf.py、radseg、radseg_demo.py。未独立运行或验证外部权重下载。
content_status: index
checked_on: '2026-11-09'
module_checked_on: '2026-11-09'
summary: 以 RADIO 输出语言对齐稠密特征，加入自相关递归注意和全局聚合以恢复空间局部性，再利用共享 RADIO 特征的 SAM 掩码细化，提高开放词汇像素预测的效率。
sources:
- url: https://openaccess.thecvf.com/content/CVPR2026F/html/Alama_RADSeg_Unleashing_Parameter_and_Compute_Efficient_Zero-Shot_Open-Vocabulary_Segmentation_Using_CVPRF_2026_paper.html
  locator: 正式发表来源：出版页面／作者项目的会议说明
- url: https://openaccess.thecvf.com/content/CVPR2026F/papers/Alama_RADSeg_Unleashing_Parameter_and_Compute_Efficient_Zero-Shot_Open-Vocabulary_Segmentation_Using_CVPRF_2026_paper.pdf
  locator: 方法部分；Figure 2（PDF 第 3 页）；实验 Table 1（PDF 第 6 页）
- url: https://github.com/RADSeg-OVSS/RADSeg
  locator: 官方 README、目录与开放范围；未独立运行
figures:
- id: fig2
  label: Figure 2
  asset: assets/figures/radseg-fig2.png
  page: 3
  version: CVPR Findings 2026 出版方正式版
  source_url: https://openaccess.thecvf.com/content/CVPR2026F/papers/Alama_RADSeg_Unleashing_Parameter_and_Compute_Efficient_Zero-Shot_Open-Vocabulary_Segmentation_Using_CVPRF_2026_paper.pdf
  source_sha256: 367668ab8e207d6a7cef6f99961c2c21a73763f70026c050fd99a8c249124236
  clip_pdf_points:
  - 45
  - 45
  - 567
  - 274.786
methods:
- id: semantic-operation
  track: vocabulary
  problems:
  - alignment
  - efficiency
  title: 聚合视觉语义细化
  question: 单一聚合骨干怎样兼顾文本对齐和局部定位？
  operation: 以 RADIO 输出语言对齐稠密特征，加入自相关递归注意和全局聚合以恢复空间局部性，再利用共享 RADIO 特征的 SAM 掩码细化，提高开放词汇像素预测的效率。
  input: 图像、RADIO 稠密特征及文本
  output: 语言对齐像素特征与细化掩码
  stage: 免任务训练推理
  supervision: 预训练 RADIO 及相关适配器，无目标语义训练标注
  origin: proposed
  origin_note: 本文设计的聚合视觉语义细化流程；所用预训练模型、通用投影及基础算子沿用已有方法，不计作本文新提出。
  evidence:
  - url: https://openaccess.thecvf.com/content/CVPR2026F/papers/Alama_RADSeg_Unleashing_Parameter_and_Compute_Efficient_Zero-Shot_Open-Vocabulary_Segmentation_Using_CVPRF_2026_paper.pdf
    locator: 方法部分；Figure 2（PDF 第 3 页）；实验 Table 1（PDF 第 6 页）
  figure: fig2
  figure_guide: 沿 RADIO backbone、recursive attention、global aggregation 与 mask refinement 阅读。
  depicted: true
  route:
  - 预训练视觉语言特征
  - 聚合视觉语义细化
  - 像素／区域类别表示
  - 开放词汇分割
  result_tables:
  - table1
results:
- id: table1
  label: Table 1
  asset: assets/results/radseg-table1.png
  page: 6
  version: CVPR Findings 2026 出版方正式版
  source_url: https://openaccess.thecvf.com/content/CVPR2026F/papers/Alama_RADSeg_Unleashing_Parameter_and_Compute_Efficient_Zero-Shot_Open-Vocabulary_Segmentation_Using_CVPRF_2026_paper.pdf
  source_sha256: 367668ab8e207d6a7cef6f99961c2c21a73763f70026c050fd99a8c249124236
  clip_pdf_points:
  - 55
  - 329
  - 558
  - 615
  title: RADSeg：主要实验结果
  setting: 不同模型规模、输入分辨率限制下的二维零样本分割。
  metrics: mIoU ↑（按模型规模与输入分辨率分组）
  reading: 正式发表为 CVPR Findings 2026；对齐模型规模和分辨率后再看效果与速度。
---

# RADSeg

本页按研究问题提取相关操作；模块图、输入输出、证据和主要结果表在上方展开查看。

## 研究问题

单一聚合骨干怎样兼顾文本对齐和局部定位？

## 相关操作

以 RADIO 输出语言对齐稠密特征，加入自相关递归注意和全局聚合以恢复空间局部性，再利用共享 RADIO 特征的 SAM 掩码细化，提高开放词汇像素预测的效率。

## 实验阅读

不同模型规模、输入分辨率限制下的二维零样本分割。 正式发表为 CVPR Findings 2026；对齐模型规模和分辨率后再看效果与速度。 主表是整体系统结果，单一模块的贡献需结合原文消融。

## 原文依据

- [本次阅读的原文版本](https://openaccess.thecvf.com/content/CVPR2026F/papers/Alama_RADSeg_Unleashing_Parameter_and_Compute_Efficient_Zero-Shot_Open-Vocabulary_Segmentation_Using_CVPRF_2026_paper.pdf)：方法部分；Figure 2（PDF 第 3 页）；实验 Table 1（PDF 第 6 页）。
- [正式发表来源](https://openaccess.thecvf.com/content/CVPR2026F/html/Alama_RADSeg_Unleashing_Parameter_and_Compute_Efficient_Zero-Shot_Open-Vocabulary_Segmentation_Using_CVPRF_2026_paper.html)。
- [官方实现](https://github.com/RADSeg-OVSS/RADSeg)：已核对官方实现目录：environment.yml、evaluation、hubconf.py、radseg、radseg_demo.py。未独立运行或验证外部权重下载。
