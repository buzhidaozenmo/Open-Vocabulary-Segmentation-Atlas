---
paper_id: ptv3
title: 'Point Transformer V3: Simpler Faster Stronger'
short_name: PTv3
authors:
- Wu, Xiaoyang
- Jiang, Li
- Wang, Peng-Shuai
- Liu, Zhijian
- Liu, Xihui
- Qiao, Yu
- Ouyang, Wanli
- He, Tong
- Zhao, Hengshuang
year: 2024
preprint_date: unknown
venue: CVPR
publication_status: published
primary_direction: 3d
modalities:
- point_cloud
task_setting: supervised_backbone
task_types:
- semantic
techniques:
- geometry
- efficient_inference
datasets:
- ScanNet
- S3DIS
paper_url: https://openaccess.thecvf.com/content/CVPR2024/papers/Wu_Point_Transformer_V3_Simpler_Faster_Stronger_CVPR_2024_paper.pdf
publication_url: https://openaccess.thecvf.com/content/CVPR2024/html/Wu_Point_Transformer_V3_Simpler_Faster_Stronger_CVPR_2024_paper.html
code_status: public
code_url: https://github.com/Pointcept/PointTransformerV3
code_details: 官方仓库公开模型实现与安装、推理文档，训练与数据流程另见 Pointcept；当前独立仓库已更新，本文说明按 CVPR 2024 原文整理，未运行。
content_status: index
checked_on: '2026-11-11'
module_checked_on: '2026-11-11'
summary: 用空间填充曲线把点坐标变成序列，通过多排序局部注意力和稀疏卷积位置编码建立几何上下文。
sources:
- url: https://openaccess.thecvf.com/content/CVPR2024/html/Wu_Point_Transformer_V3_Simpler_Faster_Stronger_CVPR_2024_paper.html
  locator: 出版方正式发表记录
- url: https://openaccess.thecvf.com/content/CVPR2024/papers/Wu_Point_Transformer_V3_Simpler_Faster_Stronger_CVPR_2024_paper.pdf
  locator: 按模块列出的原文章节、原图及结果表
- url: https://github.com/Pointcept/PointTransformerV3
  locator: 官方 README 与根目录；未独立运行
figures:
- id: fig3
  label: Figure 3
  asset: assets/figures/ptv3-fig3.png
  page: 4
  version: CVPR 2024 出版方正式版
  source_url: https://openaccess.thecvf.com/content/CVPR2024/papers/Wu_Point_Transformer_V3_Simpler_Faster_Stronger_CVPR_2024_paper.pdf
  source_sha256: 530be4e23a5042604c0fcdc3288968a9cd7ce0792307567de808b3d39601883d
  clip_pdf_points:
  - 48
  - 70
  - 548
  - 296
methods:
- id: serialized-neighborhood
  track: pointcloud
  problems:
  - geometry
  title: 坐标序列化构造注意力邻域
  question: 无需逐层精确 KNN 时如何保留空间邻域？
  operation: 点坐标按网格离散并编码为 Z-order、Hilbert 及其转置排序；记录排序与逆映射，在连续序列 patch 中做注意力，并切换／打乱排序传播跨 patch 上下文。另以带残差的稀疏卷积 xCPE
    提供位置线索。
  input: 点坐标、点特征
  output: 编码几何上下文的点特征
  stage: 骨干前向；可用于监督或自监督任务
  supervision: PTv3 论文分割实验使用标注；骨干算子本身不定义监督
  origin: proposed
  origin_note: 本文框架中的具体设计；预训练骨干与基础算子不视为本文首创。
  evidence:
  - &id001
    locator: §4.1–4.3，Figure 3–6
    url: https://openaccess.thecvf.com/content/CVPR2024/papers/Wu_Point_Transformer_V3_Simpler_Faster_Stronger_CVPR_2024_paper.pdf
  figure: fig3
  figure_guide: 四组从左至右分别为空间曲线、点排序与局部 patch；patch 交互见 Figure 5，xCPE 见 Figure 6，本图不单独画出 xCPE。
  depicted: true
  route:
  - 三维坐标
  - 序列化局部注意力
  - 点特征
  - 骨干编码
  geometry:
    families:
    - coordinates
    signal: 三维坐标、网格及空间填充曲线
    mechanism: 用坐标决定序列 patch 和注意力可交换的信息范围，再用不同排序增加跨邻域交互。
    changes: 注意力邻接与点特征
    stage: 训练与推理前向
    semantic_role: 这是几何骨干；需另接语义头或语言对齐目标，原文主表为闭集监督评测。
    route:
    - 坐标与空间邻域
    - 序列化局部注意力
    - 注意力邻接
    - 骨干编码
    evidence:
    - *id001
results:
- id: table5
  label: Table 5
  asset: assets/results/ptv3-table5.png
  page: 7
  version: CVPR 2024 出版方正式版
  source_url: https://openaccess.thecvf.com/content/CVPR2024/papers/Wu_Point_Transformer_V3_Simpler_Faster_Stronger_CVPR_2024_paper.pdf
  source_sha256: 530be4e23a5042604c0fcdc3288968a9cd7ce0792307567de808b3d39601883d
  clip_pdf_points:
  - 49
  - 72
  - 289
  - 216
  title: 室内语义分割
  setting: ScanNet、ScanNet200、S3DIS；原表保留验证 / 测试、Area 5 / 6-fold，以及额外数据配置。
  metrics: mIoU ↑
  reading: 这是闭集监督分割的骨干评测；PTv3 本身不是语言对齐模型。不同数据配置按原表分组比较。
---

# PTv3

【原文事实】用空间填充曲线把点坐标变成序列，通过多排序局部注意力和稀疏卷积位置编码建立几何上下文。

## 资料范围

正式发表于 CVPR 2024，本页图表读取 CVPR 2024 出版方正式版。按研究关注点整理相关模块，未独立复现实验。

## 任务与能力范围

这是几何骨干；需另接语义头或语言对齐目标，原文主表为闭集监督评测。

## 关注的几何操作

**坐标序列化构造注意力邻域**：点坐标按网格离散并编码为 Z-order、Hilbert 及其转置排序；记录排序与逆映射，在连续序列 patch 中做注意力，并切换／打乱排序传播跨 patch 上下文。另以带残差的稀疏卷积 xCPE 提供位置线索。

依据：§4.1–4.3，Figure 3–6。

## 代码开放情况

【官方文档说明】官方仓库公开模型实现与安装、推理文档，训练与数据流程另见 Pointcept；当前独立仓库已更新，本文说明按 CVPR 2024 原文整理，未运行。

## 实验阅读

Table 5：室内语义分割。ScanNet、ScanNet200、S3DIS；原表保留验证 / 测试、Area 5 / 6-fold，以及额外数据配置。 这是闭集监督分割的骨干评测；PTv3 本身不是语言对齐模型。不同数据配置按原表分组比较。
