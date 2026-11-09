# Open-Vocabulary Segmentation Research Atlas

以 3D 点云为重点的中文开放词汇分割科研知识库：梳理研究问题、方法、评测设置与有证据的技术关系。

**[浏览知识库网站 →](https://buzhidaozenmo.github.io/Open-Vocabulary-Segmentation-Atlas/)**

[![Build & Deploy](https://github.com/buzhidaozenmo/Open-Vocabulary-Segmentation-Atlas/actions/workflows/pages.yml/badge.svg)](https://github.com/buzhidaozenmo/Open-Vocabulary-Segmentation-Atlas/actions/workflows/pages.yml)

<!-- PAPERS:START -->

## 论文目录

当前收录 **15 篇论文**，其中 **5 篇样例笔记**。可以直接在 GitHub 阅读下方分类清单、打开原论文和官方代码，或进入仓库内的笔记。

[3D 点云](#papers-3d) | [2D 图像](#papers-2d) | [视频](#papers-video) | [RGB-D / 多视角](#papers-multiview) | [NeRF / 3DGS](#papers-3dgs)

✅ 已查到实际官方实现；❔ 尚未确认官方代码。代码状态不代表已完成运行或复现。预印本单独标注；“索引”表示尚未完成样例级整理。

<a id="papers-3d"></a>

### 3D 点云 · 7 篇

| 论文 | 发表 | 研究内容 | 官方代码与开放情况 | 笔记 |
| --- | --- | --- | --- | --- |
| **GeoGuide**<br>[GeoGuide: Hierarchical Geometric Guidance for Open-Vocabulary 3D Semantic Segmentation](https://arxiv.org/abs/2603.26260) | [CVPR 2026](https://openaccess.thecvf.com/content/CVPR2026/html/Tao_GeoGuide_Hierarchical_Geometric_Guidance_for_Open-Vocabulary_3D_Semantic_Segmentation_CVPR_2026_paper.html) | 从超点、实例内部和实例之间建立几何语义一致性。 | ❔ 尚未找到可核实的官方公开实现入口；不能据此断言作者明确不开源。 | [索引](docs/papers/geoguide.md) |
| **GeoPurify**<br>[GeoPurify: A Data-Efficient Geometric Distillation Framework for Open-Vocabulary 3D Segmentation](https://arxiv.org/abs/2510.02186) | [ICLR 2026](https://proceedings.iclr.cc/paper_files/paper/2026/hash/039bc8e424e1fc196b4203555b54ebc4-Abstract-Conference.html) | 通过几何关系蒸馏与几何引导池化，净化投影到三维的语义特征。 | ✅ [Code](https://github.com/tj12323/GeoPurify)<br>公开模型、配置、训练和评测脚本；提供ScanNet与Matterport3D检查点入口。 | [样例笔记](docs/papers/geopurify.md) |
| **SAS**<br>[SAS: Segment Any 3D Scene with Integrated 2D Priors](https://arxiv.org/abs/2503.08512) | [ICCV 2025](https://openaccess.thecvf.com/content/ICCV2025/html/Li_SAS_Segment_Any_3D_Scene_with_Integrated_2D_Priors_ICCV_2025_paper.html) | 对齐多个二维教师，估计类别能力并融合，再以超点与自蒸馏训练三维模型。 | ✅ [Code](https://github.com/peoplelu/SAS)<br>公开能力构建、特征提取融合与分阶段训练实现；提供预处理特征入口，依赖多个外部教师模型。 | [样例笔记](docs/papers/sas.md) |
| **RegionPLC**<br>[RegionPLC: Regional Point-Language Contrastive Learning for Open-World 3D Scene Understanding](https://arxiv.org/abs/2304.00962) | [CVPR 2024](https://openaccess.thecvf.com/content/CVPR2024/papers/Yang_RegionPLC_Regional_Point-Language_Contrastive_Learning_for_Open-World_3D_Scene_Understanding_CVPR_2024_paper.pdf) | 以区域级语言监督与对比学习建立更密集的三维语言关联。 | ✅ [Code](https://github.com/CVMI-Lab/PLA/tree/regionplc)<br>实际实现位于 regionplc 分支；与 PLA 主分支分开。 | [索引](docs/papers/regionplc.md) |
| **OpenMask3D**<br>[OpenMask3D: Open-Vocabulary 3D Instance Segmentation](https://arxiv.org/abs/2306.13631) | [NeurIPS 2023](https://proceedings.neurips.cc/paper_files/paper/2023/hash/d77b5482e38339a8068791d939126be2-Abstract-Conference.html) | 用类别无关三维实例掩码和多视角区域特征进行开放词汇实例分割。 | ✅ [Code](https://github.com/OpenMask3D/openmask3d)<br>公开特征提取、聚合与评测流程；依赖3D掩码模型、SAM等外部权重。 | [索引](docs/papers/openmask3d.md) |
| **OpenScene**<br>[OpenScene: 3D Scene Understanding with Open Vocabularies](https://arxiv.org/abs/2211.15654) | [CVPR 2023](https://openaccess.thecvf.com/content/CVPR2023/html/Peng_OpenScene_3D_Scene_Understanding_With_Open_Vocabularies_CVPR_2023_paper.html) | 多视角二维特征如何成为可供文本查询的三维点特征。 | ✅ [Code](https://github.com/pengsongyou/openscene)<br>官方实现包含多视角融合、3D蒸馏与评测；提供预训练模型及预处理特征入口。 | [样例笔记](docs/papers/openscene.md) |
| **PLA**<br>[PLA: Language-Driven Open-Vocabulary 3D Scene Understanding](https://arxiv.org/abs/2211.16321) | [CVPR 2023](https://github.com/CVMI-Lab/PLA) | 通过点云与语言关联构建三维开放词汇能力，作为蒸馏路线的对照。 | ✅ [Code](https://github.com/CVMI-Lab/PLA)<br>官方 main 分支包含实现；有数据准备、训练推理及模型文档。具体监督设置待精读。 | [索引](docs/papers/pla.md) |

<a id="papers-2d"></a>

### 2D 图像 · 3 篇

| 论文 | 发表 | 研究内容 | 官方代码与开放情况 | 笔记 |
| --- | --- | --- | --- | --- |
| **CorrCLIPv2**<br>[CorrCLIPv2: Harnessing Unlabeled Images for Open-Vocabulary Semantic Segmentation](https://arxiv.org/abs/2610.24757) | [IJCV 2026](https://link.springer.com/article/10.1007/s11263-026-03027-3) | 重建CLIP相关性，以无标注图像记忆库与多CLIP集成缓解上下文偏差。 | ✅ [Code](https://github.com/zdk258/CorrCLIP/tree/master/CorrCLIPv2)<br>CorrCLIPv2 子目录已提供实际实现、配置、评测和记忆库相关说明。 | [样例笔记](docs/papers/corrclipv2.md) |
| **EOVSAM**<br>[EOVSAM: Efficient Open-Vocabulary Segmentation with SAM 3 in One Pass](https://arxiv.org/abs/2608.02284) | arXiv 2026<br>**预印本** | 将SAM3适配为单次前向掩码生成器，以注意力聚合支持开放词汇识别。 | ✅ [Code](https://github.com/hustvl/EOVSAM)<br>官方仓库提供训练与语义/全景评测配置、模型入口和SAM3基线流程；未独立验证下载与运行。 | [样例笔记](docs/papers/eovsam.md) |
| **SAM3**<br>[SAM 3: Segment Anything with Concepts](https://arxiv.org/abs/2511.16719) | [ICLR 2026](https://proceedings.iclr.cc/paper_files/paper/2026/hash/e0982cbc81401df3430ee1ff780dc7a2-Abstract-Conference.html) | 通过文本概念或图像示例分割匹配实例，并支持视频中的身份跟踪。 | ✅ [Code](https://github.com/facebookresearch/sam3)<br>提供推理、微调、示例与检查点入口；权重需按官方访问与许可流程获取。 | [索引](docs/papers/sam3.md) |

<a id="papers-video"></a>

### 视频 · 2 篇

| 论文 | 发表 | 研究内容 | 官方代码与开放情况 | 笔记 |
| --- | --- | --- | --- | --- |
| **EntitySAM**<br>[EntitySAM: Segment Everything in Video](https://openaccess.thecvf.com/content/CVPR2025/papers/Ye_EntitySAM_Segment_Everything_in_Video_CVPR_2025_paper.pdf) | [CVPR 2025](https://openaccess.thecvf.com/content/CVPR2025/papers/Ye_EntitySAM_Segment_Everything_in_Video_CVPR_2025_paper.pdf) | 以SAM2扩展自动发现和跟踪视频实体；作为类别无关相关任务参考。 | ✅ [Code](https://github.com/ymq2017/entitysam)<br>训练代码、评测代码和检查点已发布；核心任务不是文本类别驱动的OVSS。 | [索引](docs/papers/entitysam.md) |
| **TROY-VIS**<br>[Towards Real-Time Open-Vocabulary Video Instance Segmentation](https://arxiv.org/abs/2412.04434) | [WACV 2025](https://openaccess.thecvf.com/content/WACV2025/papers/Yan_Towards_Real-Time_Open-Vocabulary_Video_Instance_Segmentation_WACV_2025_paper.pdf) | 通过解耦特征增强、文本缓存与时序插值平衡视频分割精度和速度。 | ✅ [Code](https://github.com/google-research/troyvis)<br>提供实际实现、训练测试文档与模型列表入口。 | [索引](docs/papers/troyvis.md) |

<a id="papers-multiview"></a>

### RGB-D / 多视角 · 2 篇

| 论文 | 发表 | 研究内容 | 官方代码与开放情况 | 笔记 |
| --- | --- | --- | --- | --- |
| **OTAS**<br>[OTAS: Open-vocabulary Token Alignment for Outdoor Segmentation](https://arxiv.org/abs/2507.08851) | [ICRA 2026](https://github.com/SimonSchwaiger/otas) | 在单视图或多视图中对齐基础模型token，建立室外可查询语义表示。 | ✅ [Code](https://github.com/SimonSchwaiger/otas)<br>官方仓库包含核心模型、推理、检查点下载脚本、演示与ROS 2接口；ICRA录用由作者仓库公告确认。 | [索引](docs/papers/otas.md) |
| **OV-Octree-Graph**<br>[Open-Vocabulary Octree-Graph for 3D Scene Understanding](https://arxiv.org/abs/2411.16253) | [ICCV 2025](https://openaccess.thecvf.com/content/ICCV2025/html/Wang_Open-Vocabulary_Octree-Graph_for_3D_Scene_Understanding_ICCV_2025_paper.html) | 融合RGB-D序列的区域与实例特征，以八叉树图表达三维语义。 | ✅ [Code](https://github.com/yifeisu/OV-Octree-Graph)<br>公开实例构建、特征聚合及运行脚本；需外部二维模型与依赖。 | [索引](docs/papers/octreegraph.md) |

<a id="papers-3dgs"></a>

### NeRF / 3DGS · 1 篇

| 论文 | 发表 | 研究内容 | 官方代码与开放情况 | 笔记 |
| --- | --- | --- | --- | --- |
| **LangSplatV2**<br>[LangSplatV2: High-dimensional 3D Language Gaussian Splatting with 450+ FPS](https://arxiv.org/abs/2507.07136) | [NeurIPS 2025](https://langsplat-v2.github.io/) | 用高效的高维语言高斯表示改善场景文本查询的精度与速度。 | ✅ [Code](https://github.com/ZhaoYujie2002/LangSplatV2)<br>官方仓库提供预处理、训练、多个数据集评测流程及模型/数据入口。 | [索引](docs/papers/langsplatv2.md) |

## 数据集与方法比较

- [数据集与评测设置](docs/benchmarks.md)
- [五篇样例的方法比较](docs/insights.md)
- [研究地图与技术矩阵](https://buzhidaozenmo.github.io/Open-Vocabulary-Segmentation-Atlas/atlas/)

最近核查：**2026-11-09**。目标约100篇，后续按研究方向持续扩展。

<!-- PAPERS:END -->

## 本地浏览

需要 Python 3.11 或更新版本。在仓库根目录运行：

```bash
python3 -m venv .codex_tmp/venv
.codex_tmp/venv/bin/pip install --cache-dir .codex_tmp/pip-cache -r requirements.txt
.codex_tmp/venv/bin/python scripts/build.py --serve
```

打开 <http://127.0.0.1:8000/>。浏览器需要 HTTP 服务；不要直接双击构建产物。修改源文件后重新运行命令以刷新汇总数据。

```bash
# 校验元数据、证据和关系，再严格构建
.codex_tmp/venv/bin/python scripts/build.py --check
```

## 内容维护

| 路径 | 用途 |
| --- | --- |
| `docs/papers/` | 每篇论文的唯一数据源：YAML 元数据 + Markdown 笔记 |
| `data/` | 受控技术词表、数据集与论文关系 |
| `templates/` | 论文、方法和评测记录模板 |
| `scripts/` | 校验与页面生成 |
| `.github/workflows/pages.yml` | 推送 main 后校验、构建、发布 GitHub Pages |
| `.codex_tmp/` | 本地依赖、源文缓存、预览和构建产物，已忽略 |

用 `templates/paper_template.md` 新建论文，保持稳定 `paper_id`，填写真实来源后运行：

```bash
.codex_tmp/venv/bin/python scripts/update_readme.py
.codex_tmp/venv/bin/python scripts/build.py --check
```

README 的分类清单和网站使用同一份论文元数据。更新脚本只替换清单区，保留其他说明；构建会检查二者是否同步。

GitHub Pages 使用 Actions 部署；仓库 About 的 Website 与本 README 指向相同地址。构建失败时保留上一次成功部署。

## 证据与版权

笔记区分原文事实、官方文档说明、分析推断和待验证问题。引用结果均是论文报告值，不是本仓库复现值。正式出版版本与所读预印本版本分别记录。

本仓库不分发论文 PDF、数据集或模型权重；原文和代码遵循各自许可。原创笔记与脚本的使用许可见 [LICENSE](LICENSE)。
