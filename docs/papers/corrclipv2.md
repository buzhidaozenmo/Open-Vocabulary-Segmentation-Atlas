---
paper_id: corrclipv2
title: 'CorrCLIPv2: Harnessing Unlabeled Images for Open-Vocabulary Semantic Segmentation'
short_name: CorrCLIPv2
authors:
- Dengke Zhang
- Fagui Liu
- Quan Tang
- C. L. Philip Chen
year: 2026
preprint_date: '2026-10-17'
venue: IJCV
publication_status: published
primary_direction: 2d
modalities:
- image
task_setting: open_vocabulary
task_types:
- semantic
techniques:
- semantic_alignment
- region_aggregation
- retrieval
- fusion
datasets:
- ADE20K
- PASCAL
- COCO
- Cityscapes
- MESS
paper_url: https://arxiv.org/abs/2610.24757
publication_url: https://link.springer.com/article/10.1007/s11263-026-03027-3
code_status: public
code_url: https://github.com/zdk258/CorrCLIP/tree/master/CorrCLIPv2
code_details: CorrCLIPv2 子目录已提供实际实现、配置、评测和记忆库相关说明。
content_status: detailed_sample
checked_on: '2026-11-09'
summary: 重建CLIP相关性，以无标注图像记忆库与多CLIP集成缓解上下文偏差。
sources:
- url: https://link.springer.com/article/10.1007/s11263-026-03027-3
  locator: 正式发表来源
- url: https://arxiv.org/html/2610.24757v1
  locator: v1 §3 / Table 6、10、12
- url: https://github.com/zdk258/CorrCLIP/tree/master/CorrCLIPv2
  locator: 官方 README / 公开目录；未运行
figures:
- id: fig3
  asset: assets/figures/corrclipv2-fig3.png
  label: Figure 3
  page: 7
  version: arXiv 2610.24757v1
  source_url: https://arxiv.org/pdf/2610.24757v1
  clip_pdf_points:
  - 64
  - 45
  - 525
  - 290
  source_sha256: 66138d73fa96404748dd529cf7c8ab929e937871419c2ed391e10a5171bea59d
- id: fig6
  asset: assets/figures/corrclipv2-fig6.png
  label: Figure 6
  page: 10
  version: arXiv 2610.24757v1
  source_url: https://arxiv.org/pdf/2610.24757v1
  clip_pdf_points:
  - 72
  - 45
  - 293
  - 206
  source_sha256: 66138d73fa96404748dd529cf7c8ab929e937871419c2ed391e10a5171bea59d
- id: fig7
  asset: assets/figures/corrclipv2-fig7.png
  label: Figure 7
  page: 10
  version: arXiv 2610.24757v1
  source_url: https://arxiv.org/pdf/2610.24757v1
  clip_pdf_points:
  - 310
  - 45
  - 532
  - 185
  source_sha256: 66138d73fa96404748dd529cf7c8ab929e937871419c2ed391e10a5171bea59d
methods:
- id: correlation
  track: vocabulary
  problems:
  - alignment
  - regions
  title: 重建 CLIP 的关联范围和关联值
  question: 图像级 CLIP 特征如何变成像素预测？
  operation: 用类别无关区域掩码限制 patch 交互范围，以自监督视觉模型的相似性重建相关值；聚合 CLIP 值特征，经过空间／语义分支细化后，与类别文本嵌入比较，并利用区域掩码更新预测。
  input: 图像、CLIP 与视觉基础模型特征、区域掩码
  output: 密集语言对齐特征与分割图
  stage: 推理
  supervision: 冻结预训练模型；该流程不做参数训练
  origin: modified
  origin_note: CorrCLIPv2 沿用 CorrCLIP 单图像基础流程；新增跨图检索另列。
  origin_refs:
  - url: https://arxiv.org/abs/2411.10086
    locator: CorrCLIPv2 文中 CorrCLIP 单图基础方法
  evidence:
  - url: https://arxiv.org/pdf/2610.24757v1
    locator: §3.2.1–3.2.3，Figure 3
  figure: fig3
  figure_guide: 总图上方 Scope Reconstruction 与 Value Reconstruction 两条路径，再看输出与 Textual Encoder 的匹配。
  depicted: true
  route:
  - 二维密集特征
  - 相关性重建
  - 二维密集特征
  - 文本相似度分类
- id: retrieval
  track: vocabulary
  problems:
  - alignment
  - reliability
  title: 视觉键检索、语言语义值回读
  question: 如何用跨图同类实例减轻单图上下文偏差？
  operation: 离线在同一区域内分别池化 VFM 特征与 CorrCLIP 特征，保存为索引键和语义值；在线以 VFM 区域特征检索 top-k 邻居，将对应语义值平均成支持集，再用于语义增强。
  input: 无标注图像库、当前图像区域特征
  output: 跨图语义支持特征
  stage: 离线建库＋在线检索
  supervision: 预训练模型与无标注图库；无新增参数训练
  origin: proposed
  origin_note: 本文 VFM-Indexed Semantic Retrieval；普通 MAP 池化并非本文独创。
  origin_refs: []
  evidence:
  - url: https://arxiv.org/pdf/2610.24757v1
    locator: §3.3.2，Eq.12–13，Figure 6–7
  figure: fig7
  figure_guide: 独立在线检索图：MAP→Search Top-K→Retrieve CorrCLIP Features→Mean；离线建库见同文 Figure 6。
  depicted: true
  route:
  - 跨图语义库
  - 视觉键语义值检索
  - 区域语义原型
  - 语义增强
