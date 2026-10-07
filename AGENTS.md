# Academic Logical Writing Skills — 维护约定

## 范围
本仓库 `VISjudy/academic-logical-writing-skills` 是科研写作类skill的维护位置；将技能源放在 `skills/<skill-name>/`。
不要自动同步到旧的3dgs-paper-workbench仓库，不删除或合并旧PR。

## 维护
- 先读目标skill的SKILL.md、README与CHANGELOG，再修改相关文件。
- 保留用户确认的写作内容与审查规则；局部反馈不能被扩大为通用硬性要求。
- 通用规则、领域案例、学术文献快照分开；不把旧案例中的论断当作当前科研事实。
- 新规则应记录反馈、反例、适用范围与行为验收用例；更新根目录索引及对应CHANGELOG。
- 不添加只有名称、没有内容的技能；未提供能力不得标为已支持。
- 脚本不存凭据，不索取明文token，不默认联网执行或修改全局agent配置。
- 删除、不可恢复覆盖、force-push、修改原仓库前，必须取得针对具体对象的用户确认。

## 验证
提交前执行 `python scripts/validate_all.py`，检查本地链接与元数据。
区分结构测试、复制安装测试、模型行为测试与用户机器加载测试；未执行的项目应明确注明。
只有实际创建并回读确认远程仓库与提交后，才报告已发布。
