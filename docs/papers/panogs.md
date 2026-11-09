---
paper_id: panogs
title: 'PanoGS: Gaussian-based Panoptic Segmentation for 3D Open Vocabulary Scene Understanding'
short_name: PanoGS
authors:
- Zhai, Hongjia
- Li, Hai
- Li, Zhenzhe
- Pan, Xiaokun
- He, Yijia
- Zhang, Guofeng
year: 2025
preprint_date: unknown
venue: CVPR
publication_status: published
primary_direction: 3dgs
modalities:
- gaussian
- image
task_setting: open_vocabulary
task_types:
- panoptic
techniques:
- semantic_alignment
datasets:
- ScanNet
- Replica
paper_url: https://openaccess.thecvf.com/content/CVPR2025/papers/Zhai_PanoGS_Gaussian-based_Panoptic_Segmentation_for_3D_Open_Vocabulary_Scene_Understanding_CVPR_2025_paper.pdf
publication_url: https://openaccess.thecvf.com/content/CVPR2025/html/Zhai_PanoGS_Gaussian-based_Panoptic_Segmentation_for_3D_Open_Vocabulary_Scene_Understanding_CVPR_2025_paper.html
code_status: public
code_url: https://github.com/zhaihongjia/PanoGS
code_details: 已核对官方仓库实际实现目录：configs、datasets、decoders、environment.yml、eval_replica.py、eval_scannet.py。运行及外部权重可用性未独立复现。
content_status: index
checked_on: '2026-11-09'
module_checked_on: '2026-11-09'
summary: 把回投融合的二维特征云作为监督，用金字塔三平面与解码器学习连续高斯语言表示；结合语言和几何图割形成超基元，再根据二维 SAM 掩码分布定义边亲和并聚类得到实例。
sources:
- url: https://openaccess.thecvf.com/content/CVPR2025/html/Zhai_PanoGS_Gaussian-based_Panoptic_Segmentation_for_3D_Open_Vocabulary_Scene_Understanding_CVPR_2025_paper.html
  locator: 正式发表页面及作者信息
- url: https://openaccess.thecvf.com/content/CVPR2025/papers/Zhai_PanoGS_Gaussian-based_Panoptic_Segmentation_for_3D_Open_Vocabulary_Scene_Understanding_CVPR_2025_paper.pdf
  locator: 方法部分；Figure 2（PDF 第 3 页）；实验 Table 1（PDF 第 6 页）
- url: https://github.com/zhaihongjia/PanoGS
  locator: 官方 README 与实际代码目录；不表示已运行
figures:
- id: figure2
  label: Figure 2
  asset: assets/figures/panogs-figure2.png
  page: 3
  version: CVPR 2025 出版方正式版
  source_url: https://openaccess.thecvf.com/content/CVPR2025/papers/Zhai_PanoGS_Gaussian-based_Panoptic_Segmentation_for_3D_Open_Vocabulary_Scene_Understanding_CVPR_2025_paper.pdf
  source_sha256: 1d206aebca1a83de8eda5cd378123f80a68bf87eacb92c3e19a694b8df78f49c
  clip_pdf_points:
  - 55
  - 50
  - 558
  - 238.67697143554688
methods:
- id: semantic-operation
  track: vocabulary
  problems:
  - alignment
  - regions
  title: 连续语言场与图聚类
  question: 如何将多视角语言语义关联到可分实例的高斯？
  operation: 把回投融合的二维特征云作为监督，用金字塔三平面与解码器学习连续高斯语言表示；结合语言和几何图割形成超基元，再根据二维 SAM 掩码分布定义边亲和并聚类得到实例。
  input: 位姿 RGB-D、多视角语言特征、SAM 掩码
  output: 三维语义高斯与一致实例
  stage: 场景优化、图聚类及文本查询
  supervision: 二维语言教师、SAM 掩码及 RGB-D 重建
  origin: proposed
  origin_note: 本文设计的连续语言场与图聚类流程；其预训练基础模型与通用组件沿用已有方法，不计作本文新提出。
  origin_refs:
  - url: https://openaccess.thecvf.com/content/CVPR2025/papers/Zhai_PanoGS_Gaussian-based_Panoptic_Segmentation_for_3D_Open_Vocabulary_Scene_Understanding_CVPR_2025_paper.pdf
    locator: 方法部分列明的基础模型及其参考文献
  evidence:
  - url: https://openaccess.thecvf.com/content/CVPR2025/papers/Zhai_PanoGS_Gaussian-based_Panoptic_Segmentation_for_3D_Open_Vocabulary_Scene_Understanding_CVPR_2025_paper.pdf
    locator: 方法部分；Figure 2（PDF 第 3 页）；实验 Table 1（PDF 第 6 页）
  figure: figure2
  figure_guide: (a) 重建高斯并关联三平面语言码，(b) 反投影融合特征监督语言字段，(c) 语言几何图割与 SAM 边亲和生成一致实例。
  depicted: true
  route:
  - 二维语言与 SAM
  - 连续语言场与图聚类
  - 三维实例语义表示
  - 全景语义查询
  result_tables:
  - table1
results:
- id: table1
  label: Table 1
  asset: assets/results/panogs-table1.png
  page: 6
  version: CVPR 2025 出版方正式版
  source_url: https://openaccess.thecvf.com/content/CVPR2025/papers/Zhai_PanoGS_Gaussian-based_Panoptic_Segmentation_for_3D_Open_Vocabulary_Scene_Understanding_CVPR_2025_paper.pdf
  source_sha256: 1d206aebca1a83de8eda5cd378123f80a68bf87eacb92c3e19a694b8df78f49c
  clip_pdf_points:
  - 55
  - 53
  - 299
  - 211
  title: PanoGS：主要实验结果
  setting: ScanNetV2 的三维语义／全景协议；保留重实现星号及高斯过滤条件。
  metrics: mIoU／mAcc／PQ ↑
  reading: 本表包含分割和全景指标，逐列比较，不混合其单位。
---

# PanoGS

本页按研究问题提取相关操作；模块原图、具体输入输出、来源与主要实验结果在上方展开查看。

## 研究问题

如何将多视角语言语义关联到可分实例的高斯？

## 相关操作

把回投融合的二维特征云作为监督，用金字塔三平面与解码器学习连续高斯语言表示；结合语言和几何图割形成超基元，再根据二维 SAM 掩码分布定义边亲和并聚类得到实例。

## 实验阅读

ScanNetV2 的三维语义／全景协议；保留重实现星号及高斯过滤条件。 本表包含分割和全景指标，逐列比较，不混合其单位。 主要结果是整套方法的效果，不能单凭该表归因到一个模块。

## 原文依据

- [出版方原文](https://openaccess.thecvf.com/content/CVPR2025/papers/Zhai_PanoGS_Gaussian-based_Panoptic_Segmentation_for_3D_Open_Vocabulary_Scene_Understanding_CVPR_2025_paper.pdf)：方法部分；Figure 2（PDF 第 3 页）；实验 Table 1（PDF 第 6 页）。
- [官方实现](https://github.com/zhaihongjia/PanoGS)：已检查公开目录，未独立运行训练或评测。
