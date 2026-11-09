---
paper_id: hovsg
title: Hierarchical Open-Vocabulary 3D Scene Graphs for Language-Grounded Robot Navigation
short_name: HOV-SG
authors:
- Abdelrhman Werby
- Chenguang Huang
- Martin BÃ¼chner
- Abhinav Valada
- Wolfram Burgard
year: 2024
preprint_date: unknown
venue: RSS
publication_status: published
primary_direction: multiview
modalities:
- point_cloud
- image
task_setting: open_vocabulary
task_types:
- semantic
techniques:
- semantic_alignment
datasets: []
paper_url: https://www.roboticsproceedings.org/rss20/p077.pdf
publication_url: https://www.roboticsproceedings.org/rss20/p077.html
code_status: public
code_url: https://github.com/hovsg/HOV-SG
code_details: 已核对官方实现目录：application、config、environment.yaml、hovsg、media、setup.py。未独立运行或验证外部权重下载。
content_status: index
checked_on: '2026-11-09'
module_checked_on: '2026-11-09'
summary: 按 SAM 掩码提取 CLIP 语义并融合到三维点，合并三维区域后对每个对象的特征用 DBSCAN 去噪并选多数簇；再结合几何构建楼层、房间、对象层级以支持语言查询。
sources:
- url: https://www.roboticsproceedings.org/rss20/p077.html
  locator: 正式发表来源：出版页面／作者项目的会议说明
- url: https://www.roboticsproceedings.org/rss20/p077.pdf
  locator: 方法部分；Fig. 2（PDF 第 3 页）；实验 TABLE I（PDF 第 6 页）
- url: https://github.com/hovsg/HOV-SG
  locator: 官方 README、目录与开放范围；未独立运行
figures:
- id: fig2
  label: Fig. 2
  asset: assets/figures/hovsg-fig2.png
  page: 3
  version: RSS 2024 出版方正式版
  source_url: https://www.roboticsproceedings.org/rss20/p077.pdf
  source_sha256: 14d5798355988d500d0ccc5c7b19fb65918d66289f9bf121aaa8607ff9bebd06
  clip_pdf_points:
  - 45
  - 45
  - 567
  - 177.013
methods:
- id: semantic-operation
  track: pointcloud
  problems:
  - multiview
  - reliability
  - regions
  title: 对象特征净化与层级图
  question: 多视图语义怎样形成可靠的对象级特征？
  operation: 按 SAM 掩码提取 CLIP 语义并融合到三维点，合并三维区域后对每个对象的特征用 DBSCAN 去噪并选多数簇；再结合几何构建楼层、房间、对象层级以支持语言查询。
  input: RGB-D、SAM 掩码、多视角 CLIP 与几何
  output: 净化对象语义及层级三维场景图
  stage: 建图、聚合和查询推理
  supervision: 预训练基础模型与深度位姿，无目标场景语义训练
  origin: proposed
  origin_note: 本文设计的对象特征净化与层级图流程；所用预训练模型、通用投影及基础算子沿用已有方法，不计作本文新提出。
  evidence:
  - url: https://www.roboticsproceedings.org/rss20/p077.pdf
    locator: 方法部分；Fig. 2（PDF 第 3 页）；实验 TABLE I（PDF 第 6 页）
  figure: fig2
  figure_guide: 重点看点级特征聚合、merged 3D masks 和多数语义特征；楼层房间是后续结构。
  depicted: true
  route:
  - 多视角二维语义
  - 对象特征净化与层级图
  - 三维实例／点特征
  - 三维分割与查询
  result_tables:
  - tablei
results:
- id: tablei
  label: TABLE I
  asset: assets/results/hovsg-tablei.png
  page: 6
  version: RSS 2024 出版方正式版
  source_url: https://www.roboticsproceedings.org/rss20/p077.pdf
  source_sha256: 14d5798355988d500d0ccc5c7b19fb65918d66289f9bf121aaa8607ff9bebd06
  clip_pdf_points:
  - 45
  - 55
  - 305
  - 212
  title: HOV-SG：主要实验结果
  setting: 开放词汇三维语义分割；按原表数据集与对象语义设置。
  metrics: mIoU／mAcc 等 ↑
  reading: 语义分割与楼层／房间分割是不同任务，主表只比较同类指标。
---

# HOV-SG

本页按研究问题提取相关操作；模块图、输入输出、证据和主要结果表在上方展开查看。

## 研究问题

多视图语义怎样形成可靠的对象级特征？

## 相关操作

按 SAM 掩码提取 CLIP 语义并融合到三维点，合并三维区域后对每个对象的特征用 DBSCAN 去噪并选多数簇；再结合几何构建楼层、房间、对象层级以支持语言查询。

## 实验阅读

开放词汇三维语义分割；按原表数据集与对象语义设置。 语义分割与楼层／房间分割是不同任务，主表只比较同类指标。 主表是整体系统结果，单一模块的贡献需结合原文消融。

## 原文依据

- [本次阅读的原文版本](https://www.roboticsproceedings.org/rss20/p077.pdf)：方法部分；Fig. 2（PDF 第 3 页）；实验 TABLE I（PDF 第 6 页）。
- [正式发表来源](https://www.roboticsproceedings.org/rss20/p077.html)。
- [官方实现](https://github.com/hovsg/HOV-SG)：已核对官方实现目录：application、config、environment.yaml、hovsg、media、setup.py。未独立运行或验证外部权重下载。
