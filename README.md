# Novel-Craft

面向 AI 协作小说创作的公开框架。

`novel-craft` 关注的不是"一键写更多"，而是"怎么把小说写得更稳、更像人、更不容易模板化"。

## 这是什么

用 AI 写小说写久了，你一定遇到过这些问题：

- 角色写着写着就没了灵魂，变成一个标签在跑——温柔的永远温柔，冷酷的永远冷酷，像 NPC 不像人
- 前面写得好的桥段，后面被 AI 原样再来一遍，你自己都觉得腻了
- 写了几十章之后，角色状态乱了、伏笔丢了、前后矛盾了，AI 根本记不住
- 换一个对话窗口，之前攒的所有默契和语感全没了，从头来过

novel-craft 就是来解决这些问题的。

它不帮你自动生成小说，它帮你在和 AI 协作写作的过程中，把角色写活、把套路打破、把长篇写稳。

## 快速开始

点击页面上方绿色 **Code** 按钮 → **Download ZIP**，解压到本地。然后从 [`SKILL.md`](./SKILL.md) 开始读。

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
