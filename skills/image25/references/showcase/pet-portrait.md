# 一只猫的肖像 · 编辑基准图

[全部实图案例](../visual-gallery.md) · [31 类图谱](../gallery.md) · [安装与使用](https://github.com/Fangx-AI/awesome-image2.5/blob/main/docs/getting-started.md)

![一只猫的肖像 · 编辑基准图](https://raw.githubusercontent.com/Fangx-AI/awesome-image2.5/main/assets/showcase/pet-portrait.png)

**适用：** 宠物角色参考、身份保持实验

**写法拆解：** 用不对称面部花纹建立可观察的身份特征。

**换成你的内容：** 替换宠物类别及花纹；以实际出图作为下一步参考。

**检查与局限：** 耳部花纹与初始描述不完全一致。

<details><summary>完整提示词与复现命令</summary>

~~~text
Create a photorealistic editorial portrait of one fictional adult domestic cat, landscape 3:2. The cat has a distinctive asymmetrical face: mostly cream fur, a charcoal gray patch around its left eye (viewer right), both ears charcoal, pale green eyes, pink nose, cream chest and gray-striped tail curved on the cushion beside it. Sitting upright on a simple oatmeal linen cushion on a light oak window bench, front-facing head slightly angled toward the camera. Soft overcast daylight from the left, warm off-white wall behind, a gently out-of-focus green plant far in the background. Full cat ears, front paws and tail remain visible in frame. Natural fur detail, no over-sharpening, believable paws and whiskers, calm curious expression. No collar, clothing, accessories, text or watermark. This is an original fictional cat created as a reference for a subsequent controlled scarf edit; make its markings and scene clear and stable.
~~~

以下命令在已克隆的仓库根目录运行，需要单独安装 CLI 并配置 API Key。只安装 Skill 时，可直接复制上方提示词到宿主生图工具；参考图需另外提供。

以下是官方 API 复现用法，实际结果可能不同；本页展示由宿主内置工具生成。

~~~sh
image25 --prompt-file assets/showcase/pet-portrait.txt --model flare -o generated/pet-portrait.png --dry-run
image25 --prompt-file assets/showcase/pet-portrait.txt --model flare -o generated/pet-portrait.png
~~~

[下载提示词](https://raw.githubusercontent.com/Fangx-AI/awesome-image2.5/main/assets/showcase/pet-portrait.txt) · [来源与生成记录](https://raw.githubusercontent.com/Fangx-AI/awesome-image2.5/main/assets/showcase/pet-portrait.json)

</details>

[继续看其他案例](../visual-gallery.md)
