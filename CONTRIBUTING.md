# 参与贡献

欢迎完善 Image 2.5 提示词、真实出图案例、Skills 与 CLI。

## 提交提示词或案例

优先选择明确场景，说明它解决的具体问题。新增提示词放在 `skills/image25/references/prompts/`，并在 [画廊](skills/image25/references/gallery.md) 中添加条目。

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
