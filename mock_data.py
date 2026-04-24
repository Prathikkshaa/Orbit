import pandas as pd
from datetime import datetime, timedelta
import random

random.seed(42)

def get_past_date(days_ago):
    return (datetime.now() - timedelta(days=days_ago)).strftime('%Y-%m-%d')


SUBJECTS = {
    "Polity": {
        "coverage": 5, "pyq_coverage": 0,
        "revision_count": 0, "confidence": 5,
    },
    "History": {
        "coverage": 10, "pyq_coverage": 5,
        "revision_count": 0, "confidence": 8,
    },
    "Geography": {
        "coverage": 5, "pyq_coverage": 0,
        "revision_count": 0, "confidence": 5,
    },
    "Economy": {
        "coverage": 3, "pyq_coverage": 0,
        "revision_count": 0, "confidence": 3,
    },
    "Science": {
        "coverage": 5, "pyq_coverage": 0,
        "revision_count": 0, "confidence": 5,
    },
    "Environment": {
        "coverage": 3, "pyq_coverage": 0,
        "revision_count": 0, "confidence": 3,
    },
    "Tamil Nadu History": {
        "coverage": 15, "pyq_coverage": 8,
        "revision_count": 1, "confidence": 12,
    },
    "Aptitude": {
        "coverage": 3, "pyq_coverage": 0,
        "revision_count": 0, "confidence": 3,
    },
}


HABITS = {
    "Workout":     {"streak": 12, "done_today": False},
    "TNPSC Study": {"streak": 4,  "done_today": False},
    "Reading":     {"streak": 1,  "done_today": False},
    "Writing":     {"streak": 0,  "done_today": False},
}


WEEKLY_PRIORITIES = [
    {"title": "Set this Sunday — Priority 1",
     "status": False, "progress": 0},
    {"title": "Set this Sunday — Priority 2",
     "status": False, "progress": 0},
    {"title": "Set this Sunday — Priority 3",
     "status": False, "progress": 0},
]


SKILLS = [
    {"name": "AI Workflows",      "sessions": 15,
     "artifacts": 4,  "level": "Builder",          "progress": 70},
    {"name": "Automation Scripts","sessions": 4,
     "artifacts": 1,  "level": "Beginner",          "progress": 20},
    {"name": "Dashboards",        "sessions": 6,
     "artifacts": 2,  "level": "Intermediate",      "progress": 45},
    {"name": "Research Writing",  "sessions": 20,
     "artifacts": 10, "level": "System Architect",  "progress": 90},
]


_base = 78.5
_weight_dates  = [get_past_date(i) for i in range(60, -1, -1)]
_weight_values = [
    round(_base - ((60 - i) * 0.05) + random.uniform(-0.15, 0.15), 1)
    for i in range(61)
]
WEIGHT_HISTORY = pd.DataFrame({
    "date":   pd.to_datetime(_weight_dates),
    "weight": _weight_values,
})
WEIGHT_GOAL = 72.0


_savings_months = [
    (datetime.now().replace(day=1) - timedelta(days=30 * i)).strftime('%b %Y')
    for i in range(5, -1, -1)
]
_savings_values = [2000, 3500, 4000, 5500, 5000, 3000]
SAVINGS_HISTORY = pd.DataFrame({
    "month":   _savings_months,
    "savings": _savings_values,
})
SAVINGS_GOAL = 50000


IDEAS = [
    {"id": "idea-1", "title": "TNPSC Revision Tracker",
     "stage": "Project Candidate",
     "description": "Streamlit app to log daily subject coverage and auto-flag weak areas."},
    {"id": "idea-2", "title": "Auto-PYQ Extractor",
     "stage": "Researching",
     "description": "Script to parse TNPSC old papers from PDF into structured JSON."},
    {"id": "idea-3", "title": "AI Habit Scoring System",
     "stage": "Captured",
     "description": "LLM-based daily habit evaluator with performance score and feedback."},
    {"id": "idea-4", "title": "Constitutional Amendment Map",
     "stage": "Knowledge Only",
     "description": "Visual timeline of key amendments — Polity study aid."},
    {"id": "idea-5", "title": "Personal Finance Tracker",
     "stage": "Project Candidate",
     "description": "Lightweight expense and savings tracker synced to this dashboard."},
    {"id": "idea-6", "title": "Memory Flashcard App",
     "stage": "Researching",
     "description": "Spaced repetition system using a local LLM to generate and grade cards."},
    {"id": "idea-7", "title": "Agentic Daily Planner",
     "stage": "Captured",
     "description": "AI agent that reads your backlog and builds a prioritised daily plan."},
    {"id": "idea-8", "title": "Nutrition Macro Tracker",
     "stage": "Archived",
     "description": "Log meals and track protein, carbs, fat against daily targets."},
]


MAINS_PAPERS = {
    "Paper II": [
        {"theme_name": "Indian Polity",
         "coverage": 5,  "answer_practice": 0, "confidence": 5},
        {"theme_name": "Science & Technology",
         "coverage": 5,  "answer_practice": 0, "confidence": 5},
        {"theme_name": "Tamil Society",
         "coverage": 10, "answer_practice": 0, "confidence": 8},
    ],
    "Paper III": [
        {"theme_name": "Geography",
         "coverage": 5, "answer_practice": 0, "confidence": 5},
        {"theme_name": "Environment",
         "coverage": 3, "answer_practice": 0, "confidence": 3},
        {"theme_name": "Indian Economy",
         "coverage": 3, "answer_practice": 0, "confidence": 3},
    ],
    "Paper IV": [
        {"theme_name": "Data Interpretation",
         "coverage": 8, "answer_practice": 0, "confidence": 7},
        {"theme_name": "Aptitude",
         "coverage": 5, "answer_practice": 0, "confidence": 4},
        {"theme_name": "Logical Reasoning",
         "coverage": 8, "answer_practice": 0, "confidence": 7},
    ],
}


WEEKLY_SCHEDULE = {
    "Monday": {
        "6:00 AM": "Workout",
        "9:00 AM": "Polity",
        "2:00 PM": "Reading",
        "7:00 PM": "Revision",
    },
    "Tuesday": {
        "6:00 AM": "Workout",
        "9:00 AM": "History",
        "2:00 PM": "Geography",
        "7:00 PM": "Answer Writing",
    },
    "Wednesday": {
        "6:00 AM": "Workout",
        "9:00 AM": "Economy",
        "2:00 PM": "Science",
        "7:00 PM": "Aptitude",
    },
    "Thursday": {
        "6:00 AM": "Workout",
        "9:00 AM": "Tamil Nadu History",
        "2:00 PM": "Environment",
        "7:00 PM": "Revision",
    },
    "Friday": {
        "6:00 AM": "Workout",
        "9:00 AM": "Polity",
        "2:00 PM": "Reading",
        "7:00 PM": "Writing",
    },
    "Saturday": {
        "6:00 AM": "Workout",
        "9:00 AM": "History",
        "2:00 PM": "Tamil Nadu History",
        "7:00 PM": "Revision — Polity",
    },
    "Sunday": {
        "6:00 AM": "Rest",
        "9:00 AM": "Economy",
        "2:00 PM": "Aptitude",
        "7:00 PM": "Weekly Review + Priority Setting",
    },
}
