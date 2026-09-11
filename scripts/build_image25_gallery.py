"""Build the Image 2.5 community index with explicit evidence tiers."""
import collections,html,json,re
from pathlib import Path
from urllib.parse import urlsplit,urlunsplit
R=Path(__file__).resolve().parents[1]
raw=json.loads((R/'catalog/web-image25.json').read_text(encoding='utf-8'))['records']+json.loads((R/'catalog/community-image25.json').read_text(encoding='utf-8'))['records']
def category(e):
 if e.get('category') not in ['Imported showcase','Uncategorized']:return {'Layout and type':'海报与文字','Documents':'出版与版式','Style lock':'插画与艺术','Character':'角色与游戏','UI and interfaces':'界面与屏幕','Cinematic showcase':'建筑与场景','Storyboards and advertising':'产品与商业'}.get(e['category'],e['category'])
 t=e['title'].lower()
 rules=[('海报与文字','海报 封面 wordmark 字母 排版'),('界面与屏幕','截图 屏幕 ui'),('摄影与人像','肖像 人像 自拍 曝光 摄影 剪影'),
 ('角色与游戏','角色 动漫 游戏 公仔 手办 娃娃 q版 表情包'),('品牌与图标','logo 图标 emoji 名片 印章 徽章 别针'),
 ('信息与教育','信息图 解剖 论文 食谱 预报 地图 藏宝图 涂色'),('建筑与场景','建筑 城市 都市 房间 景观 场景 飞岛'),
 ('产品与商业','广告 包装 键帽 花盆 腕托 冰棒 雪糕 胶囊'),('插画与艺术','插画 艺术 水彩 纸雕 云彩 玻璃 材质 地毯 丝绸')]
 for c,words in rules:
  if any(w in t for w in words.split()):return c
 return '插画与艺术'
seen=set();entries=[];duplicates=[]
for e in raw:
 key=tuple(sorted(urlunsplit((*urlsplit(i['url'])[:3],'','')) for i in e['images']))
 if key in seen:duplicates.append(e['id']);continue
 seen.add(key);e=dict(e);e['category']=category(e);e['title']=re.sub(r'^Case \d+ — ','',e['title']);entries.append(e)
labels={'official-sample':'官方示例','provider-reported':'平台声明','author-reported-with-command':'作者实测附命令','author-claim-via-public-mirror':'X 作者声明·镜像读取','author-reported-not-independently-tested':'社区作者声明'}
groups=collections.defaultdict(list)
for e in entries:groups[e['category']].append(e)
def summary(e,prefix=''):
 tag=labels[e['verification']]
 return [f"### {e['title']}",'',f"![{e['title']}]({e['images'][0]['url']})",'',
 f"**{e['author']} · {tag} · {e['model_claim']}**",'',
 e.get('note','作者提供图像与案例页，本项目未独立重跑；点击原页查看完整提示词及生成条件。'),'',
 f"[图片、提示词与来源详情]({prefix}cases/{e['id']}.md) · [原始出处]({e['source_url']})",'']
