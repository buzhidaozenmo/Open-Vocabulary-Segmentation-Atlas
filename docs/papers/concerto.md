---
paper_id: concerto
title: 'Concerto: Joint 2D-3D Self-Supervised Learning Emerges Spatial Representations'
short_name: Concerto
authors:
- Yujia Zhang
- Xiaoyang Wu
- Yixing Lao
- Chengyao Wang
- Zhuotao Tian
- Naiyan Wang
- Hengshuang Zhao
year: 2025
preprint_date: unknown
venue: NeurIPS
publication_status: published
primary_direction: 3d
modalities:
- point_cloud
- image
task_setting: joint_self_supervised_representation
task_types:
- representation
- semantic
techniques:
- geometry
- feature_distillation
- semantic_alignment
datasets:
- ScanNet
- ScanNet++
- S3DIS
paper_url: https://arxiv.org/pdf/2510.23607v2
publication_url: https://proceedings.nips.cc/paper_files/paper/2025/hash/649a31f2cb31a73b92c68b15bbf44442-Abstract-Conference.html
code_status: public
code_url: https://github.com/Pointcept/Concerto
code_details: 官方独立仓库提供预训练模型入口、推理与可视化，预训练流程指向 Pointcept；公开目录不代表本文所有语言探测配置均已核实，未运行。
content_status: index
checked_on: '2026-11-11'
module_checked_on: '2026-11-11'
summary: 沿用 Sonata 的三维自蒸馏，以相机对应关联点云与图像 patch；另训练线性语言探测头接入 CLIP 空间。
sources:
- url: https://proceedings.nips.cc/paper_files/paper/2025/hash/649a31f2cb31a73b92c68b15bbf44442-Abstract-Conference.html
  locator: 出版方正式发表记录
- url: https://arxiv.org/pdf/2510.23607v2
  locator: 按模块列出的原文章节、原图及结果表
- url: https://github.com/Pointcept/Concerto
  locator: 官方 README 与根目录；未独立运行
figures:
- id: fig3
  label: Figure 3
  asset: assets/figures/concerto-fig3.png
  page: 4
  version: arXiv 2510.23607v2
  source_url: https://arxiv.org/pdf/2510.23607v2
  source_sha256: 1c62699cb23e3034084210986d76dd66bea6a84de45ab56a6aa351b21803b113
  clip_pdf_points:
  - 105
  - 60
  - 510
  - 224
- id: fig7
  label: Figure 7
  asset: assets/figures/concerto-fig7.png
  page: 18
  version: arXiv 2510.23607v2
  source_url: https://arxiv.org/pdf/2510.23607v2
  source_sha256: 1c62699cb23e3034084210986d76dd66bea6a84de45ab56a6aa351b21803b113
  clip_pdf_points:
  - 105
  - 65
  - 510
  - 369
methods:
- id: joint-embedding
  track: pointcloud
  problems:
  - geometry
  title: 以相机对应连接二维外观与三维结构
  question: 二维细节怎样参与三维表征学习？
  operation: 三维分支沿用 Sonata 自蒸馏；跨模态分支以相机参数建立像素—点对应，将落入同一图像 patch 的点特征取均值，经预测分支匹配图像编码器 patch 特征，并以余弦目标与三维目标联合优化。
  input: 点云、配对图像、相机参数
  output: 融合外观与空间结构的点表征
  stage: 联合自监督预训练
  supervision: 三维自监督与二维自监督教师，不用类别标签
  origin: proposed
  origin_note: 本文框架中的具体设计；预训练骨干与基础算子不视为本文首创。
  evidence:
  - &id001
    locator: §3.1–3.3，Figure 3
    url: https://arxiv.org/pdf/2510.23607v2
  figure: fig3
  figure_guide: 看 (a) 的三维师生分支与 (b) 的相机条件、预测器、图像 patch 对齐。
  depicted: true
  route:
  - 点云与图像自监督
  - 联合嵌入预测
  - 三维表征
  - 下游表征评测
  geometry:
    families:
    - pretrained
    - visibility
    signal: Sonata 式三维自蒸馏、相机参数与像素—点对应
    mechanism: 几何对应规定哪些点共同预测哪个图像 patch，而三维自蒸馏保持空间结构；不是推理时直接拼接两套特征。
    changes: 点表征与跨模态训练目标
    stage: 预训练
    semantic_role: DINOv2 patch 目标提供外观特征；接入文本还需单独的语言探测头。
    route:
    - 三维预训练表征
    - 跨模态对应学习
    - 多尺度点表征
    - 预训练／下游
    evidence:
    - *id001
  origin_refs:
  - url: https://arxiv.org/abs/2503.16429
    locator: §3.1 明确沿用 Sonata；PTv3 为骨干
  result_tables:
  - table1
