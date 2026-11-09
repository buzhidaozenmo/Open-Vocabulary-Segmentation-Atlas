---
paper_id: fsegllava
title: 'The Power of Prior: Training-Free Open-Vocabulary Semantic Segmentation with LLaVA'
short_name: FSeg-LLaVA
authors:
- Zhang, Bingfeng
- Yu, Siyue
- Li, Hui
- Lin, Jiahua
- Wang, Wenwu
- Xiao, Jimin
year: 2026
preprint_date: unknown
venue: CVPR
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
- ADE20K
paper_url: https://openaccess.thecvf.com/content/CVPR2026/papers/Zhang_The_Power_of_Prior_Training-Free_Open-Vocabulary_Semantic_Segmentation_with_LLaVA_CVPR_2026_paper.pdf
publication_url: https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_The_Power_of_Prior_Training-Free_Open-Vocabulary_Semantic_Segmentation_with_LLaVA_CVPR_2026_paper.html
code_status: public
code_url: https://github.com/zbf1991/FSeg-LLaVA
code_details: 已核对官方仓库实际实现目录：CONTRIBUTING.md、MANIFEST.in、infer.py、llava、pyproject.toml、requirements.txt。运行及外部权重可用性未独立复现。
content_status: index
checked_on: '2026-11-09'
module_checked_on: '2026-11-09'
summary: 问答流程先保留模型判断在图中的前景类别；在 LLaVA 内部层计算视觉 token 与类别文本 token 的响应，合成可靠激活并生成空间提示，最后交给 SAM 产生掩码。
sources:
- url: https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_The_Power_of_Prior_Training-Free_Open-Vocabulary_Semantic_Segmentation_with_LLaVA_CVPR_2026_paper.html
  locator: 正式发表页面及作者信息
- url: https://openaccess.thecvf.com/content/CVPR2026/papers/Zhang_The_Power_of_Prior_Training-Free_Open-Vocabulary_Semantic_Segmentation_with_LLaVA_CVPR_2026_paper.pdf
  locator: 方法部分；Figure 2（PDF 第 4 页）；实验 Table 1（PDF 第 7 页）
- url: https://github.com/zbf1991/FSeg-LLaVA
  locator: 官方 README 与实际代码目录；不表示已运行
figures:
- id: figure2
  label: Figure 2
  asset: assets/figures/fsegllava-figure2.png
  page: 4
  version: CVPR 2026 出版方正式版
  source_url: https://openaccess.thecvf.com/content/CVPR2026/papers/Zhang_The_Power_of_Prior_Training-Free_Open-Vocabulary_Semantic_Segmentation_with_LLaVA_CVPR_2026_paper.pdf
  source_sha256: 6f619f9df2c99d6ad8843a8cb6432194905c5b6765df55b53b7582da611c5d63
  clip_pdf_points:
  - 55
  - 50
  - 558
  - 353.5459899902344
methods:
- id: semantic-operation
  track: vocabulary
  problems:
  - prompt
  - alignment
  title: 文本激活转提示
  question: LLaVA 的语义知识怎样形成 SAM 的空间提示？
  operation: 问答流程先保留模型判断在图中的前景类别；在 LLaVA 内部层计算视觉 token 与类别文本 token 的响应，合成可靠激活并生成空间提示，最后交给 SAM 产生掩码。
  input: 图像、候选前景类别、LLaVA 内部特征
  output: 类别条件 SAM 掩码
  stage: 免任务训练推理
  supervision: 预训练 LLaVA 与 SAM；无需显式背景类别名称
  origin: proposed
  origin_note: 本文设计的文本激活转提示流程；其预训练基础模型与通用组件沿用已有方法，不计作本文新提出。
  origin_refs:
  - url: https://openaccess.thecvf.com/content/CVPR2026/papers/Zhang_The_Power_of_Prior_Training-Free_Open-Vocabulary_Semantic_Segmentation_with_LLaVA_CVPR_2026_paper.pdf
    locator: 方法部分列明的基础模型及其参考文献
  evidence:
  - url: https://openaccess.thecvf.com/content/CVPR2026/papers/Zhang_The_Power_of_Prior_Training-Free_Open-Vocabulary_Semantic_Segmentation_with_LLaVA_CVPR_2026_paper.pdf
    locator: 方法部分；Figure 2（PDF 第 4 页）；实验 Table 1（PDF 第 7 页）
  figure: figure2
  figure_guide: 左上问答分支筛选图中类别；视觉／文本 token 响应经匹配分支形成可靠激活，下面由激活生成空间提示并进入 SAM。
  depicted: true
  route:
  - LLaVA 与 SAM
  - 文本激活转提示
  - 类别空间提示
  - 开放词汇分割
  result_tables:
  - table1
results:
- id: table1
  label: Table 1
  asset: assets/results/fsegllava-table1.png
  page: 7
  version: CVPR 2026 出版方正式版
  source_url: https://openaccess.thecvf.com/content/CVPR2026/papers/Zhang_The_Power_of_Prior_Training-Free_Open-Vocabulary_Semantic_Segmentation_with_LLaVA_CVPR_2026_paper.pdf
  source_sha256: 6f619f9df2c99d6ad8843a8cb6432194905c5b6765df55b53b7582da611c5d63
  clip_pdf_points:
  - 55
  - 55
  - 558
  - 284
  title: FSeg-LLaVA：主要实验结果
  setting: 不同 LLaVA 版本及二维分割基准；原表标注无需额外背景定义。
  metrics: mIoU ↑
  reading: Thing 类数据集与 Stuff 场景分开看，且注意 LLaVA 模型规模。
---

# FSeg-LLaVA

本页按研究问题提取相关操作；模块原图、具体输入输出、来源与主要实验结果在上方展开查看。

## 研究问题

LLaVA 的语义知识怎样形成 SAM 的空间提示？

## 相关操作

问答流程先保留模型判断在图中的前景类别；在 LLaVA 内部层计算视觉 token 与类别文本 token 的响应，合成可靠激活并生成空间提示，最后交给 SAM 产生掩码。

## 实验阅读

不同 LLaVA 版本及二维分割基准；原表标注无需额外背景定义。 Thing 类数据集与 Stuff 场景分开看，且注意 LLaVA 模型规模。 主要结果是整套方法的效果，不能单凭该表归因到一个模块。

## 原文依据

- [出版方原文](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhang_The_Power_of_Prior_Training-Free_Open-Vocabulary_Semantic_Segmentation_with_LLaVA_CVPR_2026_paper.pdf)：方法部分；Figure 2（PDF 第 4 页）；实验 Table 1（PDF 第 7 页）。
- [官方实现](https://github.com/zbf1991/FSeg-LLaVA)：已检查公开目录，未独立运行训练或评测。
