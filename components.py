import streamlit as st
import datetime
from utils import render_safe_html

def get_color_class(val):
    if val < 40: return "accent-red"
    if val < 70: return "accent-yellow"
    return "accent-green"

def render_metric_card(title, value, subtitle, accent_color="accent-primary"):
    return f"""
    <div style="background: var(--bg-surface); border: 1px solid var(--bg-border); border-radius: 14px; padding: 18px 20px; border-top: 3px solid var(--{accent_color});">
        <div style="font-size: 10px; font-weight: 600; letter-spacing: 2px; color: var(--text-muted); text-transform: uppercase; margin-bottom: 8px;">{title}</div>
        <div style="font-size: 32px; font-weight: 700; color: var(--text-primary); letter-spacing: -1px; line-height: 1;">{value}</div>
        <div style="font-size: 11px; color: var(--text-secondary); margin-top: 6px;">{subtitle}</div>
    </div>
    """

def render_subject_card(subject_name, subject_data):
    cov = subject_data.get('coverage', 0)
    pyq = subject_data.get('pyq_coverage', 0)
    conf = subject_data.get('confidence', 0)
    revs = subject_data.get('revision_count', 0)
    accentv = get_color_class(cov)
    
    html = f"""
    <div style="background: var(--bg-surface); border: 1px solid var(--bg-border); border-radius: 14px; padding: 20px 22px; margin-bottom: 12px; border-top: 3px solid var(--{accentv}); box-shadow: 0 1px 3px rgba(0,0,0,0.08), 0 4px 16px rgba(0,0,0,0.06);">
        <div style="font-size: 15px; font-weight: 700; color: var(--text-primary); margin-bottom: 16px; display: flex; justify-content: space-between;">
            {subject_name}
            <span style="background: var(--bg-elevated); color: var(--text-muted); font-size: 10px; padding: 2px 8px; border-radius: 99px;">{revs} revisions</span>
        </div>
        <div style="margin-bottom: 14px;">
            <div style="display:flex; justify-content: space-between; margin-bottom: 5px;">
                <span style="font-size:11px; color:var(--text-muted); letter-spacing:1px; font-weight: 500;">COVERAGE</span>
                <span style="font-size:11px; font-weight:700; color:var(--{get_color_class(cov)});">{cov}%</span>
            </div>
            <div style="height: 5px; background: var(--bg-elevated); border-radius: 99px;">
                <div style="width: {cov}%; height: 100%; background: var(--{get_color_class(cov)}); border-radius: 99px;"></div>
            </div>
        </div>
        <div style="margin-bottom: 14px;">
            <div style="display:flex; justify-content: space-between; margin-bottom: 5px;">
                <span style="font-size:11px; color:var(--text-muted); letter-spacing:1px; font-weight: 500;">PYQ COVERAGE</span>
                <span style="font-size:11px; font-weight:700; color:var(--{get_color_class(pyq)});">{pyq}%</span>
            </div>
            <div style="height: 5px; background: var(--bg-elevated); border-radius: 99px;">
                <div style="width: {pyq}%; height: 100%; background: var(--{get_color_class(pyq)}); border-radius: 99px;"></div>
            </div>
        </div>
        <div style="margin-bottom: 16px;">
            <div style="display:flex; justify-content: space-between; margin-bottom: 5px;">
                <span style="font-size:11px; color:var(--text-muted); letter-spacing:1px; font-weight: 500;">CONFIDENCE</span>
                <span style="font-size:11px; font-weight:700; color:var(--{get_color_class(conf)});">{conf}%</span>
            </div>
            <div style="height: 5px; background: var(--bg-elevated); border-radius: 99px;">
                <div style="width: {conf}%; height: 100%; background: var(--{get_color_class(conf)}); border-radius: 99px;"></div>
            </div>
        </div>
        <div style="text-align: center; width: 100%;">
            <span style="background-color: rgba(var(--{accentv}-rgb), 0.1); color: var(--{accentv}); padding: 4px 12px; border-radius: 99px; font-size: 10px; font-weight: 700; text-transform: uppercase;">{'STRONG' if cov >= 70 else 'MODERATE' if cov >= 40 else 'WEAK'}</span>
        </div>
    </div>
    """
    render_safe_html(html)

