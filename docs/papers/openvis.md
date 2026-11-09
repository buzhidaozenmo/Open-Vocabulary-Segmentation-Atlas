---
paper_id: openvis
title: 'OpenVIS: Open-vocabulary Video Instance Segmentation'
short_name: OpenVIS / InstFormer
authors:
- Guo, Pinxue
- Huang, Hao
- He, Peiyang
- Liu, Xuefeng
- Xiao, Tianjun
- Zhang, Wenqiang
year: 2025
preprint_date: unknown
venue: AAAI
publication_status: published
primary_direction: video
modalities:
- video
task_setting: open_vocabulary
task_types:
- video_instance
techniques:
- semantic_alignment
datasets:
- BURST
paper_url: https://raw.githubusercontent.com/PinxueGuo/OpenVIS/main/OpenVIS_AAAI-25_paper.pdf
publication_url: https://ojs.aaai.org/index.php/AAAI/article/view/32338
code_status: public
code_url: https://github.com/PinxueGuo/OpenVIS
code_details: 已核对官方实现目录：OpenVIS_AAAI-25_paper.pdf、adapter-transformers、code_guide.md、configs、datasets、demo_video。未独立运行或验证外部权重下载。
content_status: index
checked_on: '2026-11-09'
module_checked_on: '2026-11-09'
summary: 掩码提议分支生成类别无关候选；InstCLIP 根据实例引导掩码提取区域表示，用轻量适配保留文本对应，再通过实例 token 的 rollout 关联实现跨帧身份匹配。
sources:
- url: https://ojs.aaai.org/index.php/AAAI/article/view/32338
  locator: 正式发表来源：出版页面／作者项目的会议说明
- url: https://raw.githubusercontent.com/PinxueGuo/OpenVIS/main/OpenVIS_AAAI-25_paper.pdf
  locator: 方法部分；Figure 3（PDF 第 5 页）；实验 Table 1（PDF 第 6 页）
- url: https://github.com/PinxueGuo/OpenVIS
  locator: 官方 README、目录与开放范围；未独立运行
figures:
- id: fig3
  label: Figure 3
  asset: assets/figures/openvis-fig3.png
  page: 5
  version: 作者公开 PDF（SHA256 固定版本）
  source_url: https://raw.githubusercontent.com/PinxueGuo/OpenVIS/main/OpenVIS_AAAI-25_paper.pdf
  source_sha256: bc5808a6d1891a48d78a195b12d19d7519cd55da33b9c114cb40fd3d391088d4
  clip_pdf_points:
  - 50
  - 45
  - 297
  - 200.381
methods:
- id: semantic-operation
  track: vocabulary
  problems:
  - alignment
  - temporal
  - regions
  title: 掩码引导实例语言对齐
  question: 视频实例怎样获得保留开放词汇能力的特征？
  operation: 掩码提议分支生成类别无关候选；InstCLIP 根据实例引导掩码提取区域表示，用轻量适配保留文本对应，再通过实例 token 的 rollout 关联实现跨帧身份匹配。
  input: 视频帧、候选掩码、类别文本与历史实例 token
  output: 跨帧实例掩码和开放词汇类别
  stage: 轻量适配与跟踪训练；视频推理
  supervision: 有限类别视频／图像训练数据和预训练 CLIP
  origin: proposed
  origin_note: 本文设计的掩码引导实例语言对齐流程；所用预训练模型、通用投影及基础算子沿用已有方法，不计作本文新提出。
  evidence:
  - url: https://raw.githubusercontent.com/PinxueGuo/OpenVIS/main/OpenVIS_AAAI-25_paper.pdf
    locator: 方法部分；Figure 3（PDF 第 5 页）；实验 Table 1（PDF 第 6 页）
  figure: fig3
  figure_guide: 图中重点看 InstCLIP 的 instance guidance mask；完整 rollout tracker 见 Figure 2。
  depicted: true
  route:
  - 预训练视觉语言特征
  - 掩码引导实例语言对齐
  - 视频实例语义
  - 开放词汇分割
  result_tables:
  - table1
results:
- id: table1
  label: Table 1
  asset: assets/results/openvis-table1.png
  page: 6
  version: 作者公开 PDF（SHA256 固定版本）
  source_url: https://raw.githubusercontent.com/PinxueGuo/OpenVIS/main/OpenVIS_AAAI-25_paper.pdf
  source_sha256: bc5808a6d1891a48d78a195b12d19d7519cd55da33b9c114cb40fd3d391088d4
  clip_pdf_points:
  - 50
  - 45
  - 562
  - 245
  title: OpenVIS / InstFormer：主要实验结果
  setting: BURST 与 LVVIS 的 OpenVIS，原表同时比较零样本性质。
  metrics: AP ↑
  reading: LVVIS／BURST 与已见 YouTube-VIS 全监督结果分开阅读。
---

# OpenVIS / InstFormer

本页按研究问题提取相关操作；模块图、输入输出、证据和主要结果表在上方展开查看。

## 研究问题

视频实例怎样获得保留开放词汇能力的特征？

## 相关操作

掩码提议分支生成类别无关候选；InstCLIP 根据实例引导掩码提取区域表示，用轻量适配保留文本对应，再通过实例 token 的 rollout 关联实现跨帧身份匹配。

## 实验阅读

BURST 与 LVVIS 的 OpenVIS，原表同时比较零样本性质。 LVVIS／BURST 与已见 YouTube-VIS 全监督结果分开阅读。 主表是整体系统结果，单一模块的贡献需结合原文消融。

## 原文依据

- [本次阅读的原文版本](https://raw.githubusercontent.com/PinxueGuo/OpenVIS/main/OpenVIS_AAAI-25_paper.pdf)：方法部分；Figure 3（PDF 第 5 页）；实验 Table 1（PDF 第 6 页）。
- [正式发表来源](https://ojs.aaai.org/index.php/AAAI/article/view/32338)。
- [官方实现](https://github.com/PinxueGuo/OpenVIS)：已核对官方实现目录：OpenVIS_AAAI-25_paper.pdf、adapter-transformers、code_guide.md、configs、datasets、demo_video。未独立运行或验证外部权重下载。
