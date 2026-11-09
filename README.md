# Open-Vocabulary Segmentation Research Atlas

以 3D 点云为重点的中文开放词汇分割科研知识库：梳理研究问题、方法、评测设置与有证据的技术关系。

**[浏览知识库网站 →](https://buzhidaozenmo.github.io/Open-Vocabulary-Segmentation-Atlas/)**

[![Build & Deploy](https://github.com/buzhidaozenmo/Open-Vocabulary-Segmentation-Atlas/actions/workflows/pages.yml/badge.svg)](https://github.com/buzhidaozenmo/Open-Vocabulary-Segmentation-Atlas/actions/workflows/pages.yml)

## 当前内容

- 首批 15 篇论文索引，涵盖 3D、2D、视频、多视角与 3DGS。
- 5 篇带原文版本、章节/表格定位的样例笔记：OpenScene、SAS、GeoPurify、CorrCLIPv2、EOVSAM。
- 组合筛选、全文搜索、研究时间线、技术矩阵、横向比较及评测协议说明。
- 目标约 100 篇；未精读、代码未确认、预印本等状态均明确标注。

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

用 `templates/paper_template.md` 新建论文，保持稳定 `paper_id`，填写真实来源后运行构建。网站统计、列表、时间线、矩阵均自动更新，不另行手改汇总列表。

GitHub Pages 使用 Actions 部署；仓库 About 的 Website 与本 README 指向相同地址。构建失败时保留上一次成功部署。

## 证据与版权

笔记区分原文事实、官方文档说明、分析推断和待验证问题。引用结果均是论文报告值，不是本仓库复现值。正式出版版本与所读预印本版本分别记录。

本仓库不分发论文 PDF、数据集或模型权重；原文和代码遵循各自许可。原创笔记与脚本的使用许可见 [LICENSE](LICENSE)。
