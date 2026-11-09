---
paper_id: cua_o3d
title: Cross-Modal and Uncertainty-Aware Agglomeration for Open-Vocabulary 3D Scene Understanding
short_name: CUA-O3D
authors:
- Jinlong Li
- Cristiano Saltori
- Fabio Poiesi
- Nicu Sebe
year: 2025
preprint_date: '2025-03-20'
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
- feature_distillation
- reliability
- fusion
datasets:
- ScanNet
- Matterport3D
paper_url: https://openaccess.thecvf.com/content/CVPR2025/papers/Li_Cross-Modal_and_Uncertainty-Aware_Agglomeration_for_Open-Vocabulary_3D_Scene_Understanding_CVPR_2025_paper.pdf
publication_url: https://openaccess.thecvf.com/content/CVPR2025/html/Li_Cross-Modal_and_Uncertainty-Aware_Agglomeration_for_Open-Vocabulary_3D_Scene_Understanding_CVPR_2025_paper.html
code_status: public
code_url: https://github.com/TyroneLi/CUA_O3D
code_details: 官方仓库含二维特征提取、多教师蒸馏、评测和跨数据集脚本；本轮未确认完整预训练检查点下载入口，未运行。
content_status: index
checked_on: '2026-11-09'
module_checked_on: '2026-11-09'
summary: 分别蒸馏 LSeg、DINOv2、Stable Diffusion，并学习不确定性权重调节异构教师监督。
sources:
- url: https://openaccess.thecvf.com/content/CVPR2025/html/Li_Cross-Modal_and_Uncertainty-Aware_Agglomeration_for_Open-Vocabulary_3D_Scene_Understanding_CVPR_2025_paper.html
  locator: CVPR 2025 正式发表页面
- url: https://openaccess.thecvf.com/content/CVPR2025/papers/Li_Cross-Modal_and_Uncertainty-Aware_Agglomeration_for_Open-Vocabulary_3D_Scene_Understanding_CVPR_2025_paper.pdf
  locator: CVPR 2025 正文 §3–4，方法图及主要结果表
- url: https://github.com/TyroneLi/CUA_O3D
  locator: 官方 README 与实际目录；未运行或逐行审计
figures:
- id: fig3
  asset: assets/figures/cua_o3d-fig3.png
  label: Figure 3
  page: 5
  version: CVPR 2025 出版方正式版
  source_url: https://openaccess.thecvf.com/content/CVPR2025/papers/Li_Cross-Modal_and_Uncertainty-Aware_Agglomeration_for_Open-Vocabulary_3D_Scene_Understanding_CVPR_2025_paper.pdf
  clip_pdf_points:
  - 55
  - 67
  - 557
  - 257
  source_sha256: 5246b82745084aa91702f0d9b06355ca3dd97ec54988a58262a29592a964a644
methods:
- id: projection
  track: pointcloud
  problems:
  - projection
  - multiview
  title: 分别投影多种二维教师到共同点集
  question: 不同教师特征怎样对应到相同的三维观测？
  operation: 分别从 LSeg、DINOv2、Stable Diffusion 提取多视图特征，以带位姿图像与点云的齐次坐标建立点—像素对应，把各路特征映射到点上；保留各教师空间，而非强行先平均异构特征。
  input: 点云、带位姿多视图、三路二维特征
  output: 对应同一场景的逐点教师目标
  stage: 离线目标构建／训练
  supervision: 预训练二维模型；需要相机几何信息，不用人工三维语义标签
  origin: modified
  origin_note: 在 OpenScene 类投影蒸馏流程上扩展多个异构教师；官方文档另要求各路使用一致的点索引。
  origin_refs:
  - url: https://arxiv.org/abs/2211.15654
    locator: 本文 §3.3 引用 OpenScene [62] 的三维蒸馏基础
  evidence:
  - url: https://openaccess.thecvf.com/content/CVPR2025/papers/Li_Cross-Modal_and_Uncertainty-Aware_Agglomeration_for_Open-Vocabulary_3D_Scene_Understanding_CVPR_2025_paper.pdf
    locator: §3.3，Figure 3；官方 README 特征提取说明
  figure: fig3
  figure_guide: 看底部三条 Multi-view 3D Projection 到各教师目标的路径；图中未展开具体相机或可见性公式。
  depicted: true
  route:
  - 异构二维教师
  - 可见性与跨视角融合
  - 逐点特征
  - 二维到三维传递
