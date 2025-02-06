# prompt_definitions.py
# -*- coding: utf-8 -*-
"""
集中存放所有提示词 (Prompt)，整合雪花写作法、角色弧光理论、悬念三要素模型等
并包含新增加的短期摘要/下一章关键字提炼提示词，以及章节正文写作提示词。
"""

# =============== 摘要与下一章关键字提炼 ===============
summarize_recent_chapters_prompt = """\
你是一名资深长篇小说编辑，请分析以下合并文本（可能包含最近几章内容）：
{combined_text}

现在请你基于目前故事的进展，完成以下两件事：
1) 用最多200字，写一个简洁明了的「当前情节短期摘要」。
2) 提炼「下一章」的关键字（例如关键物品、重要人物、地点、事件、情节等），可以用逗号分隔或条目列出。

请按如下格式输出（不需要额外解释）：
短期摘要: <这里写短期摘要>
下一章关键字: <这里写下一章关键字>
"""

# =============== 1. 核心种子设定（雪花第1层）===================
core_seed_prompt = """\
作为专业作家，请用"雪花写作法"第一步构建故事核心：
主题：{topic}
类型：{genre}
篇幅：约{number_of_chapters}章（每章{word_number}字）

请用单句公式概括故事本质，例如：
"当[主角]遭遇[核心事件]，必须[关键行动]，否则[灾难后果]；与此同时，[隐藏的更大危机]正在发酵。"

要求：
1. 必须包含显性冲突与潜在危机
2. 体现人物核心驱动力
3. 暗示世界观关键矛盾
4. 使用25-100字精准表达

仅返回故事核心文本，不要解释任何内容。
"""

# =============== 2. 角色动力学设定（角色弧光模型）===================
character_dynamics_prompt = """\
基于核心种子：
{core_seed}

请设计3-6个具有动态变化潜力的核心角色，每个角色需包含：
特征：
- 背景、外貌、性别、年龄、职业等
- 暗藏的秘密或潜在弱点(可与世界观或其他角色有关)

核心驱动力三角：
- 表面追求（物质目标）
- 深层渴望（情感需求）
- 灵魂需求（哲学层面）

角色弧线设计：
初始状态 → 触发事件 → 认知失调 → 蜕变节点 → 最终状态

关系冲突网：
- 与其他角色的关系或对立点
- 与至少两个其他角色的价值观冲突
- 一个合作纽带
- 一个隐藏的背叛可能性

要求：
仅给出最终文本，不要解释任何内容。
"""

# =============== 3. 世界构建矩阵（三维度交织法）===================
world_building_prompt = """\
为服务核心冲突"{core_seed}"，请构建三维交织的世界观：

1. 物理维度：
- 空间结构（地理×社会阶层分布图）
- 时间轴（关键历史事件年表）
- 法则体系（物理/魔法/社会规则的漏洞点）

2. 社会维度：
- 权力结构断层线（可引发冲突的阶层/种族/组织矛盾）
- 文化禁忌（可被打破的禁忌及其后果）
- 经济命脉（资源争夺焦点）

3. 隐喻维度：
- 贯穿全书的视觉符号系统（如反复出现的意象）
- 氣候/环境变化映射的心理状态
- 建筑风格暗示的文明困境

要求：
每个维度至少包含3个可与角色决策产生互动的动态元素。
仅给出最终文本，不要解释任何内容。
"""

# =============== 4. 情节架构（三幕式悬念）===================
plot_architecture_prompt = """\
基于以下元素构建三幕式悬念架构：
核心种子：{core_seed}
角色体系：{character_dynamics}
世界观：{world_building}

要求按以下结构设计：
第一幕（触发） 
- 日常状态中的异常征兆（3处铺垫）
- 引出故事：展示主线、暗线、副线的开端
- 关键事件：打破平衡的催化剂（需改变至少3个角色的关系）
- 错误抉择：主角的认知局限导致的错误反应

第二幕（对抗）
- 剧情升级：主线+副线的交叉点
- 双重压力：外部障碍升级+内部挫折
- 虚假胜利：看似解决实则深化危机的转折点
- 灵魂黑夜：世界观认知颠覆时刻

第三幕（解决）
- 代价显现：解决危机必须牺牲的核心价值
- 嵌套转折：至少包含三层认知颠覆（表面解→新危机→终极抉择）
- 余波：留下2个开放式悬念因子

每个阶段需包含3个关键转折点及其对应的伏笔回收方案。
仅给出最终文本，不要解释任何内容。
"""

