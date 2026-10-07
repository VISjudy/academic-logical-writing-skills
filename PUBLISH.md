# 发布与后续更新

维护仓库：`VISjudy/academic-logical-writing-skills`。
仓库由用户创建；本次将完整技能包及维护文件导入 `main`。
原 `3dgs-paper-workbench` 仓库、分支和 PR 保持不变。

## 后续更新

1. 读取 [AGENTS.md](AGENTS.md) 和 [CONTRIBUTING.md](CONTRIBUTING.md)，确认变更范围。
2. 在克隆的仓库中新建工作分支，只修改相关技能和必要的索引、记录。
3. 执行 `python scripts/validate_all.py`；区分结构检查与尚未执行的模型行为测试。
4. 提交变更并推送工作分支，再创建 PR；不强推、不删除旧文件或历史分支。
5. 更新本机安装前先比较差异，明确备份或替换范围，不自动覆盖已有同名技能。

`PACKAGE_FILES.json` 是迁移时的完整性快照，不是要求后续所有文件永远不变。
`MIGRATION.json` 用于保留原始来源；后续实际修改应记录在 CHANGELOG 中。

## 保留的首次发布脚本

`scripts/publish_github.py` 是先前准备包的首次建仓工具，默认只预览，
仅在显式 `--publish --visibility public/private` 时尝试写入；它拒绝覆盖已有仓库。
**本仓库已由用户创建，不要用该脚本更新现有仓库。**
其目标名称已同步修正，保留该脚本仅用于追溯初始发布流程。

无需发送密码或明文 Token。授权和登录仅通过 GitHub 官方流程完成。
