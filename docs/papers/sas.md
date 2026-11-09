---
paper_id: sas
title: 'SAS: Segment Any 3D Scene with Integrated 2D Priors'
short_name: SAS
authors:
- Zhuoyuan Li
- Jiahao Lu
- Jiacheng Deng
- Hanzhi Chang
- Lifan Wu
- Yanzhe Liang
- Tianzhu Zhang
year: 2025
preprint_date: '2025-03-11'
venue: ICCV
publication_status: published
primary_direction: 3d
modalities:
- point_cloud
- image
task_setting: open_vocabulary
task_types:
- semantic
techniques:
- semantic_alignment
- feature_distillation
- region_aggregation
- reliability
- temporal
- fusion
datasets:
- ScanNet
- Matterport3D
- nuScenes
paper_url: https://arxiv.org/abs/2503.08512
publication_url: https://openaccess.thecvf.com/content/ICCV2025/html/Li_SAS_Segment_Any_3D_Scene_with_Integrated_2D_Priors_ICCV_2025_paper.html
code_status: public
code_url: https://github.com/peoplelu/SAS
code_details: 公开能力构建、特征提取融合与分阶段训练实现；提供预处理特征入口，依赖多个外部教师模型。
content_status: detailed_sample
checked_on: '2026-11-09'
summary: 对齐多个二维教师，估计类别能力并融合，再以超点与自蒸馏训练三维模型。
sources:
- url: https://openaccess.thecvf.com/content/ICCV2025/html/Li_SAS_Segment_Any_3D_Scene_with_Integrated_2D_Priors_ICCV_2025_paper.html
  locator: 正式发表来源
- url: https://arxiv.org/html/2503.08512v1
  locator: v1 §3 / Table 1、3
- url: https://github.com/peoplelu/SAS
  locator: 官方 README / 公开目录；未运行
figures:
- id: fig2
  asset: assets/figures/sas-fig2.png
  label: Figure 2
  page: 3
  version: arXiv 2503.08512v1
  source_url: https://arxiv.org/pdf/2503.08512v1
  clip_pdf_points:
  - 56
  - 45
  - 556
  - 351
  source_sha256: 9f50e30794266863762c6fc79f2b8a440bf0a7a6622b107dddb70ce5b0f6e457
- id: fig3
  asset: assets/figures/sas-fig3.png
  label: Figure 3
  page: 4
  version: arXiv 2503.08512v1
  source_url: https://arxiv.org/pdf/2503.08512v1
  clip_pdf_points:
  - 56
  - 45
  - 298
  - 221
  source_sha256: 9f50e30794266863762c6fc79f2b8a440bf0a7a6622b107dddb70ce5b0f6e457
- id: fig4
  asset: assets/figures/sas-fig4.png
  label: Figure 4
  page: 5
  version: arXiv 2503.08512v1
  source_url: https://arxiv.org/pdf/2503.08512v1
  clip_pdf_points:
  - 56
  - 45
  - 556
  - 235
  source_sha256: 9f50e30794266863762c6fc79f2b8a440bf0a7a6622b107dddb70ce5b0f6e457
methods:
- id: textbridge
  track: pointcloud
  problems:
  - alignment
  - reliability
  title: 用文本桥统一异构教师特征
  question: 不同二维教师的嵌入空间如何统一？
  operation: LSeg 路径保留语言对齐特征；SEEM 生成掩码及名词标签，TAP 生成区域描述；将描述中的对象名词替换为 SEEM 标签，再用共享 CLIP 文本编码器编码并赋回掩码像素，统一嵌入空间。
  input: LSeg 特征、SEEM 掩码与 TAP 描述
  output: 统一语言空间的二维特征
  stage: 教师目标构建
  supervision: 预训练 LSeg、SEEM、TAP、CLIP
  origin: proposed
  origin_note: 本文提出 Model Alignment via Text；组件模型本身沿用已有实现。
  origin_refs: []
  evidence:
  - url: https://arxiv.org/pdf/2503.08512v1
    locator: §3.1，Figure 3
  figure: fig3
  figure_guide: 独立模块图：重点看下方掩码→描述→共享文本编码器→像素赋值路径。
  depicted: true
  route:
  - 异构二维教师
  - 文本桥接对齐
  - 二维密集特征
  - 二维到三维传递
