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
---
# OV-Octree-Graph

## 当前整理状态

本条目仅完成索引与来源核查，尚未按完整模板精读；不据此生成方法继承关系或实验排名。

## 收录理由

融合RGB-D序列的区域与实例特征，以八叉树图表达三维语义。

## 开源情况

【官方文档说明】公开实例构建、特征聚合及运行脚本；需外部二维模型与依赖。 本轮没有安装或运行代码，没有独立验证权重下载。

## 后续核查

核对输入输出、训练监督、推理输入、版本、评测协议和原文图表。作者完整列表与预印本日期未填写时表示尚未核查，不能解释为论文没有作者或预印本。
