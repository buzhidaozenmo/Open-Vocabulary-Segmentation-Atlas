---
paper_id: drsplat
title: 'Dr. Splat: Directly Referring 3D Gaussian Splatting via Direct Language Embedding Registration'
short_name: Dr. Splat
authors:
- Kim Jun-Seong
- GeonU Kim
- Kim Yu-Ji
- Yu-Chiang Frank Wang
- Jaesung Choe
- Tae-Hyun Oh
year: 2025
preprint_date: unknown
venue: CVPR
publication_status: published
primary_direction: 3dgs
modalities:
- gaussian
- image
task_setting: open_vocabulary
task_types:
- language_field
techniques:
- semantic_alignment
- region_aggregation
- efficient_inference
datasets:
- LERF
- ScanNet
paper_url: https://openaccess.thecvf.com/content/CVPR2025/papers/Jun-Seong_Dr._Splat_Directly_Referring_3D_Gaussian_Splatting_via_Direct_Language_CVPR_2025_paper.pdf
publication_url: https://openaccess.thecvf.com/content/CVPR2025/html/Jun-Seong_Dr._Splat_Directly_Referring_3D_Gaussian_Splatting_via_Direct_Language_CVPR_2025_paper.html
code_status: public
code_url: https://github.com/kaist-ami/Dr-Splat
code_details: 官方仓库含预处理、特征登记、评测与运行脚本；需先有训练好的场景 3DGS 及外部 SAM／CLIP，未运行。
content_status: index
checked_on: '2026-11-09'
module_checked_on: '2026-11-09'
summary: 按渲染贡献直接登记高斯语言特征，以共享乘积量化码本支持三维文本查询。
sources:
- url: https://openaccess.thecvf.com/content/CVPR2025/html/Jun-Seong_Dr._Splat_Directly_Referring_3D_Gaussian_Splatting_via_Direct_Language_CVPR_2025_paper.html
  locator: 正式发表：出版方页面／DOI；期刊状态另由官方仓库文档确认
- url: https://openaccess.thecvf.com/content/CVPR2025/papers/Jun-Seong_Dr._Splat_Directly_Referring_3D_Gaussian_Splatting_via_Direct_Language_CVPR_2025_paper.pdf
  locator: 本次所读原文版本的 §3–5／III–V、方法图及主要结果表
- url: https://github.com/kaist-ami/Dr-Splat
  locator: 官方仓库实际目录与文档／项目页；未运行
figures:
- id: fig4
  label: Figure 4
  asset: assets/figures/drsplat-fig4.png
  page: 4
  version: CVPR 2025 出版方正式版
  source_url: https://openaccess.thecvf.com/content/CVPR2025/papers/Jun-Seong_Dr._Splat_Directly_Referring_3D_Gaussian_Splatting_via_Direct_Language_CVPR_2025_paper.pdf
  clip_pdf_points:
  - 55
  - 50
  - 558
  - 202
  source_sha256: a8104a9911992a50fc9130404bf78db1233ff198126a3796def4fc8a578066e1
methods:
- id: registration
  track: vocabulary
  problems:
  - alignment
  - regions
  title: 按渲染贡献直接登记高斯语言特征
  question: 不反复优化语言场，怎样把多视图语义赋给高斯？
  operation: 沿用 SAM 区域裁切获得 CLIP 特征；对每像素沿射线选贡献最大的 top-k 高斯，以透射率乘有效不透明度作为权重。跨掩码／跨视图累计各高斯的语义贡献，加权平均并归一化，直接登记到高斯。
  input: 已优化场景高斯、带位姿图像、区域 CLIP 特征
  output: 每高斯直接可查询的语言特征
  stage: 场景特征构建
  supervision: 预训练 CLIP、SAM 和已训练好的 3DGS；语言登记无梯度优化，不代表几何重建免训练
  origin: modified
  origin_note: 区域 CLIP 提取沿用 LangSplat；本文采用按高斯渲染贡献的直接登记。
  origin_refs:
  - url: https://arxiv.org/abs/2312.16084
    locator: §3.1 明确 Following LangSplat 提取区域 CLIP 特征
  evidence:
  - url: https://openaccess.thecvf.com/content/CVPR2025/papers/Jun-Seong_Dr._Splat_Directly_Referring_3D_Gaussian_Splatting_via_Direct_Language_CVPR_2025_paper.pdf
    locator: §3.1，Eq.3–6
  figure: fig4
  figure_guide: 独立登记图按 (a) Top-k 高斯映射→(b) 多视图加权聚合→(c) PQ 登记阅读。
  depicted: true
  route:
  - 二维区域特征
  - 渲染贡献语义登记
  - 高斯语言场
  - 文本相似度分类