- id: projection
  track: pointcloud
  problems:
  - projection
  - multiview
  title: 沿用 OpenScene 的像素点映射与多视角融合
  question: 异构教师对齐后怎样从多视图传到相同的三维点？
  operation: 文本桥接先得到两种二维密集特征；依照 OpenScene 计算像素—点对应与多视角融合，分别生成 LSeg 和 SEEM 两路逐点特征，再进入本文的能力加权融合。
  input: 语言空间对齐的二维特征、点云、RGB-D 相机信息
  output: 相同三维点上的两路教师特征
  stage: 教师目标构建
  supervision: 预训练二维教师；标定与深度信息
  origin: reused
  origin_note: SAS §3.1 明确说明 follow OpenScene，属于沿用步骤，不是本文核心创新。
  origin_refs:
  - url: https://arxiv.org/abs/2211.15654
    locator: OpenScene §3.1；SAS 引用 [53]
  evidence:
  - url: https://arxiv.org/pdf/2503.08512v1#page=4
    locator: §3.1 末段，Figure 2
  figure: fig2
  figure_guide: 主图上方从二维特征到 Point Features；相机对应与遮挡计算未单独展开，具体映射来源为 OpenScene。
  depicted: true
  route:
  - 二维密集特征
  - 可见性与跨视角融合
  - 逐点特征
  - 二维到三维传递
- id: capability
  track: pointcloud
  problems:
  - reliability
  - multiview
  title: 合成图估计类别能力，再按能力融合
  question: 没有人工类别验证集时怎样选择教师？
  operation: 用 Stable Diffusion 生成类别图像，借生成注意力与 SAM 构造伪掩码，以 mIoU 估计每个教师的类别能力；将两路特征映射并多视角融合到点后，分别得到两种类别预测。对每个教师，平均它在这两个候选类别上的能力，再以温度
    softmax 得到融合权重。
  input: 合成类别图与伪掩码、已投影融合的两路逐点教师特征
  output: 类别能力表、加权融合逐点二维目标
  stage: 能力估计与训练目标构造
  supervision: 生成模型和预训练 SAM；伪标签不等于没有先验监督
  origin: proposed
  origin_note: 本文的 Annotation-free Model Capability Construction 及 capability-guided fusion。
  origin_refs: []
  evidence:
  - url: https://arxiv.org/pdf/2503.08512v1
    locator: §3.2–3.3，Figure 4
  figure: fig4
  figure_guide: 独立能力图从合成图、伪掩码、教师预测看向最右能力估计；融合操作本身在 §3.3 与总图。
  depicted: true
  route:
  - 异构二维教师
  - 可靠性加权与选择
  - 逐点特征
  - 二维到三维传递
- id: superpoint
  track: pointcloud
  problems:
  - distillation
  - regions
  title: 超点聚合与双尺度特征蒸馏
  question: 如何利用区域几何减轻逐点噪声？
  operation: 在非重叠超点内分别平均三维网络特征和融合后的二维目标；把二维超点均值赋回各成员点，同时计算逐点与超点级的 1−cos 损失，抑制超点内部语义波动。
  input: 融合二维目标、三维点及超点划分
  output: 点级与超点级语言对齐三维特征
  stage: 训练
  supervision: 二维教师目标和几何超点；无需人工三维语义标签
  origin: modified
  origin_note: 超点蒸馏明确类似 GGSD；本文将其用于多教师融合目标，并在后续增加独立的时序集成自蒸馏。
  origin_refs:
  - url: https://arxiv.org/abs/2407.13362
    locator: SAS §3.4 引用 [76] GGSD（ECCV 2024）：Open Vocabulary 3D Scene Understanding via Geometry Guided Self-Distillation
  evidence:
  - url: https://arxiv.org/pdf/2503.08512v1
    locator: §3.3–3.4，Figure 2
  figure: fig2
  figure_guide: 总图右侧 Superpoint 与 Distillation 连接；超点内部平均操作需结合公式阅读。
  depicted: true
  route:
  - 二维密集特征
  - 超点聚合与蒸馏
  - 逐点特征
  - 特征蒸馏
module_checked_on: '2026-11-09'
---
# SAS

## 资料范围与版本

阅读 arXiv:2503.08512 **v1（2025-03-11）** 正文及附录；正式来源为 ICCV 2025。以下数值对应 v1，不假定与会议最终版逐字一致。官方仓库仅做文档与目录核查，未运行。

## 任务

【原文事实】目标为开放词汇三维语义分割。离线准备使用多视角 RGB、相机参数、多个二维模型、扩散模型和 SAM；训练三维点网络，主实验报告纯三维模型推理结果。不要把离线多模型管线与部署时的纯三维推理成本混为一谈。

