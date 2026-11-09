---
paper_id: geopurify
title: 'GeoPurify: A Data-Efficient Geometric Distillation Framework for Open-Vocabulary
  3D Segmentation'
short_name: GeoPurify
authors:
- Weijia Dou
- Xu Zhang
- Yi Bin
- Jian Liu
- Bo Peng
- Guoqing Wang
- Yang Yang
- Heng Tao Shen
year: 2026
preprint_date: '2025-10-02'
venue: ICLR
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
- geometry
- region_aggregation
datasets:
- ScanNet
- Matterport3D
paper_url: https://arxiv.org/abs/2510.02186
publication_url: https://proceedings.iclr.cc/paper_files/paper/2026/hash/039bc8e424e1fc196b4203555b54ebc4-Abstract-Conference.html
code_status: public
code_url: https://github.com/tj12323/GeoPurify
code_details: 公开模型、配置、训练和评测脚本；提供ScanNet与Matterport3D检查点入口。
content_status: detailed_sample
checked_on: '2026-11-09'
summary: 通过几何关系蒸馏与几何引导池化，净化投影到三维的语义特征。
sources:
- url: https://proceedings.iclr.cc/paper_files/paper/2026/hash/039bc8e424e1fc196b4203555b54ebc4-Abstract-Conference.html
  locator: 正式发表来源
- url: https://arxiv.org/html/2510.02186v2
  locator: v2 §3 / Table 1、4
- url: https://github.com/tj12323/GeoPurify
  locator: 官方 README / 公开目录；未运行
---
# GeoPurify

## 资料范围与版本

阅读 arXiv:2510.02186 **v2（2026-02-11）**，正式发表于 ICLR 2026。正文和附录的实验以此版本为准。检查官方 README 与公开资源入口，未运行网络，尚未逐行验证池化实现。

## 任务

【原文事实】冻结二维 VLM 产生多视角语义特征，投影聚合到三维；训练阶段另外使用冻结的三维自监督教师 Sonata 学习几何关系。目标是开放词汇三维语义分割，不使用训练场景的三维语义标签。

“约 1.5% 数据”指该实验中训练学生使用的三维场景子集，**不包含二维基础模型与 Sonata 原始预训练的总数据成本**，不能解释为整个系统只看过 1.5% 数据。

## 研究问题

二维语义跨视图投影后容易碎片化，直接平滑又可能抹去边界。作者提出先学习哪些点在几何上应当相近，再用这种关系传播语义，避免重新训练一个大型语义编码器（§1、Fig.2）。

## 方法

1. **语义初始化（§3.2）。** 冻结 generalist VLM，采样可见视图的像素特征并加权聚合，得到初始逐点语义特征。语义标签来自模型表征，不由几何学生凭空生成。
2. **Geometric Contrastive Distillation（§3.3）。** 冻结 Sonata 提供关系空间，训练稀疏三维 CNN 学生。正负样本按教师特征相似性构造，同时加入全局负样本与空间近但特征不同的局部难负样本，用 InfoNCE 约束学生几何嵌入。
3. **关系而非逐向量回归。** 教师决定点对的关系，学生更新自己的嵌入；原文强调不是直接回归教师的每个特征向量。学生从三维几何产生几何嵌入（v2 §3.3），不能把它简单写成“把语义向量输入一个去噪MLP”。
4. **Geometry-Guided Pooling（§3.4）。** 在体素局部邻域内，以几何嵌入余弦相似度经 softmax 建稀疏亲和矩阵 `A`；迭代执行 `F_next = A × F_current`，最后映射回原始点。几何学生控制传播权重，语义特征是被传播内容。

## 实验 {#experiments}

【原文事实】Table 1 在约 1.5% 三维训练数据配置下，报告 ScanNetV2 **55.1 mIoU / 72.5 mAcc**，Matterport3D **40.2 / 62.4**。作者另列全量训练与既有论文结果，不能把这些行当作完全相同训练预算的控制实验。

Table 4 更直接支持净化模块的作用：

| ScanNetV2 配置 | mIoU | mAcc |
| --- | ---: | ---: |
| 聚合二维特征，不净化 | 50.2 | 68.1 |
| 加入 GeoPurify | 55.1 | 72.5 |
| 仅 macro 对比采样 | 53.5 | 70.8 |
| hybrid 对比采样 | 55.1 | 72.5 |

这些是原文结果，不是本站实验。语义教师、输入特征和推理模式与 SAS 不同，暂不放入统一排名。

## 局限

**版本内待核查差异：** §3.1 使用了“single pooling operation”的表述，但 §3.4 式(4)明确定义迭代，Table 4 的默认设置为 **T=18**，并比较 T=1、6、18、36。本文按操作定义与消融表解释为迭代传播；最终复现应再检查官方默认配置与代码，不擅自认定只有一次池化。

【分析推断】传播能修正局部不一致，但错误邻接也可能把语义错误扩散；几何相似不保证语义类别相同。少量训练场景的代表性、跨域教师几何先验和外部 VLM 质量均影响适用范围。附录 C 的子集选择实验可帮助分析稳定性，不能仅凭单个子集结果声称任意少样本均有效。

## 横向理解

OpenScene 学习与二维目标一致的三维语义嵌入；GeoPurify 学习几何关系并净化既有语义。SAS 的多教师融合也可减少噪声，但证据不足以直接断言二者组合必然提升效果。

## 开源情况

【官方文档说明】仓库有 `models/`、`config/`、`run/` 与数据处理代码，提供 ScanNet、Matterport3D 检查点入口。权重链接可见性不等于已完成下载验证。池化次数及学生输入的实现核查仍列为后续工作。

## 证据

| 主张 | 原始材料定位 |
| --- | --- |
| 教师学生与输入输出 | [v2 §3.1–3.3 / Fig.2](https://arxiv.org/html/2510.02186v2#S3) |
| 亲和矩阵与迭代传播 | [§3.4，式(3)–(4)](https://arxiv.org/html/2510.02186v2#S3.SS4) |
| 主实验与净化消融 | [§4，Table 1、4](https://arxiv.org/html/2510.02186v2#S4) |
| 子集与默认超参 | [Appendix A、C](https://arxiv.org/html/2510.02186v2#A1) |
| 实现与模型入口 | [官方仓库](https://github.com/tj12323/GeoPurify) |
