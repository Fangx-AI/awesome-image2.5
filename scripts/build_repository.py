"""Build a GitHub-native, category-first README and self-contained Skill atlas."""
import collections
import html
import json
import re
from pathlib import Path

R = Path(__file__).resolve().parents[1]
REPO = 'https://github.com/Fangx-AI/awesome-image2.5'
RAW = 'https://raw.githubusercontent.com/Fangx-AI/awesome-image2.5/main/'
taxonomy = json.loads((R/'catalog/taxonomy.json').read_text(encoding='utf-8'))
current = json.loads((R/'catalog/image25-index.json').read_text(encoding='utf-8'))['entries']
legacy = json.loads((R/'catalog/reference-atlas.json').read_text(encoding='utf-8'))
own = json.loads((R/'catalog/showcase.json').read_text(encoding='utf-8'))
by_slug = {c['slug']: c for c in taxonomy}
by_number = {n: c['slug'] for c in taxonomy for n in c['laplace_numbers']}
groups = collections.defaultdict(list)
overrides = {
 'official-retrofuturism':'retro-and-cyberpunk','official-cyberpunk':'retro-and-cyberpunk',
 'official-mid-century-modern-posters':'typography-and-posters','official-wedding-invitation':'events-and-experience',
 'official-impressionist-cityscape':'fine-art-painting','official-sci-fi-surrealism':'cinematic-film-references',
 'official-vintage-national-park-stamps':'brand-systems-and-identity','official-presentation-image':'research-paper-figures',
 'official-mosaic':'more-illustration-styles','official-stickers':'brand-systems-and-identity',
 'official-80s-headshot':'photography','official-baby-portrait-after':'edit-endpoint-showcase',
 'reely-sunburst-desk-mockup':'screen-photography','reely-sunburst-label-edit':'edit-endpoint-showcase',
 'reely-sunburst-exhibition-poster':'typography-and-posters','reely-sunburst-character-turnaround':'character-design',
 'reely-sunburst-night-studio':'photography','reely-sunburst-ceramic-caddy':'product-and-food',
 'reely-sunburst-lab-composite':'edit-endpoint-showcase','reely-sunburst-isometric-diorama':'isometric',
 'reely-sunburst-phone-in-hand':'screen-photography','reely-sunburst-sticker-transparent':'brand-systems-and-identity',
 'simon-raccoon-chart':'edit-endpoint-showcase','x-2097447432757887207':'illustration',
 'x-2097513469172129825':'photography','x-2097411028510179759':'photography',
 'x-2097486896750338125':'edit-endpoint-showcase',
}
for e in current:
    match = re.match(r'laplace-(\d+)-', e['id'])
    slug = by_number.get(int(match[1])) if match else overrides.get(e['id'])
    if not slug:
        raise ValueError('Unclassified source: '+e['id'])
    groups[slug].append(e)
own_groups = {
 'tea-campaign':'typography-and-posters','tea-lightbox':'edit-endpoint-showcase',
 'pet-portrait':'photography','pet-scarf':'edit-endpoint-showcase','field-notes-ui':'ui-ux-mockups',
 'rainy-bookshop':'illustration','ceramic-skincare':'beauty-and-lifestyle','coffee-packaging':'brand-systems-and-identity',
 'citrus-menu':'product-and-food','outdoor-watch':'product-and-food','botanical-fieldguide':'infographics-and-field-guides',
 'rooftop-library':'architecture-and-interior','courier-character':'character-design','isometric-teahouse':'isometric',
}
labels = {'official-sample':'官方示例','provider-reported':'平台声明','author-reported-with-command':'作者附命令',
 'author-claim-via-public-mirror':'X 作者声明','author-reported-not-independently-tested':'社区作者声明'}

def source_case(e):
    return dict(id=e['id'],title=e['title'],image=e['images'][0]['url'],
      tag='Image 2.5 · '+labels[e['verification']],author=e['author'],source=e['source_url'],
      prompt=e.get('prompt_excerpt'),prompt_url=e['prompt_url'],kind='source')

def own_case(e):
    return dict(id=e['id'],title=e['title'],image=RAW+'assets/showcase/'+e['id']+'.png',
      tag='本项目生成 · 精确型号未知',author='Fangx-AI',source=REPO+'/blob/main/docs/showcase.md',
      prompt=e['prompt'],note=e['check'],metadata='Generated: '+e['date']+' · Postprocessing: '+e['postprocessing'],kind='own')