module_checked_on: '2026-11-09'
results:
- id: table1
  label: Table 1
  asset: assets/results/corrclipv2-table1.png
  title: 十个标准二维开放词汇分割基准
  setting: 十个基准各自报告 mIoU；保留全监督、弱监督及免训练方法的分组。
  metrics: mIoU ↑；Mean ↑
  reading: 看最下方 CorrCLIPv2 与同组 VFM-based 免训练方法；不同训练组的结果不要当作相同监督条件。
  page: 13
  version: arXiv 2610.24757v1
  source_url: https://arxiv.org/pdf/2610.24757v1
  source_sha256: 66138d73fa96404748dd529cf7c8ab929e937871419c2ed391e10a5171bea59d
  clip_pdf_points:
  - 64
  - 68
  - 524
  - 472
---
# CorrCLIPv2

## 资料范围与版本

阅读 arXiv:2610.24757 **v1（2026-10-17）**。正式版本发表在 IJCV，DOI 为 `10.1007/s11263-026-03027-3`。以下方法和表号对应可访问的预印本；期刊页面用于确认发表身份，未假定两版本完全一致。官方实现与 README 做静态范围核查，未运行评测。

## 任务

【原文事实】输入图像与候选文本类别，输出逐像素语义类别。方法不更新任务模型参数，但构建离线外部图像记忆库，并依赖预训练 CLIP、视觉基础模型及掩码生成器。因此 training-free 不等于“没有离线数据或预训练成本”。

## 研究问题

CLIP 图像级语义强，但 patch 之间的跨类别关联会污染局部预测；单个物体的特征又易受背景上下文影响。方法先控制单图信息交互，再从其他图像中的相似物体补充语义（§1、§3）。

## 方法

1. **Scope Reconstruction（§3.2.1）。** 用类别无关掩码约束 patch 交互范围，减少不同对象之间不必要的信息混合。掩码不直接提供目标类别标签。
2. **Value Reconstruction（§3.2.2）。** 借助空间一致性较强的自监督视觉特征，重算范围内部的相关性；不能只把方法概括成“使用 SAM 生成掩码”。
3. **特征与输出修正（§3.2.3–3.2.4）。** 空间和语义分支补充特征，区域内多数投票统一输出。区域一致性假设也带来欠分割时的风险。
4. **VISR（§3.3.2）。** 离线为区域保存视觉索引及 CorrCLIP 语义特征。在线用视觉基础模型特征检索相近对象，再聚合检索到的语义信息，降低单幅图像的上下文偏差。索引特征与被聚合语义特征是两个角色。
5. **DMCE（§3.3.3）。** 将额外 CLIP 编码的部分成本转移到离线记忆库，多模型知识可在在线阶段组合；并不表示所有计算和存储都消失。

## 实验 {#experiments}

【原文事实】Table 1 覆盖 10 个标准评测协议，Table 2 为 MESS 的 22 个跨域数据集。不能把不同标签集的分数直接当成相同难度比较，也不能把训练免费方法与使用密集监督的方法不加说明混排。

Table 6 中 **ViT-L 配置的 ADE20K-150** 消融为：

| 配置 | mIoU |
| --- | ---: |
| CorrCLIP-L | 32.9 |
| 加 VISR | 35.4 |
| 再加 DMCE | 36.5 |

这支持检索与集成在该配置中的增益。Table 10 在 RTX 4090、FP16 下记录在线延迟与显存，包含标准和 fast 配置；比较时必须连同掩码生成器、视觉基础模型及离线记忆库一起记录，不能只引用一个 FPS。

## 局限

【原文事实】§4.6、Table 12 的 oracle prompt 实验只提供实际出现的类别，性能明显上升，说明大词表中的无关语义仍是瓶颈。oracle 用到真实存在类别，不是可直接部署的标准推理设置。

【分析推断】记忆库覆盖与检索质量可能影响长尾类别；相似外观不保证相同语义。将其迁移到三维时，区域定义、跨视角重复及几何邻接都需重新验证，不能直接宣称已有三维效果。

## 横向理解

它与 EOVSAM 分别代表“冻结表示、重构关联并检索”和“监督适配掩码生成与识别”的路线。两者训练数据和模型依赖不同，不根据 ADE20K 单个分数给出公平优劣结论。

## 开源情况

【官方文档说明】同一仓库包含 CorrCLIPv1、CorrCLIPv2 两个自包含目录；v2 有配置、评测及记忆库流程。需根据指定的掩码生成器、VFM、CLIP 和记忆库选择配置，不能仅凭方法名复现论文某一行。

## 证据

| 主张 | 原始材料定位 |
| --- | --- |
| 单图相关性重建 | [v1 §3.2](https://arxiv.org/html/2610.24757v1#S3.SS2) |
| VISR 与 DMCE | [§3.3](https://arxiv.org/html/2610.24757v1#S3.SS3) |
| 检索与集成的消融 | [Table 6](https://arxiv.org/html/2610.24757v1#S4.T6) |
| 延迟与显存设置 | [Table 10](https://arxiv.org/html/2610.24757v1#S4.T10) |
| 语义干扰与 oracle 差距 | [§4.6 / Table 12](https://arxiv.org/html/2610.24757v1#S4.SS6) |
| 实际公开目录 | [官方 v2 实现](https://github.com/zdk258/CorrCLIP/tree/master/CorrCLIPv2) |
