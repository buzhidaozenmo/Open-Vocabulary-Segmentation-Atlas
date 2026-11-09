---
paper_id: cliper
title: 'CLIPer: Hierarchically Improving Spatial Representation of CLIP for Open-Vocabulary Semantic Segmentation'
short_name: CLIPer
authors:
- Lin Sun
- Jiale Cao
- Jin Xie
- Xiaoheng Jiang
- Yanwei Pang
year: 2025
preprint_date: unknown
venue: ICCV
publication_status: published
primary_direction: 2d
modalities:
- image
task_setting: open_vocabulary
task_types:
- semantic
techniques:
- semantic_alignment
- fusion
datasets:
- PASCAL
- COCO
- Cityscapes
- ADE20K
paper_url: https://openaccess.thecvf.com/content/ICCV2025/papers/Sun_CLIPer_Hierarchically_Improving_Spatial_Representation_of_CLIP_for_Open-Vocabulary_Semantic_ICCV_2025_paper.pdf
publication_url: https://openaccess.thecvf.com/content/ICCV2025/html/Sun_CLIPer_Hierarchically_Improving_Spatial_Representation_of_CLIP_for_Open-Vocabulary_Semantic_ICCV_2025_paper.html
code_status: public
code_url: https://github.com/linsun449/cliper.code
code_details: 官方仓库含 modified_clip、diffusion_model、推理脚本及演示；文档说明运行时下载依赖模型，未独立验证。
content_status: index
checked_on: '2026-11-09'
module_checked_on: '2026-11-09'
summary: 融合 CLIP 早层特征，并用扩散模型注意力补足开放词汇预测的局部细节。
sources:
- url: https://openaccess.thecvf.com/content/ICCV2025/html/Sun_CLIPer_Hierarchically_Improving_Spatial_Representation_of_CLIP_for_Open-Vocabulary_Semantic_ICCV_2025_paper.html
  locator: 正式发表：出版方页面／DOI；期刊状态另由官方仓库文档确认
- url: https://openaccess.thecvf.com/content/ICCV2025/papers/Sun_CLIPer_Hierarchically_Improving_Spatial_Representation_of_CLIP_for_Open-Vocabulary_Semantic_ICCV_2025_paper.pdf
  locator: 本次所读原文版本的 §3–5／III–V、方法图及主要结果表
- url: https://github.com/linsun449/cliper.code
  locator: 官方仓库实际目录与文档／项目页；未运行
figures:
- id: fig4
  label: Figure 4
  asset: assets/figures/cliper-fig4.png
  page: 4
  version: ICCV 2025 出版方正式版
  source_url: https://openaccess.thecvf.com/content/ICCV2025/papers/Sun_CLIPer_Hierarchically_Improving_Spatial_Representation_of_CLIP_for_Open-Vocabulary_Semantic_ICCV_2025_paper.pdf
  clip_pdf_points:
  - 55
  - 50
  - 557
  - 305
  source_sha256: 814ca2e0969a8031a44d821746a6afcdd87ff69bd8c62583e96e31a71567abc2
methods:
- id: earlyfusion
  track: vocabulary
  problems:
  - alignment
  - regions
  title: 早层注意力与特征的末层对齐融合
  question: 怎样利用早层空间结构，同时保持 CLIP 的文本匹配能力？
  operation: 收集末层之前的各层嵌入及注意力图，平均注意力并替换末层原注意力；不同层嵌入分别经过该末层的语言对齐处理，再与类别文本算相似度，平均得到粗分割图。
  input: CLIP 多层嵌入与注意力、类别文本
  output: 空间更连贯的粗语义图
  stage: 推理
  supervision: 预训练 CLIP；免任务训练，不引入像素标签
  origin: proposed
  origin_note: 本文 early-layer fusion；末层移除 FFN 和残差的处理按原文沿用相关先行方法。
  origin_refs: []
  evidence:
  - url: https://openaccess.thecvf.com/content/ICCV2025/papers/Sun_CLIPer_Hierarchically_Improving_Spatial_Representation_of_CLIP_for_Open-Vocabulary_Semantic_ICCV_2025_paper.pdf
    locator: §3.3，Eq.3–5
  figure: fig4
  figure_guide: 主架构上部 Early-layer Fusion：多层特征和注意力→末层对齐→Similarity & Fusion。
  depicted: true
  route:
  - 二维密集特征
  - 多层特征对齐融合
  - 二维密集特征
  - 文本相似度分类
