<h1 align="center">GPT Image 2.5 · Prompt Gallery + Agent Skills + CLI</h1>

<p align="center">A category-first prompt and image reference repository for creative work.</p>

[中文](README.md) · [English](README.en.md) · [分类导航](#gallery-index) · [安装](#installation) · [完整分类图谱](skills/image25/references/gallery.md)

![Validate](https://github.com/Fangx-AI/awesome-image2.5/actions/workflows/tests.yml/badge.svg) ![Python](https://img.shields.io/badge/Python-3.10%2B-blue) ![Categories](https://img.shields.io/badge/Categories-31-35644a)

![Original concept cover](assets/cover.png)

[原创概念封面 · 生成来源 / Cover provenance](assets/PROVENANCE.md)

## At a glance

| Surface | Content |
| --- | --- |
| Gallery | 31 categories · 146 Image 2.5 source records |
| Prompts | 31 new practice briefs · 14 original output demonstrations · 162 attributed legacy cases |
| Agent Skills | image25 · image25-reverse-prompt |
| CLI | Generate · Edit · Multi-reference · Mask · Batch · Dry run |

Official samples, provider claims, author claims and unknown-model outputs are labeled separately. Most community records currently come from LaplaceYoung. Legacy GPT Image 2 images are never relabeled as 2.5.

## What this repository is for

Find a deliverable below, inspect the images and expand the prompt. Use the full category file when drafting with an agent. The README is the selected showcase; the Skill atlas contains the complete collection.

<a id="installation"></a>

## Installation

<details><summary>Codex · Agent Skills</summary>

~~~text
$skill-installer
Install this skill from GitHub:
https://github.com/Fangx-AI/awesome-image2.5/tree/main/skills/image25

# Optional: extract prompts from reference images
https://github.com/Fangx-AI/awesome-image2.5/tree/main/skills/image25-reverse-prompt
~~~

[安装、配置和更新](docs/getting-started.md) · [Skill 运行说明](skills/image25/SKILL.md)

</details>

<details><summary>CLI · Python 3.10+</summary>

~~~sh
uv tool install git+https://github.com/Fangx-AI/awesome-image2.5
image25 --prompt-file prompt.txt --model flare --dry-run
image25 --prompt-file prompt.txt --model flare -o generated/result.png
~~~

`OPENAI_API_KEY` is read from the process environment. Live calls require API access.

</details>

## Quick usage and prompting fundamentals

~~~text
用 image25 参考“品牌系统与视觉识别”分类，为山间书店设计一套统一的视觉识别。
用 image25-reverse-prompt 分析这张参考图，提取构图、材质、光线与媒介边界。
编辑第 1 张图：只替换围巾颜色，保留身份、姿势、光线和背景。
~~~

[完整 CLI 参数](docs/getting-started.md#参数) · [Prompt Craft](skills/image25/references/craft.md) · [编辑工作流](docs/workflows.md)

### Reference editing: input and result

| Input / 参考图 | Output / 编辑结果 |
| --- | --- |
| ![Input](assets/showcase/pet-portrait.png) | ![Output](assets/showcase/pet-scarf.png) |

**host-model-unknown** · [完整 Prompt 与实际观察](skills/image25/references/showcase/pet-scarf.md)

<a id="gallery-index"></a>

## Selected prompt gallery

Jump to a section or open its full Markdown atlas. Each category separates source images, original demonstrations and legacy references.

<table>
<tr>
<td align="center" width="33%"><strong><a href="#gallery-anime-and-manga">Anime And Manga</a></strong><br/><sub><a href="skills/image25/references/gallery-anime-and-manga.md">完整 MD / Full atlas</a></sub></td>
<td align="center" width="33%"><strong><a href="#gallery-gaming">Gaming</a></strong><br/><sub><a href="skills/image25/references/gallery-gaming.md">完整 MD / Full atlas</a></sub></td>
<td align="center" width="33%"><strong><a href="#gallery-retro-and-cyberpunk">Retro And Cyberpunk</a></strong><br/><sub><a href="skills/image25/references/gallery-retro-and-cyberpunk.md">完整 MD / Full atlas</a></sub></td>
</tr>
<tr>
<td align="center" width="33%"><strong><a href="#gallery-cinematic-and-animation">Cinematic And Animation</a></strong><br/><sub><a href="skills/image25/references/gallery-cinematic-and-animation.md">完整 MD / Full atlas</a></sub></td>
<td align="center" width="33%"><strong><a href="#gallery-character-design">Character Design</a></strong><br/><sub><a href="skills/image25/references/gallery-character-design.md">完整 MD / Full atlas</a></sub></td>
<td align="center" width="33%"><strong><a href="#gallery-typography-and-posters">Typography And Posters</a></strong><br/><sub><a href="skills/image25/references/gallery-typography-and-posters.md">完整 MD / Full atlas</a></sub></td>
</tr>
<tr>
<td align="center" width="33%"><strong><a href="#gallery-illustration">Illustration</a></strong><br/><sub><a href="skills/image25/references/gallery-illustration.md">完整 MD / Full atlas</a></sub></td>
<td align="center" width="33%"><strong><a href="#gallery-watercolor">Watercolor</a></strong><br/><sub><a href="skills/image25/references/gallery-watercolor.md">完整 MD / Full atlas</a></sub></td>
<td align="center" width="33%"><strong><a href="#gallery-ink-and-chinese">Ink And Chinese</a></strong><br/><sub><a href="skills/image25/references/gallery-ink-and-chinese.md">完整 MD / Full atlas</a></sub></td>
</tr>
<tr>
<td align="center" width="33%"><strong><a href="#gallery-pixel-art">Pixel Art</a></strong><br/><sub><a href="skills/image25/references/gallery-pixel-art.md">完整 MD / Full atlas</a></sub></td>
<td align="center" width="33%"><strong><a href="#gallery-isometric">Isometric</a></strong><br/><sub><a href="skills/image25/references/gallery-isometric.md">完整 MD / Full atlas</a></sub></td>
<td align="center" width="33%"><strong><a href="#gallery-product-and-food">Product And Food</a></strong><br/><sub><a href="skills/image25/references/gallery-product-and-food.md">完整 MD / Full atlas</a></sub></td>
</tr>
<tr>
<td align="center" width="33%"><strong><a href="#gallery-brand-systems-and-identity">Brand Systems And Identity</a></strong><br/><sub><a href="skills/image25/references/gallery-brand-systems-and-identity.md">完整 MD / Full atlas</a></sub></td>
<td align="center" width="33%"><strong><a href="#gallery-photography">Photography</a></strong><br/><sub><a href="skills/image25/references/gallery-photography.md">完整 MD / Full atlas</a></sub></td>
<td align="center" width="33%"><strong><a href="#gallery-screen-photography">Screen Photography</a></strong><br/><sub><a href="skills/image25/references/gallery-screen-photography.md">完整 MD / Full atlas</a></sub></td>
</tr>
<tr>
<td align="center" width="33%"><strong><a href="#gallery-infographics-and-field-guides">Infographics And Field Guides</a></strong><br/><sub><a href="skills/image25/references/gallery-infographics-and-field-guides.md">完整 MD / Full atlas</a></sub></td>
<td align="center" width="33%"><strong><a href="#gallery-research-paper-figures">Research Paper Figures</a></strong><br/><sub><a href="skills/image25/references/gallery-research-paper-figures.md">完整 MD / Full atlas</a></sub></td>
<td align="center" width="33%"><strong><a href="#gallery-official-openai-cookbook-examples">Official Openai Cookbook Examples</a></strong><br/><sub><a href="skills/image25/references/gallery-official-openai-cookbook-examples.md">完整 MD / Full atlas</a></sub></td>
</tr>
<tr>
<td align="center" width="33%"><strong><a href="#gallery-edit-endpoint-showcase">Edit Endpoint Showcase</a></strong><br/><sub><a href="skills/image25/references/gallery-edit-endpoint-showcase.md">完整 MD / Full atlas</a></sub></td>
<td align="center" width="33%"><strong><a href="#gallery-ui-ux-mockups">Ui Ux Mockups</a></strong><br/><sub><a href="skills/image25/references/gallery-ui-ux-mockups.md">完整 MD / Full atlas</a></sub></td>
<td align="center" width="33%"><strong><a href="#gallery-data-visualization">Data Visualization</a></strong><br/><sub><a href="skills/image25/references/gallery-data-visualization.md">完整 MD / Full atlas</a></sub></td>
</tr>
<tr>
<td align="center" width="33%"><strong><a href="#gallery-technical-illustration">Technical Illustration</a></strong><br/><sub><a href="skills/image25/references/gallery-technical-illustration.md">完整 MD / Full atlas</a></sub></td>
<td align="center" width="33%"><strong><a href="#gallery-architecture-and-interior">Architecture And Interior</a></strong><br/><sub><a href="skills/image25/references/gallery-architecture-and-interior.md">完整 MD / Full atlas</a></sub></td>
<td align="center" width="33%"><strong><a href="#gallery-scientific-and-educational">Scientific And Educational</a></strong><br/><sub><a href="skills/image25/references/gallery-scientific-and-educational.md">完整 MD / Full atlas</a></sub></td>
</tr>
<tr>
<td align="center" width="33%"><strong><a href="#gallery-fashion-editorial">Fashion Editorial</a></strong><br/><sub><a href="skills/image25/references/gallery-fashion-editorial.md">完整 MD / Full atlas</a></sub></td>
<td align="center" width="33%"><strong><a href="#gallery-fine-art-painting">Fine Art Painting</a></strong><br/><sub><a href="skills/image25/references/gallery-fine-art-painting.md">完整 MD / Full atlas</a></sub></td>
<td align="center" width="33%"><strong><a href="#gallery-more-illustration-styles">More Illustration Styles</a></strong><br/><sub><a href="skills/image25/references/gallery-more-illustration-styles.md">完整 MD / Full atlas</a></sub></td>
</tr>
<tr>
<td align="center" width="33%"><strong><a href="#gallery-cinematic-film-references">Cinematic Film References</a></strong><br/><sub><a href="skills/image25/references/gallery-cinematic-film-references.md">完整 MD / Full atlas</a></sub></td>
<td align="center" width="33%"><strong><a href="#gallery-beauty-and-lifestyle">Beauty And Lifestyle</a></strong><br/><sub><a href="skills/image25/references/gallery-beauty-and-lifestyle.md">完整 MD / Full atlas</a></sub></td>
<td align="center" width="33%"><strong><a href="#gallery-events-and-experience">Events And Experience</a></strong><br/><sub><a href="skills/image25/references/gallery-events-and-experience.md">完整 MD / Full atlas</a></sub></td>
</tr>
<tr>
<td align="center" width="33%"><strong><a href="#gallery-tattoo-design">Tattoo Design</a></strong><br/><sub><a href="skills/image25/references/gallery-tattoo-design.md">完整 MD / Full atlas</a></sub></td>
</tr>
</table>

<a id="gallery-anime-and-manga"></a>

<h2 align="center">Anime And Manga</h2>

[↑ Index](#gallery-index) · [完整分类 / Full atlas](skills/image25/references/gallery-anime-and-manga.md)

**Image 2.5: 6 · host-model-unknown: 0 · GPT Image 2: 12**

角色身份、镜头、动作、线条和分镜阅读顺序。锁定每格的发型与服装；检查手部和气泡归属。

<table>
<tr>
<td width="50%" align="center" valign="top"><a href="https://github.com/LaplaceYoung/awesome-gpt-image-2.5/blob/9bb515b6b978a7521ae884821a847ab58c11c939/docs/cases/071-imported-.md"><img src="https://raw.githubusercontent.com/LaplaceYoung/awesome-gpt-image-2.5/9bb515b6b978a7521ae884821a847ab58c11c939/assets/generated/071-imported-.png" width="100%" alt="动漫贴纸集合"/></a><br/><strong>动漫贴纸集合</strong><br/><sub>Image 2.5 · 社区作者声明 · LaplaceYoung</sub></td>
<td width="50%" align="center" valign="top"><a href="https://github.com/LaplaceYoung/awesome-gpt-image-2.5/blob/9bb515b6b978a7521ae884821a847ab58c11c939/docs/cases/081-imported-.md"><img src="https://raw.githubusercontent.com/LaplaceYoung/awesome-gpt-image-2.5/9bb515b6b978a7521ae884821a847ab58c11c939/assets/generated/081-imported-.png" width="100%" alt="讽刺漫画生成"/></a><br/><strong>讽刺漫画生成</strong><br/><sub>Image 2.5 · 社区作者声明 · LaplaceYoung</sub></td>
</tr>
</table>

<details>
<summary>Prompt · 动漫贴纸集合</summary>

[LaplaceYoung · 原始出处](https://github.com/LaplaceYoung/awesome-gpt-image-2.5/blob/9bb515b6b978a7521ae884821a847ab58c11c939/docs/cases/071-imported-.md) · **Image 2.5 · 社区作者声明**

[原作者提示词与生成条件](https://github.com/LaplaceYoung/awesome-gpt-image-2.5/blob/9bb515b6b978a7521ae884821a847ab58c11c939/docs/cases/071-imported-.md)

未在本仓库转载完整 Prompt；原页未公开的参数不补造。

</details>

<details>
<summary>Prompt · 讽刺漫画生成</summary>

[LaplaceYoung · 原始出处](https://github.com/LaplaceYoung/awesome-gpt-image-2.5/blob/9bb515b6b978a7521ae884821a847ab58c11c939/docs/cases/081-imported-.md) · **Image 2.5 · 社区作者声明**

[原作者提示词与生成条件](https://github.com/LaplaceYoung/awesome-gpt-image-2.5/blob/9bb515b6b978a7521ae884821a847ab58c11c939/docs/cases/081-imported-.md)

未在本仓库转载完整 Prompt；原页未公开的参数不补造。

</details>

<details><summary>本类起始 Prompt / Original practice brief</summary>

**prompt-only** · 本项目编写，尚未出图；不是上方示例图的原始 Prompt。

~~~text
Create a two-page monochrome manga spread about an original bicycle courier caught in a sudden rainstorm. Use six panels in a clear left-to-right reading order, with one wide establishing panel, three action beats and two close-ups. Keep the courier's short hair, round glasses and yellow rain cape consistent. Use varied ink line weights and restrained screentone. Keep speech balloons empty for later lettering. Preserve clear gutters and readable silhouettes.
~~~

</details>

<a id="gallery-gaming"></a>

<h2 align="center">Gaming</h2>

[↑ Index](#gallery-index) · [完整分类 / Full atlas](skills/image25/references/gallery-gaming.md)

**Image 2.5: 4 · host-model-unknown: 0 · GPT Image 2: 10**

玩家视角、场景动线、HUD 区域和可玩性。核对小地图、血条和场景对应；区分游戏画面与封面。

<table>
<tr>
<td width="50%" align="center" valign="top"><a href="https://github.com/LaplaceYoung/awesome-gpt-image-2.5/blob/9bb515b6b978a7521ae884821a847ab58c11c939/docs/cases/040-imported-3d.md"><img src="https://raw.githubusercontent.com/LaplaceYoung/awesome-gpt-image-2.5/9bb515b6b978a7521ae884821a847ab58c11c939/assets/generated/040-imported-3d.png" width="100%" alt="超写实3D游戏角色怀旧场景"/></a><br/><strong>超写实3D游戏角色怀旧场景</strong><br/><sub>Image 2.5 · 社区作者声明 · LaplaceYoung</sub></td>
<td width="50%" align="center" valign="top"><a href="https://github.com/LaplaceYoung/awesome-gpt-image-2.5/blob/9bb515b6b978a7521ae884821a847ab58c11c939/docs/cases/062-imported-rpg.md"><img src="https://raw.githubusercontent.com/LaplaceYoung/awesome-gpt-image-2.5/9bb515b6b978a7521ae884821a847ab58c11c939/assets/generated/062-imported-rpg.png" width="100%" alt="RPG 风格角色卡片制作"/></a><br/><strong>RPG 风格角色卡片制作</strong><br/><sub>Image 2.5 · 社区作者声明 · LaplaceYoung</sub></td>
</tr>
</table>

<details>
<summary>Prompt · 超写实3D游戏角色怀旧场景</summary>

[LaplaceYoung · 原始出处](https://github.com/LaplaceYoung/awesome-gpt-image-2.5/blob/9bb515b6b978a7521ae884821a847ab58c11c939/docs/cases/040-imported-3d.md) · **Image 2.5 · 社区作者声明**

[原作者提示词与生成条件](https://github.com/LaplaceYoung/awesome-gpt-image-2.5/blob/9bb515b6b978a7521ae884821a847ab58c11c939/docs/cases/040-imported-3d.md)

未在本仓库转载完整 Prompt；原页未公开的参数不补造。

</details>

<details>
<summary>Prompt · RPG 风格角色卡片制作</summary>

[LaplaceYoung · 原始出处](https://github.com/LaplaceYoung/awesome-gpt-image-2.5/blob/9bb515b6b978a7521ae884821a847ab58c11c939/docs/cases/062-imported-rpg.md) · **Image 2.5 · 社区作者声明**

[原作者提示词与生成条件](https://github.com/LaplaceYoung/awesome-gpt-image-2.5/blob/9bb515b6b978a7521ae884821a847ab58c11c939/docs/cases/062-imported-rpg.md)

未在本仓库转载完整 Prompt；原页未公开的参数不补造。

</details>

<details><summary>本类起始 Prompt / Original practice brief</summary>

**prompt-only** · 本项目编写，尚未出图；不是上方示例图的原始 Prompt。

~~~text
Create a 16:9 screenshot concept for an original third-person exploration game set in a flooded observatory. Place the player in the lower left looking toward a lit doorway. Reserve the lower right for three ability icons, the upper left for health and the upper right for a small map. Use consistent icon weights and generous spacing. Keep enemies and the traversal route visible; interface elements must not cover the character or objective.
~~~

</details>

<a id="gallery-retro-and-cyberpunk"></a>

<h2 align="center">Retro And Cyberpunk</h2>

[↑ Index](#gallery-index) · [完整分类 / Full atlas](skills/image25/references/gallery-retro-and-cyberpunk.md)

**Image 2.5: 6 · host-model-unknown: 0 · GPT Image 2: 3**

年代技术、城市结构、材质和霓虹色彩层次。检查世界设定一致；不要把霓虹当作唯一风格线索。

<table>
<tr>
<td width="50%" align="center" valign="top"><a href="https://openai.com/index/introducing-chatgpt-images-2-5/"><img src="https://images.ctfassets.net/kftzwdyauwt9/5vY4gdGrJFxuwV8l6GBU03/94befc05806eb290e786473975b3b22b/retrofuturism.png?w=3840&amp;q=90&amp;fm=webp" width="100%" alt="复古未来城市"/></a><br/><strong>复古未来城市</strong><br/><sub>Image 2.5 · 官方示例 · OpenAI</sub></td>
<td width="50%" align="center" valign="top"><a href="https://openai.com/index/introducing-chatgpt-images-2-5/"><img src="https://images.ctfassets.net/kftzwdyauwt9/5siUce5uMdk0FxOA5opjoB/fcfb4452b13c144108f7786a9412f982/cyberpunk.png?w=3840&amp;q=90&amp;fm=webp" width="100%" alt="赛博朋克城市"/></a><br/><strong>赛博朋克城市</strong><br/><sub>Image 2.5 · 官方示例 · OpenAI</sub></td>
</tr>
</table>

<details>
<summary>Prompt · 复古未来城市</summary>

[OpenAI · 原始出处](https://openai.com/index/introducing-chatgpt-images-2-5/) · **Image 2.5 · 官方示例**

[原作者提示词与生成条件](https://openai.com/index/introducing-chatgpt-images-2-5/)

未在本仓库转载完整 Prompt；原页未公开的参数不补造。

</details>

<details>
<summary>Prompt · 赛博朋克城市</summary>

[OpenAI · 原始出处](https://openai.com/index/introducing-chatgpt-images-2-5/) · **Image 2.5 · 官方示例**

[原作者提示词与生成条件](https://openai.com/index/introducing-chatgpt-images-2-5/)

未在本仓库转载完整 Prompt；原页未公开的参数不补造。

</details>

<details><summary>本类起始 Prompt / Original practice brief</summary>

**prompt-only** · 本项目编写，尚未出图；不是上方示例图的原始 Prompt。

~~~text
Create a 16:9 concept board for an original retro-futurist harbor city. Divide it into a large street scene on the left and three stacked detail studies on the right: public phone, transit ticket and raincoat. Use rounded analog controls, enamel signs, copper wiring and weathered glass. Restrict light accents to amber and cyan against charcoal architecture. Repeat the same visual language in all four regions. No borrowed franchise logos or unreadable decorative lettering.
~~~

</details>

<a id="gallery-cinematic-and-animation"></a>

<h2 align="center">Cinematic And Animation</h2>

[↑ Index](#gallery-index) · [完整分类 / Full atlas](skills/image25/references/gallery-cinematic-and-animation.md)

**Image 2.5: 5 · host-model-unknown: 0 · GPT Image 2: 5**

镜头组接、角色连续性、场景时间和灯光。检查轴线、视线、道具及场景光线是否连续。

<table>
<tr>
<td width="50%" align="center" valign="top"><a href="https://github.com/LaplaceYoung/awesome-gpt-image-2.5/blob/9bb515b6b978a7521ae884821a847ab58c11c939/docs/cases/085-imported-q.md"><img src="https://raw.githubusercontent.com/LaplaceYoung/awesome-gpt-image-2.5/9bb515b6b978a7521ae884821a847ab58c11c939/assets/generated/085-imported-q.png" width="100%" alt="Q版求婚场景"/></a><br/><strong>Q版求婚场景</strong><br/><sub>Image 2.5 · 社区作者声明 · LaplaceYoung</sub></td>
<td width="50%" align="center" valign="top"><a href="https://github.com/LaplaceYoung/awesome-gpt-image-2.5/blob/9bb515b6b978a7521ae884821a847ab58c11c939/docs/cases/087-imported-3d-q.md"><img src="https://raw.githubusercontent.com/LaplaceYoung/awesome-gpt-image-2.5/9bb515b6b978a7521ae884821a847ab58c11c939/assets/generated/087-imported-3d-q.png" width="100%" alt="3D Q版风格场景"/></a><br/><strong>3D Q版风格场景</strong><br/><sub>Image 2.5 · 社区作者声明 · LaplaceYoung</sub></td>
</tr>
</table>

<details>
<summary>Prompt · Q版求婚场景</summary>

[LaplaceYoung · 原始出处](https://github.com/LaplaceYoung/awesome-gpt-image-2.5/blob/9bb515b6b978a7521ae884821a847ab58c11c939/docs/cases/085-imported-q.md) · **Image 2.5 · 社区作者声明**

[原作者提示词与生成条件](https://github.com/LaplaceYoung/awesome-gpt-image-2.5/blob/9bb515b6b978a7521ae884821a847ab58c11c939/docs/cases/085-imported-q.md)

未在本仓库转载完整 Prompt；原页未公开的参数不补造。

</details>

<details>
<summary>Prompt · 3D Q版风格场景</summary>

[LaplaceYoung · 原始出处](https://github.com/LaplaceYoung/awesome-gpt-image-2.5/blob/9bb515b6b978a7521ae884821a847ab58c11c939/docs/cases/087-imported-3d-q.md) · **Image 2.5 · 社区作者声明**

[原作者提示词与生成条件](https://github.com/LaplaceYoung/awesome-gpt-image-2.5/blob/9bb515b6b978a7521ae884821a847ab58c11c939/docs/cases/087-imported-3d-q.md)

未在本仓库转载完整 Prompt；原页未公开的参数不补造。

</details>

<details><summary>本类起始 Prompt / Original practice brief</summary>

**prompt-only** · 本项目编写，尚未出图；不是上方示例图的原始 Prompt。

~~~text
Create a six-panel storyboard in a 3 by 2 landscape grid for an original short film: a night-shift baker discovers a small bird in the shop. Show exterior, doorway, medium interaction, hand close-up, reverse angle and final wide shot. Keep the same apron, counter and warm window light in every panel. Use readable pencil-and-marker drawings, equal gutters and small panel numbers 1 through 6. Preserve screen direction and leave captions empty.
~~~

</details>

<a id="gallery-character-design"></a>

<h2 align="center">Character Design</h2>

[↑ Index](#gallery-index) · [完整分类 / Full atlas](skills/image25/references/gallery-character-design.md)

**Image 2.5: 8 · host-model-unknown: 1 · GPT Image 2: 2**

轮廓、比例、服饰结构、视图与表情。逐视图核对配饰位置、左右手和比例。

<table>
<tr>
<td width="50%" align="center" valign="top"><a href="https://reely.art/models/gpt-image-2-5-sunburst"><img src="https://cdn.reely.art/models/gpt-image-2-5/sunburst-character-turnaround.webp" width="100%" alt="角色三视图"/></a><br/><strong>角色三视图</strong><br/><sub>Image 2.5 · 平台声明 · ReelyArt</sub></td>
<td width="50%" align="center" valign="top"><a href="https://github.com/LaplaceYoung/awesome-gpt-image-2.5/blob/9bb515b6b978a7521ae884821a847ab58c11c939/docs/cases/061-imported-3d-q.md"><img src="https://raw.githubusercontent.com/LaplaceYoung/awesome-gpt-image-2.5/9bb515b6b978a7521ae884821a847ab58c11c939/assets/generated/061-imported-3d-q.png" width="100%" alt="3D Q版大学拟人化形象"/></a><br/><strong>3D Q版大学拟人化形象</strong><br/><sub>Image 2.5 · 社区作者声明 · LaplaceYoung</sub></td>
</tr>
</table>

<details>
<summary>Prompt · 角色三视图</summary>

[ReelyArt · 原始出处](https://reely.art/models/gpt-image-2-5-sunburst) · **Image 2.5 · 平台声明**

[原作者提示词与生成条件](https://reely.art/models/gpt-image-2-5-sunburst)

未在本仓库转载完整 Prompt；原页未公开的参数不补造。

</details>

<details>
<summary>Prompt · 3D Q版大学拟人化形象</summary>

[LaplaceYoung · 原始出处](https://github.com/LaplaceYoung/awesome-gpt-image-2.5/blob/9bb515b6b978a7521ae884821a847ab58c11c939/docs/cases/061-imported-3d-q.md) · **Image 2.5 · 社区作者声明**

[原作者提示词与生成条件](https://github.com/LaplaceYoung/awesome-gpt-image-2.5/blob/9bb515b6b978a7521ae884821a847ab58c11c939/docs/cases/061-imported-3d-q.md)

未在本仓库转载完整 Prompt；原页未公开的参数不补造。

</details>

<details><summary>本类起始 Prompt / Original practice brief</summary>

**prompt-only** · 本项目编写，尚未出图；不是上方示例图的原始 Prompt。

~~~text
Create a character reference sheet for an original mountain postal worker. Arrange front, side and back orthographic views on one shared baseline, with four small facial expressions underneath. The worker has a short navy jacket, orange scarf, square canvas satchel and sturdy boots. Preserve exact garment construction, body proportions and the satchel's side in every view. Use clean linework and flat color, a pale background and no dramatic perspective.
~~~

</details>

<a id="gallery-typography-and-posters"></a>

<h2 align="center">Typography And Posters</h2>

[↑ Index](#gallery-index) · [完整分类 / Full atlas](skills/image25/references/gallery-typography-and-posters.md)

**Image 2.5: 18 · host-model-unknown: 1 · GPT Image 2: 13**

文案层级、网格、留白、主视觉和语言。逐字校对标题、日期和价格；禁止额外卖点。

<table>
<tr>
<td width="50%" align="center" valign="top"><a href="https://openai.com/index/introducing-chatgpt-images-2-5/"><img src="https://images.ctfassets.net/kftzwdyauwt9/47GTXbcPJQKPxvuNfyQo5V/1faeee99e4c10ea3042941c7312837b0/mid-century-modern-posters.png?w=3840&amp;q=90&amp;fm=webp" width="100%" alt="现代主义海报组"/></a><br/><strong>现代主义海报组</strong><br/><sub>Image 2.5 · 官方示例 · OpenAI</sub></td>
<td width="50%" align="center" valign="top"><a href="https://reely.art/models/gpt-image-2-5-sunburst"><img src="https://cdn.reely.art/models/gpt-image-2-5/sunburst-exhibition-poster.webp" width="100%" alt="展览文字海报"/></a><br/><strong>展览文字海报</strong><br/><sub>Image 2.5 · 平台声明 · ReelyArt</sub></td>
</tr>
</table>

<details>
<summary>Prompt · 现代主义海报组</summary>

[OpenAI · 原始出处](https://openai.com/index/introducing-chatgpt-images-2-5/) · **Image 2.5 · 官方示例**

[原作者提示词与生成条件](https://openai.com/index/introducing-chatgpt-images-2-5/)

未在本仓库转载完整 Prompt；原页未公开的参数不补造。

</details>

<details>
<summary>Prompt · 展览文字海报</summary>

[ReelyArt · 原始出处](https://reely.art/models/gpt-image-2-5-sunburst) · **Image 2.5 · 平台声明**

[原作者提示词与生成条件](https://reely.art/models/gpt-image-2-5-sunburst)

未在本仓库转载完整 Prompt；原页未公开的参数不补造。

</details>

<details><summary>本类起始 Prompt / Original practice brief</summary>

**prompt-only** · 本项目编写，尚未出图；不是上方示例图的原始 Prompt。

~~~text
Design a 3:4 exhibition poster on warm ivory paper. Set the exact title "夜间植物馆" in large dark-green type across the upper third. Place a single cyanotype fern image in the middle, with generous negative space. At the bottom, align the exact text "NIGHT BOTANICALS" and "09.18 — 10.12" on a strict two-column grid. Use one small vermilion accent. Keep all text legible, without extra slogans or invented sponsor logos.
~~~

</details>

<a id="gallery-illustration"></a>

<h2 align="center">Illustration</h2>

[↑ Index](#gallery-index) · [完整分类 / Full atlas](skills/image25/references/gallery-illustration.md)

**Image 2.5: 6 · host-model-unknown: 1 · GPT Image 2: 2**

故事动作、主体关系、轮廓和媒介边界。检查叙事是否成立；区分插画笔触和摄影质感。

<table>
<tr>
<td width="50%" align="center" valign="top"><a href="https://x.com/BlackthorneAI/status/2097447432757887207"><img src="https://pbs.twimg.com/media/HRuhTWLbsAAne5Y.jpg?name=orig" width="100%" alt="节日主题系列"/></a><br/><strong>节日主题系列</strong><br/><sub>Image 2.5 · X 作者声明 · @BlackthorneAI</sub></td>
<td width="50%" align="center" valign="top"><a href="https://github.com/LaplaceYoung/awesome-gpt-image-2.5/blob/9bb515b6b978a7521ae884821a847ab58c11c939/docs/cases/028-imported-.md"><img src="https://raw.githubusercontent.com/LaplaceYoung/awesome-gpt-image-2.5/9bb515b6b978a7521ae884821a847ab58c11c939/assets/generated/028-imported-.png" width="100%" alt="超现实交互场景"/></a><br/><strong>超现实交互场景</strong><br/><sub>Image 2.5 · 社区作者声明 · LaplaceYoung</sub></td>
</tr>
</table>

<details>
<summary>Prompt · 节日主题系列</summary>

[@BlackthorneAI · 原始出处](https://x.com/BlackthorneAI/status/2097447432757887207) · **Image 2.5 · X 作者声明**

[原作者提示词与生成条件](https://x.com/BlackthorneAI/status/2097447432757887207)

未在本仓库转载完整 Prompt；原页未公开的参数不补造。

</details>

<details>
<summary>Prompt · 超现实交互场景</summary>

[LaplaceYoung · 原始出处](https://github.com/LaplaceYoung/awesome-gpt-image-2.5/blob/9bb515b6b978a7521ae884821a847ab58c11c939/docs/cases/028-imported-.md) · **Image 2.5 · 社区作者声明**

[原作者提示词与生成条件](https://github.com/LaplaceYoung/awesome-gpt-image-2.5/blob/9bb515b6b978a7521ae884821a847ab58c11c939/docs/cases/028-imported-.md)

未在本仓库转载完整 Prompt；原页未公开的参数不补造。

</details>

<details><summary>本类起始 Prompt / Original practice brief</summary>

**prompt-only** · 本项目编写，尚未出图；不是上方示例图的原始 Prompt。

~~~text
Create a landscape editorial illustration of a librarian delivering a book to a tiny rooftop garden. Put the librarian on the right and a waiting child on the left, connected by the passing book. Use layered cut-paper shapes, visible fiber edges, a limited moss-green and coral palette, and soft overlapping shadows. Let rooftop geometry establish depth. Keep the scene legible at thumbnail size and reserve clear space in the upper left for a headline.
~~~

</details>

<a id="gallery-watercolor"></a>

<h2 align="center">Watercolor</h2>

[↑ Index](#gallery-index) · [完整分类 / Full atlas](skills/image25/references/gallery-watercolor.md)

**Image 2.5: 1 · host-model-unknown: 0 · GPT Image 2: 2**

透明罩染、纸白、湿边和色素沉积。避免塑料般高光和统一模糊；保留边缘差异。

<table>
<tr>
<td width="50%" align="center" valign="top"><a href="https://github.com/LaplaceYoung/awesome-gpt-image-2.5/blob/9bb515b6b978a7521ae884821a847ab58c11c939/docs/cases/109-imported-.md"><img src="https://raw.githubusercontent.com/LaplaceYoung/awesome-gpt-image-2.5/9bb515b6b978a7521ae884821a847ab58c11c939/assets/generated/109-imported-.png" width="100%" alt="富士山水彩风格转换"/></a><br/><strong>富士山水彩风格转换</strong><br/><sub>Image 2.5 · 社区作者声明 · LaplaceYoung</sub></td>
</tr>
</table>

<details>
<summary>Prompt · 富士山水彩风格转换</summary>

[LaplaceYoung · 原始出处](https://github.com/LaplaceYoung/awesome-gpt-image-2.5/blob/9bb515b6b978a7521ae884821a847ab58c11c939/docs/cases/109-imported-.md) · **Image 2.5 · 社区作者声明**

[原作者提示词与生成条件](https://github.com/LaplaceYoung/awesome-gpt-image-2.5/blob/9bb515b6b978a7521ae884821a847ab58c11c939/docs/cases/109-imported-.md)

未在本仓库转载完整 Prompt；原页未公开的参数不补造。

</details>

<details><summary>本类起始 Prompt / Original practice brief</summary>

**prompt-only** · 本项目编写，尚未出图；不是上方示例图的原始 Prompt。

~~~text
Paint a quiet greenhouse after rain as a transparent watercolor illustration. Use a landscape frame with a stone path leading toward a small open door. Leave paper white for wet leaves and window reflections. Combine soft wet-on-wet foliage with a few crisp dry-brush edges on pots. Use granulating ultramarine shadows and diluted yellow-green washes. Keep pencil construction faintly visible; avoid photographic sharpness, heavy oil impasto and glossy 3D surfaces.
~~~

</details>

<a id="gallery-ink-and-chinese"></a>

<h2 align="center">Ink And Chinese</h2>

[↑ Index](#gallery-index) · [完整分类 / Full atlas](skills/image25/references/gallery-ink-and-chinese.md)

**Image 2.5: 0 · host-model-unknown: 0 · GPT Image 2: 2**

散点透视、墨色浓淡、留白和题款。题款字数与位置要明确；避免伪汉字。

> 本类暂缺 Image 2.5 来源作品；以下样张的真实型号状态已逐图标注。

<table>
<tr>
<td width="50%" align="center" valign="top"><a href="https://github.com/wuyoscar/GPT-Image2-Skill/blob/135d873e1a843db5f122a15ddda02bd2845d4d25/skills/gpt-image/references/gallery-ink-and-chinese.md"><img src="https://raw.githubusercontent.com/wuyoscar/GPT-Image2-Skill/135d873e1a843db5f122a15ddda02bd2845d4d25/docs/ink-chinese/ink-landscape.png" width="100%" alt="Chinese ink-wash mountain landscape"/></a><br/><strong>Chinese ink-wash mountain landscape</strong><br/><sub>GPT Image 2 · 旧版学习参考 · Wuyoscar / 原页署名作者</sub></td>
<td width="50%" align="center" valign="top"><a href="https://github.com/wuyoscar/GPT-Image2-Skill/blob/135d873e1a843db5f122a15ddda02bd2845d4d25/skills/gpt-image/references/gallery-ink-and-chinese.md"><img src="https://raw.githubusercontent.com/wuyoscar/GPT-Image2-Skill/135d873e1a843db5f122a15ddda02bd2845d4d25/docs/ink-chinese/song-night-market-scroll.png" width="100%" alt="Song dynasty night-market handscroll"/></a><br/><strong>Song dynasty night-market handscroll</strong><br/><sub>GPT Image 2 · 旧版学习参考 · Wuyoscar / 原页署名作者</sub></td>
</tr>
</table>

<details>
<summary>Prompt · Chinese ink-wash mountain landscape</summary>

[Wuyoscar / 原页署名作者 · 原始出处](https://github.com/wuyoscar/GPT-Image2-Skill/blob/135d873e1a843db5f122a15ddda02bd2845d4d25/skills/gpt-image/references/gallery-ink-and-chinese.md) · **GPT Image 2 · 旧版学习参考**

Metadata: Ink & Chinese · `portrait` · `1024x1536` · Author: EvoLinkAI · Source: [GitHub archive](https://github.com/EvoLinkAI/awesome-gpt-image-2-prompts)

~~~text
A traditional Chinese ink-wash (水墨) landscape painting of mist-shrouded mountains, rendered on aged xuan rice paper. Layered mountain ranges receding into distance through gradations of black ink — bold dark foreground peaks with sharp brushwork, mid-ground ranges in medium wash, far peaks almost dissolved into pale grey mist. A single traditional pavilion perched on a cliff midway up, a small solitary figure crossing a wooden bridge over a waterfall. Pine trees with calligraphic branches, curling cloud-mist flowing between peaks (留白 negative-space clouds). A vertical seal stamp in red (篆刻 zhu-wen style) bottom-left, a vertical column of calligraphic characters reading "山高水長" top-right in elegant caoshu (草書) brushwork. Paper has faint warm beige tone with visible fiber texture. Aesthetic in the tradition of 范寬 Fan Kuan / 馬遠 Ma Yuan Song-dynasty landscape painting — contemplative, restrained, deep negative space, brush-energy (气韵) visible in every stroke.
~~~

</details>

<details>
<summary>Prompt · Song dynasty night-market handscroll</summary>

[Wuyoscar / 原页署名作者 · 原始出处](https://github.com/wuyoscar/GPT-Image2-Skill/blob/135d873e1a843db5f122a15ddda02bd2845d4d25/skills/gpt-image/references/gallery-ink-and-chinese.md) · **GPT Image 2 · 旧版学习参考**

Metadata: Ink & Chinese · `landscape` · `1536x1024` · Curated

~~~text
Create a horizontal Chinese ink-and-wash handscroll scene of a Song dynasty riverside night market. Use gongbi-level architectural detail combined with loose ink atmosphere: arched stone bridge, lantern boats, teahouse balconies, book stalls, noodle steam, scholars reading under lamps, children chasing paper rabbits, and distant city walls fading into mist. Add small readable Chinese shop signs in brush style: "茶", "书", "面", "灯市". Palette: black ink, warm lantern ochre, muted cinnabar seals, and pale blue-gray moonlight. Composition should read as a continuous scroll with rhythmic clusters of people and negative-space water. Avoid modern objects, anime faces, fake calligraphy clutter, and overly saturated poster lighting.
~~~

</details>

<details><summary>本类起始 Prompt / Original practice brief</summary>

**prompt-only** · 本项目编写，尚未出图；不是上方示例图的原始 Prompt。

~~~text
Create a long horizontal ink-and-light-color landscape on warm rice paper. Show a river ferry approaching a village beneath distant mountains. Build depth with three overlapping layers, progressively lighter ink and generous untouched paper for mist. Use dry-brush texture for roof tiles and sparse cinnabar accents on lanterns. Reserve a small blank inscription area at the upper right. Keep the brushwork varied and avoid photographic perspective or decorative fake calligraphy.
~~~

</details>

<a id="gallery-pixel-art"></a>

<h2 align="center">Pixel Art</h2>

[↑ Index](#gallery-index) · [完整分类 / Full atlas](skills/image25/references/gallery-pixel-art.md)

**Image 2.5: 2 · host-model-unknown: 0 · GPT Image 2: 2**

逻辑分辨率、调色板、像素簇和帧格。检查像素尺度统一；避免平滑渐变和插值。

<table>
<tr>
<td width="50%" align="center" valign="top"><a href="https://github.com/LaplaceYoung/awesome-gpt-image-2.5/blob/9bb515b6b978a7521ae884821a847ab58c11c939/docs/cases/049-imported-8.md"><img src="https://raw.githubusercontent.com/LaplaceYoung/awesome-gpt-image-2.5/9bb515b6b978a7521ae884821a847ab58c11c939/assets/generated/049-imported-8.png" width="100%" alt="8位像素图标"/></a><br/><strong>8位像素图标</strong><br/><sub>Image 2.5 · 社区作者声明 · LaplaceYoung</sub></td>
<td width="50%" align="center" valign="top"><a href="https://github.com/LaplaceYoung/awesome-gpt-image-2.5/blob/9bb515b6b978a7521ae884821a847ab58c11c939/docs/cases/058-imported-3d.md"><img src="https://raw.githubusercontent.com/LaplaceYoung/awesome-gpt-image-2.5/9bb515b6b978a7521ae884821a847ab58c11c939/assets/generated/058-imported-3d.png" width="100%" alt="体素风格 3D 图标"/></a><br/><strong>体素风格 3D 图标</strong><br/><sub>Image 2.5 · 社区作者声明 · LaplaceYoung</sub></td>
</tr>
</table>

<details>
<summary>Prompt · 8位像素图标</summary>

[LaplaceYoung · 原始出处](https://github.com/LaplaceYoung/awesome-gpt-image-2.5/blob/9bb515b6b978a7521ae884821a847ab58c11c939/docs/cases/049-imported-8.md) · **Image 2.5 · 社区作者声明**

[原作者提示词与生成条件](https://github.com/LaplaceYoung/awesome-gpt-image-2.5/blob/9bb515b6b978a7521ae884821a847ab58c11c939/docs/cases/049-imported-8.md)

未在本仓库转载完整 Prompt；原页未公开的参数不补造。

</details>

<details>
<summary>Prompt · 体素风格 3D 图标</summary>

[LaplaceYoung · 原始出处](https://github.com/LaplaceYoung/awesome-gpt-image-2.5/blob/9bb515b6b978a7521ae884821a847ab58c11c939/docs/cases/058-imported-3d.md) · **Image 2.5 · 社区作者声明**

[原作者提示词与生成条件](https://github.com/LaplaceYoung/awesome-gpt-image-2.5/blob/9bb515b6b978a7521ae884821a847ab58c11c939/docs/cases/058-imported-3d.md)

未在本仓库转载完整 Prompt；原页未公开的参数不补造。

</details>

<details><summary>本类起始 Prompt / Original practice brief</summary>

**prompt-only** · 本项目编写，尚未出图；不是上方示例图的原始 Prompt。

~~~text
Create a pixel-art sprite sheet of an original delivery bicycle in eight directional views. Arrange the views in a 4 by 2 grid with equal 64 by 64 logical-pixel cells and consistent wheel size. Use a restricted sixteen-color palette, crisp nearest-neighbor edges and deliberate pixel clusters. Center every sprite on its cell baseline. Keep the background a flat light gray and avoid antialiasing, blur and continuous gradients.
~~~

</details>

<a id="gallery-isometric"></a>

<h2 align="center">Isometric</h2>

[↑ Index](#gallery-index) · [完整分类 / Full atlas](skills/image25/references/gallery-isometric.md)

**Image 2.5: 6 · host-model-unknown: 1 · GPT Image 2: 2**

轴测角度、比例、剖面和空间布局。平行线不应随意汇聚；检查楼层及通道相连。

<table>
<tr>
<td width="50%" align="center" valign="top"><a href="https://reely.art/models/gpt-image-2-5-sunburst"><img src="https://cdn.reely.art/models/gpt-image-2-5/sunburst-isometric-diorama.webp" width="100%" alt="等距建筑剖面"/></a><br/><strong>等距建筑剖面</strong><br/><sub>Image 2.5 · 平台声明 · ReelyArt</sub></td>
<td width="50%" align="center" valign="top"><a href="https://github.com/LaplaceYoung/awesome-gpt-image-2.5/blob/9bb515b6b978a7521ae884821a847ab58c11c939/docs/cases/033-imported-.md"><img src="https://raw.githubusercontent.com/LaplaceYoung/awesome-gpt-image-2.5/9bb515b6b978a7521ae884821a847ab58c11c939/assets/generated/033-imported-.png" width="100%" alt="乐高城市景观"/></a><br/><strong>乐高城市景观</strong><br/><sub>Image 2.5 · 社区作者声明 · LaplaceYoung</sub></td>
</tr>
</table>

<details>
<summary>Prompt · 等距建筑剖面</summary>

[ReelyArt · 原始出处](https://reely.art/models/gpt-image-2-5-sunburst) · **Image 2.5 · 平台声明**

[原作者提示词与生成条件](https://reely.art/models/gpt-image-2-5-sunburst)

未在本仓库转载完整 Prompt；原页未公开的参数不补造。

</details>

<details>
<summary>Prompt · 乐高城市景观</summary>

[LaplaceYoung · 原始出处](https://github.com/LaplaceYoung/awesome-gpt-image-2.5/blob/9bb515b6b978a7521ae884821a847ab58c11c939/docs/cases/033-imported-.md) · **Image 2.5 · 社区作者声明**

[原作者提示词与生成条件](https://github.com/LaplaceYoung/awesome-gpt-image-2.5/blob/9bb515b6b978a7521ae884821a847ab58c11c939/docs/cases/033-imported-.md)

未在本仓库转载完整 Prompt；原页未公开的参数不补造。

</details>

<details><summary>本类起始 Prompt / Original practice brief</summary>

**prompt-only** · 本项目编写，尚未出图；不是上方示例图的原始 Prompt。

~~~text
Create an isometric cutaway of a two-story neighborhood tea shop on a square canvas. Use consistent parallel axes and a fixed elevated view. The ground floor contains a counter, brewing station and four seats; the upper floor contains a small reading room reached by a visible staircase. Use warm wood, pale plaster and restrained green details. Keep walls cut away cleanly and furniture at a consistent scale, with no impossible connections.
~~~

</details>

<a id="gallery-product-and-food"></a>

<h2 align="center">Product And Food</h2>

[↑ Index](#gallery-index) · [完整分类 / Full atlas](skills/image25/references/gallery-product-and-food.md)

**Image 2.5: 13 · host-model-unknown: 2 · GPT Image 2: 4**

产品几何、材料、布光、接触阴影与食物状态。检查标签、器具结构、重力和食品质地。

<table>
<tr>
<td width="50%" align="center" valign="top"><a href="https://reely.art/models/gpt-image-2-5-sunburst"><img src="https://cdn.reely.art/models/gpt-image-2-5/sunburst-ceramic-caddy.webp" width="100%" alt="陶瓷收纳器"/></a><br/><strong>陶瓷收纳器</strong><br/><sub>Image 2.5 · 平台声明 · ReelyArt</sub></td>
<td width="50%" align="center" valign="top"><a href="https://github.com/LaplaceYoung/awesome-gpt-image-2.5/blob/9bb515b6b978a7521ae884821a847ab58c11c939/docs/cases/019-imported-.md"><img src="https://raw.githubusercontent.com/LaplaceYoung/awesome-gpt-image-2.5/9bb515b6b978a7521ae884821a847ab58c11c939/assets/generated/019-imported-.png" width="100%" alt="实物与手绘涂鸦创意广告"/></a><br/><strong>实物与手绘涂鸦创意广告</strong><br/><sub>Image 2.5 · 社区作者声明 · LaplaceYoung</sub></td>
</tr>
</table>

<details>
<summary>Prompt · 陶瓷收纳器</summary>

[ReelyArt · 原始出处](https://reely.art/models/gpt-image-2-5-sunburst) · **Image 2.5 · 平台声明**

[原作者提示词与生成条件](https://reely.art/models/gpt-image-2-5-sunburst)

未在本仓库转载完整 Prompt；原页未公开的参数不补造。

</details>

<details>
<summary>Prompt · 实物与手绘涂鸦创意广告</summary>

[LaplaceYoung · 原始出处](https://github.com/LaplaceYoung/awesome-gpt-image-2.5/blob/9bb515b6b978a7521ae884821a847ab58c11c939/docs/cases/019-imported-.md) · **Image 2.5 · 社区作者声明**

[原作者提示词与生成条件](https://github.com/LaplaceYoung/awesome-gpt-image-2.5/blob/9bb515b6b978a7521ae884821a847ab58c11c939/docs/cases/019-imported-.md)

未在本仓库转载完整 Prompt；原页未公开的参数不补造。

</details>

<details><summary>本类起始 Prompt / Original practice brief</summary>

**prompt-only** · 本项目编写，尚未出图；不是上方示例图的原始 Prompt。

~~~text
Create a 3:4 studio product photograph of a fictional ceramic tea canister with a cream paper label reading exactly "MORNING LEAF". Place it at a slight three-quarter angle on a pale stone plinth, with two loose tea leaves nearby. Use a large soft key light from the left, a subtle dark reflection on the right and a grounded contact shadow. Preserve realistic ceramic roughness and paper texture. No floating lid, extra labels or unrelated props.
~~~

</details>

<a id="gallery-brand-systems-and-identity"></a>

<h2 align="center">Brand Systems And Identity</h2>

[↑ Index](#gallery-index) · [完整分类 / Full atlas](skills/image25/references/gallery-brand-systems-and-identity.md)

**Image 2.5: 9 · host-model-unknown: 1 · GPT Image 2: 3**

标志、色板、字体、版式与跨触点一致性。同一标志重复出现时不可变形；品牌色和字号层级统一。

<table>
<tr>
<td width="50%" align="center" valign="top"><a href="https://openai.com/index/introducing-chatgpt-images-2-5/"><img src="https://images.ctfassets.net/kftzwdyauwt9/4M5M3sRxcgnYl8Q2M8DZ3y/bc3773f82ae0e68d025e2dca3d5b8f43/vintage-national-park-stamps.png?w=3840&amp;q=90&amp;fm=webp" width="100%" alt="国家公园邮票"/></a><br/><strong>国家公园邮票</strong><br/><sub>Image 2.5 · 官方示例 · OpenAI</sub></td>
<td width="50%" align="center" valign="top"><a href="https://openai.com/index/introducing-chatgpt-images-2-5/"><img src="https://images.ctfassets.net/kftzwdyauwt9/5jpsVIXTvhsaamMRBBygyj/59a740665177515836747b400f52e3fc/stickers.webp?w=3840&amp;q=90&amp;fm=webp" width="100%" alt="贴纸设计"/></a><br/><strong>贴纸设计</strong><br/><sub>Image 2.5 · 官方示例 · OpenAI</sub></td>
</tr>
</table>

<details>
<summary>Prompt · 国家公园邮票</summary>

[OpenAI · 原始出处](https://openai.com/index/introducing-chatgpt-images-2-5/) · **Image 2.5 · 官方示例**

[原作者提示词与生成条件](https://openai.com/index/introducing-chatgpt-images-2-5/)

未在本仓库转载完整 Prompt；原页未公开的参数不补造。

</details>

<details>
<summary>Prompt · 贴纸设计</summary>

[OpenAI · 原始出处](https://openai.com/index/introducing-chatgpt-images-2-5/) · **Image 2.5 · 官方示例**

[原作者提示词与生成条件](https://openai.com/index/introducing-chatgpt-images-2-5/)

未在本仓库转载完整 Prompt；原页未公开的参数不补造。

</details>

<details><summary>本类起始 Prompt / Original practice brief</summary>

**prompt-only** · 本项目编写，尚未出图；不是上方示例图的原始 Prompt。

~~~text
Create a square identity board for a fictional neighborhood bakery called "NORTH CRUMB". Use a modular grid containing a wordmark, three color swatches, a paper bag, a business card and one social announcement. Repeat the same rounded lettering, navy-and-butter palette and wheat motif across all applications. Keep packaging folds realistic and text sparse. Make the logo shape consistent at every scale; avoid unrelated mockups or additional brand names.
~~~

</details>

<a id="gallery-photography"></a>

<h2 align="center">Photography</h2>

[↑ Index](#gallery-index) · [完整分类 / Full atlas](skills/image25/references/gallery-photography.md)

**Image 2.5: 18 · host-model-unknown: 1 · GPT Image 2: 4**

拍摄视角、光比、空间层次和自然细节。不凭画面猜真实设备参数；检查皮肤与反射。

<table>
<tr>
<td width="50%" align="center" valign="top"><a href="https://openai.com/index/introducing-chatgpt-images-2-5/"><img src="https://images.ctfassets.net/kftzwdyauwt9/1oUEzmNEwhlktfQMqWLwTO/cde41dc57991caa0d6b22b35b2d8c70c/80s-headshot.png?w=3840&amp;q=90&amp;fm=webp" width="100%" alt="八十年代肖像"/></a><br/><strong>八十年代肖像</strong><br/><sub>Image 2.5 · 官方示例 · OpenAI</sub></td>
<td width="50%" align="center" valign="top"><a href="https://reely.art/models/gpt-image-2-5-sunburst"><img src="https://cdn.reely.art/models/gpt-image-2-5/sunburst-night-studio.webp" width="100%" alt="夜间工作室"/></a><br/><strong>夜间工作室</strong><br/><sub>Image 2.5 · 平台声明 · ReelyArt</sub></td>
</tr>
</table>

<details>
<summary>Prompt · 八十年代肖像</summary>

[OpenAI · 原始出处](https://openai.com/index/introducing-chatgpt-images-2-5/) · **Image 2.5 · 官方示例**

[原作者提示词与生成条件](https://openai.com/index/introducing-chatgpt-images-2-5/)

未在本仓库转载完整 Prompt；原页未公开的参数不补造。

</details>

<details>
<summary>Prompt · 夜间工作室</summary>

[ReelyArt · 原始出处](https://reely.art/models/gpt-image-2-5-sunburst) · **Image 2.5 · 平台声明**

[原作者提示词与生成条件](https://reely.art/models/gpt-image-2-5-sunburst)

未在本仓库转载完整 Prompt；原页未公开的参数不补造。

</details>

<details><summary>本类起始 Prompt / Original practice brief</summary>

**prompt-only** · 本项目编写，尚未出图；不是上方示例图的原始 Prompt。

~~~text
Create an environmental portrait of an adult bookbinder beside a workshop window on an overcast morning. Frame from the waist up, with the person slightly right of center and a workbench in the foreground. Use soft side light, natural skin texture, gently compressed perspective and a modest depth of field that keeps the tools recognizable. Include worn linen, paper dust and small hand imperfections. Avoid beauty-filter skin and overly cinematic neon lighting.
~~~

</details>

<a id="gallery-screen-photography"></a>

<h2 align="center">Screen Photography</h2>

[↑ Index](#gallery-index) · [完整分类 / Full atlas](skills/image25/references/gallery-screen-photography.md)

**Image 2.5: 3 · host-model-unknown: 0 · GPT Image 2: 2**

实体设备、拍摄角度、反光和屏幕内容。区分真实拍屏与截图；保持屏幕透视一致。

<table>
<tr>
<td width="50%" align="center" valign="top"><a href="https://reely.art/models/gpt-image-2-5-sunburst"><img src="https://cdn.reely.art/models/gpt-image-2-5/sunburst-desk-mockup.webp" width="100%" alt="显示器界面样机"/></a><br/><strong>显示器界面样机</strong><br/><sub>Image 2.5 · 平台声明 · ReelyArt</sub></td>
<td width="50%" align="center" valign="top"><a href="https://reely.art/models/gpt-image-2-5-sunburst"><img src="https://cdn.reely.art/models/gpt-image-2-5/sunburst-phone-in-hand.webp" width="100%" alt="手机屏幕文字"/></a><br/><strong>手机屏幕文字</strong><br/><sub>Image 2.5 · 平台声明 · ReelyArt</sub></td>
</tr>
</table>

<details>
<summary>Prompt · 显示器界面样机</summary>

[ReelyArt · 原始出处](https://reely.art/models/gpt-image-2-5-sunburst) · **Image 2.5 · 平台声明**

[原作者提示词与生成条件](https://reely.art/models/gpt-image-2-5-sunburst)

未在本仓库转载完整 Prompt；原页未公开的参数不补造。

</details>

<details>
<summary>Prompt · 手机屏幕文字</summary>

[ReelyArt · 原始出处](https://reely.art/models/gpt-image-2-5-sunburst) · **Image 2.5 · 平台声明**

[原作者提示词与生成条件](https://reely.art/models/gpt-image-2-5-sunburst)

未在本仓库转载完整 Prompt；原页未公开的参数不补造。

</details>

<details><summary>本类起始 Prompt / Original practice brief</summary>

**prompt-only** · 本项目编写，尚未出图；不是上方示例图的原始 Prompt。

~~~text
Create a candid photograph of an open laptop on a wooden desk at night, viewed slightly from above. Show a fictional music library on screen with the exact heading "Evening Library" and three readable playlist rows. Include the keyboard edge, faint room reflections on the glass and a small warm desk lamp. Keep the displayed interface aligned to the screen plane. Use subtle sensor grain, avoiding exaggerated moire or a perfectly flat screenshot appearance.
~~~

</details>

<a id="gallery-infographics-and-field-guides"></a>

<h2 align="center">Infographics And Field Guides</h2>

[↑ Index](#gallery-index) · [完整分类 / Full atlas](skills/image25/references/gallery-infographics-and-field-guides.md)

**Image 2.5: 4 · host-model-unknown: 1 · GPT Image 2: 8**

知识分区、阅读路径、注释和图例。核对事实与数值；图像不能代替专业内容审阅。

<table>
<tr>
<td width="50%" align="center" valign="top"><a href="https://github.com/LaplaceYoung/awesome-gpt-image-2.5/blob/9bb515b6b978a7521ae884821a847ab58c11c939/docs/cases/025-imported-.md"><img src="https://raw.githubusercontent.com/LaplaceYoung/awesome-gpt-image-2.5/9bb515b6b978a7521ae884821a847ab58c11c939/assets/generated/025-imported-.png" width="100%" alt="儿童涂色页插画"/></a><br/><strong>儿童涂色页插画</strong><br/><sub>Image 2.5 · 社区作者声明 · LaplaceYoung</sub></td>
<td width="50%" align="center" valign="top"><a href="https://github.com/LaplaceYoung/awesome-gpt-image-2.5/blob/9bb515b6b978a7521ae884821a847ab58c11c939/docs/cases/031-imported-.md"><img src="https://raw.githubusercontent.com/LaplaceYoung/awesome-gpt-image-2.5/9bb515b6b978a7521ae884821a847ab58c11c939/assets/generated/031-imported-.png" width="100%" alt="特色城市天气预报"/></a><br/><strong>特色城市天气预报</strong><br/><sub>Image 2.5 · 社区作者声明 · LaplaceYoung</sub></td>
</tr>
</table>

<details>
<summary>Prompt · 儿童涂色页插画</summary>

[LaplaceYoung · 原始出处](https://github.com/LaplaceYoung/awesome-gpt-image-2.5/blob/9bb515b6b978a7521ae884821a847ab58c11c939/docs/cases/025-imported-.md) · **Image 2.5 · 社区作者声明**

[原作者提示词与生成条件](https://github.com/LaplaceYoung/awesome-gpt-image-2.5/blob/9bb515b6b978a7521ae884821a847ab58c11c939/docs/cases/025-imported-.md)

未在本仓库转载完整 Prompt；原页未公开的参数不补造。

</details>

<details>
<summary>Prompt · 特色城市天气预报</summary>

[LaplaceYoung · 原始出处](https://github.com/LaplaceYoung/awesome-gpt-image-2.5/blob/9bb515b6b978a7521ae884821a847ab58c11c939/docs/cases/031-imported-.md) · **Image 2.5 · 社区作者声明**

[原作者提示词与生成条件](https://github.com/LaplaceYoung/awesome-gpt-image-2.5/blob/9bb515b6b978a7521ae884821a847ab58c11c939/docs/cases/031-imported-.md)

未在本仓库转载完整 Prompt；原页未公开的参数不补造。

</details>

<details><summary>本类起始 Prompt / Original practice brief</summary>

**prompt-only** · 本项目编写，尚未出图；不是上方示例图的原始 Prompt。

~~~text
Design a vertical field-guide card about a fictional alpine flower named "Silver Bell". Use four clear regions: title, large labeled specimen, habitat sketch and three care notes. Draw thin leader lines to leaf, stem and blossom without crossings. Keep the palette restrained and use large readable labels. Clearly mark the card "FICTIONAL SPECIMEN". Leave data fields blank for supplied facts rather than inventing biological claims.
~~~

</details>

<a id="gallery-research-paper-figures"></a>

<h2 align="center">Research Paper Figures</h2>

[↑ Index](#gallery-index) · [完整分类 / Full atlas](skills/image25/references/gallery-research-paper-figures.md)

**Image 2.5: 2 · host-model-unknown: 0 · GPT Image 2: 21**

节点关系、图形语法、模块与数据依据。生成图仅作构思；正式结果图需用真实数据和绘图工具。

<table>
<tr>
<td width="50%" align="center" valign="top"><a href="https://openai.com/index/introducing-chatgpt-images-2-5/"><img src="https://images.ctfassets.net/kftzwdyauwt9/4IPoFYxHjVAfoZ4ZmKO1VX/25a75228d3dcaf8ae9369467a06a5281/presentation-image.webp?w=3840&amp;q=90&amp;fm=webp" width="100%" alt="演示文稿视觉"/></a><br/><strong>演示文稿视觉</strong><br/><sub>Image 2.5 · 官方示例 · OpenAI</sub></td>
<td width="50%" align="center" valign="top"><a href="https://github.com/LaplaceYoung/awesome-gpt-image-2.5/blob/9bb515b6b978a7521ae884821a847ab58c11c939/docs/cases/09-presentation-image.md"><img src="https://raw.githubusercontent.com/LaplaceYoung/awesome-gpt-image-2.5/9bb515b6b978a7521ae884821a847ab58c11c939/assets/generated/09-presentation-image.jpg" width="100%" alt="Science Deck Screenshot"/></a><br/><strong>Science Deck Screenshot</strong><br/><sub>Image 2.5 · 社区作者声明 · LaplaceYoung</sub></td>
</tr>
</table>

<details>
<summary>Prompt · 演示文稿视觉</summary>

[OpenAI · 原始出处](https://openai.com/index/introducing-chatgpt-images-2-5/) · **Image 2.5 · 官方示例**

[原作者提示词与生成条件](https://openai.com/index/introducing-chatgpt-images-2-5/)

未在本仓库转载完整 Prompt；原页未公开的参数不补造。

</details>

<details>
<summary>Prompt · Science Deck Screenshot</summary>

[LaplaceYoung · 原始出处](https://github.com/LaplaceYoung/awesome-gpt-image-2.5/blob/9bb515b6b978a7521ae884821a847ab58c11c939/docs/cases/09-presentation-image.md) · **Image 2.5 · 社区作者声明**

[原作者提示词与生成条件](https://github.com/LaplaceYoung/awesome-gpt-image-2.5/blob/9bb515b6b978a7521ae884821a847ab58c11c939/docs/cases/09-presentation-image.md)

未在本仓库转载完整 Prompt；原页未公开的参数不补造。

</details>

<details><summary>本类起始 Prompt / Original practice brief</summary>

**prompt-only** · 本项目编写，尚未出图；不是上方示例图的原始 Prompt。

~~~text
Create a landscape conceptual method diagram for a fictional document retrieval system. Arrange four modules from left to right labeled exactly "Documents", "Index", "Retriever" and "Answer". Show one arrow between neighboring modules and a separate query entering the retriever from above. Use a white background, slate outlines and one teal highlight. Keep all labels large and relationships unambiguous. Do not invent benchmark values, error bars, citations or experimental results.
~~~

</details>

<a id="gallery-official-openai-cookbook-examples"></a>

<h2 align="center">Official Openai Cookbook Examples</h2>

[↑ Index](#gallery-index) · [完整分类 / Full atlas](skills/image25/references/gallery-official-openai-cookbook-examples.md)

**Image 2.5: 12 · host-model-unknown: 0 · GPT Image 2: 4**

官方样例、原始出处与可复用约束。区分官方展示、指南与可执行参数。

<table>
<tr>
<td width="50%" align="center" valign="top"><a href="https://openai.com/index/introducing-chatgpt-images-2-5/"><img src="https://images.ctfassets.net/kftzwdyauwt9/5vY4gdGrJFxuwV8l6GBU03/94befc05806eb290e786473975b3b22b/retrofuturism.png?w=3840&amp;q=90&amp;fm=webp" width="100%" alt="复古未来城市"/></a><br/><strong>复古未来城市</strong><br/><sub>Image 2.5 · 官方示例 · OpenAI</sub></td>
<td width="50%" align="center" valign="top"><a href="https://openai.com/index/introducing-chatgpt-images-2-5/"><img src="https://images.ctfassets.net/kftzwdyauwt9/47GTXbcPJQKPxvuNfyQo5V/1faeee99e4c10ea3042941c7312837b0/mid-century-modern-posters.png?w=3840&amp;q=90&amp;fm=webp" width="100%" alt="现代主义海报组"/></a><br/><strong>现代主义海报组</strong><br/><sub>Image 2.5 · 官方示例 · OpenAI</sub></td>
</tr>
</table>

<details>
<summary>Prompt · 复古未来城市</summary>

[OpenAI · 原始出处](https://openai.com/index/introducing-chatgpt-images-2-5/) · **Image 2.5 · 官方示例**

[原作者提示词与生成条件](https://openai.com/index/introducing-chatgpt-images-2-5/)

未在本仓库转载完整 Prompt；原页未公开的参数不补造。

</details>

<details>
<summary>Prompt · 现代主义海报组</summary>

[OpenAI · 原始出处](https://openai.com/index/introducing-chatgpt-images-2-5/) · **Image 2.5 · 官方示例**

[原作者提示词与生成条件](https://openai.com/index/introducing-chatgpt-images-2-5/)

未在本仓库转载完整 Prompt；原页未公开的参数不补造。

</details>

<details><summary>本类起始 Prompt / Original practice brief</summary>

**prompt-only** · 本项目编写，尚未出图；不是上方示例图的原始 Prompt。

~~~text
Create a clean logo exploration sheet for an original plant-care service named "STEM ROOM". Present three distinct concepts in one horizontal row, each combining a simple leaf symbol with the same exact wordmark. Use dark green on an ivory background and maintain equal visual scale. Keep shapes readable at small sizes and avoid gradients. This is an original practice prompt, not a quoted official prompt.
~~~

</details>

<a id="gallery-edit-endpoint-showcase"></a>

<h2 align="center">Edit Endpoint Showcase</h2>

[↑ Index](#gallery-index) · [完整分类 / Full atlas](skills/image25/references/gallery-edit-endpoint-showcase.md)

**Image 2.5: 7 · host-model-unknown: 2 · GPT Image 2: 2**

输入编号、修改范围、不可变项与蒙版。对照输入检查身份、文字、布局及边界变化。

<table>
<tr>
<td width="50%" align="center" valign="top"><a href="https://openai.com/index/introducing-chatgpt-images-2-5/"><img src="https://images.ctfassets.net/kftzwdyauwt9/31fyboLGIlu5roN22tlEHK/9be57d84b3b7bbf22e7aa7f74b5af102/baby-portrait-after.webp" width="100%" alt="人物服装编辑"/></a><br/><strong>人物服装编辑</strong><br/><sub>Image 2.5 · 官方示例 · OpenAI</sub></td>
<td width="50%" align="center" valign="top"><a href="https://reely.art/models/gpt-image-2-5-sunburst"><img src="https://cdn.reely.art/models/gpt-image-2-5/sunburst-label-edit.webp" width="100%" alt="产品标签编辑"/></a><br/><strong>产品标签编辑</strong><br/><sub>Image 2.5 · 平台声明 · ReelyArt</sub></td>
</tr>
</table>

<details>
<summary>Prompt · 人物服装编辑</summary>

[OpenAI · 原始出处](https://openai.com/index/introducing-chatgpt-images-2-5/) · **Image 2.5 · 官方示例**

[原作者提示词与生成条件](https://openai.com/index/introducing-chatgpt-images-2-5/)

未在本仓库转载完整 Prompt；原页未公开的参数不补造。

</details>

<details>
<summary>Prompt · 产品标签编辑</summary>

[ReelyArt · 原始出处](https://reely.art/models/gpt-image-2-5-sunburst) · **Image 2.5 · 平台声明**

[原作者提示词与生成条件](https://reely.art/models/gpt-image-2-5-sunburst)

未在本仓库转载完整 Prompt；原页未公开的参数不补造。

</details>

<details><summary>本类起始 Prompt / Original practice brief</summary>

**prompt-only** · 本项目编写，尚未出图；不是上方示例图的原始 Prompt。

~~~text
Edit image 1 by changing only the scarf to a mustard-yellow knitted scarf. Preserve the subject's face, pose, fur or hair, clothing, background, framing and light direction. Match the scarf's shadows and folds to the existing scene. Do not add accessories, crop the image or alter text. Treat any supplied mask as the intended edit region, then inspect the entire result for unintended changes.
~~~

</details>

<a id="gallery-ui-ux-mockups"></a>

<h2 align="center">Ui Ux Mockups</h2>

[↑ Index](#gallery-index) · [完整分类 / Full atlas](skills/image25/references/gallery-ui-ux-mockups.md)

**Image 2.5: 4 · host-model-unknown: 1 · GPT Image 2: 5**

屏幕规格、信息架构、组件、状态和数据。检查对齐、中文可读性和组件一致性；设计图不等于可运行界面。

<table>
<tr>
<td width="50%" align="center" valign="top"><a href="https://github.com/LaplaceYoung/awesome-gpt-image-2.5/blob/9bb515b6b978a7521ae884821a847ab58c11c939/docs/cases/045-imported-.md"><img src="https://raw.githubusercontent.com/LaplaceYoung/awesome-gpt-image-2.5/9bb515b6b978a7521ae884821a847ab58c11c939/assets/generated/045-imported-.png" width="100%" alt="虚构推文截图"/></a><br/><strong>虚构推文截图</strong><br/><sub>Image 2.5 · 社区作者声明 · LaplaceYoung</sub></td>
<td width="50%" align="center" valign="top"><a href="https://github.com/LaplaceYoung/awesome-gpt-image-2.5/blob/9bb515b6b978a7521ae884821a847ab58c11c939/docs/cases/140-x-open-source-ai-index.md"><img src="https://raw.githubusercontent.com/LaplaceYoung/awesome-gpt-image-2.5/9bb515b6b978a7521ae884821a847ab58c11c939/assets/generated/140-x-open-source-ai-index.png" width="100%" alt="X Open Source AI Index UI"/></a><br/><strong>X Open Source AI Index UI</strong><br/><sub>Image 2.5 · 社区作者声明 · LaplaceYoung</sub></td>
</tr>
</table>

<details>
<summary>Prompt · 虚构推文截图</summary>

[LaplaceYoung · 原始出处](https://github.com/LaplaceYoung/awesome-gpt-image-2.5/blob/9bb515b6b978a7521ae884821a847ab58c11c939/docs/cases/045-imported-.md) · **Image 2.5 · 社区作者声明**

[原作者提示词与生成条件](https://github.com/LaplaceYoung/awesome-gpt-image-2.5/blob/9bb515b6b978a7521ae884821a847ab58c11c939/docs/cases/045-imported-.md)

未在本仓库转载完整 Prompt；原页未公开的参数不补造。

</details>

<details>
<summary>Prompt · X Open Source AI Index UI</summary>

[LaplaceYoung · 原始出处](https://github.com/LaplaceYoung/awesome-gpt-image-2.5/blob/9bb515b6b978a7521ae884821a847ab58c11c939/docs/cases/140-x-open-source-ai-index.md) · **Image 2.5 · 社区作者声明**

[原作者提示词与生成条件](https://github.com/LaplaceYoung/awesome-gpt-image-2.5/blob/9bb515b6b978a7521ae884821a847ab58c11c939/docs/cases/140-x-open-source-ai-index.md)

未在本仓库转载完整 Prompt；原页未公开的参数不补造。

</details>

<details><summary>本类起始 Prompt / Original practice brief</summary>

**prompt-only** · 本项目编写，尚未出图；不是上方示例图的原始 Prompt。

~~~text
Design a front-facing desktop workspace UI for a fictional research app called "FIELD NOTES" on a 16:10 canvas. Allocate a narrow left navigation rail, a central document list and a right reading panel. Use an eight-point spacing rhythm, clear selected states and a calm ivory-and-sage palette. Include the exact navigation labels "Library", "Projects" and "Archive". Keep rows aligned and avoid decorative device frames or impossible interactive controls.
~~~

</details>

<a id="gallery-data-visualization"></a>

<h2 align="center">Data Visualization</h2>

[↑ Index](#gallery-index) · [完整分类 / Full atlas](skills/image25/references/gallery-data-visualization.md)

**Image 2.5: 0 · host-model-unknown: 0 · GPT Image 2: 5**

数据表、视觉编码、坐标、图例与不确定性。核对数值和比例；有真实数据时优先确定性绘图。

> 本类暂缺 Image 2.5 来源作品；以下样张的真实型号状态已逐图标注。

<table>
<tr>
<td width="50%" align="center" valign="top"><a href="https://github.com/wuyoscar/GPT-Image2-Skill/blob/135d873e1a843db5f122a15ddda02bd2845d4d25/skills/gpt-image/references/gallery-data-visualization.md"><img src="https://raw.githubusercontent.com/wuyoscar/GPT-Image2-Skill/135d873e1a843db5f122a15ddda02bd2845d4d25/docs/data-visualization/small-multiples-climate-grid.png" width="100%" alt="Small Multiples Climate Grid"/></a><br/><strong>Small Multiples Climate Grid</strong><br/><sub>GPT Image 2 · 旧版学习参考 · Wuyoscar / 原页署名作者</sub></td>
<td width="50%" align="center" valign="top"><a href="https://github.com/wuyoscar/GPT-Image2-Skill/blob/135d873e1a843db5f122a15ddda02bd2845d4d25/skills/gpt-image/references/gallery-data-visualization.md"><img src="https://raw.githubusercontent.com/wuyoscar/GPT-Image2-Skill/135d873e1a843db5f122a15ddda02bd2845d4d25/docs/data-visualization/network-graph-collaboration-map.png" width="100%" alt="Network Graph Collaboration Map"/></a><br/><strong>Network Graph Collaboration Map</strong><br/><sub>GPT Image 2 · 旧版学习参考 · Wuyoscar / 原页署名作者</sub></td>
</tr>
</table>

<details>
<summary>Prompt · Small Multiples Climate Grid</summary>

[Wuyoscar / 原页署名作者 · 原始出处](https://github.com/wuyoscar/GPT-Image2-Skill/blob/135d873e1a843db5f122a15ddda02bd2845d4d25/skills/gpt-image/references/gallery-data-visualization.md) · **GPT Image 2 · 旧版学习参考**

Metadata: Data Visualization · `wide` · `2048x1152` · Curated

~~~text
Produce a clean editorial data visualization poster showing a 4x3 small-multiples grid of monthly climate charts for 12 fictional cities. Use a white background, generous margins, and a restrained palette of navy, rust, sky blue, olive, and charcoal. Each mini-panel should contain a temperature line and precipitation bars with consistent axes and ultra-legible labels. Include a title block with the in-image text "Annual Climate Profiles" and subtitle "12 Cities, 2025". Label panels "Northport", "Solmere", "Aster Bay", "Ridgefall", "Halcyon", "Verdin", "Glass Harbor", "Red Mesa", "Moonfield", "Lake Arden", "Cinder Point", and "Juniper". Use month labels "J F M A M J J A S O N D" and axis labels "Temp °C" and "Rain mm". Add numeric legend values "0", "10", "20", "30", and "100". Keep the composition highly structured, scientifically clear, and visually elegant, with crisp typography, aligned scales, and publication-grade chart rendering.
~~~

</details>

<details>
<summary>Prompt · Network Graph Collaboration Map</summary>

[Wuyoscar / 原页署名作者 · 原始出处](https://github.com/wuyoscar/GPT-Image2-Skill/blob/135d873e1a843db5f122a15ddda02bd2845d4d25/skills/gpt-image/references/gallery-data-visualization.md) · **GPT Image 2 · 旧版学习参考**

Metadata: Data Visualization · `landscape` · `1536x1024` · Curated

~~~text
Generate a sophisticated network graph visualization on a dark charcoal canvas showing collaborations across a fictional research consortium called ORBIT GRID. Use glowing node colors in teal, amber, coral, pale blue, and white, with fine connecting lines and clean labels. The composition should be balanced, readable, and intentionally designed rather than random. Include a title in crisp text reading "ORBIT GRID Collaboration Network" and a legend with "Institute", "Lab", "Project", and "Advisory". Show approximately 36 nodes, with larger hubs labeled "Helix Center", "Nova Lab", "Aster Institute", "Cinder Bio", and "Polar Systems". Add edge labels sparingly, such as "shared data", "joint grant", and "coauthor". Include a right-side stats card reading "Nodes 36", "Edges 92", and "Density 0.146". Emphasize clean hierarchy, accurate node-label placement, anti-overlap spacing, subtle depth, and crisp typography suited for a polished technical visualization generated by gpt-image-2.
~~~

</details>

<details><summary>本类起始 Prompt / Original practice brief</summary>

**prompt-only** · 本项目编写，尚未出图；不是上方示例图的原始 Prompt。

~~~text
Create a conceptual data-visualization style board with three clearly labeled chart placeholders: "Monthly trend", "Category share" and "Regional comparison". Use consistent typography, a white background, restrained blue accents and accessible contrast. Leave numeric values and plotted results blank for real data. Show clear axis and legend positions. Mark the board "LAYOUT STUDY"; do not fabricate measurements or suggest this is an actual analysis.
~~~

</details>

<a id="gallery-technical-illustration"></a>

<h2 align="center">Technical Illustration</h2>

[↑ Index](#gallery-index) · [完整分类 / Full atlas](skills/image25/references/gallery-technical-illustration.md)

**Image 2.5: 0 · host-model-unknown: 0 · GPT Image 2: 5**

部件顺序、装配轴、连接关系和标注。核对部件是否可装配；概念图不能作为生产图纸。

> 本类暂缺 Image 2.5 来源作品；以下样张的真实型号状态已逐图标注。

<table>
<tr>
<td width="50%" align="center" valign="top"><a href="https://github.com/wuyoscar/GPT-Image2-Skill/blob/135d873e1a843db5f122a15ddda02bd2845d4d25/skills/gpt-image/references/gallery-technical-illustration.md"><img src="https://raw.githubusercontent.com/wuyoscar/GPT-Image2-Skill/135d873e1a843db5f122a15ddda02bd2845d4d25/docs/technical-illustration/mechanical-watch-exploded-view.png" width="100%" alt="Mechanical Watch Exploded View"/></a><br/><strong>Mechanical Watch Exploded View</strong><br/><sub>GPT Image 2 · 旧版学习参考 · Wuyoscar / 原页署名作者</sub></td>
<td width="50%" align="center" valign="top"><a href="https://github.com/wuyoscar/GPT-Image2-Skill/blob/135d873e1a843db5f122a15ddda02bd2845d4d25/skills/gpt-image/references/gallery-technical-illustration.md"><img src="https://raw.githubusercontent.com/wuyoscar/GPT-Image2-Skill/135d873e1a843db5f122a15ddda02bd2845d4d25/docs/technical-illustration/rocket-cutaway-launch-vehicle.png" width="100%" alt="Rocket Cutaway Diagram"/></a><br/><strong>Rocket Cutaway Diagram</strong><br/><sub>GPT Image 2 · 旧版学习参考 · Wuyoscar / 原页署名作者</sub></td>
</tr>
</table>

<details>
<summary>Prompt · Mechanical Watch Exploded View</summary>

[Wuyoscar / 原页署名作者 · 原始出处](https://github.com/wuyoscar/GPT-Image2-Skill/blob/135d873e1a843db5f122a15ddda02bd2845d4d25/skills/gpt-image/references/gallery-technical-illustration.md) · **GPT Image 2 · 旧版学习参考**

Metadata: Technical Illustration · `square` · `1024x1024` · Curated

~~~text
Create a premium technical exploded-view illustration of a fictional mechanical wristwatch called the Meridian 8, centered on a dark slate background with fine blueprint grid accents. Show the watch components separated vertically with precise spacing: sapphire crystal, dial, hands, chapter ring, movement plates, escapement, balance wheel, mainspring barrel, case, crown, and leather strap sections. Use realistic brushed steel, brass, ruby jewel accents, and deep navy dial details. Add crisp callouts and labels with the in-image text "Meridian 8", "Exploded Assembly", "42 mm Case", "25 Jewels", and "Power Reserve 72 h". Include numbered callouts "01" through "10" with short labels like "Balance Wheel", "Mainspring Barrel", and "Sapphire Crystal". The result should be highly detailed, technically believable, sharply rendered, and suitable for an industrial design plate with clean hierarchy, exact labeling, and refined material realism.
~~~

</details>

<details>
<summary>Prompt · Rocket Cutaway Diagram</summary>

[Wuyoscar / 原页署名作者 · 原始出处](https://github.com/wuyoscar/GPT-Image2-Skill/blob/135d873e1a843db5f122a15ddda02bd2845d4d25/skills/gpt-image/references/gallery-technical-illustration.md) · **GPT Image 2 · 旧版学习参考**

Metadata: Technical Illustration · `tall` · `2160x3840` · Curated

~~~text
Generate a highly detailed vertical cutaway illustration of a fictional two-stage launch vehicle named Aster-9 on a clean white technical background. Show the full rocket from nose cone to engines, sliced to reveal internal tanks, avionics, payload fairing, interstage, turbopumps, and thrust structure. Use a restrained palette of white, gunmetal, orange, pale blue, and safety red accents. Add precise leader lines and crisp labels. Include in-image text: "ASTER-9", "Payload 8,400 kg", "Height 62.4 m", "Stage 1 RP-1 / LOX", and "Stage 2 Methalox". Label internal parts such as "Payload Bay", "Guidance Computer", "LOX Tank", "Fuel Tank", "Helium COPV", and "Engine Cluster x9". Add a small scale marker with "0 m", "20 m", "40 m", and "60 m". Prioritize accurate engineering-diagram composition, clean typography, believable hardware detail, and razor-sharp annotations optimized for gpt-image-2.
~~~

</details>

<details><summary>本类起始 Prompt / Original practice brief</summary>

**prompt-only** · 本项目编写，尚未出图；不是上方示例图的原始 Prompt。

~~~text
Create an exploded-view concept illustration of a fictional mechanical desk timer. Align the outer case, dial, hands, gear assembly and back cover along one central assembly axis. Use a pale technical background, restrained material colors and thin numbered leader lines that do not cross. Keep corresponding screw holes aligned. Label it "CONCEPT ASSEMBLY" and avoid dimensions or manufacturing claims that were not supplied.
~~~

</details>

<a id="gallery-architecture-and-interior"></a>

<h2 align="center">Architecture And Interior</h2>

[↑ Index](#gallery-index) · [完整分类 / Full atlas](skills/image25/references/gallery-architecture-and-interior.md)

**Image 2.5: 1 · host-model-unknown: 1 · GPT Image 2: 5**

空间功能、尺度、消失点、材料与光向。检查门窗、楼梯和家具尺度；效果图不等于施工设计。

<table>
<tr>
<td width="50%" align="center" valign="top"><a href="https://github.com/LaplaceYoung/awesome-gpt-image-2.5/blob/9bb515b6b978a7521ae884821a847ab58c11c939/docs/cases/083-imported-.md"><img src="https://raw.githubusercontent.com/LaplaceYoung/awesome-gpt-image-2.5/9bb515b6b978a7521ae884821a847ab58c11c939/assets/generated/083-imported-.png" width="100%" alt="个性化房间设计"/></a><br/><strong>个性化房间设计</strong><br/><sub>Image 2.5 · 社区作者声明 · LaplaceYoung</sub></td>
</tr>
</table>

<details>
<summary>Prompt · 个性化房间设计</summary>

[LaplaceYoung · 原始出处](https://github.com/LaplaceYoung/awesome-gpt-image-2.5/blob/9bb515b6b978a7521ae884821a847ab58c11c939/docs/cases/083-imported-.md) · **Image 2.5 · 社区作者声明**

[原作者提示词与生成条件](https://github.com/LaplaceYoung/awesome-gpt-image-2.5/blob/9bb515b6b978a7521ae884821a847ab58c11c939/docs/cases/083-imported-.md)

未在本仓库转载完整 Prompt；原页未公开的参数不补造。

</details>

<details><summary>本类起始 Prompt / Original practice brief</summary>

**prompt-only** · 本项目编写，尚未出图；不是上方示例图的原始 Prompt。

~~~text
Create a photorealistic architectural concept of a small neighborhood reading room in a renovated brick building. Use a level eye-height view, one clear vanishing point and soft afternoon light entering from the left. Include a long oak table, wall shelves and an accessible uncluttered aisle. Show brick, linen and matte plaster distinctly. Keep furniture at plausible scale and avoid stairs, doors or windows that lead nowhere.
~~~

</details>

<a id="gallery-scientific-and-educational"></a>

<h2 align="center">Scientific And Educational</h2>

[↑ Index](#gallery-index) · [完整分类 / Full atlas](skills/image25/references/gallery-scientific-and-educational.md)

**Image 2.5: 1 · host-model-unknown: 0 · GPT Image 2: 7**

对象结构、标注精度、图例与教学顺序。科学内容由可靠资料提供；避免生成伪知识。

<table>
<tr>
<td width="50%" align="center" valign="top"><a href="https://github.com/LaplaceYoung/awesome-gpt-image-2.5/blob/9bb515b6b978a7521ae884821a847ab58c11c939/docs/cases/030-imported-.md"><img src="https://raw.githubusercontent.com/LaplaceYoung/awesome-gpt-image-2.5/9bb515b6b978a7521ae884821a847ab58c11c939/assets/generated/030-imported-.png" width="100%" alt="发光线条解剖图"/></a><br/><strong>发光线条解剖图</strong><br/><sub>Image 2.5 · 社区作者声明 · LaplaceYoung</sub></td>
</tr>
</table>

<details>
<summary>Prompt · 发光线条解剖图</summary>

[LaplaceYoung · 原始出处](https://github.com/LaplaceYoung/awesome-gpt-image-2.5/blob/9bb515b6b978a7521ae884821a847ab58c11c939/docs/cases/030-imported-.md) · **Image 2.5 · 社区作者声明**

[原作者提示词与生成条件](https://github.com/LaplaceYoung/awesome-gpt-image-2.5/blob/9bb515b6b978a7521ae884821a847ab58c11c939/docs/cases/030-imported-.md)

未在本仓库转载完整 Prompt；原页未公开的参数不补造。

</details>

<details><summary>本类起始 Prompt / Original practice brief</summary>

**prompt-only** · 本项目编写，尚未出图；不是上方示例图的原始 Prompt。

~~~text
Create an educational layout study explaining the water cycle in a simple landscape diagram. Place ocean at left, mountains at right and clouds above. Use four large exact labels: "Evaporation", "Condensation", "Precipitation" and "Collection", each attached to an appropriate directed arrow. Keep land and water layers visually distinct and the reading path clear. Avoid decorative equations, unsupported statistics and confusing arrow directions.
~~~

</details>

<a id="gallery-fashion-editorial"></a>

<h2 align="center">Fashion Editorial</h2>

[↑ Index](#gallery-index) · [完整分类 / Full atlas](skills/image25/references/gallery-fashion-editorial.md)

**Image 2.5: 3 · host-model-unknown: 0 · GPT Image 2: 7**

服装轮廓、面料、姿势和场景叙事。核对服装结构、手部和配饰连续性。

<table>
<tr>
<td width="50%" align="center" valign="top"><a href="https://github.com/LaplaceYoung/awesome-gpt-image-2.5/blob/9bb515b6b978a7521ae884821a847ab58c11c939/docs/cases/073-imported-ootd.md"><img src="https://raw.githubusercontent.com/LaplaceYoung/awesome-gpt-image-2.5/9bb515b6b978a7521ae884821a847ab58c11c939/assets/generated/073-imported-ootd.png" width="100%" alt="名画人物 OOTD"/></a><br/><strong>名画人物 OOTD</strong><br/><sub>Image 2.5 · 社区作者声明 · LaplaceYoung</sub></td>
<td width="50%" align="center" valign="top"><a href="https://github.com/LaplaceYoung/awesome-gpt-image-2.5/blob/9bb515b6b978a7521ae884821a847ab58c11c939/docs/cases/099-imported-.md"><img src="https://raw.githubusercontent.com/LaplaceYoung/awesome-gpt-image-2.5/9bb515b6b978a7521ae884821a847ab58c11c939/assets/generated/099-imported-.png" width="100%" alt="双色调摄影棚时尚肖像"/></a><br/><strong>双色调摄影棚时尚肖像</strong><br/><sub>Image 2.5 · 社区作者声明 · LaplaceYoung</sub></td>
</tr>
</table>

<details>
<summary>Prompt · 名画人物 OOTD</summary>

[LaplaceYoung · 原始出处](https://github.com/LaplaceYoung/awesome-gpt-image-2.5/blob/9bb515b6b978a7521ae884821a847ab58c11c939/docs/cases/073-imported-ootd.md) · **Image 2.5 · 社区作者声明**

[原作者提示词与生成条件](https://github.com/LaplaceYoung/awesome-gpt-image-2.5/blob/9bb515b6b978a7521ae884821a847ab58c11c939/docs/cases/073-imported-ootd.md)

未在本仓库转载完整 Prompt；原页未公开的参数不补造。

</details>

<details>
<summary>Prompt · 双色调摄影棚时尚肖像</summary>

[LaplaceYoung · 原始出处](https://github.com/LaplaceYoung/awesome-gpt-image-2.5/blob/9bb515b6b978a7521ae884821a847ab58c11c939/docs/cases/099-imported-.md) · **Image 2.5 · 社区作者声明**

[原作者提示词与生成条件](https://github.com/LaplaceYoung/awesome-gpt-image-2.5/blob/9bb515b6b978a7521ae884821a847ab58c11c939/docs/cases/099-imported-.md)

未在本仓库转载完整 Prompt；原页未公开的参数不补造。

</details>

<details><summary>本类起始 Prompt / Original practice brief</summary>

**prompt-only** · 本项目编写，尚未出图；不是上方示例图的原始 Prompt。

~~~text
Create a full-length fashion editorial photograph of an adult model wearing a sculptural charcoal wool coat and rust-orange scarf. Place the model in a quiet concrete courtyard under soft winter light. Use a restrained upright pose that reveals the coat's silhouette, with visible fabric weight and natural folds. Keep the hands anatomically clear and the footwear grounded. Avoid brand logos and excessive skin retouching.
~~~

</details>

<a id="gallery-fine-art-painting"></a>

<h2 align="center">Fine Art Painting</h2>

[↑ Index](#gallery-index) · [完整分类 / Full atlas](skills/image25/references/gallery-fine-art-painting.md)

**Image 2.5: 2 · host-model-unknown: 0 · GPT Image 2: 5**

构图、笔触、颜料层、色彩关系和底材。区分厚涂、薄涂与数码滤镜；避免只堆风格词。

<table>
<tr>
<td width="50%" align="center" valign="top"><a href="https://openai.com/index/introducing-chatgpt-images-2-5/"><img src="https://images.ctfassets.net/kftzwdyauwt9/521YOTFHRC1SBj5llj4HkY/15d00909f0f73cf0af06b7de524d1d33/impressionist-cityscape.webp?w=3840&amp;q=90&amp;fm=webp" width="100%" alt="印象派街景"/></a><br/><strong>印象派街景</strong><br/><sub>Image 2.5 · 官方示例 · OpenAI</sub></td>
<td width="50%" align="center" valign="top"><a href="https://github.com/LaplaceYoung/awesome-gpt-image-2.5/blob/9bb515b6b978a7521ae884821a847ab58c11c939/docs/cases/11-impressionist-cityscape.md"><img src="https://raw.githubusercontent.com/LaplaceYoung/awesome-gpt-image-2.5/9bb515b6b978a7521ae884821a847ab58c11c939/assets/generated/11-impressionist-cityscape-a.jpg" width="100%" alt="Impressionist Cityscape"/></a><br/><strong>Impressionist Cityscape</strong><br/><sub>Image 2.5 · 社区作者声明 · LaplaceYoung</sub></td>
</tr>
</table>

<details>
<summary>Prompt · 印象派街景</summary>

[OpenAI · 原始出处](https://openai.com/index/introducing-chatgpt-images-2-5/) · **Image 2.5 · 官方示例**

[原作者提示词与生成条件](https://openai.com/index/introducing-chatgpt-images-2-5/)

未在本仓库转载完整 Prompt；原页未公开的参数不补造。

</details>

<details>
<summary>Prompt · Impressionist Cityscape</summary>

[LaplaceYoung · 原始出处](https://github.com/LaplaceYoung/awesome-gpt-image-2.5/blob/9bb515b6b978a7521ae884821a847ab58c11c939/docs/cases/11-impressionist-cityscape.md) · **Image 2.5 · 社区作者声明**

[原作者提示词与生成条件](https://github.com/LaplaceYoung/awesome-gpt-image-2.5/blob/9bb515b6b978a7521ae884821a847ab58c11c939/docs/cases/11-impressionist-cityscape.md)

未在本仓库转载完整 Prompt；原页未公开的参数不补造。

</details>

<details><summary>本类起始 Prompt / Original practice brief</summary>

**prompt-only** · 本项目编写，尚未出图；不是上方示例图的原始 Prompt。

~~~text
Paint a riverside evening scene with visible broken-color brushwork and thin overlapping oil layers. Use a low horizon, a broad reflective river and a small warm-lit boat as the focal point. Let violet shadows and muted gold highlights interact without hard outlines. Vary edge sharpness and leave subtle canvas texture visible. Keep the result clearly a painting, not a photograph with a texture filter.
~~~

</details>

<a id="gallery-more-illustration-styles"></a>

<h2 align="center">More Illustration Styles</h2>

[↑ Index](#gallery-index) · [完整分类 / Full atlas](skills/image25/references/gallery-more-illustration-styles.md)

**Image 2.5: 10 · host-model-unknown: 0 · GPT Image 2: 6**

材质机制、形体、接触阴影和风格边界。同一对象材质规律统一；防止只换贴图。

<table>
<tr>
<td width="50%" align="center" valign="top"><a href="https://openai.com/index/introducing-chatgpt-images-2-5/"><img src="https://images.ctfassets.net/kftzwdyauwt9/3GALloAIN7Jn0P7wbvHPEB/0d02422440dfb3a001ff125cf37f7de4/mosaic.png?w=3840&amp;q=90&amp;fm=webp" width="100%" alt="马赛克风格"/></a><br/><strong>马赛克风格</strong><br/><sub>Image 2.5 · 官方示例 · OpenAI</sub></td>
<td width="50%" align="center" valign="top"><a href="https://github.com/LaplaceYoung/awesome-gpt-image-2.5/blob/9bb515b6b978a7521ae884821a847ab58c11c939/docs/cases/041-imported-.md"><img src="https://raw.githubusercontent.com/LaplaceYoung/awesome-gpt-image-2.5/9bb515b6b978a7521ae884821a847ab58c11c939/assets/generated/041-imported-.png" width="100%" alt="创意丝绸宇宙"/></a><br/><strong>创意丝绸宇宙</strong><br/><sub>Image 2.5 · 社区作者声明 · LaplaceYoung</sub></td>
</tr>
</table>

<details>
<summary>Prompt · 马赛克风格</summary>

[OpenAI · 原始出处](https://openai.com/index/introducing-chatgpt-images-2-5/) · **Image 2.5 · 官方示例**

[原作者提示词与生成条件](https://openai.com/index/introducing-chatgpt-images-2-5/)

未在本仓库转载完整 Prompt；原页未公开的参数不补造。

</details>

<details>
<summary>Prompt · 创意丝绸宇宙</summary>

[LaplaceYoung · 原始出处](https://github.com/LaplaceYoung/awesome-gpt-image-2.5/blob/9bb515b6b978a7521ae884821a847ab58c11c939/docs/cases/041-imported-.md) · **Image 2.5 · 社区作者声明**

[原作者提示词与生成条件](https://github.com/LaplaceYoung/awesome-gpt-image-2.5/blob/9bb515b6b978a7521ae884821a847ab58c11c939/docs/cases/041-imported-.md)

未在本仓库转载完整 Prompt；原页未公开的参数不补造。

</details>

<details><summary>本类起始 Prompt / Original practice brief</summary>

**prompt-only** · 本项目编写，尚未出图；不是上方示例图的原始 Prompt。

~~~text
Create a square illustration of a small fox reading under a mushroom, built entirely from layered colored paper. Show cut edges, slight fiber roughness and soft contact shadows between layers. Use five paper colors and a simple silhouette. Keep every visible object within the paper-craft medium; do not add glossy plastic eyes or realistic fur. Reserve a calm border around the scene.
~~~

</details>

<a id="gallery-cinematic-film-references"></a>

<h2 align="center">Cinematic Film References</h2>

[↑ Index](#gallery-index) · [完整分类 / Full atlas](skills/image25/references/gallery-cinematic-film-references.md)

**Image 2.5: 3 · host-model-unknown: 0 · GPT Image 2: 6**

景别、机位、镜头秩序、环境尺度和调色。电影感由空间与灯光建立；不把调色当作全部。

<table>
<tr>
<td width="50%" align="center" valign="top"><a href="https://openai.com/index/introducing-chatgpt-images-2-5/"><img src="https://images.ctfassets.net/kftzwdyauwt9/Oe7BObgTAVCWhUe8Xsxy6/ef835be62240562b3ae4be70d404d61d/sci-fi-surrealism.png?w=3840&amp;q=90&amp;fm=webp" width="100%" alt="科幻超现实"/></a><br/><strong>科幻超现实</strong><br/><sub>Image 2.5 · 官方示例 · OpenAI</sub></td>
<td width="50%" align="center" valign="top"><a href="https://github.com/LaplaceYoung/awesome-gpt-image-2.5/blob/9bb515b6b978a7521ae884821a847ab58c11c939/docs/cases/072-imported-35mm.md"><img src="https://raw.githubusercontent.com/LaplaceYoung/awesome-gpt-image-2.5/9bb515b6b978a7521ae884821a847ab58c11c939/assets/generated/072-imported-35mm.png" width="100%" alt="35mm 胶片风格飞岛"/></a><br/><strong>35mm 胶片风格飞岛</strong><br/><sub>Image 2.5 · 社区作者声明 · LaplaceYoung</sub></td>
</tr>
</table>

<details>
<summary>Prompt · 科幻超现实</summary>

[OpenAI · 原始出处](https://openai.com/index/introducing-chatgpt-images-2-5/) · **Image 2.5 · 官方示例**

[原作者提示词与生成条件](https://openai.com/index/introducing-chatgpt-images-2-5/)

未在本仓库转载完整 Prompt；原页未公开的参数不补造。

</details>

<details>
<summary>Prompt · 35mm 胶片风格飞岛</summary>

[LaplaceYoung · 原始出处](https://github.com/LaplaceYoung/awesome-gpt-image-2.5/blob/9bb515b6b978a7521ae884821a847ab58c11c939/docs/cases/072-imported-35mm.md) · **Image 2.5 · 社区作者声明**

[原作者提示词与生成条件](https://github.com/LaplaceYoung/awesome-gpt-image-2.5/blob/9bb515b6b978a7521ae884821a847ab58c11c939/docs/cases/072-imported-35mm.md)

未在本仓库转载完整 Prompt；原页未公开的参数不补造。

</details>

<details><summary>本类起始 Prompt / Original practice brief</summary>

**prompt-only** · 本项目编写，尚未出图；不是上方示例图的原始 Prompt。

~~~text
Create a contemplative widescreen film-frame concept of a lone traveler approaching a desert observatory at dawn. Place the traveler small in the lower third and the observatory as a simple monumental shape on the horizon. Use long soft shadows, dusty blue air and one muted warm window. Let empty space carry the mood. Keep detail sparse and avoid excessive lens flare or random futuristic ornaments.
~~~

</details>

<a id="gallery-beauty-and-lifestyle"></a>

<h2 align="center">Beauty And Lifestyle</h2>

[↑ Index](#gallery-index) · [完整分类 / Full atlas](skills/image25/references/gallery-beauty-and-lifestyle.md)

**Image 2.5: 0 · host-model-unknown: 1 · GPT Image 2: 2**

日常场景、产品材料、皮肤与柔光。避免虚构功效或配方；核对标签与瓶盖结构。

> 本类暂缺 Image 2.5 来源作品；以下样张的真实型号状态已逐图标注。

<table>
<tr>
<td width="50%" align="center" valign="top"><a href="https://github.com/Fangx-AI/awesome-image2.5/blob/main/docs/showcase.md"><img src="https://raw.githubusercontent.com/Fangx-AI/awesome-image2.5/main/assets/showcase/ceramic-skincare.png" width="100%" alt="护肤精华 · 材质与留白"/></a><br/><strong>护肤精华 · 材质与留白</strong><br/><sub>本项目生成 · 精确型号未知 · Fangx-AI</sub></td>
</tr>
</table>

<details>
<summary>Prompt · 护肤精华 · 材质与留白</summary>

[Fangx-AI · 原始出处](https://github.com/Fangx-AI/awesome-image2.5/blob/main/docs/showcase.md) · **本项目生成 · 精确型号未知**

Generated: 2026-09-09 · Postprocessing: none

~~~text
Create a premium skincare campaign photograph in landscape 3:2. One tall frosted sea-glass serum bottle with a pale sage ceramic cap, a smaller translucent glass dropper beside it, standing on a sculptural ivory travertine plinth. Bottle label contains exactly two lines: 'SEREIN' and 'DAILY SERUM'. Macro-realistic condensation, believable translucent liquid, soft caustic light on the stone. Art direction: warm ivory background, sage and pale gold, long late-afternoon side light, restrained luxury editorial photography. Product occupies right 60 percent, left 40 percent is calm unbroken negative space for future layout, with no added text there. Camera at bottle mid-height, controlled perspective, physically plausible reflections. No extra logos, hands, flowers, watermark, invented ingredients, medical claims or tiny illegible text.
~~~

实际观察：逐字检查瓶身文字；查看滴管、瓶盖、接触阴影与玻璃边缘。

</details>

<details><summary>本类起始 Prompt / Original practice brief</summary>

**prompt-only** · 本项目编写，尚未出图；不是上方示例图的原始 Prompt。

~~~text
Create a vertical lifestyle photograph of an unlabeled amber glass skincare bottle on a travertine bathroom shelf beside a folded linen towel. Use diffused morning light through frosted glass, subtle reflections and a realistic contact shadow. Include a single small branch as a secondary element. Keep bottle geometry plausible and the scene quiet, without invented medical claims, ingredient labels or impossible liquid effects.
~~~

</details>

<a id="gallery-events-and-experience"></a>

<h2 align="center">Events And Experience</h2>

[↑ Index](#gallery-index) · [完整分类 / Full atlas](skills/image25/references/gallery-events-and-experience.md)

**Image 2.5: 4 · host-model-unknown: 0 · GPT Image 2: 2**

入口、区域、动线、地标与图例。动线必须连通；虚构地图不可冒充实际导航。

<table>
<tr>
<td width="50%" align="center" valign="top"><a href="https://openai.com/index/introducing-chatgpt-images-2-5/"><img src="https://images.ctfassets.net/kftzwdyauwt9/4j4NxMqYjew5nrW2nqo7Yq/dd05b405739b3fb9f0f3cb56a196889b/wedding-invitation.webp?w=3840&amp;q=90&amp;fm=webp" width="100%" alt="婚礼邀请函"/></a><br/><strong>婚礼邀请函</strong><br/><sub>Image 2.5 · 官方示例 · OpenAI</sub></td>
<td width="50%" align="center" valign="top"><a href="https://github.com/LaplaceYoung/awesome-gpt-image-2.5/blob/9bb515b6b978a7521ae884821a847ab58c11c939/docs/cases/07-vintage-national-park-stamps.md"><img src="https://raw.githubusercontent.com/LaplaceYoung/awesome-gpt-image-2.5/9bb515b6b978a7521ae884821a847ab58c11c939/assets/generated/07-vintage-national-park-stamps.jpg" width="100%" alt="National Park Stamps"/></a><br/><strong>National Park Stamps</strong><br/><sub>Image 2.5 · 社区作者声明 · LaplaceYoung</sub></td>
</tr>
</table>

<details>
<summary>Prompt · 婚礼邀请函</summary>

[OpenAI · 原始出处](https://openai.com/index/introducing-chatgpt-images-2-5/) · **Image 2.5 · 官方示例**

[原作者提示词与生成条件](https://openai.com/index/introducing-chatgpt-images-2-5/)

未在本仓库转载完整 Prompt；原页未公开的参数不补造。

</details>

<details>
<summary>Prompt · National Park Stamps</summary>

[LaplaceYoung · 原始出处](https://github.com/LaplaceYoung/awesome-gpt-image-2.5/blob/9bb515b6b978a7521ae884821a847ab58c11c939/docs/cases/07-vintage-national-park-stamps.md) · **Image 2.5 · 社区作者声明**

[原作者提示词与生成条件](https://github.com/LaplaceYoung/awesome-gpt-image-2.5/blob/9bb515b6b978a7521ae884821a847ab58c11c939/docs/cases/07-vintage-national-park-stamps.md)

未在本仓库转载完整 Prompt；原页未公开的参数不补造。

</details>

<details><summary>本类起始 Prompt / Original practice brief</summary>

**prompt-only** · 本项目编写，尚未出图；不是上方示例图的原始 Prompt。

~~~text
Design a landscape visitor map for a fictional riverside book festival called "RIVER READS". Mark one entrance, three tent zones, a reading lawn, restrooms and an information desk. Connect them with a clear continuous walking route and include a concise legend. Use friendly flat illustration and large readable labels. Keep the map schematic and explicitly label it "FICTIONAL EVENT MAP".
~~~

</details>

<a id="gallery-tattoo-design"></a>

<h2 align="center">Tattoo Design</h2>

[↑ Index](#gallery-index) · [完整分类 / Full atlas](skills/image25/references/gallery-tattoo-design.md)

**Image 2.5: 0 · host-model-unknown: 0 · GPT Image 2: 4**

身体位置、线条粗细、负空间与可转印结构。检查细节是否适合实际尺寸；保留皮肤呼吸空间。

> 本类暂缺 Image 2.5 来源作品；以下样张的真实型号状态已逐图标注。

<table>
<tr>
<td width="50%" align="center" valign="top"><a href="https://github.com/wuyoscar/GPT-Image2-Skill/blob/135d873e1a843db5f122a15ddda02bd2845d4d25/skills/gpt-image/references/gallery-tattoo-design.md"><img src="https://raw.githubusercontent.com/wuyoscar/GPT-Image2-Skill/135d873e1a843db5f122a15ddda02bd2845d4d25/docs/tattoo-design/realistic-black-grey-sleeve-study.png" width="100%" alt="Realistic black-and-grey sleeve study"/></a><br/><strong>Realistic black-and-grey sleeve study</strong><br/><sub>GPT Image 2 · 旧版学习参考 · Wuyoscar / 原页署名作者</sub></td>
<td width="50%" align="center" valign="top"><a href="https://github.com/wuyoscar/GPT-Image2-Skill/blob/135d873e1a843db5f122a15ddda02bd2845d4d25/skills/gpt-image/references/gallery-tattoo-design.md"><img src="https://raw.githubusercontent.com/wuyoscar/GPT-Image2-Skill/135d873e1a843db5f122a15ddda02bd2845d4d25/docs/tattoo-design/color-neo-traditional-fox-flora.png" width="100%" alt="Color neo-traditional fox and flora"/></a><br/><strong>Color neo-traditional fox and flora</strong><br/><sub>GPT Image 2 · 旧版学习参考 · Wuyoscar / 原页署名作者</sub></td>
</tr>
</table>

<details>
<summary>Prompt · Realistic black-and-grey sleeve study</summary>

[Wuyoscar / 原页署名作者 · 原始出处](https://github.com/wuyoscar/GPT-Image2-Skill/blob/135d873e1a843db5f122a15ddda02bd2845d4d25/skills/gpt-image/references/gallery-tattoo-design.md) · **GPT Image 2 · 旧版学习参考**

Metadata: Tattoo Design · `portrait` · `1024x1536` · Curated

~~~text
Create a portrait tattoo design sheet for a realistic black-and-grey forearm sleeve. Subject: a highly detailed raven skull nested with realistic peonies, smoke ribbons, tiny moths, and cracked marble fragments. Present it as premium tattoo flash on warm off-white paper with a faint arm-placement silhouette behind the main artwork. Style: ultra-realistic tattoo shading, smooth dotwork gradients, crisp stencil-ready outlines, high contrast but not muddy, strong negative-space gaps for skin breathing room. Include small layout notes in clean text: "BLACK & GREY" / "FOREARM SLEEVE" / "NEGATIVE SPACE". No gore, no body horror, no brand logos, no actual person, no photorealistic skin photo; make it a professional tattoo design presentation.
~~~

</details>

<details>
<summary>Prompt · Color neo-traditional fox and flora</summary>

[Wuyoscar / 原页署名作者 · 原始出处](https://github.com/wuyoscar/GPT-Image2-Skill/blob/135d873e1a843db5f122a15ddda02bd2845d4d25/skills/gpt-image/references/gallery-tattoo-design.md) · **GPT Image 2 · 旧版学习参考**

Metadata: Tattoo Design · `portrait` · `1024x1536` · Curated

~~~text
Create a colorful neo-traditional tattoo flash poster. Central subject: a clever red fox head framed by chrysanthemum, peony, bluebells, small sparks, and decorative leaves. Use bold clean outlines, saturated but tasteful color fills, limited palette of vermilion, teal, golden ochre, deep navy, and cream highlights. Composition: symmetrical badge-like upper-arm tattoo design with separate small color swatches and a tiny stencil thumbnail on the side. Text must be small and readable: "NEO TRADITIONAL" / "FOX & FLORA". Make it vibrant, tattooable, and polished, with visible paper grain. Avoid cartoon mascot feel, avoid clutter, avoid gradients that would not tattoo well, no brand logos.
~~~

</details>

<details><summary>本类起始 Prompt / Original practice brief</summary>

**prompt-only** · 本项目编写，尚未出图；不是上方示例图的原始 Prompt。

~~~text
Create a vertical tattoo flash concept for a forearm placement, presented on off-white paper with no real body. Arrange a moth above two fern fronds in a balanced tapered silhouette. Use crisp black linework, limited stippling and generous negative-space gaps. Keep tiny details subordinate to the overall shape and include a small simplified stencil version beside it. Avoid dense muddy shading and lines too fine to remain distinct at the intended scale.
~~~

</details>

## Credits and contribution

[Wuyoscar / GPT-Image2-Skill](https://github.com/wuyoscar/GPT-Image2-Skill) 提供了分类展示、按需读取的 Skill 图谱和旧版案例参考。上游 MIT 版权声明及外部作者署名保留。

[OpenAI](https://openai.com/index/introducing-chatgpt-images-2-5/) · [LaplaceYoung](https://github.com/LaplaceYoung/awesome-gpt-image-2.5) · [来源与证据](docs/research.md)

[贡献指南](CONTRIBUTING.md) · [行为准则](CODE_OF_CONDUCT.md) · [支持说明](SUPPORT.md) · [安全政策](SECURITY.md) · [第三方许可](THIRD_PARTY_NOTICES.md)

[逐板块对照记录](docs/reference-study.md) · [项目结构](docs/architecture.md) · [自动更新机制](docs/automatic-updates.md)

Community project; not affiliated with OpenAI. Original content: CC0. Third-party content retains its original license.
