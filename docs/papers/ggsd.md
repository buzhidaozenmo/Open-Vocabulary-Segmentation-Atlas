---
paper_id: ggsd
title: Open Vocabulary 3D Scene Understanding via Geometry Guided Self-Distillation
short_name: GGSD
authors:
- Pengfei Wang
- Yuxi Wang
- Shuai Li
- Zhaoxiang Zhang
- Zhen Lei
- Lei Zhang
year: 2024
preprint_date: unknown
venue: ECCV
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
- geometry
- feature_distillation
- region_aggregation
datasets: []
paper_url: https://arxiv.org/pdf/2407.13362v1
publication_url: https://doi.org/10.1007/978-3-031-72633-0_25
code_status: partial
code_url: https://github.com/Wang-pengfei/GGSD
code_details: 官方仓库有实现文件及特征下载入口，但 README 明确说明代码尚未完整整理、不能直接执行；标为部分公开，未运行。
content_status: index
checked_on: '2026-11-09'
module_checked_on: '2026-11-11'
summary: 先以超点几何一致性约束二维到三维知识蒸馏，减少区域内部语义噪声；得到几何更稳定的三维学生后，再用其预测进行三维自蒸馏，利用三维表征补足二维教师局限。
sources:
- url: https://doi.org/10.1007/978-3-031-72633-0_25
  locator: 正式发表来源：出版页面／作者项目的会议说明
- url: https://arxiv.org/pdf/2407.13362v1
  locator: 方法部分；Fig. 2（PDF 第 5 页）；实验 Table 1（PDF 第 10 页）
- url: https://github.com/Wang-pengfei/GGSD
  locator: 官方 README、目录与开放范围；未独立运行
figures:
- id: fig2
  label: Fig. 2
  asset: assets/figures/ggsd-fig2.png
  page: 5
  version: arXiv 2407.13362v1
  source_url: https://arxiv.org/pdf/2407.13362v1
  source_sha256: a78783cc176d8c95f40ce269abd3ade41130b9b8358eab8e4c9f1639c3e65764
  clip_pdf_points:
  - 134
  - 105
  - 481
  - 319.614
methods:
- id: semantic-operation
  track: pointcloud
  problems:
  - distillation
  - geometry
  - reliability
  title: 几何引导自蒸馏
  question: 如何利用三维几何纠正二维教师噪声？
  operation: 用 VCCS 生成几何超点，分别平均区域内二维融合特征与三维学生特征，以 1−cos 对齐两个超点均值并叠加逐点蒸馏损失；自蒸馏阶段以 EMA 三维教师生成伪标签，在超点内投票统一目标类别。
  input: 二维语言教师、点云超点及学生预测
  output: 几何一致的语言对齐点特征
  stage: 二维到三维蒸馏与三维自蒸馏训练
  supervision: 预训练二维语义特征、超点几何及学生伪监督
  origin: proposed
  origin_note: 本文设计的几何引导自蒸馏流程；所用预训练模型、通用投影及基础算子沿用已有方法，不计作本文新提出。
  evidence:
  - &id001
    url: https://arxiv.org/pdf/2407.13362v1
    locator: §3.3 Eq.(2)–(4)：超点均值及余弦损失；§3.4 Eq.(5)：EMA 伪标签与超点投票
  figure: fig2
  figure_guide: 看 Geometry Guided Distillation 与 Geometry Guided Self-Distillation 两个训练阶段。
  depicted: true
  route:
  - 多视角二维语义
  - 几何引导自蒸馏
  - 三维实例／点特征
  - 三维分割与查询
  result_tables:
  - table1
  geometry:
    families:
    - superpoints
    signal: 点云的几何超点划分
    mechanism: 用 VCCS 生成几何超点，分别平均区域内二维融合特征与三维学生特征，以 1−cos 对齐两个超点均值并叠加逐点蒸馏损失；自蒸馏阶段以 EMA 三维教师生成伪标签，在超点内投票统一目标类别。
    changes: 蒸馏目标与区域内一致性
    stage: 两阶段训练
    semantic_role: 二维模型提供语言空间，超点几何改善学生的空间一致性；官方代码仍为部分公开。
    route:
    - 超点与区域结构
    - 超点一致性蒸馏
    - 蒸馏权重与目标
    - 二维到三维训练
    evidence:
    - *id001
results:
- id: table1
  label: Table 1
  asset: assets/results/ggsd-table1.png
  page: 10
  version: arXiv 2407.13362v1
  source_url: https://arxiv.org/pdf/2407.13362v1
  source_sha256: a78783cc176d8c95f40ce269abd3ade41130b9b8358eab8e4c9f1639c3e65764
  clip_pdf_points:
  - 134
  - 110
  - 481
  - 399
  title: GGSD：主要实验结果
  setting: 标准三维分割基准；灰色为引用结果，† 为作者复测。
  metrics: mIoU／mAcc ↑
  reading: 开放扩展词表另见 Table 2，标准固定词表不能独自证明自由文本泛化。
---

# GGSD

本页按研究问题提取相关操作；模块图、输入输出、证据和主要结果表在上方展开查看。

## 研究问题

如何利用三维几何纠正二维教师噪声？

## 相关操作

先以超点几何一致性约束二维到三维知识蒸馏，减少区域内部语义噪声；得到几何更稳定的三维学生后，再用其预测进行三维自蒸馏，利用三维表征补足二维教师局限。

## 实验阅读

标准三维分割基准；灰色为引用结果，† 为作者复测。 开放扩展词表另见 Table 2，标准固定词表不能独自证明自由文本泛化。 主表是整体系统结果，单一模块的贡献需结合原文消融。

## 原文依据

- [本次阅读的原文版本](https://arxiv.org/pdf/2407.13362v1)：方法部分；Fig. 2（PDF 第 5 页）；实验 Table 1（PDF 第 10 页）。
- [正式发表来源](https://doi.org/10.1007/978-3-031-72633-0_25)。
- [官方实现](https://github.com/Wang-pengfei/GGSD)：官方仓库有实现文件及特征下载入口，但 README 明确说明代码尚未完整整理、不能直接执行；标为部分公开，未运行。
