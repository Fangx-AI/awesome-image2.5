# 平面海报 → 灯箱样机

[全部实图案例](../visual-gallery.md) · [31 类图谱](../gallery.md) · [安装与使用](https://github.com/Fangx-AI/awesome-image2.5/blob/main/docs/getting-started.md)

![平面海报 → 灯箱样机](https://raw.githubusercontent.com/Fangx-AI/awesome-image2.5/main/assets/showcase/tea-lightbox.png)

**适用：** 提案中的投放场景样机

**写法拆解：** 先完成平面稿，再用参考图指定载体、视角与反射强度。

**换成你的内容：** 替换投放环境，保留参考图与完整画面要求。

**检查与局限：** 文字与图案可能重绘；不能作为像素保真贴图。

<details><summary>完整提示词与复现命令</summary>

~~~text
Use this exact Chinese tea campaign poster as the artwork inside a realistic vertical illuminated advertising lightbox in a refined contemporary transit-station interior. Preserve the complete original poster artwork including the exact headline 慢下来，喝口茶, the subheading 山间冷泡茶, the bottle label 山间, bottle, glass, tea leaves, relative layout and colors. Do not redesign, crop or rewrite the poster. Show the entire lightbox with a thin brushed-metal frame, photographed almost straight-on with slight environmental perspective. Neutral pale stone wall, clean tiled floor, warm soft overhead lighting and subtle glass reflections that do not obscure text. The poster is the dominant focus and fully readable. No people, transit logos, station names or other text. Landscape 3:2 composition with modest surrounding context.
~~~

**输入参考（按命令顺序）：**

![参考图 1](https://raw.githubusercontent.com/Fangx-AI/awesome-image2.5/main/assets/showcase/tea-campaign.png)

以下命令在已克隆的仓库根目录运行，需要单独安装 CLI 并配置 API Key。只安装 Skill 时，可直接复制上方提示词到宿主生图工具；参考图需另外提供。

以下是官方 API 复现用法，实际结果可能不同；本页展示由宿主内置工具生成。

~~~sh
image25 --prompt-file assets/showcase/tea-lightbox.txt -i assets/showcase/tea-campaign.png --model sunburst -o generated/tea-lightbox.png --dry-run
image25 --prompt-file assets/showcase/tea-lightbox.txt -i assets/showcase/tea-campaign.png --model sunburst -o generated/tea-lightbox.png
~~~

[下载提示词](https://raw.githubusercontent.com/Fangx-AI/awesome-image2.5/main/assets/showcase/tea-lightbox.txt) · [来源与生成记录](https://raw.githubusercontent.com/Fangx-AI/awesome-image2.5/main/assets/showcase/tea-lightbox.json)

</details>

[继续看其他案例](../visual-gallery.md)
