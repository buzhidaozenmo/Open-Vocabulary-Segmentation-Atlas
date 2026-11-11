---
paper_id: maskclustering
title: 'MaskClustering: View Consensus based Mask Graph Clustering for Open-Vocabulary 3D Instance Segmentation'
short_name: MaskClustering
authors:
- Mi Yan
- Jiazhao Zhang
- Yan Zhu
- He Wang
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
- ScanNet++
- ScanNet
- Matterport3D
paper_url: https://openaccess.thecvf.com/content/CVPR2024/papers/Yan_MaskClustering_View_Consensus_based_Mask_Graph_Clustering_for_Open-Vocabulary_3D_CVPR_2024_paper.pdf
publication_url: https://openaccess.thecvf.com/content/CVPR2024/html/Yan_MaskClustering_View_Consensus_based_Mask_Graph_Clustering_for_Open-Vocabulary_3D_CVPR_2024_paper.html
code_status: public
code_url: https://github.com/PKU-EPIC/MaskClustering
code_details: 官方仓库含 graph、main.py、evaluation、配置和 CropFormer 权重准备入口；本轮未运行。
content_status: index
checked_on: '2026-11-09'
module_checked_on: '2026-11-11'
summary: 用共同观察视角的合并共识构建掩码图，迭代聚类形成三维实例。
sources:
- url: https://openaccess.thecvf.com/content/CVPR2024/html/Yan_MaskClustering_View_Consensus_based_Mask_Graph_Clustering_for_Open-Vocabulary_3D_CVPR_2024_paper.html
  locator: 正式发表：出版方页面／DOI；期刊状态另由官方仓库文档确认
- url: https://openaccess.thecvf.com/content/CVPR2024/papers/Yan_MaskClustering_View_Consensus_based_Mask_Graph_Clustering_for_Open-Vocabulary_3D_CVPR_2024_paper.pdf
  locator: 本次所读原文版本的 §3–5／III–V、方法图及主要结果表
- url: https://github.com/PKU-EPIC/MaskClustering
  locator: 官方仓库实际目录与文档／项目页；未运行
figures:
- id: fig3
  label: Figure 3
  asset: assets/figures/maskclustering-fig3.png
  page: 4
  version: CVPR 2024 出版方正式版
  source_url: https://openaccess.thecvf.com/content/CVPR2024/papers/Yan_MaskClustering_View_Consensus_based_Mask_Graph_Clustering_for_Open-Vocabulary_3D_CVPR_2024_paper.pdf
  clip_pdf_points:
  - 305
  - 50
  - 548
  - 233
  source_sha256: bcddaa4b052720ef73bc38d82215cb020ccf8c432dd585625c92176853753270
- id: fig4
  label: Figure 4
  asset: assets/figures/maskclustering-fig4.png
  page: 5
  version: CVPR 2024 出版方正式版
  source_url: https://openaccess.thecvf.com/content/CVPR2024/papers/Yan_MaskClustering_View_Consensus_based_Mask_Graph_Clustering_for_Open-Vocabulary_3D_CVPR_2024_paper.pdf
  clip_pdf_points:
  - 305
  - 68
  - 548
  - 162
  source_sha256: bcddaa4b052720ef73bc38d82215cb020ccf8c432dd585625c92176853753270
methods:
- id: consensus
  track: pointcloud
  problems:
  - multiview
  - regions
  - reliability
  title: 以共同观察视图的支持比例判断同实例
  question: 几何重叠很低的跨视角掩码怎样判断应当合并？
  operation: 找出两掩码同时可见的观察帧；若某观察帧存在一个掩码近似包含两者的可见点集，则计为支持。以支持帧数／观察帧数作为 view consensus rate，超过阈值才在掩码图中连边。
  input: 二维掩码及对应三维点集、各帧可见关系
  output: 全局掩码图的共识边
  stage: 推理／实例构建
  supervision: 预训练二维掩码预测器、相机与深度；该聚类方法不另训练
  origin: proposed
  origin_note: 本文 view consensus rate，不是简单两帧 IoU。
  origin_refs: []
  evidence:
  - &id001
    url: https://openaccess.thecvf.com/content/CVPR2024/papers/Yan_MaskClustering_View_Consensus_based_Mask_Graph_Clustering_for_Open-Vocabulary_3D_CVPR_2024_paper.pdf
    locator: §3.2.1–3.2.2，Eq.1–3
  figure: fig3
  figure_guide: 独立共识图中两掩码共被三帧观察、两帧支持，例子给出 2/3 共识；阈值策略另见原文。
  depicted: true
  route:
  - 二维区域掩码
  - 多视角掩码共识
  - 掩码图
  - 实例构建
  geometry:
    families:
    - visibility
    - affinity
    signal: 掩码提升后的三维点集与共同可见帧
    mechanism: 先确定两掩码的共同观察帧，再统计其中有单个掩码近似包含两者可见点集的支持比例，以共识阈值建立掩码图边。
    changes: 掩码图边与实例聚类
    stage: 推理实例构建
    semantic_role: 几何共视是建立共识边的依据，实例类别另外由语言对齐特征给出。
    route:
    - 深度与相机几何
    - 共视掩码共识
    - 区域邻接图
    - 实例构建
    evidence:
    - *id001
