---
paper_id: troyvis
title: Towards Real-Time Open-Vocabulary Video Instance Segmentation
short_name: TROY-VIS
authors: []
year: 2025
preprint_date: '2024-12-05'
venue: WACV
publication_status: published
primary_direction: video
modalities:
- video
task_setting: open_vocabulary
task_types:
- video_instance
techniques:
- temporal
- efficient_inference
datasets:
- LV-VIS
- BURST
paper_url: https://arxiv.org/abs/2412.04434
publication_url: https://openaccess.thecvf.com/content/WACV2025/papers/Yan_Towards_Real-Time_Open-Vocabulary_Video_Instance_Segmentation_WACV_2025_paper.pdf
code_status: public
code_url: https://github.com/google-research/troyvis
code_details: 提供实际实现、训练测试文档与模型列表入口。
content_status: index
checked_on: '2026-11-09'
summary: 通过解耦特征增强、文本缓存与时序插值平衡视频分割精度和速度。
sources:
- url: https://openaccess.thecvf.com/content/WACV2025/papers/Yan_Towards_Real-Time_Open-Vocabulary_Video_Instance_Segmentation_WACV_2025_paper.pdf
  locator: 正式发表来源
- url: https://github.com/google-research/troyvis
  locator: 官方 README / 公开目录；未运行
figures:
- id: fig2
  asset: assets/figures/troyvis-fig2.png
  label: Figure 2
  page: 4
  version: arXiv 2412.04434v1
  source_url: https://arxiv.org/pdf/2412.04434v1
  clip_pdf_points:
  - 48
  - 45
  - 548
  - 320
  source_sha256: 9c5f669968a27ea21c7b4753fe11d39b15c7e5ffd25dce9bcf89e21dc044e3d4
- id: fig3
  asset: assets/figures/troyvis-fig3.png
  label: Figure 3
  page: 5
  version: arXiv 2412.04434v1
  source_url: https://arxiv.org/pdf/2412.04434v1
  clip_pdf_points:
  - 48
  - 45
  - 289
  - 214
  source_sha256: 9c5f669968a27ea21c7b4753fe11d39b15c7e5ffd25dce9bcf89e21dc044e3d4
methods:
- id: textmemory
  track: vocabulary
  problems:
  - alignment
  - efficiency
  title: 区域文本匹配与类别嵌入缓存
  question: 词汇量增加时如何避免重复编码类别文本？
  operation: 沿用 GLEE 的视觉语言匹配框架，以文本类别嵌入替代固定分类器；将类别名称→文本嵌入存入字典，直接读出已缓存类别，新类别才执行文本编码；另将跨模态注意力与多尺度注意力解耦以降低交互代价。
  input: 类别名称、缓存字典、多尺度视觉特征
  output: 语言条件视觉特征与类别嵌入
  stage: 推理；编码器冻结时也适用训练
  supervision: 大规模图像预训练及图像／视频联合微调
  origin: modified
  origin_note: 在 GLEE 框架上修改；Flash Embedding Memory 与解耦增强器由本文设计。
  origin_refs:
  - url: https://arxiv.org/abs/2312.09158
    locator: TROY-VIS §3 原始框架 GLEE
  evidence:
  - url: https://arxiv.org/pdf/2412.04434v1
    locator: §3、§3.1–3.2，Figure 2
  figure: fig2
  figure_guide: 独立图画出了跨模态／尺度注意力解耦；类别字典缓存未在图中画出，按 §3.2 文字理解。
  depicted: false
  route:
  - 类别文本
  - 跨模态交互与缓存
  - 类别与视觉嵌入
  - 文本相似度分类
- id: kernel
  track: vocabulary
  problems:
  - temporal
  - efficiency
  title: 跨帧传播实例核
  question: 如何保持实例语义同时减少逐帧解码？
  operation: 只在稀疏关键帧运行实例解码器得到准确实例核；非关键帧用相邻关键帧线性插值或最近邻复制得到代理核，与当前像素特征卷积生成掩码；因果最近邻只用过去关键帧。
  input: 关键帧实例核、每帧像素特征
  output: 跨帧实例掩码
  stage: 推理
  supervision: 依赖已训练网络；插值自身无需训练
  origin: proposed
  origin_note: 本文 kernel interpolation；双向插值与因果版本分别记录，不混称在线。
  origin_refs: []
  evidence:
  - url: https://arxiv.org/pdf/2412.04434v1
    locator: §3.3，Figure 3
  figure: fig3
  figure_guide: 独立核插值图：实线圈为准确核，虚线圈为代理核；三列区分 linear、NN、causal NN。
  depicted: true
  route:
  - 视频实例语义
  - 实例核时序传播
  - 视频实体记忆
  - 跨帧语义保持
module_checked_on: '2026-11-09'
results:
- id: table2
  label: Table 2
  asset: assets/results/troyvis-table2.png
  title: 开放词汇视频实例分割主结果
  setting: BURST 的 ALL／Common／Uncommon 与 LV-VIS 的整体／基类／新类评估；原表同时列 FPS。
  metrics: HOTA／track mAP ↑；AP／APb／APn ↑；FPS ↑
  reading: 看 TROY-VIS 在 LV-VIS 的 APn 与 FPS，以及 BURST 的 Uncommon 列；时序关联质量与分割精度分别看。
  page: 8
  version: arXiv 2412.04434v1
  source_url: https://arxiv.org/pdf/2412.04434v1
  source_sha256: 9c5f669968a27ea21c7b4753fe11d39b15c7e5ffd25dce9bcf89e21dc044e3d4
  clip_pdf_points:
  - 47
  - 69
  - 548
  - 263
- id: table1
  label: Table 1
  asset: assets/results/troyvis-table1.png
  title: 文本缓存与各组件延迟
  setting: A100、480p 输入、LV-VIS；比较 GLEE-Lite、增加 FEM 的版本及 TROY-VIS。
  metrics: 总延迟与各组件延迟 ms ↓
  reading: 看 Text Encoder 行的缓存收益及 Total 行；该表硬件不同于其他论文的速度表，不作跨论文 FPS 排名。
  page: 7
  version: arXiv 2412.04434v1
  source_url: https://arxiv.org/pdf/2412.04434v1
  source_sha256: 9c5f669968a27ea21c7b4753fe11d39b15c7e5ffd25dce9bcf89e21dc044e3d4
  clip_pdf_points:
  - 306
  - 155
  - 548
  - 290
---
# TROY-VIS

## 当前整理状态

已按研究关注点核查下列方法模块与配图；尚未完成全文样例笔记，不据此生成实验排名。

## 收录理由

通过解耦特征增强、文本缓存与时序插值平衡视频分割精度和速度。

## 开源情况

【官方文档说明】提供实际实现、训练测试文档与模型列表入口。 本轮没有安装或运行代码，没有独立验证权重下载。
