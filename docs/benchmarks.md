# 数据集与评测

## 先对齐协议，再比较数字

本版只在各论文笔记中保留有原文表号的结果，**尚未建立跨论文排行榜**。例如 SAS 与 GeoPurify 的3D训练规模、二维教师、推理输入不同，不能把 mIoU 放在同一列就认为公平。

| 必须核对的项目 | 常见误区 |
| --- | --- |
| 数据集版本与划分 | ScanNet v2 和 ScanNet200 混用；validation 与 test 混用 |
| 类别集合、忽略类别与映射 | 20类与4类未见类别、21类与160类；忽略背景的 f-mIoU 与全类 mIoU |
| 任务与指标 | 语义 mIoU、实例 AP、全景 PQ、概念提示指标混排 |
| 训练监督与数据规模 | 无3D语义标签误写成无监督；忽略基础模型预训练或外部记忆库 |
| Backbone与教师 | 更强教师或更多预训练来源被误归因于单个模块 |
| 推理输入与后处理 | 纯3D蒸馏、2D融合、2D–3D集成；SAM后处理或oracle类别过滤 |
| 效率测量 | 硬件、分辨率、词表大小、精度、离线建库与在线成本不同 |

## 首批数据集入口

| 数据集 / 集合 | 主要用途 | 首轮核查提醒 |
| --- | --- | --- |
| [ScanNet](https://www.scan-net.org/) | 室内RGB-D与三维分割 | 区分v2/200、训练监督、4类与全类、语义与实例 |
| [Matterport3D](https://niessner.github.io/Matterport/) | 建筑多视角与三维理解 | 记录原始类别与NYU长尾映射；mAcc与mIoU分开 |
| [nuScenes](https://www.nuscenes.org/) | 室外多传感器驾驶场景 | 核对具体类别映射、提示词和LiDAR/RGB使用方式 |
| [ADE20K](https://ade20k.csail.mit.edu/) | 图像语义与全景分割 | 150/847类，以及语义mIoU与全景PQ分开 |
| [PASCAL Context](https://cs.stanford.edu/~roozbeh/pascal-context/) | 图像语义分割 | 59/60/459类；与VOC20/21分开 |
| [COCO](https://cocodataset.org/) | 多种训练和评测任务 | Stuff、Panoptic、Object不是同一协议 |
| [LV-VIS](https://github.com/haochenheheda/LVVIS) | 大词汇视频实例分割 | 记录已见/未见类别、AP与跟踪设置 |

以上为官方入口与协议核查清单，详细规模与版本需在数据集专页中逐项核实后补充。

## 已有结果证据入口

- [OpenScene：Table 4的三种特征模式](papers/openscene.md#experiments)
- [SAS：Table 3的融合与蒸馏消融](papers/sas.md#experiments)
- [GeoPurify：Table 4的净化与采样消融](papers/geopurify.md#experiments)
- [CorrCLIPv2：Table 6的检索与集成消融](papers/corrclipv2.md#experiments)
- [EOVSAM：Table 1和Table 4](papers/eovsam.md#experiments)

统一实验记录模板位于仓库 `templates/benchmark_template.yaml`。只有协议核查完成的条目才能分配同一比较组；未核实值保留空值，不能填0。
