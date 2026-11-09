---
paper_id: eovsam
title: 'EOVSAM: Efficient Open-Vocabulary Segmentation with SAM 3 in One Pass'
short_name: EOVSAM
authors:
- Haomin Peng
- Yongkang Li
- Zhaoxiang Liu
- Xiaojie Jin
- Shiguo Lian
- Yunchao Wei
- Xinggang Wang
year: 2026
preprint_date: '2026-08-03'
venue: arXiv
publication_status: preprint
primary_direction: 2d
modalities:
- image
task_setting: open_vocabulary
task_types:
- semantic
- panoptic
techniques:
- semantic_alignment
- region_aggregation
- efficient_inference
datasets:
- ADE20K
- PASCAL
- COCO
paper_url: https://arxiv.org/abs/2608.02284
publication_url: ''
code_status: public
code_url: https://github.com/hustvl/EOVSAM
code_details: 官方仓库提供训练与语义/全景评测配置、模型入口和SAM3基线流程；未独立验证下载与运行。
content_status: detailed_sample
checked_on: '2026-11-09'
summary: 将SAM3适配为单次前向掩码生成器，以注意力聚合支持开放词汇识别。
sources:
- url: https://arxiv.org/abs/2608.02284
  locator: 预印本身份
- url: https://arxiv.org/html/2608.02284v1
  locator: v1 Approach / Table 1、4
- url: https://github.com/hustvl/EOVSAM
  locator: 官方 README / 公开目录；未运行
figures:
- id: fig2
  asset: assets/figures/eovsam-fig2.png
  label: Figure 2
  page: 3
  version: arXiv 2608.02284v1
  source_url: https://arxiv.org/pdf/2608.02284v1
  clip_pdf_points:
  - 51
  - 45
  - 560
  - 248
  source_sha256: e64284eb685abdf944e639233235d3090fae775a38d4e92e1763ace1385081c6
- id: fig3
  asset: assets/figures/eovsam-fig3.png
  label: Figure 3
  page: 4
  version: arXiv 2608.02284v1
  source_url: https://arxiv.org/pdf/2608.02284v1
  clip_pdf_points:
  - 316
  - 45
  - 561
  - 452
  source_sha256: e64284eb685abdf944e639233235d3090fae775a38d4e92e1763ace1385081c6
methods:
- id: aggregation
  track: vocabulary
  problems:
  - alignment
  - regions
  title: 单次掩码生成与注意力语义聚合
  question: 怎样避免每个文本类别重复运行 SAM3？
  operation: 用共享骨干并行产生 SAM 与 SigLIP 特征；移除文本条件的掩码生成依赖，单次解码得到掩码及可学习注意力；按注意力聚合 SigLIP 特征，再与目标类别的 SigLIP 文本嵌入做余弦分类。
  input: 图像、目标类别文本
  output: 多个掩码及开放词汇类别分数
  stage: 训练与单次前向推理
  supervision: 预训练 SAM3／SigLIP2 对齐骨干和 COCO Panoptic 掩码监督
  origin: modified
  origin_note: 在 SAM3 上修改骨干与解码分类流程；Attentional Aggregation 为本文设计。
  origin_refs:
  - url: https://arxiv.org/abs/2511.16719
    locator: EOVSAM §3 以 SAM3 为基础
  evidence:
  - url: https://arxiv.org/pdf/2608.02284v1
    locator: §3，Figure 2–3
  figure: fig3
  figure_guide: 独立聚合比较图看 (c) Attentional Aggregation，并保留梯度流图例；总流程另见 Figure 2。
  depicted: true
  route:
  - 二维区域特征
  - 注意力区域聚合
  - 实例特征
  - 文本相似度分类
module_checked_on: '2026-11-09'
---
# EOVSAM

## 资料范围与版本

阅读 arXiv:2608.02284 **v1（2026-08-03）**。本轮未核实到顶会顶刊正式收录，因此始终标为预印本。官方仓库已提供实际训练与评测入口；未下载训练权重、未运行评测。

## 任务

【原文事实】研究二维开放词汇语义与全景分割。训练使用 COCO Panoptic 的监督，测试以新的文本类别词表分类。它是 **有任务训练的 SAM3 适配方法**，不属于 training-free 方法。

