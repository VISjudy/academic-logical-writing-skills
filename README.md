# Academic Logical Writing Skills｜学术逻辑写作技能库

集中维护研究计划书、论文写作、文献综述与审稿回复等科研写作技能。
当前提供 **proposal-logic-review**；其他类别为后续扩展范围，不代表已经实现。

**检查目标—现状—Gap—科学问题—方法—验证为什么相连，再修改文字。**

## 技能目录

| Skill | 用途 | 入口 |
|---|---|---|
| proposal-logic-review | 主线梳理、两页 proposal、中英文写作、导师式追问、逻辑审查与局部修订 | [SKILL.md](skills/proposal-logic-review/SKILL.md) · [使用说明](skills/proposal-logic-review/README.md) |

## 在本地 Codex 安装

在支持 skill-installer 的 Codex 对话中输入：

```text
$skill-installer
请从以下 GitHub 目录安装完整的 proposal-logic-review：
https://github.com/VISjudy/academic-logical-writing-skills/tree/main/skills/proposal-logic-review
保留整个目录及相对引用文件。已有同名技能时，先比较并询问，不直接覆盖。
安装完成后报告实际路径。
```

也可克隆本仓库后，运行仅做本地复制的安装器：

```bash
git clone https://github.com/VISjudy/academic-logical-writing-skills.git
cd academic-logical-writing-skills
python skills/proposal-logic-review/scripts/install_local.py
```

安装器默认复制到 `~/.agents/skills/proposal-logic-review`，拒绝覆盖已有目录，不修改全局配置。
Windows 可使用 `py`，macOS/Linux 可使用 `python3`；请在运行 Codex 的同一系统和用户环境操作。
仓库上传不等于已经安装或更新了本机技能。

## 调用示例

```text
$proposal-logic-review
审查我的 proposal。先解释目标—现状—Gap—科学问题—方法—验证之间的每个连接，
每个连接用一句话表达。最多指出三个关键逻辑断点，不立即重写全文。
```

完整模式、排查说明和模板见[技能说明](skills/proposal-logic-review/README.md)。

## 后续维护

每个新技能放入 `skills/<skill-name>/`，独立维护 `SKILL.md`、必要的参考材料、模板与验收用例。
通用规则、领域案例及文献快照分别保存；修订需记录反馈、反例和适用边界。
当前只迁移 proposal-logic-review，不自动复制旧仓库中的其他技能。
维护约定见 [AGENTS.md](AGENTS.md)，贡献流程见 [CONTRIBUTING.md](CONTRIBUTING.md)。

```bash
python scripts/validate_all.py
```

结构检查不等于模型行为测试、科研事实核查或用户本机加载测试。
不提交凭据、原始简历、申请表、未公开论文全文、个人邮件或大型研究数据。
本仓库保留已授权技能包中的范例，不新增这些原始材料；未擅自添加开源许可证。

## 来源与迁移

原来源为 `VISjudy/3dgs-paper-workbench` 的 `add-proposal-logic-review` 分支，
提交 `cc1043fabee51898a7af764d78cf4efc6818d7ef`。
核心写作与审查规则不变；本仓库名称、安装链接及维护入口按用户要求更新。
原仓库、分支与 PR 不作修改，也不自动双向同步。

[MIGRATION.json](MIGRATION.json) 记录来源与保留文件哈希；
[PACKAGE_FILES.json](PACKAGE_FILES.json) 为本次迁移快照的文件校验清单。
更新发布流程见 [PUBLISH.md](PUBLISH.md)。
