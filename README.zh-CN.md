<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/maker-dark.svg">
  <img src="assets/maker-light.svg" width="100%" alt="王钰钦 — 从日常生活出发，做小产品，也做帮助自己使用 AI 的工具。">
</picture>

### 你好，我是王钰钦 / Yuqin

独立产品创作者。我做的东西，往往来自自己想做的一件小事：随口记下一件待办，从普通照片里发现一点知识，或让没做完的 AI 任务接着往下走。

**[逛逛我的网站 ↗](https://yuqin.wang/)** &nbsp; · &nbsp; [文章](https://yuqin.wang/#/articles) &nbsp; · &nbsp; [English](README.md)

## 现在主推：随口清单

**说一句记下，说一句完成。** 一个接在语音输入习惯后面的桌面待办工具：识别要做什么、做完了什么，按需提醒，并保留撤销入口。

[<img src="assets/voice-todo-zh.svg" width="100%" alt="随口清单的创建与完成流程示意，非应用截图。">](https://github.com/wangyuqin378-cpu/voice-todo)

**macOS 26 · 开发版 · 源码已公开**。目前需要本机构建，尚无公证安装包；后台语音需要明确的开头口令。外部转写接收仍在试验，真人语音和通知送达待验收。

**[了解与构建 →](https://github.com/wangyuqin378-cpu/voice-todo/blob/main/README.zh-CN.md)** · [使用指南](https://github.com/wangyuqin378-cpu/voice-todo/blob/main/docs/USAGE.md)

## 把日常，再看仔细一点

<table>
<tr>
<td width="50%" valign="top">
  <h3><a href="https://github.com/wangyuqin378-cpu/jianwei">见微 / Jianwei</a></h3>
  <p>相册里，藏着一点新知识。把日常照片变成知识卡，每张卡都能追溯来源。</p>
  <p><strong>iPhone · 开发中</strong></p>
  <p align="center"><a href="https://yuqin.wang/#/project/jianwei"><img src="assets/jianwei-today.webp" width="190" alt="见微真实开发预览：一张扫帚照片、知识卡和来源链接。"></a></p>
  <p><a href="https://yuqin.wang/#/project/jianwei"><strong>看看产品 ↗</strong></a> · <a href="https://github.com/wangyuqin378-cpu/jianwei">查看仓库</a></p>
</td>
<td width="50%" valign="top">
  <h3><a href="https://yuqin.wang/#/project/city">城市副本 / City Copy</a></h3>
  <p>给散步找一个小理由。跟着每日任务观察城市，拍下发现，再做成自己的城市小志。</p>
  <p><strong>iPhone · 开发中</strong></p>
  <p align="center"><a href="https://yuqin.wang/#/project/city"><img src="assets/city-task.webp" width="190" alt="城市副本真实开发预览：今天的城市探索小任务。"></a></p>
  <p><a href="https://yuqin.wang/#/project/city"><strong>看看产品 ↗</strong></a> · 源码私有</p>
</td>
</tr>
</table>

<details>
<summary>关于这些开发预览</summary>

图片来自持续开发中的真实界面。见微公开仓库保留较早的工程快照，不能据此复现图中版本。两个产品的公开下载、最终真机验收和正式分发仍待完成。

</details>

## 让有用的工作，接着往下走

### [Context Continuity](https://github.com/wangyuqin378-cpu/context-continuity)

AI 长任务也需要书签。保存已经做出的决定、找到的证据和下一步，让新会话接着做。

<picture>
  <source media="(prefers-color-scheme: dark) and (max-width: 600px)" srcset="assets/continuity-mobile-dark.svg">
  <source media="(max-width: 600px)" srcset="assets/continuity-mobile-light.svg">
  <source media="(prefers-color-scheme: dark)" srcset="assets/continuity-dark.svg">
  <img src="assets/continuity-light.svg" width="100%" alt="使用过程：决定和证据 → 保存带有下一步的检查点 → 在新会话中继续。">
</picture>

**[跟着示例试一次 →](https://github.com/wangyuqin378-cpu/context-continuity/tree/main/examples/quickstart)** &nbsp; · &nbsp; [v2.1.0](https://github.com/wangyuqin378-cpu/context-continuity/releases/tag/v2.1.0) · MIT · Python 3.9+

上图是流程示意。已支持的行为与评测边界见仓库说明。

### 工作台上的其他尝试

- **[Prompt Generation Loop](https://github.com/wangyuqin378-cpu/prompt-generation-loop)** — 从产品目标和坏例出发，生成可测试的 Prompt。*Agent Skill 原型。*
- **[Codex Resume Manager](https://github.com/wangyuqin378-cpu/codex-resume-manager)** — 额度恢复后，继续已登记守护的原任务。*macOS 本地工具；真实额度中断验收待完成。*
- **[Just Do It](https://github.com/wangyuqin378-cpu/just-do-it)** — 把纪要和零散输入整理成行动与后续事项。*依赖内部服务的工作流实验。*
- **[Texas Hold’em](https://github.com/wangyuqin378-cpu/texas-holdem)** — 给朋友开一桌浏览器牌局，也能和机器人练习。*学习 Demo。*

## 工作台上的新进展

最近的公开开发记录，点进去可以看到具体改动。

<!-- updates:start -->
- 2026-09-17 · **开发更新** · voice-todo — [docs: explain voice workflow, setup and build28 opening phrases](https://github.com/wangyuqin378-cpu/voice-todo/commit/61b8951e5c7932b634b87994d68900aa79341e7f)
- 2026-09-17 · **开发更新** · codex-resume-manager — [docs: clarify purpose, first use and motivation in both languages](https://github.com/wangyuqin378-cpu/codex-resume-manager/commit/b7050a7c132d33df44abac1929a9fe7a03ceff7d)
- 2026-09-17 · **开发更新** · prompt-generation-loop — [docs: clarify purpose, first use and motivation in both languages](https://github.com/wangyuqin378-cpu/prompt-generation-loop/commit/96bdf6b115710f457bc497222cd20193a2c1d6d7)
- 2026-09-17 · **开发更新** · context-continuity — [docs: clarify purpose, first use and motivation in both languages](https://github.com/wangyuqin378-cpu/context-continuity/commit/16da5c9a8f4a2d9f9f6f2092c8fde5d96bc08e32)
- 2026-09-17 · **开发更新** · jianwei — [docs: clarify purpose, first use and motivation in both languages](https://github.com/wangyuqin378-cpu/jianwei/commit/70c8ff48d796f381a748ded4d7f599bc8f7738cf)
<!-- updates:end -->

[完整更新 →](UPDATES.md) &nbsp; · &nbsp; [更多作品与故事 ↗](https://yuqin.wang/#/projects)
