---
paper_id: octreegraph
title: Open-Vocabulary Octree-Graph for 3D Scene Understanding
short_name: OV-Octree-Graph
authors: []
year: 2025
preprint_date: '2024-11-25'
venue: ICCV
publication_status: published
primary_direction: multiview
modalities:
- point_cloud
- image
task_setting: open_vocabulary
task_types:
- semantic
- instance
techniques:
- geometry
- region_aggregation
- fusion
datasets:
- ScanNet
- Replica
paper_url: https://arxiv.org/abs/2411.16253
publication_url: https://openaccess.thecvf.com/content/ICCV2025/html/Wang_Open-Vocabulary_Octree-Graph_for_3D_Scene_Understanding_ICCV_2025_paper.html
code_status: public
code_url: https://github.com/yifeisu/OV-Octree-Graph
code_details: 公开实例构建、特征聚合及运行脚本；需外部二维模型与依赖。
content_status: index
checked_on: '2026-11-09'
summary: 融合RGB-D序列的区域与实例特征，以八叉树图表达三维语义。
sources:
- url: https://openaccess.thecvf.com/content/ICCV2025/html/Wang_Open-Vocabulary_Octree-Graph_for_3D_Scene_Understanding_ICCV_2025_paper.html
  locator: 正式发表来源
- url: https://github.com/yifeisu/OV-Octree-Graph
  locator: 官方 README / 公开目录；未运行
figures:
- id: fig2
  asset: assets/figures/octreegraph-fig2.png
  label: Figure 2
  page: 3
  version: arXiv 2411.16253v2
  source_url: https://arxiv.org/pdf/2411.16253v2
  clip_pdf_points:
  - 56
  - 45
  - 556
  - 310
  source_sha256: c38b5fc602bacf464d0606523e2ac025fee57424d5fdc5b12488df8e938b81d5
- id: fig3
  asset: assets/figures/octreegraph-fig3.png
  label: Figure 3
  page: 3
  version: arXiv 2411.16253v2
  source_url: https://arxiv.org/pdf/2411.16253v2
  clip_pdf_points:
  - 317
  - 391
  - 550
  - 448
  source_sha256: c38b5fc602bacf464d0606523e2ac025fee57424d5fdc5b12488df8e938b81d5
methods:
- id: cgsm
  track: pointcloud
  problems:
  - projection
  - multiview
  - regions
  title: 按时间分组的三维实例合并
  question: 不同视角的区域如何合并而避免欠分割扩散？
  operation: 将按时间排列的视图分组，投影区域得到三维片段；依据几何重叠与视觉／描述相似性合并，先组内再按序跨组合并；利用特征方差识别并剔除欠分割片段。
  input: 带位姿 RGB-D、二维区域及语义特征
  output: 跨视图一致三维实例
  stage: 地图构建／推理
  supervision: 预训练掩码及视觉语言模型；需要相机位姿
  origin: proposed
  origin_note: 本文 Chronological Group-wise Segment Merging；投影操作不是本文独创。
  origin_refs: []
  evidence:
  - url: https://arxiv.org/pdf/2411.16253v2
    locator: §3.1–3.3，Figure 2–3
  figure: fig3
  figure_guide: 独立图看时间分组和前一组合并结果的递推；具体几何／语义阈值按 §3.3。
  depicted: true
  route:
  - 二维区域特征
  - 时序分组区域合并
  - 三维实例片段
  - 二维到三维传递
- id: ifa
  track: vocabulary
  problems:
  - alignment
  - reliability
  title: 兼顾实例内部与相邻实例的特征聚合
  question: 三维实例的开放词汇特征如何聚合并区分邻居？
  operation: 先求实例特征中心；依据特征对本实例中心的相似度奖励一致观测，并减去对相似邻居中心的响应，softmax 归一化后加权聚合；视觉和描述特征分别处理，再融合用于文本查询。
  input: 每实例多视角视觉／描述特征、邻居实例
  output: 可文本查询的实例嵌入
  stage: 地图构建与查询
  supervision: 预训练视觉语言模型；无新增类别标签
  origin: proposed
  origin_note: 本文 Instance Feature Aggregation；本模块归开放词汇表示主线，而非按三维表示自动归点云。
  origin_refs: []
  evidence:
  - url: https://arxiv.org/pdf/2411.16253v2
    locator: §3.4，Figure 2(b)
  figure: fig2
  figure_guide: 看总图中下方 IFA：实例内部奖励、实例之间惩罚及视觉／描述融合。
  depicted: true
  route:
  - 二维区域特征
  - 实例内外对比聚合
  - 实例特征
  - 文本相似度分类
module_checked_on: '2026-11-09'
results:
- id: table1
  label: Table 1
  asset: assets/results/octreegraph-table1.png
  title: 多视角建图后的三维语义分割
  setting: Replica 与 ScanNet；原表分别列 OVSeg 与 ViT-H-14 作为 CLIP Backbone。
  metrics: mIoU ↑；F-mIoU ↑；mAcc ↑
  reading: 优先比较相同骨干的 Ours 与基线；保留原表的小数尺度，不另行换算为百分数。
  page: 6
  version: arXiv 2411.16253v2
  source_url: https://arxiv.org/pdf/2411.16253v2
  source_sha256: c38b5fc602bacf464d0606523e2ac025fee57424d5fdc5b12488df8e938b81d5
  clip_pdf_points:
  - 90
  - 72
  - 524
  - 247
- id: table2
  label: Table 2
  asset: assets/results/octreegraph-table2.png
  title: 三维实例分割主结果
  setting: ScanNet200；原表按监督掩码／zero-shot 掩码及监督语义／zero-shot 语义划分组别。
  metrics: AP ↑；AP50 ↑；AP25 ↑
  reading: 主要看 z.s. mask + z.s. semantic 组内 Ours 与相同设置方法；前两组使用监督掩码，条件不同。
  page: 6
  version: arXiv 2411.16253v2
  source_url: https://arxiv.org/pdf/2411.16253v2
  source_sha256: c38b5fc602bacf464d0606523e2ac025fee57424d5fdc5b12488df8e938b81d5
  clip_pdf_points:
  - 55
  - 261
  - 298
  - 486
---
# OV-Octree-Graph

## 当前整理状态

已按研究关注点核查下列方法模块与配图；尚未完成全文样例笔记，不据此生成实验排名。

## 收录理由

融合RGB-D序列的区域与实例特征，以八叉树图表达三维语义。

## 开源情况

【官方文档说明】公开实例构建、特征聚合及运行脚本；需外部二维模型与依赖。 本轮没有安装或运行代码，没有独立验证权重下载。