- id: heads
  track: pointcloud
  problems:
  - distillation
  - alignment
  title: 多分支蒸馏保留语义与空间先验
  question: 语言模型和非语言视觉教师如何共同训练点云网络？
  operation: 共享 MinkowskiNet 三维骨干，建立三路 MLP 映射，分别拟合各教师空间；LSeg 与 Stable Diffusion 路采用余弦损失，DINOv2 路采用 L1；Stable Diffusion
    的逐点特征沿通道去均值。开放词汇查询使用语言对齐分支，不把 DINOv2 直接当文本空间。
  input: 逐点三维特征、三路投影二维目标
  output: 兼顾语言与视觉空间先验的三维表征
  stage: 训练；语言匹配用于推理
  supervision: 冻结二维教师；训练点云骨干与投影头，无三维类别监督
  origin: proposed
  origin_note: 本文的异构空间独立映射与损失组合；骨干和各二维编码器沿用已有模型。
  origin_refs: []
  evidence:
  - url: https://openaccess.thecvf.com/content/CVPR2025/papers/Li_Cross-Modal_and_Uncertainty-Aware_Agglomeration_for_Open-Vocabulary_3D_Scene_Understanding_CVPR_2025_paper.pdf
    locator: §3.3，Eq.1–5，Figure 3
  figure: fig3
  figure_guide: 看三维骨干右侧三组 F3D、各路损失与教师目标；三条 MLP 映射保留各教师特征空间。
  depicted: true
  route:
  - 异构二维教师
  - 多分支特征蒸馏
  - 逐点特征
  - 特征蒸馏
- id: uncertainty
  track: pointcloud
  problems:
  - reliability
  - distillation
  title: 按教师噪声标量自适应加权蒸馏
  question: 各教师特征尺度与模态歧义不同，怎样调节监督强度？
  operation: 为三路监督分别学习噪声标量 σi，以 1/(2σi²) 加权对应蒸馏损失，并加对数正则项约束权重；噪声越大该路贡献越低。原文稳定化将 log σi 改为 log(1+σi)；推理去掉不确定性模块。
  input: 各路蒸馏损失、学习的噪声标量
  output: 自适应多教师训练目标
  stage: 训练
  supervision: 二维教师特征作为目标；不以人工类别 IoU 作为能力表
  origin: proposed
  origin_note: 本文的确定性不确定性蒸馏建模；它调节训练损失，不是 SAS 式按类别查能力表。
  origin_refs: []
  evidence:
  - url: https://openaccess.thecvf.com/content/CVPR2025/papers/Li_Cross-Modal_and_Uncertainty-Aware_Agglomeration_for_Open-Vocabulary_3D_Scene_Understanding_CVPR_2025_paper.pdf
    locator: §3.3，Eq.6–11，Figure 3
  figure: fig3
  figure_guide: 看图中 σ1、σ2、σ3 与各路损失的加权；对数正则与稳定化细节见公式。
  depicted: true
  route:
  - 异构二维教师
  - 可靠性加权与选择
  - 逐点特征
  - 特征蒸馏
results:
- id: table2
  asset: assets/results/cua_o3d-table2.png
  label: Table 2
  page: 6
  version: CVPR 2025 出版方正式版
  source_url: https://openaccess.thecvf.com/content/CVPR2025/papers/Li_Cross-Modal_and_Uncertainty-Aware_Agglomeration_for_Open-Vocabulary_3D_Scene_Understanding_CVPR_2025_paper.pdf
  clip_pdf_points:
  - 314
  - 68
  - 557
  - 358
  source_sha256: 5246b82745084aa91702f0d9b06355ca3dd97ec54988a58262a29592a964a644
  title: 三维开放词汇语义分割主结果
  setting: ScanNetV2 与 Matterport3D；区分全监督、上界和 zero-shot；3D 与 2D3D 行分开，† 为原论文 LSeg 结果。
  metrics: mIoU ↑；mAcc ↑
  reading: 优先与 OpenScene 的 reimple 同条件比较；Matterport3D 上 CUA-O3D (2D3D) 的 42.2 并未超过原论文 OpenScene-2D3D 的 43.4。
---
# CUA-O3D

## 资料范围与状态

本轮核查 CVPR 2025 正式正文 §3–4、方法图与主结果表，以及官方仓库文档和实际目录。已完成研究关注点的定向模块整理，尚未完成全文样例笔记；没有运行代码或复现实验。

## 关注的问题

分别蒸馏 LSeg、DINOv2、Stable Diffusion，并学习不确定性权重调节异构教师监督。

## 实验阅读

【原文事实】ScanNetV2 与 Matterport3D；区分全监督、上界和 zero-shot；3D 与 2D3D 行分开，† 为原论文 LSeg 结果。 优先与 OpenScene 的 reimple 同条件比较；Matterport3D 上 CUA-O3D (2D3D) 的 42.2 并未超过原论文 OpenScene-2D3D 的 43.4。 结果来自原文报告，完整比较行、训练组与脚注见展开区原表。

## 开源情况

【官方文档说明】官方仓库含二维特征提取、多教师蒸馏、评测和跨数据集脚本；本轮未确认完整预训练检查点下载入口，未运行。 依赖的外部教师和模型许可需遵循各原始项目。
