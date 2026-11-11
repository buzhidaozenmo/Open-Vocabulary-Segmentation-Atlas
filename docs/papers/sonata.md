---
paper_id: sonata
title: 'Sonata: Self-Supervised Learning of Reliable Point Representations'
short_name: Sonata
authors:
- Wu, Xiaoyang
- DeTone, Daniel
- Frost, Duncan
- Shen, Tianwei
- Xie, Chris
- Yang, Nan
- Engel, Jakob
- Newcombe, Richard
- Zhao, Hengshuang
- Straub, Julian
year: 2025
preprint_date: unknown
venue: CVPR
publication_status: published
primary_direction: 3d
modalities:
- point_cloud
task_setting: self_supervised_representation
task_types:
- representation
techniques:
- geometry
- feature_distillation
datasets:
- ScanNet
- ScanNet++
- S3DIS
paper_url: https://openaccess.thecvf.com/content/CVPR2025/papers/Wu_Sonata_Self-Supervised_Learning_of_Reliable_Point_Representations_CVPR_2025_paper.pdf
publication_url: https://openaccess.thecvf.com/content/CVPR2025/html/Wu_Sonata_Self-Supervised_Learning_of_Reliable_Point_Representations_CVPR_2025_paper.html
code_status: public
code_url: https://github.com/facebookresearch/sonata
code_details: 官方独立仓库提供预训练权重入口、推理及可视化；预训练流程在 Pointcept。代码 Apache-2.0，权重 CC-BY-NC-4.0；未运行。
content_status: index
checked_on: '2026-11-11'
module_checked_on: '2026-11-11'
summary: 以点自蒸馏学习三维表征，通过移除解码器、特征上投与扰动遮挡点减轻几何捷径；可作为冻结几何教师。
sources:
- url: https://openaccess.thecvf.com/content/CVPR2025/html/Wu_Sonata_Self-Supervised_Learning_of_Reliable_Point_Representations_CVPR_2025_paper.html
  locator: 出版方正式发表记录
- url: https://openaccess.thecvf.com/content/CVPR2025/papers/Wu_Sonata_Self-Supervised_Learning_of_Reliable_Point_Representations_CVPR_2025_paper.pdf
  locator: 按模块列出的原文章节、原图及结果表
- url: https://github.com/facebookresearch/sonata
  locator: 官方 README 与根目录；未独立运行
figures:
- id: fig5
  label: Figure 5
  asset: assets/figures/sonata-fig5.png
  page: 4
  version: CVPR 2025 出版方正式版
  source_url: https://openaccess.thecvf.com/content/CVPR2025/papers/Wu_Sonata_Self-Supervised_Learning_of_Reliable_Point_Representations_CVPR_2025_paper.pdf
  source_sha256: 3204e6ac4b724201964fc5fcd0c1223269a74bdd82138caaef04ec5dc412efa8
  clip_pdf_points:
  - 315
  - 60
  - 556
  - 325
methods:
- id: self-distillation
  track: pointcloud
  problems:
  - geometry
  title: 学习几何表征并抑制几何捷径
  question: 怎样让点云自监督表征超越浅层空间线索？
  operation: EMA 教师编码全局视图，学生编码局部和遮挡视图；按增强前空间距离建立点对应并自蒸馏。移除解码器，以池化映射上投并拼接多尺度特征，额外扰动被遮挡点并逐步提高遮挡难度。
  input: 增强点云及颜色；跨视图点对应
  output: 多尺度逐点三维表征
  stage: 自监督预训练；冻结特征供下游使用
  supervision: 点云自身的视图一致性，不用三维类别标注；下游探测另需标注
  origin: proposed
  origin_note: 本文框架中的具体设计；预训练骨干与基础算子不视为本文首创。
  evidence:
  - &id001
    locator: §3–4.2，Figure 5–6，Table 3
    url: https://openaccess.thecvf.com/content/CVPR2025/papers/Wu_Sonata_Self-Supervised_Learning_of_Reliable_Point_Representations_CVPR_2025_paper.pdf
  figure: fig5
  figure_guide: Figure 5 展示视图、师生和点对应路径；移除解码器、扰动与调度的微设计未在此图逐项画出，见 §4.2 与 Figure 6。
  depicted: true
  route:
  - 点云自身监督
  - 点自蒸馏
  - 三维表征
  - 下游表征评测
  geometry:
    families:
    - pretrained
    - coordinates
    signal: 点坐标、空间增强前对应及层级池化映射
    mechanism: 用空间对应确定蒸馏对象，同时扰乱过于容易利用的坐标线索，使网络从输入特征和上下文学习表征。
    changes: 点特征；多尺度空间上下文
    stage: 预训练；下游冻结或微调
    semantic_role: Sonata 无原生文本分类头；几何表征可包含语义结构，但类别接口来自另行训练的下游头。
    route:
    - 三维预训练表征
    - 点自蒸馏
    - 多尺度点表征
    - 预训练／下游
    evidence:
    - *id001
results:
- id: table3
  label: Table 3
  asset: assets/results/sonata-table3.png
  page: 7
  version: CVPR 2025 出版方正式版
  source_url: https://openaccess.thecvf.com/content/CVPR2025/papers/Wu_Sonata_Self-Supervised_Learning_of_Reliable_Point_Representations_CVPR_2025_paper.pdf
  source_sha256: 3204e6ac4b724201964fc5fcd0c1223269a74bdd82138caaef04ec5dc412efa8
  clip_pdf_points:
  - 58
  - 70
  - 283
  - 210
  title: 几何与图像自监督特征的互补性
  setting: ScanNet / ScanNet200 验证集；分别比较线性探测 lin. 与解码器探测 dec.。探测头使用下游标注。
  metrics: mIoU、mAcc、allAcc ↑
  reading: 先比较相同 lin. 设置，再看加入 DINOv2 / DINOv2.5 的行；这是有监督探测，不是开放词汇零样本分割。
---

# Sonata

【原文事实】以点自蒸馏学习三维表征，通过移除解码器、特征上投与扰动遮挡点减轻几何捷径；可作为冻结几何教师。

## 资料范围

正式发表于 CVPR 2025，本页图表读取 CVPR 2025 出版方正式版。按研究关注点整理相关模块，未独立复现实验。

## 任务与能力范围

Sonata 无原生文本分类头；几何表征可包含语义结构，但类别接口来自另行训练的下游头。

## 关注的几何操作

**学习几何表征并抑制几何捷径**：EMA 教师编码全局视图，学生编码局部和遮挡视图；按增强前空间距离建立点对应并自蒸馏。移除解码器，以池化映射上投并拼接多尺度特征，额外扰动被遮挡点并逐步提高遮挡难度。

依据：§3–4.2，Figure 5–6，Table 3。

## 代码开放情况

【官方文档说明】官方独立仓库提供预训练权重入口、推理及可视化；预训练流程在 Pointcept。代码 Apache-2.0，权重 CC-BY-NC-4.0；未运行。

## 实验阅读

Table 3：几何与图像自监督特征的互补性。ScanNet / ScanNet200 验证集；分别比较线性探测 lin. 与解码器探测 dec.。探测头使用下游标注。 先比较相同 lin. 设置，再看加入 DINOv2 / DINOv2.5 的行；这是有监督探测，不是开放词汇零样本分割。
