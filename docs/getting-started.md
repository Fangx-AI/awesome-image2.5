# 安装与使用

[返回首页](../README.md) · [English](getting-started.en.md) · [文档导航](README.md) · [常见问题](troubleshooting.md)

| 你的目标 | 需要什么 | 下一步 |
| --- | --- | --- |
| 浏览作品、复制提示词 | GitHub 页面即可 | [提示词使用方法](prompts.md) |
| 让 Agent 生成或编辑图片 | 生成 Skill + 宿主生图工具，或独立 CLI | [安装 Skill](#skills) |
| 从参考图提炼提示词 | 反推 Skill + 能看图的 Agent | [安装 Skill](#skills) |
| 在终端指定模型生成 | Python 3.10+、CLI、有效的 API 访问权限 | [安装 CLI](#cli) |

<a id="skills"></a>

## 安装 Agent Skill

在带有 `$skill-installer` 的 Codex 对话中发送以下内容。这是发给 Agent 的请求，不是终端命令：

```text
$skill-installer
请从下面的 GitHub 目录安装 image25：
https://github.com/Fangx-AI/awesome-image2.5/tree/main/skills/image25
```

需要看图提炼提示词时，再安装第二个 Skill：

```text
$skill-installer
请从下面的 GitHub 目录安装 image25-reverse-prompt：
https://github.com/Fangx-AI/awesome-image2.5/tree/main/skills/image25-reverse-prompt
```

安装完成后，在下一轮对话中试用：

```text
用 image25 参考品牌系统分类，帮我写一份三款茶叶包装的提示词，先不要生图。
```

反推 Skill 的试用方式：上传一张参考图，再发送“用 image25-reverse-prompt 提取这张图的构图、光线和材质，输出可改写的提示词”。它提炼可见内容，不恢复作者未公开的原始提示词。

其他支持 Skill 的 Agent：按照其安装方式导入完整 `skills/image25/` 或 `skills/image25-reverse-prompt/` 文件夹，保留 `references/`。不要只复制 `SKILL.md`。运行时之间的安装路径不同，本项目未逐一端到端验证。

Skill 不附带 API Key，也不会自动安装 CLI。宿主已有生图工具时可以使用该工具；只有工具披露精确型号才能将输出标为指定模型的结果。

<a id="cli"></a>

## 安装 CLI

Python 3.10+ 环境中：
```sh
uv tool install git+https://github.com/Fangx-AI/awesome-image2.5
image25 --help
```

没有 uv 时，也可以使用 pip 从仓库安装：

```sh
python -m pip install git+https://github.com/Fangx-AI/awesome-image2.5
image25 --help
```

以上方式需要 Git。要运行案例页中的 `assets/showcase/...` 命令，请先克隆仓库并进入根目录；单独安装 CLI 不会下载这些图片：

```sh
git clone https://github.com/Fangx-AI/awesome-image2.5.git
cd awesome-image2.5
```

<a id="first-run"></a>

## 第一次运行：无需密钥的预检

```sh
image25 -p "A small ceramic fox on a pale green background" --model flare --dry-run
```

成功时终端输出包含 `model`、`prompt`、`size` 和输出路径的 JSON；不会生成图片，也不会调用 API。这样可以先确认安装成功，无需准备提示词文件。

## 配置 API Key

通过本机密钥管理工具或终端设置 `OPENAI_API_KEY`。不在聊天、Issue 或提交中粘贴真实密钥。

PowerShell：
```powershell
$env:OPENAI_API_KEY = '<your-key>'
```

Bash / zsh：
```sh
export OPENAI_API_KEY='<your-key>'
```

示例值需要在自己的终端替换。CLI 只读取进程环境，不读取 .env 或家目录文件；官方端点固定为 https://api.openai.com/v1。真实请求按账户规则计费。

## 提示词文件

把完整提示词保存为 UTF-8 的 `prompt.txt`，避免复杂引号：
```sh
image25 --prompt-file prompt.txt --model flare --size 1536x1024 --dry-run
image25 --prompt-file prompt.txt --model flare --size 1536x1024 -o generated/poster.png
```

第二条命令会实际调用 API。成功后得到 `generated/poster.png` 和对应的 `.png.json` 记录。编辑与多图示例中的输入文件也需要先准备好。

## 多图合成

输入顺序对应提示词中的 image 1、image 2：
```sh
image25 --prompt-file composite.txt --model sunburst -i scene.png -i object.png -o generated/composite.png
```

## 蒙版编辑

蒙版为带 alpha 通道的 PNG，尺寸与第一张参考图相同。透明区域表示要编辑的区域。
```sh
image25 --prompt-file edit.txt --model sunburst -i original.png --mask mask.png -o generated/edit.png
```

## 透明输出和格式

```sh
image25 -p "A small ceramic fox, isolated" --background transparent --format webp -o generated/fox.webp
```

JPEG 不支持透明背景；输出文件后缀必须匹配格式。

## 参数

| 参数 | 用法 |
| :--- | :--- |
| `-p / --prompt` | 文本提示词；与 --prompt-file、--recipe 三选一 |
| `--prompt-file` | UTF-8 文件 |
| `--recipe` | 使用本地实验配方 ID；不自动套用配方建议尺寸与模型 |
| `--model` | flare、sunburst 或相应完整模型名；默认 flare |
| `-i / --image` | 可重复，提供本地参考图片后自动走编辑接口 |
| `--mask` | 第一张参考图对应的 PNG 蒙版 |
| `--size` | 默认 1024x1024；支持 auto 或有效 WIDTHxHEIGHT |
| `--quality` | auto、low、medium、high、xhigh、max |
| `--background` | auto、opaque、transparent |
| `--format` | png、jpeg、webp；默认 png |
| `-o / --output` | 默认 generated/image.png；不覆盖已有文件 |
| `--dry-run` | 校验并打印请求，不联网、不计费 |

## 输出与常见问题

输出图旁会保存 `文件名.png.json`，包含提示词、请求模型、参数和 request ID。分享时检查是否包含私人提示词或文件名称。

- 找不到命令：确认 uv 工具目录已加入 PATH，或在克隆目录中使用 `uv run image25`。
- 缺少密钥：先用 --dry-run 验证，再在当前终端配置 OPENAI_API_KEY。
- 输出已存在：改用新文件名。
- 400：检查参数、尺寸和图像格式。
- 401 / 403：检查密钥与模型访问权限。
- 429：检查账户限额与速率限制。
- 超时：服务端可能已处理请求；CLI 不会自动重试，先确认情况再决定是否再生成。

本地模拟测试不证明真实账户访问已开通。

## 离线检索与批量任务

`catalog` 检索的是提示词实验配方；带图来源案例请使用 [31 类图谱](../skills/image25/references/gallery.md)。

```sh
image25 catalog "poster" --kind original --limit 5
image25 catalog --show chinese-poster
image25 --recipe chinese-poster --size 1024x1536 --dry-run
```

克隆仓库后，可预检[批量清单](../examples/batch.json)：

```sh
image25 batch examples/batch.json --dry-run
```

确认清单后移除 `--dry-run` 才会逐项生成。相对路径以清单所在目录为基准；该样例输出到 `examples/generated/`。失败即停，重跑前移除已完成任务或换输出文件名。

## 更新安装

CLI 可按自己的安装方式，重新从上面的 GitHub 地址执行升级安装。Skill 是独立副本，不随 CLI 更新：让 Agent 对比已安装 Skill 与仓库版本，保留你的本地改动后更新整个文件夹。遇到“已存在”时，不要将重复安装当作更新成功。

[继续：参考图编辑工作流](workflows.md) · [API 详细参数](../skills/image25/references/api.md)