dest=R/'docs/image25';(dest/'cases').mkdir(parents=True,exist_ok=True)
for e in entries:
 page=['# '+e['title'],'','[来源索引](../README.md) · [31 类创作图谱](../../../skills/image25/references/gallery.md) · [如何使用提示词](../../prompts.md)','',
 f"作者：{e['author']} · 分类：{e['category']}",'',f"模型依据：{e['model_claim']} · {labels[e['verification']]}",'',
 e.get('note','作者声明使用 Image 2.5；此记录不代表本项目独立测试。'),'']
 for i,p in enumerate(e['images'],1):page+=[f"![{e['title']} · {i}]({p['url']})",'']
 if e.get('reference_images'):
  page+=['## 输入参考','']
  for p in e['reference_images']:page+=[f"![输入参考]({p['url']})",'']
 page+=['## 提示词与复现','',
 f"[查看原页及已公开的提示词资料]({e['prompt_url']})",'',
 '原页未公开完整提示词或参数时，不补造“原始 Prompt”。参考图编辑需要作者公开的输入图，或使用你自己的参考图。','']
 if e.get('prompt_excerpt'):page+=['已公开的简短指令：','','~~~text',e['prompt_excerpt'],'~~~','']
 page+=['## 来源记录','',f"[原始出处]({e['source_url']})",'',e['rights'],'',
        '[继续浏览来源作品](../README.md) · [反馈图片或来源错误](https://github.com/Fangx-AI/awesome-image2.5/issues/new?template=correction.md)','']
 (dest/'cases'/f"{e['id']}.md").write_text('\n'.join(page),encoding='utf-8')
 title=html.escape(e['title'])
 body='<a href="../../gallery.html">返回搜索图库</a><h1>'+title+'</h1><p>'+html.escape(e['author']+' · '+labels[e['verification']]+' · '+e['model_claim'])+'</p>'
 body+='<p>'+html.escape(e.get('note','作者声明使用 Image 2.5；本项目未独立重跑。'))+'</p>'
 for img in e['images']:body+='<img src="'+html.escape(img['url'],quote=True)+'" alt="'+title+'">'
 if e.get('reference_images'):
  body+='<h2>输入参考</h2>'
  for img in e['reference_images']:body+='<img src="'+html.escape(img['url'],quote=True)+'" alt="输入参考">'
 if e.get('prompt_excerpt'):body+='<h2>已公开的简短指令</h2><pre>'+html.escape(e['prompt_excerpt'])+'</pre>'
 body+='<p><a href="'+html.escape(e['prompt_url'],quote=True)+'">查看原页及已公开的提示词资料</a></p><p>未公开的提示词或参数不补造。作者保留原始权利。</p>'
 shell='<!doctype html><html lang="zh-CN"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>'+title+'</title><style>body{max-width:1100px;margin:40px auto;padding:0 24px;background:#f4f2ec;color:#243127;font:17px/1.8 system-ui}img{display:block;max-width:100%;max-height:85vh;margin:24px auto}a{color:#35644a}</style>'+body+'</html>'
 (dest/'cases'/f"{e['id']}.html").write_text(shell,encoding='utf-8')
index=['# Image 2.5 来源图库','',f'{len(entries)} 个带图来源条目。官方、平台及社区作者声明分别标注；作者声明不等于本项目独立实测。','',
 '[项目首页](../../README.md) · [31 类创作图谱](../../skills/image25/references/gallery.md) · [怎样使用提示词](../prompts.md)','',
 '本页按较宽的来源分组浏览。需要水彩、纹身、分镜等细分创作方向，请使用 31 类创作图谱。','',
 '| 分类 | 条目 |','| --- | ---: |']
for n,(cat,group) in enumerate(groups.items(),1):
 name=f'category-{n:02d}.md'
 index += [f'| [{cat}]({name}) | {len(group)} |']
 page=['# '+cat,'','[全部分类](README.md)','']
 for e in group:page+=summary(e)
 (dest/name).write_text('\n'.join(page),encoding='utf-8')
