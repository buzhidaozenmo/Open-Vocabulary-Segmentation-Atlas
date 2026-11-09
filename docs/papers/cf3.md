---
paper_id: cf3
title: 'CF3: Compact and Fast 3D Feature Fields'
short_name: CF3
authors:
- Lee, Hyunjoon
- Min, Joonkyu
- Park, Jaesik
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
paper_url: https://arxiv.org/pdf/2508.05254v3
publication_url: https://openaccess.thecvf.com/content/ICCV2025/html/Lee_CF3_Compact_and_Fast_3D_Feature_Fields_ICCV_2025_paper.html
code_status: public
code_url: https://github.com/SNU-VGILab/CF3
code_details: 已核对官方实现目录：3d_seg.py、3d_seg、LICENSE.md、arguments、compact_feature_field.py、configs。未独立运行或验证外部权重下载。
content_status: index
checked_on: '2026-11-09'
module_checked_on: '2026-11-09'
summary: 利用预训练高斯的渲染贡献加权融合二维特征，直接在融合后的高斯特征上训练自编码器；随后依据特征和几何优化进行自适应剪枝、合并，保留可查询的紧凑语言表示。
sources:
- url: https://openaccess.thecvf.com/content/ICCV2025/html/Lee_CF3_Compact_and_Fast_3D_Feature_Fields_ICCV_2025_paper.html
  locator: 正式发表来源：出版页面／作者项目的会议说明
- url: https://arxiv.org/pdf/2508.05254v3
  locator: 方法部分；Figure 2（PDF 第 2 页）；实验 Table 2（PDF 第 6 页）
- url: https://github.com/SNU-VGILab/CF3
  locator: 官方 README、目录与开放范围；未独立运行
figures:
- id: fig2
  label: Figure 2
  asset: assets/figures/cf3-fig2.png
  page: 2
  version: arXiv 2508.05254v3
  source_url: https://arxiv.org/pdf/2508.05254v3
  source_sha256: 2996788bb2d1853924e9ebf8d66ae453a4aa7654a5a6d64b54a45cf05af3b3f0
  clip_pdf_points:
  - 45
  - 45
  - 567
  - 271.003
methods:
- id: semantic-operation
  track: vocabulary
  problems:
  - alignment
  - efficiency
  title: 高斯语言特征压缩
  question: 多视角语言特征怎样压缩到紧凑高斯场？
  operation: 利用预训练高斯的渲染贡献加权融合二维特征，直接在融合后的高斯特征上训练自编码器；随后依据特征和几何优化进行自适应剪枝、合并，保留可查询的紧凑语言表示。
  input: 预训练 3DGS、多视角语言特征和相机
  output: 压缩稀疏的高斯语言特征场
  stage: 特征融合、场景自编码及稀疏化优化
  supervision: 二维基础模型特征与已有场景高斯
  origin: proposed
  origin_note: 本文设计的高斯语言特征压缩流程；所用预训练模型、通用投影及基础算子沿用已有方法，不计作本文新提出。
  evidence:
  - url: https://arxiv.org/pdf/2508.05254v3
    locator: 方法部分；Figure 2（PDF 第 2 页）；实验 Table 2（PDF 第 6 页）
  figure: fig2
  figure_guide: 沿 Feature Lifting → Gaussian Auto-encoder → Adaptive Sparsification 阅读；单独稀疏化图为 Figure 4。
  depicted: true
  route:
  - 预训练视觉语言特征
  - 高斯语言特征压缩
  - 高斯语言场／索引
  - 三维分割与查询
  result_tables:
  - table2
results:
- id: table2
  label: Table 2
  asset: assets/results/cf3-table2.png
  page: 6
  version: arXiv 2508.05254v3
  source_url: https://arxiv.org/pdf/2508.05254v3
  source_sha256: 2996788bb2d1853924e9ebf8d66ae453a4aa7654a5a6d64b54a45cf05af3b3f0
  clip_pdf_points:
  - 309
  - 310
  - 558
  - 425
  title: CF3：主要实验结果
  setting: LERF，CLIP+SAM 语义特征；保留模型存储、速度及语义指标。
  metrics: mIoU／mAcc ↑；存储 ↓；FPS ↑
  reading: 本表是语言特征场的整体权衡，不能只看高斯数量判断语义保真。
---

# CF3

本页按研究问题提取相关操作；模块图、输入输出、证据和主要结果表在上方展开查看。

## 研究问题

多视角语言特征怎样压缩到紧凑高斯场？

## 相关操作

利用预训练高斯的渲染贡献加权融合二维特征，直接在融合后的高斯特征上训练自编码器；随后依据特征和几何优化进行自适应剪枝、合并，保留可查询的紧凑语言表示。

## 实验阅读

LERF，CLIP+SAM 语义特征；保留模型存储、速度及语义指标。 本表是语言特征场的整体权衡，不能只看高斯数量判断语义保真。 主表是整体系统结果，单一模块的贡献需结合原文消融。

## 原文依据

- [本次阅读的原文版本](https://arxiv.org/pdf/2508.05254v3)：方法部分；Figure 2（PDF 第 2 页）；实验 Table 2（PDF 第 6 页）。
- [正式发表来源](https://openaccess.thecvf.com/content/ICCV2025/html/Lee_CF3_Compact_and_Fast_3D_Feature_Fields_ICCV_2025_paper.html)。
- [官方实现](https://github.com/SNU-VGILab/CF3)：已核对官方实现目录：3d_seg.py、3d_seg、LICENSE.md、arguments、compact_feature_field.py、configs。未独立运行或验证外部权重下载。
