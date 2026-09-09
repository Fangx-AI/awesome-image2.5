### 局部编辑：只增加围巾

![局部编辑：只增加围巾](https://raw.githubusercontent.com/Fangx-AI/awesome-image2.5/main/assets/showcase/pet-scarf.png)

**适用：** 增加配饰、局部产品展示

**写法拆解：** 明确只改哪一项，并逐项列出脸部、姿态和背景不变量。

**换成你的内容：** 将围巾替换成另一件配饰，保持一次只改一件事。

**检查与局限：** 目视身份相近，不代表背景与毛发逐像素保持。

<details><summary>完整提示词与复现命令</summary>

~~~text
Edit this exact cat photograph. Add only a small mustard-yellow knitted scarf wrapped naturally around the cat's neck, with a short loose end resting on the chest. Preserve the cat's exact facial identity, asymmetrical gray face patch, eye color, ears, whiskers, body shape, front paw position and curved tail. Preserve the window, cushion, plant, background, camera angle, crop and lighting. The scarf should be physically plausible with a soft contact shadow and visible knit texture. Do not change or beautify anything else. No text, collar or other accessories.
~~~

以下是官方 API 复现用法，实际结果可能不同；本页展示由宿主内置工具生成。

~~~sh
image25 --prompt-file assets/showcase/pet-scarf.txt -i assets/showcase/pet-portrait.png --model sunburst -o generated/pet-scarf.png
~~~

[下载提示词](https://raw.githubusercontent.com/Fangx-AI/awesome-image2.5/main/assets/showcase/pet-scarf.txt) · [来源与生成记录](https://raw.githubusercontent.com/Fangx-AI/awesome-image2.5/main/assets/showcase/pet-scarf.json)

</details>
