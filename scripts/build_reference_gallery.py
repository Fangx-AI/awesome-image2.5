"""Publish the attributed reference atlas alongside original case studies."""
import html,json,re
from pathlib import Path
R=Path(__file__).resolve().parents[1]
data=json.loads((R/"catalog/reference-atlas.json").read_text(encoding="utf-8"))
entries=data["entries"]
titles=['动漫与漫画','游戏','复古与赛博朋克','电影与动画','角色设计','排版与海报','插画','水彩','水墨与中国风','像素艺术','等距场景','产品与食品','品牌系统','摄影','信息图与图鉴','科研图示','官方 Cookbook','参考图编辑','UI 与 UX','数据可视化','技术插图','建筑与室内','科学与教育','时尚编辑','纯艺术绘画','插画风格','电影风格','美妆与生活','活动与导览','纹身设计','屏幕摄影']
# Match names instead of relying on filesystem ordering.
slugs=['anime-and-manga','gaming','retro-and-cyberpunk','cinematic-and-animation','character-design','typography-and-posters','illustration','watercolor','ink-and-chinese','pixel-art','isometric','product-and-food','brand-systems-and-identity','photography','infographics-and-field-guides','research-paper-figures','official-openai-cookbook-examples','edit-endpoint-showcase','ui-ux-mockups','data-visualization','technical-illustration','architecture-and-interior','scientific-and-educational','fashion-editorial','fine-art-painting','more-illustration-styles','cinematic-film-references','beauty-and-lifestyle','events-and-experience','tattoo-design','screen-photography']
names=dict(zip(['gallery-'+s+'.md' for s in slugs],titles))
def esc(s):return html.escape(s,quote=True)
def case(e,prefix=""):
 result=[f"### {e['number']:03d} · {e['title']}",'',f"原始模型：GPT Image 2 · 上游参考 · [作者与来源]({prefix}docs/reference-atlas/{e['category_file']})",'',
 '<details><summary>完整提示词 · 下载 · 改用 Image 2.5</summary>','']
 for i,p in enumerate(e['prompts'],1):
  result+=['~~~text',p['text'],'~~~','',f"[下载提示词]({prefix}docs/reference-atlas/prompts/{e['id']}-{i}.txt)",'']
 result+=['保持原提示词作为起点，按自己的对象、文字与布局修改。此处原图不是 Image 2.5 的复现结果。','',
 '~~~sh',f"image25 --prompt-file docs/reference-atlas/prompts/{e['id']}-1.txt --model flare --dry-run",'~~~','',
 '若案例需要输入图片，请先提供自己的参考图，并加入 -i；确认请求后再生成。原文中的特殊参数、数据或图片占位符应先替换。','',
 f"[上游原页]({e['upstream']}) · [MIT 许可]({prefix}vendor/gpt-image2/LICENSE)",'','</details>','']
 return result
original=(R/'README.md').read_text(encoding='utf-8')
# build_showcase.py creates the original-only README first.
original=original.replace('](assets/','](../assets/').replace('](docs/','](').replace('](skills/','](../skills/').replace('](README.en.md)','](../README.en.md)').replace('](CONTRIBUTING.md)','](../CONTRIBUTING.md)').replace('](LICENSE)','](../LICENSE)')
(R/'docs/original-gallery.md').write_text(original,encoding='utf-8')
intro=['<h1 align="center">Awesome Image 2.5</h1>','',
 '<p align="center">图像提示词画廊 · 参考图编辑 · Agent Skills · CLI</p>','',
 '[新增实图](docs/original-gallery.md) · [搜索全部案例](docs/gallery.html) · [快速开始](docs/getting-started.md) · [贡献](CONTRIBUTING.md)','',
 '**基于 [Wuyoscar / GPT-Image2-Skill](https://github.com/wuyoscar/GPT-Image2-Skill) 的完整参考图谱改造。** 保留上游 31 类、162 个案例的提示词、图像引用及作者来源，并加入本项目 14 个实图案例和 Image 2.5 使用工具。',
 '',
 '| 内容 | 来源与状态 |','| --- | --- |',
 '| 162 个参考案例 | 上游 GPT Image 2 图谱；保留原始模型，不冒充 Image 2.5 实测 |',
 '| 14 个新增实图案例 | 本项目通过宿主生成；精确模型 ID 未返回 |',
 '| Image 2.5 CLI | 可指定 Flare / Sunburst；生成时保存请求记录 |','',
 '## 怎么用','',
 '1. 看下面的分类预览，找到接近自己目标的作品。',
 '2. 展开对应提示词，替换对象、文字和参考图。',
 '3. 复制到生图工具，或用 CLI 预检并运行；对照文字、结构、身份和布局检查结果。','',
 '[安装与参数说明](docs/getting-started.md) · [图像编辑工作流](docs/workflows.md) · [案例来源与许可](THIRD_PARTY_NOTICES.md)','',
 '## 本项目新增作品','',
 '| 系列包装 | 角色三视图 |','| --- | --- |',
 '| ![系列包装](assets/showcase/coffee-packaging.png) | ![三视图](assets/showcase/courier-character.png) |',
 '| [提示词与实际偏差](docs/original-gallery.md) | [提示词与实际偏差](docs/original-gallery.md) |','',
 '[浏览新增的商业设计、图鉴、建筑、宠物编辑等 14 个案例 →](docs/original-gallery.md)','',
 '<a id="atlas"></a>','## 完整参考图谱','',
 '以下图片与案例来自上游 GPT Image 2 图谱，原作者和原始来源见对应分类页。图片通过固定提交的上游地址引用，需要联网加载。','',
 '| 分类 | 案例 | 分类 | 案例 |','| --- | ---: | --- | ---: |']
