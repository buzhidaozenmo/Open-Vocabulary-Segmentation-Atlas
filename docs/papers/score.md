---
paper_id: score
title: 'SCORE: Scene Context Matters in Open-Vocabulary Remote Sensing Instance Segmentation'
short_name: SCORE
authors:
- Shiqi Huang
- Shuting He
- Huaiyuan Qin
- Bihan Wen
year: 2025
preprint_date: unknown
venue: ICCV
publication_status: published
primary_direction: remote
modalities:
- image
task_setting: open_vocabulary
task_types:
- instance
techniques:
- semantic_alignment
- region_aggregation
- fusion
datasets:
- iSAID
- SIOR
- NWPU-VHR-10
- SOTA
- FAST
paper_url: https://openaccess.thecvf.com/content/ICCV2025/papers/Huang_SCORE_Scene_Context_Matters_in_Open-Vocabulary_Remote_Sensing_Instance_Segmentation_ICCV_2025_paper.pdf
publication_url: https://openaccess.thecvf.com/content/ICCV2025/html/Huang_SCORE_Scene_Context_Matters_in_Open-Vocabulary_Remote_Sensing_Instance_Segmentation_ICCV_2025_paper.html
code_status: public
code_url: https://github.com/HuangShiqi128/SCORE
code_details: 官方仓库含 train_net.py、配置、iSAID／SIOR 评测脚本和数据入口；依赖外部 RemoteCLIP 检查点，未运行。
content_status: index
checked_on: '2026-11-09'
module_checked_on: '2026-11-09'
summary: 把遥感区域上下文注入实例特征，并以全局场景信息适配文本分类器。
sources:
- url: https://openaccess.thecvf.com/content/ICCV2025/html/Huang_SCORE_Scene_Context_Matters_in_Open-Vocabulary_Remote_Sensing_Instance_Segmentation_ICCV_2025_paper.html
  locator: 正式发表：出版方页面／DOI；期刊状态另由官方仓库文档确认
- url: https://openaccess.thecvf.com/content/ICCV2025/papers/Huang_SCORE_Scene_Context_Matters_in_Open-Vocabulary_Remote_Sensing_Instance_Segmentation_ICCV_2025_paper.pdf
  locator: 本次所读原文版本的 §3–5／III–V、方法图及主要结果表
- url: https://github.com/HuangShiqi128/SCORE
  locator: 官方仓库实际目录与文档／项目页；未运行
figures:
- id: fig2
  label: Figure 2
  asset: assets/figures/score-fig2.png
  page: 3
  version: ICCV 2025 出版方正式版
  source_url: https://openaccess.thecvf.com/content/ICCV2025/papers/Huang_SCORE_Scene_Context_Matters_in_Open-Vocabulary_Remote_Sensing_Instance_Segmentation_ICCV_2025_paper.pdf
  clip_pdf_points:
  - 55
  - 50
  - 558
  - 298
  source_sha256: 2521d7f4741ce61e275965d29e25f47684617dc253a8fbbb5705653cf9bfefb7
- id: fig3
  label: Figure 3
  asset: assets/figures/score-fig3.png
  page: 4
  version: ICCV 2025 出版方正式版
  source_url: https://openaccess.thecvf.com/content/ICCV2025/papers/Huang_SCORE_Scene_Context_Matters_in_Open-Vocabulary_Remote_Sensing_Instance_Segmentation_ICCV_2025_paper.pdf
  clip_pdf_points:
  - 55
  - 50
  - 298
  - 267
  source_sha256: 2521d7f4741ce61e275965d29e25f47684617dc253a8fbbb5705653cf9bfefb7
