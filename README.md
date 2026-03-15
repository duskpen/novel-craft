# Novel-Craft

面向 AI 协作小说创作的公开框架。

`novel-craft` 关注的不是"一键写更多"，而是"怎么把小说写得更稳、更像人、更不容易模板化"。

## 这是什么

一个 `docs + templates` 形式的公开仓库，核心关注点：

- **角色活人感**：角色不是标签在运行，而是像人一样会偏、会绕、会不最优
- **反模板**：前面写得好的东西不会被原样再来一遍
- **长篇不失真**：AI 不会自然记住长篇真正重要的东西，所以靠结构化状态管理来维护

它不是全自动写书引擎，不是多 Agent 生产线。它是一套帮你在 AI 协作写作中把质量守住的框架。

## 快速开始

1. 先读 [`SKILL.md`](./SKILL.md)——这是整个框架从头到尾的教学入口，读完就能开始写。
2. 复制 `templates/` 里的模板到你自己的项目目录，按需填写。
3. 看 [`examples/full-character-example.md`](./examples/full-character-example.md) 理解角色构建的完整流程。
4. 按 3 章为一个批次推进，写完用审稿清单复盘。

用 AI 协作写作时，把 [`SKILL.md`](./SKILL.md) 作为第一份喂给 AI 的文件。

## 仓库结构

```text
novel-craft/
├── SKILL.md                  ← AI 入口，教学式，从头读到尾
├── README.md                 ← 你在这里
├── methods/                  ← 方法论
│   ├── writing-rules.md         写作实战规则（四条铁律）
│   ├── character-design.md      角色构建
│   ├── multi-character.md       多人场景
│   ├── review-checklist.md      审稿清单
│   ├── story-structure.md       章节与弧结构
│   ├── longform-management.md   长篇状态管理
│   └── worldbuilding-feed.md    世界观喂法
├── patches/                  ← 补丁
│   ├── anti-template.md         反模板
│   └── liveness-patch.md        活人感
├── templates/                ← 可复制模板
│   ├── character-palette.template.md
│   ├── character-appearance.template.md
│   ├── character-build-checklist.template.md
│   ├── multi-faces.template.md
│   ├── behavior-boundaries.template.md
│   ├── story-outline.template.md
│   ├── worldbuilding.template.md
│   ├── longform-state.template.md
│   ├── chapter-input-pack.template.md
│   ├── batch-notes.template.md
│   ├── session-snapshot.template.md
│   └── handoff.template.md
├── tools/                    ← 本地检查工具
│   ├── ban-check.py
│   └── README.md
├── examples/                 ← 示例
│   ├── full-character-example.md  完整角色构建示例
│   └── mini-workflow.md           极小工作流示例
└── docs/                     ← 文档
    ├── recommended-workflow.md
    ├── release-scope.md
    └── roadmap.md
```

## 当前边界

这个仓库不包含任何正在创作中的具体小说项目材料（正文、角色档案、世界观答案、大纲答案、批次进度）。

具体边界见 [`docs/release-scope.md`](./docs/release-scope.md)。

## 路线图

当前阶段：公开框架仓库。后续方向见 [`docs/roadmap.md`](./docs/roadmap.md)。

## 许可证

[MIT](./LICENSE)
