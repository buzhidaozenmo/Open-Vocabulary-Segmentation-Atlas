---
paper_id: talk2dino
title: 'Talking to DINO: Bridging Self-Supervised Vision Backbones with Language for Open-Vocabulary Segmentation'
short_name: Talk2DINO
authors:
- Barsellotti, Luca
- Bianchi, Lorenzo
- Messina, Nicola
- Carrara, Fabio
- Cornia, Marcella
- Baraldi, Lorenzo
- Falchi, Fabrizio
- Cucchiara, Rita
year: 2025
preprint_date: unknown
venue: ICCV
publication_status: published
primary_direction: 2d
modalities:
- image
task_setting: open_vocabulary
task_types:
- semantic
techniques:
- semantic_alignment
datasets:
- PASCAL
- COCO
- Cityscapes
- ADE20K
paper_url: https://openaccess.thecvf.com/content/ICCV2025/papers/Barsellotti_Talking_to_DINO_Bridging_Self-Supervised_Vision_Backbones_with_Language_for_ICCV_2025_paper.pdf
publication_url: https://openaccess.thecvf.com/content/ICCV2025/html/Barsellotti_Talking_to_DINO_Bridging_Self-Supervised_Vision_Backbones_with_Language_for_ICCV_2025_paper.html
code_status: public
code_url: https://github.com/lorebianchi98/Talk2DINO
code_details: 已核对官方仓库实际实现目录：configs、demo.py、dino_extraction_v2.py、hf_demo.ipynb、pikachu_seg.png、requirements.txt。运行及外部权重可用性未独立复现。
content_status: index
checked_on: '2026-11-09'
module_checked_on: '2026-11-09'
summary: 冻结 CLIP 文本编码器和 DINOv2，在训练图文配对上学习文本到 DINO patch 空间的映射；用 DINO 注意图选择局部视觉特征做对齐，推理时将映射后的类别文本与稠密 patch 比较并清理背景。
sources:
- url: https://openaccess.thecvf.com/content/ICCV2025/html/Barsellotti_Talking_to_DINO_Bridging_Self-Supervised_Vision_Backbones_with_Language_for_ICCV_2025_paper.html
  locator: 正式发表页面及作者信息
- url: https://openaccess.thecvf.com/content/ICCV2025/papers/Barsellotti_Talking_to_DINO_Bridging_Self-Supervised_Vision_Backbones_with_Language_for_ICCV_2025_paper.pdf
  locator: 方法部分；Figure 2（PDF 第 3 页）；实验 Table 1（PDF 第 6 页）
- url: https://github.com/lorebianchi98/Talk2DINO
  locator: 官方 README 与实际代码目录；不表示已运行
figures:
- id: figure2
  label: Figure 2
  asset: assets/figures/talk2dino-figure2.png
  page: 3
  version: ICCV 2025 出版方正式版
  source_url: https://openaccess.thecvf.com/content/ICCV2025/papers/Barsellotti_Talking_to_DINO_Bridging_Self-Supervised_Vision_Backbones_with_Language_for_ICCV_2025_paper.pdf
  source_sha256: b30eee692e8d5d65207496d8caafddc5d610dc39ba4b414aefbe03ad1dd271ee
  clip_pdf_points:
  - 55
  - 50
  - 558
  - 273.23028564453125
methods:
- id: semantic-operation
  track: vocabulary
  problems:
  - alignment
  title: 局部图文映射
  question: DINO 的局部结构怎样与文本对应？
  operation: 冻结 CLIP 文本编码器和 DINOv2，在训练图文配对上学习文本到 DINO patch 空间的映射；用 DINO 注意图选择局部视觉特征做对齐，推理时将映射后的类别文本与稠密 patch 比较并清理背景。
  input: 图文训练配对；推理图像和类别文本
  output: 语言可查询的 DINO 稠密特征
  stage: 映射训练及分割推理
  supervision: 图像—文本配对，不依赖像素类别标注
  origin: proposed
  origin_note: 本文设计的局部图文映射流程；其预训练基础模型与通用组件沿用已有方法，不计作本文新提出。
  origin_refs:
  - url: https://openaccess.thecvf.com/content/ICCV2025/papers/Barsellotti_Talking_to_DINO_Bridging_Self-Supervised_Vision_Backbones_with_Language_for_ICCV_2025_paper.pdf
    locator: 方法部分列明的基础模型及其参考文献
  evidence:
  - url: https://openaccess.thecvf.com/content/ICCV2025/papers/Barsellotti_Talking_to_DINO_Bridging_Self-Supervised_Vision_Backbones_with_Language_for_ICCV_2025_paper.pdf
    locator: 方法部分；Figure 2（PDF 第 3 页）；实验 Table 1（PDF 第 6 页）
  figure: figure2
  figure_guide: 左上 DINOv2 的注意图选择局部视觉特征，下方 CLIP Text 经可学习映射 ψ 到 DINO 空间，训练对齐发生在冻结骨干之间。
  depicted: true
  route:
  - CLIP 文本与 DINOv2
  - 局部图文映射
  - 像素类别相似度
  - 开放词汇分割
  result_tables:
  - table1
results:
- id: table1
  label: Table 1
  asset: assets/results/talk2dino-table1.png
  page: 6
  version: ICCV 2025 出版方正式版
  source_url: https://openaccess.thecvf.com/content/ICCV2025/papers/Barsellotti_Talking_to_DINO_Bridging_Self-Supervised_Vision_Backbones_with_Language_for_ICCV_2025_paper.pdf
  source_sha256: b30eee692e8d5d65207496d8caafddc5d610dc39ba4b414aefbe03ad1dd271ee
  clip_pdf_points:
  - 55
  - 55
  - 558
  - 426
  title: Talk2DINO：主要实验结果
  setting: 八组含／不含背景基准；保留视觉骨干是否冻结及掩码细化条件。
  metrics: mIoU ↑
  reading: 冻结骨干不等于整套方法免训练；映射网络需要图文训练。
---

# Talk2DINO

本页按研究问题提取相关操作；模块原图、具体输入输出、来源与主要实验结果在上方展开查看。

## 研究问题

DINO 的局部结构怎样与文本对应？

## 相关操作

冻结 CLIP 文本编码器和 DINOv2，在训练图文配对上学习文本到 DINO patch 空间的映射；用 DINO 注意图选择局部视觉特征做对齐，推理时将映射后的类别文本与稠密 patch 比较并清理背景。

## 实验阅读

八组含／不含背景基准；保留视觉骨干是否冻结及掩码细化条件。 冻结骨干不等于整套方法免训练；映射网络需要图文训练。 主要结果是整套方法的效果，不能单凭该表归因到一个模块。

## 原文依据

- [出版方原文](https://openaccess.thecvf.com/content/ICCV2025/papers/Barsellotti_Talking_to_DINO_Bridging_Self-Supervised_Vision_Backbones_with_Language_for_ICCV_2025_paper.pdf)：方法部分；Figure 2（PDF 第 3 页）；实验 Table 1（PDF 第 6 页）。
- [官方实现](https://github.com/lorebianchi98/Talk2DINO)：已检查公开目录，未独立运行训练或评测。
