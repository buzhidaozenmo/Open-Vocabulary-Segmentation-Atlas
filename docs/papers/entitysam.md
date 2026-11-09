---
paper_id: entitysam
title: 'EntitySAM: Segment Everything in Video'
short_name: EntitySAM
authors: []
year: 2025
preprint_date: unknown
venue: CVPR
publication_status: published
primary_direction: video
modalities:
- video
task_setting: related_class_agnostic
task_types:
- video_entity
techniques:
- temporal
- region_aggregation
datasets:
- VIPSeg
- COCO
paper_url: https://openaccess.thecvf.com/content/CVPR2025/papers/Ye_EntitySAM_Segment_Everything_in_Video_CVPR_2025_paper.pdf
publication_url: https://openaccess.thecvf.com/content/CVPR2025/papers/Ye_EntitySAM_Segment_Everything_in_Video_CVPR_2025_paper.pdf
code_status: public
code_url: https://github.com/ymq2017/entitysam
code_details: 训练代码、评测代码和检查点已发布；核心任务不是文本类别驱动的OVSS。
content_status: index
checked_on: '2026-11-09'
summary: 以SAM2扩展自动发现和跟踪视频实体；作为类别无关相关任务参考。
sources:
- url: https://openaccess.thecvf.com/content/CVPR2025/papers/Ye_EntitySAM_Segment_Everything_in_Video_CVPR_2025_paper.pdf
  locator: 正式发表来源
- url: https://github.com/ymq2017/entitysam
  locator: 官方 README / 公开目录；未运行
---
# EntitySAM

## 当前整理状态

本条目仅完成索引与来源核查，尚未按完整模板精读；不据此生成方法继承关系或实验排名。

## 收录理由

以SAM2扩展自动发现和跟踪视频实体；作为类别无关相关任务参考。

## 开源情况

【官方文档说明】训练代码、评测代码和检查点已发布；核心任务不是文本类别驱动的OVSS。 本轮没有安装或运行代码，没有独立验证权重下载。

## 后续核查

核对输入输出、训练监督、推理输入、版本、评测协议和原文图表。作者完整列表与预印本日期未填写时表示尚未核查，不能解释为论文没有作者或预印本。

> 相关任务参考：类别无关实体分割不等于文本类别驱动的开放词汇语义分割。
