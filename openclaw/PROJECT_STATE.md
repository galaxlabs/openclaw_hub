# OpenClaw Project State (source of truth)

Date: 2026-02-24

## Goal
Personal agent to help Abdul Quddos:
- Track AI agent tools/news (public knowledge hub)
- LinkedIn-only job saving + analysis + drafts (manual send)
- Interview preparation
- Later: connect to Frappe DocTypes

## Repo
Path: ~/openclaw_hub
Remote: GitHub galaxlabs/openclaw_hub (branch main)

## Folder structure
00_inbox
01_tools
02_agents
03_news
04_linkedin_posts
05_job_hunt
06_tutorials
templates/
openclaw/

## Working commands
- Create job file:
  openclaw/bin/openclaw job "Company" "Role" "URL"
- Analyze a job file with Ollama:
  openclaw/bin/openclaw analyze path/to/job.md

## Ollama
Installed on VPS (CPU-only)
API: http://localhost:11434
Model tested: llama3.2:1b
Note: 1b model may not follow strict formatting; consider llama3.2:3b or better (RAM permitting).

## Python environment
Venv: openclaw/venv
Installed: requests
Package fix: openclaw/__init__.py
Ollama client: openclaw/ollama_client.py

## Prompt
Prompt file: openclaw/prompts/job_analysis.txt
Goal: force sections + avoid duplication
Issue: model sometimes ignores rules (1b weakness)

## Current next tasks
1) Improve model output reliability (try llama3.2:3b)
2) Update analyzer to re-write a specific section instead of appending messy output
3) Add skills system (skills.yaml + openclaw skills)
4) Auto git commit after analyze (optional)
