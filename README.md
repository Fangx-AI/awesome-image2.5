# Awesome Image 2.5

**从第一张图，到可复用的创作工作流。**

精选 AI 图像生成模型、创作工具、控制技术与学习资源，附带可修改的中文提示词模板。面向创作者、设计师和开发者。

[资源导航](#资源导航) · [提示词模板](docs/prompts.md) · [入门路线](docs/getting-started.md) · [贡献资源](CONTRIBUTING.md)

> `Image 2.5` 是本合集的项目名称，不指代某个模型版本，也不表示与模型厂商存在官方关联。

## 从这里开始

| 你想做什么 | 先看这里 | 下一步 |
| :--- | :--- | :--- |
| 使用可视化界面创作 | [InvokeAI](https://github.com/invoke-ai/InvokeAI) | 阅读安装要求，再尝试文生图与画布编辑 |
| 搭建可以复用的工作流 | [ComfyUI](https://github.com/Comfy-Org/ComfyUI) | 从官方示例开始，记录模型与节点版本 |
| 研究文字渲染和图像编辑 | [Qwen-Image](https://github.com/QwenLM/Qwen-Image) | 查看相应模型版本的示例与硬件要求 |
| 用 Python 编写生成流程 | [Diffusers](https://github.com/huggingface/diffusers) | 运行所选模型对应的官方 pipeline 示例 |
| 通过参考图控制生成 | [IP-Adapter](https://github.com/tencent-ailab/IP-Adapter) | 检查基础模型与适配器是否匹配 |
| 微调自己的视觉风格 | [AI Toolkit](https://github.com/ostris/ai-toolkit) | 先确认目标模型支持情况，准备有使用权的数据 |

## 资源导航

- [生成模型](#生成模型)
- [创作界面](#创作界面)
- [开发与训练](#开发与训练)
- [参考图与结构控制](#参考图与结构控制)
- [修复与放大](#修复与放大)
- [学习与工作流](#学习与工作流)

### 生成模型

模型仓库、推理代码和模型权重可能采用不同许可证；下载和商用前请分别查看对应版本的说明。

| 项目 | 简介 | 适合探索 |
| :--- | :--- | :--- |
| [FLUX.1](https://github.com/black-forest-labs/flux) | Black Forest Labs 的 FLUX.1 官方推理仓库 | 文生图推理与模型集成 |
| [Qwen-Image](https://github.com/QwenLM/Qwen-Image) | 提供图像生成、复杂文字渲染与图像编辑相关模型和示例 | 带文字的视觉设计、编辑任务 |
| [HunyuanImage 3.0](https://github.com/Tencent-Hunyuan/HunyuanImage-3.0) | 腾讯混元的原生多模态图像生成项目 | 多模态图像生成研究与部署 |

### 创作界面

- [ComfyUI](https://github.com/Comfy-Org/ComfyUI) — 节点式生成界面、API 与后端，适合组织和分享工作流。
- [InvokeAI](https://github.com/invoke-ai/InvokeAI) — 面向视觉创作的生成工具，提供 Web 界面与创作工作流。
- [Stable Diffusion Web UI](https://github.com/AUTOMATIC1111/stable-diffusion-webui) — Stable Diffusion 的 Web 界面；扩展和模型兼容性以项目文档为准。

### 开发与训练

- [Diffusers](https://github.com/huggingface/diffusers) — 基于 PyTorch 的扩散模型工具库，用于推理、实验与训练流程。
- [AI Toolkit](https://github.com/ostris/ai-toolkit) — 扩散模型微调工具集；使用前确认所需模型及训练方式受支持。
- [Kohya SS](https://github.com/bmaltais/kohya_ss) — Stable Diffusion 训练相关的图形界面与工具入口。

### 参考图与结构控制

- [ControlNet](https://github.com/lllyasviel/ControlNet) — 为扩散模型增加条件控制，可用于研究姿态、边缘与深度等结构约束。
- [IP-Adapter](https://github.com/tencent-ailab/IP-Adapter) — 为预训练文生图扩散模型提供图像提示能力。

这些组件不是通用插件。基础模型架构、权重、预处理器与运行工具需要匹配。

### 修复与放大

- [Real-ESRGAN](https://github.com/xinntao/Real-ESRGAN) — 面向真实图像与视频的修复项目，可用于探索生成图后处理与放大。

### 学习与工作流

- [ComfyUI Examples](https://github.com/comfyanonymous/ComfyUI_examples) — ComfyUI 官方示例仓库，适合从已有工作流理解节点连接。
- [Diffusion Models Course](https://github.com/huggingface/diffusion-models-class) — Hugging Face 扩散模型课程材料，适合补足原理与代码实践；运行旧课程时留意依赖版本。

## 中文提示词

从描述“想要什么”开始，再补充构图、光线、材质和约束。每次只修改少量条件，便于比较结果。

```text
主体：一台透明外壳的便携式收音机。
场景：浅灰色摄影棚背景，桌面干净。
构图：三分之四侧面视角，主体位于右侧，左侧留出标题空间。
光线：大面积柔光，边缘有轻微轮廓光。
材质：透明塑料、磨砂金属、可见的内部电路。
约束：不添加品牌标识、水印或额外文字。
用途：横版科技产品介绍配图。
```

[查看 5 个完整模板 →](docs/prompts.md)

模板是本项目编写的创作起点，尚未做跨模型出图验证。画幅、分辨率、种子等设置请使用工具实际支持的参数。

## 收录标准

1. 优先链接官方仓库或原作者资源，避免二次搬运与失效镜像。
2. 每个条目说明用途，不用未经验证的“最强”“免费商用”等结论。
3. 工具、模型和学习材料分开归类；收录不等于质量排名。
4. 新增资源需提供来源和具体价值；欢迎补充可复现的案例。
5. 已失效、迁移或归档的资源通过 Issue 或 PR 标明，再决定更新或移除。

首版核验：**2026-09-09**。本次确认了 14 个上游仓库可访问且未归档，检查了项目定位；未进行本地安装、性能评测或许可证法律审查。本合集不是完整榜单，也不承诺持续实时更新。

## 参与贡献

欢迎提交模型、工具、教程，以及有参数记录的生成案例。请先阅读 [贡献指南](CONTRIBUTING.md)，再通过 [Issue](https://github.com/Fangx-AI/awesome-image2.5/issues/new/choose) 或 Pull Request 提交。

## 许可

本项目原创文档与提示词采用 [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/)，详见 [LICENSE](LICENSE)。链接项目、模型权重、品牌标识及第三方素材遵循各自许可。
