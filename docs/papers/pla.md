---
paper_id: pla
title: 'PLA: Language-Driven Open-Vocabulary 3D Scene Understanding'
short_name: PLA
authors: []
year: 2023
preprint_date: unknown
venue: CVPR
publication_status: published
primary_direction: 3d
modalities:
- point_cloud
- image
task_setting: open_vocabulary
task_types:
- semantic
- instance
techniques:
- semantic_alignment
datasets:
- ScanNet
paper_url: https://arxiv.org/abs/2211.16312
publication_url: https://openaccess.thecvf.com/content/CVPR2023/html/Ding_PLA_Language-Driven_Open-Vocabulary_3D_Scene_Understanding_CVPR_2023_paper.html
code_status: public
code_url: https://github.com/CVMI-Lab/PLA
code_details: 官方 main 分支包含实现、数据准备和训练推理文档；训练使用基类三维标注与图像生成的语言监督。
content_status: index
checked_on: '2026-11-09'
summary: 通过点云与语言关联构建三维开放词汇能力，作为蒸馏路线的对照。
sources:
- url: https://openaccess.thecvf.com/content/CVPR2023/html/Ding_PLA_Language-Driven_Open-Vocabulary_3D_Scene_Understanding_CVPR_2023_paper.html
  locator: 正式发表来源
- url: https://github.com/CVMI-Lab/PLA
  locator: 官方 README / 公开目录；未运行
figures:
- id: fig2
  asset: assets/figures/pla-fig2.png
  label: Figure 2
  page: 3
  version: arXiv 2211.16312v2
  source_url: https://arxiv.org/pdf/2211.16312v2
  clip_pdf_points:
  - 48
  - 45
  - 548
  - 176
  source_sha256: 28526dcffbbef224c56bdc90c3e8131ed2603ef51053c61789581fd6ba31c457
- id: fig3
  asset: assets/figures/pla-fig3.png
  label: Figure 3
  page: 4
  version: arXiv 2211.16312v2
  source_url: https://arxiv.org/pdf/2211.16312v2
  clip_pdf_points:
  - 48
  - 45
  - 548
  - 183
  source_sha256: 28526dcffbbef224c56bdc90c3e8131ed2603ef51053c61789581fd6ba31c457
methods:
- id: association
  track: pointcloud
  problems:
  - projection
  - multiview
  - alignment
  title: 场景／视图／实体三级点语言关联
  question: 图像描述如何对应到不同粒度点集？
  operation: 先生成视图描述，汇总为场景描述；由深度、位姿得到每幅图像可见点集；再用相邻视图点集和实体词集合的交、差构造局部实体关联，将描述嵌入作为点集监督。
  input: 多视图 RGB-D、图像描述
  output: 场景／视图／实体级点集—描述配对
  stage: 训练数据构造与对比学习
  supervision: 预训练描述模型；总体方法另使用基类三维标注
  origin: proposed
  origin_note: 本文提出图像桥接的分层点语言关联；投影本身是基础几何步骤。
  origin_refs: []
  evidence:
  - url: https://arxiv.org/pdf/2211.16312v2
    locator: §3.3–3.4，Figure 3
  figure: fig3
  figure_guide: 独立关联图：从图像描述向右看 scene、view、entity 三层点集配对。
  depicted: true
  route:
  - 区域文本描述
  - 多粒度点语言关联
  - 点集文本对
  - 对比学习
- id: classifier
  track: pointcloud
  problems:
  - alignment
  - unseen
  title: 文本类别分类器与基类／新类校准
  question: 未见类别怎样进入分类，如何减轻基类偏置？
  operation: 冻结文本编码器生成类别嵌入，用适配后的点特征与其计算相似度；训练二元头估计基类／新类概率，对两组语义分数分别加权后合并。
  input: 点特征、基类与新类类别文本
  output: 校准后的逐点类别分数
  stage: 训练与推理
  supervision: 基类语义标签；二元监督区分基类标注点与非基类点
  origin: modified
  origin_note: 文本分类器明确遵循 LSeg；二元校准按本文 §3.2 实现。
  origin_refs:
  - url: https://vladlen.info/papers/LSeg.pdf
    locator: PLA §3.2 “Following LSeg”
  evidence:
  - url: https://arxiv.org/pdf/2211.16312v2
    locator: §3.2，Figure 2
  figure: fig2
  figure_guide: 看右上 Language 模块的类别嵌入，与下方 Binary Head 对分类分数的校准路径。
  depicted: true
  route:
  - 类别文本
  - 文本分类与校准
  - 逐点类别分数
  - 文本相似度分类
module_checked_on: '2026-11-09'
---
# PLA

## 当前整理状态

已按研究关注点核查下列方法模块与配图；尚未完成全文样例笔记，不据此生成实验排名。

## 收录理由

通过点云与语言关联构建三维开放词汇能力，作为蒸馏路线的对照。

## 开源情况

【官方文档说明】官方 main 分支包含实现；有数据准备、训练推理及模型文档。具体监督设置待精读。 本轮没有安装或运行代码，没有独立验证权重下载。
