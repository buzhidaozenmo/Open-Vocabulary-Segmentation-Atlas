---
paper_id: resclip
title: 'ResCLIP: Residual Attention for Training-free Dense Vision-language Inference'
short_name: ResCLIP
authors:
- Yang, Yuhang
- Deng, Jinhong
- Li, Wen
- Duan, Lixin
year: 2025
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
datasets: []
paper_url: https://openaccess.thecvf.com/content/CVPR2025/papers/Yang_ResCLIP_Residual_Attention_for_Training-free_Dense_Vision-language_Inference_CVPR_2025_paper.pdf
publication_url: https://openaccess.thecvf.com/content/CVPR2025/html/Yang_ResCLIP_Residual_Attention_for_Training-free_Dense_Vision-language_Inference_CVPR_2025_paper.html
code_status: public
code_url: https://github.com/yvhangyang/ResCLIP
code_details: 已核对官方实现目录：clip、configs、custom_datasets.py、datasets、demo.py、eval.py。未独立运行或验证外部权重下载。
content_status: index
checked_on: '2026-11-09'
module_checked_on: '2026-11-09'
summary: RCS 把非末层 query-key 交叉相关注意作为残差引入末块，重构局部空间关系；SFR 再用语义分割响应修正注意分数，使同类别区域的聚合更一致。
sources:
- url: https://openaccess.thecvf.com/content/CVPR2025/html/Yang_ResCLIP_Residual_Attention_for_Training-free_Dense_Vision-language_Inference_CVPR_2025_paper.html
  locator: 正式发表来源：出版页面／作者项目的会议说明
- url: https://openaccess.thecvf.com/content/CVPR2025/papers/Yang_ResCLIP_Residual_Attention_for_Training-free_Dense_Vision-language_Inference_CVPR_2025_paper.pdf
  locator: 方法部分；Figure 4（PDF 第 5 页）；实验 Table 1（PDF 第 6 页）
- url: https://github.com/yvhangyang/ResCLIP
  locator: 官方 README、目录与开放范围；未独立运行
figures:
- id: fig4
  label: Figure 4
  asset: assets/figures/resclip-fig4.png
  page: 5
  version: CVPR 2025 出版方正式版
  source_url: https://openaccess.thecvf.com/content/CVPR2025/papers/Yang_ResCLIP_Residual_Attention_for_Training-free_Dense_Vision-language_Inference_CVPR_2025_paper.pdf
  source_sha256: 8814b21568bac8f6b2df6e0abf7e4f3bd0d0d422bd5d30f20d8e12bec9ccfc05
  clip_pdf_points:
  - 45
  - 45
  - 567
  - 288.145
methods:
- id: semantic-operation
  track: vocabulary
  problems:
  - alignment
  - reliability
  title: 残差注意与语义反馈
  question: CLIP 中层空间关系怎样保留到最后输出？
  operation: RCS 把非末层 query-key 交叉相关注意作为残差引入末块，重构局部空间关系；SFR 再用语义分割响应修正注意分数，使同类别区域的聚合更一致。
  input: CLIP 中间层注意、末层特征与文本
  output: 经空间残差及语义反馈增强的类别图
  stage: 免任务训练推理
  supervision: 冻结 CLIP，无目标分割训练标签
  origin: proposed
  origin_note: 本文设计的残差注意与语义反馈流程；所用预训练模型、通用投影及基础算子沿用已有方法，不计作本文新提出。
  evidence:
  - url: https://openaccess.thecvf.com/content/CVPR2025/papers/Yang_ResCLIP_Residual_Attention_for_Training-free_Dense_Vision-language_Inference_CVPR_2025_paper.pdf
    locator: 方法部分；Figure 4（PDF 第 5 页）；实验 Table 1（PDF 第 6 页）
  figure: fig4
  figure_guide: 看 RCS 中 intermediate cross-correlation attention，以及 SFR 的 semantic feedback 连接。
  depicted: true
  route:
  - 预训练视觉语言特征
  - 残差注意与语义反馈
  - 像素／区域类别表示
  - 开放词汇分割
  result_tables:
  - table1
results:
- id: table1
  label: Table 1
  asset: assets/results/resclip-table1.png
  page: 6
  version: CVPR 2025 出版方正式版
  source_url: https://openaccess.thecvf.com/content/CVPR2025/papers/Yang_ResCLIP_Residual_Attention_for_Training-free_Dense_Vision-language_Inference_CVPR_2025_paper.pdf
  source_sha256: 8814b21568bac8f6b2df6e0abf7e4f3bd0d0d422bd5d30f20d8e12bec9ccfc05
  clip_pdf_points:
  - 55
  - 55
  - 558
  - 340
  title: ResCLIP：主要实验结果
  setting: 无背景语义分割基准；含背景结果另见 Table 2。
  metrics: mIoU ↑
  reading: with-background 与 without-background 分开比较，保留骨干条件。
---

# ResCLIP

本页按研究问题提取相关操作；模块图、输入输出、证据和主要结果表在上方展开查看。

## 研究问题

CLIP 中层空间关系怎样保留到最后输出？

## 相关操作

RCS 把非末层 query-key 交叉相关注意作为残差引入末块，重构局部空间关系；SFR 再用语义分割响应修正注意分数，使同类别区域的聚合更一致。

## 实验阅读

无背景语义分割基准；含背景结果另见 Table 2。 with-background 与 without-background 分开比较，保留骨干条件。 主表是整体系统结果，单一模块的贡献需结合原文消融。

## 原文依据

- [本次阅读的原文版本](https://openaccess.thecvf.com/content/CVPR2025/papers/Yang_ResCLIP_Residual_Attention_for_Training-free_Dense_Vision-language_Inference_CVPR_2025_paper.pdf)：方法部分；Figure 4（PDF 第 5 页）；实验 Table 1（PDF 第 6 页）。
- [正式发表来源](https://openaccess.thecvf.com/content/CVPR2025/html/Yang_ResCLIP_Residual_Attention_for_Training-free_Dense_Vision-language_Inference_CVPR_2025_paper.html)。
- [官方实现](https://github.com/yvhangyang/ResCLIP)：已核对官方实现目录：clip、configs、custom_datasets.py、datasets、demo.py、eval.py。未独立运行或验证外部权重下载。
