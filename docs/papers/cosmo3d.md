---
paper_id: cosmo3d
title: 'CoSMo3D: Open-World Promptable 3D Semantic Segmentation through LLM-Guided Canonical Spatial Modeling'
short_name: CoSMo3D
authors:
- Jin, Li
- Chen, Weikai
- Wang, Yujie
- Yin, Yingda
- Hu, Zeyu
- Zhang, Runze
- Luo, Keyang
- Qian, Shengju
- Wang, Xin
- Qin, Xueying
year: 2026
preprint_date: unknown
venue: CVPR
publication_status: published
primary_direction: 3d
modalities:
- point_cloud
- image
task_setting: open_vocabulary
task_types:
- semantic
techniques:
- semantic_alignment
datasets: []
paper_url: https://openaccess.thecvf.com/content/CVPR2026/papers/Jin_CoSMo3D_Open-World_Promptable_3D_Semantic_Segmentation_through_LLM-Guided_Canonical_Spatial_CVPR_2026_paper.pdf
publication_url: https://openaccess.thecvf.com/content/CVPR2026/html/Jin_CoSMo3D_Open-World_Promptable_3D_Semantic_Segmentation_through_LLM-Guided_Canonical_Spatial_CVPR_2026_paper.html
code_status: public
code_url: https://github.com/JinLi998/CoSMo3D
code_details: 已核对官方仓库实际实现目录：app、common、data_test、environment.txt、environment.yml、eval_benchmark。运行及外部权重可用性未独立复现。
content_status: index
checked_on: '2026-11-09'
module_checked_on: '2026-11-11'
summary: 以 Point Transformer 编码形状、SigLIP 编码文本；训练时增加规范坐标嵌入分支，通过语义对比、规范地图锚定和规范包围盒校准约束，使不同姿态下的部件特征对应到稳定的规范空间。
sources:
- url: https://openaccess.thecvf.com/content/CVPR2026/html/Jin_CoSMo3D_Open-World_Promptable_3D_Semantic_Segmentation_through_LLM-Guided_Canonical_Spatial_CVPR_2026_paper.html
  locator: 正式发表页面及作者信息
- url: https://openaccess.thecvf.com/content/CVPR2026/papers/Jin_CoSMo3D_Open-World_Promptable_3D_Semantic_Segmentation_through_LLM-Guided_Canonical_Spatial_CVPR_2026_paper.pdf
  locator: 方法部分；Figure 2（PDF 第 3 页）；实验 Table 1（PDF 第 7 页）
- url: https://github.com/JinLi998/CoSMo3D
  locator: 官方 README 与实际代码目录；不表示已运行
figures:
- id: figure2
  label: Figure 2
  asset: assets/figures/cosmo3d-figure2.png
  page: 3
  version: CVPR 2026 出版方正式版
  source_url: https://openaccess.thecvf.com/content/CVPR2026/papers/Jin_CoSMo3D_Open-World_Promptable_3D_Semantic_Segmentation_through_LLM-Guided_Canonical_Spatial_CVPR_2026_paper.pdf
  source_sha256: a9a51230835f61c7eb342f95627e71f3cb3a1eb87bf928af5bdacbeb50e187a1
  clip_pdf_points:
  - 55
  - 50
  - 558
  - 243.77297973632812
