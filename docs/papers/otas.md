---
paper_id: otas
title: 'OTAS: Open-vocabulary Token Alignment for Outdoor Segmentation'
short_name: OTAS
authors: []
year: 2026
preprint_date: '2025-07-08'
venue: ICRA
publication_status: published
primary_direction: multiview
modalities:
- point_cloud
- image
task_setting: open_vocabulary
task_types:
- semantic
techniques:
- semantic_alignment
- geometry
- fusion
- efficient_inference
datasets:
- ORFD
- TartanAir
paper_url: https://arxiv.org/abs/2507.08851
publication_url: https://github.com/SimonSchwaiger/otas
code_status: public
code_url: https://github.com/SimonSchwaiger/otas
code_details: 官方仓库包含核心模型、推理、检查点下载脚本、演示与ROS 2接口；ICRA录用由作者仓库公告确认。
content_status: index
checked_on: '2026-11-09'
summary: 在单视图或多视图中对齐基础模型token，建立室外可查询语义表示。
sources:
- url: https://github.com/SimonSchwaiger/otas
  locator: 正式发表来源
- url: https://github.com/SimonSchwaiger/otas
  locator: 官方 README / 公开目录；未运行
figures:
- id: fig2
  asset: assets/figures/otas-fig2.png
  label: Figure 2
  page: 3
  version: arXiv 2507.08851v2
  source_url: https://arxiv.org/pdf/2507.08851v2
  clip_pdf_points:
  - 51
  - 45
  - 561
  - 245
  source_sha256: 66bb17e8839c87774ca91c6fc02d5e144d401e24e237848b3edf301f7d561fba
methods:
- id: map
  track: vocabulary
  problems:
  - alignment
  - regions
  title: 视觉聚类提供区域，语言 token 提供名称
  question: 非对象中心场景怎样获得可查询的密集语义？
  operation: 将 DINOv2 token 降维聚类成语义区域；在这些区域内对 CLIP 稠密 token 做 masked average pooling，归一化后与正／负文本提示比较，借冻结掩码细化器恢复像素边界。
  input: 图像、DINOv2 与 CLIP token、文本提示
  output: 语言区域特征与像素相关性
  stage: 推理
  supervision: 冻结预训练视觉、语言及掩码模型；无任务训练
  origin: modified
  origin_note: 沿用 Feature Splatting 的 MAP 思路，本文改为在共享空间的粗特征网格上池化，并结合视觉 token 聚类。
  origin_refs:
  - url: https://arxiv.org/abs/2404.01223
    locator: OTAS §III.B 引用 [5] Feature Splatting（ECCV 2024）的 MAP
  evidence:
  - url: https://arxiv.org/pdf/2507.08851v2
    locator: §III.A–C，Figure 2(b–d)
  figure: fig2
  figure_guide: 主图 b 聚类→c MAP→d 掩码细化；区域边界来自视觉聚类，类别语义来自语言 token。
  depicted: true
  route:
  - 二维密集特征
  - 视觉聚类与语言池化
  - 区域语义原型
  - 文本相似度分类
  result_tables:
  - table3
- id: spatial
  track: pointcloud
  problems:
  - projection
  - multiview
  - geometry
  title: 几何条件聚类与体素语义池化
  question: 多视图 token 怎样形成空间一致的语言点云？
  operation: 以 patch 中值深度反投影并由位姿变换到全局，拼接坐标与视觉 token 后降维聚类；将区域语言特征回投到全局点云，再在体素内平均，使跨视角语义得到空间聚合。
  input: 多视图 token、深度、相机内外参
  output: 可文本查询的空间语言点云
  stage: 多视图构建／推理
  supervision: 预训练编码器；需要深度与位姿，无额外三维网络训练
  origin: proposed
  origin_note: 本文空间条件聚类与空间池化；基础反投影和体素平均不主张独创。
  origin_refs: []
  evidence:
  - url: https://arxiv.org/pdf/2507.08851v2
    locator: §III.D，Figure 2(e)
  figure: fig2
  figure_guide: 看右侧 Geometry 分支对聚类及池化的条件连接；体素平均细节需结合 §III.D。
  depicted: true
  route:
  - 二维密集特征
  - 几何条件聚类
  - 逐点特征
  - 二维到三维传递
  result_tables:
  - table2
module_checked_on: '2026-11-09'
results:
- id: table2
  label: Table II
  asset: assets/results/otas-table2.png
  title: 多视图三维植被分割
  setting: TartanAir，已知相机位姿构建语言点云，逐点评估植被；Sec 为重建总时间，不含评估。
  metrics: IoU／Fsc／Pre／Rec ↑；Sec ↓
  reading: 逐场景比较 OTAS Spatial 与 OpenFusion、ConceptGraphs，并同时看分割质量和重建耗时。
  page: 5
  version: arXiv 2507.08851v2
  source_url: https://arxiv.org/pdf/2507.08851v2
  source_sha256: 66bb17e8839c87774ca91c6fc02d5e144d401e24e237848b3edf301f7d561fba
  clip_pdf_points:
  - 51
  - 295
  - 302
  - 562
- id: table3
  label: Table III
  asset: assets/results/otas-table3.png
  title: 单视图二维室外分割
  setting: ORFD；原表分 Fine-tuned 与 Zero-Shot 两组，† 为引用工作重实现。
  metrics: IoU／Fsc／Pre／Rec ↑；FPS ↑
  reading: 看 OTAS Small／Large 的质量和速度；原表保留微调方法与零样本方法的分组。
  page: 5
  version: arXiv 2507.08851v2
  source_url: https://arxiv.org/pdf/2507.08851v2
  source_sha256: 66bb17e8839c87774ca91c6fc02d5e144d401e24e237848b3edf301f7d561fba
  clip_pdf_points:
  - 310
  - 293
  - 561
  - 506
---
# OTAS

## 当前整理状态

已按研究关注点核查下列方法模块与配图；尚未完成全文样例笔记，不据此生成实验排名。

## 收录理由

在单视图或多视图中对齐基础模型token，建立室外可查询语义表示。

## 开源情况

【官方文档说明】官方仓库包含核心模型、推理、检查点下载脚本、演示与ROS 2接口；ICRA录用由作者仓库公告确认。 本轮没有安装或运行代码，没有独立验证权重下载。
