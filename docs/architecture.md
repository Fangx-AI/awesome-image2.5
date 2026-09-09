# 项目结构与维护

所有发布页面统一运行 `python scripts/build_all.py` 重建。它按依赖顺序构建提示词实验区、本项目实图、旧版图谱、来源详情，最后由 `build_repository.py` 构建 GitHub README 与 31 类 Skill 图谱；不要只运行其中一个脚本后提交首页。

`catalog/taxonomy.json` 维护 31 类的顺序、用途、检查点、新编练习 Prompt 和社区作品归类；`catalog/category-index.json` 是生成的计数索引。`skills/image25/references/gallery.md` 是 Skill 的正式分类入口；原有未出图实验目录迁到 `prompt-lab-index.md`。中英 README 使用同一份样张与分类顺序生成。

`catalog/web-image25.json` 与 `catalog/community-image25.json` 是当前来源记录，生成 `catalog/image25-index.json`、分类页面及独立 Markdown / HTML 详情页。`scripts/collect_x_posts.py` 批量读取已发现的公开 X 链接；`scripts/collect_community_cases.py` 读取固定提交的社区案例。采集需要网络，日常构建不需要网络。

`vendor/gpt-image2/` 保留上游原始快照与 MIT 许可。这里的原始相对链接不作本地导航使用；面向读者的转换版本在 `docs/reference-atlas/`。旧版资料与型号未知的本项目生成记录不进入默认 Image 2.5 筛选。

```text
catalog/recipes.json               提示词与元数据的维护源
catalog/recipes.csv / recipes.jsonl 批量导出
src/image25/                       安装包与 CLI
skills/image25/                    生图编辑 Skill 与可独立安装的参考资料
skills/image25-reverse-prompt/      看图提炼提示词 Skill
scripts/build_catalog.py           生成提示词实验区、导出和安装包数据
scripts/build_showcase.py          生成实图首页、画廊与 Skill 案例
catalog/showcase-notes.json        实图用途、拆解、替换方法与观察记录
scripts/gallery-template.html      提示词实验区模板
docs/prompt-lab.html               未出图提示词搜索
docs/gallery.html                 可搜索的实图画廊
docs/showcase.md                  有真实图片的精选案例
assets/showcase/                  精选输出与生成来源记录
tests/                           不调用付费接口的测试
```

## 更新提示词

编辑 catalog/recipes.json 后运行：

```sh
python scripts/build_all.py
python -m unittest discover -s tests -v
```

每条记录必须有唯一 id、所属分类、完整提示词、mode、kind、family_id、variant、status、建议尺寸和最低参考图数量。

变体的 family_id 必须对应基础案例。变体不能通过改标题伪装成不同的原创场景，也不进入实图首页。

## 更新实图案例

将原始 PNG、完整 TXT 提示词及 JSON 生成记录放入 assets/showcase/；在 catalog/showcase-notes.json 写入实际观察。在 build_showcase.py 的分类路由中登记案例 ID，然后运行 python scripts/build_showcase.py。首页、搜索画廊与 Skill 参考页从同一份资料生成。不要直接修改生成页。生成记录中模型未知时保留 null，不推断具体模型。

## 使用边界

`--recipe` 只选择提示词，不静默覆盖 CLI 模型、尺寸或质量。索引中的 model 和 size 是建议值，实际请求以命令行设置为准。
批量清单相对路径以清单所在目录为基准；任务相互独立，不支持把前一任务尚未生成的输出当作下一任务输入。
批量运行失败即停；成功文件保留。再次运行请移除已完成任务或更换输出路径。

## 发布前

确认生成资料与维护源一致、所有本地链接有效、安装包包含 catalog JSON、CLI dry-run 可用、测试通过。公开图像需要注明来源。不要把私人输入图或环境文件放进提交。
