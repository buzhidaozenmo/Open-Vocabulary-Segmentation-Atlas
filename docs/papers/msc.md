---
paper_id: msc
title: 'Masked Scene Contrast: A Scalable Framework for Unsupervised 3D Representation Learning'
short_name: MSC
authors:
- Wu, Xiaoyang
- Wen, Xin
- Liu, Xihui
- Zhao, Hengshuang
year: 2023
preprint_date: unknown
venue: CVPR
publication_status: published
primary_direction: 3d
modalities:
- point_cloud
task_setting: self_supervised_representation
task_types:
- representation
techniques:
- geometry
- feature_distillation
datasets:
- ScanNet
paper_url: https://openaccess.thecvf.com/content/CVPR2023/papers/Wu_Masked_Scene_Contrast_A_Scalable_Framework_for_Unsupervised_3D_Representation_CVPR_2023_paper.pdf
publication_url: https://openaccess.thecvf.com/content/CVPR2023/html/Wu_Masked_Scene_Contrast_A_Scalable_Framework_for_Unsupervised_3D_Representation_CVPR_2023_paper.html
code_status: public
code_url: https://github.com/Pointcept/Pointcept
code_details: 官方实现集成在 Pointcept；公开 configs、pointcept、训练评测脚本，README 列出 MSC 及模型资源；未运行。
content_status: index
checked_on: '2026-11-11'
module_checked_on: '2026-11-11'
summary: 利用三维位置建立跨增强视图点对，并重建遮挡点的颜色与表面法向，在场景尺度学习几何表征。
sources:
- url: https://openaccess.thecvf.com/content/CVPR2023/html/Wu_Masked_Scene_Contrast_A_Scalable_Framework_for_Unsupervised_3D_Representation_CVPR_2023_paper.html
  locator: 出版方正式发表记录
- url: https://openaccess.thecvf.com/content/CVPR2023/papers/Wu_Masked_Scene_Contrast_A_Scalable_Framework_for_Unsupervised_3D_Representation_CVPR_2023_paper.pdf
  locator: 按模块列出的原文章节、原图及结果表
- url: https://github.com/Pointcept/Pointcept
  locator: 官方 README 与根目录；未独立运行
figures:
- id: fig3
  label: Figure 3
  asset: assets/figures/msc-fig3.png
  page: 4
  version: CVPR 2023 出版方正式版
  source_url: https://openaccess.thecvf.com/content/CVPR2023/papers/Wu_Masked_Scene_Contrast_A_Scalable_Framework_for_Unsupervised_3D_Representation_CVPR_2023_paper.pdf
  source_sha256: 67bb39faeb547d3c39381e5687c5be81221157046555637c956bbf09c70c338f
  clip_pdf_points:
  - 48
  - 70
  - 548
  - 351
methods:
- id: normal-reconstruction
  track: pointcloud
  problems:
  - geometry
  title: 空间点对与表面法向重建
  question: 哪些几何信号能够作为无类别标签的训练目标？
  operation: 从同一场景增强出两个点云视图，以空间近邻点对做 InfoNCE；按增强前网格生成互补遮挡，替换点输入特征，并重建遮挡点颜色和 surfel 法向，以 MSE／余弦损失补充对比目标。
  input: 点坐标、颜色、由表面估计的法向
  output: 可迁移到下游任务的点特征
  stage: 自监督预训练
  supervision: 场景自身的空间对应、颜色与法向目标；下游任务另用标注
  origin: proposed
  origin_note: 本文框架中的具体设计；预训练骨干与基础算子不视为本文首创。
  evidence:
  - &id001
    locator: §4.1–4.3，Figure 3，Table 2
    url: https://openaccess.thecvf.com/content/CVPR2023/papers/Wu_Masked_Scene_Contrast_A_Scalable_Framework_for_Unsupervised_3D_Representation_CVPR_2023_paper.pdf
  figure: fig3
  figure_guide: 看 Matching Points、Contrastive Learning 和右侧 Reconstruction；重建颜色与法向而不是简单恢复离散点坐标。
  depicted: true
  route:
  - 点云自身监督
  - 点对比与法向重建
  - 三维表征
  - 下游表征评测
  geometry:
    families:
    - coordinates
    signal: 增强前空间点对应与表面法向
    mechanism: 空间对应规定正样本；法向是遮挡重建目标，给编码器施加局部表面结构约束。
    changes: 点表征的预训练目标
    stage: 预训练
    semantic_role: 重建几何学习表征，不提供语言类别；Table 2 记录标注微调的下游效果。
    route:
    - 坐标与空间邻域
    - 法向重建与点对比
    - 多尺度点表征
    - 预训练／下游
    evidence:
    - *id001
results:
- id: table2
  label: Table 2
  asset: assets/results/msc-table2.png
  page: 8
  version: CVPR 2023 出版方正式版
  source_url: https://openaccess.thecvf.com/content/CVPR2023/papers/Wu_Masked_Scene_Contrast_A_Scalable_Framework_for_Unsupervised_3D_Representation_CVPR_2023_paper.pdf
  source_sha256: 67bb39faeb547d3c39381e5687c5be81221157046555637c956bbf09c70c338f
  clip_pdf_points:
  - 47
  - 69
  - 290
  - 419
  title: 预训练后的下游任务与数据效率
  setting: ScanNet / ScanNet200；ScanNet 与 ARKitScenes 跨数据集预训练；语义、实例、少场景及少标注三个子表。
  metrics: 语义 mIoU ↑；实例 mAP@0.5 ↑
  reading: 完整保留 (a)(b)(c) 三部分。下游微调使用对应标注，几何重建预训练不等于零样本语言分割。
---

# MSC

【原文事实】利用三维位置建立跨增强视图点对，并重建遮挡点的颜色与表面法向，在场景尺度学习几何表征。

## 资料范围

正式发表于 CVPR 2023，本页图表读取 CVPR 2023 出版方正式版。按研究关注点整理相关模块，未独立复现实验。

## 任务与能力范围

重建几何学习表征，不提供语言类别；Table 2 记录标注微调的下游效果。

## 关注的几何操作

**空间点对与表面法向重建**：从同一场景增强出两个点云视图，以空间近邻点对做 InfoNCE；按增强前网格生成互补遮挡，替换点输入特征，并重建遮挡点颜色和 surfel 法向，以 MSE／余弦损失补充对比目标。

依据：§4.1–4.3，Figure 3，Table 2。

## 代码开放情况

【官方文档说明】官方实现集成在 Pointcept；公开 configs、pointcept、训练评测脚本，README 列出 MSC 及模型资源；未运行。

## 实验阅读

Table 2：预训练后的下游任务与数据效率。ScanNet / ScanNet200；ScanNet 与 ARKitScenes 跨数据集预训练；语义、实例、少场景及少标注三个子表。 完整保留 (a)(b)(c) 三部分。下游微调使用对应标注，几何重建预训练不等于零样本语言分割。