- id: clustering
  track: pointcloud
  problems:
  - regions
  - reliability
  - alignment
  title: 先可信边聚类，再汇聚实例语言特征
  question: 怎样避免少量观察和欠分割掩码导致错误传播？
  operation: 用跨帧掩码 ID 分布的分散程度过滤欠分割节点；优先使用观察者多的边合并连通分量，更新节点及共识，逐轮降低观察数门槛。最终沿用 OpenMask3D，选覆盖较好的视图掩码、多尺度裁切并平均 CLIP
    特征。
  input: 掩码共识图、多帧 RGB、CLIP 编码器
  output: 三维实例及其语言特征
  stage: 推理／特征构建
  supervision: 预训练二维掩码模型与 CLIP；不另训练聚类网络
  origin: modified
  origin_note: 图更新与欠分割过滤为本文设计；末尾语言特征提取明确沿用 OpenMask3D。
  origin_refs:
  - url: https://arxiv.org/abs/2306.13631
    locator: §3.4 明确 Following OpenMask3D
  evidence:
  - url: https://openaccess.thecvf.com/content/CVPR2024/papers/Yan_MaskClustering_View_Consensus_based_Mask_Graph_Clustering_for_Open-Vocabulary_3D_CVPR_2024_paper.pdf
    locator: §3.2.3–3.4
  figure: fig4
  figure_guide: 独立迭代聚类图显示观察数门槛与图更新；过滤及 CLIP 裁切聚合未画出，分别看 §3.2.3 和 §3.4。
  depicted: false
  route:
  - 二维区域掩码
  - 可信掩码图聚类
  - 实例特征
  - 文本相似度分类
results:
- id: table1
  label: Table 1
  asset: assets/results/maskclustering-table1.png
  page: 6
  version: CVPR 2024 出版方正式版
  source_url: https://openaccess.thecvf.com/content/CVPR2024/papers/Yan_MaskClustering_View_Consensus_based_Mask_Graph_Clustering_for_Open-Vocabulary_3D_CVPR_2024_paper.pdf
  clip_pdf_points:
  - 47
  - 68
  - 548
  - 189
  source_sha256: bcddaa4b052720ef73bc38d82215cb020ccf8c432dd585625c92176853753270
  title: 零样本三维实例分割
  setting: ScanNet++、Matterport3D；同时报告带语义类别和类别无关的实例分割。
  metrics: AP／AP50／AP25 ↑
  reading: Semantic 列包含分类效果，Class-agnostic 列更直接反映几何实例提议质量，两者分开看。
---
# MaskClustering

## 资料范围与状态

核查版本：CVPR 2024 出版方正式版；正式发表来源另见出版方链接。已完成与研究关注点有关的方法、配图和主结果表定向整理，尚未完成全文样例笔记。图中的方法关系以原文为准，未独立运行实现。

## 关注的问题

【原文事实】用共同观察视角的合并共识构建掩码图，迭代聚类形成三维实例。

## 实验阅读

ScanNet++、Matterport3D；同时报告带语义类别和类别无关的实例分割。 Semantic 列包含分类效果，Class-agnostic 列更直接反映几何实例提议质量，两者分开看。 数值保留在原始结果表中；它们是论文报告值，不是本库复现值。

## 开源情况

【官方文档说明／项目页核查】官方仓库含 graph、main.py、evaluation、配置和 CropFormer 权重准备入口；本轮未运行。 本轮没有安装依赖、执行训练或验证复现结果。
