---
paper_id: replace_with_stable_id
title: 待填写完整标题
short_name: 待填写简称
authors: []
year: 2026
preprint_date: unknown
venue: arXiv
publication_status: preprint
primary_direction: 2d
modalities: [image]
task_setting: open_vocabulary
task_types: [semantic]
techniques: []
datasets: []
paper_url: https://arxiv.org/abs/REPLACE
publication_url: ''
code_status: unconfirmed
code_url: ''
code_details: 尚未核实；不能根据论文的代码链接判断已经发布
content_status: index
checked_on: '2026-11-09'
summary: 用一句话说明研究问题与方法，缺少原文时不补写技术细节
module_checked_on: '2026-11-09'
figures:
  - id: fig2
    asset: assets/figures/REPLACE-fig2.png
    label: Figure 2
    page: 3
    version: 待填写精确 PDF 版本
    source_url: https://arxiv.org/pdf/REPLACEv1
    clip_pdf_points: [0, 0, 100, 100]
    source_sha256: 待填写下载 PDF 的 SHA256
methods:
  - id: replace_module_id
    track: vocabulary  # vocabulary / pointcloud；混合模态逐模块归类
    problems: [alignment]  # 受控问题见 scripts/methods.py PROBLEMS
    title: 待填写相关模块
    question: 待填写与你的研究有关的具体问题
    operation: 待填写实际计算、选择、对应或聚合步骤；不能只填技术名
    input: 待填写
    output: 待填写
    stage: 训练／推理／离线构建；按原文填写
    supervision: 必要标注、教师或预训练信息
    origin: unverified  # proposed / reused / modified / unverified
    origin_note: 说明本文设计与沿用部分；未核实归属明确保留
    origin_refs: []  # 沿用模块必须填写原始引用的 url 和 locator
    evidence:
      - url: https://arxiv.org/pdf/REPLACEv1
        locator: 原文章节、公式或图号
    figure: fig2
    depicted: true  # 没有画出该操作时 false，图解中如实说明
    figure_guide: 看哪个区域、连接路径；若操作未画出，明确指出
    route: [语义来源, 相关操作, 输出表示, 预测或用途]  # 替换为具体规范化标签
    result_tables: [table1]  # 可省略；省略时展示本论文全部主结果表
    # 几何相关模块可增加以下字段，填写后自动进入几何专题；分类见 scripts/geometry.py。
    # geometry:
    #   families: [pretrained, affinity]
    #   signal: 几何信号的具体来源或模型
    #   mechanism: 如何对应、计算、聚合或约束
    #   changes: 改变的特征、权重、边、区域或损失
    #   stage: 预训练／训练／推理
    #   semantic_role: 类别语义来自哪里；几何负责什么
    #   route: [几何来源, 使用方式, 改变的表示, 参与环节]
    #   evidence:
    #     - url: https://arxiv.org/pdf/REPLACEv1
    #       locator: 几何操作的章节、公式及引用来源
results:
  - id: table1
    label: Table 1
    asset: assets/results/REPLACE-table1.png
    title: 待填写主结果表的任务
    setting: 数据集、划分、监督、骨干或速度硬件条件；按原文填写
    metrics: 指标及方向，例如 mIoU ↑；延迟 ms ↓
    reading: 该看哪一行与哪些同设置基线，不编造总排名
    page: 5
    version: 待填写精确 PDF 版本
    source_url: https://arxiv.org/pdf/REPLACEv1
    clip_pdf_points: [0, 0, 100, 100]
    source_sha256: 待填写下载 PDF 的 SHA256
sources:
  - url: https://arxiv.org/abs/REPLACE
    locator: 待填写原文版本、章节或图表
---
# 待填写论文简称

## 资料范围与版本

原文版本、正式发表来源、实际检查的代码范围。未运行实验时明确说明。

## 任务

输入、输出、训练监督与推理输入；区分开放词汇、指代、提示及开放集设置。

## 研究问题

【原文事实】作者观察到的具体问题与证据。

## 方法

流程、模块输入输出、教师学生、冻结与更新参数、训练损失、推理流程。

## 实验

数据集版本、划分、类别、指标、训练数据、推理输入；结果对应原文表号。

## 局限

原文明确局限与【分析推断】分开。未核实的实现和协议列入待核查项。

## 横向理解

有证据的方法关系；技术相似性不等于继承，不据此断言创新性。

## 证据

| 主张 | 来源与定位 | 核查范围 |
| --- | --- | --- |
| 待填写 | 原文 § / Fig. / Table | 原文 / 官方文档 / 实际代码 |
