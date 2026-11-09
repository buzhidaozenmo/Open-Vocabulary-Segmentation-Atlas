---
paper_id: geoguide
title: 'GeoGuide: Hierarchical Geometric Guidance for Open-Vocabulary 3D Semantic Segmentation'
short_name: GeoGuide
authors: []
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
- feature_distillation
- geometry
- region_aggregation
- reliability
datasets:
- ScanNet
- Matterport3D
- nuScenes
paper_url: https://arxiv.org/abs/2603.26260
publication_url: https://openaccess.thecvf.com/content/CVPR2026/html/Tao_GeoGuide_Hierarchical_Geometric_Guidance_for_Open-Vocabulary_3D_Semantic_Segmentation_CVPR_2026_paper.html
code_status: unconfirmed
code_url: ''
code_details: 尚未找到可核实的官方公开实现入口；不能据此断言作者明确不开源。
content_status: index
checked_on: '2026-11-09'
summary: 从超点、实例内部和实例之间建立几何语义一致性。
sources:
- url: https://openaccess.thecvf.com/content/CVPR2026/html/Tao_GeoGuide_Hierarchical_Geometric_Guidance_for_Open-Vocabulary_3D_Semantic_Segmentation_CVPR_2026_paper.html
  locator: 正式发表来源
figures:
- id: fig2
  asset: assets/figures/geoguide-fig2.png
  label: Figure 2
  page: 4
  version: arXiv 2603.26260v1
  source_url: https://arxiv.org/pdf/2603.26260v1
  clip_pdf_points:
  - 56
  - 45
  - 556
  - 278
  source_sha256: f88d3230fcf875771ed99b06862b5abd82a0a56795780aae434a3b62c5bfcb12
- id: fig4
  asset: assets/figures/geoguide-fig4.png
  label: Figure 4
  page: 5
  version: arXiv 2603.26260v1
  source_url: https://arxiv.org/pdf/2603.26260v1
  clip_pdf_points:
  - 56
  - 45
  - 298
  - 164
  source_sha256: f88d3230fcf875771ed99b06862b5abd82a0a56795780aae434a3b62c5bfcb12
methods:
- id: usd
  track: pointcloud
  problems:
  - reliability
  - distillation
  - regions
  title: 几何与语义残差预测二维教师可靠性
  question: 超点内哪些二维特征更值得蒸馏？
  operation: 分别计算点几何／二维语义与其超点均值的差，拼接后经 MLP 预测可靠性权重；加权池化二维语义，并用点级、超点级余弦损失监督三维语义适配器。
  input: 点几何、投影二维特征、超点划分
  output: 可靠性加权目标与三维语义
  stage: 训练
  supervision: 冻结三维骨干与二维教师；训练适配器及模块
  origin: proposed
  origin_note: 本文 Uncertainty-Based Superpoint Distillation；本轮未验证官方实现。
  origin_refs: []
  evidence:
  - url: https://arxiv.org/pdf/2603.26260v1
    locator: §3.3.1，Eq.2–4，Figure 4
  figure: fig4
  figure_guide: 独立 USD 图：减去超点均值、拼接、MLP、weight pooling、Cosine Similarity Loss。
  depicted: true
  route:
  - 二维与三维语义
  - 可靠性加权与选择
  - 超点特征
  - 特征蒸馏
- id: relations
  track: pointcloud
  problems:
  - geometry
  - regions
  title: 实例重建与实例间关系一致性
  question: 局部对齐后如何约束完整实例及实例关系？
  operation: 随机遮掉实例掩码的一部分，对剩余语义特征池化，按其与全场景点的相似度重建完整掩码；另对实例级几何和语义特征构造两两相似矩阵并施加一致性约束。
  input: 类别无关三维实例掩码、几何与语义特征
  output: 实例内及实例间一致的语义
  stage: 训练
  supervision: 已有类别无关三维实例方法产生的掩码；无需手工类别标签
  origin: proposed
  origin_note: 本文 IMR 与 IIRC 两项约束；实例掩码生成器沿用已有方法。
  origin_refs: []
  evidence:
  - url: https://arxiv.org/pdf/2603.26260v1
    locator: §3.3.2–3.3.3，Eq.5–9，Figure 2
  figure: fig2
  figure_guide: 总图右侧中部 IMR 和底部 Inter-Instance Relationship Consistency；原图没有逐项展开所有公式。
  depicted: true
  route:
  - 三维几何先验
  - 实例与关系约束
  - 实例特征
  - 几何一致性约束
module_checked_on: '2026-11-09'
---
# GeoGuide

## 当前整理状态

已按研究关注点核查下列方法模块与配图；尚未完成全文样例笔记，不据此生成实验排名。

## 收录理由

从超点、实例内部和实例之间建立几何语义一致性。

## 开源情况

【官方文档说明】尚未找到可核实的官方公开实现入口；不能据此断言作者明确不开源。 本轮没有安装或运行代码，没有独立验证权重下载。