def legacy_case(e):
    return dict(id=e['id'],title=e['title'],image=e['images'][0],tag='GPT Image 2 · 旧版学习参考',
      author='Wuyoscar / 原页署名作者',source=e['upstream'],prompt=e['prompts'][0]['text'],metadata=e['metadata'],kind='legacy')

def preview(cases):
    lines=['<table>']
    for start in range(0,len(cases),2):
        lines.append('<tr>')
        for e in cases[start:start+2]:
            lines.append('<td width="50%" align="center" valign="top"><a href="'+html.escape(e['source'],quote=True)+'"><img src="'+html.escape(e['image'],quote=True)+'" width="100%" alt="'+html.escape(e['title'],quote=True)+'"/></a><br/><strong>'+html.escape(e['title'])+'</strong><br/><sub>'+html.escape(e['tag']+' · '+e['author'])+'</sub></td>')
        lines.append('</tr>')
    lines.extend(['</table>',''])
    return lines

def details(e):
    lines=['<details>', '<summary>Prompt · '+html.escape(e['title'])+'</summary>','',
           f"[{e['author']} · 原始出处]({e['source']}) · **{e['tag']}**",'']
    if e.get('metadata'): lines += [e['metadata'],'']
    if e.get('prompt'):
        if e['kind']=='source': lines+=['原页公开的短指令；完整条件以作者原页为准。','']
        lines+=['~~~text',e['prompt'],'~~~','']
    if e.get('prompt_url'):
        lines += [f"[原作者提示词与生成条件]({e['prompt_url']})",'',
                  '未在本仓库转载完整 Prompt；原页未公开的参数不补造。','']
    if e.get('note'): lines += ['实际观察：'+e['note'],'']
    return lines+['</details>','']

catalog=[]
refs=R/'skills/image25/references'
# Preserve the prompt-only router before replacing the canonical Skill front door.
(refs/'prompt-lab-index.md').write_text((refs/'gallery.md').read_text(encoding='utf-8'),encoding='utf-8')
for c in taxonomy:
    slug=c['slug']; filename='gallery-'+slug+'.md'
    old=[e for e in legacy['entries'] if e['category_file']==filename]
    recent=[source_case(e) for e in groups[slug]]
    # Official material is a deliberate cross-reference, not another unique case count.
    if slug=='official-openai-cookbook-examples': recent=[source_case(e) for e in current if e['verification']=='official-sample']
    originals=[own_case(e) for e in own if own_groups[e['id']]==slug]
    selected=recent[:2]
    if not selected: selected=originals[:2] or [legacy_case(e) for e in old[:2]]
    c.update(file=filename,current_count=len(recent),own_count=len(originals),legacy_count=len(old),selected=selected)
    page=['# '+c['title'],'','[分类索引](gallery.md) · [Prompt Craft](craft.md)','',
          f"Image 2.5 来源 {len(recent)} · 本项目型号未知实图 {len(originals)} · 旧版学习参考 {len(old)}",'',
          '## 本类怎样写','',c['schema'],'','检查：'+c['check'],'',
          '## 可改写的起始 Prompt','',
          '**本项目新编写的练习 Prompt，尚未出图；不是下方来源作品的原始提示词。**','',
          '~~~text',c['prompt'],'~~~','',
          '## Image 2.5 来源作品','']
    if not recent: page+=['当前尚无归入本类的 Image 2.5 来源实图；下方保留明确标注的其他学习资料。','']
    for e in recent: page+=['### '+e['title'],'']+preview([e])+details(e)
    if originals:
        page+=['## 本项目实图：精确型号未知','']
        for e in originals: page+=['### '+e['title'],'']+preview([e])+details(e)
    page+=['## GPT Image 2 学习图谱','',
           '**以下是旧版模型作品；保留原作者与 MIT 许可，不计入 Image 2.5 来源数量。**','',
           '[上游许可与第三方声明]('+REPO+'/blob/main/THIRD_PARTY_NOTICES.md)','']
    for e in old: page+=['### '+e['title'],'']+preview([legacy_case(e)])+details(legacy_case(e))
    (refs/filename).write_text('\n'.join(page)+'\n',encoding='utf-8')
    catalog.append({k:v for k,v in c.items() if k not in ['prompt','selected']})
