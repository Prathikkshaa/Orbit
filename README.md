# ⚡ Orbit — Personal Command Dashboard

A frontend-first execution control system built with **Streamlit**, designed for TNPSC Group 1 preparation tracking, skill-building, habit management, analytics, and idea pipeline management.

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.32+-FF4B4B?style=flat&logo=streamlit&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-Charts-3F4F75?style=flat&logo=plotly&logoColor=white)

---

## Pages

| Page | Purpose |
|------|---------|
| **Today Command Panel** | Daily focus subject, habits, priorities, and execution status |
| **Study Radar** | Subject-wise coverage, PYQ tracking, and confidence gauges |
| **Subject Map** | Paper-wise theme analysis with answer practice metrics |
| **Skill Builder Engine** | Technical skill tracking with Plotly progress bars |
| **Health + Finance Control** | Weight trend chart and savings projection with goal lines |
| **Idea Pipeline** | Kanban board with drag-stage transitions via dropdowns |
| **Analytics Cockpit** | Computed readiness scores, velocity, and lagging subject alerts |
| **Calendar Scheduler** | Weekly time-block allocation grid with editable slots |

## Features

- 🌗 **Dark / Light mode** with full CSS variable system
- 📊 **Plotly charts** with transparent, theme-aware styling
- 🔗 **Dynamic linkage** — scheduler edits update the Today Panel focus topic
- 📌 **Persistent top ribbon** showing focus subject, prelims/mains readiness, and habit score
- 💾 **Session state persistence** — toggles, edits, and selections survive reruns
- 🧮 **Computed analytics** — no hardcoded metrics, everything derived from data

## Quick Start

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Project Structure

```
├── app.py            # Main routing, sidebar, global ribbon, page renderers
├── components.py     # Reusable HTML component functions (cards, kanban, scheduler)
├── layout.py         # Page headers, column helpers, chart theme
├── theme.py          # CSS variable injection, font imports, dark/light tokens
├── mock_data.py      # Structured data (subjects, habits, schedule, ideas, etc.)
├── utils.py          # Computation helpers + render_safe_html sanitizer
└── requirements.txt  # Dependencies
```

## Tech Stack

- **Streamlit** — UI framework
- **Plotly** — Interactive charts (gauge, line, bar, scatter)
- **Pandas / NumPy** — Data structures and trend projection
- **Custom CSS** — Inter font, CSS variables, zero-dependency design system

---

*Built by [@Prathikkshaa](https://github.com/Prathikkshaa)*
