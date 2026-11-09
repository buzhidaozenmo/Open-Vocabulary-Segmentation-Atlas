---
paper_id: mpec
title: Masked Point-Entity Contrast for Open-Vocabulary 3D Scene Understanding
short_name: MPEC
authors:
- Yan Wang
- Baoxiong Jia
- Ziyu Zhu
- Siyuan Huang
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
- geometry
datasets:
- ScanNet
- Matterport3D
paper_url: https://openaccess.thecvf.com/content/CVPR2025/papers/Wang_Masked_Point-Entity_Contrast_for_Open-Vocabulary_3D_Scene_Understanding_CVPR_2025_paper.pdf
publication_url: https://openaccess.thecvf.com/content/CVPR2025/html/Wang_Masked_Point-Entity_Contrast_for_Open-Vocabulary_3D_Scene_Understanding_CVPR_2025_paper.html
code_status: unconfirmed
code_url: ''
code_details: 未找到可核实的官方实现入口；项目页的 Code 尚未链接到实际代码。论文可读，不据此断言作者明确不开源。
content_status: index
checked_on: '2026-11-09'
module_checked_on: '2026-11-09'
summary: 以三维实体为中介，将增强点云视图的一致性与实体语言对齐分开学习。
sources:
- url: https://openaccess.thecvf.com/content/CVPR2025/html/Wang_Masked_Point-Entity_Contrast_for_Open-Vocabulary_3D_Scene_Understanding_CVPR_2025_paper.html
  locator: 正式发表：出版方页面／DOI；期刊状态另由官方仓库文档确认
- url: https://openaccess.thecvf.com/content/CVPR2025/papers/Wang_Masked_Point-Entity_Contrast_for_Open-Vocabulary_3D_Scene_Understanding_CVPR_2025_paper.pdf
  locator: 本次所读原文版本的 §3–5／III–V、方法图及主要结果表
- url: https://mpec-3d.github.io/
  locator: 官方仓库实际目录与文档／项目页；未运行
figures:
- id: fig2
  label: Figure 2
  asset: assets/figures/mpec-fig2.png
  page: 4
  version: CVPR 2025 出版方正式版
  source_url: https://openaccess.thecvf.com/content/CVPR2025/papers/Wang_Masked_Point-Entity_Contrast_for_Open-Vocabulary_3D_Scene_Understanding_CVPR_2025_paper.pdf
  clip_pdf_points:
  - 55
  - 50
  - 558
  - 284
  source_sha256: 74971063690b0300e7872753e578b8b643ee30be758bd13c18cb43c0aa6cb0c7
methods:
- id: pointentity
  track: pointcloud
  problems:
  - regions
  - geometry
  title: 遮挡增强视图上的点—实体对比
  question: 如何使部分可见点保持完整实体语义？
  operation: 对同一场景生成两种三维增强视图，按原始空间网格随机遮挡颜色并填入可学习 token；计算一视图中点与另一视图实体成员点的平均余弦相似度，以同一实体作正例，其他实体与背景点作负例，并双向对比。
  input: 点云、实体提议、两种三维增强及遮挡
  output: 具实体区分能力的逐点特征
  stage: 训练
  supervision: 现成三维实例提议及已有配对数据；这里的 view 是三维增强视图，不是 RGB 相机视图
  origin: proposed
  origin_note: 本文 Point-to-Entity Alignment；不将三维增强一致性误记为相机多视角投影。
  origin_refs: []
  evidence:
  - url: https://openaccess.thecvf.com/content/CVPR2025/papers/Wang_Masked_Point-Entity_Contrast_for_Open-Vocabulary_3D_Scene_Understanding_CVPR_2025_paper.pdf
    locator: §3.1，Eq.1–6
  figure: fig2
  figure_guide: 看左侧 View u／v 的网格遮挡与下方 point-to-entity contrast；图中没有相机投影。
  depicted: true
  route:
  - 三维实体先验
  - 跨增强视图实体对比
  - 逐点特征
  - 几何一致性约束
- id: entitylanguage
  track: pointcloud
  problems:
  - alignment
  - regions
  title: 多描述的实体—语言双向对齐
  question: 同一实体有多个描述时，怎样避免把正确描述当负例？
  operation: 先平均两视图匹配点特征，经 VL-Adapter 对齐文本维度；文本到实体用对比交叉熵，实体到文本用二元交叉熵容纳同一实体的多条正确描述；推理以逐点语言特征与类别文本相似度分类。
  input: 合并点特征、实体成员关系、实体描述
  output: 可文本查询的点特征
  stage: 训练；文本查询用于推理
  supervision: 现成实体提议、SceneVerse 流程生成的描述／指代表达、冻结 CLIP 文本编码器
  origin: proposed
  origin_note: 本文 Entity-to-Language Alignment；实体提议及描述生成依赖已有数据流程。
  origin_refs: []
  evidence:
  - url: https://openaccess.thecvf.com/content/CVPR2025/papers/Wang_Masked_Point-Entity_Contrast_for_Open-Vocabulary_3D_Scene_Understanding_CVPR_2025_paper.pdf
    locator: §3.2–3.3，Eq.7–14
  figure: fig2
  figure_guide: 看右侧 VL-Adapter、CLIP Text Encoder 与 entity-to-language contrast；多正例 BCE 的方向见 Eq.12。
  depicted: true
  route:
  - 区域文本描述
  - 实体语言对比
  - 逐点特征
  - 文本相似度分类
results:
- id: table1
  label: Table 1
  asset: assets/results/mpec-table1.png
  page: 6
  version: CVPR 2025 出版方正式版
  source_url: https://openaccess.thecvf.com/content/CVPR2025/papers/Wang_Masked_Point-Entity_Contrast_for_Open-Vocabulary_3D_Scene_Understanding_CVPR_2025_paper.pdf
  clip_pdf_points:
  - 55
  - 68
  - 299
  - 299
  source_sha256: 74971063690b0300e7872753e578b8b643ee30be758bd13c18cb43c0aa6cb0c7
  title: ScanNet 三维开放词汇语义分割
  setting: ScanNet；区分二维、三维方法及 SPUNet16／32 骨干；结果为前景指标，保留复测来源标记。
  metrics: f-mIoU ↑；f-mAcc ↑
  reading: 按同一骨干比较 MPEC 与基线；本表的前景指标不与其他论文包含背景的 mIoU 混排。
---
# MPEC

## 资料范围与状态

核查版本：CVPR 2025 出版方正式版；正式发表来源另见出版方链接。已完成与研究关注点有关的方法、配图和主结果表定向整理，尚未完成全文样例笔记。本文所用多视图主要是三维数据增强视图，与多相机 RGB-D 投影不同。

## 关注的问题

【原文事实】以三维实体为中介，将增强点云视图的一致性与实体语言对齐分开学习。

## 实验阅读

ScanNet；区分二维、三维方法及 SPUNet16／32 骨干；结果为前景指标，保留复测来源标记。 按同一骨干比较 MPEC 与基线；本表的前景指标不与其他论文包含背景的 mIoU 混排。 数值保留在原始结果表中；它们是论文报告值，不是本库复现值。

## 开源情况

【官方文档说明／项目页核查】未找到可核实的官方实现入口；项目页的 Code 尚未链接到实际代码。论文可读，不据此断言作者明确不开源。 本轮没有安装依赖、执行训练或验证复现结果。
