---
paper_id: semla
title: 'Semantic Library Adaptation: LoRA Retrieval and Fusion for Open-Vocabulary Semantic Segmentation'
short_name: SemLA
authors:
- Qorbani, Reza
- Villani, Gianluca
- Panagiotakopoulos, Theodoros
- Colomer, Marc Botet
- Härenstam-Nielsen, Linus
- Segu, Mattia
- Dovesi, Pier Luigi
- Karlgren, Jussi
- Cremers, Daniel
- Tombari, Federico
- Poggi, Matteo
year: 2025
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
datasets: []
paper_url: https://openaccess.thecvf.com/content/CVPR2025/papers/Qorbani_Semantic_Library_Adaptation_LoRA_Retrieval_and_Fusion_for_Open-Vocabulary_Semantic_CVPR_2025_paper.pdf
publication_url: https://openaccess.thecvf.com/content/CVPR2025/html/Qorbani_Semantic_Library_Adaptation_LoRA_Retrieval_and_Fusion_for_Open-Vocabulary_Semantic_CVPR_2025_paper.html
code_status: public
code_url: https://github.com/rezaqorbani/SemLA
code_details: 已核对官方实现目录：catseg、config、domain_orchestrator、experiments.py、experiments.sh、generate_embeddings.py。未独立运行或验证外部权重下载。
content_status: index
checked_on: '2026-11-09'
module_checked_on: '2026-11-09'
summary: 先分别在源域训练 LoRA 适配器，用 CLIP 特征建立适配器索引；测试时将当前输入作为域查询检索相关适配器，按权重合并得到当前图像的分割模型，无需再对测试图做梯度训练。
sources:
- url: https://openaccess.thecvf.com/content/CVPR2025/html/Qorbani_Semantic_Library_Adaptation_LoRA_Retrieval_and_Fusion_for_Open-Vocabulary_Semantic_CVPR_2025_paper.html
  locator: 正式发表来源：出版页面／作者项目的会议说明
- url: https://openaccess.thecvf.com/content/CVPR2025/papers/Qorbani_Semantic_Library_Adaptation_LoRA_Retrieval_and_Fusion_for_Open-Vocabulary_Semantic_CVPR_2025_paper.pdf
  locator: 方法部分；Figure 1（PDF 第 1 页）；实验 Table 1（PDF 第 6 页）
- url: https://github.com/rezaqorbani/SemLA
  locator: 官方 README、目录与开放范围；未独立运行
figures:
- id: fig1
  label: Figure 1
  asset: assets/figures/semla-fig1.png
  page: 1
  version: CVPR 2025 出版方正式版
  source_url: https://openaccess.thecvf.com/content/CVPR2025/papers/Qorbani_Semantic_Library_Adaptation_LoRA_Retrieval_and_Fusion_for_Open-Vocabulary_Semantic_CVPR_2025_paper.pdf
  source_sha256: 383ff6bb80b3ca9708b83b6f341543637689e1c2d967e76ae718339307bf99d7
  clip_pdf_points:
  - 309
  - 267
  - 558
  - 508.285
methods:
- id: semantic-operation
  track: vocabulary
  problems:
  - alignment
  - unseen
  title: 语义索引适配器检索
  question: 目标域变化时怎样选择合适的分割适配器？
  operation: 先分别在源域训练 LoRA 适配器，用 CLIP 特征建立适配器索引；测试时将当前输入作为域查询检索相关适配器，按权重合并得到当前图像的分割模型，无需再对测试图做梯度训练。
  input: 输入图像、CLIP 域特征和已训练 LoRA 库
  output: 按输入合并的分割适配器
  stage: 源域适配器训练；测试时检索融合
  supervision: 源域分割标注；测试阶段无额外标签
  origin: proposed
  origin_note: 本文设计的语义索引适配器检索流程；所用预训练模型、通用投影及基础算子沿用已有方法，不计作本文新提出。
  evidence:
  - url: https://openaccess.thecvf.com/content/CVPR2025/papers/Qorbani_Semantic_Library_Adaptation_LoRA_Retrieval_and_Fusion_for_Open-Vocabulary_Semantic_CVPR_2025_paper.pdf
    locator: 方法部分；Figure 1（PDF 第 1 页）；实验 Table 1（PDF 第 6 页）
  figure: fig1
  figure_guide: 看 CLIP domain navigator 到 adapter retrieval／fusion 的连接；库构建另见 Figure 2。
  depicted: true
  route:
  - 预训练视觉语言特征
  - 语义索引适配器检索
  - 像素／区域类别表示
  - 开放词汇分割
  result_tables:
  - table1
results:
- id: table1
  label: Table 1
  asset: assets/results/semla-table1.png
  page: 6
  version: CVPR 2025 出版方正式版
  source_url: https://openaccess.thecvf.com/content/CVPR2025/papers/Qorbani_Semantic_Library_Adaptation_LoRA_Retrieval_and_Fusion_for_Open-Vocabulary_Semantic_CVPR_2025_paper.pdf
  source_sha256: 383ff6bb80b3ca9708b83b6f341543637689e1c2d967e76ae718339307bf99d7
  clip_pdf_points:
  - 55
  - 55
  - 558
  - 165
  title: SemLA：主要实验结果
  setting: 20-domain benchmark；CAT-Seg 的 leave-one-out 设置。
  metrics: mIoU ↑
  reading: 本表排除目标域对应适配器；不要与 all-inclusive 设置混排。
---

# SemLA

本页按研究问题提取相关操作；模块图、输入输出、证据和主要结果表在上方展开查看。

## 研究问题

目标域变化时怎样选择合适的分割适配器？

## 相关操作

先分别在源域训练 LoRA 适配器，用 CLIP 特征建立适配器索引；测试时将当前输入作为域查询检索相关适配器，按权重合并得到当前图像的分割模型，无需再对测试图做梯度训练。

## 实验阅读

20-domain benchmark；CAT-Seg 的 leave-one-out 设置。 本表排除目标域对应适配器；不要与 all-inclusive 设置混排。 主表是整体系统结果，单一模块的贡献需结合原文消融。

## 原文依据

- [本次阅读的原文版本](https://openaccess.thecvf.com/content/CVPR2025/papers/Qorbani_Semantic_Library_Adaptation_LoRA_Retrieval_and_Fusion_for_Open-Vocabulary_Semantic_CVPR_2025_paper.pdf)：方法部分；Figure 1（PDF 第 1 页）；实验 Table 1（PDF 第 6 页）。
- [正式发表来源](https://openaccess.thecvf.com/content/CVPR2025/html/Qorbani_Semantic_Library_Adaptation_LoRA_Retrieval_and_Fusion_for_Open-Vocabulary_Semantic_CVPR_2025_paper.html)。
- [官方实现](https://github.com/rezaqorbani/SemLA)：已核对官方实现目录：catseg、config、domain_orchestrator、experiments.py、experiments.sh、generate_embeddings.py。未独立运行或验证外部权重下载。
