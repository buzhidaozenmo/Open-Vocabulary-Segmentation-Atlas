---
paper_id: glaclip
title: 'Looking Beyond the Window: Global-Local Aligned CLIP for Training-free Open-Vocabulary Semantic Segmentation'
short_name: GLA-CLIP
authors:
- Lee, ByeongCheol
- Seong, Hyun Seok
- Hyun, Sangeek
- Park, Gilhan
- Moon, WonJun
- Heo, Jae-Pil
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
- Cityscapes
- ADE20K
paper_url: https://openaccess.thecvf.com/content/CVPR2026/papers/Lee_Looking_Beyond_the_Window_Global-Local_Aligned_CLIP_for_Training-free_Open-Vocabulary_CVPR_2026_paper.pdf
publication_url: https://openaccess.thecvf.com/content/CVPR2026/html/Lee_Looking_Beyond_the_Window_Global-Local_Aligned_CLIP_for_Training-free_Open-Vocabulary_CVPR_2026_paper.html
code_status: public
code_url: https://github.com/2btlFe/GLA-CLIP
code_details: 已核对官方仓库实际实现目录：__init__.py、cfg.py、configs、custom_datasets.py、datasets、eval.py。运行及外部权重可用性未独立复现。
content_status: index
checked_on: '2026-11-09'
module_checked_on: '2026-11-09'
summary: 将各窗口的键和值扩展为全图窗口集合；用来自所有窗口的高相似 token 聚合代理锚点，缓解窗口内部查询偏置，再通过动态注意力归一化适配对象尺度，聚合 CLIP 值特征后与文本匹配。
sources:
- url: https://openaccess.thecvf.com/content/CVPR2026/html/Lee_Looking_Beyond_the_Window_Global-Local_Aligned_CLIP_for_Training-free_Open-Vocabulary_CVPR_2026_paper.html
  locator: 正式发表页面及作者信息
- url: https://openaccess.thecvf.com/content/CVPR2026/papers/Lee_Looking_Beyond_the_Window_Global-Local_Aligned_CLIP_for_Training-free_Open-Vocabulary_CVPR_2026_paper.pdf
  locator: 方法部分；Figure 2（PDF 第 3 页）；实验 Table 1（PDF 第 6 页）
- url: https://github.com/2btlFe/GLA-CLIP
  locator: 官方 README 与实际代码目录；不表示已运行
figures:
- id: figure2
  label: Figure 2
  asset: assets/figures/glaclip-figure2.png
  page: 3
  version: CVPR 2026 出版方正式版
  source_url: https://openaccess.thecvf.com/content/CVPR2026/papers/Lee_Looking_Beyond_the_Window_Global-Local_Aligned_CLIP_for_Training-free_Open-Vocabulary_CVPR_2026_paper.pdf
  source_sha256: 71c67af920bee5d12e63380183ad0e881e9fa13bdd3a07728cc0ff0f82c0d934
  clip_pdf_points:
  - 55
  - 50
  - 558
  - 262.3849792480469
methods:
- id: semantic-operation
  track: vocabulary
  problems:
  - alignment
  - regions
  title: 全局局部注意聚合
  question: 独立滑窗之间的语义如何保持一致？
  operation: 将各窗口的键和值扩展为全图窗口集合；用来自所有窗口的高相似 token 聚合代理锚点，缓解窗口内部查询偏置，再通过动态注意力归一化适配对象尺度，聚合 CLIP 值特征后与文本匹配。
  input: 多窗口 CLIP 与视觉基础模型特征、文本
  output: 跨窗口一致的像素语言特征
  stage: 免任务训练推理
  supervision: 冻结预训练 CLIP／视觉模型
  origin: proposed
  origin_note: 本文设计的全局局部注意聚合流程；其预训练基础模型与通用组件沿用已有方法，不计作本文新提出。
  origin_refs:
  - url: https://openaccess.thecvf.com/content/CVPR2026/papers/Lee_Looking_Beyond_the_Window_Global-Local_Aligned_CLIP_for_Training-free_Open-Vocabulary_CVPR_2026_paper.pdf
    locator: 方法部分列明的基础模型及其参考文献
  evidence:
  - url: https://openaccess.thecvf.com/content/CVPR2026/papers/Lee_Looking_Beyond_the_Window_Global-Local_Aligned_CLIP_for_Training-free_Open-Vocabulary_CVPR_2026_paper.pdf
    locator: 方法部分；Figure 2（PDF 第 3 页）；实验 Table 1（PDF 第 6 页）
  figure: figure2
  figure_guide: 依次看 Sec. 3.2 Key-Value Extension、Sec. 3.3 Proxy Anchor 和 Sec. 3.4 Dynamic Normalization；查询来自当前窗口，键和值覆盖其他窗口。
  depicted: true
  route:
  - CLIP 与视觉结构特征
  - 全局局部注意聚合
  - 像素语言特征
  - 开放词汇分割
  result_tables:
  - table1
results:
- id: table1
  label: Table 1
  asset: assets/results/glaclip-table1.png
  page: 6
  version: CVPR 2026 出版方正式版
  source_url: https://openaccess.thecvf.com/content/CVPR2026/papers/Lee_Looking_Beyond_the_Window_Global-Local_Aligned_CLIP_for_Training-free_Open-Vocabulary_CVPR_2026_paper.pdf
  source_sha256: 71c67af920bee5d12e63380183ad0e881e9fa13bdd3a07728cc0ff0f82c0d934
  clip_pdf_points:
  - 55
  - 53
  - 558
  - 384
  title: GLA-CLIP：主要实验结果
  setting: ViT-B/16 八基准；原表区分 DS hyperparameter、rename trick、默认与 Best 手调设置。
  metrics: mIoU ↑
  reading: 默认 Ours 与手调 Best 分开；多提示重命名也是额外条件。
---

# GLA-CLIP

本页按研究问题提取相关操作；模块原图、具体输入输出、来源与主要实验结果在上方展开查看。

## 研究问题

独立滑窗之间的语义如何保持一致？

## 相关操作

将各窗口的键和值扩展为全图窗口集合；用来自所有窗口的高相似 token 聚合代理锚点，缓解窗口内部查询偏置，再通过动态注意力归一化适配对象尺度，聚合 CLIP 值特征后与文本匹配。

## 实验阅读

ViT-B/16 八基准；原表区分 DS hyperparameter、rename trick、默认与 Best 手调设置。 默认 Ours 与手调 Best 分开；多提示重命名也是额外条件。 主要结果是整套方法的效果，不能单凭该表归因到一个模块。

## 原文依据

- [出版方原文](https://openaccess.thecvf.com/content/CVPR2026/papers/Lee_Looking_Beyond_the_Window_Global-Local_Aligned_CLIP_for_Training-free_Open-Vocabulary_CVPR_2026_paper.pdf)：方法部分；Figure 2（PDF 第 3 页）；实验 Table 1（PDF 第 6 页）。
- [官方实现](https://github.com/2btlFe/GLA-CLIP)：已检查公开目录，未独立运行训练或评测。
