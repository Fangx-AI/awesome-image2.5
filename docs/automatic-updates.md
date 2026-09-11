# 持续采集、自动审核与发布

本项目由 Codex 的定时任务执行每日更新，运行位置是维护者的本机 Codex 环境。GitHub 保存审核后的仓库内容；当前不是无需本机在线的 GitHub Actions 云端 AI 审核服务。

## 每次运行

1. 检查远端提交和工作区，保护尚未提交的人工修改。
2. 通过公开 GitHub API 发现新仓库和 X 帖子线索，增量读取已知案例库与官方来源。
3. 在 `.cache/update-review/` 保存候选结果，不直接覆盖正式目录。
4. 由 Agent 阅读原始来源、查看实际图片，审核模型依据、提示词与图片关系、来源许可、重复和分类。关键词命中只算线索。
5. 通过审核的条目加入正式维护源，保留官方、平台或作者声明的证据标签；自动审核不等于独立重跑模型。
6. 构建 README 和 Skill 图谱，运行测试与链接检查，检查差异后自动提交、推送并验证 CI。

不需要人工逐条批准。证据缺失、来源矛盾、无法查看图片或授权不清的候选不发布；来源故障不删除既有内容。没有有效变化时不制造空提交。

## 采集命令

```sh
python scripts/discover_updates.py --output-dir .cache/update-review
python scripts/collect_community_cases.py --output .cache/update-review/community.json
python scripts/collect_x_posts.py .cache/update-review/new-x-seeds.json --output .cache/update-review/x.json
```

采集程序只做发现、读取和初步筛选，最终内容判断由定时运行的 Agent 执行。审核通过的新条目可使用 `category_slug` 指定 31 类中的类别；必须与 `catalog/taxonomy.json` 中的 slug 匹配。

## 运行边界

自动任务依赖本机 Codex 可运行、网络可用和 GitHub 登录有效。离线期间不会假装完成审核。任务出错时保留原仓库并报告阻塞，不绕过登录或付费访问限制，不调用付费生图 API 来凑案例。

重大来源错误、凭据失效、无法解决的合并冲突会报告维护者；正常审核与发布不再请求确认。定时设置在 Codex 自动任务中管理，代码和审核方法在本仓库维护。