methods:
- id: semantic-operation
  track: pointcloud
  problems:
  - geometry
  - alignment
  title: 规范空间语义对齐
  question: 点云姿态变化时怎样稳定对应文本部件？
  operation: 以 Point Transformer 编码形状、SigLIP 编码文本；训练时增加规范坐标嵌入分支，通过语义对比、规范地图锚定和规范包围盒校准约束，使不同姿态下的部件特征对应到稳定的规范空间。
  input: 物体点云、部件文本与训练规范空间监督
  output: 文本可查询的逐点部件表示
  stage: 训练规范分支；推理特征分支
  supervision: LLM 辅助对齐后的规范数据及部件语义配对
  origin: proposed
  origin_note: 本文设计的规范空间语义对齐流程；其预训练基础模型与通用组件沿用已有方法，不计作本文新提出。
  origin_refs:
  - url: https://openaccess.thecvf.com/content/CVPR2026/papers/Jin_CoSMo3D_Open-World_Promptable_3D_Semantic_Segmentation_through_LLM-Guided_Canonical_Spatial_CVPR_2026_paper.pdf
    locator: 方法部分列明的基础模型及其参考文献
  evidence:
  - &id001
    url: https://openaccess.thecvf.com/content/CVPR2026/papers/Jin_CoSMo3D_Open-World_Promptable_3D_Semantic_Segmentation_through_LLM-Guided_Canonical_Spatial_CVPR_2026_paper.pdf
    locator: 方法部分；Figure 2（PDF 第 3 页）；实验 Table 1（PDF 第 7 页）
  figure: figure2
  figure_guide: 左侧 Feature Extraction Branch 提取形状和文本特征；右侧 Canonical Embedding Branch 通过 map anchoring、box calibration
    与 semantic contrastive 约束规范空间，仅训练时使用。
  depicted: true
  route:
  - 点云与部件文本
  - 规范空间语义对齐
  - 逐点部件表示
  - 提示分割
  result_tables:
  - table1
  geometry:
    families:
    - canonical
    signal: 物体规范坐标、规范地图与包围盒监督
    mechanism: 训练规范嵌入分支，以 map anchoring 和 box calibration 保持空间锚点，并与语义对比约束共同优化，使姿态变化时部件对应更稳定。
    changes: 部件空间对应与训练约束
    stage: 训练规范分支；推理特征分支
    semantic_role: 规范空间为部件语义提供几何锚定；文本特征来自 SigLIP，几何不独立定义部件词义。
    route:
    - 规范空间与形状
    - 规范坐标锚定
    - 部件空间对应
    - 部件语义预测
    evidence:
    - *id001
results:
- id: table1
  label: Table 1
  asset: assets/results/cosmo3d-table1.png
  page: 7
  version: CVPR 2026 出版方正式版
  source_url: https://openaccess.thecvf.com/content/CVPR2026/papers/Jin_CoSMo3D_Open-World_Promptable_3D_Semantic_Segmentation_through_LLM-Guided_Canonical_Spatial_CVPR_2026_paper.pdf
  source_sha256: a9a51230835f61c7eb342f95627e71f3cb3a1eb87bf928af5bdacbeb50e187a1
  clip_pdf_points:
  - 55
  - 54
  - 558
  - 279
  title: CoSMo3D：主要实验结果
  setting: 粗粒度、细粒度、ShapeNet-Part、PartNet-E；保留重训练／微调星号。
  metrics: mIoU ↑
  reading: 这是物体部件及姿态泛化，不能当作室内多视角场景分割结果。
---

# CoSMo3D

本页按研究问题提取相关操作；模块原图、具体输入输出、来源与主要实验结果在上方展开查看。

## 研究问题

点云姿态变化时怎样稳定对应文本部件？

## 相关操作

以 Point Transformer 编码形状、SigLIP 编码文本；训练时增加规范坐标嵌入分支，通过语义对比、规范地图锚定和规范包围盒校准约束，使不同姿态下的部件特征对应到稳定的规范空间。

## 实验阅读

粗粒度、细粒度、ShapeNet-Part、PartNet-E；保留重训练／微调星号。 这是物体部件及姿态泛化，不能当作室内多视角场景分割结果。 主要结果是整套方法的效果，不能单凭该表归因到一个模块。

## 原文依据

- [出版方原文](https://openaccess.thecvf.com/content/CVPR2026/papers/Jin_CoSMo3D_Open-World_Promptable_3D_Semantic_Segmentation_through_LLM-Guided_Canonical_Spatial_CVPR_2026_paper.pdf)：方法部分；Figure 2（PDF 第 3 页）；实验 Table 1（PDF 第 7 页）。
- [官方实现](https://github.com/JinLi998/CoSMo3D)：已检查公开目录，未独立运行训练或评测。
