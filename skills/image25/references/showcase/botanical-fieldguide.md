# 植物图鉴 · 多面板信息

[全部实图案例](../visual-gallery.md) · [31 类图谱](../gallery.md) · [安装与使用](https://github.com/Fangx-AI/awesome-image2.5/blob/main/docs/getting-started.md)

![植物图鉴 · 多面板信息](https://raw.githubusercontent.com/Fangx-AI/awesome-image2.5/main/assets/showcase/botanical-fieldguide.png)

**适用：** 植物科普版式、博物馆图鉴视觉探索

**写法拆解：** 主图与局部细节分区，给每个面板限定一个内容与标签。

**换成你的内容：** 替换植物种类时同步修改局部细节描述与学名，避免仅替换标题。

**检查与局限：** 主图、三个细节框及标签齐全；植物结构尚未经专业核验，不能直接用作鉴定依据。

<details><summary>完整提示词与复现命令</summary>

~~~text
Create an exquisite botanical field-guide plate about the rosemary plant, landscape 3:2. Ivory archival paper, natural-history watercolor combined with precise fine ink linework, elegant readable editorial typography, orderly museum-book composition. Exact title 'ROSEMARY', subtitle 'Salvia rosmarinus'. Main left illustration: one large anatomically believable rosemary branch with narrow opposite needle-like green leaves, woody stem, and small pale blue flowers. Right column: three separately framed detail studies with exact labels 'LEAF', 'FLOWER', 'STEM'; a clearly enlarged leaf pair, a small blue flower closeup, and a woody stem detail respectively. Thin understated leader lines with no crossing, a balanced generous grid, small muted sage and blue color swatches along bottom without labels. No invented measurements, medicinal claims, additional paragraphs, garbled microtext or decorative stamps. The illustration should be detailed enough to inspire an educational design while keeping each panel immediately legible.
~~~

以下命令在已克隆的仓库根目录运行，需要单独安装 CLI 并配置 API Key。只安装 Skill 时，可直接复制上方提示词到宿主生图工具；参考图需另外提供。

以下是官方 API 复现用法，实际结果可能不同；本页展示由宿主内置工具生成。

~~~sh
image25 --prompt-file assets/showcase/botanical-fieldguide.txt --model flare -o generated/botanical-fieldguide.png --dry-run
image25 --prompt-file assets/showcase/botanical-fieldguide.txt --model flare -o generated/botanical-fieldguide.png
~~~

[下载提示词](https://raw.githubusercontent.com/Fangx-AI/awesome-image2.5/main/assets/showcase/botanical-fieldguide.txt) · [来源与生成记录](https://raw.githubusercontent.com/Fangx-AI/awesome-image2.5/main/assets/showcase/botanical-fieldguide.json)

</details>

[继续看其他案例](../visual-gallery.md)