- id: language-probing
  track: pointcloud
  problems:
  - geometry
  title: 把三维表征映射进 CLIP 语言空间
  question: 几何表征怎样获得文本查询接口？
  operation: 冻结的预训练 Concerto 表征后接简单线性层，以 LSeg 图像编码器的对齐特征监督该层；查询时与文本空间匹配。附录明确此对齐过程不使用 mask 与 crop 增强。
  input: Concerto 点特征、LSeg 目标；查询文本
  output: 文本空间中的三维特征与语言定位
  stage: 训练语言探测头；推理文本查询
  supervision: LSeg 预训练特征；不用目标三维语义标签
  origin: proposed
  origin_note: 本文框架中的具体设计；预训练骨干与基础算子不视为本文首创。
  evidence:
  - &id002
    locator: §4.1 Language probing、Table 5，附录 B.2
    url: https://arxiv.org/pdf/2510.23607v2
  figure: fig7
  figure_guide: 这是语言定位结果图，展示 Chair、Sink、Bed、Sofa 热图和 PCA；原文没有独立画出线性映射模块，计算操作见附录 B.2。
  depicted: false
  route:
  - 三维表征与LSeg
  - 线性语言探测
  - 语言对齐点特征
  - 文本查询
  geometry:
    families:
    - pretrained
    signal: 冻结 Concerto 的空间一致点表征
    mechanism: 保持三维骨干，训练线性映射使空间点表征进入 LSeg／CLIP 语言空间；几何表征本身不产生文本类别。
    changes: 点特征的输出空间
    stage: 语言探测训练；查询推理
    semantic_role: 类别语义来自 LSeg／CLIP；Table 5 与有监督线性语义探测 Table 1 是不同协议。
    route:
    - 三维预训练表征
    - 线性语言对齐
    - 语言对齐点表征
    - 开放词汇查询
    evidence:
    - *id002
  result_tables:
  - table5
results:
- id: table1
  label: Table 1
  asset: assets/results/concerto-table1.png
  page: 3
  version: arXiv 2510.23607v2
  source_url: https://arxiv.org/pdf/2510.23607v2
  source_sha256: 1c62699cb23e3034084210986d76dd66bea6a84de45ab56a6aa351b21803b113
  clip_pdf_points:
  - 105
  - 60
  - 510
  - 205
  title: 二维、三维与联合表征的线性探测
  setting: ScanNet / ScanNet200 验证集；冻结特征，训练线性语义探测头。
  metrics: mIoU、mAcc、allAcc ↑
  reading: 联合学习与特征拼接是不同方案；线性语义探测需要标注，不能把此表当成语言零样本结果。
- id: table5
  label: Table 5
  asset: assets/results/concerto-table5.png
  page: 8
  version: arXiv 2510.23607v2
  source_url: https://arxiv.org/pdf/2510.23607v2
  source_sha256: 1c62699cb23e3034084210986d76dd66bea6a84de45ab56a6aa351b21803b113
  clip_pdf_points:
  - 357
  - 343
  - 489
  - 422
  title: 语言空间探测
  setting: ScanNet 验证集；线性头以 LSeg 特征为目标训练，不用目标三维语义标签。
  metrics: mIoU、mAcc、allAcc ↑
  reading: 本表专门评估语言探测。Concerto 为 44.56 mIoU；与 Table 1 的有监督语义探测协议分开阅读。
---

# Concerto

【原文事实】沿用 Sonata 的三维自蒸馏，以相机对应关联点云与图像 patch；另训练线性语言探测头接入 CLIP 空间。

## 资料范围

正式发表于 NeurIPS 2025，本页图表读取 arXiv 2510.23607v2。按研究关注点整理相关模块，未独立复现实验。

## 任务与能力范围

DINOv2 patch 目标提供外观特征；接入文本还需单独的语言探测头。

## 关注的几何操作

**以相机对应连接二维外观与三维结构**：三维分支沿用 Sonata 自蒸馏；跨模态分支以相机参数建立像素—点对应，将落入同一图像 patch 的点特征取均值，经预测分支匹配图像编码器 patch 特征，并以余弦目标与三维目标联合优化。

依据：§3.1–3.3，Figure 3。

**把三维表征映射进 CLIP 语言空间**：冻结的预训练 Concerto 表征后接简单线性层，以 LSeg 图像编码器的对齐特征监督该层；查询时与文本空间匹配。附录明确此对齐过程不使用 mask 与 crop 增强。

依据：§4.1 Language probing、Table 5，附录 B.2。

## 代码开放情况

【官方文档说明】官方独立仓库提供预训练模型入口、推理与可视化，预训练流程指向 Pointcept；公开目录不代表本文所有语言探测配置均已核实，未运行。

## 实验阅读

Table 1：二维、三维与联合表征的线性探测。ScanNet / ScanNet200 验证集；冻结特征，训练线性语义探测头。 联合学习与特征拼接是不同方案；线性语义探测需要标注，不能把此表当成语言零样本结果。

Table 5：语言空间探测。ScanNet 验证集；线性头以 LSeg 特征为目标训练，不用目标三维语义标签。 本表专门评估语言探测。Concerto 为 44.56 mIoU；与 Table 1 的有监督语义探测协议分开阅读。
