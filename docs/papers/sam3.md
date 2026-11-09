---
paper_id: sam3
title: 'SAM 3: Segment Anything with Concepts'
short_name: SAM3
authors: []
year: 2026
preprint_date: '2025-11-20'
venue: ICLR
publication_status: published
primary_direction: 2d
modalities:
- image
- video
task_setting: concept_prompt
task_types:
- concept_prompt
- instance
techniques:
- prompt
- temporal
datasets:
- SA-Co
paper_url: https://arxiv.org/abs/2511.16719
publication_url: https://proceedings.iclr.cc/paper_files/paper/2026/hash/e0982cbc81401df3430ee1ff780dc7a2-Abstract-Conference.html
code_status: public
code_url: https://github.com/facebookresearch/sam3
code_details: 提供推理、微调、示例与检查点入口；权重需按官方访问与许可流程获取。
content_status: index
checked_on: '2026-11-09'
summary: 通过文本概念或图像示例分割匹配实例，并支持视频中的身份跟踪。
sources:
- url: https://proceedings.iclr.cc/paper_files/paper/2026/hash/e0982cbc81401df3430ee1ff780dc7a2-Abstract-Conference.html
  locator: 正式发表来源
- url: https://github.com/facebookresearch/sam3
  locator: 官方 README / 公开目录；未运行
figures:
- id: fig4
  asset: assets/figures/sam3-fig4.png
  label: Figure 4
  page: 4
  version: arXiv 2511.16719v2
  source_url: https://arxiv.org/pdf/2511.16719v2
  clip_pdf_points:
  - 68
  - 45
  - 545
  - 205
  source_sha256: 19e8a44e7fc33bc6cf237f6b4ac3948a79b33f7ffc62d09012fcac6fc9fb016f
methods:
- id: concept
  track: vocabulary
  problems:
  - alignment
  - unseen
  title: 概念条件检测与独立存在性判断
  question: 文本概念如何影响掩码，而不是事后固定类别分类？
  operation: 图像特征与文本／示例提示经融合编码器交互；检测查询产生匹配实例的框、分数与掩码，独立 presence token 估计概念是否存在，减少把定位质量和语义存在性混在一个分数中的问题。
  input: 图像、短文本概念或图像示例
  output: 概念匹配实例掩码及存在性分数
  stage: 训练与推理
  supervision: 大规模概念—图像／视频掩码数据及预训练视觉语言骨干
  origin: proposed
  origin_note: 本文的概念分割检测器与 presence token；主图为概览。
  origin_refs: []
  evidence:
  - url: https://arxiv.org/pdf/2511.16719v2
    locator: §2–3，Figure 4；附录 C.1，Figure 10
  figure: fig4
  figure_guide: 看提示编码器→融合编码器→检测器分支；presence token 的细节在附录 Figure 10，概览没有独立展开。
  depicted: true
  route:
  - 概念文本与示例
  - 概念条件跨模态交互
  - 实例掩码
  - 概念条件分割
  result_tables:
  - table1
- id: tracking
  track: vocabulary
  problems:
  - temporal
  title: 概念检测与对象记忆跟踪协作
  question: 视频中新出现的概念实例如何进入并保持身份？
  operation: 检测器逐帧识别概念匹配对象，跟踪器根据对象记忆传播掩码；关联两路结果，接入新检测并维护现有对象身份，结合时序后处理稳定输出。
  input: 视频帧、概念提示、对象记忆
  output: 带身份的概念实例 masklets
  stage: 推理；组件经训练
  supervision: 概念视频标注与预训练跟踪能力
  origin: modified
  origin_note: 本文概念检测器与基于 SAM2 的跟踪器协同；不是仅用固定首帧掩码传播。
  origin_refs:
  - url: https://arxiv.org/abs/2408.00714
    locator: SAM3 原文引用 SAM2 跟踪架构
  evidence:
  - url: https://arxiv.org/pdf/2511.16719v2
    locator: §3，附录 C.2，Figure 4
  figure: fig4
  figure_guide: 看检测器与底部 memory / tracker 的连接及输出视频掩码。
  depicted: true
  route:
  - 概念文本与示例
  - 检测与记忆关联
  - 视频实体记忆
  - 跨帧语义保持
  result_tables:
  - table5
module_checked_on: '2026-11-09'
results:
- id: table1
  label: Table 1
  asset: assets/results/sam3-table1.png
  title: 文本概念驱动的图像分割主结果
  setting: 实例分割、框检测和语义分割三组任务，含 LVIS、SA-Co、COCO、ADE-847、PC-59、Cityscapes；原表灰色标记使用了相应闭集训练数据的结果。
  metrics: cgF1／pmF1、AP／APo、mIoU；按各列任务解释，均为 ↑
  reading: 看 SAM3 在各任务的对应列；APo、†、δ、灰色结果的解释全部保留在表注。
  page: 8
  version: arXiv 2511.16719v2
  source_url: https://arxiv.org/pdf/2511.16719v2
  source_sha256: 19e8a44e7fc33bc6cf237f6b4ac3948a79b33f7ffc62d09012fcac6fc9fb016f
  clip_pdf_points:
  - 68
  - 59
  - 545
  - 237
- id: table5
  label: Table 5
  asset: assets/results/sam3-table5.png
  title: 文本提示视频概念分割主结果
  setting: SA-Co/VEval 测试集与 LVVIS、BURST、YTVIS21、OVIS 公共基准；候选名词短语数量在原表中注明。
  metrics: cgF1 ↑；pHOTA ↑；mAP ↑；HOTA ↑
  reading: 按数据集和指标分别比较 SAM3 与视频基线，† 对应原表的零样本适用说明。
  page: 9
  version: arXiv 2511.16719v2
  source_url: https://arxiv.org/pdf/2511.16719v2
  source_sha256: 19e8a44e7fc33bc6cf237f6b4ac3948a79b33f7ffc62d09012fcac6fc9fb016f
  clip_pdf_points:
  - 68
  - 273
  - 545
  - 418
---
# SAM3

## 当前整理状态

已按研究关注点核查下列方法模块与配图；尚未完成全文样例笔记，不据此生成实验排名。

## 收录理由

通过文本概念或图像示例分割匹配实例，并支持视频中的身份跟踪。

## 开源情况

【官方文档说明】提供推理、微调、示例与检查点入口；权重需按官方访问与许可流程获取。 本轮没有安装或运行代码，没有独立验证权重下载。


> 本条目主要归入2D，但同时具有视频模态标签；全站仅计一次。概念提示分割与标准OVSS评测分别记录。