- id: compensation
  track: vocabulary
  problems:
  - alignment
  - regions
  title: 扩散模型注意力细化语义图
  question: CLIP 粗类别图的细节怎样恢复？
  operation: 以图像和空文本提示获取 Stable Diffusion 高分辨率多头自注意力；跨头做矩阵连乘得到融合空间关系，再左乘上采样后的 CLIP 粗语义图，最后恢复输入分辨率。
  input: CLIP 粗类别图、扩散模型空间注意力
  output: 像素级细化语义图
  stage: 推理
  supervision: 预训练 CLIP 和 Stable Diffusion；无任务微调
  origin: proposed
  origin_note: 本文 fine-grained compensation 与 self-fused self-attention；不生成新增类别标签。
  origin_refs: []
  evidence:
  - url: https://openaccess.thecvf.com/content/ICCV2025/papers/Sun_CLIPer_Hierarchically_Improving_Spatial_Representation_of_CLIP_for_Open-Vocabulary_Semantic_ICCV_2025_paper.pdf
    locator: §3.3，Eq.6–7
  figure: fig4
  figure_guide: 主图下部 Fine-grained Compensation：SD attention→SFSA→与粗图的细化连接。
  depicted: true
  route:
  - 扩散模型空间先验
  - 空间注意力细化
  - 像素语义图
  - 语义细化
results:
- id: table1
  label: Table 1
  asset: assets/results/cliper-table1.png
  page: 6
  version: ICCV 2025 出版方正式版
  source_url: https://openaccess.thecvf.com/content/ICCV2025/papers/Sun_CLIPer_Hierarchically_Improving_Spatial_Representation_of_CLIP_for_Open-Vocabulary_Semantic_ICCV_2025_paper.pdf
  clip_pdf_points:
  - 55
  - 69
  - 558
  - 368
  source_sha256: 814ca2e0969a8031a44d821746a6afcdd87ff69bd8c62583e96e31a71567abc2
  title: 八个二维语义分割基准
  setting: 原表区分训练式与免训练方法、ViT-B／L，以及 ‡ 滑窗推理；包含／不包含背景的任务分别列出。
  metrics: mIoU ↑；Avg. ↑
  reading: 优先比较相同骨干与滑窗设置；扩散模型用于空间细化，不等于新增类别训练标签。
---
# CLIPer

## 资料范围与状态

核查版本：ICCV 2025 出版方正式版；正式发表来源另见出版方链接。已完成与研究关注点有关的方法、配图和主结果表定向整理，尚未完成全文样例笔记。图中的方法关系以原文为准，未独立运行实现。

## 关注的问题

【原文事实】融合 CLIP 早层特征，并用扩散模型注意力补足开放词汇预测的局部细节。

## 实验阅读

原表区分训练式与免训练方法、ViT-B／L，以及 ‡ 滑窗推理；包含／不包含背景的任务分别列出。 优先比较相同骨干与滑窗设置；扩散模型用于空间细化，不等于新增类别训练标签。 数值保留在原始结果表中；它们是论文报告值，不是本库复现值。

## 开源情况

【官方文档说明／项目页核查】官方仓库含 modified_clip、diffusion_model、推理脚本及演示；文档说明运行时下载依赖模型，未独立验证。 本轮没有安装依赖、执行训练或验证复现结果。
