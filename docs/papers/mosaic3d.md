---
paper_id: mosaic3d
title: 'Mosaic3D: Foundation Dataset and Model for Open-Vocabulary 3D Segmentation'
short_name: Mosaic3D
authors:
- Junha Lee
- Chunghyun Park
- Jaesung Choe
- Yu-Chiang Frank Wang
- Jan Kautz
- Minsu Cho
- Chris Choy
year: 2025
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
- region_aggregation
- fusion
datasets:
- ScanNet
- ScanNet++
- Matterport3D
paper_url: https://openaccess.thecvf.com/content/CVPR2025/papers/Lee_Mosaic3D_Foundation_Dataset_and_Model_for_Open-Vocabulary_3D_Segmentation_CVPR_2025_paper.pdf
publication_url: https://openaccess.thecvf.com/content/CVPR2025/html/Lee_Mosaic3D_Foundation_Dataset_and_Model_for_Open-Vocabulary_3D_Segmentation_CVPR_2025_paper.html
code_status: public
code_url: https://github.com/NVlabs/Mosaic3D
code_details: 官方仓库含训练评测、配置、数据处理和 Model Zoo；依赖 Segment3D 等外部模型，未运行或验证权重下载。
content_status: index
checked_on: '2026-11-09'
module_checked_on: '2026-11-09'
summary: 由多视图生成三维区域描述配对，再训练语言对齐点云编码器及实例解码器。
sources:
- url: https://openaccess.thecvf.com/content/CVPR2025/html/Lee_Mosaic3D_Foundation_Dataset_and_Model_for_Open-Vocabulary_3D_Segmentation_CVPR_2025_paper.html
  locator: 正式发表：出版方页面／DOI；期刊状态另由官方仓库文档确认
- url: https://openaccess.thecvf.com/content/CVPR2025/papers/Lee_Mosaic3D_Foundation_Dataset_and_Model_for_Open-Vocabulary_3D_Segmentation_CVPR_2025_paper.pdf
  locator: 本次所读原文版本的 §3–5／III–V、方法图及主要结果表
- url: https://github.com/NVlabs/Mosaic3D
  locator: 官方仓库实际目录与文档／项目页；未运行
figures:
- id: fig3
  label: Figure 3
  asset: assets/figures/mosaic3d-fig3.png
  page: 4
  version: CVPR 2025 出版方正式版
  source_url: https://openaccess.thecvf.com/content/CVPR2025/papers/Lee_Mosaic3D_Foundation_Dataset_and_Model_for_Open-Vocabulary_3D_Segmentation_CVPR_2025_paper.pdf
  clip_pdf_points:
  - 55
  - 50
  - 558
  - 184
  source_sha256: 1a9b55cb26a0adae3cc8c61cec09d808f2bd33d9da9fdb468bc070c11b80beb6
- id: fig5
  label: Figure 5
  asset: assets/figures/mosaic3d-fig5.png
  page: 5
  version: CVPR 2025 出版方正式版
  source_url: https://openaccess.thecvf.com/content/CVPR2025/papers/Lee_Mosaic3D_Foundation_Dataset_and_Model_for_Open-Vocabulary_3D_Segmentation_CVPR_2025_paper.pdf
  clip_pdf_points:
  - 55
  - 50
  - 558
  - 238
  source_sha256: 1a9b55cb26a0adae3cc8c61cec09d808f2bd33d9da9fdb468bc070c11b80beb6
methods:
- id: association
  track: pointcloud
  problems:
  - projection
  - multiview
  - alignment
  title: 区域描述与深度一致的像素—点配对
  question: 怎样把精确二维区域及描述变成三维监督？
  operation: 用 Grounded-SAM／SEEM 生成区域，区域感知 VLM Osprey 为其生成描述；将点投影到各图像，只有像素在掩码内且投影深度与深度图差值低于阈值时，才赋予该区域描述。
  input: 多视图 RGB-D、相机参数、二维区域及描述
  output: 三维掩码—文本配对
  stage: 离线数据构建
  supervision: 预训练分割与描述模型、带位姿和深度的场景；配对生成不需要人工三维语义标签
  origin: proposed
  origin_note: 本文数据引擎；调用的二维分割、描述模型及基础投影沿用已有技术。
  origin_refs: []
  evidence:
  - url: https://openaccess.thecvf.com/content/CVPR2025/papers/Lee_Mosaic3D_Foundation_Dataset_and_Model_for_Open-Vocabulary_3D_Segmentation_CVPR_2025_paper.pdf
    locator: §3.1，Eq.1
  figure: fig3
  figure_guide: 独立数据引擎图按 (a) 区域→(b) 描述→(c) Projection & Inclusion Test→(d) 配对阅读。
  depicted: true
  route:
  - 区域文本描述
  - 深度一致投影配对
  - 点集文本对
  - 二维到三维传递
  result_tables:
  - table1
