---
paper_id: scclip
title: Self-Calibrated CLIP for Training-Free Open-Vocabulary Segmentation
short_name: SC-CLIP
authors:
- Sule Bai
- Yong Liu
- Yifei Han
- Haoji Zhang
- Yansong Tang
- Jie Zhou
- Jiwen Lu
year: 2025
preprint_date: unknown
venue: IEEE TIP
publication_status: published
primary_direction: 2d
modalities:
- image
task_setting: open_vocabulary
task_types:
- semantic
techniques:
- semantic_alignment
- reliability
- fusion
datasets:
- PASCAL
- COCO
- Cityscapes
- ADE20K
- MESS
paper_url: https://arxiv.org/pdf/2411.15869v3
publication_url: https://doi.org/10.1109/TIP.2025.3639996
code_status: public
code_url: https://github.com/SuleBai/SC-CLIP
code_details: 官方仓库含 scclip_segmentor.py、eval.py、配置及演示；方法免任务训练，仍依赖预训练 CLIP，未运行。
content_status: index
checked_on: '2026-11-09'
module_checked_on: '2026-11-09'
summary: 替换异常 token，以 CLIP 中层相似性修正深层聚合，并通过末层对齐融合多层语义。
sources:
- url: https://doi.org/10.1109/TIP.2025.3639996
  locator: 正式发表：出版方页面／DOI；期刊状态另由官方仓库文档确认
- url: https://arxiv.org/pdf/2411.15869v3
  locator: 本次所读原文版本的 §3–5／III–V、方法图及主要结果表
- url: https://github.com/SuleBai/SC-CLIP
  locator: 官方仓库实际目录与文档／项目页；未运行
figures:
- id: fig3
  label: Figure 3
  asset: assets/figures/scclip-fig3.png
  page: 3
  version: arXiv 2411.15869v3
  source_url: https://arxiv.org/pdf/2411.15869v3
  clip_pdf_points:
  - 45
  - 45
  - 568
  - 163
  source_sha256: f2d33b7a9bbe94739631b7d31587ac886dbbe5871020dc7f4844fa6707d4d150
- id: fig5
  label: Figure 5
  asset: assets/figures/scclip-fig5.png
  page: 5
  version: arXiv 2411.15869v3
  source_url: https://arxiv.org/pdf/2411.15869v3
  clip_pdf_points:
  - 45
  - 45
  - 568
  - 221
  source_sha256: f2d33b7a9bbe94739631b7d31587ac886dbbe5871020dc7f4844fa6707d4d150
methods:
- id: anomaly
  track: vocabulary
  problems:
  - alignment
  - reliability
  title: LOF 定位异常 token 并以邻域替换
  question: 异常 token 吸走注意力时，怎样恢复局部信息？
  operation: 在末层前的 token 特征上使用 LOF 检测局部密度异常；将异常 token 替换为周围 3×3 非异常邻居的插值，排除中心及其他异常 token，再执行末层密集预测。
  input: CLIP 末层前 patch 特征
  output: 修复后的空间 token 特征
  stage: 推理
  supervision: 预训练 CLIP；无新参数训练或额外视觉骨干
  origin: modified
  origin_note: LOF 异常检测沿用已有算法；邻域替换与 CLIP 密集推理组合为本文设计。
  origin_refs:
  - url: https://sigmodrecord.org/2000/06/07/lof-identifying-density-based-local-outliers/
    locator: 原文 [17] LOF，Breunig et al., 2000
  evidence:
  - url: https://arxiv.org/pdf/2411.15869v3
    locator: §III.B，Eq.3
  figure: fig3
  figure_guide: 独立图 (a) 看 Locate Anomaly Token→Replace；(b) 对比修复后的注意力。
  depicted: true
  route:
  - 二维密集特征
  - 异常特征邻域修复
  - 二维密集特征
  - 文本相似度分类
- id: coherence
  track: vocabulary
  problems:
  - alignment
  - regions
  title: 中层相似性聚合与两次末层对齐
  question: 如何把 CLIP 中层空间一致性接入语言预测？
  operation: 用中层 patch 相似度归一化加权深层特征，并增强末层 self-self attention；多层信息不直接加到语言嵌入，而把原末层前特征与中层融合特征分别送过末层后再融合，保留文本对齐能力。
  input: CLIP 中层／深层特征与注意力
  output: 语言对齐密集特征和类别图
  stage: 推理
  supervision: 预训练 CLIP；免任务训练
  origin: proposed
  origin_note: 本文 self-adjusting 与 two-pass 策略；两次末层前向并非视频时间记忆。
  origin_refs: []
  evidence:
  - url: https://arxiv.org/pdf/2411.15869v3
    locator: §III.C–D，Eq.4–5
  figure: fig5
  figure_guide: 独立图展示 (a) 中层相似性聚合与 (b) 注意力增强；two-pass 细节未画在此图中，见 §III.D。
  depicted: true
  route:
  - 二维密集特征
  - 中层引导对齐融合
  - 二维密集特征
  - 文本相似度分类
results:
- id: table1
  label: Table I
  asset: assets/results/scclip-table1.png
  page: 6
  version: arXiv 2411.15869v3
  source_url: https://arxiv.org/pdf/2411.15869v3
  clip_pdf_points:
  - 45
  - 48
  - 568
  - 383
  source_sha256: f2d33b7a9bbe94739631b7d31587ac886dbbe5871020dc7f4844fa6707d4d150
  title: 八个二维开放词汇分割基准
  setting: 当前所读 arXiv v3 Table I；作者按 IV-A 协议复测方法，区分 ViT-B／16 与 ViT-L／14。
  metrics: mIoU ↑；Avg. ↑
  reading: 看各骨干下的 SC-CLIP 行；保留背景类别划分及 †、* 等复测说明。
---
# SC-CLIP

## 资料范围与状态

核查版本：arXiv 2411.15869v3；正式发表来源另见出版方链接。已完成与研究关注点有关的方法、配图和主结果表定向整理，尚未完成全文样例笔记。图中的方法关系以原文为准，未独立运行实现。

## 关注的问题

【原文事实】替换异常 token，以 CLIP 中层相似性修正深层聚合，并通过末层对齐融合多层语义。

## 实验阅读

当前所读 arXiv v3 Table I；作者按 IV-A 协议复测方法，区分 ViT-B／16 与 ViT-L／14。 看各骨干下的 SC-CLIP 行；保留背景类别划分及 †、* 等复测说明。 数值保留在原始结果表中；它们是论文报告值，不是本库复现值。

## 开源情况

【官方文档说明／项目页核查】官方仓库含 scclip_segmentor.py、eval.py、配置及演示；方法免任务训练，仍依赖预训练 CLIP，未运行。 本轮没有安装依赖、执行训练或验证复现结果。
