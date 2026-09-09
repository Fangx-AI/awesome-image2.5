# 社区来源与学习入口

[返回首页](../README.md)

只把能追溯的来源列入本页；作者的模型声明与本项目独立实测分开记录。第三方图片和长提示词留在原站，版权归原作者。

| 来源 | 可以学到什么 | 证据范围 |
| --- | --- | --- |
| [OpenAI Images 2.5 发布页](https://openai.com/index/introducing-chatgpt-images-2-5/) | 参考主体保持、局部修改与多轮编辑 | 官方演示；并非本项目实测 |
| [Simon Willison 的 Sunburst 实践](https://simonwillison.net/2026/Sep/8/introducing-chatgpt-images-25/) | 为现有图表增加角色，附输入、结果与命令 | 作者明确使用 gpt-image-2.5-sunburst |
| [UI 生成对比讨论](https://www.reddit.com/r/codex/comments/1wb8p1g/gpt_image_25_comparison_for_ui_generation/) | 观察不同模型与质量档的 UI 输出 | 社区作者对比，非受控基准 |
| [Axios 编辑体验](https://www.axios.com/2026/09/08/exclusive-hands-on-with-chatgpts-new-image-editor) | 宠物参考图跨风格编辑 | 媒体作者体验 |
| [GPT-Image2-Skill](https://github.com/wuyoscar/GPT-Image2-Skill) | 分类组织、案例展示及工作流设计 | 参考项目；不将旧模型案例改标为 2.5 |

## 可复用的来源采集

运行前安装 GitHub CLI 并登录：

```sh
python scripts/collect_sources.py
```

脚本通过 GitHub API 固定上游提交，8 路并发读取案例文档，提取并去重来源链接，保存到 [候选索引](../catalog/source-candidates.json)。首次读取 33 份文档，获得 50 个链接，其中 12 个 X 帖子链接。这个数字表示发现的链接，不表示已读取或验证的帖子。

候选条目包含出处文件、验证状态与模型状态。X 帖子仍需可访问的正文、作者、原图及模型依据才能升级为正式案例。Microsoft MAI-Image-2.5 与 GPT Image 2.5 分开处理。

## 提交一个有用的案例

请附原始链接、作者、模型依据、输入图、完整提示词、输出图与失败细节。若许可不明确，提交链接和简短评价即可。案例应体现一个明确任务，避免把同场景微调计成大量独立作品。

