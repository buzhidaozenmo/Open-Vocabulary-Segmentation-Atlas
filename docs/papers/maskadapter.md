---
paper_id: maskadapter
title: 'Mask-Adapter: The Devil is in the Masks for Open-Vocabulary Segmentation'
short_name: Mask-Adapter
authors:
- Yongkang Li
- Tianheng Cheng
- Bin Feng
- Wenyu Liu
- Xinggang Wang
year: 2025
preprint_date: '2024-12-05'
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
- region_aggregation
datasets:
- COCO
- ADE20K
- PASCAL
paper_url: https://openaccess.thecvf.com/content/CVPR2025/papers/Li_Mask-Adapter_The_Devil_is_in_the_Masks_for_Open-Vocabulary_Segmentation_CVPR_2025_paper.pdf
publication_url: https://openaccess.thecvf.com/content/CVPR2025/html/Li_Mask-Adapter_The_Devil_is_in_the_Masks_for_Open-Vocabulary_Segmentation_CVPR_2025_paper.html
code_status: public
code_url: https://github.com/hustvl/MaskAdapter
code_details: 官方仓库含 mask_adapter、训练入口、配置和已发布权重表，提供 SAM-2 演示；未运行，未独立验证权重下载。
content_status: index
checked_on: '2026-11-09'
module_checked_on: '2026-11-09'
summary: 用可学习语义激活图聚合 CLIP 区域特征，并用掩码一致性训练改善开放词汇分类。
sources:
- url: https://openaccess.thecvf.com/content/CVPR2025/html/Li_Mask-Adapter_The_Devil_is_in_the_Masks_for_Open-Vocabulary_Segmentation_CVPR_2025_paper.html
  locator: CVPR 2025 正式发表页面
- url: https://openaccess.thecvf.com/content/CVPR2025/papers/Li_Mask-Adapter_The_Devil_is_in_the_Masks_for_Open-Vocabulary_Segmentation_CVPR_2025_paper.pdf
  locator: CVPR 2025 正文 §3–4，方法图及主要结果表
- url: https://github.com/hustvl/MaskAdapter
  locator: 官方 README 与实际目录；未运行或逐行审计
figures:
- id: fig3
  asset: assets/figures/maskadapter-fig3.png
  label: Figure 3
  page: 4
  version: CVPR 2025 出版方正式版
  source_url: https://openaccess.thecvf.com/content/CVPR2025/papers/Li_Mask-Adapter_The_Devil_is_in_the_Masks_for_Open-Vocabulary_Segmentation_CVPR_2025_paper.pdf
  clip_pdf_points:
  - 55
  - 60
  - 557
  - 235
  source_sha256: d47d35a4c8fd29831e5a64ce503d8eebebe601fe5d19f7ad0f77dced575a2df5
methods:
- id: semanticmaps
  track: vocabulary
  problems:
  - alignment
  - regions
  title: 语义激活图替代固定掩码池化
  question: 高质量掩码为什么仍可能被 CLIP 错分，怎样改善区域语义？
  operation: 把二值掩码用步幅卷积 patchify 到 CLIP 特征分辨率，与 CLIP 特征相加，经 ConvNeXt 块输出每个掩码的 K 张语义激活图；各图归一化后加权聚合 CLIP 特征，再跨 K 个嵌入平均，与文本嵌入匹配。激活范围可包含掩码外上下文。
  input: 类别无关掩码、CLIP 图像特征、类别文本
  output: 开放词汇掩码嵌入与类别分数
  stage: 训练与推理
  supervision: 冻结 CLIP 和掩码生成器；以 COCO 掩码及类别监督训练适配器；不是免训练方法
  origin: proposed
  origin_note: 本文的语义激活图与掩码适配器；CLIP 文本匹配沿用预训练模型能力。
  origin_refs: []
  evidence:
  - url: https://openaccess.thecvf.com/content/CVPR2025/papers/Li_Mask-Adapter_The_Devil_is_in_the_Masks_for_Open-Vocabulary_Segmentation_CVPR_2025_paper.pdf
    locator: §3.2，Eq.3–4，Figure 3
  figure: fig3
  figure_guide: 主图 (b) 看 Patchify→特征融合→ConvNeXt→激活图；(a) 看激活图池化后与文本嵌入匹配。
  depicted: true
  route:
  - 二维区域特征
  - 注意力区域聚合
  - 实例特征
  - 文本相似度分类
