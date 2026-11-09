---
paper_id: onlineanyseg
title: 'OnlineAnySeg: Online Zero-Shot 3D Segmentation by Visual Foundation Model Guided 2D Mask Merging'
short_name: OnlineAnySeg
authors:
- Tang, Yijie
- Zhang, Jiazhao
- Lan, Yuqing
- Guo, Yulan
- Dong, Dezun
- Zhu, Chenyang
- Xu, Kai
year: 2025
preprint_date: unknown
venue: CVPR
publication_status: published
primary_direction: 3d
modalities:
- point_cloud
- image
task_setting: open_vocabulary
task_types:
- instance
techniques:
- semantic_alignment
datasets:
- ScanNet
paper_url: https://openaccess.thecvf.com/content/CVPR2025/papers/Tang_OnlineAnySeg_Online_Zero-Shot_3D_Segmentation_by_Visual_Foundation_Model_Guided_CVPR_2025_paper.pdf
publication_url: https://openaccess.thecvf.com/content/CVPR2025/html/Tang_OnlineAnySeg_Online_Zero-Shot_3D_Segmentation_by_Visual_Foundation_Model_Guided_CVPR_2025_paper.html
code_status: public
code_url: https://github.com/yjtang249/OnlineAnySeg
code_details: 已核对官方实现目录：Dataset、Instance.py、MaskGraph.py、Metrics.py、PC_extractor.py、Scene_rep.py。未独立运行或验证外部权重下载。
content_status: index
checked_on: '2026-11-09'
module_checked_on: '2026-11-09'
summary: 将二维掩码提升到统一三维体素哈希空间，以哈希查询取得重叠候选；用相似性过滤完成实例合并，并同步维护掩码—实例映射表，避免对所有点对做重复空间比较。
sources:
- url: https://openaccess.thecvf.com/content/CVPR2025/html/Tang_OnlineAnySeg_Online_Zero-Shot_3D_Segmentation_by_Visual_Foundation_Model_Guided_CVPR_2025_paper.html
  locator: 正式发表来源：出版页面／作者项目的会议说明
- url: https://openaccess.thecvf.com/content/CVPR2025/papers/Tang_OnlineAnySeg_Online_Zero-Shot_3D_Segmentation_by_Visual_Foundation_Model_Guided_CVPR_2025_paper.pdf
  locator: 方法部分；Figure 3（PDF 第 5 页）；实验 Table 1（PDF 第 7 页）
- url: https://github.com/yjtang249/OnlineAnySeg
  locator: 官方 README、目录与开放范围；未独立运行
figures:
- id: fig3
  label: Figure 3
  asset: assets/figures/onlineanyseg-fig3.png
  page: 5
  version: CVPR 2025 出版方正式版
  source_url: https://openaccess.thecvf.com/content/CVPR2025/papers/Tang_OnlineAnySeg_Online_Zero-Shot_3D_Segmentation_by_Visual_Foundation_Model_Guided_CVPR_2025_paper.pdf
  source_sha256: 95bd25b6da1d2abf55bf0282ec4f47677b008010c5caab6d2acb14be82f9acdf
  clip_pdf_points:
  - 309
  - 45
  - 558
  - 176.844
methods:
- id: semantic-operation
  track: pointcloud
  problems:
  - projection
  - multiview
  - regions
  - efficiency
  title: 体素哈希掩码关联
  question: 在线如何快速判断新掩码属于哪个三维实例？
  operation: 将二维掩码提升到统一三维体素哈希空间，以哈希查询取得重叠候选；用相似性过滤完成实例合并，并同步维护掩码—实例映射表，避免对所有点对做重复空间比较。
  input: 带位姿 RGB-D 流、二维掩码与体素哈希
  output: 在线更新的三维实例及对应表
  stage: 增量建图与实例查询推理
  supervision: 二维基础模型、深度与位姿，无目标三维实例训练标注
  origin: proposed
  origin_note: 本文设计的体素哈希掩码关联流程；所用预训练模型、通用投影及基础算子沿用已有方法，不计作本文新提出。
  evidence:
  - url: https://openaccess.thecvf.com/content/CVPR2025/papers/Tang_OnlineAnySeg_Online_Zero-Shot_3D_Segmentation_by_Visual_Foundation_Model_Guided_CVPR_2025_paper.pdf
    locator: 方法部分；Figure 3（PDF 第 5 页）；实验 Table 1（PDF 第 7 页）
  figure: fig3
  figure_guide: 重点看动态同步映射表如何随 Mask Merging 更新，主流程见 Figure 2。
  depicted: true
  route:
  - 多视角二维语义
  - 体素哈希掩码关联
  - 三维实例／点特征
  - 三维分割与查询
  result_tables:
  - table1
results:
- id: table1
  label: Table 1
  asset: assets/results/onlineanyseg-table1.png
  page: 7
  version: CVPR 2025 出版方正式版
  source_url: https://openaccess.thecvf.com/content/CVPR2025/papers/Tang_OnlineAnySeg_Online_Zero-Shot_3D_Segmentation_by_Visual_Foundation_Model_Guided_CVPR_2025_paper.pdf
  source_sha256: 95bd25b6da1d2abf55bf0282ec4f47677b008010c5caab6d2acb14be82f9acdf
  clip_pdf_points:
  - 55
  - 55
  - 558
  - 212
  title: OnlineAnySeg：主要实验结果
  setting: ScanNet200 与 SceneNN 完整序列，保留在线／离线及映射评测差异。
  metrics: AP／AR 等 ↑，按原表列
  reading: 在线实例会被映射至真值几何评测，先核对原文对齐方式。
---

# OnlineAnySeg

本页按研究问题提取相关操作；模块图、输入输出、证据和主要结果表在上方展开查看。

## 研究问题

在线如何快速判断新掩码属于哪个三维实例？

## 相关操作

将二维掩码提升到统一三维体素哈希空间，以哈希查询取得重叠候选；用相似性过滤完成实例合并，并同步维护掩码—实例映射表，避免对所有点对做重复空间比较。

## 实验阅读

ScanNet200 与 SceneNN 完整序列，保留在线／离线及映射评测差异。 在线实例会被映射至真值几何评测，先核对原文对齐方式。 主表是整体系统结果，单一模块的贡献需结合原文消融。

## 原文依据

- [本次阅读的原文版本](https://openaccess.thecvf.com/content/CVPR2025/papers/Tang_OnlineAnySeg_Online_Zero-Shot_3D_Segmentation_by_Visual_Foundation_Model_Guided_CVPR_2025_paper.pdf)：方法部分；Figure 3（PDF 第 5 页）；实验 Table 1（PDF 第 7 页）。
- [正式发表来源](https://openaccess.thecvf.com/content/CVPR2025/html/Tang_OnlineAnySeg_Online_Zero-Shot_3D_Segmentation_by_Visual_Foundation_Model_Guided_CVPR_2025_paper.html)。
- [官方实现](https://github.com/yjtang249/OnlineAnySeg)：已核对官方实现目录：Dataset、Instance.py、MaskGraph.py、Metrics.py、PC_extractor.py、Scene_rep.py。未独立运行或验证外部权重下载。
