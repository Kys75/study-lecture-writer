# study-lecture-writer · 讲义与学习笔记写作

帮助 Agent 编写、续写和修订面向学习者的讲义、概念解释、公式推导与论文导读。重点是按需解释新概念、补齐前置知识、保持符号含义一致，并让读者能够重建推理过程。

由 [Kys75](https://github.com/Kys75) 维护，初始内容整理自作者本机使用的 Skill。仓库根目录就是完整 Skill；核心规则见 [SKILL.md](SKILL.md)。这是独立的 Agent Skill，不是 Obsidian 应用插件。

## 在 Codex 中安装

先确保 Codex 能正常工作，再把下面这段话复制给 Agent。如果仓库为私有，你的 GitHub 账号还需要具备读取权限，并在本机完成相应认证。

```text
请从 https://github.com/Kys75/study-lecture-writer 安装 study-lecture-writer。
Skill 位于仓库根目录；如果使用 skill-installer，请指定仓库内路径 .，并把安装名称设为 study-lecture-writer。
安装到当前用户的 .agents/skills/study-lecture-writer 目录。
先阅读仓库说明并检查已有同名 Skill；已有时先比较差异，不要直接覆盖。
保留 SKILL.md、agents 以及仓库附带的 scripts、references、assets 等目录。
完成后报告来源版本和实际安装位置，并检查 Skill 能否被识别。
```

此方式适用于 Mac 和 Windows，由 Agent 根据当前系统处理路径。新 Skill 未出现时，先开一个新对话；仍未出现再重启客户端。

### 手动安装（可选，需要 Git）

Mac 终端：

```sh
mkdir -p "$HOME/.agents/skills"
git clone https://github.com/Kys75/study-lecture-writer.git "$HOME/.agents/skills/study-lecture-writer"
```

Windows PowerShell：

```powershell
New-Item -ItemType Directory -Force "$HOME/.agents/skills" | Out-Null
git clone https://github.com/Kys75/study-lecture-writer.git "$HOME/.agents/skills/study-lecture-writer"
```

最终应直接存在 `.agents/skills/study-lecture-writer/SKILL.md`。已有同名目录时先比较版本，不要删除或覆盖已有改动。

## 使用示例

```text
请使用 $study-lecture-writer，为只学过高中数学的读者写一篇梯度下降入门讲义。先说明它要解决的问题，在每个概念第一次需要时解释它，给出一个能手算的小例子。保存到当前项目的 gradient-descent.md，并区分定义、假设和推导结果。
```

可以直接在对话中解释，也可以按用户要求保存 Markdown。它支持新讲义、系列讲义续写、针对困惑的解释与已有内容修订；不会要求所有材料都采用同一种篇幅或排版。

## 依赖

写作规则本身没有额外程序依赖。可选的 Markdown 格式检查脚本需要 Python 3.10 或更新版本，仅使用标准库。引用资料需要当前 Agent 能读取相应来源。

## 检查方法与边界

在本仓库或已安装的 Skill 目录中运行；把示例文件路径替换为自己的文件。使用本机有效的 Python 命令：通常 Mac 为 `python3`，Windows 为 `python` 或 `py`。

```sh
python scripts/validate_markdown_notes.py --allow-blank-lines "path/to/lecture.md"
```

常规 Markdown 可使用上面的 `--allow-blank-lines`。只有明确采用紧凑、无空行笔记风格时才省略它。退出码 `0` 表示所检查的格式项通过，`1` 表示失败。

脚本仅检查空行规则和未转义的 `$$` 分隔符数量是否成对，**不能验证公式正确性、完整 LaTeX 语法或教学质量**。定义、推导、前置知识和符号含义仍需按 Skill 中的内容审查规则核对。

## 资源

- [讲义质量标准](references/lecture-standards.md)
- [持续学习与修订流程](references/interactive-workflow.md)
- [可选的 Obsidian 排版规则](references/obsidian-markdown.md)
- [格式检查脚本](scripts/validate_markdown_notes.py)

## 更新

请 Agent 对比已安装版本与本仓库的改动，再更新需要的文件；保留本地定制。维护者在本仓库修改源文件，安装目录只是使用副本。安装或更新后记录使用的提交版本，并做一次小任务验证。

当前发布检查覆盖 Skill 结构、资源链接和本机 Python 脚本行为；没有把这些检查等同于所有模型和所有操作系统上的完整任务验收。
