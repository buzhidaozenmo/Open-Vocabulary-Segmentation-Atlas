---
paper_id: regionplc
title: 'RegionPLC: Regional Point-Language Contrastive Learning for Open-World 3D Scene Understanding'
short_name: RegionPLC
authors: []
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
- semantic
- instance
techniques:
- semantic_alignment
- region_aggregation
- fusion
datasets:
- ScanNet
- nuScenes
paper_url: https://arxiv.org/abs/2304.00962
publication_url: https://openaccess.thecvf.com/content/CVPR2024/papers/Yang_RegionPLC_Regional_Point-Language_Contrastive_Learning_for_Open-World_3D_Scene_Understanding_CVPR_2024_paper.pdf
code_status: public
code_url: https://github.com/CVMI-Lab/PLA/tree/regionplc
code_details: 实际实现位于 regionplc 分支；与 PLA 主分支分开。
content_status: index
checked_on: '2026-11-09'
summary: 以区域级语言监督与对比学习建立更密集的三维语言关联。
sources:
- url: https://openaccess.thecvf.com/content/CVPR2024/papers/Yang_RegionPLC_Regional_Point-Language_Contrastive_Learning_for_Open-World_3D_Scene_Understanding_CVPR_2024_paper.pdf
  locator: 正式发表来源
- url: https://github.com/CVMI-Lab/PLA/tree/regionplc
  locator: 官方 README / 公开目录；未运行
figures:
- id: fig1
  asset: assets/figures/regionplc-fig1.png
  label: Figure 1
  page: 3
  version: arXiv 2304.00962v4
  source_url: https://arxiv.org/pdf/2304.00962v4
  clip_pdf_points:
  - 48
  - 45
  - 548
  - 245
  source_sha256: 7db6afcc07c80355cd737eed900814ae5fa739e6c8da733d8963cebdaa0095ab
methods:
- id: sfusion
  track: pointcloud
  problems:
  - multiview
  - reliability
  title: 按三维区域重叠补充多来源描述
  question: 多种二维描述怎样融合而不重复或互相冲突？
  operation: 先选主描述源；对候选描述对应的点集计算与主源区域的最大 IoU，只加入落在阈值范围内的低重叠候选，并控制补充比例，减少高重叠区域的冗余或冲突监督。
  input: 不同描述器生成的区域点集—文本对
  output: 空间互补的训练配对集合
  stage: 训练前配对筛选
  supervision: 预训练检测／描述模型；支持基类标注或无三维标注设置
  origin: proposed
  origin_note: 本文提出 SFusion；区域点像素关联沿用原文引用的已有三维语言关联工作。
  origin_refs: []
  evidence:
  - url: https://arxiv.org/pdf/2304.00962v4
    locator: §3.2、§3.4，Eq.2，Figure 1
  figure: fig1
  figure_guide: 主图左下 3D-aware SFusion；重叠阈值筛选细节见 Eq.2，主图没有画出全部数值条件。
  depicted: true
  route:
  - 区域文本描述
  - 可靠性加权与选择
  - 点集文本对
  - 二维到三维传递
- id: rpdc
  track: pointcloud
  problems:
  - alignment
  - regions
  title: 逐点对比与区域大小归一化
  question: 区域监督怎样保留点的区分性？
  operation: 不先把全部点特征平均成一个区域向量，而是逐点计算与描述嵌入的匹配概率，再在区域内池化对数概率；按区域大小归一化，缓解大小区域梯度尺度不均。
  input: 点特征、区域描述嵌入与点集成员关系
  output: 具备局部区分性的语言对齐特征
  stage: 训练
  supervision: 区域点语言配对；任务设置决定是否另加基类标注
  origin: proposed
  origin_note: 本文的 region-aware point-discriminative contrastive learning。
  origin_refs: []
  evidence:
  - url: https://arxiv.org/pdf/2304.00962v4
    locator: §3.5，Eq.3–6，Figure 1
  figure: fig1
  figure_guide: 对比主图右侧 CLIP-style 与 Region-aware point-discriminative 两条优化路径。
  depicted: true
  route:
  - 区域文本描述
  - 逐点区域对比
  - 逐点特征
  - 对比学习
module_checked_on: '2026-11-09'
---
# RegionPLC

## 当前整理状态

已按研究关注点核查下列方法模块与配图；尚未完成全文样例笔记，不据此生成实验排名。

## 收录理由

以区域级语言监督与对比学习建立更密集的三维语言关联。

## 开源情况

【官方文档说明】实际实现位于 regionplc 分支；与 PLA 主分支分开。 本轮没有安装或运行代码，没有独立验证权重下载。
