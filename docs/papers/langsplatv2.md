---
paper_id: langsplatv2
title: 'LangSplatV2: High-dimensional 3D Language Gaussian Splatting with 450+ FPS'
short_name: LangSplatV2
authors: []
year: 2025
preprint_date: '2025-07-09'
venue: NeurIPS
publication_status: published
primary_direction: 3dgs
modalities:
- gaussian
- image
task_setting: open_vocabulary
task_types:
- language_field
techniques:
- semantic_alignment
- region_aggregation
- efficient_inference
datasets:
- LERF
- 3D-OVS
- Mip-NeRF360
paper_url: https://arxiv.org/abs/2507.07136
publication_url: https://langsplat-v2.github.io/
code_status: public
code_url: https://github.com/ZhaoYujie2002/LangSplatV2
code_details: 官方仓库提供预处理、训练、多个数据集评测流程及模型/数据入口。
content_status: index
checked_on: '2026-11-09'
summary: 用高效的高维语言高斯表示改善场景文本查询的精度与速度。
sources:
- url: https://langsplat-v2.github.io/
  locator: 正式发表来源
- url: https://github.com/ZhaoYujie2002/LangSplatV2
  locator: 官方 README / 公开目录；未运行
figures:
- id: fig2
  asset: assets/figures/langsplatv2-fig2.png
  label: Figure 2
  page: 5
  version: arXiv 2507.07136v2
  source_url: https://arxiv.org/pdf/2507.07136v2
  clip_pdf_points:
  - 105
  - 45
  - 508
  - 207
  source_sha256: 82382be73a62705b63f5c708f47aca3071907c8c99ee2d72b6407f9307f6ae22
methods:
- id: supervision
  track: vocabulary
  problems:
  - alignment
  - regions
  title: SAM 区域 CLIP 特征监督语言场
  question: 高斯语言场的开放词汇语义从哪里来？
  operation: 沿用 SAM 的多层级区域提取 CLIP 图像特征；把这些高维语言特征作为二维监督，通过多视角渲染损失优化高斯语义表示，使渲染特征回到可与文本匹配的 CLIP 空间。
  input: 多视图图像、SAM 区域 CLIP 特征
  output: 语言高斯的二维监督目标
  stage: 预处理与逐场景训练
  supervision: 预训练 SAM、CLIP 与场景图像；不需要人工类别标注
  origin: reused
  origin_note: 区域特征与层级语义监督沿用 LangSplat；本文改变语言表示及渲染方式。
  origin_refs:
  - url: https://arxiv.org/abs/2312.16084
    locator: LangSplatV2 §3.1 对 LangSplat 的回顾及 Figure 2 预处理流程
  evidence:
  - url: https://arxiv.org/pdf/2507.07136v2
    locator: §3.1、§3.3–3.4，Figure 2
  figure: fig2
  figure_guide: 看主图右侧预处理 SAM→CLIP→Hierarchical Semantics 与 Cos Loss 的监督回路。
  depicted: true
  route:
  - 二维区域特征
  - 区域语言场监督
  - 高斯语言场
  - 语言场训练
- id: codebook
  track: vocabulary
  problems:
  - alignment
  - efficiency
  title: 全局码本与稀疏系数保存高维语义
  question: 怎样存储和查询高维语言特征而降低解码代价？
  operation: 为场景学习高维全局语言码本，每个高斯只保留 top-K 非零系数；以稀疏系数混合码本表示语言嵌入，渲染系数图后线性恢复高维特征，再与文本查询计算相关性。
  input: 全局码本、每高斯稀疏系数、文本嵌入
  output: 高维语言特征图与查询相关性
  stage: 逐场景训练＋推理
  supervision: 二维区域语言监督；不是点云语义蒸馏
  origin: proposed
  origin_note: 本文 3D Sparse Coefficient Field 与稀疏渲染；码本是场景共享而非固定类别表。
  origin_refs: []
  evidence:
  - url: https://arxiv.org/pdf/2507.07136v2
    locator: §3.3–3.4，Eq.5，Figure 2
  figure: fig2
  figure_guide: 看左侧 Global Codebook 与 Sparse Coefficient，沿 Rendering 到 512-dim Language Feature Map。
  depicted: true
  route:
  - 二维区域特征
  - 稀疏码本表示
  - 高斯语言场
  - 文本相似度分类
module_checked_on: '2026-11-09'
---
# LangSplatV2

## 当前整理状态

已按研究关注点核查下列方法模块与配图；尚未完成全文样例笔记，不据此生成实验排名。

## 收录理由

用高效的高维语言高斯表示改善场景文本查询的精度与速度。

## 开源情况

【官方文档说明】官方仓库提供预处理、训练、多个数据集评测流程及模型/数据入口。 本轮没有安装或运行代码，没有独立验证权重下载。
