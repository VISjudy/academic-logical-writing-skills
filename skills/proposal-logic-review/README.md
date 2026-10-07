# Proposal Logic Review｜研究计划书写作与逻辑审查

独立仓库分发版：1.0.2。核心写作规则与1.0.0保持一致；保留1.0.1的完整安装器与展示配置。

维护位置：`VISjudy/academic-logical-writing-skills` 的 `skills/proposal-logic-review/`。
后续该技能在本仓库维护；原工作台仓库中的版本保留为历史来源。

**先检查目标—进展—Gap—问题—方法—验证为什么相连，再修改文字。**

## 安装与调用

在已发布的仓库中，可向支持 skill-installer 的本地 Codex 输入：

```text
$skill-installer
从以下目录安装完整的 proposal-logic-review：
https://github.com/VISjudy/academic-logical-writing-skills/tree/main/skills/proposal-logic-review
保留整个目录及所有相对引用文件。已有同名技能时先比较并询问，不要覆盖。
```

也可克隆独立仓库后运行：

```bash
python skills/proposal-logic-review/scripts/install_local.py
```

安装器默认复制至 `~/.agents/skills/proposal-logic-review`，支持 `--destination`，
不联网、不删除、不覆盖已有安装，也不改动全局 `AGENTS.md` 或 `config.toml`。
请在运行 Codex 的同一操作系统和用户环境下安装；Windows 与 WSL 目录不同。

```text
$proposal-logic-review
先检查我的 proposal 各部分之间的逻辑连接，指出最多三个关键断点，不立即改写全文。
```

完整文件和结构校验成功不代表已经在用户电脑上成功加载，也不代表通过了模型行为评估。
官方使用与目录依据（核对日期2026-10-07）：https://developers.openai.com/codex/skills

## 使用模式

### 梳理主线

> 按 proposal-logic-review 的 SKILL.md，以梳理模式处理我的草稿。先确认目标—已有进展—Gap—科学问题之间的连接，每个连接用一句话表达。不要立即扩写完整 proposal。

### 严格审查

> 按这个 skill 审查我的 proposal。只把稿件已经写出的内容当成论据，不能用我的背景替它补洞。先指出最多三个最影响成立性的逻辑断点，逐项给出原句、缺失前提、关键追问和最小修订。区分缺证据与已证伪。

### 导师式拷问

> 按这个 skill 逐轮追问。每次只问一个最关键的问题，从“为什么这个目标需要这种研究”开始；我回答后再判断能否进入下一层，不要直接替我发明结论。

### 写完整稿

> 按这个 skill，根据我已确认的主线写中英文 proposal。正文各两页，参考文献不计页数。保持已确认段落，方法逐项对应科学问题，详细审查笔记不要进入正文。

### 局部润色

> 只压缩选中段落，保留含义、证据范围和承诺程度。不要修改其他部分或重开已确定主线。

## 文件说明

| 文件 | 用途 |
|---|---|
| `SKILL.md` | 触发范围、工作模式、核心规则和交付检查 |
| `references/writing-playbook.md` | 页内结构、过渡句、凝练原则、双语与版本控制 |
| `references/review-protocol.md` | 证据、逻辑、方法对应、公平验证和追问协议 |
| `references/urban-3dgs-case.md` | 本篇 proposal 的写法解读、链条、例句和修订反例 |
| `references/source-ledger.md` | 依据文件、来源定位、派生规则与隐私说明 |
| `templates/argument-workbook.md` | 主张—依据—问题—方法—验证及锁定内容工作表 |
| `templates/two-page-proposal.md` | 可替换的中英文正式稿骨架 |
| `templates/review-report.md` | 最多三项核心缺陷的审查报告格式 |
| `templates/blind-review-brief.md` | 仅在实际支持隔离委派时使用的评审包 |
| `examples/approved-excerpts.md` | 当前确认稿的中英文节选和共用参考文献快照 |
| `evals/behavior-tests.md` | 检验 skill 是否重犯历史错误的情景用例 |
| `scripts/validate_package.py` | 检查入口格式、目录链接和模板基本完整性，不评判科研质量 |
| `CHANGELOG.md` | 版本与修订记录 |

## 核心判断

好的 proposal 不需要预先知道答案，却必须说明：问题为何值得研究、现有证据尚不足以决定什么、为什么候选方法可能有效，以及什么结果会支持或削弱这一解释。

本案例文献及工具名称只作为作者确认版本中的写法示例。本次不重新核验这些文献，也不把它们固化为最新 SOTA。复用时应按实际任务和检索权限更新。
