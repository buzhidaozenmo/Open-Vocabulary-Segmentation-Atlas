---
paper_id: dvispp
title: 'DVIS++: Improved Decoupled Framework for Universal Video Segmentation'
short_name: OV-DVIS++
authors:
- Tao Zhang
- Xingye Tian
- Yikang Zhou
- Shunping Ji
- Xuebo Wang
- Xin Tao
- Yuan Zhang
- Pengfei Wan
- Zhongyuan Wang
- Yu Wu
year: 2025
preprint_date: unknown
venue: IEEE TPAMI
publication_status: published
primary_direction: video
modalities:
- video
task_setting: open_vocabulary
task_types:
- video_instance
techniques:
- semantic_alignment
- temporal
datasets:
- YouTube-VIS
- OVIS
- VSPW
- VIPSeg
paper_url: https://arxiv.org/pdf/2312.13305v1
publication_url: https://doi.org/10.1109/TPAMI.2025.3552694
code_status: public
code_url: https://github.com/KlingAIResearch/DVIS_Plus
code_details: 官方 DVIS_Plus 仓库包含 ov_dvis 相关实现、训练评测入口和 Model Zoo；本条聚焦同篇论文的 OV-DVIS++ 扩展，未运行。
content_status: index
checked_on: '2026-11-09'
module_checked_on: '2026-11-09'
summary: 在 DVIS++ 中接入冻结 CLIP，以跨帧对象表示完成开放词汇视频分类与分割。
sources:
- url: https://doi.org/10.1109/TPAMI.2025.3552694
  locator: 正式发表：出版方页面／DOI；期刊状态另由官方仓库文档确认
- url: https://arxiv.org/pdf/2312.13305v1
  locator: 本次所读原文版本的 §3–5／III–V、方法图及主要结果表
- url: https://github.com/KlingAIResearch/DVIS_Plus
  locator: 官方仓库实际目录与文档／项目页；未运行
figures:
- id: fig8
  label: Figure 8
  asset: assets/figures/dvispp-fig8.png
  page: 7
  version: arXiv 2312.13305v1
  source_url: https://arxiv.org/pdf/2312.13305v1
  clip_pdf_points:
  - 309
  - 45
  - 568
  - 167
  source_sha256: 55b2a53365ab9ea7adbdeec6055ae60fe792d792b405b665e3b0c86078a1dff0
- id: fig9
  label: Figure 9
  asset: assets/figures/dvispp-fig9.png
  page: 7
  version: arXiv 2312.13305v1
  source_url: https://arxiv.org/pdf/2312.13305v1
  clip_pdf_points:
  - 309
  - 218
  - 568
  - 333
  source_sha256: 55b2a53365ab9ea7adbdeec6055ae60fe792d792b405b665e3b0c86078a1dff0
methods:
- id: segmenter
  track: vocabulary
  problems:
  - alignment
  - regions
  title: 冻结 CLIP 上的开放词汇视频分割器
  question: 固定视频类别分类器怎样改成任意文本类别？
  operation: 以冻结 CLIP 作图像骨干，由分割头产生对象查询和掩码；对象表示及掩码池化视觉特征分别与文本嵌入匹配，再作几何集成，以文本相似度代替固定词表分类。
  input: 视频帧、类别文本、对象查询与掩码
  output: 开放词汇帧级对象类别及掩码
  stage: 训练与推理
  supervision: 预训练 CLIP；分割器使用图像分割数据训练，原表区分 COCO 与联合视频训练
  origin: modified
  origin_note: 原文明确受 FC-CLIP 启发构建开放词汇 segmenter；保留冻结视觉语言骨干。
  origin_refs:
  - url: https://github.com/bytedance/fc-clip
    locator: §3.6 明确采用 FC-CLIP 的冻结 CLIP 分割思路
  evidence:
  - url: https://arxiv.org/pdf/2312.13305v1
    locator: §3.6，Figure 8
  figure: fig8
  figure_guide: 独立 open-vocabulary segmenter 图看双路 Mask Pooling、文本匹配与 Geometric Ensemble。
  depicted: true
  route:
  - 二维区域特征
  - 区域文本匹配与集成
  - 视频实例类别
  - 文本相似度分类
- id: temporal
  track: vocabulary
  problems:
  - alignment
  - temporal
  title: 参考表示辅助分类并共享语言分类头
  question: 物体某帧缺少可辨外观时如何保留类别信息？
  operation: Referring Tracker 把前一时刻参考表示与当前跟踪查询结合用于类别预测；跟踪器及 Temporal Refiner 复用分割器冻结的掩码和类别头，只学习对象表示映射，减少重新训练分类头对开放词汇能力的破坏。
  input: 帧级对象查询、历史参考表示、共享分割头
  output: 类别稳定的对象轨迹与掩码
  stage: 训练与视频推理
  supervision: 已有开放词汇分割器；训练条件按原表区分纯图像伪视频和联合视频数据
  origin: proposed
  origin_note: 本文 OV-DVIS++ 对跟踪和细化模块的开放词汇适配；整套 DVIS++ 的闭集结果另行区分。
  origin_refs: []
  evidence:
  - url: https://arxiv.org/pdf/2312.13305v1
    locator: §3.6，Figure 9
  figure: fig9
  figure_guide: 独立 OV-DVIS++ 图看 RefT−1 与当前查询的合并，以及共享 Class & Mask Head。
  depicted: true
  route:
  - 视频实例语义
  - 参考表示时序关联
  - 视频实体记忆
  - 跨帧语义保持
results:
- id: table5
  label: Table 5
  asset: assets/results/dvispp-table5.png
  page: 12
  version: arXiv 2312.13305v1
  source_url: https://arxiv.org/pdf/2312.13305v1
  clip_pdf_points:
  - 45
  - 41
  - 568
  - 289
  source_sha256: 55b2a53365ab9ea7adbdeec6055ae60fe792d792b405b665e3b0c86078a1dff0
  title: 开放词汇视频实例分割
  setting: YouTube-VIS 2019／2021、OVIS 验证集；原表区分 Supervised 与 Zero-Shot、online／offline、COCO 与联合训练。
  metrics: AP／AP50／AP75 ↑；AR1／AR10 ↑
  reading: 比较相同骨干和训练数据的 online／offline 行；保留监督结果作参照，不当作零样本成绩。
---
# OV-DVIS++

## 资料范围与状态

核查版本：arXiv 2312.13305v1；正式发表来源另见出版方链接。已完成与研究关注点有关的方法、配图和主结果表定向整理，尚未完成全文样例笔记。图中的方法关系以原文为准，未独立运行实现。

## 关注的问题

【原文事实】在 DVIS++ 中接入冻结 CLIP，以跨帧对象表示完成开放词汇视频分类与分割。

## 实验阅读

YouTube-VIS 2019／2021、OVIS 验证集；原表区分 Supervised 与 Zero-Shot、online／offline、COCO 与联合训练。 比较相同骨干和训练数据的 online／offline 行；保留监督结果作参照，不当作零样本成绩。 数值保留在原始结果表中；它们是论文报告值，不是本库复现值。

## 开源情况

【官方文档说明／项目页核查】官方 DVIS_Plus 仓库包含 ov_dvis 相关实现、训练评测入口和 Model Zoo；本条聚焦同篇论文的 OV-DVIS++ 扩展，未运行。 本轮没有安装依赖、执行训练或验证复现结果。
