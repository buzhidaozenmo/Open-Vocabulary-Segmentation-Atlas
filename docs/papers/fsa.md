---
paper_id: fsa
title: Plug-in Feedback Self-adaptive Attention in CLIP for Training-free Open-Vocabulary Segmentation
short_name: FSA
authors:
- Chi, Zhixiang
- Wu, Yanan
- Gu, Li
- Liu, Huan
- Wang, Ziqiang
- Zhang, Yang
- Wang, Yang
- Plataniotis, Konstantinos
year: 2025
preprint_date: unknown
venue: ICCV
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
- PASCAL
- COCO
- Cityscapes
- ADE20K
paper_url: https://openaccess.thecvf.com/content/ICCV2025/papers/Chi_Plug-in_Feedback_Self-adaptive_Attention_in_CLIP_for_Training-free_Open-Vocabulary_Segmentation_ICCV_2025_paper.pdf
publication_url: https://openaccess.thecvf.com/content/ICCV2025/html/Chi_Plug-in_Feedback_Self-adaptive_Attention_in_CLIP_for_Training-free_Open-Vocabulary_Segmentation_ICCV_2025_paper.html
code_status: public
code_url: https://github.com/chi-chi-zx/FSA
code_details: 已核对官方仓库实际实现目录：FSA_Proxy_segmentor.py、__pycache__、configs、custom_datasets.py、datasets、dist_test.sh。运行及外部权重可用性未独立复现。
content_status: index
checked_on: '2026-11-09'
module_checked_on: '2026-11-09'
summary: 用均匀注意力对照分支隔离初始注意贡献；从输出类别分布的成对 KL 散度构造 patch 相关性，经置信度剪枝得到稀疏反馈，再以多种适配方式回注初始注意并集成。
sources:
- url: https://openaccess.thecvf.com/content/ICCV2025/html/Chi_Plug-in_Feedback_Self-adaptive_Attention_in_CLIP_for_Training-free_Open-Vocabulary_Segmentation_ICCV_2025_paper.html
  locator: 正式发表页面及作者信息
- url: https://openaccess.thecvf.com/content/ICCV2025/papers/Chi_Plug-in_Feedback_Self-adaptive_Attention_in_CLIP_for_Training-free_Open-Vocabulary_Segmentation_ICCV_2025_paper.pdf
  locator: 方法部分；Figure 4（PDF 第 4 页）；实验 Table 2（PDF 第 6 页）
- url: https://github.com/chi-chi-zx/FSA
  locator: 官方 README 与实际代码目录；不表示已运行
figures:
- id: figure4
  label: Figure 4
  asset: assets/figures/fsa-figure4.png
  page: 4
  version: ICCV 2025 出版方正式版
  source_url: https://openaccess.thecvf.com/content/ICCV2025/papers/Chi_Plug-in_Feedback_Self-adaptive_Attention_in_CLIP_for_Training-free_Open-Vocabulary_Segmentation_ICCV_2025_paper.pdf
  source_sha256: 6f7585e6f944d1920798b55263b0db0f5d8a37faaadee37398ef194a309d75af
  clip_pdf_points:
  - 55
  - 50
  - 558
  - 255.63812255859375
methods:
- id: semantic-operation
  track: vocabulary
  problems:
  - alignment
  - reliability
  title: 预测反馈校准
  question: 最终文本预测怎样反馈修正中间注意力？
  operation: 用均匀注意力对照分支隔离初始注意贡献；从输出类别分布的成对 KL 散度构造 patch 相关性，经置信度剪枝得到稀疏反馈，再以多种适配方式回注初始注意并集成。
  input: 原分割器输出分布与中间注意图
  output: 语义一致性增强的注意图及分割
  stage: 免任务训练的反馈推理
  supervision: 冻结预训练模型与基础分割器预测，无目标标注
  origin: proposed
  origin_note: 本文设计的预测反馈校准流程；其预训练基础模型与通用组件沿用已有方法，不计作本文新提出。
  origin_refs:
  - url: https://openaccess.thecvf.com/content/ICCV2025/papers/Chi_Plug-in_Feedback_Self-adaptive_Attention_in_CLIP_for_Training-free_Open-Vocabulary_Segmentation_ICCV_2025_paper.pdf
    locator: 方法部分列明的基础模型及其参考文献
  evidence:
  - url: https://openaccess.thecvf.com/content/ICCV2025/papers/Chi_Plug-in_Feedback_Self-adaptive_Attention_in_CLIP_for_Training-free_Open-Vocabulary_Segmentation_ICCV_2025_paper.pdf
    locator: 方法部分；Figure 4（PDF 第 4 页）；实验 Table 2（PDF 第 6 页）
  figure: figure4
  figure_guide: 上部双分支以均匀注意隔离原注意贡献；下部从输出分布构建反馈相关性，剪枝后回注原注意并集成。
  depicted: true
  route:
  - 分割输出与 CLIP 注意力
  - 预测反馈校准
  - 修正注意与像素分数
  - 开放词汇分割
  result_tables:
  - table2
results:
- id: table2
  label: Table 2
  asset: assets/results/fsa-table2.png
  page: 6
  version: ICCV 2025 出版方正式版
  source_url: https://openaccess.thecvf.com/content/ICCV2025/papers/Chi_Plug-in_Feedback_Self-adaptive_Attention_in_CLIP_for_Training-free_Open-Vocabulary_Segmentation_ICCV_2025_paper.pdf
  source_sha256: 6f7585e6f944d1920798b55263b0db0f5d8a37faaadee37398ef194a309d75af
  clip_pdf_points:
  - 55
  - 53
  - 558
  - 332
  title: FSA：主要实验结果
  setting: Table 2 在八基准中接入不同现有方法；保留各方法的原骨干。
  metrics: mIoU ↑
  reading: 比较同一基础方法的两行；这是插件增益，不是所有模型共享一个绝对分数。
---

# FSA

本页按研究问题提取相关操作；模块原图、具体输入输出、来源与主要实验结果在上方展开查看。

## 研究问题

最终文本预测怎样反馈修正中间注意力？

## 相关操作

用均匀注意力对照分支隔离初始注意贡献；从输出类别分布的成对 KL 散度构造 patch 相关性，经置信度剪枝得到稀疏反馈，再以多种适配方式回注初始注意并集成。

## 实验阅读

Table 2 在八基准中接入不同现有方法；保留各方法的原骨干。 比较同一基础方法的两行；这是插件增益，不是所有模型共享一个绝对分数。 主要结果是整套方法的效果，不能单凭该表归因到一个模块。

## 原文依据

- [出版方原文](https://openaccess.thecvf.com/content/ICCV2025/papers/Chi_Plug-in_Feedback_Self-adaptive_Attention_in_CLIP_for_Training-free_Open-Vocabulary_Segmentation_ICCV_2025_paper.pdf)：方法部分；Figure 4（PDF 第 4 页）；实验 Table 2（PDF 第 6 页）。
- [官方实现](https://github.com/chi-chi-zx/FSA)：已检查公开目录，未独立运行训练或评测。