## 研究问题

原始 SAM3 为单概念提示生成匹配掩码。逐类别处理大词表产生重复计算，多类别结果还需要解决掩码冲突。EOVSAM 将定位与开放词汇识别整合为单次前向，避免随类别数反复执行提示条件解码（Introduction、Approach、Fig.1–2）。

## 方法

1. **去除提示条件的掩码生成。** 从 fusion encoder 与 detector decoder 移除文本 cross-attention，保留可加载 SAM3 权重的主要结构，使对象查询一次产生多个掩码。这里的 prompt-free 指掩码生成不再逐概念条件化，**最终分类仍使用文本词表**。
2. **双角色视觉特征。** 用 C-RADIOv4 的特征头分别提供适于 SAM3 定位和 SigLIP2 识别的表示，避免独立运行多个大型视觉编码器。不能误写成所有视觉编码均由原始 SAM3 backbone 完成。
3. **Attentional Aggregation（式(3)–(4)）。** 解码器注意力对 SigLIP2 空间特征加权，形成每个对象的嵌入，再与 SigLIP2 文本分类器比较。连续注意力使识别目标能够参与端到端优化，而不是先二值化掩码后独立分类。
4. **辅助 SAM 分类与目标存在性。** 方法还构建 SAM 文本分类器及背景 token，作为存在性和补充分类信号；它与主 SigLIP2 开放词汇识别分支不是同一个角色。
5. **联合损失（Objective）。** 包含分类、掩码 BCE/Dice、开放词汇识别以及边框 L1/GIoU 等监督。可训练参数与冻结细节需要按训练配置逐项核查，本站不凭结构图补写。

## 实验 {#experiments}

【原文事实】Table 1 区分 COCO-Stuff、COCO Panoptic、SA-Co 训练来源；带 † 的 SAM3 是作者复现结果。这意味着“优于 SAM3”并非同一训练预算下只改一个模块的实验。

| 配置 / Table 1 | A-150 mIoU | A-847 mIoU | PC-59 mIoU | PC-459 mIoU |
| --- | ---: | ---: | ---: | ---: |
| SAM3 † | 37.8 | 14.0 | 58.3 | 18.3 |
| EOVSAM | 39.0 | 16.6 | 60.9 | 20.4 |

Table 4 中移除 SAM3 预训练权重后 A-150 为 **35.2**，移除注意力聚合为 **22.6**，完整配置为 **39.0 mIoU**；支持预训练初始化与聚合设计对该系统重要。Table 3 的速度需连同分辨率与词表规模解释，不能把“最高338倍”当成所有数据集与硬件通用加速。

## 局限

【分析推断】掩码生成虽不逐类别解码，但最终与 K 个文本类别比较仍依赖词表大小，不是整体复杂度与 K 完全无关。新 backbone、SAM3 初始化和额外监督共同影响结果，不能把全部增益解释为单个注意力模块。预印本与未来正式版本也可能变化。

## 横向理解

这是明确基于 SAM3 的后续适配，关系可由 Approach / Fig.2 直接支持。与 CorrCLIPv2 比较时，应先区分是否训练、外部数据、掩码生成方式与 backbone；本站暂不建立统一排名。

## 开源情况

【官方文档说明】仓库提供 `train_net.py`、训练配置、semantic/panoptic 评测配置、模型下载入口及 `SAM3OVS/` 基线。外部 RADIO、SAM3 等组成部分有各自许可，公开实现不意味着所有依赖采用同一许可。未独立验证权重下载与代码运行。

## 证据

| 主张 | 原始材料定位 |
| --- | --- |
| 单次前向架构 | [v1 Approach / Fig.2](https://arxiv.org/html/2608.02284v1#Sx3) |
| 注意力聚合与监督目标 | [Approach，式(3)–(5)](https://arxiv.org/html/2608.02284v1#Sx3) |
| 语义主结果及训练来源 | [Table 1](https://arxiv.org/html/2608.02284v1#Sx3.T1) |
| 速度与组件消融 | [Table 3–4](https://arxiv.org/html/2608.02284v1#Sx4) |
| 已公开的训练与评测入口 | [官方 README](https://github.com/hustvl/EOVSAM) |
