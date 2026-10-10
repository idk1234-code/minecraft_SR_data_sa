# 复现与 GitHub 发布说明

本摘要位于 [idk1234-code/minecraft_SR_data_sa](https://github.com/idk1234-code/minecraft_SR_data_sa)。所有文档和图的内部链接均使用相对路径。

摘要包包含结案说明、成就清单、两组证据表、第二组距离数组、种子清单、规则和校验文件。`python tools/verify_summary.py` 只读检查这些材料。

完整训练和地图生成复现使用两个完整研究包，作为 [阶段结案 Release](https://github.com/idk1234-code/minecraft_SR_data_sa/releases/tag/biome-search-2026-10-11) 的附件保存，名称和校验见 [附件记录](../data/reproduction_release_assets.json)：

- [模块及单目标研究复现包](https://github.com/idk1234-code/minecraft_SR_data_sa/releases/download/biome-search-2026-10-11/modular_single_target_reproduction.zip)
- [完整 1 万格长距离研究复现包](https://github.com/idk1234-code/minecraft_SR_data_sa/releases/download/biome-search-2026-10-11/longhaul_single_target_reproduction.zip)

这些大型包没有重复放入摘要仓库。GitHub 对大文件的处理方式见 [官方说明](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github)。

第二组固定搜索器的补充配对检验可运行 `python tools/review_fixed_experts.py` 重算，依赖 numpy 和 scipy；不会运行新地图或训练。重算使用公开的 `data/validation_b_arrays.npz`。

本摘要的模拟预算、视野和群系家族定义必须与发现率一起引用。原版 1.16.1 成就清单只校验了进度要求，不把模拟发现率升级为实际客户端完成率。
