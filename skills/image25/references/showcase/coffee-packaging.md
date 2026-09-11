# 咖啡包装 · 系列一致性

[全部实图案例](../visual-gallery.md) · [31 类图谱](../gallery.md) · [安装与使用](https://github.com/Fangx-AI/awesome-image2.5/blob/main/docs/getting-started.md)

![咖啡包装 · 系列一致性](https://raw.githubusercontent.com/Fangx-AI/awesome-image2.5/main/assets/showcase/coffee-packaging.png)

**适用：** 咖啡品牌提案、系列包装方向探索

**写法拆解：** 先锁定袋型、文字位置与尺度，再允许配色和插画变化。

**换成你的内容：** 同时替换三款名称及风味色，保留同一版式系统。

**检查与局限：** 三袋版式和配色系统清楚，但模型额外加入了 SPECIALTY COFFEE ROASTERS 小字，未完全遵循只使用指定文字的要求。不是印刷刀模。

<details><summary>完整提示词与复现命令</summary>

~~~text
Create a sophisticated brand packaging presentation for a fictional coffee roaster named 'ALTITUDE'. Landscape 3:2, three upright matte paper coffee bags aligned on one warm ivory studio surface, equal shape and scale, realistic folded tops and bottom gussets. Each bag carries the same crisp ALTITUDE wordmark at the same position and a different bold minimal abstract mountain illustration. Left bag deep midnight blue with copper illustration and the readable label '01 DAWN'; middle warm burnt orange with cream illustration and '02 SUMMIT'; right muted forest green with pale sage illustration and '03 DUSK'. Consistent graphic system, disciplined hierarchy, tactile uncoated paper, delicate natural shadows, premium contemporary graphic design, photographed almost straight-on. Nothing overlaps text. No cups, beans, decorative objects, extra labels, claims or watermark. Make this a convincing coordinated packaging design, not three unrelated styles.
~~~

以下命令在已克隆的仓库根目录运行，需要单独安装 CLI 并配置 API Key。只安装 Skill 时，可直接复制上方提示词到宿主生图工具；参考图需另外提供。

以下是官方 API 复现用法，实际结果可能不同；本页展示由宿主内置工具生成。

~~~sh
image25 --prompt-file assets/showcase/coffee-packaging.txt --model flare -o generated/coffee-packaging.png --dry-run
image25 --prompt-file assets/showcase/coffee-packaging.txt --model flare -o generated/coffee-packaging.png
~~~

[下载提示词](https://raw.githubusercontent.com/Fangx-AI/awesome-image2.5/main/assets/showcase/coffee-packaging.txt) · [来源与生成记录](https://raw.githubusercontent.com/Fangx-AI/awesome-image2.5/main/assets/showcase/coffee-packaging.json)

</details>

[继续看其他案例](../visual-gallery.md)
