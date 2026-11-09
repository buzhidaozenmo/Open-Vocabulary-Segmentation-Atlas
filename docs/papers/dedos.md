---
paper_id: dedos
title: 'Images as Noisy Labels: Unleashing the Potential of the Diffusion Model for Open-Vocabulary Semantic Segmentation'
short_name: DEDOS
authors:
- Li, Fan
- Wang, Xuanbin
- Wang, Xuan
- Zhang, Zhaoxiang
- Xu, Yuelei
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
- ADE20K
- PASCAL
- COCO
paper_url: https://openaccess.thecvf.com/content/ICCV2025/papers/Li_Images_as_Noisy_Labels_Unleashing_the_Potential_of_the_Diffusion_ICCV_2025_paper.pdf
publication_url: https://openaccess.thecvf.com/content/ICCV2025/html/Li_Images_as_Noisy_Labels_Unleashing_the_Potential_of_the_Diffusion_ICCV_2025_paper.html
code_status: public
code_url: https://github.com/FanLiHub/DEDOS
code_details: 已核对官方实现目录：DEDOS、DenoiseDiff、configs、datasets、demo、index.html。未独立运行或验证外部权重下载。
content_status: index
checked_on: '2026-11-09'
module_checked_on: '2026-11-09'
summary: 在图像去噪过程中用可学习代理查询抽取稳定场景骨架，把纹理等细节与场景结构分离；以去噪前后 CLIP 特征约束查询对齐，再将所得空间先验用于开放词汇分割。
sources:
- url: https://openaccess.thecvf.com/content/ICCV2025/html/Li_Images_as_Noisy_Labels_Unleashing_the_Potential_of_the_Diffusion_ICCV_2025_paper.html
  locator: 正式发表来源：出版页面／作者项目的会议说明
- url: https://openaccess.thecvf.com/content/ICCV2025/papers/Li_Images_as_Noisy_Labels_Unleashing_the_Potential_of_the_Diffusion_ICCV_2025_paper.pdf
  locator: 方法部分；Figure 2（PDF 第 4 页）；实验 Table 1（PDF 第 6 页）
- url: https://github.com/FanLiHub/DEDOS
  locator: 官方 README、目录与开放范围；未独立运行
figures:
- id: fig2
  label: Figure 2
  asset: assets/figures/dedos-fig2.png
  page: 4
  version: ICCV 2025 出版方正式版
  source_url: https://openaccess.thecvf.com/content/ICCV2025/papers/Li_Images_as_Noisy_Labels_Unleashing_the_Potential_of_the_Diffusion_ICCV_2025_paper.pdf
  source_sha256: b0b692acd87ed7a96968375b76af7db3c2b166f042b05994c95488481275c7dd
  clip_pdf_points:
  - 45
  - 45
  - 567
  - 325.747
methods:
- id: semantic-operation
  track: vocabulary
  problems:
  - alignment
  - regions
  title: 扩散场景先验对齐
  question: 扩散特征怎样为语言分割提供空间结构？
  operation: 在图像去噪过程中用可学习代理查询抽取稳定场景骨架，把纹理等细节与场景结构分离；以去噪前后 CLIP 特征约束查询对齐，再将所得空间先验用于开放词汇分割。
  input: 图像、扩散去噪特征、代理查询和文本
  output: 场景先验增强的像素类别表示
  stage: COCO-Stuff 训练及分割推理
  supervision: COCO-Stuff 像素语义标注；预训练扩散模型和 CLIP
  origin: proposed
  origin_note: 本文设计的扩散场景先验对齐流程；所用预训练模型、通用投影及基础算子沿用已有方法，不计作本文新提出。
  evidence:
  - url: https://openaccess.thecvf.com/content/ICCV2025/papers/Li_Images_as_Noisy_Labels_Unleashing_the_Potential_of_the_Diffusion_ICCV_2025_paper.pdf
    locator: 方法部分；Figure 2（PDF 第 4 页）；实验 Table 1（PDF 第 6 页）
  figure: fig2
  figure_guide: 沿 proxy queries、diffusion denoising、CLIP supervision 的对应连接阅读。
  depicted: true
  route:
  - 预训练视觉语言特征
  - 扩散场景先验对齐
  - 像素／区域类别表示
  - 开放词汇分割
  result_tables:
  - table1
results:
- id: table1
  label: Table 1
  asset: assets/results/dedos-table1.png
  page: 6
  version: ICCV 2025 出版方正式版
  source_url: https://openaccess.thecvf.com/content/ICCV2025/papers/Li_Images_as_Noisy_Labels_Unleashing_the_Potential_of_the_Diffusion_ICCV_2025_paper.pdf
  source_sha256: b0b692acd87ed7a96968375b76af7db3c2b166f042b05994c95488481275c7dd
  clip_pdf_points:
  - 55
  - 55
  - 558
  - 301
  title: DEDOS：主要实验结果
  setting: COCO-Stuff 训练，测试 ADE20K、PASCAL 等；保留 Additional Dataset 列。
  metrics: mIoU ↑
  reading: 在相同 CLIP 骨干和训练数据下比较，扩散先验与分割训练都参与结果。
---

# DEDOS

本页按研究问题提取相关操作；模块图、输入输出、证据和主要结果表在上方展开查看。

## 研究问题

扩散特征怎样为语言分割提供空间结构？

## 相关操作

在图像去噪过程中用可学习代理查询抽取稳定场景骨架，把纹理等细节与场景结构分离；以去噪前后 CLIP 特征约束查询对齐，再将所得空间先验用于开放词汇分割。

## 实验阅读

COCO-Stuff 训练，测试 ADE20K、PASCAL 等；保留 Additional Dataset 列。 在相同 CLIP 骨干和训练数据下比较，扩散先验与分割训练都参与结果。 主表是整体系统结果，单一模块的贡献需结合原文消融。

## 原文依据

- [本次阅读的原文版本](https://openaccess.thecvf.com/content/ICCV2025/papers/Li_Images_as_Noisy_Labels_Unleashing_the_Potential_of_the_Diffusion_ICCV_2025_paper.pdf)：方法部分；Figure 2（PDF 第 4 页）；实验 Table 1（PDF 第 6 页）。
- [正式发表来源](https://openaccess.thecvf.com/content/ICCV2025/html/Li_Images_as_Noisy_Labels_Unleashing_the_Potential_of_the_Diffusion_ICCV_2025_paper.html)。
- [官方实现](https://github.com/FanLiHub/DEDOS)：已核对官方实现目录：DEDOS、DenoiseDiff、configs、datasets、demo、index.html。未独立运行或验证外部权重下载。
