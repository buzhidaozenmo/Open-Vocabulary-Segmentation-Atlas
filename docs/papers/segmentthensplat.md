---
paper_id: segmentthensplat
title: 'Segment then Splat: Unified 3D Open-Vocabulary Segmentation via Gaussian Splatting'
short_name: Segment then Splat
authors:
- Yiren Lu
- Yunlai Zhou
- Yiran Qiao
- Chaoda Song
- Tuo Liang
- Jing Ma
- Huan Wang
- Yu Yin
year: 2025
preprint_date: unknown
venue: NeurIPS
publication_status: published
primary_direction: 3dgs
modalities:
- gaussian
- image
task_setting: open_vocabulary
task_types:
- semantic
techniques:
- semantic_alignment
datasets:
- LERF
paper_url: https://arxiv.org/pdf/2503.22204v2
publication_url: https://papers.neurips.cc/paper_files/paper/2025/hash/f2644105c6680950b0adbfa0a2cfb177-Abstract-Conference.html
code_status: public
code_url: https://github.com/luyr/Segment-then-Splat
code_details: 已核对官方实现目录：arguments、convert.py、full_eval.py、gaussian_renderer、helpers、lpipsPyTorch。未独立运行或验证外部权重下载。
content_status: index
checked_on: '2026-11-09'
module_checked_on: '2026-11-09'
summary: 在重建前先用跨帧跟踪建立对象掩码并给高斯赋对象身份，优化中约束对象—高斯对应；重建后为每组对象登记 CLIP 嵌入，文本查询通过对象组检索完成，支持静态与动态场景。
sources:
- url: https://papers.neurips.cc/paper_files/paper/2025/hash/f2644105c6680950b0adbfa0a2cfb177-Abstract-Conference.html
  locator: 正式发表来源：出版页面／作者项目的会议说明
- url: https://arxiv.org/pdf/2503.22204v2
  locator: 方法部分；Figure 2（PDF 第 4 页）；实验 Table 1（PDF 第 8 页）
- url: https://github.com/luyr/Segment-then-Splat
  locator: 官方 README、目录与开放范围；未独立运行
figures:
- id: fig2
  label: Figure 2
  asset: assets/figures/segmentthensplat-fig2.png
  page: 4
  version: arXiv 2503.22204v2
  source_url: https://arxiv.org/pdf/2503.22204v2
  source_sha256: 709ce099eed7ccc658b2e0cbfcd270f3edcc181734fa398be7936f1f6ab920fa
  clip_pdf_points:
  - 45
  - 45
  - 567
  - 210.17
methods:
- id: semantic-operation
  track: vocabulary
  problems:
  - temporal
  - regions
  - alignment
  title: 对象分组后语义绑定
  question: 怎样避免每个高斯都单独学习语言场？
  operation: 在重建前先用跨帧跟踪建立对象掩码并给高斯赋对象身份，优化中约束对象—高斯对应；重建后为每组对象登记 CLIP 嵌入，文本查询通过对象组检索完成，支持静态与动态场景。
  input: 多视角／视频掩码、对象身份、CLIP 与高斯
  output: 带文本语义的对象高斯组
  stage: 跟踪、分组重建及查询推理
  supervision: 二维跟踪掩码、RGB 重建信号与 CLIP 特征
  origin: proposed
  origin_note: 本文设计的对象分组后语义绑定流程；所用预训练模型、通用投影及基础算子沿用已有方法，不计作本文新提出。
  evidence:
  - url: https://arxiv.org/pdf/2503.22204v2
    locator: 方法部分；Figure 2（PDF 第 4 页）；实验 Table 1（PDF 第 8 页）
  figure: fig2
  figure_guide: 看多视图 mask tracking → object-specific Gaussians → CLIP association；并留意对象重建损失。
  depicted: true
  route:
  - 预训练视觉语言特征
  - 对象分组后语义绑定
  - 高斯语言场／索引
  - 三维分割与查询
  result_tables:
  - table1
results:
- id: table1
  label: Table 1
  asset: assets/results/segmentthensplat-table1.png
  page: 8
  version: arXiv 2503.22204v2
  source_url: https://arxiv.org/pdf/2503.22204v2
  source_sha256: 709ce099eed7ccc658b2e0cbfcd270f3edcc181734fa398be7936f1f6ab920fa
  clip_pdf_points:
  - 305
  - 239
  - 506
  - 450
  title: Segment then Splat：主要实验结果
  setting: 静态 LERF-OVS／3DOVS 与动态 HyperNeRF／Neu3D，保留训练时间。
  metrics: mIoU ↑，时间 ↓
  reading: 2D 与 3D 输出分组不同；静态和动态场景分开看。
---

# Segment then Splat

本页按研究问题提取相关操作；模块图、输入输出、证据和主要结果表在上方展开查看。

## 研究问题

怎样避免每个高斯都单独学习语言场？

## 相关操作

在重建前先用跨帧跟踪建立对象掩码并给高斯赋对象身份，优化中约束对象—高斯对应；重建后为每组对象登记 CLIP 嵌入，文本查询通过对象组检索完成，支持静态与动态场景。

## 实验阅读

静态 LERF-OVS／3DOVS 与动态 HyperNeRF／Neu3D，保留训练时间。 2D 与 3D 输出分组不同；静态和动态场景分开看。 主表是整体系统结果，单一模块的贡献需结合原文消融。

## 原文依据

- [本次阅读的原文版本](https://arxiv.org/pdf/2503.22204v2)：方法部分；Figure 2（PDF 第 4 页）；实验 Table 1（PDF 第 8 页）。
- [正式发表来源](https://papers.neurips.cc/paper_files/paper/2025/hash/f2644105c6680950b0adbfa0a2cfb177-Abstract-Conference.html)。
- [官方实现](https://github.com/luyr/Segment-then-Splat)：已核对官方实现目录：arguments、convert.py、full_eval.py、gaussian_renderer、helpers、lpipsPyTorch。未独立运行或验证外部权重下载。