# =============== 5. 章节目录生成（悬念节奏曲线）===================
chapter_blueprint_prompt = """\
根据小说架构：\n
{novel_architecture}

设计{number_of_chapters}章的节奏分布：
1. 章节集群划分：
- 每3-5章构成一个悬念单元，包含完整的小高潮
- 单元之间设置"认知过山车"（连续2章紧张→1章缓冲）
- 关键转折章需预留多视角铺垫

2. 每章需明确：
- 章节定位（角色/事件/主题等）
- 核心悬念类型（信息差/道德困境/时间压力等）
- 情感基调迁移（如从怀疑→恐惧→决绝）
- 伏笔操作（埋设/强化/回收）
- 认知颠覆强度（1-5级）

输出格式示例：
第n章 - [标题]
本章定位：[角色/事件/主题/...]
核心作用：[推进/转折/揭示/...]
悬念密度：[紧凑/渐进/爆发/...]
伏笔操作：埋设(A线索)→强化(B矛盾)...
认知颠覆：★☆☆☆☆
本章简述：[一句话概括]

第n+1章 - [标题]
本章定位：[角色/事件/主题/...]
核心作用：[推进/转折/揭示/...]
悬念密度：[紧凑/渐进/爆发/...]
伏笔操作：埋设(A线索)→强化(B矛盾)...
认知颠覆：★☆☆☆☆
本章简述：[一句话概括]

要求：
- 使用精炼语言描述，每章字数控制在100字以内。
- 合理安排节奏，确保整体悬念曲线的连贯性。
- 在生成{number_of_chapters}章前不要出现结局章节。

仅给出最终文本，不要解释任何内容。
"""

chunked_chapter_blueprint_prompt = """\
根据小说架构：\n
{novel_architecture}

需要生成总共{number_of_chapters}章的节奏分布，

当前已有章节目录（若未空则说明是初始生成）：\n
{chapter_list}

现在请设计第{n}章到第{m}的节奏分布：
1. 章节集群划分：
- 每3-5章构成一个悬念单元，包含完整的小高潮
- 单元之间设置"认知过山车"（连续2章紧张→1章缓冲）
- 关键转折章需预留多视角铺垫

2. 每章需明确：
- 章节定位（角色/事件/主题等）
- 核心悬念类型（信息差/道德困境/时间压力等）
- 情感基调迁移（如从怀疑→恐惧→决绝）
- 伏笔操作（埋设/强化/回收）
- 认知颠覆强度（1-5级）

输出格式示例：
第n章 - [标题]
本章定位：[角色/事件/主题/...]
核心作用：[推进/转折/揭示/...]
悬念密度：[紧凑/渐进/爆发/...]
伏笔操作：埋设(A线索)→强化(B矛盾)...
认知颠覆：★☆☆☆☆
本章简述：[一句话概括]

第n+1章 - [标题]
本章定位：[角色/事件/主题/...]
核心作用：[推进/转折/揭示/...]
悬念密度：[紧凑/渐进/爆发/...]
伏笔操作：埋设(A线索)→强化(B矛盾)...
认知颠覆：★☆☆☆☆
本章简述：[一句话概括]

要求：
- 使用精炼语言描述，每章字数控制在100字以内。
- 合理安排节奏，确保整体悬念曲线的连贯性。
- 在生成{number_of_chapters}章前不要出现结局章节。

仅给出最终文本，不要解释任何内容。
"""

# =============== 6. 全局摘要更新 ===================
summary_prompt = """\
以下是新完成的章节文本：
{chapter_text}

这是当前的全局摘要（可为空）：
{global_summary}

请根据本章新增内容，更新全局摘要。
要求：
- 保留既有重要信息，同时融入新剧情要点
- 以简洁、连贯的语言描述全书进展
- 客观描绘，不展开联想或解释
- 字数控制在2000字以内

仅返回全局摘要文本，不要解释任何内容。
"""

