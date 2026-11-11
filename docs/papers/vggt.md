---
paper_id: vggt
title: 'VGGT: Visual Geometry Grounded Transformer'
short_name: VGGT
authors:
- Wang, Jianyuan
- Chen, Minghao
- Karaev, Nikita
- Vedaldi, Andrea
- Rupprecht, Christian
- Novotny, David
year: 2025
preprint_date: unknown
venue: CVPR
publication_status: published
primary_direction: multiview
modalities:
- image
task_setting: geometric_reconstruction
task_types:
- geometry_estimation
techniques:
- geometry
- fusion
datasets:
- RealEstate10K
- CO3Dv2
paper_url: https://openaccess.thecvf.com/content/CVPR2025/papers/Wang_VGGT_Visual_Geometry_Grounded_Transformer_CVPR_2025_paper.pdf
publication_url: https://openaccess.thecvf.com/content/CVPR2025/html/Wang_VGGT_Visual_Geometry_Grounded_Transformer_CVPR_2025_paper.html
code_status: public
code_url: https://github.com/facebookresearch/vggt
code_details: 官方仓库公开模型、推理与可视化、COLMAP 导出及 training 目录；README 提供权重入口，许可单列于 LICENSE.txt；未运行。
content_status: index
checked_on: '2026-11-11'
module_checked_on: '2026-11-11'
summary: 以帧内与跨帧交替自注意力联合预测相机、深度、点图和跟踪；提供多视图几何对应，不直接生成类别语义。
sources:
- url: https://openaccess.thecvf.com/content/CVPR2025/html/Wang_VGGT_Visual_Geometry_Grounded_Transformer_CVPR_2025_paper.html
  locator: 出版方正式发表记录
- url: https://openaccess.thecvf.com/content/CVPR2025/papers/Wang_VGGT_Visual_Geometry_Grounded_Transformer_CVPR_2025_paper.pdf
  locator: 按模块列出的原文章节、原图及结果表
- url: https://github.com/facebookresearch/vggt
  locator: 官方 README 与根目录；未独立运行
figures:
- id: fig2
  label: Figure 2
  asset: assets/figures/vggt-fig2.png
  page: 3
  version: CVPR 2025 出版方正式版
  source_url: https://openaccess.thecvf.com/content/CVPR2025/papers/Wang_VGGT_Visual_Geometry_Grounded_Transformer_CVPR_2025_paper.pdf
  source_sha256: b2e33f1040badf274373ad810c6ac0c272597195427ac6a0f171d5933b639a0e
  clip_pdf_points:
  - 56
  - 70
  - 556
  - 291
methods:
- id: joint-geometry
  track: pointcloud
  problems:
  - geometry
  title: 多视图联合估计相机、深度与点图
  question: 无已知相机输入时如何获得多视图三维对应？
  operation: 图像分块后加入相机 token，交替执行帧内与全局自注意力；相机头估计内外参，DPT 密集头预测深度、点图和跟踪特征，并估计深度／点图不确定性。输出统一在首相机坐标系；跟踪头匹配查询点在其他图像中的位置。
  input: 一组 RGB 图像，不要求预先给定相机
  output: 相机参数、深度、点图、不确定性和点轨迹
  stage: 以三维标注训练；多图前向推理
  supervision: 大量三维标注数据的多任务监督，不是无监督重建
  origin: proposed
  origin_note: 本文框架中的具体设计；预训练骨干与基础算子不视为本文首创。
  evidence:
  - &id001
    locator: §3.1–3.3，Figure 2，Table 1
    url: https://openaccess.thecvf.com/content/CVPR2025/papers/Wang_VGGT_Visual_Geometry_Grounded_Transformer_CVPR_2025_paper.pdf
  figure: fig2
  figure_guide: 左侧多帧 token 经帧内／全局注意力，到相机头和 DPT 的密集输出；点图、深度与跟踪在右侧分开标示。
  depicted: true
  route:
  - 多视图图像
  - 联合几何估计
  - 相机深度与点图
  - 多视图重建
  geometry:
    families:
    - reconstruction
    - visibility
    signal: 多视图图像学习得到的相机、深度、点图及不确定性
    mechanism: 通过跨帧联合预测建立统一空间对应；不确定性参与训练损失并表示预测可靠性。
    changes: 几何坐标与跨视图对应
    stage: 几何估计训练与推理
    semantic_role: VGGT 输出几何与对应，不输出开放词汇类别；论文的位姿表不能解释为分割效果。
    route:
    - 多视图图像
    - 联合几何估计
    - 相机深度与对应
    - 几何重建
    evidence:
    - *id001
results:
- id: table1
  label: Table 1
  asset: assets/results/vggt-table1.png
  page: 5
  version: CVPR 2025 出版方正式版
  source_url: https://openaccess.thecvf.com/content/CVPR2025/papers/Wang_VGGT_Visual_Geometry_Grounded_Transformer_CVPR_2025_paper.pdf
  source_sha256: b2e33f1040badf274373ad810c6ac0c272597195427ac6a0f171d5933b639a0e
  clip_pdf_points:
  - 315
  - 70
  - 556
  - 297
  title: 多视图相机位姿估计
  setting: RealEstate10K / CO3Dv2；随机 10 帧；H100 测速；括号表示未在 CO3D 训练。
  metrics: AUC@30 ↑；时间 ↓
  reading: 此表衡量相机几何，不衡量分割语义；注意训练数据与全局对齐 / 束调整设置，保留所有方法行和脚注。
---

# VGGT

【原文事实】以帧内与跨帧交替自注意力联合预测相机、深度、点图和跟踪；提供多视图几何对应，不直接生成类别语义。

## 资料范围

正式发表于 CVPR 2025，本页图表读取 CVPR 2025 出版方正式版。按研究关注点整理相关模块，未独立复现实验。

## 任务与能力范围

VGGT 输出几何与对应，不输出开放词汇类别；论文的位姿表不能解释为分割效果。

## 关注的几何操作

**多视图联合估计相机、深度与点图**：图像分块后加入相机 token，交替执行帧内与全局自注意力；相机头估计内外参，DPT 密集头预测深度、点图和跟踪特征，并估计深度／点图不确定性。输出统一在首相机坐标系；跟踪头匹配查询点在其他图像中的位置。

依据：§3.1–3.3，Figure 2，Table 1。

## 代码开放情况

【官方文档说明】官方仓库公开模型、推理与可视化、COLMAP 导出及 training 目录；README 提供权重入口，许可单列于 LICENSE.txt；未运行。

## 实验阅读

Table 1：多视图相机位姿估计。RealEstate10K / CO3Dv2；随机 10 帧；H100 测速；括号表示未在 CO3D 训练。 此表衡量相机几何，不衡量分割语义；注意训练数据与全局对齐 / 束调整设置，保留所有方法行和脚注。