- id: decoder
  track: pointcloud
  problems:
  - regions
  - alignment
  title: 多视图描述合并与语言实例解码
  question: 如何把分散的视图描述变成可直接预测的三维实例？
  operation: 先以区域语言对比训练点云编码器；再按 IoU 将多视图区域描述匹配到 Segment3D 实例，同一实例保留多条描述。用语言点特征及采样位置查询训练 Mask3D 式解码器，结合二值掩码损失与掩码描述对比，预测语言对齐实例。
  input: 语言点特征、Segment3D 实例、区域描述集合
  output: 实例掩码及语言嵌入
  stage: 两阶段训练；推理仅需点云与文本
  supervision: 预训练 Segment3D 伪实例及生成描述；不使用人工三维类别标签，但依赖已有模型
  origin: modified
  origin_note: 编码器采用区域对比思路；解码器沿用 Mask3D，本文加入描述合并及语言实例监督。
  origin_refs:
  - url: https://arxiv.org/abs/2304.00962
    locator: 本文区域对比训练所引 RegionPLC
  - url: https://github.com/JonasSchult/Mask3D
    locator: §4.2 明确使用 Mask3D 解码架构
  evidence:
  - url: https://openaccess.thecvf.com/content/CVPR2025/papers/Lee_Mosaic3D_Foundation_Dataset_and_Model_for_Open-Vocabulary_3D_Segmentation_CVPR_2025_paper.pdf
    locator: §4.1–4.2，Algorithm 1，Eq.2–5
  figure: fig5
  figure_guide: 模型图展示两阶段和 mask decoder；跨视图描述的 IoU 归并由 Algorithm 1 描述，未完整画入主图。
  depicted: true
  route:
  - 区域文本描述
  - 实例描述合并与解码
  - 实例特征
  - 文本相似度分类
  result_tables:
  - table2
results:
- id: table1
  label: Table 1
  asset: assets/results/mosaic3d-table1.png
  page: 7
  version: CVPR 2025 出版方正式版
  source_url: https://openaccess.thecvf.com/content/CVPR2025/papers/Lee_Mosaic3D_Foundation_Dataset_and_Model_for_Open-Vocabulary_3D_Segmentation_CVPR_2025_paper.pdf
  clip_pdf_points:
  - 55
  - 68
  - 558
  - 245
  source_sha256: 1a9b55cb26a0adae3cc8c61cec09d808f2bd33d9da9fdb468bc070c11b80beb6
  title: 多数据集三维开放词汇语义分割
  setting: ScanNet20／200、ScanNet++、Matterport3D；不计背景类；原表保留 Source Datasets 与训练数据组合。
  metrics: f-mIoU ↑；f-mAcc ↑
  reading: 区分仅 ScanNet 训练与全量多数据集训练的 Mosaic3D，不能把所有提升都归因于架构。
- id: table2
  label: Table 2
  asset: assets/results/mosaic3d-table2.png
  page: 7
  version: CVPR 2025 出版方正式版
  source_url: https://openaccess.thecvf.com/content/CVPR2025/papers/Lee_Mosaic3D_Foundation_Dataset_and_Model_for_Open-Vocabulary_3D_Segmentation_CVPR_2025_paper.pdf
  clip_pdf_points:
  - 55
  - 250
  - 558
  - 501
  source_sha256: 1a9b55cb26a0adae3cc8c61cec09d808f2bd33d9da9fdb468bc070c11b80beb6
  title: ScanNet200 三维开放词汇实例分割
  setting: 原表按推理输入、三维提议网络以及是否需要二维 CLIP 推理分组；保留时延列。
  metrics: mAP／mAP50／mAP25 ↑；Latency ↓
  reading: 先核对 3D／3D+2D 输入及提议网络，再比较各组结果与时延。
---
# Mosaic3D

## 资料范围与状态

核查版本：CVPR 2025 出版方正式版；正式发表来源另见出版方链接。已完成与研究关注点有关的方法、配图和主结果表定向整理，尚未完成全文样例笔记。图中的方法关系以原文为准，未独立运行实现。

## 关注的问题

【原文事实】由多视图生成三维区域描述配对，再训练语言对齐点云编码器及实例解码器。

## 实验阅读

ScanNet20／200、ScanNet++、Matterport3D；不计背景类；原表保留 Source Datasets 与训练数据组合。 区分仅 ScanNet 训练与全量多数据集训练的 Mosaic3D，不能把所有提升都归因于架构。 数值保留在原始结果表中；它们是论文报告值，不是本库复现值。

## 开源情况

【官方文档说明／项目页核查】官方仓库含训练评测、配置、数据处理和 Model Zoo；依赖 Segment3D 等外部模型，未运行或验证权重下载。 本轮没有安装依赖、执行训练或验证复现结果。
