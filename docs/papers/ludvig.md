---
paper_id: ludvig
title: 'LUDVIG: Learning-Free Uplifting of 2D Visual Features to Gaussian Splatting Scenes'
short_name: LUDVIG
authors:
- Marrie, Juliette
- Menegaux, Romain
- Arbel, Michael
- Larlus, Diane
- Mairal, Julien
year: 2025
preprint_date: unknown
venue: ICCV
publication_status: published
primary_direction: 3dgs
modalities:
- gaussian
- image
task_setting: open_vocabulary
task_types:
- semantic
techniques:
- semantic_alignment
datasets:
- LERF
paper_url: https://openaccess.thecvf.com/content/ICCV2025/papers/Marrie_LUDVIG_Learning-Free_Uplifting_of_2D_Visual_Features_to_Gaussian_Splatting_ICCV_2025_paper.pdf
publication_url: https://openaccess.thecvf.com/content/ICCV2025/html/Marrie_LUDVIG_Learning-Free_Uplifting_of_2D_Visual_Features_to_Gaussian_Splatting_ICCV_2025_paper.html
code_status: public
code_url: https://github.com/naver/ludvig
code_details: 已核对官方实现目录：LICENSE.txt、NOTICE.txt、clip_utils、configs、demo.jpg、demo.py。未独立运行或验证外部权重下载。
content_status: index
checked_on: '2026-11-09'
module_checked_on: '2026-11-09'
summary: 按二维渲染贡献将每视角特征加权登记到高斯；再借助 DINOv2 特征建立高斯图并扩散查询响应，修正粗语义的局部一致性，避免逐场景优化完整语言场。
sources:
- url: https://openaccess.thecvf.com/content/ICCV2025/html/Marrie_LUDVIG_Learning-Free_Uplifting_of_2D_Visual_Features_to_Gaussian_Splatting_ICCV_2025_paper.html
  locator: 正式发表来源：出版页面／作者项目的会议说明
- url: https://openaccess.thecvf.com/content/ICCV2025/papers/Marrie_LUDVIG_Learning-Free_Uplifting_of_2D_Visual_Features_to_Gaussian_Splatting_ICCV_2025_paper.pdf
  locator: 方法部分；Figure 2（PDF 第 4 页）；实验 Table 3（PDF 第 8 页）
- url: https://github.com/naver/ludvig
  locator: 官方 README、目录与开放范围；未独立运行
figures:
- id: fig2
  label: Figure 2
  asset: assets/figures/ludvig-fig2.png
  page: 4
  version: ICCV 2025 出版方正式版
  source_url: https://openaccess.thecvf.com/content/ICCV2025/papers/Marrie_LUDVIG_Learning-Free_Uplifting_of_2D_Visual_Features_to_Gaussian_Splatting_ICCV_2025_paper.pdf
  source_sha256: 81cea49d2f205124a77ed8954c6b71d501fcedf42469ad601af7e0bad4a3d833
  clip_pdf_points:
  - 45
  - 45
  - 567
  - 204.074
methods:
- id: semantic-operation
  track: vocabulary
  problems:
  - alignment
  - regions
  - efficiency
  title: 加权登记与图扩散
  question: 无需特征场优化怎样获得可查询语义？
  operation: 按二维渲染贡献将每视角特征加权登记到高斯；再借助 DINOv2 特征建立高斯图并扩散查询响应，修正粗语义的局部一致性，避免逐场景优化完整语言场。
  input: 预训练高斯、二维 CLIP／DINO 特征和查询
  output: 高斯语义特征与扩散响应
  stage: 特征登记与查询推理
  supervision: 冻结基础模型、已有重建及相机
  origin: proposed
  origin_note: 本文设计的加权登记与图扩散流程；所用预训练模型、通用投影及基础算子沿用已有方法，不计作本文新提出。
  evidence:
  - url: https://openaccess.thecvf.com/content/ICCV2025/papers/Marrie_LUDVIG_Learning-Free_Uplifting_of_2D_Visual_Features_to_Gaussian_Splatting_ICCV_2025_paper.pdf
    locator: 方法部分；Figure 2（PDF 第 4 页）；实验 Table 3（PDF 第 8 页）
  figure: fig2
  figure_guide: 看 uplifting 中二维特征的加权累积；图扩散单独由 Figure 4 展示。
  depicted: true
  route:
  - 预训练视觉语言特征
  - 加权登记与图扩散
  - 高斯语言场／索引
  - 三维分割与查询
  result_tables:
  - table3
results:
- id: table3
  label: Table 3
  asset: assets/results/ludvig-table3.png
  page: 8
  version: ICCV 2025 出版方正式版
  source_url: https://openaccess.thecvf.com/content/ICCV2025/papers/Marrie_LUDVIG_Learning-Free_Uplifting_of_2D_Visual_Features_to_Gaussian_Splatting_ICCV_2025_paper.pdf
  source_sha256: 81cea49d2f205124a77ed8954c6b71d501fcedf42469ad601af7e0bad4a3d833
  clip_pdf_points:
  - 55
  - 265
  - 299
  - 337
  title: LUDVIG：主要实验结果
  setting: LERF 对象文本定位，与交互掩码传播实验分开。
  metrics: 定位准确率 ↑
  reading: 本表衡量文本定位，不当作像素 mIoU；掩码传播主结果另见 Table 1。
---

# LUDVIG

本页按研究问题提取相关操作；模块图、输入输出、证据和主要结果表在上方展开查看。

## 研究问题

无需特征场优化怎样获得可查询语义？

## 相关操作

按二维渲染贡献将每视角特征加权登记到高斯；再借助 DINOv2 特征建立高斯图并扩散查询响应，修正粗语义的局部一致性，避免逐场景优化完整语言场。

## 实验阅读

LERF 对象文本定位，与交互掩码传播实验分开。 本表衡量文本定位，不当作像素 mIoU；掩码传播主结果另见 Table 1。 主表是整体系统结果，单一模块的贡献需结合原文消融。

## 原文依据

- [本次阅读的原文版本](https://openaccess.thecvf.com/content/ICCV2025/papers/Marrie_LUDVIG_Learning-Free_Uplifting_of_2D_Visual_Features_to_Gaussian_Splatting_ICCV_2025_paper.pdf)：方法部分；Figure 2（PDF 第 4 页）；实验 Table 3（PDF 第 8 页）。
- [正式发表来源](https://openaccess.thecvf.com/content/ICCV2025/html/Marrie_LUDVIG_Learning-Free_Uplifting_of_2D_Visual_Features_to_Gaussian_Splatting_ICCV_2025_paper.html)。
- [官方实现](https://github.com/naver/ludvig)：已核对官方实现目录：LICENSE.txt、NOTICE.txt、clip_utils、configs、demo.jpg、demo.py。未独立运行或验证外部权重下载。
