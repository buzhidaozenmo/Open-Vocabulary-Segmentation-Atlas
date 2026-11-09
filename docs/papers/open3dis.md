---
paper_id: open3dis
title: 'Open3DIS: Open-Vocabulary 3D Instance Segmentation with 2D Mask Guidance'
short_name: Open3DIS
authors:
- Phuc Nguyen
- Tuan Duc Ngo
- Evangelos Kalogerakis
- Chuang Gan
- Anh Tran
- Cuong Pham
- Khoi Nguyen
year: 2024
preprint_date: unknown
venue: CVPR
publication_status: published
primary_direction: 3d
modalities:
- point_cloud
- image
task_setting: open_vocabulary
task_types:
- instance
techniques:
- geometry
- region_aggregation
- semantic_alignment
datasets:
- ScanNet
- S3DIS
- Replica
paper_url: https://openaccess.thecvf.com/content/CVPR2024/papers/Nguyen_Open3DIS_Open-Vocabulary_3D_Instance_Segmentation_with_2D_Mask_Guidance_CVPR_2024_paper.pdf
publication_url: https://openaccess.thecvf.com/content/CVPR2024/html/Nguyen_Open3DIS_Open-Vocabulary_3D_Instance_Segmentation_with_2D_Mask_Guidance_CVPR_2024_paper.html
code_status: public
code_url: https://github.com/VinAIResearch/Open3DIS
code_details: 官方仓库含实例提议、特征提取、评测、配置与数据准备文档；依赖二维模型及三维提议网络，未运行。
content_status: index
checked_on: '2026-11-09'
module_checked_on: '2026-11-09'
summary: 以二维掩码引导超点生长和跨帧合并，再以可见性累积实例语言特征。
sources:
- url: https://openaccess.thecvf.com/content/CVPR2024/html/Nguyen_Open3DIS_Open-Vocabulary_3D_Instance_Segmentation_with_2D_Mask_Guidance_CVPR_2024_paper.html
  locator: 正式发表：出版方页面／DOI；期刊状态另由官方仓库文档确认
- url: https://openaccess.thecvf.com/content/CVPR2024/papers/Nguyen_Open3DIS_Open-Vocabulary_3D_Instance_Segmentation_with_2D_Mask_Guidance_CVPR_2024_paper.pdf
  locator: 本次所读原文版本的 §3–5／III–V、方法图及主要结果表
- url: https://github.com/VinAIResearch/Open3DIS
  locator: 官方仓库实际目录与文档／项目页；未运行
figures:
- id: fig3
  label: Figure 3
  asset: assets/figures/open3dis-fig3.png
  page: 4
  version: CVPR 2024 出版方正式版
  source_url: https://openaccess.thecvf.com/content/CVPR2024/papers/Nguyen_Open3DIS_Open-Vocabulary_3D_Instance_Segmentation_with_2D_Mask_Guidance_CVPR_2024_paper.pdf
  clip_pdf_points:
  - 305
  - 50
  - 548
  - 246
  source_sha256: b08de32926f34a1740545224ccabe36152d72d073e4d0d3f662048cfcd626fbc
- id: fig4
  label: Figure 4
  asset: assets/figures/open3dis-fig4.png
  page: 5
  version: CVPR 2024 出版方正式版
  source_url: https://openaccess.thecvf.com/content/CVPR2024/papers/Nguyen_Open3DIS_Open-Vocabulary_3D_Instance_Segmentation_with_2D_Mask_Guidance_CVPR_2024_paper.pdf
  clip_pdf_points:
  - 305
  - 68
  - 548
  - 168
  source_sha256: b08de32926f34a1740545224ccabe36152d72d073e4d0d3f662048cfcd626fbc
