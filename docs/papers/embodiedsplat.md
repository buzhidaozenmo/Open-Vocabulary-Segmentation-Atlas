---
paper_id: embodiedsplat
title: 'EmbodiedSplat: Online Feed-Forward Semantic 3DGS for Open-Vocabulary 3D Scene Understanding'
short_name: EmbodiedSplat
authors:
- Lee, Seungjun
- Wang, Zihan
- Wang, Yunsong
- Lee, Gim Hee
year: 2026
preprint_date: unknown
venue: CVPR
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
- ScanNet
- ScanNet++
- Replica
paper_url: https://openaccess.thecvf.com/content/CVPR2026/papers/Lee_EmbodiedSplat_Online_Feed-Forward_Semantic_3DGS_for_Open-Vocabulary_3D_Scene_Understanding_CVPR_2026_paper.pdf
publication_url: https://openaccess.thecvf.com/content/CVPR2026/html/Lee_EmbodiedSplat_Online_Feed-Forward_Semantic_3DGS_for_Open-Vocabulary_3D_Scene_Understanding_CVPR_2026_paper.html
code_status: public
code_url: https://github.com/0nandon/EmbodiedSplat
code_details: 已核对官方仓库实际实现目录：config、documents、download_data.py、modules、process_scannet.py、requirements.txt。运行及外部权重可用性未独立复现。
content_status: index
checked_on: '2026-11-09'
module_checked_on: '2026-11-09'
summary: 以全局 CLIP 码本和在线稀疏系数字段把二维语言特征绑定到每个高斯，避免存储完整稠密向量；再将高斯特征点云送入 3D U-Net 和时序记忆适配器，融合几何感知特征补偿二维语义。
sources:
- url: https://openaccess.thecvf.com/content/CVPR2026/html/Lee_EmbodiedSplat_Online_Feed-Forward_Semantic_3DGS_for_Open-Vocabulary_3D_Scene_Understanding_CVPR_2026_paper.html
  locator: 正式发表页面及作者信息
- url: https://openaccess.thecvf.com/content/CVPR2026/papers/Lee_EmbodiedSplat_Online_Feed-Forward_Semantic_3DGS_for_Open-Vocabulary_3D_Scene_Understanding_CVPR_2026_paper.pdf
  locator: 方法部分；Figure 2（PDF 第 3 页）；实验 Table 1（PDF 第 6 页）
- url: https://github.com/0nandon/EmbodiedSplat
  locator: 官方 README 与实际代码目录；不表示已运行
figures:
- id: figure2
  label: Figure 2
  asset: assets/figures/embodiedsplat-figure2.png
  page: 3
  version: CVPR 2026 出版方正式版
  source_url: https://openaccess.thecvf.com/content/CVPR2026/papers/Lee_EmbodiedSplat_Online_Feed-Forward_Semantic_3DGS_for_Open-Vocabulary_3D_Scene_Understanding_CVPR_2026_paper.pdf
  source_sha256: 81de9d28e160b67ba877e52157955fbdaa0b95eecf24065717a402b19b22f7ee
  clip_pdf_points:
  - 55
  - 50
  - 558
  - 214.9141387939453
methods:
- id: semantic-operation
  track: vocabulary
  problems:
  - alignment
  - efficiency
  title: 语义压缩与几何融合
  question: 在线高斯语义如何压缩并结合三维几何？
  operation: 以全局 CLIP 码本和在线稀疏系数字段把二维语言特征绑定到每个高斯，避免存储完整稠密向量；再将高斯特征点云送入 3D U-Net 和时序记忆适配器，融合几何感知特征补偿二维语义。
  input: 流式图像、前馈高斯、CLIP 特征及码本
  output: 带语义的在线高斯场
  stage: 模型训练、在线前馈重建及文本查询
  supervision: 二维语义教师及场景重建训练信号
  origin: proposed
  origin_note: 本文设计的语义压缩与几何融合流程；其预训练基础模型与通用组件沿用已有方法，不计作本文新提出。
  origin_refs:
  - url: https://openaccess.thecvf.com/content/CVPR2026/papers/Lee_EmbodiedSplat_Online_Feed-Forward_Semantic_3DGS_for_Open-Vocabulary_3D_Scene_Understanding_CVPR_2026_paper.pdf
    locator: 方法部分列明的基础模型及其参考文献
  evidence:
  - url: https://openaccess.thecvf.com/content/CVPR2026/papers/Lee_EmbodiedSplat_Online_Feed-Forward_Semantic_3DGS_for_Open-Vocabulary_3D_Scene_Understanding_CVPR_2026_paper.pdf
    locator: 方法部分；Figure 2（PDF 第 3 页）；实验 Table 1（PDF 第 6 页）
  figure: figure2
  figure_guide: 沿 CLIP Global Codebook 与 Sparse Coefficient Field 的二维语义绑定路径，再看 3D U-Net／时序记忆产生的几何感知特征如何融合到在线高斯。
  depicted: true
  route:
  - CLIP 与高斯几何
  - 语义压缩与几何融合
  - 高斯语义字段
  - 在线语义查询
  result_tables:
  - table1
results:
- id: table1
  label: Table 1
  asset: assets/results/embodiedsplat-table1.png
  page: 6
  version: CVPR 2026 出版方正式版
  source_url: https://openaccess.thecvf.com/content/CVPR2026/papers/Lee_EmbodiedSplat_Online_Feed-Forward_Semantic_3DGS_for_Open-Vocabulary_3D_Scene_Understanding_CVPR_2026_paper.pdf
  source_sha256: 81de9d28e160b67ba877e52157955fbdaa0b95eecf24065717a402b19b22f7ee
  clip_pdf_points:
  - 55
  - 54
  - 558
  - 277
  title: EmbodiedSplat：主要实验结果
  setting: ScanNet、ScanNet200、ScanNet++；保留重建时间及方法输入条件。
  metrics: mIoU／mAcc ↑，时间 ↓
  reading: 同时看分割指标与重建时间；二维模型与重建计算范围按原文设置解释。
---

# EmbodiedSplat

本页按研究问题提取相关操作；模块原图、具体输入输出、来源与主要实验结果在上方展开查看。

## 研究问题

在线高斯语义如何压缩并结合三维几何？

## 相关操作

以全局 CLIP 码本和在线稀疏系数字段把二维语言特征绑定到每个高斯，避免存储完整稠密向量；再将高斯特征点云送入 3D U-Net 和时序记忆适配器，融合几何感知特征补偿二维语义。

## 实验阅读

ScanNet、ScanNet200、ScanNet++；保留重建时间及方法输入条件。 同时看分割指标与重建时间；二维模型与重建计算范围按原文设置解释。 主要结果是整套方法的效果，不能单凭该表归因到一个模块。

## 原文依据

- [出版方原文](https://openaccess.thecvf.com/content/CVPR2026/papers/Lee_EmbodiedSplat_Online_Feed-Forward_Semantic_3DGS_for_Open-Vocabulary_3D_Scene_Understanding_CVPR_2026_paper.pdf)：方法部分；Figure 2（PDF 第 3 页）；实验 Table 1（PDF 第 6 页）。
- [官方实现](https://github.com/0nandon/EmbodiedSplat)：已检查公开目录，未独立运行训练或评测。
