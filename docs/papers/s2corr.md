---
paper_id: s2corr
title: Open-Vocabulary Domain Generalization in Urban-Scene Segmentation
short_name: S²-Corr
authors:
- Zhao, Dong
- Zang, Qi
- Pu, Nan
- Li, Wenjing
- Sebe, Nicu
- Zhong, Zhun
year: 2026
preprint_date: unknown
venue: CVPR
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
- Cityscapes
paper_url: https://openaccess.thecvf.com/content/CVPR2026/papers/Zhao_Open-Vocabulary_Domain_Generalization_in_Urban-Scene_Segmentation_CVPR_2026_paper.pdf
publication_url: https://openaccess.thecvf.com/content/CVPR2026/html/Zhao_Open-Vocabulary_Domain_Generalization_in_Urban-Scene_Segmentation_CVPR_2026_paper.html
code_status: public
code_url: https://github.com/DZhaoXd/s2_corr
code_details: 已核对官方仓库实际实现目录：bash.sh、check.py、configs、datasets、demo、eval_7to19.sh。运行及外部权重可用性未独立复现。
content_status: index
checked_on: '2026-11-09'
module_checked_on: '2026-11-09'
summary: 先计算 CLIP 图文相关性，再以分块状态空间模型聚合相关性；块内处理局部空间、跨块传播上下文，使类别文本与像素的对应在城市驾驶域变化下更一致，最终解码类别图。
sources:
- url: https://openaccess.thecvf.com/content/CVPR2026/html/Zhao_Open-Vocabulary_Domain_Generalization_in_Urban-Scene_Segmentation_CVPR_2026_paper.html
  locator: 正式发表页面及作者信息
- url: https://openaccess.thecvf.com/content/CVPR2026/papers/Zhao_Open-Vocabulary_Domain_Generalization_in_Urban-Scene_Segmentation_CVPR_2026_paper.pdf
  locator: 方法部分；Figure 3（PDF 第 4 页）；实验 Table 3（PDF 第 7 页）
- url: https://github.com/DZhaoXd/s2_corr
  locator: 官方 README 与实际代码目录；不表示已运行
figures:
- id: figure3
  label: Figure 3
  asset: assets/figures/s2corr-figure3.png
  page: 4
  version: CVPR 2026 出版方正式版
  source_url: https://openaccess.thecvf.com/content/CVPR2026/papers/Zhao_Open-Vocabulary_Domain_Generalization_in_Urban-Scene_Segmentation_CVPR_2026_paper.pdf
  source_sha256: d6899179bfb5fe0fff4c6d96210efbf6729733411771bbc763c9209d13b8b721
  clip_pdf_points:
  - 55
  - 50
  - 558
  - 262.80828857421875
methods:
- id: semantic-operation
  track: vocabulary
  problems:
  - alignment
  - unseen
  title: 跨域相关性聚合
  question: 跨域后失真的图文相关性怎样修正？
  operation: 先计算 CLIP 图文相关性，再以分块状态空间模型聚合相关性；块内处理局部空间、跨块传播上下文，使类别文本与像素的对应在城市驾驶域变化下更一致，最终解码类别图。
  input: 城市图像、类别文本及相关性体
  output: 经过域鲁棒细化的像素类别图
  stage: 训练及跨域推理
  supervision: 源驾驶域分割标注；目标域不参与训练
  origin: proposed
  origin_note: 本文设计的跨域相关性聚合流程；其预训练基础模型与通用组件沿用已有方法，不计作本文新提出。
  origin_refs:
  - url: https://openaccess.thecvf.com/content/CVPR2026/papers/Zhao_Open-Vocabulary_Domain_Generalization_in_Urban-Scene_Segmentation_CVPR_2026_paper.pdf
    locator: 方法部分列明的基础模型及其参考文献
  evidence:
  - url: https://openaccess.thecvf.com/content/CVPR2026/papers/Zhao_Open-Vocabulary_Domain_Generalization_in_Urban-Scene_Segmentation_CVPR_2026_paper.pdf
    locator: 方法部分；Figure 3（PDF 第 4 页）；实验 Table 3（PDF 第 7 页）
  figure: figure3
  figure_guide: 上部是 CLIP 图文编码和相关性聚合；下部放大 S²-Corr 的分块状态空间模型，展示局部 chunk 与跨块上下文聚合。
  depicted: true
  route:
  - CLIP 图文相关性
  - 跨域相关性聚合
  - 像素类别分数
  - 跨域开放词汇分割
  result_tables:
  - table3
results:
- id: table3
  label: Table 3
  asset: assets/results/s2corr-table3.png
  page: 7
  version: CVPR 2026 出版方正式版
  source_url: https://openaccess.thecvf.com/content/CVPR2026/papers/Zhao_Open-Vocabulary_Domain_Generalization_in_Urban-Scene_Segmentation_CVPR_2026_paper.pdf
  source_sha256: d6899179bfb5fe0fff4c6d96210efbf6729733411771bbc763c9209d13b8b721
  clip_pdf_points:
  - 55
  - 54
  - 558
  - 238
  title: S²-Corr：主要实验结果
  setting: synthetic-to-real OVDG-SS；按 Dv-19／Dv-58、骨干及训练域分组。
  metrics: mIoU 等 ↑，按类别分组列
  reading: 同时核对未见域与未见类，不能把普通同域分割值直接放在本协议中比较。
---

# S²-Corr

本页按研究问题提取相关操作；模块原图、具体输入输出、来源与主要实验结果在上方展开查看。

## 研究问题

跨域后失真的图文相关性怎样修正？

## 相关操作

先计算 CLIP 图文相关性，再以分块状态空间模型聚合相关性；块内处理局部空间、跨块传播上下文，使类别文本与像素的对应在城市驾驶域变化下更一致，最终解码类别图。

## 实验阅读

synthetic-to-real OVDG-SS；按 Dv-19／Dv-58、骨干及训练域分组。 同时核对未见域与未见类，不能把普通同域分割值直接放在本协议中比较。 主要结果是整套方法的效果，不能单凭该表归因到一个模块。

## 原文依据

- [出版方原文](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhao_Open-Vocabulary_Domain_Generalization_in_Urban-Scene_Segmentation_CVPR_2026_paper.pdf)：方法部分；Figure 3（PDF 第 4 页）；实验 Table 3（PDF 第 7 页）。
- [官方实现](https://github.com/DZhaoXd/s2_corr)：已检查公开目录，未独立运行训练或评测。
