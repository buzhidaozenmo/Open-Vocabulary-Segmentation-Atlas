---
paper_id: openscene
title: 'OpenScene: 3D Scene Understanding with Open Vocabularies'
short_name: OpenScene
authors:
- Songyou Peng
- Kyle Genova
- Chiyu Max Jiang
- Andrea Tagliasacchi
- Marc Pollefeys
- Thomas Funkhouser
year: 2023
preprint_date: '2022-11-28'
venue: CVPR
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
- fusion
datasets:
- ScanNet
- Matterport3D
- nuScenes
paper_url: https://arxiv.org/abs/2211.15654
publication_url: https://openaccess.thecvf.com/content/CVPR2023/html/Peng_OpenScene_3D_Scene_Understanding_With_Open_Vocabularies_CVPR_2023_paper.html
code_status: public
code_url: https://github.com/pengsongyou/openscene
code_details: 官方实现包含多视角融合、3D蒸馏与评测；提供预训练模型及预处理特征入口。
content_status: detailed_sample
checked_on: '2026-11-09'
summary: 多视角二维特征如何成为可供文本查询的三维点特征。
sources:
- url: https://openaccess.thecvf.com/content/CVPR2023/html/Peng_OpenScene_3D_Scene_Understanding_With_Open_Vocabularies_CVPR_2023_paper.html
  locator: 正式发表来源
- url: https://arxiv.org/pdf/2211.15654v2
  locator: v2 §3 / Table 4
- url: https://github.com/pengsongyou/openscene
  locator: 官方 README / 公开目录；未运行
figures:
- id: fig3
  asset: assets/figures/openscene-fig3.png
  label: Figure 3
  page: 3
  version: arXiv 2211.15654v2
  source_url: https://arxiv.org/pdf/2211.15654v2
  clip_pdf_points:
  - 305
  - 45
  - 549
  - 234
  source_sha256: 31a4c88491fa9b38180e251b64422107c7d3028ef21b1c9e01581501b7868f0e
methods:
- id: projection
  track: pointcloud
  problems:
  - projection
  - multiview
  title: 投影、可见性筛选与跨视角平均
  question: 同一个三维点从哪些像素接收语义？
  operation: 用相机内外参将点投到各视图，借深度检查遮挡；收集可见像素的二维语言对齐特征，对同一点的多视角特征取均值。
  input: 点云、带位姿 RGB-D、二维密集特征
  output: 逐点多视角融合特征
  stage: 训练目标生成／带图像推理
  supervision: 预训练二维教师；需要深度与相机标定
  origin: unverified
  origin_note: 本文基础投影与融合步骤；本轮未核查这些通用操作的历史首创来源。
  origin_refs: []
  evidence:
  - url: https://arxiv.org/pdf/2211.15654v2
    locator: §3.1，Figure 3
  figure: fig3
  figure_guide: 看左上多视图到中间 Multi-view Feature Fusion，再到逐点二维特征；主图没有展开深度可见性公式。
  depicted: true
  route:
  - 二维密集特征
  - 可见性与跨视角融合
  - 逐点特征
  - 二维到三维传递
- id: distill
  track: pointcloud
  problems:
  - distillation
  title: 用余弦损失蒸馏到点云网络
  question: 怎样让点云网络保留二维教师的语言空间？
  operation: 用多视角融合特征作为目标，最小化逐点 1−cos 相似度；推理时将三维特征与任意文本类别嵌入比较。
  input: 融合二维特征、点云
  output: 语言对齐三维特征
  stage: 训练；文本分类用于推理
  supervision: 无需三维语义标签；依赖预训练二维教师
  origin: modified
  origin_note: 沿用预训练二维语言空间，在三维网络上实施特征蒸馏。
  origin_refs:
  - url: https://vladlen.info/papers/LSeg.pdf
    locator: 原文 §3.1 引用的二维教师 LSeg
  evidence:
  - url: https://arxiv.org/pdf/2211.15654v2
    locator: §3.2–3.3，Figure 3
  figure: fig3
  figure_guide: 看 E3D 到 L 的蒸馏连接；右侧余弦相似度连接文本查询。
  depicted: true
  route:
  - 二维密集特征
  - 特征蒸馏
  - 逐点特征
  - 文本相似度分类
- id: ensemble
  track: pointcloud
  problems:
  - reliability
  title: 按文本匹配置信度选择二维或三维特征
  question: 二维细节和三维上下文冲突时如何取舍？
  operation: 分别计算二维融合特征、三维网络特征对候选文本的余弦相似度，以各自最高相似度比较置信度，逐点选择较可信的一路，而非把两路直接平均。
  input: 二维融合与三维网络特征、候选文本
  output: 二维／三维集成预测
  stage: 推理
  supervision: 预训练文本编码器；无需新增标签
  origin: proposed
  origin_note: 本文的二维三维集成规则；不据此宣称置信度选择思想的历史首创。
  origin_refs: []
  evidence:
  - url: https://arxiv.org/pdf/2211.15654v2
    locator: §3.3，Figure 3
  figure: fig3
  figure_guide: 看 f2D、f3D 汇合为 f2D3D 的路径；选择规则需要结合 §3.3 阅读。
  depicted: true
  route:
  - 二维与三维语义
  - 可靠性加权与选择
  - 逐点特征
  - 文本相似度分类
