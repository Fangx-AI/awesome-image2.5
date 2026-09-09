<div align="center">

# Awesome Image 2.5

### 把灵感变成图像，把好图变成可复用的 Skill。

**GPT Image 2.5 提示词画廊 · Agent Skills · 生图 / 改图 CLI**

[English](README.en.md) · [浏览画廊](skills/image25/references/gallery.md) · [快速开始](docs/getting-started.md) · [参与贡献](CONTRIBUTING.md)

![Image 2.5 创意概念封面](assets/cover.png)

**12 个原创配方 · 2 个 Skills · Flare / Sunburst 双模型 · 中文优先**

</div>

## 三种打开方式

| 你想怎么用 | 入口 |
| :--- | :--- |
| 找到提示词，复制就用 | [分类提示词画廊](skills/image25/references/gallery.md) |
| 让 Agent 帮你构思、生图、改图 | [Image 2.5 Skill](skills/image25/SKILL.md) |
| 给一张图，提炼可复用提示词 | [Reverse Prompt Skill](skills/image25-reverse-prompt/SKILL.md) |
| 用命令行连接官方 API | [CLI 安装与使用](docs/getting-started.md) |

## 提示词画廊

从商业摄影到中文海报，从界面设计到参考图编辑。点击分类查看完整提示词，并下载独立文本文件。

| 摄影与空间 | 设计与插画 | 参考图编辑 |
| :--- | :--- | :--- |
| [透明收音机 · 产品摄影](skills/image25/references/prompts/product-radio.txt) | [植物小店 · 等距插画](skills/image25/references/prompts/botanical-shop.txt) | [宠物围巾 · 保持身份](skills/image25/references/prompts/pet-costume.txt) |
| [沙漠圆门 · 建筑空间](skills/image25/references/prompts/desert-portal.txt) | [城市微光 · 中文海报](skills/image25/references/prompts/chinese-poster.txt) | [中文标题 · 文字替换](skills/image25/references/prompts/text-localize.txt) |
| [柠檬意面 · 美食摄影](skills/image25/references/prompts/food-editorial.txt) | [阅读应用 · 界面概念](skills/image25/references/prompts/app-mockup.txt) | [多图参考 · 物件合成](skills/image25/references/prompts/reference-composite.txt) |
| [专注时刻 · 文章封面](skills/image25/references/prompts/editorial-cover.txt) | [植物探险家 · 角色设定](skills/image25/references/prompts/character-sheet.txt) | [MOSS · 品牌提案](skills/image25/references/prompts/brand-board.txt) |

> **来源与验证状态：** 上方封面是原创创意概念图，生成宿主未提供精确模型标识，不作为 Image 2.5 模型实测证据。12 个配方均为原创、尚未通过指定模型验证的提示词。详见 [图像来源记录](assets/PROVENANCE.md)。

<details>
<summary><strong>展开示例：城市微光 · 中文海报</strong></summary>

```text
为城市夜间摄影展设计一张竖版海报。
主视觉是一束橙色路灯照在湿润的深蓝街道上，倒影形成简洁几何形状。
上方清晰写出标题“城市微光”，下方仅写“夜间摄影展”。
中文文字准确，标题明显大于副标题，留白充足。
不增加其他文字、日期、标志或水印。
```

建议尺寸：1024x1536。生成后逐字检查文字。

</details>

<details>
<summary><strong>展开示例：保持宠物身份的局部编辑</strong></summary>

```text
为输入图中的宠物加一条芥末黄色针织围巾。
保持面部比例、毛色花纹、眼睛颜色、姿态和表情。
保留原始背景、相机角度和裁切。
围巾自然地围在脖子上，不遮挡脸部，光照和阴影与原图一致。
其余内容不变。
```

需要一张参考图；生成后检查围巾之外的区域是否发生变化。

</details>

## 安装 Skill

在 Codex 中使用内置安装器，分别提供需要的 Skill 文件夹链接：

```text
$skill-installer
安装 https://github.com/Fangx-AI/awesome-image2.5/tree/main/skills/image25
```

```text
$skill-installer
安装 https://github.com/Fangx-AI/awesome-image2.5/tree/main/skills/image25-reverse-prompt
```

其他支持 Agent Skills 的运行时，可将相应完整文件夹放入其文档指定的 skills 目录。不要覆盖已有同名 Skill。Skill 的安装与 CLI 安装相互独立。

安装后可以这样说：

```text
用 $image25 帮我生成一张“城市微光”中文海报。
用 $image25 给这张产品图换背景，保持产品形状和文字。
用 $image25-reverse-prompt 分析这张参考图，提炼中文提示词。
```

## CLI 快速开始

需要 Python 3.10+ 和 uv。先安装工具，再通过本机环境变量配置 OPENAI_API_KEY。

```sh
uv tool install git+https://github.com/Fangx-AI/awesome-image2.5
```

先检查请求，不调用 API：

```sh
image25 -p "A translucent cobalt-blue radio, studio photography" --model flare --dry-run
```

文生图：

```sh
image25 -p "A translucent cobalt-blue radio, studio photography" --model flare --size 1536x1024 -o generated/radio.png
```

参考图编辑：

```sh
image25 -p "Add a mustard scarf. Preserve the pet and background." --model sunburst -i pet.png -o generated/pet-edit.png
```

透明背景：

```sh
image25 -p "A tiny ceramic fox, isolated" --background transparent -o generated/fox.png
```

[更多用法：多图合成、蒙版、提示词文件、参数与故障排查 →](docs/getting-started.md)

每次调用生成 1 张图，并保存提示词、模型和参数的 JSON 记录。CLI 不覆盖现有文件、不自动重试，也不读取其他目录里的密钥文件。

## Image 2.5 模型

| CLI 选项 | 实际模型标识 | 官方定位 |
| :--- | :--- | :--- |
| `--model flare`（默认） | `gpt-image-2.5-flare` | 日常高质量图像生成，侧重速度 |
| `--model sunburst` | `gpt-image-2.5-sunburst` | 图像生成与编辑，侧重编辑精度 |

质量选项：`auto / low / medium / high / xhigh / max`。

核验日期：2026-09-09。来源：[Flare](https://developers.openai.com/api/docs/models/gpt-image-2.5-flare)、[Sunburst](https://developers.openai.com/api/docs/models/gpt-image-2.5-sunburst)、[图像生成指南](https://developers.openai.com/api/docs/guides/image-generation)。

## 开发与验证

```sh
git clone https://github.com/Fangx-AI/awesome-image2.5.git
cd awesome-image2.5
uv sync
uv run python -m unittest discover -s tests -v
```

自动化测试使用模拟响应，覆盖请求路由、模型参数、参考图顺序、蒙版校验、输出保存及失败清理。尚未通过本仓库 CLI 发起真实付费生图请求。

## 致谢与贡献

项目形态参考 [wuyoscar/GPT-Image2-Skill](https://github.com/wuyoscar/GPT-Image2-Skill) 的「画廊 + Skills + CLI」组织方式。本仓库的提示词与实现独立编写，未复制其代码或示例图片。

欢迎提交附带模型、提示词、参数和来源的真实 Image 2.5 案例，详见 [贡献指南](CONTRIBUTING.md)。

原创代码与文档采用 [CC0 1.0](LICENSE)。第三方内容遵循原许可。本项目由社区维护，与 OpenAI 无官方关联。