router=['# Image 2.5 分类图谱','',
        '先按交付物选择分类，再读取对应文件中的实际案例和 Prompt。通常只读一个分类；混合任务最多读取邻近两到三个分类。','',
        '31 类是组织体系，不代表每类都有 Image 2.5 实图。官方栏目重复引用官方样例，不增加唯一条目总数。','',
        '| 分类 | 2.5 来源 | 型号未知实图 | 旧版参考 |','| --- | ---: | ---: | ---: |']
for c in taxonomy: router.append(f"| [{c['title']}]({c['file']}) | {c['current_count']} | {c['own_count']} | {c['legacy_count']} |")
router+=['','[写法与检查](craft.md) · [仅提示词实验区](prompt-lab-index.md) · [API 参数](api.md)','']
(refs/'gallery.md').write_text('\n'.join(router),encoding='utf-8')
(R/'catalog/category-index.json').write_text(json.dumps(catalog,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

def readme(english=False):
    title='GPT Image 2.5 · Prompt Gallery + Agent Skills + CLI'
    lines=['<h1 align="center">'+title+'</h1>','',
      '<p align="center">'+('A category-first prompt and image reference repository for creative work.' if english else '按创作任务组织的提示词、效果图、Agent Skills 与生图工具。')+'</p>','',
      '[中文](README.md) · [English](README.en.md) · [分类导航](#gallery-index) · [安装](#installation) · [完整分类图谱](skills/image25/references/gallery.md)','',
      '![Validate](https://github.com/Fangx-AI/awesome-image2.5/actions/workflows/tests.yml/badge.svg) ![Python](https://img.shields.io/badge/Python-3.10%2B-blue) ![Categories](https://img.shields.io/badge/Categories-31-35644a)','',
      '![Original concept cover](assets/cover.png)','',
      '[原创概念封面 · 生成来源 / Cover provenance](assets/PROVENANCE.md)','',
      '## '+('At a glance' if english else '✨ 一眼看懂'),'',
      '| '+('Surface | Content' if english else '板块 | 内容')+' |','| --- | --- |',
      '| Gallery | 31 categories · 146 Image 2.5 source records |',
      '| Prompts | 31 new practice briefs · 14 original output demonstrations · 162 attributed legacy cases |',
      '| Agent Skills | image25 · image25-reverse-prompt |',
      '| CLI | Generate · Edit · Multi-reference · Mask · Batch · Dry run |','',
      ('Official samples, provider claims, author claims and unknown-model outputs are labeled separately. Most community records currently come from LaplaceYoung. Legacy GPT Image 2 images are never relabeled as 2.5.' if english else '官方样例、平台声明、作者声明和本项目型号未知输出分别标注。当前社区来源较集中于 LaplaceYoung；GPT Image 2 学习图不会改名充当 2.5 实测。'),'',
      '## '+('What this repository is for' if english else '🔎 这个仓库适合什么场景'),'',
      ('Find a deliverable below, inspect the images and expand the prompt. Use the full category file when drafting with an agent. The README is the selected showcase; the Skill atlas contains the complete collection.' if english else '做动漫分镜、游戏 HUD、中文海报、品牌系统、摄影、科研示意、UI、建筑或参考图编辑：先在下方找对应板块，看成组效果图，展开 Prompt，再进入同类完整资料。README 展示精选；Skill 分类文件保留完整案例。'),'',
      '<a id="installation"></a>','', '## '+('Installation' if english else '📥 安装'),'',
      '<details><summary>Codex · Agent Skills</summary>','',
      '~~~text','$skill-installer','Install this skill from GitHub:',REPO+'/tree/main/skills/image25','',
      '# Optional: extract prompts from reference images',REPO+'/tree/main/skills/image25-reverse-prompt','~~~','',
      '[安装、配置和更新](docs/getting-started.md) · [Skill 运行说明](skills/image25/SKILL.md)','', '</details>','',
      '<details><summary>CLI · Python 3.10+</summary>','',
      '~~~sh','uv tool install git+https://github.com/Fangx-AI/awesome-image2.5',
      'image25 --prompt-file prompt.txt --model flare --dry-run',
      'image25 --prompt-file prompt.txt --model flare -o generated/result.png','~~~','',
      '`OPENAI_API_KEY` is read from the process environment. Live calls require API access.','', '</details>','',
      '## '+('Quick usage and prompting fundamentals' if english else '⚡ 快速使用与提示词基础'),'',
      '~~~text','用 image25 参考“品牌系统与视觉识别”分类，为山间书店设计一套统一的视觉识别。',
      '用 image25-reverse-prompt 分析这张参考图，提取构图、材质、光线与媒介边界。',
      '编辑第 1 张图：只替换围巾颜色，保留身份、姿势、光线和背景。','~~~','',
      '[完整 CLI 参数](docs/getting-started.md#参数) · [Prompt Craft](skills/image25/references/craft.md) · [编辑工作流](docs/workflows.md)','',
      '### '+('Reference editing: input and result' if english else '参考图编辑：输入与结果'),'',
      '| Input / 参考图 | Output / 编辑结果 |','| --- | --- |',
      '| ![Input](assets/showcase/pet-portrait.png) | ![Output](assets/showcase/pet-scarf.png) |','',
      '**host-model-unknown** · [完整 Prompt 与实际观察](skills/image25/references/showcase/pet-scarf.md)','',
      '<a id="gallery-index"></a>','', '## '+('Selected prompt gallery' if english else '🎨 提示词精选展示'),'',
      ('Jump to a section or open its full Markdown atlas. Each category separates source images, original demonstrations and legacy references.' if english else '点击分类名称跳到本页样张；点击“完整 MD”读取该类全部作品、提示词、写法和检查要点。'),'', '<table>']
    for start in range(0,len(taxonomy),3):
        lines.append('<tr>')
        for c in taxonomy[start:start+3]:
            name=c['slug'].replace('-',' ').title() if english else c['title']
            lines.append(f'<td align="center" width="33%"><strong><a href="#gallery-{c["slug"]}">{name}</a></strong><br/><sub><a href="skills/image25/references/{c["file"]}">完整 MD / Full atlas</a></sub></td>')
        lines.append('</tr>')
    lines+=['</table>','']
    for c in taxonomy:
        name=c['slug'].replace('-',' ').title() if english else c['title']
        lines += [f'<a id="gallery-{c["slug"]}"></a>','',f'<h2 align="center">{name}</h2>','',
          f'[↑ Index](#gallery-index) · [完整分类 / Full atlas](skills/image25/references/{c["file"]})','',
          f"**Image 2.5: {c['current_count']} · host-model-unknown: {c['own_count']} · GPT Image 2: {c['legacy_count']}**",'',
          c['schema']+'。'+c['check']+'。','']
        if not c['current_count']: lines+=['> 本类暂缺 Image 2.5 来源作品；以下样张的真实型号状态已逐图标注。','']
        lines+=preview(c['selected'])
        for e in c['selected']: lines+=details(e)
        lines += ['<details><summary>本类起始 Prompt / Original practice brief</summary>','',
          '**prompt-only** · 本项目编写，尚未出图；不是上方示例图的原始 Prompt。','',
          '~~~text',c['prompt'],'~~~','', '</details>','']
    lines += ['## '+('Credits and contribution' if english else '🙏 致谢与贡献'),'',
      '[Wuyoscar / GPT-Image2-Skill](https://github.com/wuyoscar/GPT-Image2-Skill) 提供了分类展示、按需读取的 Skill 图谱和旧版案例参考。上游 MIT 版权声明及外部作者署名保留。', '',
      '[OpenAI](https://openai.com/index/introducing-chatgpt-images-2-5/) · [LaplaceYoung](https://github.com/LaplaceYoung/awesome-gpt-image-2.5) · [来源与证据](docs/research.md)','',
      '[贡献指南](CONTRIBUTING.md) · [行为准则](CODE_OF_CONDUCT.md) · [支持说明](SUPPORT.md) · [安全政策](SECURITY.md) · [第三方许可](THIRD_PARTY_NOTICES.md)','',
      '[逐板块对照记录](docs/reference-study.md) · [项目结构](docs/architecture.md)','',
      'Community project; not affiliated with OpenAI. Original content: CC0. Third-party content retains its original license.','']
    return '\n'.join(lines)

(R/'README.md').write_text(readme(),encoding='utf-8')
(R/'README.en.md').write_text(readme(True),encoding='utf-8')
print('Built GitHub-first README and 31 self-contained category files.')
