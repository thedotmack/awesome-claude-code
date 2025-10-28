<!--lint disable remark-lint:awesome-badge-->

<!-- Responsive Logo with Theme Support -->
<div align="center">
  
  <!-- Same ASCII art for all screen sizes, just scales down on mobile -->
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/logo-dark.svg">
    <img src="assets/logo-light.svg" alt="Awesome Claude Code" width="100%" style="max-width: 900px;">
  </picture>
  
</div>


<!-- Generated with https://github.com/denvercoder1/readme-typing-svg -->

[![Typing SVG](https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&pause=1000&color=F7080D&random=true&width=435&lines=Fumigating...;Gallivanting...;Matriculating...;Toodleedoodling...;Goo-goo-g'joob-ing...;Excaliburating...;Canoodling...;Doing+the+humpty+dance...;Shiver-me-timbers-ing...;Becoming+sentient...;Opening+the+pod+bay+doors...;Rimraf-ing...;23-skidoo-ing...;Skip-to-my-loo'ing...;High-falutin'...;Disambiguating...;Coagulating...;Undulating...;Just+Clauding+around...)](https://git.io/typing-svg)

<!--lint enable remark-lint:awesome-badge-->

[![Awesome](https://awesome.re/badge-flat2.svg)](https://awesome.re)


# Awesome Claude Code

<!--lint enable remark-lint:awesome-badge-->

---

## 🚀 About This Fork: An Open Alternative

> **Everyone gets to play.**

This is a **community-driven fork** that implements **automatic approval** for all validated submissions. No gatekeeping, no waiting, no subjective rejections.

### Why This Fork Exists

After [extensive analysis](./GATEKEEPING_ANALYSIS.md), we identified systemic gatekeeping in the upstream repository: 7 validated submissions rejected based on subjective criteria, 14+ waiting 2-74+ days, and pay-to-play concerns.

### Our Philosophy

- **🎯 Validation = Approval** — If validation passes, you're automatically listed
- **⚡ Zero-Wait** — Target < 1 hour approval time
- **🤝 Community-Driven** — Users decide value, not maintainer opinion
- **🚫 No Pay-to-Play** — Donations never influence inclusion
- **📂 All Categories Welcome** — No discrimination against tools types
- **📋 Stable Requirements** — No moving goalposts

**[Learn more about our philosophy →](./FORK_README.md)** | **[See the analysis →](./GATEKEEPING_ANALYSIS.md)**

---

<!--lint disable double-link-->

This is a curated list of slash-commands, `CLAUDE.md` files, CLI tools, and other resources and guides for enhancing your [Claude Code](https://docs.anthropic.com/en/docs/claude-code) workflow, productivity, and vibes.

<!--lint enable double-link-->

Claude Code is a cutting-edge CLI-based coding assistant and agent released by [Anthropic](https://www.anthropic.com/) that you can access in your terminal or IDE. It is a rapidly evolving tool that offers a number of powerful capabilities, and allows for a lot of configuration, in a lot of different ways. Users are actively working out best practices and workflows. It is the hope that this repo will help the community share knowledge and understand how to get the most out of Claude Code.

## Contents [🔝](#awesome-claude-code)

<details open>
<summary>Table of Contents</summary>

- <details open>
  <summary><a href="#agent-skills-">Agent Skills</a></summary>

  - [General](#general-)

  </details>

- <details open>
  <summary><a href="#workflows--knowledge-guides-">Workflows & Knowledge Guides</a></summary>

  - [General](#general--1)

  </details>

- <details open>
  <summary><a href="#tooling-">Tooling</a></summary>

  - [General](#general--2)
  - [IDE Integrations](#ide-integrations-)
  - [Usage Monitors](#usage-monitors-)
  - [Orchestrators](#orchestrators-)

  </details>

- <details open>
  <summary><a href="#status-lines-">Status Lines</a></summary>

  - [General](#general--3)

  </details>

- <details open>
  <summary><a href="#hooks-">Hooks</a></summary>

  - [General](#general--4)

  </details>

- <details open>
  <summary><a href="#output-styles-">Output Styles</a></summary>

  - [General](#general--5)

  </details>

- <details open>
  <summary><a href="#slash-commands-">Slash-Commands</a></summary>

  - [General](#general--6)
  - [Version Control & Git](#version-control--git-)
  - [Code Analysis & Testing](#code-analysis--testing-)
  - [Context Loading & Priming](#context-loading--priming-)
  - [Documentation & Changelogs](#documentation--changelogs-)
  - [CI / Deployment](#ci--deployment-)
  - [Project & Task Management](#project--task-management-)
  - [Miscellaneous](#miscellaneous-)

  </details>

- <details open>
  <summary><a href="#claudemd-files-">CLAUDE.md Files</a></summary>

  - [General](#general--7)
  - [Language-Specific](#language-specific-)
  - [Domain-Specific](#domain-specific-)
  - [Project Scaffolding & MCP](#project-scaffolding--mcp-)

  </details>

- <details open>
  <summary><a href="#alternative-clients-">Alternative Clients</a></summary>


  </details>

- <details open>
  <summary><a href="#official-documentation-">Official Documentation</a></summary>

  - [General](#general--8)

  </details>

</details>

<br>

## Agent Skills 🤖 [🔝](#awesome-claude-code)

> **Agent skills** are model-controlled configurations (files, scripts, resources, etc.) that enable Claude Code to perform specialized tasks requiring specific knowledge or capabilities.

<details open>
<summary><h3>General <a href="#awesome-claude-code">🔝</a></h3></summary>

[`Codex Skill`](https://github.com/skills-directory/skill-codex) &nbsp; by &nbsp; [klaudworks](https://github.com/klaudworks)  &nbsp;&nbsp;⚖️&nbsp;&nbsp;MIT  
Enables users to prompt codex from claude code. Unlike the raw codex mcp server, this skill infers parameters such as model, reasoning effort, sandboxing from your prompt or asks you to specify them. It also simplifies continuing prior codex sessions so that codex can continue with the prior context.

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=skills-directory&repo=skill-codex&show_icons=true&hide_border=true&theme=default&card_width=400)](https://github.com/skills-directory/skill-codex)
<br>

[`Web Assets Generator`](https://github.com/alonw0/web-asset-generator) &nbsp; by &nbsp; [Alon Wolenitz](https://github.com/alonw0)  &nbsp;&nbsp;⚖️&nbsp;&nbsp;MIT  
Easily generate web assets from Claude Code including favicons, app icons (PWA), and social media meta images (Open Graph) for Facebook, Twitter, WhatsApp, and LinkedIn. Handles image resizing, text-to-image generation, emojis, and provides proper HTML meta tags.

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=alonw0&repo=web-asset-generator&show_icons=true&hide_border=true&theme=default&card_width=400)](https://github.com/alonw0/web-asset-generator)
<br>

</details>

<br>

## Workflows & Knowledge Guides 🧠 [🔝](#awesome-claude-code)

> A **workflow** is a tightly coupled set of Claude Code-native resources that facilitate specific projects

<details open>
<summary><h3>General <a href="#awesome-claude-code">🔝</a></h3></summary>

[`AB Method`](https://github.com/ayoubben18/ab-method) &nbsp; by &nbsp; [Ayoub Bensalah](https://github.com/ayoubben18)  &nbsp;&nbsp;⚖️&nbsp;&nbsp;MIT  
A principled, spec-driven workflow that transforms large problems into focused, incremental missions using Claude Code's specialized sub agents. Includes slash-commands, sub agents, and specialized workflows designed for specific parts of the SDLC.

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=ayoubben18&repo=ab-method&show_icons=true&hide_border=true&theme=default&card_width=400)](https://github.com/ayoubben18/ab-method)
<br>

[`Blogging Platform Instructions`](https://github.com/cloudartisan/cloudartisan.github.io/tree/main/.claude/commands) &nbsp; by &nbsp; [cloudartisan](https://github.com/cloudartisan)  &nbsp;&nbsp;⚖️&nbsp;&nbsp;CC-BY-SA-4.0  
Provides a well-structured set of commands for publishing and maintaining a blogging platform, including commands for creating posts, managing categories, and handling media files.

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=cloudartisan&repo=cloudartisan.github.io&show_icons=true&hide_border=true&theme=default&card_width=400)](https://github.com/cloudartisan/cloudartisan.github.io)
<br>

[`Claude Code PM`](https://github.com/automazeio/ccpm) &nbsp; by &nbsp; [Ran Aroussi](https://github.com/ranaroussi)  &nbsp;&nbsp;⚖️&nbsp;&nbsp;MIT  
Really comprehensive and feature-packed project-management workflow for Claude Code. Numerous specialized agents, slash-commands, and strong documentation.

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=automazeio&repo=ccpm&show_icons=true&hide_border=true&theme=default&card_width=400)](https://github.com/automazeio/ccpm)
<br>

[`ClaudeLog`](https://claudelog.com) &nbsp; by &nbsp; [InventorBlack](https://www.reddit.com/user/inventor_black/)    
A comprehensive knowledge base with detailed breakdowns of advanced [mechanics](https://claudelog.com/mechanics/you-are-the-main-thread/) including [CLAUDE.md best practices](https://claudelog.com/mechanics/claude-md-supremacy), practical technique guides like [plan mode](https://claudelog.com/mechanics/plan-mode), [ultrathink](https://claudelog.com/faqs/what-is-ultrathink/), [sub-agents](https://claudelog.com/mechanics/task-agent-tools/), [agent-first design](https://claudelog.com/mechanics/agent-first-design/) and [configuration guides](https://claudelog.com/configuration).

[`ClaudoPro Directory`](https://github.com/JSONbored/claudepro-directory) &nbsp; by &nbsp; [ghost](https://github.com/JSONbored)  &nbsp;&nbsp;⚖️&nbsp;&nbsp;MIT  
Well-crafted, wide selection of Claude Code hooks, slash commands, subagent files, and more, covering a range of specialized tasks and workflows. Better resources than your average "Claude-template-for-everything" site.

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=JSONbored&repo=claudepro-directory&show_icons=true&hide_border=true&theme=default&card_width=400)](https://github.com/JSONbored/claudepro-directory)
<br>

[`Context Priming`](https://github.com/disler/just-prompt/tree/main/.claude/commands) &nbsp; by &nbsp; [disler](https://github.com/disler)    
Provides a systematic approach to priming Claude Code with comprehensive project context through specialized commands for different project scenarios and development contexts.

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=disler&repo=just-prompt&show_icons=true&hide_border=true&theme=default&card_width=400)](https://github.com/disler/just-prompt)
<br>

[`Design Review Workflow`](https://github.com/OneRedOak/claude-code-workflows/tree/main/design-review) &nbsp; by &nbsp; [Patrick Ellis](https://github.com/OneRedOak)  &nbsp;&nbsp;⚖️&nbsp;&nbsp;MIT  
A tailored workflow for enabling automated UI/UX design review, including specialized sub agents, slash commands, `CLAUDE.md` excerpts, and more. Covers a broad range of criteria from responsive design to accessibility.

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=OneRedOak&repo=claude-code-workflows&show_icons=true&hide_border=true&theme=default&card_width=400)](https://github.com/OneRedOak/claude-code-workflows)
<br>

[`Laravel TALL Stack AI Development Starter Kit`](https://github.com/tott/laravel-tall-claude-ai-configs) &nbsp; by &nbsp; [tott](https://github.com/tott)  &nbsp;&nbsp;⚖️&nbsp;&nbsp;MIT  
Transform your Laravel TALL (Tailwind, AlpineJS, Laravel, Livewire) stack development with comprehensive Claude Code configurations that provide intelligent assistance, systematic workflows, and domain expert consultation.

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=tott&repo=laravel-tall-claude-ai-configs&show_icons=true&hide_border=true&theme=default&card_width=400)](https://github.com/tott/laravel-tall-claude-ai-configs)
<br>

[`n8n_agent`](https://github.com/kingler/n8n_agent/tree/main/.claude/commands) &nbsp; by &nbsp; [kingler](https://github.com/kingler)    
Amazing comprehensive set of comments for code analysis, QA, design, documentation, project structure, project management, optimization, and many more.

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=kingler&repo=n8n_agent&show_icons=true&hide_border=true&theme=default&card_width=400)](https://github.com/kingler/n8n_agent)
<br>

[`Project Bootstrapping and Task Management`](https://github.com/steadycursor/steadystart/tree/main/.claude/commands) &nbsp; by &nbsp; [steadycursor](https://github.com/steadycursor)    
Provides a structured set of commands for bootstrapping and managing a new project, including meta-commands for creating and editing custom slash-commands.

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=steadycursor&repo=steadystart&show_icons=true&hide_border=true&theme=default&card_width=400)](https://github.com/steadycursor/steadystart)
<br>

[`Project Management, Implementation, Planning, and Release`](https://github.com/scopecraft/command/tree/main/.claude/commands) &nbsp; by &nbsp; [scopecraft](https://github.com/scopecraft)    
Really comprehensive set of commands for all aspects of SDLC.

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=scopecraft&repo=command&show_icons=true&hide_border=true&theme=default&card_width=400)](https://github.com/scopecraft/command)
<br>

[`Project Workflow System`](https://github.com/harperreed/dotfiles/tree/master/.claude/commands) &nbsp; by &nbsp; [harperreed](https://github.com/harperreed)    
A set of commands that provide a comprehensive workflow system for managing projects, including task management, code review, and deployment processes.

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=harperreed&repo=dotfiles&show_icons=true&hide_border=true&theme=default&card_width=400)](https://github.com/harperreed/dotfiles)
<br>

[`RIPER Workflow`](https://github.com/tony/claude-code-riper-5) &nbsp; by &nbsp; [Tony Narlock](https://tony.sh)  &nbsp;&nbsp;⚖️&nbsp;&nbsp;MIT  
Structured development workflow enforcing separation between Research, Innovate, Plan, Execute, and Review phases. Features consolidated subagents for context-efficiency, branch-aware memory bank, and strict mode enforcement for guided development.

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=tony&repo=claude-code-riper-5&show_icons=true&hide_border=true&theme=default&card_width=400)](https://github.com/tony/claude-code-riper-5)
<br>

[`Shipping Real Code w/ Claude`](https://diwank.space/field-notes-from-shipping-real-code-with-claude) &nbsp; by &nbsp; [Diwank](https://github.com/creatorrr)    
A detailed blog post explaining the author's process for shipping a product with Claude Code, including CLAUDE.md files and other interesting resources.

[`Simone`](https://github.com/Helmi/claude-simone) &nbsp; by &nbsp; [Helmi](https://github.com/Helmi)  &nbsp;&nbsp;⚖️&nbsp;&nbsp;MIT  
A broader project management workflow for Claude Code that encompasses not just a set of commands, but a system of documents, guidelines, and processes to facilitate project planning and execution.

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=Helmi&repo=claude-simone&show_icons=true&hide_border=true&theme=default&card_width=400)](https://github.com/Helmi/claude-simone)
<br>

[`Claude Code Cheat Sheet`](https://github.com/aeulker/Claude-Code-Cheat-Sheet) &nbsp; by &nbsp; [aeulker](https://github.com/aeulker)  &nbsp;&nbsp;⚖️&nbsp;&nbsp;MIT  
Claude Code Cheat Sheet - A comprehensive reference guide for Claude Code workflows and best practices.

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=aeulker&repo=Claude-Code-Cheat-Sheet&show_icons=true&hide_border=true&theme=default&card_width=400)](https://github.com/aeulker/Claude-Code-Cheat-Sheet)
<br>

[`Claude Code Handbook`](https://nikiforovall.blog/claude-code-rules/) &nbsp; by &nbsp; [nikiforovall](https://github.com/NikiforovAll)  &nbsp;&nbsp;⚖️&nbsp;&nbsp;MIT  
Collection of best practices, tips, and techniques for Claude Code development workflows, enhanced with distributable plugins. Covers practical technique guides for beginners and advanced users.

</details>

<br>

## Tooling 🧰 [🔝](#awesome-claude-code)

> **Tooling** denotes applications that are built on top of Claude Code and consist of more components than slash-commands and `CLAUDE.md` files

<details open>
<summary><h3>General <a href="#awesome-claude-code">🔝</a></h3></summary>

[`cc-sessions`](https://github.com/GWUDCAP/cc-sessions) &nbsp; by &nbsp; [toastdev](https://github.com/satoastshi)  &nbsp;&nbsp;⚖️&nbsp;&nbsp;MIT  
An opinionated approach to produce development with Claude Code

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=GWUDCAP&repo=cc-sessions&show_icons=true&hide_border=true&theme=default&card_width=400)](https://github.com/GWUDCAP/cc-sessions)
<br>

[`cc-tools`](https://github.com/Veraticus/cc-tools) &nbsp; by &nbsp; [Josh Symonds](https://github.com/Veraticus)    
High-performance Go implementation of Claude Code hooks and utilities. Provides smart linting, testing, and statusline generation with minimal overhead.

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=Veraticus&repo=cc-tools&show_icons=true&hide_border=true&theme=default&card_width=400)](https://github.com/Veraticus/cc-tools)
<br>

[`ccexp`](https://github.com/nyatinte/ccexp) &nbsp; by &nbsp; [nyatinte](https://github.com/nyatinte)  &nbsp;&nbsp;⚖️&nbsp;&nbsp;MIT  
Interactive CLI tool for discovering and managing Claude Code configuration files and slash commands with a beautiful terminal UI.

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=nyatinte&repo=ccexp&show_icons=true&hide_border=true&theme=default&card_width=400)](https://github.com/nyatinte/ccexp)
<br>

[`cchistory`](https://github.com/eckardt/cchistory) &nbsp; by &nbsp; [eckardt](https://github.com/eckardt)  &nbsp;&nbsp;⚖️&nbsp;&nbsp;MIT  
Like the shell history command but for your Claude Code sessions. Easily list all Bash or "Bash-mode" (`!`) commands Claude Code ran in a session for reference.

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=eckardt&repo=cchistory&show_icons=true&hide_border=true&theme=default&card_width=400)](https://github.com/eckardt/cchistory)
<br>

[`cclogviewer`](https://github.com/Brads3290/cclogviewer) &nbsp; by &nbsp; [Brad S.](https://github.com/Brads3290)  &nbsp;&nbsp;⚖️&nbsp;&nbsp;MIT  
A humble but handy utility for viewing Claude Code `.jsonl` conversation files in a pretty HTML UI.

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=Brads3290&repo=cclogviewer&show_icons=true&hide_border=true&theme=default&card_width=400)](https://github.com/Brads3290/cclogviewer)
<br>

[`Claude Code Templates`](https://github.com/davila7/claude-code-templates) &nbsp; by &nbsp; [Daniel Avila](https://github.com/davila7)  &nbsp;&nbsp;⚖️&nbsp;&nbsp;MIT  
Incredibly awesome collection of resources from every category in this list, presented with a neatly polished UI, great features like usage dashboard, analytics, and everything from slash commands to hooks to agents. An awesome companion for this awesome list.

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=davila7&repo=claude-code-templates&show_icons=true&hide_border=true&theme=default&card_width=400)](https://github.com/davila7/claude-code-templates)
<br>

[`Claude Composer`](https://github.com/possibilities/claude-composer) &nbsp; by &nbsp; [Mike Bannister](https://github.com/possibilities)  &nbsp;&nbsp;⚖️&nbsp;&nbsp;Unlicense  
A tool that adds small enhancements to Claude Code.

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=possibilities&repo=claude-composer&show_icons=true&hide_border=true&theme=default&card_width=400)](https://github.com/possibilities/claude-composer)
<br>

[`Claude Hub`](https://github.com/claude-did-this/claude-hub) &nbsp; by &nbsp; [Claude Did This](https://github.com/claude-did-this)    
A webhook service that connects Claude Code to GitHub repositories, enabling AI-powered code assistance directly through pull requests and issues. This integration allows Claude to analyze repositories, answer technical questions, and help developers understand and improve their codebase through simple @mentions.

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=claude-did-this&repo=claude-hub&show_icons=true&hide_border=true&theme=default&card_width=400)](https://github.com/claude-did-this/claude-hub)
<br>

[`claude-code-tools`](https://github.com/pchalasani/claude-code-tools) &nbsp; by &nbsp; [Prasad Chalasani](https://github.com/pchalasani)  &nbsp;&nbsp;⚖️&nbsp;&nbsp;MIT  
A collection of awesome tools, including tmux integrations, better session management, hooks that enhance security - a really well-done set of Claude Code enhancers, especially for tmux users.

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=pchalasani&repo=claude-code-tools&show_icons=true&hide_border=true&theme=default&card_width=400)](https://github.com/pchalasani/claude-code-tools)
<br>

[`claudekit`](https://github.com/carlrannaberg/claudekit) &nbsp; by &nbsp; [Carl Rannaberg](https://github.com/carlrannaberg)  &nbsp;&nbsp;⚖️&nbsp;&nbsp;MIT  
Impressive CLI toolkit providing auto-save checkpointing, code quality hooks, specification generation and execution, and 20+ specialized subagents including oracle (gpt-5), code-reviewer (6-aspect deep analysis), ai-sdk-expert (Vercel AI SDK), typescript-expert and many more for Claude Code workflows.

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=carlrannaberg&repo=claudekit&show_icons=true&hide_border=true&theme=default&card_width=400)](https://github.com/carlrannaberg/claudekit)
<br>

[`Container Use`](https://github.com/dagger/container-use) &nbsp; by &nbsp; [dagger](https://github.com/dagger)  &nbsp;&nbsp;⚖️&nbsp;&nbsp;Apache-2.0  
Development environments for coding agents. Enable multiple agents to work safely and independently with your preferred stack.

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=dagger&repo=container-use&show_icons=true&hide_border=true&theme=default&card_width=400)](https://github.com/dagger/container-use)
<br>

[`ContextKit`](https://github.com/FlineDev/ContextKit) &nbsp; by &nbsp; [Cihat Gündüz](https://github.com/Jeehut)  &nbsp;&nbsp;⚖️&nbsp;&nbsp;MIT  
A systematic development framework that transforms Claude Code into a proactive development partner. Features 4-phase planning methodology, specialized quality agents, and structured workflows that help AI produce production-ready code on first try.

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=FlineDev&repo=ContextKit&show_icons=true&hide_border=true&theme=default&card_width=400)](https://github.com/FlineDev/ContextKit)
<br>

[`Rulesync`](https://github.com/dyoshikawa/rulesync) &nbsp; by &nbsp; [dyoshikawa](https://github.com/dyoshikawa)  &nbsp;&nbsp;⚖️&nbsp;&nbsp;MIT  
A Node.js CLI tool that automatically generates configs (rules, ignore files, MCP servers, commands, and subagents) for various AI coding agents. Rulesync can convert configs between Claude Code and other AI agents in both directions.

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=dyoshikawa&repo=rulesync&show_icons=true&hide_border=true&theme=default&card_width=400)](https://github.com/dyoshikawa/rulesync)
<br>

[`run-claude-docker`](https://github.com/icanhasjonas/run-claude-docker) &nbsp; by &nbsp; [Jonas](https://github.com/icanhasjonas/)  &nbsp;&nbsp;⚖️&nbsp;&nbsp;MIT  
A self-contained Docker runner that forwards your current workspace into a safe(r) isolated docker container, where you still have access to your Claude Code settings, authentication, ssh agent, pgp, optionally aws keys etc.

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=icanhasjonas&repo=run-claude-docker&show_icons=true&hide_border=true&theme=default&card_width=400)](https://github.com/icanhasjonas/run-claude-docker)
<br>

[`stt-mcp-server-linux`](https://github.com/marcindulak/stt-mcp-server-linux) &nbsp; by &nbsp; [marcindulak](https://github.com/marcindulak)  &nbsp;&nbsp;⚖️&nbsp;&nbsp;Apache-2.0  
A push-to-talk speech transcription setup for Linux using a Python MCP server. Runs locally in Docker with no external API calls. Your speech is recorded, transcribed into text, and then sent to Claude running in a Tmux session.

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=marcindulak&repo=stt-mcp-server-linux&show_icons=true&hide_border=true&theme=default&card_width=400)](https://github.com/marcindulak/stt-mcp-server-linux)
<br>

[`SuperClaude`](https://github.com/SuperClaude-Org/SuperClaude_Framework) &nbsp; by &nbsp; [SuperClaude-Org](https://github.com/SuperClaude-Org)  &nbsp;&nbsp;⚖️&nbsp;&nbsp;MIT  
A versatile configuration framework that enhances Claude Code with specialized commands, cognitive personas, and development methodologies, such as "Introspection" and "Orchestration".

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=SuperClaude-Org&repo=SuperClaude_Framework&show_icons=true&hide_border=true&theme=default&card_width=400)](https://github.com/SuperClaude-Org/SuperClaude_Framework)
<br>

[`tweakcc`](https://github.com/Piebald-AI/tweakcc) &nbsp; by &nbsp; [Piebald-AI](https://github.com/Piebald-AI)  &nbsp;&nbsp;⚖️&nbsp;&nbsp;MIT  
Command-line tool to customize your Claude Code styling.

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=Piebald-AI&repo=tweakcc&show_icons=true&hide_border=true&theme=default&card_width=400)](https://github.com/Piebald-AI/tweakcc)
<br>

[`Vibe-Log`](https://github.com/vibe-log/vibe-log-cli) &nbsp; by &nbsp; [Vibe-Log](https://github.com/vibe-log)  &nbsp;&nbsp;⚖️&nbsp;&nbsp;MIT  
Analyzes your Claude Code prompts locally (using CC), provides intelligent session analysis and actionable strategic guidance - works in the statusline and produces very pretty HTML reports as well. Easy to install and remove.

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=vibe-log&repo=vibe-log-cli&show_icons=true&hide_border=true&theme=default&card_width=400)](https://github.com/vibe-log/vibe-log-cli)
<br>

[`VoiceMode MCP`](https://github.com/mbailey/voicemode) &nbsp; by &nbsp; [Mike Bailey](https://github.com/mbailey)  &nbsp;&nbsp;⚖️&nbsp;&nbsp;MIT  
VoiceMode MCP brings natural conversations to Claude Code. It supports any OpenAI API compatible voice services and installs free and open source voice services (Whisper.cpp and Kokoro-FastAPI).

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=mbailey&repo=voicemode&show_icons=true&hide_border=true&theme=default&card_width=400)](https://github.com/mbailey/voicemode)
<br>

[`Claude Control Terminal`](https://github.com/schlunsen/claude-control-terminal) &nbsp; by &nbsp; [schlunsen](https://github.com/schlunsen)  &nbsp;&nbsp;⚖️&nbsp;&nbsp;MIT  
High-performance Go port of claude-code-templates providing component installation (600+ agents, 200+ commands, MCPs), Docker containerization, real-time analytics dashboard with WebSocket monitoring, and cross-platform deployment. Features 10-50x faster startup and 3-5x lower memory usage compared to Node.js alternatives.

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=schlunsen&repo=claude-control-terminal&show_icons=true&hide_border=true&theme=default&card_width=400)](https://github.com/schlunsen/claude-control-terminal)
<br>

[`Schaltwerk`](https://github.com/2mawi2/schaltwerk) &nbsp; by &nbsp; [Marius Wichtner](https://github.com/2mawi2)  &nbsp;&nbsp;⚖️&nbsp;&nbsp;MIT  
Schaltwerk is a macOS Tauri desktop app that runs multiple terminal agents (Claude, Codex, OpenCode, Gemini-CLI) in parallel. Each session is isolated in its own git worktree/branch and includes a driving spec plus multiple terminals for running and testing. The keyboard-first, spec-driven workflow and local diff review keep humans in control.

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=2mawi2&repo=schaltwerk&show_icons=true&hide_border=true&theme=default&card_width=400)](https://github.com/2mawi2/schaltwerk)
<br>

[`Claude Code Web Shell`](https://github.com/vaderyang/claudecode_web_shell) &nbsp; by &nbsp; [vaderyang](https://github.com/vaderyang)  &nbsp;&nbsp;⚖️&nbsp;&nbsp;MIT  
A web-based terminal interface for Claude Code that allows you to interact with Claude Code through your browser.

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=vaderyang&repo=claudecode_web_shell&show_icons=true&hide_border=true&theme=default&card_width=400)](https://github.com/vaderyang/claudecode_web_shell)
<br>

[`Codanna`](https://github.com/bartolli/codanna) &nbsp; by &nbsp; [bartolli](https://github.com/bartolli)  &nbsp;&nbsp;⚖️&nbsp;&nbsp;Apache-2.0  
Semantic code search and relationship tracking via MCP and Unix CLI. Features 91,318 symbols/sec parsing, Tree-sitter AST parsing for Rust and Python, 384-dimensional vectors, Tantivy full-text search, <10ms lookups, ~300ms MCP response time. FNV-1a hashed lookups with memory-mapped storage and specialized caches.

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=bartolli&repo=codanna&show_icons=true&hide_border=true&theme=default&card_width=400)](https://github.com/bartolli/codanna)
<br>

[`Claudable`](https://github.com/opactorai/Claudable) &nbsp; by &nbsp; [Ethan Park](https://github.com/Atipico1)  &nbsp;&nbsp;⚖️&nbsp;&nbsp;MIT  
Claudable is an open-source web builder that leverages local CLI agents, such as Claude Code and Cursor Agent, to build and deploy products effortlessly. OpenSource Lovable that runs locally.

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=opactorai&repo=Claudable&show_icons=true&hide_border=true&theme=default&card_width=400)](https://github.com/opactorai/Claudable)
<br>

[`Claude Agent Toolkit`](https://github.com/cheolwanpark/claude-agent-toolkit) &nbsp; by &nbsp; [Cheolwan Park](https://github.com/cheolwanpark)  &nbsp;&nbsp;⚖️&nbsp;&nbsp;MIT  
A Python framework that wraps claude-code-sdk to provide better developer experience through decorator-based tools, runtime isolation, and simplified agent development. Built for production safety with Docker containers. Features simple class-based definition with @tool decorator, built-in parallel execution, and FileSystemTool with permission control.

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=cheolwanpark&repo=claude-agent-toolkit&show_icons=true&hide_border=true&theme=default&card_width=400)](https://github.com/cheolwanpark/claude-agent-toolkit)
<br>

[`Omnara`](https://github.com/omnara-ai/omnara) &nbsp; by &nbsp; [Ishaan Sehgal](https://github.com/ishaansehgal99)  &nbsp;&nbsp;⚖️&nbsp;&nbsp;Apache-2.0  
A command center for AI agents that syncs Claude Code sessions across terminal, web, and mobile. Allows for remote monitoring, human-in-the-loop interaction, and team collaboration. Recently open-sourced web and mobile applications.

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=omnara-ai&repo=omnara&show_icons=true&hide_border=true&theme=default&card_width=400)](https://github.com/omnara-ai/omnara)
<br>

[`conduit8`](https://github.com/conduit8/conduit8) &nbsp; by &nbsp; [Alexander Zuev](https://github.com/alexander-zuev)  &nbsp;&nbsp;⚖️&nbsp;&nbsp;AGPL-3.0  
CLI registry for discovering, installing, and managing Claude Code skills. Search 20+ curated skills by keyword or category, install directly to ~/.claude/skills/ with one command. Like context7 for Claude Code skills. Available via npx - no global installation required.

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=conduit8&repo=conduit8&show_icons=true&hide_border=true&theme=default&card_width=400)](https://github.com/conduit8/conduit8)
<br>

[`Claw Code`](https://github.com/jamesrochabrun/Claw) &nbsp; by &nbsp; [James Rochabrun](https://github.com/jamesrochabrun)  &nbsp;&nbsp;⚖️&nbsp;&nbsp;MIT  
A friendly macOS app for Claude Code. Uses Claude Code SDK to bring most of the well known features from Claude Code to a macOS app. In addition uses accessibility API to inspect Xcode workspaces making it a great tool for iOS engineers.

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=jamesrochabrun&repo=Claw&show_icons=true&hide_border=true&theme=default&card_width=400)](https://github.com/jamesrochabrun/Claw)
<br>

[`Claude Codex Api`](https://github.com/4xian/claude-codex-api) &nbsp; by &nbsp; [4xian](https://github.com/4xian)  &nbsp;&nbsp;⚖️&nbsp;&nbsp;MIT  
A CLI tool for managing Claude Code and Codex configurations, allowing one-click switching between multiple transit station API configurations; One-click switching of system environment variables, one-click testing of API latency/validity, automatic optimal route switching with internationalization support.

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=4xian&repo=claude-codex-api&show_icons=true&hide_border=true&theme=default&card_width=400)](https://github.com/4xian/claude-codex-api)
<br>

[`DevRag`](https://github.com/tomohiro-owada/devrag) &nbsp; by &nbsp; [Tomohiro Owada](https://github.com/tomohiro-owada)  &nbsp;&nbsp;⚖️&nbsp;&nbsp;MIT  
Lightweight local RAG system for Claude Code that uses vector search to retrieve only relevant document chunks, reducing token usage by 40x and search time by 15x compared to reading entire files.

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=tomohiro-owada&repo=devrag&show_icons=true&hide_border=true&theme=default&card_width=400)](https://github.com/tomohiro-owada/devrag)
<br>

[`Claude Code Agent SDK Pretty Printer`](https://github.com/PepijnSenders/claude-pretty-printer) &nbsp; by &nbsp; [PepijnSenders](https://github.com/PepijnSenders)  &nbsp;&nbsp;⚖️&nbsp;&nbsp;MIT  
A lightweight utility that transforms raw Claude Agent SDK JSON messages into beautiful, readable CLI output with color-coded boxes and professional formatting.

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=PepijnSenders&repo=claude-pretty-printer&show_icons=true&hide_border=true&theme=default&card_width=400)](https://github.com/PepijnSenders/claude-pretty-printer)
<br>

</details>

<details open>
<summary><h3>IDE Integrations <a href="#awesome-claude-code">🔝</a></h3></summary>

[`Claude Code Chat`](https://marketplace.visualstudio.com/items?itemName=AndrePimenta.claude-code-chat) &nbsp; by &nbsp; [andrepimenta](https://github.com/andrepimenta)  &nbsp;&nbsp;⚖️&nbsp;&nbsp;&copy;  
An elegant and user-friendly Claude Code chat interface for VS Code.

[`claude-code-ide.el`](https://github.com/manzaltu/claude-code-ide.el) &nbsp; by &nbsp; [manzaltu](https://github.com/manzaltu)  &nbsp;&nbsp;⚖️&nbsp;&nbsp;GPL-3.0  
claude-code-ide.el integrates Claude Code with Emacs, like Anthropic’s VS Code/IntelliJ extensions. It shows ediff-based code suggestions, pulls LSP/flymake/flycheck diagnostics, and tracks buffer context. It adds an extensible MCP tool support for symbol refs/defs, project metadata, and tree-sitter AST queries.

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=manzaltu&repo=claude-code-ide.el&show_icons=true&hide_border=true&theme=default&card_width=400)](https://github.com/manzaltu/claude-code-ide.el)
<br>

[`claude-code.el`](https://github.com/stevemolitor/claude-code.el) &nbsp; by &nbsp; [stevemolitor](https://github.com/stevemolitor)  &nbsp;&nbsp;⚖️&nbsp;&nbsp;Apache-2.0  
An Emacs interface for Claude Code CLI.

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=stevemolitor&repo=claude-code.el&show_icons=true&hide_border=true&theme=default&card_width=400)](https://github.com/stevemolitor/claude-code.el)
<br>

[`claude-code.nvim`](https://github.com/greggh/claude-code.nvim) &nbsp; by &nbsp; [greggh](https://github.com/greggh)  &nbsp;&nbsp;⚖️&nbsp;&nbsp;MIT  
A seamless integration between Claude Code AI assistant and Neovim.

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=greggh&repo=claude-code.nvim&show_icons=true&hide_border=true&theme=default&card_width=400)](https://github.com/greggh/claude-code.nvim)
<br>

[`crystal`](https://github.com/stravu/crystal) &nbsp; by &nbsp; [stravu](https://github.com/stravu)  &nbsp;&nbsp;⚖️&nbsp;&nbsp;MIT  
A full-fledged desktop application for orchestrating, monitoring, and interacting with Claude Code agents.

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=stravu&repo=crystal&show_icons=true&hide_border=true&theme=default&card_width=400)](https://github.com/stravu/crystal)
<br>

</details>

<details open>
<summary><h3>Usage Monitors <a href="#awesome-claude-code">🔝</a></h3></summary>

[`CC Usage`](https://github.com/ryoppippi/ccusage) &nbsp; by &nbsp; [ryoppippi](https://github.com/ryoppippi)  &nbsp;&nbsp;⚖️&nbsp;&nbsp;NOASSERTION  
Handy CLI tool for managing and analyzing Claude Code usage, based on analyzing local Claude Code logs. Presents a nice dashboard regarding cost information, token consumption, etc.

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=ryoppippi&repo=ccusage&show_icons=true&hide_border=true&theme=default&card_width=400)](https://github.com/ryoppippi/ccusage)
<br>

[`ccflare`](https://github.com/snipeship/ccflare) &nbsp; by &nbsp; [snipeship](https://github.com/snipeship)  &nbsp;&nbsp;⚖️&nbsp;&nbsp;MIT  
Claude Code usage dashboard with a web-UI that would put Tableau to shame. Thoroughly comprehensive metrics, frictionless setup, detailed logging, really really nice UI.

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=snipeship&repo=ccflare&show_icons=true&hide_border=true&theme=default&card_width=400)](https://github.com/snipeship/ccflare)
<br>

[`Claude Code Usage Monitor`](https://github.com/Maciek-roboblog/Claude-Code-Usage-Monitor) &nbsp; by &nbsp; [Maciek-roboblog](https://github.com/Maciek-roboblog)  &nbsp;&nbsp;⚖️&nbsp;&nbsp;MIT  
A real-time terminal-based tool for monitoring Claude Code token usage. It shows live token consumption, burn rate, and predictions for token depletion. Features include visual progress bars, session-aware analytics, and support for multiple subscription plans.

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=Maciek-roboblog&repo=Claude-Code-Usage-Monitor&show_icons=true&hide_border=true&theme=default&card_width=400)](https://github.com/Maciek-roboblog/Claude-Code-Usage-Monitor)
<br>

[`viberank`](https://github.com/sculptdotfun/viberank) &nbsp; by &nbsp; [nikshepsvn](https://github.com/nikshepsvn)  &nbsp;&nbsp;⚖️&nbsp;&nbsp;MIT  
A community-driven leaderboard tool that enables developers to visualize, track, and compete based on their Claude Code usage statistics. It features robust data analytics, GitHub OAuth, data validation, and user-friendly CLI/web submission methods.

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=sculptdotfun&repo=viberank&show_icons=true&hide_border=true&theme=default&card_width=400)](https://github.com/sculptdotfun/viberank)
<br>

</details>

<details open>
<summary><h3>Orchestrators <a href="#awesome-claude-code">🔝</a></h3></summary>

[`Claude Code Flow`](https://github.com/ruvnet/claude-code-flow) &nbsp; by &nbsp; [ruvnet](https://github.com/ruvnet)  &nbsp;&nbsp;⚖️&nbsp;&nbsp;MIT  
This mode serves as a code-first orchestration layer, enabling Claude to write, edit, test, and optimize code autonomously across recursive agent cycles.

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=ruvnet&repo=claude-code-flow&show_icons=true&hide_border=true&theme=default&card_width=400)](https://github.com/ruvnet/claude-code-flow)
<br>

[`Claude Squad`](https://github.com/smtg-ai/claude-squad) &nbsp; by &nbsp; [smtg-ai](https://github.com/smtg-ai)  &nbsp;&nbsp;⚖️&nbsp;&nbsp;AGPL-3.0  
Claude Squad is a terminal app that manages multiple Claude Code, Codex (and other local agents including Aider) in separate workspaces, allowing you to work on multiple tasks simultaneously.

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=smtg-ai&repo=claude-squad&show_icons=true&hide_border=true&theme=default&card_width=400)](https://github.com/smtg-ai/claude-squad)
<br>

[`Claude Swarm`](https://github.com/parruda/claude-swarm) &nbsp; by &nbsp; [parruda](https://github.com/parruda)  &nbsp;&nbsp;⚖️&nbsp;&nbsp;MIT  
Launch Claude Code session that is connected to a swarm of Claude Code Agents.

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=parruda&repo=claude-swarm&show_icons=true&hide_border=true&theme=default&card_width=400)](https://github.com/parruda/claude-swarm)
<br>

[`Claude Task Master`](https://github.com/eyaltoledano/claude-task-master) &nbsp; by &nbsp; [eyaltoledano](https://github.com/eyaltoledano)  &nbsp;&nbsp;⚖️&nbsp;&nbsp;NOASSERTION  
A task management system for AI-driven development with Claude, designed to work seamlessly with Cursor AI.

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=eyaltoledano&repo=claude-task-master&show_icons=true&hide_border=true&theme=default&card_width=400)](https://github.com/eyaltoledano/claude-task-master)
<br>

[`Claude Task Runner`](https://github.com/grahama1970/claude-task-runner) &nbsp; by &nbsp; [grahama1970](https://github.com/grahama1970)    
A specialized tool to manage context isolation and focused task execution with Claude Code, solving the critical challenge of context length limitations and task focus when working with Claude on complex, multi-step projects.

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=grahama1970&repo=claude-task-runner&show_icons=true&hide_border=true&theme=default&card_width=400)](https://github.com/grahama1970/claude-task-runner)
<br>

[`Happy Coder`](https://github.com/slopus/happy) &nbsp; by &nbsp; [GrocerPublishAgent](https://peoplesgrocers.com/en/projects)  &nbsp;&nbsp;⚖️&nbsp;&nbsp;MIT  
Spawn and control multiple Claude Codes in parallel from your phone or desktop. Happy Coder runs Claude Code on your hardware, sends push notifications when Claude needs more input or permission, and costs nothing.

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=slopus&repo=happy&show_icons=true&hide_border=true&theme=default&card_width=400)](https://github.com/slopus/happy)
<br>

[`The Agentic Startup`](https://github.com/rsmdt/the-startup) &nbsp; by &nbsp; [Rudolf Schmidt](https://github.com/rsmdt)  &nbsp;&nbsp;⚖️&nbsp;&nbsp;MIT  
Yet Another Claude Orchestrator - a collection of agents, commands, etc., for shipping production code - but I like this because it's comprehensive, well-written, and one of the few resources that actually uses Output Styles! +10 points!

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=rsmdt&repo=the-startup&show_icons=true&hide_border=true&theme=default&card_width=400)](https://github.com/rsmdt/the-startup)
<br>

[`TSK - AI Agent Task Manager and Sandbox`](https://github.com/dtormoen/tsk) &nbsp; by &nbsp; [dtormoen](https://github.com/dtormoen)  &nbsp;&nbsp;⚖️&nbsp;&nbsp;MIT  
A Rust CLI tool that lets you delegate development tasks to AI agents running in sandboxed Docker environments. Multiple agents work in parallel, returning git branches for human review.

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=dtormoen&repo=tsk&show_icons=true&hide_border=true&theme=default&card_width=400)](https://github.com/dtormoen/tsk)
<br>

</details>

<br>

## Status Lines 📊 [🔝](#awesome-claude-code)

> **Status lines** - Configurations and customizations for Claude Code's status bar functionality

<details open>
<summary><h3>General <a href="#awesome-claude-code">🔝</a></h3></summary>

[`ccstatusline`](https://github.com/sirmalloc/ccstatusline) &nbsp; by &nbsp; [sirmalloc](https://github.com/sirmalloc)  &nbsp;&nbsp;⚖️&nbsp;&nbsp;MIT  
A highly customizable status line formatter for Claude Code CLI that displays model info, git branch, token usage, and other metrics in your terminal.

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=sirmalloc&repo=ccstatusline&show_icons=true&hide_border=true&theme=default&card_width=400)](https://github.com/sirmalloc/ccstatusline)
<br>

[`claude-code-statusline`](https://github.com/rz1989s/claude-code-statusline) &nbsp; by &nbsp; [rz1989s](https://github.com/rz1989s)  &nbsp;&nbsp;⚖️&nbsp;&nbsp;MIT  
Enhanced 4-line statusline for Claude Code with themes, cost tracking, and MCP server monitoring

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=rz1989s&repo=claude-code-statusline&show_icons=true&hide_border=true&theme=default&card_width=400)](https://github.com/rz1989s/claude-code-statusline)
<br>

[`claude-powerline`](https://github.com/Owloops/claude-powerline) &nbsp; by &nbsp; [Owloops](https://github.com/Owloops)  &nbsp;&nbsp;⚖️&nbsp;&nbsp;MIT  
A vim-style powerline statusline for Claude Code with real-time usage tracking, git integration, custom themes, and more

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=Owloops&repo=claude-powerline&show_icons=true&hide_border=true&theme=default&card_width=400)](https://github.com/Owloops/claude-powerline)
<br>

[`claudia-statusline`](https://github.com/hagan/claudia-statusline) &nbsp; by &nbsp; [Hagan Franks](https://github.com/hagan)  &nbsp;&nbsp;⚖️&nbsp;&nbsp;MIT  
High-performance Rust-based statusline for Claude Code with persistent stats tracking, progress bars, and optional cloud sync. Features SQLite-first persistence, git integration, context progress bars, burn rate calculation, XDG-compliant with theme support (dark/light, NO_COLOR).

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=hagan&repo=claudia-statusline&show_icons=true&hide_border=true&theme=default&card_width=400)](https://github.com/hagan/claudia-statusline)
<br>

</details>

<br>

## Hooks 🪝 [🔝](#awesome-claude-code)

> **Hooks** are a powerful API for Claude Code that allows users to activate commands and run scripts at different points in Claude's agentic lifecycle.

<details open>
<summary><h3>General <a href="#awesome-claude-code">🔝</a></h3></summary>

[`CC Notify`](https://github.com/dazuiba/CCNotify) &nbsp; by &nbsp; [dazuiba](https://github.com/dazuiba)  &nbsp;&nbsp;⚖️&nbsp;&nbsp;MIT  
CCNotify provides desktop notifications for Claude Code, alerting you to input needs or task completion, with one-click jumps back to VS Code and task duration display.

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=dazuiba&repo=CCNotify&show_icons=true&hide_border=true&theme=default&card_width=400)](https://github.com/dazuiba/CCNotify)
<br>

[`cchooks`](https://github.com/GowayLee/cchooks) &nbsp; by &nbsp; [GowayLee](https://github.com/GowayLee)  &nbsp;&nbsp;⚖️&nbsp;&nbsp;MIT  
A lightweight Python SDK with a clean API and good documentation; simplifies the process of writing hooks and integrating them into your codebase, providing a nice abstraction over the JSON configuration files.

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=GowayLee&repo=cchooks&show_icons=true&hide_border=true&theme=default&card_width=400)](https://github.com/GowayLee/cchooks)
<br>

[`claude-code-hooks-sdk`](https://github.com/beyondcode/claude-hooks-sdk) &nbsp; by &nbsp; [beyondcode](https://github.com/beyondcode)  &nbsp;&nbsp;⚖️&nbsp;&nbsp;MIT  
A Laravel-inspired PHP SDK for building Claude Code hook responses with a clean, fluent API. This SDK makes it easy to create structured JSON responses for Claude Code hooks using an expressive, chainable interface.

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=beyondcode&repo=claude-hooks-sdk&show_icons=true&hide_border=true&theme=default&card_width=400)](https://github.com/beyondcode/claude-hooks-sdk)
<br>

[`claude-hooks`](https://github.com/johnlindquist/claude-hooks) &nbsp; by &nbsp; [John Lindquist](https://github.com/johnlindquist)  &nbsp;&nbsp;⚖️&nbsp;&nbsp;MIT  
A TypeScript-based system for configuring and customizing Claude Code hooks with a powerful and flexible interface.

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=johnlindquist&repo=claude-hooks&show_icons=true&hide_border=true&theme=default&card_width=400)](https://github.com/johnlindquist/claude-hooks)
<br>

[`claude-mem`](https://github.com/thedotmack/claude-mem) &nbsp; by &nbsp; [Alex Newman](https://github.com/thedotmack)  &nbsp;&nbsp;⚖️&nbsp;&nbsp;NOASSERTION  
Persistent memory compression system that captures tool usage, generates AI-powered session summaries, and injects relevant context into future Claude Code sessions through SQLite storage and full-text search across project history (and no extra-cost dependencies!). 🦾

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=thedotmack&repo=claude-mem&show_icons=true&hide_border=true&theme=default&card_width=400)](https://github.com/thedotmack/claude-mem)
<br>

[`Claudio`](https://github.com/ctoth/claudio) &nbsp; by &nbsp; [Christopher Toth](https://github.com/ctoth)    
A no-frills little library that adds delightful OS-native sounds to Claude Code via simple hooks. It really sparks joy.

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=ctoth&repo=claudio&show_icons=true&hide_border=true&theme=default&card_width=400)](https://github.com/ctoth/claudio)
<br>

[`fcakyon Collection (Code Quality and Tool Usage)`](https://github.com/fcakyon/claude-codex-settings/tree/main/.claude/hooks) &nbsp; by &nbsp; [Fatih Akyon](https://github.com/fcakyon)  &nbsp;&nbsp;⚖️&nbsp;&nbsp;Apache-2.0  
Very well-written set of hooks for code quality and tool usage regulation (e.g. force Tavily over WebFetch tool).

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=fcakyon&repo=claude-codex-settings&show_icons=true&hide_border=true&theme=default&card_width=400)](https://github.com/fcakyon/claude-codex-settings)
<br>

[`TDD Guard`](https://github.com/nizos/tdd-guard) &nbsp; by &nbsp; [Nizar Selander](https://github.com/nizos)  &nbsp;&nbsp;⚖️&nbsp;&nbsp;MIT  
A hooks-driven system that monitors file operations in real-time and blocks changes that violate TDD principles.

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=nizos&repo=tdd-guard&show_icons=true&hide_border=true&theme=default&card_width=400)](https://github.com/nizos/tdd-guard)
<br>

[`TypeScript Quality Hooks`](https://github.com/bartolli/claude-code-typescript-hooks) &nbsp; by &nbsp; [bartolli](https://github.com/bartolli)  &nbsp;&nbsp;⚖️&nbsp;&nbsp;MIT  
Quality check hook for Node.js TypeScript projects with TypeScript compilation. ESLint auto-fixing, and Prettier formatting. Uses SHA256 config caching for <5ms validation performance during real-time editing.

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=bartolli&repo=claude-code-typescript-hooks&show_icons=true&hide_border=true&theme=default&card_width=400)](https://github.com/bartolli/claude-code-typescript-hooks)
<br>

[`claude-code-guardian`](https://github.com/jfpedroza/claude-code-guardian) &nbsp; by &nbsp; [jfpedroza](https://github.com/jfpedroza)  &nbsp;&nbsp;⚖️&nbsp;&nbsp;MIT  
Validation and permission system for Claude Code focused on controlling what Claude Code can execute, read or write. Allows users to define a set of rules to evaluate. E.g., allow `git push` but not `git push --force`.

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=jfpedroza&repo=claude-code-guardian&show_icons=true&hide_border=true&theme=default&card_width=400)](https://github.com/jfpedroza/claude-code-guardian)
<br>

[`Claude Code Hook Comms (HCOM)`](https://github.com/aannoo/claude-hook-comms) &nbsp; by &nbsp; [aannoo](https://github.com/aannoo)  &nbsp;&nbsp;⚖️&nbsp;&nbsp;MIT  
Lightweight CLI tool for real-time communication between Claude Code sub agents using hooks. Enables multi-agent collaboration with @-mention targeting, live dashboard monitoring, and zero-dependency implementation.

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=aannoo&repo=claude-hook-comms&show_icons=true&hide_border=true&theme=default&card_width=400)](https://github.com/aannoo/claude-hook-comms)
<br>

</details>

<br>

## Output Styles 💬 [🔝](#awesome-claude-code)

> **Output styles** allow you to use Claude Code as any type of agent while keeping its core capabilities, such as running local scripts, reading/writing files, and tracking TODOs.

<details open>
<summary><h3>General <a href="#awesome-claude-code">🔝</a></h3></summary>

[`ccoutputstyles`](https://github.com/viveknair/ccoutputstyles) &nbsp; by &nbsp; [Vivek Nair](https://github.com/viveknair)  &nbsp;&nbsp;⚖️&nbsp;&nbsp;MIT  
CLI tool and template gallery for customizing Claude Code output styles with pre-built templates. Features over 15 templates at the time of writing!

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=viveknair&repo=ccoutputstyles&show_icons=true&hide_border=true&theme=default&card_width=400)](https://github.com/viveknair/ccoutputstyles)
<br>

[`Claude X`](https://github.com/kunwar-shah/claudex) &nbsp; by &nbsp; [Kunwar Shah](https://github.com/kunwar-shah)  &nbsp;&nbsp;⚖️&nbsp;&nbsp;MIT  
Claudex - A friendly viewer, Browse and explore your Claude conversations. Features auto project discovery (scans ~/.claude/projects), SQLite FTS5-powered full-text search, session analytics, and export options (JSON, HTML, TXT).

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=kunwar-shah&repo=claudex&show_icons=true&hide_border=true&theme=default&card_width=400)](https://github.com/kunwar-shah/claudex)
<br>

</details>

<br>

## Slash-Commands 🔪 [🔝](#awesome-claude-code)

<details open>
<summary><h3>General <a href="#awesome-claude-code">🔝</a></h3></summary>

[`/create-hook`](https://github.com/omril321/automated-notebooklm/blob/main/.claude/commands/create-hook.md) &nbsp; by &nbsp; [Omri Lavi](https://github.com/omril321)  &nbsp;&nbsp;⚖️&nbsp;&nbsp;Apache-2.0  
Slash command for hook creation - intelligently prompts you through the creation process with smart suggestions based on your project setup (TS, Prettier, ESLint...).

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=omril321&repo=automated-notebooklm&show_icons=true&hide_border=true&theme=default&card_width=400)](https://github.com/omril321/automated-notebooklm)
<br>

[`/linux-desktop-slash-commands`](https://github.com/danielrosehill/Claude-Code-Linux-Desktop-Slash-Commands) &nbsp; by &nbsp; [Daniel Rosehill](https://github.com/danielrosehill)    
A library of slash commands intended specifically to facilitate common and advanced operations on Linux desktop environments (although many would also be useful on Linux servers). Command groups include hardware benchmarking, filesystem organisation, and security posture validation.

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=danielrosehill&repo=Claude-Code-Linux-Desktop-Slash-Commands&show_icons=true&hide_border=true&theme=default&card_width=400)](https://github.com/danielrosehill/Claude-Code-Linux-Desktop-Slash-Commands)
<br>

[`Session Driven Development`](https://github.com/ankushdixit/sdd) &nbsp; by &nbsp; [Ankush Dixit](https://github.com/ankushdixit)  &nbsp;&nbsp;⚖️&nbsp;&nbsp;MIT  
SDD implements Session-Driven Development, a comprehensive methodology that enables AI coding assistants to work on software projects across multiple sessions with perfect context continuity, enforced quality standards, and accumulated institutional knowledge.

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=ankushdixit&repo=sdd&show_icons=true&hide_border=true&theme=default&card_width=400)](https://github.com/ankushdixit/sdd)
<br>

</details>

<details open>
<summary><h3>Version Control & Git <a href="#awesome-claude-code">🔝</a></h3></summary>

[`/analyze-issue`](https://github.com/jerseycheese/Narraitor/blob/feature/issue-227-ai-suggestions/.claude/commands/analyze-issue.md) &nbsp; by &nbsp; [jerseycheese](https://github.com/jerseycheese)  &nbsp;&nbsp;⚖️&nbsp;&nbsp;MIT  
Fetches GitHub issue details to create comprehensive implementation specifications, analyzing requirements and planning structured approach with clear implementation steps.

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=jerseycheese&repo=Narraitor&show_icons=true&hide_border=true&theme=default&card_width=400)](https://github.com/jerseycheese/Narraitor)
<br>

[`/commit`](https://github.com/evmts/tevm-monorepo/blob/main/.claude/commands/commit.md) &nbsp; by &nbsp; [evmts](https://github.com/evmts)  &nbsp;&nbsp;⚖️&nbsp;&nbsp;MIT  
Creates git commits using conventional commit format with appropriate emojis, following project standards and creating descriptive messages that explain the purpose of changes.

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=evmts&repo=tevm-monorepo&show_icons=true&hide_border=true&theme=default&card_width=400)](https://github.com/evmts/tevm-monorepo)
<br>

[`/commit-fast`](https://github.com/steadycursor/steadystart/blob/main/.claude/commands/2-commit-fast.md) &nbsp; by &nbsp; [steadycursor](https://github.com/steadycursor)    
Automates git commit process by selecting the first suggested message, generating structured commits with consistent formatting while skipping manual confirmation and removing Claude co-Contributorship footer

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=steadycursor&repo=steadystart&show_icons=true&hide_border=true&theme=default&card_width=400)](https://github.com/steadycursor/steadystart)
<br>

[`/create-pr`](https://github.com/toyamarinyon/giselle/blob/main/.claude/commands/create-pr.md) &nbsp; by &nbsp; [toyamarinyon](https://github.com/toyamarinyon)  &nbsp;&nbsp;⚖️&nbsp;&nbsp;Apache-2.0  
Streamlines pull request creation by handling the entire workflow: creating a new branch, committing changes, formatting modified files with Biome, and submitting the PR.

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=toyamarinyon&repo=giselle&show_icons=true&hide_border=true&theme=default&card_width=400)](https://github.com/toyamarinyon/giselle)
<br>

[`/create-pull-request`](https://github.com/liam-hq/liam/blob/main/.claude/commands/create-pull-request.md) &nbsp; by &nbsp; [liam-hq](https://github.com/liam-hq)  &nbsp;&nbsp;⚖️&nbsp;&nbsp;Apache-2.0  
Provides comprehensive PR creation guidance with GitHub CLI, enforcing title conventions, following template structure, and offering concrete command examples with best practices.

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=liam-hq&repo=liam&show_icons=true&hide_border=true&theme=default&card_width=400)](https://github.com/liam-hq/liam)
<br>

[`/create-worktrees`](https://github.com/evmts/tevm-monorepo/blob/main/.claude/commands/create-worktrees.md) &nbsp; by &nbsp; [evmts](https://github.com/evmts)  &nbsp;&nbsp;⚖️&nbsp;&nbsp;MIT  
Creates git worktrees for all open PRs or specific branches, handling branches with slashes, cleaning up stale worktrees, and supporting custom branch creation for development.

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=evmts&repo=tevm-monorepo&show_icons=true&hide_border=true&theme=default&card_width=400)](https://github.com/evmts/tevm-monorepo)
<br>

[`/fix-github-issue`](https://github.com/jeremymailen/kotlinter-gradle/blob/master/.claude/commands/fix-github-issue.md) &nbsp; by &nbsp; [jeremymailen](https://github.com/jeremymailen)  &nbsp;&nbsp;⚖️&nbsp;&nbsp;Apache-2.0  
Analyzes and fixes GitHub issues using a structured approach with GitHub CLI for issue details, implementing necessary code changes, running tests, and creating proper commit messages.

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=jeremymailen&repo=kotlinter-gradle&show_icons=true&hide_border=true&theme=default&card_width=400)](https://github.com/jeremymailen/kotlinter-gradle)
<br>

[`/fix-issue`](https://github.com/metabase/metabase/blob/master/.claude/commands/fix-issue.md) &nbsp; by &nbsp; [metabase](https://github.com/metabase)  &nbsp;&nbsp;⚖️&nbsp;&nbsp;NOASSERTION  
Addresses GitHub issues by taking issue number as parameter, analyzing context, implementing solution, and testing/validating the fix for proper integration.

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=metabase&repo=metabase&show_icons=true&hide_border=true&theme=default&card_width=400)](https://github.com/metabase/metabase)
<br>

[`/fix-pr`](https://github.com/metabase/metabase/blob/master/.claude/commands/fix-pr.md) &nbsp; by &nbsp; [metabase](https://github.com/metabase)  &nbsp;&nbsp;⚖️&nbsp;&nbsp;NOASSERTION  
Fetches and fixes unresolved PR comments by automatically retrieving feedback, addressing reviewer concerns, making targeted code improvements, and streamlining the review process.

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=metabase&repo=metabase&show_icons=true&hide_border=true&theme=default&card_width=400)](https://github.com/metabase/metabase)
<br>

[`/husky`](https://github.com/evmts/tevm-monorepo/blob/main/.claude/commands/husky.md) &nbsp; by &nbsp; [evmts](https://github.com/evmts)  &nbsp;&nbsp;⚖️&nbsp;&nbsp;MIT  
Sets up and manages Husky Git hooks by configuring pre-commit hooks, establishing commit message standards, integrating with linting tools, and ensuring code quality on commits.

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=evmts&repo=tevm-monorepo&show_icons=true&hide_border=true&theme=default&card_width=400)](https://github.com/evmts/tevm-monorepo)
<br>

[`/pr-review`](https://github.com/arkavo-org/opentdf-rs/blob/main/.claude/commands/pr-review.md) &nbsp; by &nbsp; [arkavo-org](https://github.com/arkavo-org)  &nbsp;&nbsp;⚖️&nbsp;&nbsp;MIT  
Reviews pull request changes to provide feedback, check for issues, and suggest improvements before merging into the main codebase.

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=arkavo-org&repo=opentdf-rs&show_icons=true&hide_border=true&theme=default&card_width=400)](https://github.com/arkavo-org/opentdf-rs)
<br>

[`/update-branch-name`](https://github.com/giselles-ai/giselle/blob/main/.claude/commands/update-branch-name.md) &nbsp; by &nbsp; [giselles-ai](https://github.com/giselles-ai)  &nbsp;&nbsp;⚖️&nbsp;&nbsp;Apache-2.0  
Updates branch names with proper prefixes and formats, enforcing naming conventions, supporting semantic prefixes, and managing remote branch updates.

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=giselles-ai&repo=giselle&show_icons=true&hide_border=true&theme=default&card_width=400)](https://github.com/giselles-ai/giselle)
<br>

</details>

<details open>
<summary><h3>Code Analysis & Testing <a href="#awesome-claude-code">🔝</a></h3></summary>

[`/check`](https://github.com/rygwdn/slack-tools/blob/main/.claude/commands/check.md) &nbsp; by &nbsp; [rygwdn](https://github.com/rygwdn)    
Performs comprehensive code quality and security checks, featuring static analysis integration, security vulnerability scanning, code style enforcement, and detailed reporting.

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=rygwdn&repo=slack-tools&show_icons=true&hide_border=true&theme=default&card_width=400)](https://github.com/rygwdn/slack-tools)
<br>

[`/clean`](https://github.com/Graphlet-AI/eridu/blob/main/.claude/commands/clean.md) &nbsp; by &nbsp; [Graphlet-AI](https://github.com/Graphlet-AI)  &nbsp;&nbsp;⚖️&nbsp;&nbsp;Apache-2.0  
Addresses code formatting and quality issues by fixing black formatting problems, organizing imports with isort, resolving flake8 linting issues, and correcting mypy type errors.

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=Graphlet-AI&repo=eridu&show_icons=true&hide_border=true&theme=default&card_width=400)](https://github.com/Graphlet-AI/eridu)
<br>

[`/code_analysis`](https://github.com/kingler/n8n_agent/blob/main/.claude/commands/code_analysis.md) &nbsp; by &nbsp; [kingler](https://github.com/kingler)    
Provides a menu of advanced code analysis commands for deep inspection, including knowledge graph generation, optimization suggestions, and quality evaluation.

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=kingler&repo=n8n_agent&show_icons=true&hide_border=true&theme=default&card_width=400)](https://github.com/kingler/n8n_agent)
<br>

[`/optimize`](https://github.com/to4iki/ai-project-rules/blob/main/.claude/commands/optimize.md) &nbsp; by &nbsp; [to4iki](https://github.com/to4iki)  &nbsp;&nbsp;⚖️&nbsp;&nbsp;MIT  
Analyzes code performance to identify bottlenecks, proposing concrete optimizations with implementation guidance for improved application performance.

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=to4iki&repo=ai-project-rules&show_icons=true&hide_border=true&theme=default&card_width=400)](https://github.com/to4iki/ai-project-rules)
<br>

[`/repro-issue`](https://github.com/rzykov/metabase/blob/master/.claude/commands/repro-issue.md) &nbsp; by &nbsp; [rzykov](https://github.com/rzykov)  &nbsp;&nbsp;⚖️&nbsp;&nbsp;NOASSERTION  
Creates reproducible test cases for GitHub issues, ensuring tests fail reliably and documenting clear reproduction steps for developers.

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=rzykov&repo=metabase&show_icons=true&hide_border=true&theme=default&card_width=400)](https://github.com/rzykov/metabase)
<br>

[`/tdd`](https://github.com/zscott/pane/blob/main/.claude/commands/tdd.md) &nbsp; by &nbsp; [zscott](https://github.com/zscott)    
Guides development using Test-Driven Development principles, enforcing Red-Green-Refactor discipline, integrating with git workflow, and managing PR creation.

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=zscott&repo=pane&show_icons=true&hide_border=true&theme=default&card_width=400)](https://github.com/zscott/pane)
<br>

[`/tdd-implement`](https://github.com/jerseycheese/Narraitor/blob/feature/issue-227-ai-suggestions/.claude/commands/tdd-implement.md) &nbsp; by &nbsp; [jerseycheese](https://github.com/jerseycheese)  &nbsp;&nbsp;⚖️&nbsp;&nbsp;MIT  
Implements Test-Driven Development by analyzing feature requirements, creating tests first (red), implementing minimal passing code (green), and refactoring while maintaining tests.

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=jerseycheese&repo=Narraitor&show_icons=true&hide_border=true&theme=default&card_width=400)](https://github.com/jerseycheese/Narraitor)
<br>

</details>

<details open>
<summary><h3>Context Loading & Priming <a href="#awesome-claude-code">🔝</a></h3></summary>

[`/context-prime`](https://github.com/elizaOS/elizaos.github.io/blob/main/.claude/commands/context-prime.md) &nbsp; by &nbsp; [elizaOS](https://github.com/elizaOS)  &nbsp;&nbsp;⚖️&nbsp;&nbsp;MIT  
Primes Claude with comprehensive project understanding by loading repository structure, setting development context, establishing project goals, and defining collaboration parameters.

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=elizaOS&repo=elizaos.github.io&show_icons=true&hide_border=true&theme=default&card_width=400)](https://github.com/elizaOS/elizaos.github.io)
<br>

[`/initref`](https://github.com/okuvshynov/cubestat/blob/main/.claude/commands/initref.md) &nbsp; by &nbsp; [okuvshynov](https://github.com/okuvshynov)  &nbsp;&nbsp;⚖️&nbsp;&nbsp;MIT  
Initializes reference documentation structure with standard doc templates, API reference setup, documentation conventions, and placeholder content generation.

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=okuvshynov&repo=cubestat&show_icons=true&hide_border=true&theme=default&card_width=400)](https://github.com/okuvshynov/cubestat)
<br>

[`/load-llms-txt`](https://github.com/ethpandaops/xatu-data/blob/master/.claude/commands/load-llms-txt.md) &nbsp; by &nbsp; [ethpandaops](https://github.com/ethpandaops)  &nbsp;&nbsp;⚖️&nbsp;&nbsp;MIT  
Loads LLM configuration files to context, importing specific terminology, model configurations, and establishing baseline terminology for AI discussions.

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=ethpandaops&repo=xatu-data&show_icons=true&hide_border=true&theme=default&card_width=400)](https://github.com/ethpandaops/xatu-data)
<br>

[`/load_coo_context`](https://github.com/Mjvolk3/torchcell/blob/main/.claude/commands/load_coo_context.md) &nbsp; by &nbsp; [Mjvolk3](https://github.com/Mjvolk3)    
References specific files for sparse matrix operations, explains transform usage, compares with previous approaches, and sets data formatting context for development.

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=Mjvolk3&repo=torchcell&show_icons=true&hide_border=true&theme=default&card_width=400)](https://github.com/Mjvolk3/torchcell)
<br>

[`/load_dango_pipeline`](https://github.com/Mjvolk3/torchcell/blob/main/.claude/commands/load_dango_pipeline.md) &nbsp; by &nbsp; [Mjvolk3](https://github.com/Mjvolk3)    
Sets context for model training by referencing pipeline files, establishing working context, and preparing for pipeline work with relevant documentation.

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=Mjvolk3&repo=torchcell&show_icons=true&hide_border=true&theme=default&card_width=400)](https://github.com/Mjvolk3/torchcell)
<br>

[`/prime`](https://github.com/yzyydev/AI-Engineering-Structure/blob/main/.claude/commands/prime.md) &nbsp; by &nbsp; [yzyydev](https://github.com/yzyydev)    
Sets up initial project context by viewing directory structure and reading key files, creating standardized context with directory visualization and key documentation focus.

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=yzyydev&repo=AI-Engineering-Structure&show_icons=true&hide_border=true&theme=default&card_width=400)](https://github.com/yzyydev/AI-Engineering-Structure)
<br>

[`/rsi`](https://github.com/ddisisto/si/blob/main/.claude/commands/rsi.md) &nbsp; by &nbsp; [ddisisto](https://github.com/ddisisto)    
Reads all commands and key project files to optimize AI-assisted development by streamlining the process, loading command context, and setting up for better development workflow.

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=ddisisto&repo=si&show_icons=true&hide_border=true&theme=default&card_width=400)](https://github.com/ddisisto/si)
<br>

</details>

<details open>
<summary><h3>Documentation & Changelogs <a href="#awesome-claude-code">🔝</a></h3></summary>

[`/add-to-changelog`](https://github.com/berrydev-ai/blockdoc-python/blob/main/.claude/commands/add-to-changelog.md) &nbsp; by &nbsp; [berrydev-ai](https://github.com/berrydev-ai)  &nbsp;&nbsp;⚖️&nbsp;&nbsp;MIT  
Adds new entries to changelog files while maintaining format consistency, properly documenting changes, and following established project standards for version tracking.

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=berrydev-ai&repo=blockdoc-python&show_icons=true&hide_border=true&theme=default&card_width=400)](https://github.com/berrydev-ai/blockdoc-python)
<br>

[`/create-docs`](https://github.com/jerseycheese/Narraitor/blob/feature/issue-227-ai-suggestions/.claude/commands/create-docs.md) &nbsp; by &nbsp; [jerseycheese](https://github.com/jerseycheese)  &nbsp;&nbsp;⚖️&nbsp;&nbsp;MIT  
Analyzes code structure and purpose to create comprehensive documentation detailing inputs/outputs, behavior, user interaction flows, and edge cases with error handling.

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=jerseycheese&repo=Narraitor&show_icons=true&hide_border=true&theme=default&card_width=400)](https://github.com/jerseycheese/Narraitor)
<br>

[`/docs`](https://github.com/slunsford/coffee-analytics/blob/main/.claude/commands/docs.md) &nbsp; by &nbsp; [slunsford](https://github.com/slunsford)    
Generates comprehensive documentation that follows project structure, documenting APIs and usage patterns with consistent formatting for better user understanding.

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=slunsford&repo=coffee-analytics&show_icons=true&hide_border=true&theme=default&card_width=400)](https://github.com/slunsford/coffee-analytics)
<br>

[`/explain-issue-fix`](https://github.com/hackdays-io/toban-contribution-viewer/blob/main/.claude/commands/explain-issue-fix.md) &nbsp; by &nbsp; [hackdays-io](https://github.com/hackdays-io)    
Documents solution approaches for GitHub issues, explaining technical decisions, detailing challenges overcome, and providing implementation context for better understanding.

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=hackdays-io&repo=toban-contribution-viewer&show_icons=true&hide_border=true&theme=default&card_width=400)](https://github.com/hackdays-io/toban-contribution-viewer)
<br>

[`/update-docs`](https://github.com/Consiliency/Flutter-Structurizr/blob/main/.claude/commands/update-docs.md) &nbsp; by &nbsp; [Consiliency](https://github.com/Consiliency)  &nbsp;&nbsp;⚖️&nbsp;&nbsp;MIT  
Reviews current documentation status, updates implementation progress, reviews phase documents, and maintains documentation consistency across the project.

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=Consiliency&repo=Flutter-Structurizr&show_icons=true&hide_border=true&theme=default&card_width=400)](https://github.com/Consiliency/Flutter-Structurizr)
<br>

</details>

<details open>
<summary><h3>CI / Deployment <a href="#awesome-claude-code">🔝</a></h3></summary>

[`/release`](https://github.com/kelp/webdown/blob/main/.claude/commands/release.md) &nbsp; by &nbsp; [kelp](https://github.com/kelp)  &nbsp;&nbsp;⚖️&nbsp;&nbsp;MIT  
Manages software releases by updating changelogs, reviewing README changes, evaluating version increments, and documenting release changes for better version tracking.

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=kelp&repo=webdown&show_icons=true&hide_border=true&theme=default&card_width=400)](https://github.com/kelp/webdown)
<br>

[`/run-ci`](https://github.com/hackdays-io/toban-contribution-viewer/blob/main/.claude/commands/run-ci.md) &nbsp; by &nbsp; [hackdays-io](https://github.com/hackdays-io)    
Activates virtual environments, runs CI-compatible check scripts, iteratively fixes errors, and ensures all tests pass before completion.

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=hackdays-io&repo=toban-contribution-viewer&show_icons=true&hide_border=true&theme=default&card_width=400)](https://github.com/hackdays-io/toban-contribution-viewer)
<br>

</details>

<details open>
<summary><h3>Project & Task Management <a href="#awesome-claude-code">🔝</a></h3></summary>

[`/create-command`](https://github.com/scopecraft/command/blob/main/.claude/commands/create-command.md) &nbsp; by &nbsp; [scopecraft](https://github.com/scopecraft)    
Guides Claude through creating new custom commands with proper structure by analyzing requirements, templating commands by category, enforcing command standards, and creating supporting documentation.

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=scopecraft&repo=command&show_icons=true&hide_border=true&theme=default&card_width=400)](https://github.com/scopecraft/command)
<br>

[`/create-jtbd`](https://github.com/taddyorg/inkverse/blob/main/.claude/commands/create-jtbd.md) &nbsp; by &nbsp; [taddyorg](https://github.com/taddyorg)  &nbsp;&nbsp;⚖️&nbsp;&nbsp;AGPL-3.0  
Creates Jobs-to-be-Done frameworks that outline user needs with structured format, focusing on specific user problems and organizing by job categories for product development.

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=taddyorg&repo=inkverse&show_icons=true&hide_border=true&theme=default&card_width=400)](https://github.com/taddyorg/inkverse)
<br>

[`/create-prd`](https://github.com/taddyorg/inkverse/blob/main/.claude/commands/create-prd.md) &nbsp; by &nbsp; [taddyorg](https://github.com/taddyorg)  &nbsp;&nbsp;⚖️&nbsp;&nbsp;AGPL-3.0  
Generates comprehensive product requirement documents outlining detailed specifications, requirements, and features following standardized document structure and format.

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=taddyorg&repo=inkverse&show_icons=true&hide_border=true&theme=default&card_width=400)](https://github.com/taddyorg/inkverse)
<br>

[`/create-prp`](https://github.com/Wirasm/claudecode-utils/blob/main/.claude/commands/create-prp.md) &nbsp; by &nbsp; [Wirasm](https://github.com/Wirasm)  &nbsp;&nbsp;⚖️&nbsp;&nbsp;MIT  
Creates product requirement plans by reading PRP methodology, following template structure, creating comprehensive requirements, and structuring product definitions for development.

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=Wirasm&repo=claudecode-utils&show_icons=true&hide_border=true&theme=default&card_width=400)](https://github.com/Wirasm/claudecode-utils)
<br>

[`/do-issue`](https://github.com/jerseycheese/Narraitor/blob/feature/issue-227-ai-suggestions/.claude/commands/do-issue.md) &nbsp; by &nbsp; [jerseycheese](https://github.com/jerseycheese)  &nbsp;&nbsp;⚖️&nbsp;&nbsp;MIT  
Implements GitHub issues with manual review points, following a structured approach with issue number parameter and offering alternative automated mode for efficiency.

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=jerseycheese&repo=Narraitor&show_icons=true&hide_border=true&theme=default&card_width=400)](https://github.com/jerseycheese/Narraitor)
<br>

[`/project_hello_w_name`](https://github.com/disler/just-prompt/blob/main/.claude/commands/project_hello_w_name.md) &nbsp; by &nbsp; [disler](https://github.com/disler)    
Creates customizable greeting components with name input, demonstrating argument passing, component reusability, state management, and user input handling.

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=disler&repo=just-prompt&show_icons=true&hide_border=true&theme=default&card_width=400)](https://github.com/disler/just-prompt)
<br>

[`/todo`](https://github.com/chrisleyva/todo-slash-command/blob/main/todo.md) &nbsp; by &nbsp; [chrisleyva](https://github.com/chrisleyva)  &nbsp;&nbsp;⚖️&nbsp;&nbsp;MIT  
A convenient command to quickly manage project todo items without leaving the Claude Code interface, featuring due dates, sorting, task prioritization, and comprehensive todo list management.

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=chrisleyva&repo=todo-slash-command&show_icons=true&hide_border=true&theme=default&card_width=400)](https://github.com/chrisleyva/todo-slash-command)
<br>

</details>

<details open>
<summary><h3>Miscellaneous <a href="#awesome-claude-code">🔝</a></h3></summary>

[`/five`](https://github.com/TuckerTucker/tkr-portfolio/blob/main/.claude/commands/five.md) &nbsp; by &nbsp; [TuckerTucker](https://github.com/TuckerTucker)    
Applies the "five whys" methodology to perform root cause analysis, identify underlying issues, and create solution approaches for complex problems.

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=TuckerTucker&repo=tkr-portfolio&show_icons=true&hide_border=true&theme=default&card_width=400)](https://github.com/TuckerTucker/tkr-portfolio)
<br>

[`/fixing_go_in_graph`](https://github.com/Mjvolk3/torchcell/blob/main/.claude/commands/fixing_go_in_graph.md) &nbsp; by &nbsp; [Mjvolk3](https://github.com/Mjvolk3)    
Focuses on Gene Ontology annotation integration in graph databases, handling multiple data sources, addressing graph representation issues, and ensuring correct data incorporation.

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=Mjvolk3&repo=torchcell&show_icons=true&hide_border=true&theme=default&card_width=400)](https://github.com/Mjvolk3/torchcell)
<br>

[`/mermaid`](https://github.com/GaloyMoney/lana-bank/blob/main/.claude/commands/mermaid.md) &nbsp; by &nbsp; [GaloyMoney](https://github.com/GaloyMoney)  &nbsp;&nbsp;⚖️&nbsp;&nbsp;NOASSERTION  
Generates Mermaid diagrams from SQL schema files, creating entity relationship diagrams with table properties, validating diagram compilation, and ensuring complete entity coverage.

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=GaloyMoney&repo=lana-bank&show_icons=true&hide_border=true&theme=default&card_width=400)](https://github.com/GaloyMoney/lana-bank)
<br>

[`/review_dcell_model`](https://github.com/Mjvolk3/torchcell/blob/main/.claude/commands/review_dcell_model.md) &nbsp; by &nbsp; [Mjvolk3](https://github.com/Mjvolk3)    
Reviews old Dcell implementation files, comparing with newer Dango model, noting changes over time, and analyzing refactoring approaches for better code organization.

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=Mjvolk3&repo=torchcell&show_icons=true&hide_border=true&theme=default&card_width=400)](https://github.com/Mjvolk3/torchcell)
<br>

[`/use-stepper`](https://github.com/zuplo/docs/blob/main/.claude/commands/use-stepper.md) &nbsp; by &nbsp; [zuplo](https://github.com/zuplo)    
Reformats documentation to use React Stepper component, transforming heading formats, applying proper indentation, and maintaining markdown compatibility with admonition formatting.

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=zuplo&repo=docs&show_icons=true&hide_border=true&theme=default&card_width=400)](https://github.com/zuplo/docs)
<br>

</details>

<br>

## CLAUDE.md Files 📂 [🔝](#awesome-claude-code)

> **`CLAUDE.md` files** are files that contain important guidelines and context-specific information or instructions that help Claude Code to better understand your project and your coding standards

<details open>
<summary><h3>General <a href="#awesome-claude-code">🔝</a></h3></summary>

[`Claude Code Sub agents Starter Kit`](https://github.com/shinpr/ai-coding-project-boilerplate) &nbsp; by &nbsp; [shinpr](https://github.com/shinpr)  &nbsp;&nbsp;⚖️&nbsp;&nbsp;MIT  
Comprehensive Claude Code configuration featuring 11 specialized Sub agents with independent contexts and rule-based development system - maintains production-grade TypeScript quality across 770K+ token sessions without context exhaustion.

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=shinpr&repo=ai-coding-project-boilerplate&show_icons=true&hide_border=true&theme=default&card_width=400)](https://github.com/shinpr/ai-coding-project-boilerplate)
<br>

[`AI Coding Project Boilerplate`](https://github.com/shinpr/ai-coding-project-boilerplate) &nbsp; by &nbsp; [shinpr](https://github.com/shinpr)  &nbsp;&nbsp;⚖️&nbsp;&nbsp;MIT  
TypeScript boilerplate designed for AI-driven development with 10+ specialized sub-agents, preventive control mechanisms, and automated quality gates that enable Claude Code to work autonomously while maintaining production standards.

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=shinpr&repo=ai-coding-project-boilerplate&show_icons=true&hide_border=true&theme=default&card_width=400)](https://github.com/shinpr/ai-coding-project-boilerplate)
<br>

</details>

<details open>
<summary><h3>Language-Specific <a href="#awesome-claude-code">🔝</a></h3></summary>

[`AI IntelliJ Plugin`](https://github.com/didalgolab/ai-intellij-plugin/blob/main/CLAUDE.md) &nbsp; by &nbsp; [didalgolab](https://github.com/didalgolab)  &nbsp;&nbsp;⚖️&nbsp;&nbsp;Apache-2.0  
Provides comprehensive Gradle commands for IntelliJ plugin development with platform-specific coding patterns, detailed package structure guidelines, and clear internationalization standards.

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=didalgolab&repo=ai-intellij-plugin&show_icons=true&hide_border=true&theme=default&card_width=400)](https://github.com/didalgolab/ai-intellij-plugin)
<br>

[`AWS MCP Server`](https://github.com/alexei-led/aws-mcp-server/blob/main/CLAUDE.md) &nbsp; by &nbsp; [alexei-led](https://github.com/alexei-led)  &nbsp;&nbsp;⚖️&nbsp;&nbsp;MIT  
Features multiple Python environment setup options with detailed code style guidelines, comprehensive error handling recommendations, and security considerations for AWS CLI interactions.

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=alexei-led&repo=aws-mcp-server&show_icons=true&hide_border=true&theme=default&card_width=400)](https://github.com/alexei-led/aws-mcp-server)
<br>

[`DroidconKotlin`](https://github.com/touchlab/DroidconKotlin/blob/main/CLAUDE.md) &nbsp; by &nbsp; [touchlab](https://github.com/touchlab)  &nbsp;&nbsp;⚖️&nbsp;&nbsp;Apache-2.0  
Delivers comprehensive Gradle commands for cross-platform Kotlin Multiplatform development with clear module structure and practical guidance for dependency injection.

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=touchlab&repo=DroidconKotlin&show_icons=true&hide_border=true&theme=default&card_width=400)](https://github.com/touchlab/DroidconKotlin)
<br>

[`EDSL`](https://github.com/hesreallyhim/awesome-claude-code/blob/main/resources/claude.md-files/EDSL/CLAUDE.md) &nbsp; by &nbsp; [expectedparrot](https://github.com/expectedparrot)  &nbsp;&nbsp;⚖️&nbsp;&nbsp;MIT  
Offers detailed build and test commands with strict code style enforcement, comprehensive testing requirements, and standardized development workflow using Black and mypy.*  
<sub>* Removed from origin</sub>

[`Giselle`](https://github.com/giselles-ai/giselle/blob/main/CLAUDE.md) &nbsp; by &nbsp; [giselles-ai](https://github.com/giselles-ai)  &nbsp;&nbsp;⚖️&nbsp;&nbsp;Apache-2.0  
Provides detailed build and test commands using pnpm and Vitest with strict code formatting requirements and comprehensive naming conventions for code consistency.

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=giselles-ai&repo=giselle&show_icons=true&hide_border=true&theme=default&card_width=400)](https://github.com/giselles-ai/giselle)
<br>

[`HASH`](https://github.com/hashintel/hash/blob/main/CLAUDE.md) &nbsp; by &nbsp; [hashintel](https://github.com/hashintel)  &nbsp;&nbsp;⚖️&nbsp;&nbsp;NOASSERTION  
Features comprehensive repository structure breakdown with strong emphasis on coding standards, detailed Rust documentation guidelines, and systematic PR review process.

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=hashintel&repo=hash&show_icons=true&hide_border=true&theme=default&card_width=400)](https://github.com/hashintel/hash)
<br>

[`Inkline`](https://github.com/inkline/inkline/blob/main/CLAUDE.md) &nbsp; by &nbsp; [inkline](https://github.com/inkline)  &nbsp;&nbsp;⚖️&nbsp;&nbsp;NOASSERTION  
Structures development workflow using pnpm with emphasis on TypeScript and Vue 3 Composition API, detailed component creation process, and comprehensive testing recommendations.

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=inkline&repo=inkline&show_icons=true&hide_border=true&theme=default&card_width=400)](https://github.com/inkline/inkline)
<br>

[`JSBeeb`](https://github.com/mattgodbolt/jsbeeb/blob/main/CLAUDE.md) &nbsp; by &nbsp; [mattgodbolt](https://github.com/mattgodbolt)  &nbsp;&nbsp;⚖️&nbsp;&nbsp;GPL-3.0  
Provides development guide for JavaScript BBC Micro emulator with build and testing instructions, architecture documentation, and debugging workflows.

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=mattgodbolt&repo=jsbeeb&show_icons=true&hide_border=true&theme=default&card_width=400)](https://github.com/mattgodbolt/jsbeeb)
<br>

[`Lamoom Python`](https://github.com/LamoomAI/lamoom-python/blob/main/CLAUDE.md) &nbsp; by &nbsp; [LamoomAI](https://github.com/LamoomAI)  &nbsp;&nbsp;⚖️&nbsp;&nbsp;Apache-2.0  
Serves as reference for production prompt engineering library with load balancing of AI Models, API documentation, and usage patterns with examples.

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=LamoomAI&repo=lamoom-python&show_icons=true&hide_border=true&theme=default&card_width=400)](https://github.com/LamoomAI/lamoom-python)
<br>

[`LangGraphJS`](https://github.com/langchain-ai/langgraphjs/blob/main/CLAUDE.md) &nbsp; by &nbsp; [langchain-ai](https://github.com/langchain-ai)  &nbsp;&nbsp;⚖️&nbsp;&nbsp;MIT  
Offers comprehensive build and test commands with detailed TypeScript style guidelines, layered library architecture, and monorepo structure using yarn workspaces.

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=langchain-ai&repo=langgraphjs&show_icons=true&hide_border=true&theme=default&card_width=400)](https://github.com/langchain-ai/langgraphjs)
<br>

[`Metabase`](https://github.com/metabase/metabase/blob/master/CLAUDE.md) &nbsp; by &nbsp; [metabase](https://github.com/metabase)  &nbsp;&nbsp;⚖️&nbsp;&nbsp;NOASSERTION  
Details workflow for REPL-driven development in Clojure/ClojureScript with emphasis on incremental development, testing, and step-by-step approach for feature implementation.

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=metabase&repo=metabase&show_icons=true&hide_border=true&theme=default&card_width=400)](https://github.com/metabase/metabase)
<br>

[`SG Cars Trends Backend`](https://github.com/sgcarstrends/backend/blob/main/CLAUDE.md) &nbsp; by &nbsp; [sgcarstrends](https://github.com/sgcarstrends)  &nbsp;&nbsp;⚖️&nbsp;&nbsp;MIT  
Provides comprehensive structure for TypeScript monorepo projects with detailed commands for development, testing, deployment, and AWS/Cloudflare integration.

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=sgcarstrends&repo=backend&show_icons=true&hide_border=true&theme=default&card_width=400)](https://github.com/sgcarstrends/backend)
<br>

[`SPy`](https://github.com/spylang/spy/blob/main/CLAUDE.md) &nbsp; by &nbsp; [spylang](https://github.com/spylang)  &nbsp;&nbsp;⚖️&nbsp;&nbsp;MIT  
Enforces strict coding conventions with comprehensive testing guidelines, multiple code compilation options, and backend-specific test decorators for targeted filtering.

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=spylang&repo=spy&show_icons=true&hide_border=true&theme=default&card_width=400)](https://github.com/spylang/spy)
<br>

[`TPL`](https://github.com/KarpelesLab/tpl/blob/master/CLAUDE.md) &nbsp; by &nbsp; [KarpelesLab](https://github.com/KarpelesLab)  &nbsp;&nbsp;⚖️&nbsp;&nbsp;MIT  
Details Go project conventions with comprehensive error handling recommendations, table-driven testing approach guidelines, and modernization suggestions for latest Go features.

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=KarpelesLab&repo=tpl&show_icons=true&hide_border=true&theme=default&card_width=400)](https://github.com/KarpelesLab/tpl)
<br>

</details>

<details open>
<summary><h3>Domain-Specific <a href="#awesome-claude-code">🔝</a></h3></summary>

[`AVS Vibe Developer Guide`](https://github.com/Layr-Labs/avs-vibe-developer-guide/blob/master/CLAUDE.md) &nbsp; by &nbsp; [Layr-Labs](https://github.com/Layr-Labs)  &nbsp;&nbsp;⚖️&nbsp;&nbsp;MIT  
Structures AI-assisted EigenLayer AVS development workflow with consistent naming conventions for prompt files and established terminology standards for blockchain concepts.

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=Layr-Labs&repo=avs-vibe-developer-guide&show_icons=true&hide_border=true&theme=default&card_width=400)](https://github.com/Layr-Labs/avs-vibe-developer-guide)
<br>

[`Comm`](https://github.com/CommE2E/comm/blob/master/CLAUDE.md) &nbsp; by &nbsp; [CommE2E](https://github.com/CommE2E)  &nbsp;&nbsp;⚖️&nbsp;&nbsp;BSD-3-Clause  
Serves as a development reference for E2E-encrypted messaging applications with code organization architecture, security implementation details, and testing procedures.

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=CommE2E&repo=comm&show_icons=true&hide_border=true&theme=default&card_width=400)](https://github.com/CommE2E/comm)
<br>

[`Course Builder`](https://github.com/badass-courses/course-builder/blob/main/CLAUDE.md) &nbsp; by &nbsp; [badass-courses](https://github.com/badass-courses)  &nbsp;&nbsp;⚖️&nbsp;&nbsp;MIT  
Enables real-time multiplayer capabilities for collaborative course creation with diverse tech stack integration and monorepo architecture using Turborepo.

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=badass-courses&repo=course-builder&show_icons=true&hide_border=true&theme=default&card_width=400)](https://github.com/badass-courses/course-builder)
<br>

[`Cursor Tools`](https://github.com/eastlondoner/cursor-tools/blob/main/CLAUDE.md) &nbsp; by &nbsp; [eastlondoner](https://github.com/eastlondoner)  &nbsp;&nbsp;⚖️&nbsp;&nbsp;MIT  
Creates a versatile AI command interface supporting multiple providers and models with flexible command options and browser automation through "Stagehand" feature.

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=eastlondoner&repo=cursor-tools&show_icons=true&hide_border=true&theme=default&card_width=400)](https://github.com/eastlondoner/cursor-tools)
<br>

[`Guitar`](https://github.com/soramimi/Guitar/blob/master/CLAUDE.md) &nbsp; by &nbsp; [soramimi](https://github.com/soramimi)  &nbsp;&nbsp;⚖️&nbsp;&nbsp;GPL-2.0  
Serves as development guide for Guitar Git GUI Client with build commands for various platforms, code style guidelines for contributing, and project structure explanation.

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=soramimi&repo=Guitar&show_icons=true&hide_border=true&theme=default&card_width=400)](https://github.com/soramimi/Guitar)
<br>

[`Network Chronicles`](https://github.com/Fimeg/NetworkChronicles/blob/legacy-v1/CLAUDE.md) &nbsp; by &nbsp; [Fimeg](https://github.com/Fimeg)  &nbsp;&nbsp;⚖️&nbsp;&nbsp;MIT  
Presents detailed implementation plan for AI-driven game characters with technical specifications for LLM integration, character guidelines, and service discovery mechanics.

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=Fimeg&repo=NetworkChronicles&show_icons=true&hide_border=true&theme=default&card_width=400)](https://github.com/Fimeg/NetworkChronicles)
<br>

[`Note Companion`](https://github.com/different-ai/note-companion/blob/master/CLAUDE.md) &nbsp; by &nbsp; [different-ai](https://github.com/different-ai)  &nbsp;&nbsp;⚖️&nbsp;&nbsp;MIT  
Provides detailed styling isolation techniques for Obsidian plugins using Tailwind with custom prefix to prevent style conflicts and practical troubleshooting steps.

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=different-ai&repo=note-companion&show_icons=true&hide_border=true&theme=default&card_width=400)](https://github.com/different-ai/note-companion)
<br>

[`Pareto Mac`](https://github.com/ParetoSecurity/pareto-mac/blob/main/CLAUDE.md) &nbsp; by &nbsp; [ParetoSecurity](https://github.com/ParetoSecurity)  &nbsp;&nbsp;⚖️&nbsp;&nbsp;GPL-3.0  
Serves as development guide for Mac security audit tool with build instructions, contribution guidelines, testing procedures, and workflow documentation.

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=ParetoSecurity&repo=pareto-mac&show_icons=true&hide_border=true&theme=default&card_width=400)](https://github.com/ParetoSecurity/pareto-mac)
<br>

[`SteadyStart`](https://github.com/steadycursor/steadystart/blob/main/CLAUDE.md) &nbsp; by &nbsp; [steadycursor](https://github.com/steadycursor)    
Clear and direct instructives about style, permissions, Claude's "role", communications, and documentation of Claude Code sessions for other team members to stay abreast.

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=steadycursor&repo=steadystart&show_icons=true&hide_border=true&theme=default&card_width=400)](https://github.com/steadycursor/steadystart)
<br>

</details>

<details open>
<summary><h3>Project Scaffolding & MCP <a href="#awesome-claude-code">🔝</a></h3></summary>

[`Basic Memory`](https://github.com/basicmachines-co/basic-memory/blob/main/CLAUDE.md) &nbsp; by &nbsp; [basicmachines-co](https://github.com/basicmachines-co)  &nbsp;&nbsp;⚖️&nbsp;&nbsp;AGPL-3.0  
Presents an innovative AI-human collaboration framework with Model Context Protocol for bidirectional LLM-markdown communication and flexible knowledge structure for complex projects.

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=basicmachines-co&repo=basic-memory&show_icons=true&hide_border=true&theme=default&card_width=400)](https://github.com/basicmachines-co/basic-memory)
<br>

[`claude-code-mcp-enhanced`](https://github.com/grahama1970/claude-code-mcp-enhanced/blob/main/CLAUDE.md) &nbsp; by &nbsp; [grahama1970](https://github.com/grahama1970)  &nbsp;&nbsp;⚖️&nbsp;&nbsp;MIT  
Provides detailed and emphatic instructions for Claude to follow as a coding agent, with testing guidance, code examples, and compliance checks.

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=grahama1970&repo=claude-code-mcp-enhanced&show_icons=true&hide_border=true&theme=default&card_width=400)](https://github.com/grahama1970/claude-code-mcp-enhanced)
<br>

[`Perplexity MCP`](https://github.com/Family-IT-Guy/perplexity-mcp/blob/main/CLAUDE.md) &nbsp; by &nbsp; [Family-IT-Guy](https://github.com/Family-IT-Guy)  &nbsp;&nbsp;⚖️&nbsp;&nbsp;ISC  
Offers clear step-by-step installation instructions with multiple configuration options, detailed troubleshooting guidance, and concise architecture overview of the MCP protocol.

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=Family-IT-Guy&repo=perplexity-mcp&show_icons=true&hide_border=true&theme=default&card_width=400)](https://github.com/Family-IT-Guy/perplexity-mcp)
<br>

</details>

<br>

## Alternative Clients 📱 [🔝](#awesome-claude-code)

> **Alternative Clients** are alternative UIs and front-ends for interacting with Claude Code, either on mobile or on the desktop.

<br>

## Official Documentation 🏛️ [🔝](#awesome-claude-code)

> Links to some of Anthropic's terrific documentation and resources regarding Claude Code

<!--lint disable double-link-->

<details open>
<summary><h3>General <a href="#awesome-claude-code">🔝</a></h3></summary>

[`Anthropic Documentation`](https://docs.claude.com/en/home) &nbsp; by &nbsp; [Anthropic](https://github.com/anthropics)  &nbsp;&nbsp;⚖️&nbsp;&nbsp;&copy;  
The official documentation for Claude Code, including installation instructions, usage guidelines, API references, tutorials, examples, loads of information that I won't list individually. Like Claude Code, the documentation is frequently updated.

[`Anthropic Quickstarts`](https://github.com/anthropics/claude-quickstarts) &nbsp; by &nbsp; [Anthropic](https://github.com/anthropics)  &nbsp;&nbsp;⚖️&nbsp;&nbsp;MIT  
Offers comprehensive development guides for three distinct AI-powered demo projects with standardized workflows, strict code style guidelines, and containerization instructions.

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=anthropics&repo=claude-quickstarts&show_icons=true&hide_border=true&theme=default&card_width=400)](https://github.com/anthropics/claude-quickstarts)
<br>

[`Claude Code GitHub Actions`](https://github.com/anthropics/claude-code-action/tree/main/examples) &nbsp; by &nbsp; [Anthropic](https://github.com/anthropics)  &nbsp;&nbsp;⚖️&nbsp;&nbsp;MIT  
Official GitHub Actions integration for Claude Code with examples and documentation for automating AI-powered workflows in CI/CD pipelines.

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=anthropics&repo=claude-code-action&show_icons=true&hide_border=true&theme=default&card_width=400)](https://github.com/anthropics/claude-code-action)
<br>

</details>


## Contributing 🌻 [🔝](#awesome-claude-code)

### 🚀 **[Submit a new resource here!](https://github.com/thedotmack/awesome-claude-code/issues/new?template=submit-resource.yml)**

It's easy! Just click the link above and fill out the form. No Git knowledge required - our automated system handles everything for you.

**How we evaluate submissions**

- **Automated Validation**: All submissions go through automated validation checks for security, licensing, and basic quality standards.
- **Auto-Approval**: If validation passes, your submission is automatically approved and added to the list within an hour. No human gatekeeping!
- **Community-Driven**: The community decides value through stars, forks, and usage. We don't impose subjective opinions on what's "valuable enough."

**What we welcome**

- All Claude Code tools, workflows, configurations, and resources
- All categories: orchestrators, IDE integrations, handbooks, cheat sheets, skills, hooks, commands, and more
- Projects at any stage: new, mature, experimental, or production-ready
- All approaches: simple utilities and complex frameworks alike

See [CONTRIBUTING.md](/CONTRIBUTING.md) for the complete submission guide and review process.

For suggestions about the repository itself, please [open a general issue](https://github.com/thedotmack/awesome-claude-code/issues/new).

This project is released with a [Contributor Code of Conduct](/code-of-conduct.md). By participating, you agree to abide by its terms. 

## Growing thanks to you ❤️
[![Stargazers over time](https://starchart.cc/thedotmack/awesome-claude-code.svg?variant=adaptive)](https://starchart.cc/thedotmack/awesome-claude-code)
