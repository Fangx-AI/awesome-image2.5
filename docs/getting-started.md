# 安装与使用

[返回首页](../README.md) · [API 参数说明](../skills/image25/references/api.md)

## 安装

Python 3.10+ 环境中：
```sh
uv tool install git+https://github.com/Fangx-AI/awesome-image2.5
image25 --help
```

也可以克隆项目后执行 `python -m pip install .`。本仓库没有声称已经发布到 PyPI，因此不要使用不带 GitHub 地址的 `pip install image25-cli`。

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
| `-p / --prompt` | 文本提示词，与 --prompt-file 二选一 |
| `--prompt-file` | UTF-8 文件 |
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