cats=sorted(data['categories'],key=lambda c:slugs.index(c['file'][8:-3]))
for i in range(0,len(cats),2):
 pair=cats[i:i+2];cells=[]
 for c in pair:
  slug=c['file'][8:-3];cells += [f"[{names[c['file']]}](#{slug})",str(len(c['entries']))]
 if len(pair)==1:cells+=['','']
 intro+=['| '+' | '.join(cells)+' |']
body=[]
for c in cats:
 slug=c['file'][8:-3];group=[e for e in entries if e['category_file']==c['file']]
 body += ['',f'<a id="{slug}"></a>','',f"## {names[c['file']]} · {len(group)} 个案例",'',
 f"[完整分类与作者信息](docs/reference-atlas/{c['file']}) · [返回索引](#atlas)",'']
 for i in range(0,len(group),2):
  pair=group[i:i+2]
  body+=['| '+' | '.join(e['title'] for e in pair)+' |','| '+' | '.join('---' for e in pair)+' |',
  '| '+' | '.join(f"![{e['title']}]({e['images'][0]})" for e in pair)+' |','']
  for e in pair:body+=case(e)
footer=['## 工具与维护','',
 '~~~sh','uv tool install git+https://github.com/Fangx-AI/awesome-image2.5',
 'image25 --prompt-file your-prompt.txt --model flare --dry-run','~~~','',
 '[生图 Skill](skills/image25/SKILL.md) · [反推提示词 Skill](skills/image25-reverse-prompt/SKILL.md) · [实验区](docs/prompt-lab.html)','',
 '上游图谱及相关改编文档遵循 MIT 许可，保留 Wuyoscar 版权声明。第三方图像及提示词保留其原作者权利。原创部分采用 CC0。详见 [第三方声明](THIRD_PARTY_NOTICES.md)。社区项目，与 OpenAI 无官方关联。','']
(R/'README.md').write_text('\n'.join(intro+body+footer),encoding='utf-8')
# Extend the real-output HTML gallery with reference cards.
page=(R/'docs/gallery.html').read_text(encoding='utf-8')
page=page.replace('<article data-search=','<article data-kind="original" data-search=')
cards=[]
for e in entries:
 category=names[e['category_file']]
 p=e['prompts'][0]['text']
 cards+=['<article data-kind="reference" data-search="'+esc(category+' '+e['category']+' '+e['title']+' '+p)+'"><img loading="lazy" src="'+esc(e['images'][0])+'" alt="'+esc(e['title'])+'"><div class="text"><small>'+esc(category)+' · GPT Image 2 上游参考</small><h2>'+esc(e['title'])+'</h2><p>'+esc(e['metadata'])+'</p><details><summary>提示词、用法与检查</summary><p>原图不是 Image 2.5 实测。使用前替换占位符；编辑案例需要自己的参考图。</p><pre>'+esc(p)+'</pre><button onclick="copyPrompt(this)">复制提示词</button> <a download href="reference-atlas/prompts/'+e['id']+'-1.txt">下载 TXT</a><p><a href="reference-atlas/'+e['category_file']+'">完整来源与作者</a> · <a href="'+esc(e['upstream'])+'">上游原页</a></p></details></div></article>']
page=page.replace('</main>',''.join(cards)+'</main>')
page=page.replace('这些输出来自宿主内置生图工具，精确模型 ID 未提供。每个案例均记录检查要点。','162 个上游 GPT Image 2 参考案例 + 14 个本项目新增实图。来源与模型状态分别标注；上游图片需要联网加载。')
page=page.replace('<input id="search"','<label>来源 <select id="source"><option value="">全部案例</option><option value="original">本项目新增</option><option value="reference">上游参考图谱</option></select></label> <input id="search"')
page=page.replace("c.hidden=!c.dataset.search.toLowerCase().includes(search.value.trim().toLowerCase());","c.hidden=(!c.dataset.search.toLowerCase().includes(search.value.trim().toLowerCase()))||(document.getElementById('source').value!==''&&c.dataset.kind!==document.getElementById('source').value);")
page=page.replace("search.addEventListener('input',filter);","search.addEventListener('input',filter);document.getElementById('source').addEventListener('change',filter);")
(R/'docs/gallery.html').write_text(page,encoding='utf-8')
ref=['# 完整参考图谱路由','','上游 GPT Image 2 案例，不是 Image 2.5 实测。来源与 MIT 许可见仓库第三方声明。选择一个最相关分类，只读取该分类的实际提示词。','']
for c in cats:
 ref+=[f"- [{names[c['file']]}：{len(c['entries'])} 例](atlas/{c['file']})"]
 out=R/'skills/image25/references/atlas'/c['file'];out.parent.mkdir(exist_ok=True)
 source=(R/'docs/reference-atlas'/c['file']).read_text(encoding='utf-8').replace('../../vendor/gpt-image2/LICENSE','https://github.com/Fangx-AI/awesome-image2.5/blob/main/vendor/gpt-image2/LICENSE')
 out.write_text(source,encoding='utf-8')
(R/'skills/image25/references/reference-atlas.md').write_text('\n'.join(ref)+'\n',encoding='utf-8')
print('Built complete reference gallery:',len(entries),'upstream cases + original showcase')