def render_theme_card(theme_name, theme_data):
    cov = theme_data.get('coverage', 0)
    conf = theme_data.get('confidence', 0)
    prac = theme_data.get('answer_practice', 0)
    border_left = "border-left: 3px solid var(--accent-red);" if conf < 40 else ""
    weak_pill = f'<div style="margin-top: 12px; text-align: left;"><span style="background-color: rgba(240, 81, 106, 0.1); color: var(--accent-red); padding: 3px 10px; border-radius: 99px; font-size: 10px; font-weight: 700;">WEAK</span></div>' if conf < 40 else ''
    
    html = f"""
    <div style="background: var(--bg-surface); border: 1px solid var(--bg-border); {border_left} border-radius: 14px; padding: 20px 22px; margin-bottom: 12px; box-shadow: 0 1px 3px rgba(0,0,0,0.08), 0 4px 16px rgba(0,0,0,0.06);">
        <div style="font-size: 14px; font-weight: 700; color: var(--text-primary); margin-bottom: 16px;">{theme_name}</div>
        <div style="margin-bottom: 14px;">
            <div style="display:flex; justify-content: space-between; margin-bottom: 5px;">
                <span style="font-size:11px; color:var(--text-muted); letter-spacing:1px; font-weight: 500;">COVERAGE</span>
                <span style="font-size:11px; font-weight:700; color:var(--{get_color_class(cov)});">{cov}%</span>
            </div>
            <div style="height: 5px; background: var(--bg-elevated); border-radius: 99px;">
                <div style="width: {cov}%; height: 100%; background: var(--{get_color_class(cov)}); border-radius: 99px;"></div>
            </div>
        </div>
        <div style="margin-bottom: 14px;">
            <div style="display:flex; justify-content: space-between; margin-bottom: 5px;">
                <span style="font-size:11px; color:var(--text-muted); letter-spacing:1px; font-weight: 500;">CONFIDENCE</span>
                <span style="font-size:11px; font-weight:700; color:var(--{get_color_class(conf)});">{conf}%</span>
            </div>
            <div style="height: 5px; background: var(--bg-elevated); border-radius: 99px;">
                <div style="width: {conf}%; height: 100%; background: var(--{get_color_class(conf)}); border-radius: 99px;"></div>
            </div>
        </div>
        <div style="margin-top: 16px;">
            <span style="font-size: 22px; font-weight: 700; color: var(--text-primary);">{prac}</span>
            <span style="font-size: 11px; color: var(--text-muted);"> answers written</span>
        </div>
        {weak_pill}
    </div>
    """
    render_safe_html(html)

def render_scheduler_grid(schedule_dict):
    updated_schedule = {}
    days = list(schedule_dict.keys())
    cols = st.columns(7)
    time_slots = ["6:00 AM", "9:00 AM", "2:00 PM", "7:00 PM"]
    subjects_pool = ["Polity", "History", "Geography", "Economy", "Science", "Environment", "Tamil Nadu History", "Aptitude", "Workout", "Reading", "Writing", "Break", "Revision", "Current Affairs", "Answer Writing", "Essay Writing", "Mock Test", "Review Mock", "Weak Areas", "Planning", "Comprehensive Revision", "Aptitude Practice"]
    str_date = datetime.datetime.now().strftime("%b %d")
    
    for i, col in enumerate(cols):
        day = days[i]
        updated_schedule[day] = {}
        with col:
            bg_css = "background: rgba(124,111,255,0.06); border-radius: 10px 10px 0 0;" if day in ["Saturday", "Sunday"] else ""
            render_safe_html(f"""
            <div style="text-align: center; padding: 8px 4px 12px 4px; border-bottom: 2px solid var(--bg-border); margin-bottom: 8px; {bg_css}">
                <div style="font-size: 11px; font-weight: 700; letter-spacing: 2px; color: var(--text-secondary); text-transform: uppercase;">{day[:3]}</div>
                <div style="font-size: 10px; color: var(--text-muted); margin-top: 2px;">{str_date}</div>
            </div>
            """)
            for slot in time_slots:
                current_val = schedule_dict[day].get(slot, "Break")
                if current_val not in subjects_pool: subjects_pool.append(current_val)
                render_safe_html(f'<div style="font-size: 10px; color: var(--text-muted); letter-spacing: 1px; margin-bottom: 2px;">{slot}</div>')
                val = st.selectbox(label="hidden_slot", options=subjects_pool, index=subjects_pool.index(current_val), key=f"{day}_{slot}", label_visibility="collapsed")
                updated_schedule[day][slot] = val
    return updated_schedule

