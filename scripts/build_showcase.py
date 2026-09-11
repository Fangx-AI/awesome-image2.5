"""Build a visual-first README and self-contained searchable showcase."""
import json,html
from pathlib import Path
R=Path(__file__).resolve().parents[1]
groups=[('commercial','商业设计','ceramic-skincare coffee-packaging citrus-menu outdoor-watch tea-campaign tea-lightbox'),
('editing','宠物身份与局部编辑','pet-portrait pet-scarf'),
('education','图鉴与信息设计','botanical-fieldguide'),
('architecture','建筑与微缩空间','rooftop-library isometric-teahouse'),
('character','角色三视图','courier-character'),
('interface','界面设计','field-notes-ui'),
('story','叙事与风格偏差','rainy-bookshop')]
notes=json.loads((R/'catalog/showcase-notes.json').read_text(encoding='utf-8'))
entries=[]
for group,title,ids in groups:
 for id in ids.split():
  p=R/'assets/showcase'/f'{id}.json'
  if not p.exists(): continue
  e=json.loads(p.read_text(encoding='utf-8'))
  e.update(id=id,category=title,group=group,**notes[id])
  entries.append(e)
def detail(e,prefix):
 s=['### '+e['title'],'',f"![{e['title']}]({prefix}assets/showcase/{e['id']}.png)",'',
 '**适用：** '+e['use'],'','**写法拆解：** '+e['learn'],'','**换成你的内容：** '+e['change'],'',
 '**检查与局限：** '+e['check'],'',
 '<details><summary>完整提示词与复现命令</summary>','','~~~text',e['prompt'],'~~~','']
 inputs=e.get('input_images',[])
 if not inputs and e.get('input'):inputs=[e['input']+'.png']
 if inputs:
  s += ['**输入参考（按命令顺序）：**','']
  for i,inp in enumerate(inputs,1):
   s += [f"![参考图 {i}]({prefix}assets/showcase/{Path(inp).name})",'']
 command='image25 --prompt-file assets/showcase/'+e['id']+'.txt'
 for inp in inputs:command+=' -i assets/showcase/'+Path(inp).name
 command+=' --model '+('sunburst' if inputs else 'flare')+' -o generated/'+e['id']+'.png'
 s += ['以下命令在已克隆的仓库根目录运行，需要单独安装 CLI 并配置 API Key。只安装 Skill 时，可直接复制上方提示词到宿主生图工具；参考图需另外提供。', '',
 '以下是官方 API 复现用法，实际结果可能不同；本页展示由宿主内置工具生成。','','~~~sh',command+' --dry-run',command,'~~~','',
 f"[下载提示词]({prefix}assets/showcase/{e['id']}.txt) · [来源与生成记录]({prefix}assets/showcase/{e['id']}.json)",'','</details>','']
 return s
header=['<h1 align="center">Awesome Image 2.5</h1>','',
 '<p align="center">看图选方向 · 展开提示词 · 换成你的内容 · 生成与修改</p>','',
 '[English](README.en.md) · [可搜索实图画廊](docs/gallery.html) · [安装与使用](#安装与使用) · [社区来源](docs/community.md)','',
 '## 画廊导航','',
 '| 分类 | 内容 |','| --- | --- |']
for gid,title,ids in groups:
 header += [f'| [{title}](#{gid}) | '+' · '.join(e['title'].split(' · ')[0] for e in entries if e['group']==gid)+' |']
header += ['','本页仅展示实际生成的图片。每个案例包含完整提示词、适用任务、可替换内容及检查要点。宿主未返回精确模型 ID，生成记录统一标注 host-model-unknown；不把这些图片当作指定 Flare / Sunburst 的测试证据。','']
body=[]
for gid,title,ids in groups:
 group=[e for e in entries if e['group']==gid]
 body += [f'<a id="{gid}"></a>','',f'## {title}','']
 if gid=='editing':
  body+=['| 参考图 | 只增加围巾 |','| --- | --- |','| ![参考](assets/showcase/pet-portrait.png) | ![编辑](assets/showcase/pet-scarf.png) |','']
 if gid=='commercial':
  for i in range(0,len(group),2):
   pair=group[i:i+2]
   body+=['| '+' | '.join(e['title'] for e in pair)+' |','| '+' | '.join('---' for e in pair)+' |',
   '| '+' | '.join(f"![{e['title']}](assets/showcase/{e['id']}.png)" for e in pair)+' |','']
 for e in group:body+=detail(e,'')
 tail=['## 安装与使用','','~~~sh','uv tool install git+https://github.com/Fangx-AI/awesome-image2.5','~~~','',
 '在 Codex 中通过 $skill-installer 安装 [image25](skills/image25) 或 [image25-reverse-prompt](skills/image25-reverse-prompt)。',
 '安装后直接描述目标，例如“用 image25 参考系列咖啡包装，改成三款茶叶包装，保持统一版式”。','',
 '[快速开始](docs/getting-started.md) · [工作流](docs/workflows.md) · [质量标准](docs/quality.md) · [故障排查](docs/troubleshooting.md)','',
 '## 提示词实验区','','[基础场景与变体目录](skills/image25/references/gallery.md)用于探索未出图的构思，不列入精选画廊。条目数量不代表作品数量。','',
 '## 来源与贡献','','组织方式学习自 [wuyoscar/GPT-Image2-Skill](https://github.com/wuyoscar/GPT-Image2-Skill)。本页图像与提示词为独立创作。',
 '欢迎提交包含效果图、完整提示词、参考图、模型依据和出处的案例。详见 [贡献指南](CONTRIBUTING.md)。原创内容采用 [CC0](LICENSE)，第三方内容遵循原许可。社区项目，与 OpenAI 无官方关联。','']