module_checked_on: '2026-11-09'
---
# OpenScene

## 资料范围与版本

阅读版本为 arXiv:2211.15654 **v2（2023-04-06）**，正式发表于 CVPR 2023。本文的表号和 PDF 页码以该预印本为准。核查官方仓库与文档，未运行模型，未逐行审计损失实现。

## 任务

【原文事实】训练输入为三维场景及带位姿的多视角 RGB 观测；投影需要相机参数，室内场景还以深度做可见性判断。输出是可与文本比较的逐点嵌入，而非固定类别分类头。训练不使用目标三维任务的语义标签；二维教师本身已有预训练与监督来源，不能据此称整个系统“完全无监督”。

推理必须分清三种配置：**2D Fusion** 使用图像融合特征；**3D Distill** 仅以三维几何生成蒸馏特征；**2D–3D Ensemble** 同时利用二者。比较论文结果前必须记录是哪一种。

## 研究问题

固定类别训练限制了可查询概念。直接对多视角预测类别投票又丢失语义相似性：文本嵌入能表达概念之间的接近程度，因此作者先得到可查询特征，再按输入文本分类（§1–3）。

## 方法

1. **像素到点的融合（§3.1）。** 冻结 LSeg 或 OpenSeg，提取每像素特征。通过相机内外参找到点对应的像素，过滤不可见投影，对同一点的多视角特征平均，得到 `F_2D`。
2. **三维蒸馏（§3.2）。** MinkowskiNet18A 输入点的位置，输出同维逐点特征 `F_3D`。更新三维网络，目标是最小化 `1 − cosine(F_2D, F_3D)`；二维融合特征充当固定目标。式(1)–(2)解释了谁提供监督、谁更新参数。
3. **特征选择式集成（§3.3）。** 分别计算二维、三维特征与候选文本的相似度。每个分支取最高类别相似度，再选择最高分对应的那一个特征。**原文不是简单平均两分支特征。**
4. **查询（§3.4）。** 对逐点特征与文本嵌入计算余弦相似度；用于语义分类或连续查询热图。文本词表可以替换，无需为每个词表重新训练点编码器。

```mermaid
flowchart LR
  A[多视角图像与位姿] --> B[冻结二维教师]
  B --> C[可见性投影与多视角平均]
  C --> D[固定二维点特征]
  P[三维几何] --> E[可训练三维编码器]
  D -.余弦蒸馏目标.-> E
  E --> F[三维点特征]
  D --> G[按文本相似度选择分支]
  F --> G
```

## 实验 {#experiments}

【原文事实】§4.1 分别使用 nuScenes 验证集、ScanNet 验证集、Matterport3D 测试集。Table 1 是 ScanNet 的 **4 个未见类别**，不能和全类 Table 2 混为同一个协议。

Table 4（PDF p.6）中的 LSeg 配置给出以下 **ScanNet** 消融，均为论文报告值：

| 特征模式 | mIoU | mAcc |
| --- | ---: | ---: |
| 2D Fusion | 50.0 | 62.7 |
| 3D Distill | 52.9 | 63.2 |
| 2D–3D Ensemble | 54.2 | 66.6 |

该表支持“这组设置中二维与三维存在互补”。它不证明每个类别、每个外部教师或所有场景都应采用相同选择规则。Table 3 的长尾实验用 **mAcc**，不能把其分数误写成 mIoU。

## 局限

【原文事实】§6 讨论开放词汇模型、场景观测等限制；长尾与属性查询不等于已建立完备的三维常识。所读版本 Table 2 的全类表现仍落后于当时强监督方法。

【分析推断】最高相似度是相对分数，不必然经过置信度校准。投影误差、遮挡和教师误识别会进入蒸馏目标；仅优化几何学生并不能保证消除二维语义错误。多视角离线特征也带来存储和预处理成本。

## 横向理解

SAS §3.1 明确沿用 OpenScene 的像素—点对应与多视角融合，并扩展到多教师。GeoPurify 则将几何关系学习用于净化语义，适合比较“生成语义特征”和“修正语义结构”两个环节；这里不据相似性认定直接继承。

## 开源情况

【官方文档说明】仓库提供融合、蒸馏、评测流程及预训练资源。不同教师和特征模式有不同配置。资源链接存在不代表已验证能下载或复现，安装与硬件兼容性尚未检查。

## 证据

| 主张 | 原始材料定位 |
| --- | --- |
| 可见性投影、多视角平均 | [v2 PDF §3.1，p.3–4](https://arxiv.org/pdf/2211.15654v2#page=3) |
| 稀疏三维网络与余弦蒸馏 | [§3.2，式(1)–(2)，p.4](https://arxiv.org/pdf/2211.15654v2#page=4) |
| 选择式集成而非简单平均 | [§3.3，式(3)，p.4](https://arxiv.org/pdf/2211.15654v2#page=4) |
| 三种模式的结果区别 | [Table 4，p.6](https://arxiv.org/pdf/2211.15654v2#page=6) |
| 开源范围 | [官方 README](https://github.com/pengsongyou/openscene) |
