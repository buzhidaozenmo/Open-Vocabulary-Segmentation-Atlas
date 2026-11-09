---
paper_id: sam3
title: 'SAM 3: Segment Anything with Concepts'
short_name: SAM3
authors: []
year: 2026
preprint_date: '2025-11-20'
venue: ICLR
publication_status: published
primary_direction: 2d
modalities:
- image
- video
task_setting: concept_prompt
task_types:
- concept_prompt
- instance
techniques:
- prompt
- temporal
datasets:
- SA-Co
paper_url: https://arxiv.org/abs/2511.16719
publication_url: https://proceedings.iclr.cc/paper_files/paper/2026/hash/e0982cbc81401df3430ee1ff780dc7a2-Abstract-Conference.html
code_status: public
code_url: https://github.com/facebookresearch/sam3
code_details: 提供推理、微调、示例与检查点入口；权重需按官方访问与许可流程获取。
content_status: index
checked_on: '2026-11-09'
summary: 通过文本概念或图像示例分割匹配实例，并支持视频中的身份跟踪。
sources:
- url: https://proceedings.iclr.cc/paper_files/paper/2026/hash/e0982cbc81401df3430ee1ff780dc7a2-Abstract-Conference.html
  locator: 正式发表来源
- url: https://github.com/facebookresearch/sam3
  locator: 官方 README / 公开目录；未运行
---
# SAM3

## 当前整理状态

本条目仅完成索引与来源核查，尚未按完整模板精读；不据此生成方法继承关系或实验排名。

## 收录理由

通过文本概念或图像示例分割匹配实例，并支持视频中的身份跟踪。

## 开源情况

【官方文档说明】提供推理、微调、示例与检查点入口；权重需按官方访问与许可流程获取。 本轮没有安装或运行代码，没有独立验证权重下载。

## 后续核查

核对输入输出、训练监督、推理输入、版本、评测协议和原文图表。作者完整列表与预印本日期未填写时表示尚未核查，不能解释为论文没有作者或预印本。

> 本条目主要归入2D，但同时具有视频模态标签；全站仅计一次。概念提示分割与标准OVSS评测分别记录。
