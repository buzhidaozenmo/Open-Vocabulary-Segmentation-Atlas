---
paper_id: superpointtransformer
title: Efficient 3D Semantic Segmentation with Superpoint Transformer
short_name: Superpoint Transformer
authors:
- Robert, Damien
- Raguet, Hugo
- Landrieu, Loic
year: 2023
preprint_date: unknown
venue: ICCV
publication_status: published
primary_direction: 3d
modalities:
- point_cloud
task_setting: supervised_segmentation
task_types:
- semantic
techniques:
- geometry
- region_aggregation
datasets:
- S3DIS
- KITTI-360
- DALES
paper_url: https://openaccess.thecvf.com/content/ICCV2023/papers/Robert_Efficient_3D_Semantic_Segmentation_with_Superpoint_Transformer_ICCV_2023_paper.pdf
publication_url: https://openaccess.thecvf.com/content/ICCV2023/html/Robert_Efficient_3D_Semantic_Segmentation_with_Superpoint_Transformer_ICCV_2023_paper.html
code_status: public
code_url: https://github.com/drprojects/superpoint_transformer
code_details: 官方仓库公开分区与模型实现、训练评测配置、安装和预训练资源说明；部分分区依赖需编译，未运行。
content_status: index
checked_on: '2026-11-11'
module_checked_on: '2026-11-11'
summary: 把几何与颜色信号分割成层级超点，在同层邻接图与跨层父子结构上进行注意力交互。
sources:
- url: https://openaccess.thecvf.com/content/ICCV2023/html/Robert_Efficient_3D_Semantic_Segmentation_with_Superpoint_Transformer_ICCV_2023_paper.html
  locator: 出版方正式发表记录
- url: https://openaccess.thecvf.com/content/ICCV2023/papers/Robert_Efficient_3D_Semantic_Segmentation_with_Superpoint_Transformer_ICCV_2023_paper.pdf
  locator: 按模块列出的原文章节、原图及结果表
- url: https://github.com/drprojects/superpoint_transformer
  locator: 官方 README 与根目录；未独立运行
figures:
- id: fig2
  label: Figure 2
  asset: assets/figures/superpointtransformer-fig2.png
  page: 3
  version: ICCV 2023 出版方正式版
  source_url: https://openaccess.thecvf.com/content/ICCV2023/papers/Robert_Efficient_3D_Semantic_Segmentation_with_Superpoint_Transformer_ICCV_2023_paper.pdf
  source_sha256: 054ac559a61e1141b9c84a96a09556e1707bff7a6268174474f05a8377955337
  clip_pdf_points:
  - 48
  - 70
  - 290
  - 425
methods:
- id: hierarchical-partition
  track: pointcloud
  problems:
  - geometry
  title: 几何分区、层级超点图与区域注意力
  question: 几何怎样直接决定区域以及区域间信息流？
  operation: 以局部几何／颜色特征及空间近邻图建立分段常量近似，用图正则和 cut pursuit 求超点；逐层增加粒度形成父子结构。同层按近邻超点连边，以相对位置和区域特征进行层级注意力，分类最细超点。
  input: 点云几何／颜色、近邻图
  output: 层级超点与区域语义预测
  stage: 分区预处理；监督训练与推理
  supervision: 几何分区本身不需类别标签，分割网络训练需要语义标注
  origin: proposed
  origin_note: 本文框架中的具体设计；预训练骨干与基础算子不视为本文首创。
  evidence:
  - &id001
    locator: §3.1–3.3，Figure 2–3，Table 2
    url: https://openaccess.thecvf.com/content/ICCV2023/papers/Robert_Efficient_3D_Semantic_Segmentation_with_Superpoint_Transformer_ICCV_2023_paper.pdf
  figure: fig2
  figure_guide: 按 (a) 点云→(c)(e) 两级分区→(d)(f) 对应邻接图阅读；注意力网络细节另见 Figure 3。
  depicted: true
  route:
  - 点云几何与颜色
  - 层级超点分区
  - 区域邻接图
  - 监督语义分割
  geometry:
    families:
    - coordinates
    - superpoints
    - affinity
    signal: 局部几何／颜色、空间近邻、超点质心及层级父子结构
    mechanism: 几何同质性用于分区，空间邻接限制同层注意力，父子结构控制跨尺度聚合。
    changes: 区域划分、同层边、跨层连接与区域特征
    stage: 分区预处理；训练与推理
    semantic_role: 几何定义预测单元和信息流；类别语义由监督训练学习，原文不声称开放词汇。
    route:
    - 超点与区域结构
    - 层级分区与图注意力
    - 区域邻接图
    - 区域语义预测
    evidence:
    - *id001
results:
- id: table2
  label: Table 2
  asset: assets/results/superpointtransformer-table2.png
  page: 7
  version: ICCV 2023 出版方正式版
  source_url: https://openaccess.thecvf.com/content/ICCV2023/papers/Robert_Efficient_3D_Semantic_Segmentation_with_Superpoint_Transformer_ICCV_2023_paper.pdf
  source_sha256: 054ac559a61e1141b9c84a96a09556e1707bff7a6268174474f05a8377955337
  clip_pdf_points:
  - 47
  - 70
  - 291
  - 347
  title: 多基准效果与模型规模
  setting: S3DIS 6-fold / Area 5，KITTI-360 验证集与 DALES；保留模型参数量及星号对应的大模型设置。
  metrics: mIoU ↑；参数量见 Size 列
  reading: 这是闭集监督分割；几何分区不生成类别名称。不要把默认 0.21M 与带星号的 KITTI 模型规模混为一谈。
---

# Superpoint Transformer

【原文事实】把几何与颜色信号分割成层级超点，在同层邻接图与跨层父子结构上进行注意力交互。

## 资料范围

正式发表于 ICCV 2023，本页图表读取 ICCV 2023 出版方正式版。按研究关注点整理相关模块，未独立复现实验。

## 任务与能力范围

几何定义预测单元和信息流；类别语义由监督训练学习，原文不声称开放词汇。

## 关注的几何操作

**几何分区、层级超点图与区域注意力**：以局部几何／颜色特征及空间近邻图建立分段常量近似，用图正则和 cut pursuit 求超点；逐层增加粒度形成父子结构。同层按近邻超点连边，以相对位置和区域特征进行层级注意力，分类最细超点。

依据：§3.1–3.3，Figure 2–3，Table 2。

## 代码开放情况

【官方文档说明】官方仓库公开分区与模型实现、训练评测配置、安装和预训练资源说明；部分分区依赖需编译，未运行。

## 实验阅读

Table 2：多基准效果与模型规模。S3DIS 6-fold / Area 5，KITTI-360 验证集与 DALES；保留模型参数量及星号对应的大模型设置。 这是闭集监督分割；几何分区不生成类别名称。不要把默认 0.21M 与带星号的 KITTI 模型规模混为一谈。
