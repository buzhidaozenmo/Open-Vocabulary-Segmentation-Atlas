---
paper_id: ov3dcg
title: 'OV3D-CG: Open-vocabulary 3D Instance Segmentation with Contextual Guidance'
short_name: OV3D-CG
authors:
- Zhou, Mingquan
- He, Chen
- Wang, Ruiping
- Chen, Xilin
year: 2025
preprint_date: unknown
venue: ICCV
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
- Replica
paper_url: https://openaccess.thecvf.com/content/ICCV2025/papers/Zhou_OV3D-CG_Open-vocabulary_3D_Instance_Segmentation_with_Contextual_Guidance_ICCV_2025_paper.pdf
publication_url: https://openaccess.thecvf.com/content/ICCV2025/html/Zhou_OV3D-CG_Open-vocabulary_3D_Instance_Segmentation_with_Contextual_Guidance_ICCV_2025_paper.html
code_status: public
code_url: https://github.com/sgmzhou4/OV3D-CG
code_details: 已核对官方仓库实际实现目录：config.json、evaluation、requirements.txt、sai3d_masks_to_tensor.py、scene_mask_pipeline.py、semantic_module_pipline.py。运行及外部权重可用性未独立复现。
content_status: index
checked_on: '2026-11-09'
module_checked_on: '2026-11-09'
summary: 合并预训练三维实例分割器与 SAM 引导的三维提议；为每个实例选择最佳视角，用包围框、地标和 SAM 掩码形成三种上下文表示，送入 MLLM 的思维链提示完成类别判别。
sources:
- url: https://openaccess.thecvf.com/content/ICCV2025/html/Zhou_OV3D-CG_Open-vocabulary_3D_Instance_Segmentation_with_Contextual_Guidance_ICCV_2025_paper.html
  locator: 正式发表页面及作者信息
- url: https://openaccess.thecvf.com/content/ICCV2025/papers/Zhou_OV3D-CG_Open-vocabulary_3D_Instance_Segmentation_with_Contextual_Guidance_ICCV_2025_paper.pdf
  locator: 方法部分；Figure 2（PDF 第 3 页）；实验 Table 1（PDF 第 6 页）
- url: https://github.com/sgmzhou4/OV3D-CG
  locator: 官方 README 与实际代码目录；不表示已运行
figures:
- id: figure2
  label: Figure 2
  asset: assets/figures/ov3dcg-figure2.png
  page: 3
  version: ICCV 2025 出版方正式版
  source_url: https://openaccess.thecvf.com/content/ICCV2025/papers/Zhou_OV3D-CG_Open-vocabulary_3D_Instance_Segmentation_with_Contextual_Guidance_ICCV_2025_paper.pdf
  source_sha256: 43684cd414708e43443911d24871905f2fc9ed4408641564d3e01c838e58f927
  clip_pdf_points:
  - 55
  - 50
  - 558
  - 240.89761352539062
methods:
- id: semantic-operation
  track: pointcloud
  problems:
  - multiview
  - reliability
  - regions
  title: 视角选择与上下文推理
  question: 三维实例类别歧义怎样借助场景上下文消解？
  operation: 合并预训练三维实例分割器与 SAM 引导的三维提议；为每个实例选择最佳视角，用包围框、地标和 SAM 掩码形成三种上下文表示，送入 MLLM 的思维链提示完成类别判别。
  input: 点云、多视角图像、候选实例与类别查询
  output: 带上下文语义类别的三维实例
  stage: 提议生成与语义查询推理
  supervision: 预训练三维提议网络及二维模型；MLLM 先验
  origin: proposed
  origin_note: 本文设计的视角选择与上下文推理流程；其预训练基础模型与通用组件沿用已有方法，不计作本文新提出。
  origin_refs:
  - url: https://openaccess.thecvf.com/content/ICCV2025/papers/Zhou_OV3D-CG_Open-vocabulary_3D_Instance_Segmentation_with_Contextual_Guidance_ICCV_2025_paper.pdf
    locator: 方法部分列明的基础模型及其参考文献
  evidence:
  - url: https://openaccess.thecvf.com/content/ICCV2025/papers/Zhou_OV3D-CG_Open-vocabulary_3D_Instance_Segmentation_with_Contextual_Guidance_ICCV_2025_paper.pdf
    locator: 方法部分；Figure 2（PDF 第 3 页）；实验 Table 1（PDF 第 6 页）
  figure: figure2
  figure_guide: 按 ❶ 三维提议、❷ SAM 区域提议、❸ 最佳视角与三种上下文可视表示、❹ MLLM CoT 分类四个编号阅读。
  depicted: true
  route:
  - 二维三维提议与 MLLM
  - 视角选择与上下文推理
  - 三维实例类别
  - 开放词汇实例分割
  result_tables:
  - table1
results:
- id: table1
  label: Table 1
  asset: assets/results/ov3dcg-table1.png
  page: 6
  version: ICCV 2025 出版方正式版
  source_url: https://openaccess.thecvf.com/content/ICCV2025/papers/Zhou_OV3D-CG_Open-vocabulary_3D_Instance_Segmentation_with_Contextual_Guidance_ICCV_2025_paper.pdf
  source_sha256: 43684cd414708e43443911d24871905f2fc9ed4408641564d3e01c838e58f927
  clip_pdf_points:
  - 55
  - 53
  - 558
  - 230
  title: OV3D-CG：主要实验结果
  setting: ScanNet200；保留训练设置、二维／三维 proposal 来源及 Head／Common／Tail。
  metrics: AP／AP50／AP25 ↑
  reading: 先比较相同提议条件，再看长尾类别；原表全监督行仅作参照。
---

# OV3D-CG

本页按研究问题提取相关操作；模块原图、具体输入输出、来源与主要实验结果在上方展开查看。

## 研究问题

三维实例类别歧义怎样借助场景上下文消解？

## 相关操作

合并预训练三维实例分割器与 SAM 引导的三维提议；为每个实例选择最佳视角，用包围框、地标和 SAM 掩码形成三种上下文表示，送入 MLLM 的思维链提示完成类别判别。

## 实验阅读

ScanNet200；保留训练设置、二维／三维 proposal 来源及 Head／Common／Tail。 先比较相同提议条件，再看长尾类别；原表全监督行仅作参照。 主要结果是整套方法的效果，不能单凭该表归因到一个模块。

## 原文依据

- [出版方原文](https://openaccess.thecvf.com/content/ICCV2025/papers/Zhou_OV3D-CG_Open-vocabulary_3D_Instance_Segmentation_with_Contextual_Guidance_ICCV_2025_paper.pdf)：方法部分；Figure 2（PDF 第 3 页）；实验 Table 1（PDF 第 6 页）。
- [官方实现](https://github.com/sgmzhou4/OV3D-CG)：已检查公开目录，未独立运行训练或评测。