## 研究问题

一个二维教师对不同类别的识别能力并不相同，直接蒸馏会继承其错误。多个教师又可能处在不同嵌入空间，不能不经处理直接相加。SAS 分别处理“语义空间不一致”和“类别能力不一致”（§1、Fig.1–2）。

## 方法

1. **Model Alignment via Text（§3.1）。** 以 LSeg 与 SEEM 为例：SEEM 给区域和类别，TAP 补充描述，再用共享 CLIP 文本编码器编码描述并映回区域，使两教师可在共同空间内融合。文本桥接不是训练一个通用跨模型线性映射。
2. **Annotation-free Capability Construction（§3.2）。** 用扩散模型合成指定类别图像，以扩散注意力定位粗区域，再用 SAM 细化成参考掩码。比较教师掩码与参考掩码的 IoU，按类别形成能力表。参考本身是自动生成，**不是人工真值**。
3. **能力引导融合（§3.3，式(6)–(8)）。** 先由两教师特征得到点的候选类别，再从能力表取与候选类别有关的分数，温度归一化后加权特征。这里的“能力”不是直接读取每点预测 softmax 置信度。
4. **超点蒸馏（§3.4，式(10)）。** 聚合超点平均特征，组合点级与超点级余弦损失训练三维网络。超点语义一致性是方法假设，错误合并仍可能影响目标。
5. **Temporal Ensembling Self-Distillation（§3.4–3.5）。** 使用跨训练阶段的预测集成进行自蒸馏。此处 temporal 不能直接解释为“视频帧间记忆模块”。

```mermaid
flowchart LR
  A[多个二维教师] --> B[文本桥接对齐]
  C[扩散合成与SAM参考掩码] --> D[按类别估计教师能力]
  B --> E[能力加权点特征融合]
  D --> E
  E --> F[超点与点级蒸馏]
  F --> G[三维模型与集成自蒸馏]
```

## 实验 {#experiments}

【原文事实】§4.1 室内使用 LSeg+SEEM，室外使用 OpenSeg+SEEM。其 Table 1 报告 ScanNet v2 **61.9**、Matterport3D **48.6**、nuScenes **47.5 mIoU**。这些值属于所读 v1 的作者实验，不是本站复现结果。

更适合分析方法作用的是 Table 3 的 ScanNet 消融：

| 配置 | mIoU |
| --- | ---: |
| 直接相加融合二维特征 | 48.6 |
| 能力引导二维融合 | 55.5 |
| 点级蒸馏 | 56.7 |
| 超点蒸馏 | 59.2 |
| 超点蒸馏 + TESD | 61.9 |

该递进支持融合与蒸馏设计在该配置中有用，但不能把最终提升全部归给某一个模块。对比 OpenScene 时还需区分纯 3D 与 2D–3D ensemble、教师版本、词表和类别映射。

## 局限

【分析推断】合成图像上的类别能力未必与真实长尾场景一致；TAP 描述和自动参考掩码也会引入偏差。能力估计、特征准备和多模型环境增加离线成本。原文 §4.1 的类别数量表述需要结合附录与代码标签映射再核对，本站暂不据这一句建立跨论文协议组。

## 横向理解

与 OpenScene 相比，SAS 把“教师是否可靠”显式加入融合过程。与 GeoPurify 相比，前者主要增强语义来源，后者侧重语义特征进入三维后的几何一致性；两者作用位置不同，不能只按最终 mIoU 推断孰优。

## 开源情况

【官方文档说明】仓库包含 `MCC/`、`feat_fusion/`、`point_feat_extraction/`、`superpoint_extraction/`、模型与运行脚本，提供预处理特征入口。README 要求多个教师环境和外部检查点。本笔记没有确认这些流程端到端运行成功。

## 证据

| 主张 | 原始材料定位 |
| --- | --- |
| 文本桥接 | [v1 §3.1 / Fig.3](https://arxiv.org/html/2503.08512v1#S3.SS1) |
| 合成图像上的教师能力 | [§3.2 / Fig.4 / 式(3)–(5)](https://arxiv.org/html/2503.08512v1#S3.SS2) |
| 能力引导融合 | [§3.3 / 式(6)–(8)](https://arxiv.org/html/2503.08512v1#S3.SS3) |
| 主结果与消融 | [§4 / Table 1、3](https://arxiv.org/html/2503.08512v1#S4) |
| 代码公开范围 | [官方 README](https://github.com/peoplelu/SAS) |