- id: consistency
  track: vocabulary
  problems:
  - alignment
  - reliability
  title: IoU 多对匹配与掩码一致性训练
  question: 预测掩码稍有变化时，如何避免类别嵌入不稳定？
  operation: 以 IoU 阈值选择预测掩码与真值的匹配对，允许一个对象提供多个训练样本；先用真值掩码预热，再混合真值及匹配预测掩码训练，并用 1−cos 约束两者的适配器嵌入一致，配合类别交叉熵。
  input: 真值掩码及类别、预测掩码、CLIP 特征
  output: 对掩码变化更稳健的区域嵌入
  stage: 训练
  supervision: COCO-Stuff 或 COCO Panoptic 掩码及类别标签
  origin: proposed
  origin_note: IoU-based matcher、mask consistency 和两阶段对齐训练均按本文定义记录。
  origin_refs: []
  evidence:
  - url: https://openaccess.thecvf.com/content/CVPR2025/papers/Li_Mask-Adapter_The_Devil_is_in_the_Masks_for_Open-Vocabulary_Segmentation_CVPR_2025_paper.pdf
    locator: §3.3–3.5，Eq.5–7
  figure: fig3
  figure_guide: 主图标出可训练适配器；IoU 匹配和一致性损失没有画在该图中，需结合 §3.3–3.5。
  depicted: false
  route:
  - 二维区域特征
  - 掩码一致性训练
  - 实例特征
  - 对齐训练
results:
- id: table1
  asset: assets/results/maskadapter-table1.png
  label: Table 1
  page: 6
  version: CVPR 2025 出版方正式版
  source_url: https://openaccess.thecvf.com/content/CVPR2025/papers/Li_Mask-Adapter_The_Devil_is_in_the_Masks_for_Open-Vocabulary_Segmentation_CVPR_2025_paper.pdf
  clip_pdf_points:
  - 55
  - 68
  - 557
  - 387
  source_sha256: d47d35a4c8fd29831e5a64ce503d8eebebe601fe5d19f7ad0f77dced575a2df5
  title: 二维开放词汇语义分割主结果
  setting: ADE20K 150／847、PASCAL Context 59／459、PASCAL VOC 20；原表保留 VLM 骨干和 COCO-Stuff／Panoptic 训练设置。
  metrics: mIoU ↑
  reading: 按相同骨干与训练数据比较添加适配器前后；并非每列都提升，例如 FC-CLIP 的 A-847 从 14.8 降至 14.1。
---
# Mask-Adapter

## 资料范围与状态

本轮核查 CVPR 2025 正式正文 §3–4、方法图与主结果表，以及官方仓库文档和实际目录。已完成研究关注点的定向模块整理，尚未完成全文样例笔记；没有运行代码或复现实验。

## 关注的问题

用可学习语义激活图聚合 CLIP 区域特征，并用掩码一致性训练改善开放词汇分类。

## 实验阅读

【原文事实】ADE20K 150／847、PASCAL Context 59／459、PASCAL VOC 20；原表保留 VLM 骨干和 COCO-Stuff／Panoptic 训练设置。 按相同骨干与训练数据比较添加适配器前后；并非每列都提升，例如 FC-CLIP 的 A-847 从 14.8 降至 14.1。 结果来自原文报告，完整比较行、训练组与脚注见展开区原表。

## 开源情况

【官方文档说明】官方仓库含 mask_adapter、训练入口、配置和已发布权重表，提供 SAM-2 演示；未运行，未独立验证权重下载。 依赖的外部教师和模型许可需遵循各原始项目。
