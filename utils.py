import streamlit as st

def render_safe_html(html_str):
    cleaned = "\n".join([line.lstrip() for line in html_str.split('\n')])
    st.markdown(cleaned, unsafe_allow_html=True)

def compute_prelims_readiness(subjects_data):
    if not subjects_data: return 0
    total_coverage = sum([data.get("coverage", 0) for data in subjects_data.values()])
    return total_coverage / len(subjects_data)

def compute_mains_readiness(mains_papers_data):
    if not mains_papers_data: return 0
    total_confidence = 0
    count = 0
    for paper in mains_papers_data.values():
        for theme in paper:
            total_confidence += theme.get("confidence", 0)
            count += 1
    return total_confidence / count if count > 0 else 0

def compute_monthly_progress():
    return 6.5

def get_lagging_subjects(subjects_data):
    return [name for name, data in subjects_data.items() if data.get("coverage", 0) < 40 or data.get("confidence", 0) < 40]

def compute_habit_score(habit_dict):
    if not habit_dict: return 0
    done = sum(1 for v in habit_dict.values() if v.get("done_today"))
    return int((done / len(habit_dict)) * 100)
