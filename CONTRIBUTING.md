# 参与贡献

欢迎完善 Image 2.5 提示词、真实出图案例、Skills 与 CLI。

[文档导航](docs/README.md) · [提交新资源](https://github.com/Fangx-AI/awesome-image2.5/issues/new?template=resource.yml) · [更正已有案例](https://github.com/Fangx-AI/awesome-image2.5/issues/new?template=correction.md)

不熟悉代码时，提交案例链接和修改建议即可。修改文档前先确认维护源：

| 想修改什么 | 编辑哪里 |
| --- | --- |
| 中英 README、31 类页面的公共结构 | `scripts/build_repository.py` |
| 分类写法、检查点、练习提示词 | `catalog/taxonomy.json` |
| 英文首页的分类说明 | `catalog/category-notes.en.json` |
| 本项目案例的观察记录 | `catalog/showcase-notes.json` |
| 本项目案例的公共展示结构 | `scripts/build_showcase.py` |
| 外部来源详情页的公共结构 | `scripts/build_image25_gallery.py` |
| 安装、工作流、FAQ | 对应的 `docs/*.md` |

修改生成器或维护源后统一运行 `python scripts/build_all.py`，再检查生成的差异。只修改生成后的 README 会被下次构建覆盖。

## 提交提示词或案例

优先选择明确场景，说明它解决的具体问题。新增实验提示词维护在 `catalog/recipes.json`，然后运行 `python scripts/build_all.py`；不要直接编辑生成的画廊或 Skill 提示词文件。

## 提交公开来源作品

请提供原始作品页、作者、公开图片地址、模型声明所在页、提示词入口与许可信息。没有完整提示词也可以提交有价值的作品，但必须明确缺失项。案例级模型证据优于仓库首页的泛化说明；仅凭标题、发布时间或画风不能确认型号。

人工整理的来源维护在 `catalog/web-image25.json`，社区采集维护在 `catalog/community-image25.json`，X 候选链接维护在 `catalog/x-seeds.json`。参照 [采集方法](docs/research.md) 选择证据标签。保留原作者地址，不将旧版案例或未知模型输出改标为 Image 2.5。

以下字段用于本项目自己的生成案例：

每个案例提供：
- 标题、分类、完整提示词。
- 精确模型名、生成日期、尺寸、质量与格式。
- 编辑案例的参考图顺序、输入来源及使用权限。
- 原始输出、必要的后处理说明。
- 状态：prompt-only / host-model-unknown / api-verified。
- 若宣称 api-verified，附去除私人信息的请求记录；不要提交 API Key。

自创提示词可以只提交文本，但不要标记为已验证案例。转载需保留作者、来源链接与许可；不要复制无授权的示例图。当前封面的来源说明见 [PROVENANCE](assets/PROVENANCE.md)。

## 修改代码与 Skill

使用 `uv sync` 安装开发环境，再运行 `uv run python -m unittest discover -s tests -v`。测试不调用付费接口。
更改模型参数时附官方文档来源。Skill 必须连同所需 references 一起可安装，不能依赖开发者机器上的绝对路径。

## 许可

提交者同意将原创贡献按本仓库 CC0 1.0 条款提供。第三方内容需单独标注适用许可。
