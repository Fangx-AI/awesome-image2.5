<h1 align="center">Awesome Image 2.5</h1>

<p align="center">看作品，读提示词，找到可复用的创作方法。</p>

[在线搜索图库](https://fangx-ai.github.io/awesome-image2.5/) · [按分类浏览](docs/image25/README.md) · [本项目实图](docs/original-gallery.md) · [快速开始](docs/getting-started.md) · [English](README.en.md)

**146 个 Image 2.5 带图来源条目 · 11 类用途 · 14 个本项目实图案例 · 162 个旧版学习案例**

收录官方样例、平台展示与社区作者发布的作品。每个条目保留作者、图片、提示词入口和模型依据。作者声明、官方示例与本项目生成记录分别标注，避免把旧版或未知模型输出当作已验证的 2.5。

## 从作品开始

| 现代主义海报组 | 复古未来城市 |
| --- | --- |
| [![现代主义海报组](https://images.ctfassets.net/kftzwdyauwt9/47GTXbcPJQKPxvuNfyQo5V/1faeee99e4c10ea3042941c7312837b0/mid-century-modern-posters.png?w=3840&q=90&fm=webp)](docs/image25/cases/official-mid-century-modern-posters.md) | [![复古未来城市](https://images.ctfassets.net/kftzwdyauwt9/5vY4gdGrJFxuwV8l6GBU03/94befc05806eb290e786473975b3b22b/retrofuturism.png?w=3840&q=90&fm=webp)](docs/image25/cases/official-retrofuturism.md) |
| OpenAI · 官方示例 | OpenAI · 官方示例 |

| 等距建筑剖面 | 展览文字海报 |
| --- | --- |
| [![等距建筑剖面](https://cdn.reely.art/models/gpt-image-2-5/sunburst-isometric-diorama.webp)](docs/image25/cases/reely-sunburst-isometric-diorama.md) | [![展览文字海报](https://cdn.reely.art/models/gpt-image-2-5/sunburst-exhibition-poster.webp)](docs/image25/cases/reely-sunburst-exhibition-poster.md) |
| ReelyArt · 平台声明 | ReelyArt · 平台声明 |

| Feishu Collaboration UI | 晨曦光圈动漫都市 |
| --- | --- |
| [![Feishu Collaboration UI](https://raw.githubusercontent.com/LaplaceYoung/awesome-gpt-image-2.5/9bb515b6b978a7521ae884821a847ab58c11c939/assets/generated/141-feishu-collaboration-ui.png)](docs/image25/cases/laplace-141-feishu-collaboration-ui.md) | [![晨曦光圈动漫都市](https://raw.githubusercontent.com/LaplaceYoung/awesome-gpt-image-2.5/9bb515b6b978a7521ae884821a847ab58c11c939/assets/generated/123-imported-.png)](docs/image25/cases/laplace-123-imported-.md) |
| LaplaceYoung · 社区作者声明 | LaplaceYoung · 社区作者声明 |

| 树林细节与噪点测试 | 图表中加入浣熊科学家 |
| --- | --- |
| [![树林细节与噪点测试](https://pbs.twimg.com/media/HRt_pW_XEAAYiCE.jpg?name=orig)](docs/image25/cases/x-2097411028510179759.md) | [![图表中加入浣熊科学家](https://static.simonwillison.net/static/2026/racoon-chart.webp)](docs/image25/cases/simon-raccoon-chart.md) |
| @mark_k · X 作者声明·镜像读取 | Simon Willison · 作者实测附命令 |

## 按用途浏览

| 分类 | 案例 |
| --- | ---: |
| [建筑与场景](docs/image25/category-01.md) | 13 |
| [海报与文字](docs/image25/category-02.md) | 21 |
| [插画与艺术](docs/image25/category-03.md) | 28 |
| [出版与版式](docs/image25/category-04.md) | 2 |
| [品牌与图标](docs/image25/category-05.md) | 15 |
| [信息与教育](docs/image25/category-06.md) | 9 |
| [摄影与人像](docs/image25/category-07.md) | 19 |
| [参考图编辑](docs/image25/category-08.md) | 5 |
| [界面与屏幕](docs/image25/category-09.md) | 7 |
| [角色与游戏](docs/image25/category-10.md) | 17 |
| [产品与商业](docs/image25/category-11.md) | 10 |

## 怎样用到自己的工作里

1. 选作品，打开案例页查看作者来源和提示词入口。
2. 明确替换对象、文字、配色及参考图，保留布局与编辑约束。
3. 生成后检查文字、结构、身份和编辑范围；不要把好看的预览当作所有要求都已满足。

~~~sh
uv tool install git+https://github.com/Fangx-AI/awesome-image2.5
image25 --prompt-file your-prompt.txt --model flare --dry-run
image25 --prompt-file your-prompt.txt --model flare -o output.png
~~~

[安装 Skill](docs/getting-started.md) · [编辑工作流](docs/workflows.md) · [质量检查](docs/quality.md)

## 本项目实图与学习图谱

| 系列包装 | 角色三视图 |
| --- | --- |
| ![包装](assets/showcase/coffee-packaging.png) | ![角色](assets/showcase/courier-character.png) |

[14 个原创实图案例](docs/original-gallery.md)附完整提示词、拆解、替换方法和实际缺陷；宿主没有返回精确模型 ID。
[31 类完整参考图谱](docs/legacy-gallery.md)基于 Wuyoscar 的 MIT 项目改造，162 个原始案例保留 GPT Image 2 标注及作者来源。

## 来源与维护

[采集与证据记录](docs/research.md) · [投稿指南](CONTRIBUTING.md) · [第三方许可](THIRD_PARTY_NOTICES.md)

图像通过作者原始地址或上游固定提交引用，需要联网。原作者保留权利；缺失的提示词或模型证据不会补造。社区项目，与 OpenAI 无官方关联。
