---
paper_id: realm
title: 'REALM: An MLLM-Agent Framework for Open World 3D Reasoning Segmentation and Editing on Gaussian Splatting'
short_name: REALM
authors:
- Shi, Changyue
- Chen, Minghao
- Mao, Yiping
- Yang, Chuxiao
- Hu, Xinyuan
- Ding, Jiajun
- Yu, Zhou
year: 2026
preprint_date: unknown
venue: CVPR
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
- 3D-OVS
paper_url: https://openaccess.thecvf.com/content/CVPR2026/papers/Shi_REALM_An_MLLM-Agent_Framework_for_Open_World_3D_Reasoning_Segmentation_CVPR_2026_paper.pdf
publication_url: https://openaccess.thecvf.com/content/CVPR2026/html/Shi_REALM_An_MLLM-Agent_Framework_for_Open_World_3D_Reasoning_Segmentation_CVPR_2026_paper.html
code_status: public
code_url: https://github.com/ChangyueShi/REALM-Code
code_details: 已核对官方仓库实际实现目录：arguments、config、debug、ext、gaussian_renderer、reason_seg.py。运行及外部权重可用性未独立复现。
content_status: index
checked_on: '2026-11-09'
module_checked_on: '2026-11-09'
summary: 在已重建 3DGS 中渲染多个全局视角，分别让 MLLM 代理进行粗定位并聚合判断；再渲染目标近景，用局部语言掩码细化三维分割，降低任意单视角输入的敏感性。
sources:
- url: https://openaccess.thecvf.com/content/CVPR2026/html/Shi_REALM_An_MLLM-Agent_Framework_for_Open_World_3D_Reasoning_Segmentation_CVPR_2026_paper.html
  locator: 正式发表页面及作者信息
- url: https://openaccess.thecvf.com/content/CVPR2026/papers/Shi_REALM_An_MLLM-Agent_Framework_for_Open_World_3D_Reasoning_Segmentation_CVPR_2026_paper.pdf
  locator: 方法部分；Figure 3（PDF 第 3 页）；实验 Table 1（PDF 第 6 页）
- url: https://github.com/ChangyueShi/REALM-Code
  locator: 官方 README 与实际代码目录；不表示已运行
figures:
- id: figure3
  label: Figure 3
  asset: assets/figures/realm-figure3.png
  page: 3
  version: CVPR 2026 出版方正式版
  source_url: https://openaccess.thecvf.com/content/CVPR2026/papers/Shi_REALM_An_MLLM-Agent_Framework_for_Open_World_3D_Reasoning_Segmentation_CVPR_2026_paper.pdf
  source_sha256: 5a50c36752703f531e6665325123b98d0c05260790ad6cf388b5e3f367ff6e00
  clip_pdf_points:
  - 55
  - 50
  - 558
  - 343.09417724609375
methods:
- id: semantic-operation
  track: vocabulary
  problems:
  - prompt
  - regions
  title: 全局局部语言定位
  question: 隐式语言要求怎样定位到三维目标？
  operation: 在已重建 3DGS 中渲染多个全局视角，分别让 MLLM 代理进行粗定位并聚合判断；再渲染目标近景，用局部语言掩码细化三维分割，降低任意单视角输入的敏感性。
  input: 3DGS 场景、自然语言隐式指令、渲染视图
  output: 语言目标的三维掩码
  stage: 场景查询推理
  supervision: 预训练 MLLM 与掩码模型；已有场景重建
  origin: proposed
  origin_note: 本文设计的全局局部语言定位流程；其预训练基础模型与通用组件沿用已有方法，不计作本文新提出。
  origin_refs:
  - url: https://openaccess.thecvf.com/content/CVPR2026/papers/Shi_REALM_An_MLLM-Agent_Framework_for_Open_World_3D_Reasoning_Segmentation_CVPR_2026_paper.pdf
    locator: 方法部分列明的基础模型及其参考文献
  evidence:
  - url: https://openaccess.thecvf.com/content/CVPR2026/papers/Shi_REALM_An_MLLM-Agent_Framework_for_Open_World_3D_Reasoning_Segmentation_CVPR_2026_paper.pdf
    locator: 方法部分；Figure 3（PDF 第 3 页）；实验 Table 1（PDF 第 6 页）
  figure: figure3
  figure_guide: 沿上部 Global-to-Local Spatial Grounding 的全局渲染视角、MLLM 判断和近景细化阅读；下部给出语言掩码与三维表示的对应。
  depicted: true
  route:
  - 多视图与 MLLM
  - 全局局部语言定位
  - 三维目标掩码
  - 推理分割
  result_tables:
  - table1
results:
- id: table1
  label: Table 1
  asset: assets/results/realm-table1.png
  page: 6
  version: CVPR 2026 出版方正式版
  source_url: https://openaccess.thecvf.com/content/CVPR2026/papers/Shi_REALM_An_MLLM-Agent_Framework_for_Open_World_3D_Reasoning_Segmentation_CVPR_2026_paper.pdf
  source_sha256: 5a50c36752703f531e6665325123b98d0c05260790ad6cf388b5e3f367ff6e00
  clip_pdf_points:
  - 55
  - 67
  - 558
  - 176
  title: REALM：主要实验结果
  setting: LERF、3D-OVS、REALM3D 的 implicit query 协议。
  metrics: mIoU ↑
  reading: 本表比较隐式查询；与只给类别名称的分割任务分开阅读。
---

# REALM

本页按研究问题提取相关操作；模块原图、具体输入输出、来源与主要实验结果在上方展开查看。

## 研究问题

隐式语言要求怎样定位到三维目标？

## 相关操作

在已重建 3DGS 中渲染多个全局视角，分别让 MLLM 代理进行粗定位并聚合判断；再渲染目标近景，用局部语言掩码细化三维分割，降低任意单视角输入的敏感性。

## 实验阅读

LERF、3D-OVS、REALM3D 的 implicit query 协议。 本表比较隐式查询；与只给类别名称的分割任务分开阅读。 主要结果是整套方法的效果，不能单凭该表归因到一个模块。

## 原文依据

- [出版方原文](https://openaccess.thecvf.com/content/CVPR2026/papers/Shi_REALM_An_MLLM-Agent_Framework_for_Open_World_3D_Reasoning_Segmentation_CVPR_2026_paper.pdf)：方法部分；Figure 3（PDF 第 3 页）；实验 Table 1（PDF 第 6 页）。
- [官方实现](https://github.com/ChangyueShi/REALM-Code)：已检查公开目录，未独立运行训练或评测。
