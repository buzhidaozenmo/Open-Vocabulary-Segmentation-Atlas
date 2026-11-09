---
paper_id: cosine
title: Unified Open-World Segmentation with Multi-Modal Prompts
short_name: COSINE
authors:
- Yang Liu
- Yufei Yin
- Chenchen Jing
- Muzhi Zhu
- Hao Chen
- Yuling Xi
- Bo Feng
- Hao Wang
- Shiyu Li
- Chunhua Shen
year: 2025
preprint_date: unknown
venue: ICCV
publication_status: published
primary_direction: 2d
modalities:
- image
task_setting: open_vocabulary
task_types:
- panoptic
techniques:
- semantic_alignment
- prompt
- fusion
datasets:
- COCO
- ADE20K
- PASCAL
- Cityscapes
paper_url: https://openaccess.thecvf.com/content/ICCV2025/papers/Liu_Unified_Open-World_Segmentation_with_Multi-Modal_Prompts_ICCV_2025_paper.pdf
publication_url: https://openaccess.thecvf.com/content/ICCV2025/html/Liu_Unified_Open-World_Segmentation_with_Multi-Modal_Prompts_ICCV_2025_paper.html
code_status: public
code_url: https://github.com/aim-uofa/COSINE
code_details: 官方仓库含训练、推理、复现说明及 MODEL_ZOO、检查点下载脚本；模型托管依赖外部访问条件，未验证下载。
content_status: index
checked_on: '2026-11-09'
module_checked_on: '2026-11-09'
summary: 以共享提示对齐器和多模态解码器统一文本及图像提示驱动的分割。
sources:
- url: https://openaccess.thecvf.com/content/ICCV2025/html/Liu_Unified_Open-World_Segmentation_with_Multi-Modal_Prompts_ICCV_2025_paper.html
  locator: 正式发表：出版方页面／DOI；期刊状态另由官方仓库文档确认
- url: https://openaccess.thecvf.com/content/ICCV2025/papers/Liu_Unified_Open-World_Segmentation_with_Multi-Modal_Prompts_ICCV_2025_paper.pdf
  locator: 本次所读原文版本的 §3–5／III–V、方法图及主要结果表
- url: https://github.com/aim-uofa/COSINE
  locator: 官方仓库实际目录与文档／项目页；未运行
figures:
- id: fig2
  label: Figure 2
  asset: assets/figures/cosine-fig2.png
  page: 4
  version: ICCV 2025 出版方正式版
  source_url: https://openaccess.thecvf.com/content/ICCV2025/papers/Liu_Unified_Open-World_Segmentation_with_Multi-Modal_Prompts_ICCV_2025_paper.pdf
  clip_pdf_points:
  - 55
  - 50
  - 558
  - 356
  source_sha256: 6026bc2c0c13a40a0d2cc40653fe4754fa584d8d512876bd851c752522453c0a
methods:
- id: aligner
  track: vocabulary
  problems:
  - alignment
  - prompt
  title: 共享图像—提示对齐器
  question: 文本提示与视觉示例怎样进入共同分割空间？
  operation: 从模型池获得图像、视觉提示与文本特征；通过 Feature Blender、V／T Adapter 统一维度和表示，再用共享自注意力、跨注意力和 FFN 对齐图像与各模态提示。
  input: 图像、类别文本或视觉示例提示
  output: 共同空间内的图像和提示特征
  stage: 训练与推理
  supervision: 预训练模型池和语义／实例／全景等分割数据；不是免训练模型
  origin: proposed
  origin_note: 本文 SegDecoder 中的适配器与 Image-Prompt Aligner；已有编码器提供初始特征。
  origin_refs: []
  evidence:
  - url: https://openaccess.thecvf.com/content/ICCV2025/papers/Liu_Unified_Open-World_Segmentation_with_Multi-Modal_Prompts_ICCV_2025_paper.pdf
    locator: §3.1–3.2，Eq.1
  figure: fig2
  figure_guide: 总图 (b) 看 Feature Blender 和 V／T Adapter；(c) 独立子图展示共享 Image-Prompt Aligner。
  depicted: true
  route:
  - 文本与视觉提示
  - 图像提示共同对齐
  - 提示条件特征
  - 提示条件分割
- id: classification
  track: vocabulary
  problems:
  - alignment
  - prompt
  title: 联合提示解码与动态类别匹配
  question: 怎样让类别文本参与对象查询和掩码输出？
  operation: 多模态解码器联合细化对象查询、视觉／文本提示和图像特征；对象查询与细化后的提示点积给类别分数，查询经 MLP 与高分辨率 mask feature 相乘得到掩码。训练时图文提示协同，推理支持单提示或平均融合提示。
  input: 对齐图像／提示特征、对象查询、像素掩码特征
  output: 提示匹配的实例／语义掩码
  stage: 训练与推理
  supervision: 带类别和掩码的分割数据；图文提示按原文共同训练
  origin: proposed
  origin_note: 本文多模态统一解码和协同提示推理；不把额外视觉提示结果当成纯文本协议。
  origin_refs: []
  evidence:
  - url: https://openaccess.thecvf.com/content/ICCV2025/papers/Liu_Unified_Open-World_Segmentation_with_Multi-Modal_Prompts_ICCV_2025_paper.pdf
    locator: §3.2–3.3，Eq.2–4
  figure: fig2
  figure_guide: (d) Multi-Modality Decoder 看查询与提示交互；(b) 底部看 Class／Mask 输出。
  depicted: true
  route:
  - 文本与视觉提示
  - 联合提示查询解码
  - 实例掩码
  - 提示条件分割
results:
- id: table1
  label: Table 1
  asset: assets/results/cosine-table1.png
  page: 6
  version: ICCV 2025 出版方正式版
  source_url: https://openaccess.thecvf.com/content/ICCV2025/papers/Liu_Unified_Open-World_Segmentation_with_Multi-Modal_Prompts_ICCV_2025_paper.pdf
  clip_pdf_points:
  - 55
  - 69
  - 558
  - 429
  source_sha256: 6026bc2c0c13a40a0d2cc40653fe4754fa584d8d512876bd851c752522453c0a
  title: 多任务分割主结果
  setting: 原表包含 few-shot、开放词汇全景和语义分割；† 表示单尺度 COSINE，保留不同模型训练条件。
  metrics: 按任务列分别看 AP／PQ／mIoU ↑
  reading: 当前主线重点看右侧 open-voc. pano. 与 open-voc. sem. 列，不把 few-shot 成绩当成纯文本分割结果。
---
# COSINE

## 资料范围与状态

核查版本：ICCV 2025 出版方正式版；正式发表来源另见出版方链接。已完成与研究关注点有关的方法、配图和主结果表定向整理，尚未完成全文样例笔记。图中的方法关系以原文为准，未独立运行实现。

## 关注的问题

【原文事实】以共享提示对齐器和多模态解码器统一文本及图像提示驱动的分割。

## 实验阅读

原表包含 few-shot、开放词汇全景和语义分割；† 表示单尺度 COSINE，保留不同模型训练条件。 当前主线重点看右侧 open-voc. pano. 与 open-voc. sem. 列，不把 few-shot 成绩当成纯文本分割结果。 数值保留在原始结果表中；它们是论文报告值，不是本库复现值。

## 开源情况

【官方文档说明／项目页核查】官方仓库含训练、推理、复现说明及 MODEL_ZOO、检查点下载脚本；模型托管依赖外部访问条件，未验证下载。 本轮没有安装依赖、执行训练或验证复现结果。