(R/'README.md').write_text('\n'.join(header+body+tail),encoding='utf-8')
cards=[]
for e in entries:
 esc=html.escape
 cards.append('<article data-search="'+esc(e['category']+' '+e['title']+' '+e['use'])+'"><img loading="lazy" src="../assets/showcase/'+e['id']+'.png" alt="'+esc(e['title'])+'"><div class="text"><small>'+esc(e['category'])+'</small><h2>'+esc(e['title'])+'</h2><p>'+esc(e['use'])+'</p><details><summary>提示词、用法与检查</summary><p><b>写法：</b>'+esc(e['learn'])+'</p><p><b>替换：</b>'+esc(e['change'])+'</p><p><b>检查：</b>'+esc(e['check'])+'</p><pre>'+esc(e['prompt'])+'</pre><button onclick="copyPrompt(this)">复制提示词</button> <a download href="../assets/showcase/'+e['id']+'.txt">下载 TXT</a></details></div></article>')
page='''<!doctype html><html lang="zh-CN"><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Awesome Image 2.5 · 实图画廊</title><style>
*{box-sizing:border-box}body{margin:0;background:#f4f2ec;color:#252b25;font:16px/1.7 system-ui,sans-serif}header,main{max-width:1280px;margin:auto;padding:36px 24px}header{padding-top:64px}h1{font-size:clamp(32px,5vw,64px);letter-spacing:-2px;line-height:1.1}a{color:#35644a}input{width:100%;padding:16px;border:1px solid #aab5a7;border-radius:8px;font:inherit;background:white}.grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:24px}article{background:white;border:1px solid #dedfd6;border-radius:12px;overflow:hidden}article img{width:100%;height:360px;object-fit:contain;background:#ebece5;display:block}.text{padding:24px}small{color:#617259}h2{font-size:22px;margin:8px 0}summary,button{cursor:pointer}pre{white-space:pre-wrap;font:14px/1.7 monospace;overflow-wrap:anywhere;background:#f4f2ec;padding:16px}button{padding:10px 18px;background:#244932;color:white;border:0;border-radius:6px}[hidden]{display:none!important}@media(max-width:700px){.grid{grid-template-columns:1fr}article img{height:auto}header{padding-top:32px}}</style>
<header><a href="../README.md">Awesome Image 2.5</a><h1>先找到你想做的图。</h1><p>真实输出、完整提示词，以及如何换成自己的内容。</p><p>这些输出来自宿主内置生图工具，精确模型 ID 未提供。每个案例均记录检查要点。</p><input id="search" aria-label="搜索案例" placeholder="搜索：包装、菜单、宠物、界面…"><p id="count" aria-live="polite"></p><p id="notice" role="status"></p></header><main class="grid">'''
page+=''.join(cards)+'''</main><script>
const cards=[...document.querySelectorAll('article')],search=document.getElementById('search'),count=document.getElementById('count');function filter(){let n=0;for(const c of cards){c.hidden=!c.dataset.search.toLowerCase().includes(search.value.trim().toLowerCase());if(!c.hidden)n++}count.textContent=n+' 个实图案例'}search.addEventListener('input',filter);filter();async function copyPrompt(b){const s=b.parentElement.querySelector('pre').textContent;try{await navigator.clipboard.writeText(s);document.getElementById('notice').textContent='已复制提示词'}catch{document.getElementById('notice').textContent='请展开提示词手动复制，或下载 TXT。'}}
</script></html>'''
(R/'docs/gallery.html').write_text(page,encoding='utf-8')
(R/'catalog/showcase.json').write_text(json.dumps(entries,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
ref=['# 实图案例路由','','按用户目标选择一个案例，读取对应完整提示词，保留布局规则并替换具体内容。不要一次读取全部案例。','',
'本索引的图片由宿主生成，精确模型未知。提示词实验区不等同于实图案例。','']
for e in entries:
 ref += [f"## {e['title']}",'',e['use'],'',f"[完整案例](showcase/{e['id']}.md)",'']
 out=R/'skills/image25/references/showcase'/f"{e['id']}.md";out.parent.mkdir(exist_ok=True)
 content=detail(e,'https://raw.githubusercontent.com/Fangx-AI/awesome-image2.5/main/')
 content[0]='# '+e['title']
 content[2:2]=['[全部实图案例](../visual-gallery.md) · [31 类图谱](../gallery.md) · [安装与使用](https://github.com/Fangx-AI/awesome-image2.5/blob/main/docs/getting-started.md)','']
 content+=['[继续看其他案例](../visual-gallery.md)','']
 out.write_text('\n'.join(content),encoding='utf-8')
(R/'skills/image25/references/visual-gallery.md').write_text('\n'.join(ref),encoding='utf-8')
print('Built visual gallery:',len(entries),'cases')
showcase=['# 实图案例与编辑工作流','','[返回首页](../README.md) · [搜索画廊](gallery.html)','','所有输出均标注 host-model-unknown；实际观察与提示词意图分别记录。','']
for e in entries:showcase+=detail(e,'../')
(R/'docs/showcase.md').write_text('\n'.join(showcase),encoding='utf-8')
