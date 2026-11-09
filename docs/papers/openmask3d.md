---
paper_id: openmask3d
title: 'OpenMask3D: Open-Vocabulary 3D Instance Segmentation'
short_name: OpenMask3D
authors: []
year: 2023
preprint_date: unknown
venue: NeurIPS
publication_status: published
primary_direction: 3d
modalities:
- point_cloud
- image
task_setting: open_vocabulary
task_types:
- instance
techniques:
- region_aggregation
- fusion
datasets:
- ScanNet
- Replica
paper_url: https://arxiv.org/abs/2306.13631
publication_url: https://proceedings.neurips.cc/paper_files/paper/2023/hash/d77b5482e38339a8068791d939126be2-Abstract-Conference.html
code_status: public
code_url: https://github.com/OpenMask3D/openmask3d
code_details: 公开特征提取、聚合与评测流程；依赖3D掩码模型、SAM等外部权重。
content_status: index
checked_on: '2026-11-09'
summary: 用类别无关三维实例掩码和多视角区域特征进行开放词汇实例分割。
sources:
- url: https://proceedings.neurips.cc/paper_files/paper/2023/hash/d77b5482e38339a8068791d939126be2-Abstract-Conference.html
  locator: 正式发表来源
- url: https://github.com/OpenMask3D/openmask3d
  locator: 官方 README / 公开目录；未运行
---
# OpenMask3D

## 当前整理状态

本条目仅完成索引与来源核查，尚未按完整模板精读；不据此生成方法继承关系或实验排名。

## 收录理由

用类别无关三维实例掩码和多视角区域特征进行开放词汇实例分割。

## 开源情况

【官方文档说明】公开特征提取、聚合与评测流程；依赖3D掩码模型、SAM等外部权重。 本轮没有安装或运行代码，没有独立验证权重下载。

## 后续核查

核对输入输出、训练监督、推理输入、版本、评测协议和原文图表。作者完整列表与预印本日期未填写时表示尚未核查，不能解释为论文没有作者或预印本。