(dest/'README.md').write_text('\n'.join(index)+'\n',encoding='utf-8')
(R/'catalog/image25-index.json').write_text(json.dumps({'entries':entries,'duplicate_records':duplicates,'evidence_counts':dict(collections.Counter(e['verification'] for e in entries))},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
# Preserve the earlier complete GPT Image 2 atlas as a secondary learning library.
legacy=(R/'README.md').read_text(encoding='utf-8').replace('](assets/','](../assets/').replace('](docs/','](').replace('](vendor/','](../vendor/').replace('](THIRD_PARTY_NOTICES.md)','](../THIRD_PARTY_NOTICES.md)').replace('](CONTRIBUTING.md)','](../CONTRIBUTING.md)').replace('](skills/','](../skills/')
(R/'docs/legacy-gallery.md').write_text(legacy,encoding='utf-8')
head=['<h1 align="center">Awesome Image 2.5</h1>','',
 '<p align="center">看作品，读提示词，找到可复用的创作方法。</p>','',
 '[在线搜索图库](https://fangx-ai.github.io/awesome-image2.5/) · [按分类浏览](docs/image25/README.md) · [本项目实图](docs/original-gallery.md) · [快速开始](docs/getting-started.md) · [English](README.en.md)','',
 f'**{len(entries)} 个 Image 2.5 带图来源条目 · {len(groups)} 类用途 · 14 个本项目实图案例 · 162 个旧版学习案例**','',
 '收录官方样例、平台展示与社区作者发布的作品。每个条目保留作者、图片、提示词入口和模型依据。作者声明、官方示例与本项目生成记录分别标注，避免把旧版或未知模型输出当作已验证的 2.5。','',
 '## 从作品开始','']
featured=['official-mid-century-modern-posters','official-retrofuturism','reely-sunburst-isometric-diorama','reely-sunburst-exhibition-poster','laplace-141-feishu-collaboration-ui','laplace-123-imported-','x-2097411028510179759','simon-raccoon-chart']
selected=[next(e for e in entries if e['id']==id) for id in featured]
for i in range(0,len(selected),2):
 pair=selected[i:i+2]
 head+=['| '+' | '.join(e['title'] for e in pair)+' |','| --- | --- |',
 '| '+' | '.join(f"[![{e['title']}]({e['images'][0]['url']})](docs/image25/cases/{e['id']}.md)" for e in pair)+' |',
 '| '+' | '.join(e['author']+' · '+labels[e['verification']] for e in pair)+' |','']
head+=['## 按用途浏览','','| 分类 | 案例 |','| --- | ---: |']
for n,(cat,group) in enumerate(groups.items(),1):head += [f'| [{cat}](docs/image25/category-{n:02d}.md) | {len(group)} |']
head+=['','## 怎样用到自己的工作里','',
 '1. 选作品，打开案例页查看作者来源和提示词入口。',
 '2. 明确替换对象、文字、配色及参考图，保留布局与编辑约束。',
 '3. 生成后检查文字、结构、身份和编辑范围；不要把好看的预览当作所有要求都已满足。','',
 '~~~sh','uv tool install git+https://github.com/Fangx-AI/awesome-image2.5',
 'image25 --prompt-file your-prompt.txt --model flare --dry-run',
 'image25 --prompt-file your-prompt.txt --model flare -o output.png','~~~','',
 '[安装 Skill](docs/getting-started.md) · [编辑工作流](docs/workflows.md) · [质量检查](docs/quality.md)','',
 '## 本项目实图与学习图谱','',
 '| 系列包装 | 角色三视图 |','| --- | --- |','| ![包装](assets/showcase/coffee-packaging.png) | ![角色](assets/showcase/courier-character.png) |','',
 '[14 个原创实图案例](docs/original-gallery.md)附完整提示词、拆解、替换方法和实际缺陷；宿主没有返回精确模型 ID。',
 '[31 类完整参考图谱](docs/legacy-gallery.md)基于 Wuyoscar 的 MIT 项目改造，162 个原始案例保留 GPT Image 2 标注及作者来源。','',
 '## 来源与维护','',
 '[采集与证据记录](docs/research.md) · [投稿指南](CONTRIBUTING.md) · [第三方许可](THIRD_PARTY_NOTICES.md)','',
 '图像通过作者原始地址或上游固定提交引用，需要联网。原作者保留权利；缺失的提示词或模型证据不会补造。社区项目，与 OpenAI 无官方关联。','']
(R/'README.md').write_text('\n'.join(head),encoding='utf-8')
# Add source-backed Image 2.5 cards and make them the initial view.
p=R/'docs/gallery.html';page=p.read_text(encoding='utf-8')
page=page.replace('<option value="">全部案例</option>','<option value="image25" selected>Image 2.5 来源图库</option><option value="">全部案例</option>')
cards=[]
for e in entries:
 card='<article data-kind="image25" data-search="'+html.escape(e['category']+' '+e['title']+' '+e['author'],quote=True)+'">'
 card+='<a href="image25/cases/'+e['id']+'.html"><img loading="lazy" src="'+html.escape(e['images'][0]['url'],quote=True)+'" alt="'+html.escape(e['title'],quote=True)+'"></a>'
 card+='<div class="text"><small>'+html.escape(e['category']+' · '+labels[e['verification']])+'</small><h2>'+html.escape(e['title'])+'</h2><p>'+html.escape(e['author'])+'</p><a href="image25/cases/'+e['id']+'.html">查看图片与证据</a> · <a href="'+html.escape(e['prompt_url'],quote=True)+'">原页与提示词资料</a></div></article>'
 cards.append(card)
page=page.replace('<main class="grid">','<main class="grid">'+''.join(cards))
page=page.replace('真实输出、完整提示词，以及如何换成自己的内容。','浏览作品、查看来源与可用提示词。')
page=page.replace('162 个上游 GPT Image 2 参考案例 + 14 个本项目新增实图。来源与模型状态分别标注；上游图片需要联网加载。',f'{len(entries)} 个 Image 2.5 来源条目，另有本项目实图与旧版参考资料。来源和模型证据分别标注；远程图片需联网加载。')
p.write_text(page,encoding='utf-8')
print('Published Image 2.5 source index:',len(entries),'cases;',len(groups),'categories')