methods:
- id: proposals
  track: pointcloud
  problems:
  - projection
  - multiview
  - regions
  title: 超点生长与跨帧层次合并
  question: 二维掩码怎样补充小物体和几何模糊对象的三维提议？
  operation: 投影超点并计算其与二维掩码的 IoU，以最大重叠超点为种子；只合并同时满足掩码重叠和三维特征相似条件的邻接超点。再按三维区域 IoU 与特征相似性跨帧凝聚合并，并与三维提议网络结果拼接去重。
  input: 二维实例掩码、点云超点、三维特征、RGB-D 相机信息
  output: 几何连贯的三维实例提议
  stage: 离线提议构建／推理
  supervision: 二维分割器与预训练三维提议／特征网络；需相机和深度，不等于全流程无监督
  origin: proposed
  origin_note: 本文 2D-Guided-3D 提议模块；超点、二维分割器及三维骨干沿用已有方法。
  origin_refs: []
  evidence:
  - url: https://openaccess.thecvf.com/content/CVPR2024/papers/Nguyen_Open3DIS_Open-Vocabulary_3D_Instance_Segmentation_with_2D_Mask_Guidance_CVPR_2024_paper.pdf
    locator: §3.1–3.2，Eq.1
  figure: fig3
  figure_guide: 独立模块图看 Per-frame Superpoint Merging 与层次 Agglomerative Clustering 两段。
  depicted: true
  route:
  - 二维区域掩码
  - 超点生长与跨帧合并
  - 三维实例片段
  - 二维到三维传递
- id: pointfeatures
  track: pointcloud
  problems:
  - projection
  - multiview
  - alignment
  title: 可见性累计逐点 CLIP 特征
  question: 同一实例在不同视图中的语义贡献怎样保留？
  operation: 为提议选择 top-λ 视图、多尺度裁切并提取 CLIP 特征；依据各视图的点可见性，把提议特征累计回可见点并归一化。实例文本分数为成员点与文本嵌入的平均余弦相似度。
  input: 三维提议、各视图可见性、区域 CLIP 特征
  output: 逐点 CLIP 表示与实例文本分数
  stage: 特征构建及推理
  supervision: 冻结 CLIP 与已有实例提议；需 RGB-D 视图
  origin: modified
  origin_note: 在 OpenMask3D 的多视图裁切特征基础上，改为三维感知的逐点累计与查询。
  origin_refs:
  - url: https://arxiv.org/abs/2306.13631
    locator: §3.3 以 OpenMask3D 多视图特征提取为基础
  evidence:
  - url: https://openaccess.thecvf.com/content/CVPR2024/papers/Nguyen_Open3DIS_Open-Vocabulary_3D_Instance_Segmentation_with_2D_Mask_Guidance_CVPR_2024_paper.pdf
    locator: §3.3，Eq.2–3
  figure: fig4
  figure_guide: 独立特征图按三维提议→投影／多尺度裁切→CLIP→逐点累积阅读。
  depicted: true
  route:
  - 二维区域特征
  - 可见性与跨视角融合
  - 逐点特征
  - 文本相似度分类
results:
- id: table2
  label: Table 2
  asset: assets/results/open3dis-table2.png
  page: 7
  version: CVPR 2024 出版方正式版
  source_url: https://openaccess.thecvf.com/content/CVPR2024/papers/Nguyen_Open3DIS_Open-Vocabulary_3D_Instance_Segmentation_with_2D_Mask_Guidance_CVPR_2024_paper.pdf
  clip_pdf_points:
  - 47
  - 68
  - 548
  - 254
  source_sha256: b08de32926f34a1740545224ccabe36152d72d073e4d0d3f662048cfcd626fbc
  title: ScanNet200 开放词汇实例分割
  setting: 原表保留全监督参照、各类三维提议和 only 2D／only 3D／combined 版本，† 表示适配后评测。
  metrics: AP／AP50／AP25 ↑；head／common／tail AP ↑
  reading: 比较 only 2D、only 3D 与合并版本，同时注意其三维提议骨干及训练来源。
---
# Open3DIS

## 资料范围与状态

核查版本：CVPR 2024 出版方正式版；正式发表来源另见出版方链接。已完成与研究关注点有关的方法、配图和主结果表定向整理，尚未完成全文样例笔记。图中的方法关系以原文为准，未独立运行实现。

## 关注的问题

【原文事实】以二维掩码引导超点生长和跨帧合并，再以可见性累积实例语言特征。

## 实验阅读

原表保留全监督参照、各类三维提议和 only 2D／only 3D／combined 版本，† 表示适配后评测。 比较 only 2D、only 3D 与合并版本，同时注意其三维提议骨干及训练来源。 数值保留在原始结果表中；它们是论文报告值，不是本库复现值。

## 开源情况

【官方文档说明／项目页核查】官方仓库含实例提议、特征提取、评测、配置与数据准备文档；依赖二维模型及三维提议网络，未运行。 本轮没有安装依赖、执行训练或验证复现结果。
