# 采集与证据记录

## 2026-09-09

本轮从 GitHub 搜索发现候选库，批量读取 10 个仓库的首页线索，再通过公开 FxTwitter API 获取 33 条 X 帖子记录。33 条成功返回，共 63 张图片引用；只有 4 条正文明确声明 GPT Image 2.5。其他内容保留在候选证据表，不计入 Image 2.5 专区。

随后采集了 OpenAI 官方发布页、ReelyArt 模型展示、Simon Willison 实践文章及 LaplaceYoung 的公开案例页。119 个社区案例存在图片和来源页，110 个有案例级模型字段，9 个依赖仓库级生成说明。这一来源占比很高，因此本项目不会将数量当作多作者、多平台覆盖程度。

当前 Image 2.5 索引共 146 条：12 个官方示例、10 个平台声明、1 个附命令的作者实测、4 个 X 作者声明和 119 个社区作者声明。它们不是 146 次由本项目执行的独立实验。图像和提示词关系以原始案例页为准；缺少参数、输入图或许可时在详情中说明。

## 可复跑的数据流程

~~~sh
# GitHub CLI 已登录时发现并更新固定版本的旧版参考图谱
python scripts/import_reference_atlas.py

# 读取已发现的公开 X 原帖；缓存不提交
python scripts/collect_x_posts.py catalog/x-seeds.json --output catalog/x-evidence.json

# 更新社区作者案例记录
python scripts/collect_community_cases.py

# 完全离线重建所有页面
python scripts/build_all.py
python -m unittest discover -s tests -v
~~~

网络采集与页面构建分开执行，CI 不依赖外部站点当时是否可访问。采集后必须审阅模型声明与许可，再提交更新。

## 证据等级

| 标签 | 证明了什么 | 没有证明什么 |
| --- | --- | --- |
| 官方示例 | 官方将该图用于 Images 2.5 展示 | 未公开的原始参数或提示词 |
| 平台声明 | 平台明确声明所用型号 | 独立复现或性能保证 |
| 作者实测附命令 | 原页有型号、命令和结果 | 本项目自己的调用记录 |
| X 作者声明·镜像读取 | 公共镜像提供原帖正文及作者声明 | 镜像永远准确或型号已被独立验证 |
| 社区作者声明 | 案例页或仓库声明模型并附结果 | 完整 API 回执及提示词来源许可 |
| host-model-unknown | 本项目有真实生成结果 | 具体 Flare / Sunburst 型号 |
| 旧版参考 | 原始 GPT Image 2 图谱 | Image 2.5 生成结果 |

## 排除与更正

微软 MAI-Image-2.5、Qwen Image 2.5、发布日期前的旧图、只改了仓库名的 GPT Image 2 案例，都不会因标题包含 2.5 而自动进入专区。关键词匹配只是候选发现，最终标签保留证据强弱。

[机器可读索引](../catalog/image25-index.json) · [X 证据](../catalog/x-evidence.json) · [第三方声明](../THIRD_PARTY_NOTICES.md)