def render_kanban_board(ideas_list):
    stages = ["Captured", "Researching", "Project Candidate", "Knowledge Only", "Archived"]
    cols = st.columns(5)
    for i, stage in enumerate(stages):
        with cols[i]:
            stage_ideas = [idea for idea in ideas_list if idea['stage'] == stage]
            render_safe_html(f"""
            <div style="font-size: 12px; font-weight: 700; color: var(--text-secondary); letter-spacing: 2px; text-transform: uppercase; padding: 0 0 10px 0; border-bottom: 2px solid var(--bg-border); margin-bottom: 12px;">
                {stage.upper()} <span style="font-size: 11px; color: var(--text-muted); font-weight: 400;">({len(stage_ideas)})</span>
            </div>
            """)
            for idea in stage_ideas:
                with st.container():
                    render_safe_html(f'''
                    <div style="background: var(--bg-surface); border: 1px solid var(--bg-border); border-radius: 12px; padding: 14px 16px; margin-bottom: 4px;">
                        <div style="font-size: 13px; font-weight: 600; color: var(--text-primary); margin-bottom: 4px;">{idea["title"]}</div>
                        <div style="font-size: 11px; color: var(--text-secondary); line-height: 1.4;">{idea["description"][:60]}...</div>
                    </div>
                    ''')
                    new_stage = st.selectbox(label="hidden_stage", options=stages, index=stages.index(idea["stage"]), key=f"idea_{idea['id']}", label_visibility="collapsed")
                    idea['stage'] = new_stage
    return ideas_list

def render_warning_panel(warnings_list, subjects):
    if not warnings_list: return
    html = f"""
    <div style="background: var(--bg-surface); border: 1px solid var(--bg-border); border-radius: 14px; padding: 18px 20px;">
        <div style="font-size: 12px; font-weight: 600; color: var(--text-muted); letter-spacing: 2px; text-transform: uppercase; margin-bottom: 14px;">ATTENTION REQUIRED</div>
    """
    for warning in warnings_list:
        sub = warning.split("in ")[-1] if "in " in warning else warning
        data = subjects.get(sub, {"coverage": 100, "confidence": 100})
        cov = data["coverage"]
        conf = data["confidence"]
        severity_color = "var(--accent-red)" if cov < 30 and conf < 30 else ("var(--accent-yellow)" if cov < 40 or conf < 40 else "var(--accent-blue)")
        severity_val = "CRITICAL" if cov < 30 and conf < 30 else ("REVIEW" if cov < 40 or conf < 40 else "LOW")
        
        html += f"""
        <div style="display: flex; align-items: center; padding: 10px 12px; background: var(--bg-elevated); border-radius: 8px; margin-bottom: 6px; border-left: 3px solid {severity_color};">
            <div style="flex: 1;">
                <span style="font-size: 13px; font-weight: 600; color: var(--text-primary);">{sub}</span>
                <span style="font-size: 11px; color: var(--text-secondary); margin-left: 8px;">Coverage {cov}% · Confidence {conf}%</span>
            </div>
            <div style="font-size: 10px; font-weight: 700; letter-spacing: 1px; color: {severity_color}; text-transform: uppercase;">
                {severity_val}
            </div>
        </div>
        """
    html += "</div>"
    render_safe_html(html)
