---
paper_id: entitysam
title: 'EntitySAM: Segment Everything in Video'
short_name: EntitySAM
authors: []
year: 2025
preprint_date: unknown
venue: CVPR
publication_status: published
primary_direction: video
modalities:
- video
task_setting: related_class_agnostic
task_types:
- video_entity
techniques:
- temporal
- region_aggregation
datasets:
- VIPSeg
- COCO
paper_url: https://openaccess.thecvf.com/content/CVPR2025/papers/Ye_EntitySAM_Segment_Everything_in_Video_CVPR_2025_paper.pdf
publication_url: https://openaccess.thecvf.com/content/CVPR2025/papers/Ye_EntitySAM_Segment_Everything_in_Video_CVPR_2025_paper.pdf
code_status: public
code_url: https://github.com/ymq2017/entitysam
code_details: 实体训练、评测代码与检查点已公开；论文的类别命名依赖外部 GPT-4o，不属于开源实体模型本体。
content_status: index
checked_on: '2026-11-09'
summary: 以SAM2扩展自动发现和跟踪视频实体；作为类别无关相关任务参考。
sources:
- url: https://openaccess.thecvf.com/content/CVPR2025/papers/Ye_EntitySAM_Segment_Everything_in_Video_CVPR_2025_paper.pdf
  locator: 正式发表来源
- url: https://github.com/ymq2017/entitysam
  locator: 官方 README / 公开目录；未运行
figures:
- id: fig2
  asset: assets/figures/entitysam-fig2.png
  label: Figure 2
  page: 4
  version: CVPR 2025 出版方 PDF
  source_url: https://openaccess.thecvf.com/content/CVPR2025/papers/Ye_EntitySAM_Segment_Everything_in_Video_CVPR_2025_paper.pdf
  clip_pdf_points:
  - 56
  - 45
  - 556
  - 192
  source_sha256: 717622aa16da9fc5f6feb65ac93f350c643ed43a3dec9ef926cd29cf0c7efa7b
methods:
- id: vlm
  track: vocabulary
  problems:
  - alignment
  - temporal
  title: 实体跟踪后用裁切与候选文本分类
  question: 类别无关视频掩码怎样获得类别名称？
  operation: 先自动产生并跟踪实体 masklet；为每个实体选择置信度最高的一帧，用掩码引导裁切，连同候选类别名称提示交给 GPT-4o 分类。类别命名是外部视觉语言模型的推理步骤。
  input: 视频实体掩码、最高置信帧、候选类别文本
  output: 实体类别与带身份掩码
  stage: 推理
  supervision: 实体模型使用类别无关掩码监督；分类依赖外部 GPT-4o
  origin: modified
  origin_note: 沿用 SAM2 记忆构建实体模型，接入已有 GPT-4o；开源实体模型不等于分类 VLM 权重开源。
  origin_refs:
  - url: https://arxiv.org/abs/2408.00714
    locator: EntitySAM §3.2 SAM2 背景与记忆模块
  evidence:
  - url: https://openaccess.thecvf.com/content/CVPR2025/papers/Ye_EntitySAM_Segment_Everything_in_Video_CVPR_2025_paper.pdf
    locator: §3.3.2–3.3.4，Figure 2
  figure: fig2
  figure_guide: 总图画出了自动实体生成和记忆；最高置信帧裁切→GPT-4o 分类没有画出，见 §3.3.4。
  depicted: false
  route:
  - 外部视觉语言模型
  - 掩码裁切与文本分类
  - 视频实例类别
  - 外部模型分类
module_checked_on: '2026-11-09'
results:
- id: table2
  label: Table 2
  asset: assets/results/entitysam-table2.png
  title: 视频实体与全景分割主结果
  setting: COCO → VIPSeg／VIPEntitySeg；EntitySAM 不使用类别标注训练实体模型；原表区分类别无关训练与不同骨干。
  metrics: 实体：VEQ、STQ；全景：VPQ；均为 ↑
  reading: 左侧看实体分割，右侧看带类别的全景结果；类别命名使用外部 VLM，不等于实体模型本身具备文本分类器。
  page: 7
  version: CVPR 2025 出版方 PDF
  source_url: https://openaccess.thecvf.com/content/CVPR2025/papers/Ye_EntitySAM_Segment_Everything_in_Video_CVPR_2025_paper.pdf
  source_sha256: 717622aa16da9fc5f6feb65ac93f350c643ed43a3dec9ef926cd29cf0c7efa7b
  clip_pdf_points:
  - 55
  - 54
  - 557
  - 276
- id: table3
  label: Table 3
  asset: assets/results/entitysam-table3.png
  title: 开放词汇视频语义分割
  setting: COCO → VSPW；按 ResNet-50／ConvNeXt-L 等骨干分组，与各组 EntitySAM 比较。
  metrics: mIoU ↑；mVC8／mVC16 ↑
  reading: mIoU 看逐像素语义准确率；mVC8／16 看不同时间窗口的一致性。
  page: 7
  version: CVPR 2025 出版方 PDF
  source_url: https://openaccess.thecvf.com/content/CVPR2025/papers/Ye_EntitySAM_Segment_Everything_in_Video_CVPR_2025_paper.pdf
  source_sha256: 717622aa16da9fc5f6feb65ac93f350c643ed43a3dec9ef926cd29cf0c7efa7b
  clip_pdf_points:
  - 55
  - 278
  - 298
  - 409
---
# EntitySAM

## 当前整理状态

已按研究关注点核查下列方法模块与配图；尚未完成全文样例笔记，不据此生成实验排名。

## 收录理由

以SAM2扩展自动发现和跟踪视频实体；作为类别无关相关任务参考。

## 开源情况

【官方文档说明】训练代码、评测代码和检查点已发布；核心任务不是文本类别驱动的OVSS。 本轮没有安装或运行代码，没有独立验证权重下载。


> 相关任务参考：类别无关实体分割不等于文本类别驱动的开放词汇语义分割。