methods:
- id: regional
  track: vocabulary
  problems:
  - alignment
  - regions
  title: 扩张掩码汇聚遥感区域上下文
  question: 小目标或外观模糊对象怎样利用周围环境识别类别？
  operation: 以预测实例掩码为参照，按原文可学习扩张机制获得周边区域；池化 RemoteCLIP 的区域 patch 特征，再经 Transformer 与对象类别嵌入交互，给实例表示加入域内上下文。
  input: 实例掩码、类别嵌入、冻结 RemoteCLIP patch 特征
  output: 区域上下文增强的实例嵌入
  stage: 训练与推理
  supervision: iSAID 或 SIOR 实例监督；预训练通用 CLIP 与 RemoteCLIP
  origin: proposed
  origin_note: 本文 Region-Aware Integration；具体可学习形态操作按原文描述，未做代码执行核查。
  origin_refs: []
  evidence:
  - url: https://openaccess.thecvf.com/content/ICCV2025/papers/Huang_SCORE_Scene_Context_Matters_in_Open-Vocabulary_Remote_Sensing_Instance_Segmentation_ICCV_2025_paper.pdf
    locator: §3.3–3.4，Eq.2–6
  figure: fig3
  figure_guide: 独立区域图看 Adaptive Region Formation 的掩码扩张，再看 Regional Context Extraction 的 mask pooling。
  depicted: true
  route:
  - 遥感区域上下文
  - 区域上下文聚合
  - 实例特征
  - 文本相似度分类
- id: global
  track: vocabulary
  problems:
  - alignment
  - unseen
  title: 全局场景信息适配文本分类器
  question: 通用类别文本如何获得遥感领域上下文？
  operation: 类别名称套入遥感提示模板后，经冻结 CLIP 文本编码并跨模板平均；将 RemoteCLIP 全局 CLS 上下文通过跨注意力接入文本分类器。推理结合训练分支与通用 CLIP 掩码池化的词表外分类分数。
  input: 类别文本、遥感全局 CLS、实例特征
  output: 领域适配的文本分类器及实例分数
  stage: 训练与推理
  supervision: 遥感实例监督和预训练视觉语言模型；最终词表外分类仍采用通用 CLIP
  origin: proposed
  origin_note: 本文 Global Context Adaptation；模型集成依循原文引用的既有分割框架，不推断其为首次提出。
  origin_refs: []
  evidence:
  - url: https://openaccess.thecvf.com/content/ICCV2025/papers/Huang_SCORE_Scene_Context_Matters_in_Open-Vocabulary_Remote_Sensing_Instance_Segmentation_ICCV_2025_paper.pdf
    locator: §3.5–3.6，Eq.7
  figure: fig2
  figure_guide: 总图下方 Global Context Adaptation 看 CLS 与 text embeddings 的交互，再看 class prediction；推理集成见 §3.6。
  depicted: true
  route:
  - 遥感全局上下文
  - 场景条件文本适配
  - 类别文本嵌入
  - 文本相似度分类
results:
- id: table1
  label: Table 1
  asset: assets/results/score-table1.png
  page: 6
  version: ICCV 2025 出版方正式版
  source_url: https://openaccess.thecvf.com/content/ICCV2025/papers/Huang_SCORE_Scene_Context_Matters_in_Open-Vocabulary_Remote_Sensing_Instance_Segmentation_ICCV_2025_paper.pdf
  clip_pdf_points:
  - 55
  - 68
  - 558
  - 190
  source_sha256: 2521d7f4741ce61e275965d29e25f47684617dc253a8fbbb5705653cf9bfefb7
  title: 遥感开放词汇实例分割
  setting: 分别以 iSAID／SIOR 训练，对其他遥感数据集作跨数据集评测，原表左右两组对应不同训练源。
  metrics: mAP ↑；Average ↑
  reading: 分别比较两个训练源下各列结果；不把 iSAID、SIOR 的训练与测试方向交换。
---
# SCORE

## 资料范围与状态

核查版本：ICCV 2025 出版方正式版；正式发表来源另见出版方链接。已完成与研究关注点有关的方法、配图和主结果表定向整理，尚未完成全文样例笔记。图中的方法关系以原文为准，未独立运行实现。

## 关注的问题

【原文事实】把遥感区域上下文注入实例特征，并以全局场景信息适配文本分类器。

## 实验阅读

分别以 iSAID／SIOR 训练，对其他遥感数据集作跨数据集评测，原表左右两组对应不同训练源。 分别比较两个训练源下各列结果；不把 iSAID、SIOR 的训练与测试方向交换。 数值保留在原始结果表中；它们是论文报告值，不是本库复现值。

## 开源情况

【官方文档说明／项目页核查】官方仓库含 train_net.py、配置、iSAID／SIOR 评测脚本和数据入口；依赖外部 RemoteCLIP 检查点，未运行。 本轮没有安装依赖、执行训练或验证复现结果。