- id: pq
  track: vocabulary
  problems:
  - alignment
  - efficiency
  title: 共享乘积量化码本支持直接三维查询
  question: 高维语言特征怎样压缩并保留文本查询能力？
  operation: 将 CLIP 向量划分多个子向量，在共享子码本中记录各自最近质心索引；以大规模实例图块特征构建码本，登记到不同场景时复用。文本查询时通过子空间质心距离查表组合，避免先渲染所有视图再搜索。
  input: CLIP 特征、共享 PQ 子码本、文本查询
  output: 压缩高斯语言索引与三维匹配
  stage: 离线码本构建、场景登记及查询
  supervision: LVIS 实例图块得到的预训练 CLIP 特征；场景几何需预先优化
  origin: modified
  origin_note: 乘积量化为沿用方法，本文将共享码本与高斯语言登记结合。
  origin_refs:
  - url: https://doi.org/10.1109/TPAMI.2010.57
    locator: 原文所引 Product Quantization for Nearest Neighbor Search，Jégou et al.
  evidence:
  - url: https://openaccess.thecvf.com/content/CVPR2025/papers/Jun-Seong_Dr._Splat_Directly_Referring_3D_Gaussian_Splatting_via_Direct_Language_CVPR_2025_paper.pdf
    locator: §3.2–3.3
  figure: fig4
  figure_guide: 该图 (c) 标出 Product Quantization 和 PQ indices；码本构建与查询查表没有完整展开，见 §3.2–3.3。
  depicted: true
  route:
  - 二维区域特征
  - 共享乘积量化索引
  - 高斯语言场
  - 直接三维文本查询
results:
- id: table1
  label: Table 1
  asset: assets/results/drsplat-table1.png
  page: 5
  version: CVPR 2025 出版方正式版
  source_url: https://openaccess.thecvf.com/content/CVPR2025/papers/Jun-Seong_Dr._Splat_Directly_Referring_3D_Gaussian_Splatting_via_Direct_Language_CVPR_2025_paper.pdf
  clip_pdf_points:
  - 55
  - 68
  - 558
  - 198
  source_sha256: a8104a9911992a50fc9130404bf78db1233ff198126a3796def4fc8a578066e1
  title: 语言驱动的高斯对象选择
  setting: LeRF-OVS；先选择三维高斯，再渲染选中对象，用二维分割衡量对象选择效果。
  metrics: mIoU ↑；mAcc @0.25 ↑
  reading: 这是三维选择后的二维投影评测，不等同于直接的三维体积 IoU；原表保留不同方法及选择变体。
---
# Dr. Splat

## 资料范围与状态

核查版本：CVPR 2025 出版方正式版；正式发表来源另见出版方链接。已完成与研究关注点有关的方法、配图和主结果表定向整理，尚未完成全文样例笔记。图中的方法关系以原文为准，未独立运行实现。

## 关注的问题

【原文事实】按渲染贡献直接登记高斯语言特征，以共享乘积量化码本支持三维文本查询。

## 实验阅读

LeRF-OVS；先选择三维高斯，再渲染选中对象，用二维分割衡量对象选择效果。 这是三维选择后的二维投影评测，不等同于直接的三维体积 IoU；原表保留不同方法及选择变体。 数值保留在原始结果表中；它们是论文报告值，不是本库复现值。

## 开源情况

【官方文档说明／项目页核查】官方仓库含预处理、特征登记、评测与运行脚本；需先有训练好的场景 3DGS 及外部 SAM／CLIP，未运行。 本轮没有安装依赖、执行训练或验证复现结果。