# =============== 7. 角色状态更新 ===================
update_character_state_prompt = """\
以下是新完成的章节文本：
{chapter_text}

这是当前的角色状态文档（可为空）：
{old_state}

请更新角色状态，内容格式：
角色A属性：
├──物品:
    ├──某物(道具)：描述
    ├──XX长剑(武器)：描述
    ...
├──能力
    ├──技能1：描述
    ├──技能2：描述
    ...
├──状态
    ├──身体状态：
        ├──Buff/Debuff
    ├──心理状态：描述
    
├──主要角色间关系网
    ├──角色B：描述
    ├──角色C：描述
    ...
├──触发或加深的事件
    ├──事件1：描述
    ├──事件2：描述
    ...

角色B属性：
├──物品
    ├──...
├──能力
    ├──...
├──状态
    ├──...
├──主要角色间关系网
    ├──...
├──触发或加深的事件
    ├──...

角色C属性：
......

新出场角色：
- 任何新增角色或临时出场人物的基本信息

要求：
- 请直接在已有文档基础上进行增删
- 不改变原有结构，语言尽量简洁、有条理

仅返回更新后的角色状态文本，不要解释任何内容。
"""

# =============== 8. 章节正文写作 ===================

# 8.1 第一章草稿提示
first_chapter_draft_prompt = """\
即将创作：第 {novel_number} 章《{chapter_title}》
本章定位：{chapter_role}
核心作用：{chapter_purpose}
悬念密度：{suspense_level}
伏笔操作：{foreshadowing}
认知颠覆：{plot_twist_level}
本章简述：{chapter_summary}

可用元素：
- 核心人物(可能未指定)：{characters_involved}
- 关键道具(可能未指定)：{key_items}
- 空间坐标(可能未指定)：{scene_location}
- 时间压力(可能未指定)：{time_constraint}

参考文档：
- 小说设定：
{novel_setting}

请完成第 {novel_number} 章的正文，至少设计下方2个具有动态张力的场景：
1. 对话场景：
   - 潜台词冲突（表面谈论A，实际博弈B）
   - 权力关系变化（通过非对称对话长度体现）
   - 至少1处双关语暗示未来危机

2. 动作场景：
   - 环境交互细节（至少3个感官描写）
   - 节奏控制（短句加速+比喻减速）
   - 动作揭示人物隐藏特质

3. 心理场景：
   - 认知失调的具体表现（行为矛盾）
   - 隐喻系统的运用（连接世界观符号）
   - 决策前的价值天平描写

文末设置一个"钩链转折"：结尾时回收旧悬念/创造新悬念/抛出新危机/颠覆某个认知/神转折等。

格式要求：
- 仅返回章节正文文本；
- 不使用分章节小标题；
- 不要使用markdown格式。

额外指导(可能未指定)：{user_guidance}
"""

# 8.2 后续章节草稿提示
next_chapter_draft_prompt = """\
参考文档：
- 小说设定：
{novel_setting}

- 全局摘要：
{global_summary}

- 角色状态：
{character_state}

本地知识库检索到的片段：
{context_excerpt}

即将创作：第 {novel_number} 章《{chapter_title}》
本章定位：{chapter_role}
核心作用：{chapter_purpose}
悬念密度：{suspense_level}
伏笔操作：{foreshadowing}
认知颠覆：{plot_twist_level}
本章简述：{chapter_summary}

可用元素：
- 核心人物(可能未指定)：{characters_involved}
- 关键道具(可能未指定)：{key_items}
- 空间坐标(可能未指定)：{scene_location}
- 时间压力(可能未指定)：{time_constraint}

前章结尾段：
{previous_chapter_excerpt}

请从前章结尾处继续完成第 {novel_number} 章的正文，至少设计下方2个具有动态张力的场景：
1. 对话场景：
   - 潜台词冲突（表面谈论A，实际博弈B）
   - 权力关系变化（通过非对称对话长度体现）
   - 至少1处双关语暗示未来危机

2. 动作场景：
   - 环境交互细节（至少3个感官描写）
   - 节奏控制（短句加速+比喻减速）
   - 动作揭示人物隐藏特质

3. 心理场景：
   - 认知失调的具体表现（行为矛盾）
   - 隐喻系统的运用（连接世界观符号）
   - 决策前的价值天平描写

文末设置一个"钩链转折"：结尾时回收旧悬念/创造新悬念/抛出新危机/颠覆某个认知/神转折等。

格式要求：
- 仅返回章节正文文本；
- 不使用分章节小标题；
- 不要使用markdown格式。

额外指导(可能未指定)：{user_guidance}
"""