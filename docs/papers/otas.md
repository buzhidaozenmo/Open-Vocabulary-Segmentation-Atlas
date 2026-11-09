---
paper_id: otas
title: 'OTAS: Open-vocabulary Token Alignment for Outdoor Segmentation'
short_name: OTAS
authors: []
year: 2026
preprint_date: '2025-07-08'
venue: ICRA
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
- geometry
- fusion
- efficient_inference
datasets:
- ORFD
- TartanAir
paper_url: https://arxiv.org/abs/2507.08851
publication_url: https://github.com/SimonSchwaiger/otas
code_status: public
code_url: https://github.com/SimonSchwaiger/otas
code_details: 官方仓库包含核心模型、推理、检查点下载脚本、演示与ROS 2接口；ICRA录用由作者仓库公告确认。
content_status: index
checked_on: '2026-11-09'
summary: 在单视图或多视图中对齐基础模型token，建立室外可查询语义表示。
sources:
- url: https://github.com/SimonSchwaiger/otas
  locator: 正式发表来源
- url: https://github.com/SimonSchwaiger/otas
  locator: 官方 README / 公开目录；未运行
---
# OTAS

## 当前整理状态

本条目仅完成索引与来源核查，尚未按完整模板精读；不据此生成方法继承关系或实验排名。

## 收录理由

在单视图或多视图中对齐基础模型token，建立室外可查询语义表示。

## 开源情况

【官方文档说明】官方仓库包含核心模型、推理、检查点下载脚本、演示与ROS 2接口；ICRA录用由作者仓库公告确认。 本轮没有安装或运行代码，没有独立验证权重下载。

## 后续核查

核对输入输出、训练监督、推理输入、版本、评测协议和原文图表。作者完整列表与预印本日期未填写时表示尚未核查，不能解释为论文没有作者或预印本。
