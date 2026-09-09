### 快递员角色 · 三视图一致性

![快递员角色 · 三视图一致性](https://raw.githubusercontent.com/Fangx-AI/awesome-image2.5/main/assets/showcase/courier-character.png)

**适用：** 动画角色开发、三视图方向探索

**写法拆解：** 按服装部位逐项锁定跨视图不变量，并指定相同基线与尺度。

**换成你的内容：** 替换角色职业与服装颜色，保持三视图布局和服装结构清单。

**检查与局限：** 三视图的主色、背包、裤脚与鞋底基本呼应；正面肘部补丁的位置偏外，侧面背包厚度仍需人工定稿。

<details><summary>完整提示词与复现命令</summary>

~~~text
A polished animation character model sheet, landscape 3:2, on a clean warm off-white background. Exactly three equal-scale full-body views of the same adult female bicycle courier: front view, strict side profile facing right, and back view, aligned along a single baseline and generously separated. She has a short curly dark-brown bob, a mustard yellow cropped rain jacket with dark navy elbow patches, navy cuffed trousers, white high-top sneakers with orange soles, and a small square teal delivery backpack with one centered orange reflective strip. All three views must preserve the identical jacket construction, sleeve length, trouser cuffs, shoe design, backpack proportions and colors. Relaxed neutral standing pose, hands visible at sides, no bicycle or props. Stylish hand-painted 2D animation development art, expressive but restrained proportions, clear readable silhouettes, subtle soft shading, no photorealism, no labels, no arrows, no extra views, no cropped feet.
~~~

以下是官方 API 复现用法，实际结果可能不同；本页展示由宿主内置工具生成。

~~~sh
image25 --prompt-file assets/showcase/courier-character.txt --model flare -o generated/courier-character.png
~~~

[下载提示词](https://raw.githubusercontent.com/Fangx-AI/awesome-image2.5/main/assets/showcase/courier-character.txt) · [来源与生成记录](https://raw.githubusercontent.com/Fangx-AI/awesome-image2.5/main/assets/showcase/courier-character.json)

</details>
