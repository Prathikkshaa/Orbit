import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

st.set_page_config(page_title="Personal Command Dashboard", layout="wide", initial_sidebar_state="expanded")

from theme import apply_global_css_and_theme
from layout import page_header, three_column_panel, two_column_panel, apply_chart_theme
from components import render_metric_card, render_subject_card, render_theme_card, render_scheduler_grid, render_kanban_board, render_warning_panel
from mock_data import *
from utils import compute_prelims_readiness, compute_mains_readiness, compute_monthly_progress, get_lagging_subjects, compute_habit_score, render_safe_html

if "theme_mode" not in st.session_state: st.session_state.theme_mode = "Dark"
if "weekly_priorities" not in st.session_state: st.session_state.weekly_priorities = WEEKLY_PRIORITIES
if "habit_status" not in st.session_state: st.session_state.habit_status = HABITS
if "scheduler_state" not in st.session_state: st.session_state.scheduler_state = WEEKLY_SCHEDULE
if "idea_pipeline" not in st.session_state: st.session_state.idea_pipeline = IDEAS
if "coverage_values" not in st.session_state: st.session_state.coverage_values = SUBJECTS
if "confidence_values" not in st.session_state: st.session_state.confidence_values = SUBJECTS
if "active_page" not in st.session_state: st.session_state.active_page = "Today Command Panel"

with st.sidebar:
    render_safe_html("""
    <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 8px;">
        <span style="color: var(--accent-primary); font-size: 22px;">⚡</span>
        <div>
            <div style="font-size: 13px; font-weight: 700; color: var(--text-primary); letter-spacing: 2.5px; text-transform: uppercase;">PERSONAL COMMAND</div>
            <div style="font-size: 13px; font-weight: 700; color: var(--text-primary); letter-spacing: 2.5px; text-transform: uppercase;">DASHBOARD</div>
        </div>
    </div>
    <div style="height: 1px; background-color: var(--bg-border); width: 100%; margin-bottom: 12px;"></div>
    """)
    theme_toggle = st.toggle("LIGHT        /        DARK", value=(st.session_state.theme_mode == "Dark"))
    st.session_state.theme_mode = "Dark" if theme_toggle else "Light"
    render_safe_html("""
    <div style="height: 1px; background-color: var(--bg-border); width: 100%; margin-top: 12px; margin-bottom: 16px;"></div>
    <div style="font-size: 10px; color: var(--text-muted); letter-spacing: 3px; font-weight: 600; text-transform: uppercase; margin-bottom: 12px;">NAVIGATE</div>
    """)
    pages = ["Today Command Panel", "TNPSC Prelims Radar", "TNPSC Mains Depth Map", "Skill Builder Engine", "Health + Finance Control", "Idea Pipeline", "Analytics Cockpit", "Calendar Scheduler"]
    page = st.radio("Navigate", pages, index=pages.index(st.session_state.active_page), label_visibility="collapsed")
    st.session_state.active_page = page
    render_safe_html("<br><br><br>")
    render_safe_html("""
    <div style="border-top: 1px solid var(--bg-border); padding-top: 16px; margin-top: auto;">
        <div style="color: var(--text-muted); font-size: 10px; letter-spacing: 2px;">TELEMETRY LINK</div>
        <div style="color: var(--accent-green); font-size: 11px; margin-top: 4px; font-family: monospace;">[SYS] MAINFRAME BOUND</div>
        <div style="color: var(--accent-blue); font-size: 11px; margin-top: 2px; font-family: monospace;">[SYS] SESSION CACHED</div>
    </div>
    """)

is_dark = st.session_state.theme_mode == "Dark"
apply_global_css_and_theme(is_dark_mode=is_dark)

prelims_val = int(compute_prelims_readiness(st.session_state.coverage_values))
mains_val = int(compute_mains_readiness(MAINS_PAPERS))
habit_val = compute_habit_score(st.session_state.habit_status)
focus_subject = st.session_state.scheduler_state.get(datetime.now().strftime("%A"), {}).get("9:00 AM", "Review")

render_safe_html(f"""
<div style="background: var(--bg-elevated); border-bottom: 1px solid var(--bg-border); padding: 12px 24px; display: flex; justify-content: space-between; align-items: center; margin-bottom: 24px;">
    <div style="display: flex; gap: 32px;">
         <div>
             <span style="font-size: 10px; color: var(--text-muted); letter-spacing: 1px; text-transform: uppercase;">ACTIVE FOCUS</span><br>
             <span style="font-size: 13px; font-weight: 600; color: var(--accent-primary);">{focus_subject}</span>
         </div>
         <div>
             <span style="font-size: 10px; color: var(--text-muted); letter-spacing: 1px; text-transform: uppercase;">PRELIMS RED</span><br>
             <span style="font-size: 13px; font-weight: 600; color: var(--text-primary);">{prelims_val}%</span>
         </div>
         <div>
             <span style="font-size: 10px; color: var(--text-muted); letter-spacing: 1px; text-transform: uppercase;">MAINS DEPTH</span><br>
             <span style="font-size: 13px; font-weight: 600; color: var(--text-primary);">{mains_val}%</span>
         </div>
         <div>
             <span style="font-size: 10px; color: var(--text-muted); letter-spacing: 1px; text-transform: uppercase;">HABIT SCORE</span><br>
             <span style="font-size: 13px; font-weight: 600; color: var(--text-primary);">{habit_val}%</span>
         </div>
    </div>
    <div style="font-size: 11px; font-weight: 700; color: var(--accent-green); border: 1px solid var(--accent-green); padding: 4px 12px; border-radius: 99px;">
        EXECUTING
    </div>
</div>
""")

def render_today_panel():
    page_header("EXECUTION SYSTEM", "Today Command Panel", "Execute your daily targets with maximum focus.", "ON TRACK", "var(--accent-green)")
    date_str = datetime.now().strftime("%B %d, %Y")
    day = datetime.now().strftime("%A")
    sched = st.session_state.scheduler_state.get(day, {})
    focus_topic = sched.get("9:00 AM", "Preparation Focus")
    render_safe_html(f"""
    <div style="background: linear-gradient(135deg, var(--bg-elevated) 0%, var(--bg-surface) 100%); border: 1px solid var(--bg-border); border-left: 4px solid var(--accent-primary); border-radius: 0 14px 14px 0; padding: 20px 28px; display: flex; justify-content: space-between; align-items: center; margin-bottom: 24px;">
        <div>
            <div style="font-size: 20px; font-weight: 600; color: var(--text-primary);">Good morning, Prathikkshaa</div>
            <div style="font-size: 13px; color: var(--text-muted); margin-top: 4px;">{date_str}  ·  Day 47 of 365</div>
        </div>
        <div style="position: relative; width: 60px; height: 60px;">
            <svg viewBox="0 0 36 36" style="width: 100%; height: 100%;">
                <path d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831" fill="none" stroke="var(--bg-border)" stroke-width="4"/>
                <path d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831" fill="none" stroke="var(--accent-primary)" stroke-width="4" stroke-dasharray="{habit_val}, 100" />
            </svg>
            <div style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; display: flex; flex-direction: column; align-items: center; justify-content: center;">
                <span style="font-size: 14px; font-weight: 700; color: var(--text-primary); line-height: 1;">{habit_val}%</span>
                <span style="font-size: 9px; color: var(--text-muted); margin-top: 1px;">today</span>
            </div>
        </div>
    </div>
    """)
    col1, col2, col3 = three_column_panel([1.2, 1, 0.9])
    with col1:
        with st.container(border=True):
            render_safe_html(f"""
            <div style="font-size: 10px; color: var(--text-muted); letter-spacing: 2.5px; text-transform: uppercase;">TODAY'S FOCUS</div>
            <div style="margin-top: 12px; margin-bottom: 10px;">
                <span style="background-color: rgba(124, 111, 255, 0.1); color: var(--accent-primary); padding: 4px 12px; border-radius: 99px; font-size: 12px; font-weight: 600;">{day} Plan</span>
            </div>
            <div style="font-size: 18px; font-weight: 600; color: var(--text-primary); margin-bottom: 18px;">{focus_topic}</div>
            <div style="margin-bottom: 14px;">
                <div style="display:flex; justify-content: space-between; margin-bottom: 5px;">
                    <span style="font-size:11px; color:var(--text-muted); letter-spacing:1px; font-weight: 500;">COVERAGE</span>
                    <span style="font-size:11px; font-weight:700; color:var(--accent-red);">38%</span>
                </div>
                <div style="height: 5px; background: var(--bg-elevated); border-radius: 99px;">
                    <div style="width: 38%; height: 100%; background: var(--accent-red); border-radius: 99px;"></div>
                </div>
            </div>
            <div style="margin-bottom: 24px;">
                <div style="display:flex; justify-content: space-between; margin-bottom: 5px;">
                    <span style="font-size:11px; color:var(--text-muted); letter-spacing:1px; font-weight: 500;">CONFIDENCE</span>
                    <span style="font-size:11px; font-weight:700; color:var(--accent-yellow);">45%</span>
                </div>
                <div style="height: 5px; background: var(--bg-elevated); border-radius: 99px;">
                    <div style="width: 45%; height: 100%; background: var(--accent-yellow); border-radius: 99px;"></div>
                </div>
            </div>
            """)
            if st.button("Mark Complete"): pass
    with col2:
        with st.container(border=True):
            render_safe_html('<div style="font-size: 10px; color: var(--text-muted); letter-spacing: 2.5px; text-transform: uppercase; margin-bottom: 16px;">WEEKLY PRIORITIES</div>')
            for i, prio in enumerate(st.session_state.weekly_priorities):
                left_color = "var(--accent-green)" if prio["status"] else "transparent"
                text_color = "var(--text-muted)" if prio["status"] else "var(--text-primary)"
                strikethrough = "text-decoration: line-through;" if prio["status"] else ""
                with st.container():
                    r1, r2 = st.columns([1, 6])
                    with r1: prio["status"] = st.checkbox("Toggle", value=prio["status"], key=f"wp_{i}", label_visibility="collapsed")
                    with r2:
                        render_safe_html(f"""
                        <div style="background: var(--bg-elevated); border-radius: 10px; padding: 12px 14px; margin-bottom: 8px; border-left: 3px solid {left_color};">
                            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
                                <span style="font-size: 13px; font-weight: 500; color: {text_color}; {strikethrough}">{prio['title']}</span>
                                <span style="font-size: 12px; color: var(--text-muted);">{prio['progress']}%</span>
                            </div>
                            <div style="height: 4px; background: var(--bg-border); border-radius: 99px; width: 100%;">
                                <div style="width: {prio['progress']}%; background: var(--accent-primary); height: 100%; border-radius: 99px;"></div>
                            </div>
                        </div>
                        """)
    with col3:
        with st.container(border=True):
            render_safe_html('<div style="font-size: 10px; color: var(--text-muted); letter-spacing: 2.5px; text-transform: uppercase; margin-bottom: 16px;">HABITS</div>')
            for k, v in st.session_state.habit_status.items():
                done = v["done_today"]
                dot_color = "var(--accent-green)" if done else "var(--bg-border)"
                streak_html = f"<div style='color: var(--accent-yellow); font-size: 10px; font-weight: 700; margin-top: 2px;'>{v['streak']} day streak</div>" if v["streak"] > 7 else (f"<div style='color: var(--accent-primary); font-size: 10px; margin-top: 2px;'>{v['streak']} day streak</div>" if v["streak"] > 0 else "<div style='color: var(--text-muted); font-size: 10px; margin-top: 2px;'>Not started</div>")
                with st.container():
                    h1, h2, h3 = st.columns([0.5, 5, 1])
                    with h1: render_safe_html(f"<div style='width: 10px; height: 10px; border-radius: 50%; background-color: {dot_color}; margin-top: 8px;'></div>")
                    with h2:
                        render_safe_html(f"""
                        <div style="background: var(--bg-elevated); border-radius: 10px; padding: 2px 14px; margin-bottom: 8px; display: flex; flex-direction: column; justify-content: center;">
                            <div style='font-size: 13px; font-weight: 500; color: var(--text-primary);'>{k}</div>
                            {streak_html}
                        </div>
                        """)
                    with h3: v["done_today"] = st.checkbox("Habit_checkbox", value=done, key=f"habit_{k}", label_visibility="collapsed")
            
    render_safe_html("<br>")
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        render_safe_html("""
        <div style="background: var(--bg-surface); border: 1px solid var(--bg-border); border-radius: 0 14px 14px 0; border-left: 3px solid var(--accent-primary); padding: 16px 20px; box-shadow: 0 1px 3px rgba(0,0,0,0.08); height: 100%;">
            <div style="color: var(--text-muted); font-size: 9px; letter-spacing: 2px; text-transform: uppercase;">DAILY SIGNAL</div>
            <div style="color: var(--text-secondary); font-size: 12px; font-style: italic; margin-top: 8px;">"Discipline is choosing between what you want now and what you want most."</div>
        </div>
        """)
    with c2:
        render_safe_html("""
        <div style="background: var(--bg-surface); border: 1px solid var(--bg-border); border-radius: 0 14px 14px 0; border-left: 3px solid var(--accent-yellow); padding: 16px 20px; box-shadow: 0 1px 3px rgba(0,0,0,0.08); height: 100%;">
            <div style="color: var(--accent-yellow); font-size: 9px; letter-spacing: 2px; text-transform: uppercase;">CARRY-FORWARD</div>
            <div style="color: var(--text-primary); font-size: 22px; font-weight: 700; margin-top: 4px; letter-spacing: -1px;">2 tasks</div>
            <div style="color: var(--text-muted); font-size: 11px; margin-top: 2px;">from yesterday</div>
        </div>
        """)
    with c3:
        render_safe_html("""
        <div style="background: var(--bg-surface); border: 1px solid var(--bg-border); border-radius: 0 14px 14px 0; border-left: 3px solid var(--accent-red); padding: 16px 20px; box-shadow: 0 1px 3px rgba(0,0,0,0.08); height: 100%;">
            <div style="color: var(--accent-red); font-size: 9px; letter-spacing: 2px; text-transform: uppercase;">MISSED</div>
            <div style="color: var(--text-primary); font-size: 16px; font-weight: 700; margin-top: 4px;">Aptitude</div>
            <div style="color: var(--accent-red); font-size: 11px; margin-top: 2px;">skipped 3 days</div>
        </div>
        """)
    with c4:
        render_safe_html("""
        <div style="background: var(--bg-surface); border: 1px solid var(--bg-border); border-radius: 0 14px 14px 0; border-left: 3px solid var(--accent-green); padding: 16px 20px; box-shadow: 0 1px 3px rgba(0,0,0,0.08); height: 100%;">
            <div style="color: var(--text-muted); font-size: 9px; letter-spacing: 2px; text-transform: uppercase; margin-bottom: 8px;">FOCUS ENERGY</div>
            <div style="height: 5px; background: var(--bg-elevated); border-radius: 99px; width: 100%;">
                <div style="width: 72%; background: var(--accent-green); height: 100%; border-radius: 99px;"></div>
            </div>
            <div style="color: var(--accent-green); font-size: 11px; font-weight: 600; margin-top: 8px;">72% charged</div>
        </div>
        """)

def render_prelims_radar():
    page_header("TNPSC EXAM SYSTEM", "Prelims Radar", "Complete coverage visibility and weakness spotting.", "ACTIVE TRACK", "var(--accent-blue)")
    cols = st.columns(4)
    for i, (sub, data) in enumerate(st.session_state.coverage_values.items()):
        with cols[i % 4]: render_subject_card(sub, data)
    render_safe_html("<br><div style='font-size: 15px; font-weight: 700; color: var(--text-primary); margin-bottom: 16px;'>Overall Prelims Readiness</div>")
    
    overall = compute_prelims_readiness(st.session_state.coverage_values)
    accent_primary_hex = "#7C6FFF" if is_dark else "#5B50E8"
    accent_green_hex = "#2DD4A0" if is_dark else "#00A878"
    bg_elevated_hex = "#18182A" if is_dark else "#ECEEF6"
    text_primary_hex = "#EEEEFF" if is_dark else "#0D0D1E"
    text_secondary_hex = "#8888AA" if is_dark else "#5C5C7A"
    c_red = "#F0516A" if is_dark else "#D93D56"
    c_yellow = "#F0A500" if is_dark else "#D4900A"
    c_green = "#2DD4A0" if is_dark else "#00A878"

    def rgba(hex_color, alpha):
        h = hex_color.lstrip('#')
        return f"rgba({int(h[0:2], 16)},{int(h[2:4], 16)},{int(h[4:6], 16)},{alpha})"
        
    fig = go.Figure(go.Indicator(
        mode = "gauge+number", value = overall,
        gauge = dict(
            axis = dict(range=[0,100], tickcolor=text_secondary_hex, tickfont=dict(size=11, color=text_secondary_hex)),
            bar = dict(color=accent_primary_hex, thickness=0.7), bgcolor = bg_elevated_hex, borderwidth = 0,
            steps = [dict(range=[0,40], color=rgba(c_red, 0.15)), dict(range=[40,70], color=rgba(c_yellow, 0.15)), dict(range=[70,100], color=rgba(c_green, 0.15))],
            threshold = dict(line=dict(color=accent_green_hex, width=2), thickness=0.8, value=70)
        ), number = dict(font=dict(size=42, color=text_primary_hex, family="Inter"), suffix="%")
    ))
    fig.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)", height=320, margin=dict(l=0, r=0, t=10, b=10))
    st.plotly_chart(fig, use_container_width=True)

def render_mains_depth_map():
    page_header("TNPSC EXAM SYSTEM", "Mains Depth Map", "Analyze answer writing depth and thematic confidence.")
    for paper, themes in MAINS_PAPERS.items():
        theme_cnt = len(themes)
        avg_conf = int(sum(t["confidence"] for t in themes) / theme_cnt) if theme_cnt else 0
        render_safe_html(f"""
        <div style="background: var(--bg-elevated); border: 1px solid var(--bg-border); border-radius: 10px; padding: 12px 18px; margin: 16px 0 12px 0; display: flex; align-items: center; gap: 10px;">
            <div style="width: 8px; height: 8px; background: var(--accent-primary); border-radius: 50%;"></div>
            <span style="font-size: 13px; font-weight: 600; color: var(--text-primary); letter-spacing: 1px;">{paper}</span>
            <span style="font-size: 11px; color: var(--text-muted); margin-left: auto;">{theme_cnt} themes · Avg confidence {avg_conf}%</span>
        </div>
        """)
        cols = st.columns(3)
        for i, theme in enumerate(themes):
            with cols[i % 3]: render_theme_card(theme["theme_name"], theme)
                    
    render_safe_html("<br><div style='font-size: 15px; font-weight: 700; color: var(--text-primary); margin-bottom: 16px;'>Mains Readiness by Paper</div>")
    avg_conf_dict = {paper: sum(t["confidence"] for t in themes) / len(themes) if themes else 0 for paper, themes in MAINS_PAPERS.items()}
    df = pd.DataFrame({"Paper": list(avg_conf_dict.keys()), "Confidence": list(avg_conf_dict.values())})
    color_map = {p: ("#F0516A" if val < 40 else "#F0A500" if val < 70 else "#2DD4A0") if is_dark else ("#D93D56" if val < 40 else "#D4900A" if val < 70 else "#00A878") for p, val in avg_conf_dict.items()}
    df["Color"] = df["Paper"].map(color_map)
    fig = px.bar(df, x="Confidence", y="Paper", orientation='h', color="Paper", color_discrete_map=color_map)
    fig.update_layout(xaxis_range=[0, 100], height=220, showlegend=False)
    fig.update_traces(marker_line_width=0)
    st.plotly_chart(apply_chart_theme(fig, is_dark), use_container_width=True)

def render_skill_engine():
    page_header("LEARNING VECTORS", "Skill Builder Engine", "Tracking technical proficiency and velocity.", "LEARNING", "var(--accent-primary)")
    c1, c2 = st.columns(2)
    for i, skill in enumerate(SKILLS):
        df = pd.DataFrame({"Metric": ["Progress"], "Value": [skill["progress"]]})
        fig = px.bar(df, x="Value", y="Metric", orientation='h', color_discrete_sequence=[("#7C6FFF" if is_dark else "#5B50E8")])
        fig.update_layout(xaxis_range=[0, 100], height=120, margin=dict(l=0, r=0, t=0, b=0), showlegend=False, xaxis_title=None, yaxis_title=None, yaxis_showticklabels=False)
        with c1 if i % 2 == 0 else c2:
            with st.container(border=True):
                render_safe_html(f"""
                <div style="display:flex; justify-content:space-between; align-items:center;">
                    <div style="font-size:16px; font-weight:700; color:var(--text-primary);">{skill['name']}</div>
                    <div style="font-size:16px; font-weight:700; color:var(--accent-primary);">{skill['progress']}%</div>
                </div>
                <div style="font-size:12px; color:var(--text-muted); margin-bottom:0px;">{skill['level']} · {skill['sessions']} sessions · {skill['artifacts']} artifacts</div>
                """)
                st.plotly_chart(apply_chart_theme(fig, is_dark), use_container_width=True, key=f"skill_{i}")

def render_health_finance():
    page_header("PERSONAL CONTROL", "Health + Finance", "Vital tracking for sustained performance.")
    col1, col2 = two_column_panel()
    with col1:
        fig = px.line(WEIGHT_HISTORY, x="date", y="weight")
        c_prim = "#7C6FFF" if is_dark else "#5B50E8"
        fig.update_traces(line_color=c_prim, line_width=2.5, fill='tozeroy', fillcolor=f'rgba({int(c_prim.lstrip("#")[0:2],16)},{int(c_prim.lstrip("#")[2:4],16)},{int(c_prim.lstrip("#")[4:6],16)},0.08)')
        fig.add_hline(y=WEIGHT_GOAL, line_dash="dash", line_color=("#2DD4A0" if is_dark else "#00A878"), annotation_text=f"Target: {WEIGHT_GOAL} kg")
        st.plotly_chart(apply_chart_theme(fig, is_dark), use_container_width=True)
    with col2:
        x = np.array(range(len(SAVINGS_HISTORY)))
        m, c = np.polyfit(x, np.array(SAVINGS_HISTORY["savings"]), 1)
        future_x = np.array([len(x), len(x)+1, len(x)+2])
        future_months = [(datetime.now().replace(day=1) + timedelta(days=30*i)).strftime('%b %Y') for i in range(1, 4)]
        fig = go.Figure()
        fig.add_trace(go.Bar(x=SAVINGS_HISTORY["month"], y=SAVINGS_HISTORY["savings"], marker_color=("#7C6FFF" if is_dark else "#5B50E8"), name="Actual"))
        fig.add_trace(go.Scatter(x=future_months, y=(m * future_x + c), mode="lines+markers", line=dict(color="#F0A500", dash="dash"), name="Projection"))
        fig.add_hline(y=SAVINGS_GOAL, line_dash="dash", line_color=("#2DD4A0" if is_dark else "#00A878"), annotation_text="Goal")
        st.plotly_chart(apply_chart_theme(fig, is_dark), use_container_width=True)

def render_idea_pipeline():
    page_header("KNOWLEDGE HUB", "Idea Pipeline", "Convert floating thoughts into execution-ready specs.")
    st.session_state.idea_pipeline = render_kanban_board(st.session_state.idea_pipeline)

def render_analytics_cockpit():
    page_header("STRATEGIC LAYER", "Analytics Cockpit", "Strategic oversight of all learning vectors.", "DATA LIVE", "var(--accent-blue)")
    subjects = st.session_state.coverage_values
    render_safe_html(f"""
    <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 16px; margin-bottom: 24px;">
        {render_metric_card("PRELIMS READINESS", f"{int(compute_prelims_readiness(subjects))}%", "Avg Coverage", "accent-primary")}
        {render_metric_card("MAINS READINESS", f"{int(compute_mains_readiness(MAINS_PAPERS))}%", "Avg Confidence", "accent-blue")}
        {render_metric_card("MONTHLY VELOCITY", f"+{compute_monthly_progress()}%", "vs Last Month", "accent-green")}
        {render_metric_card("LAGGING SUBJECTS", str(len(get_lagging_subjects(subjects))), "Coverage < 40%", "accent-red")}
    </div>
    """)
    lagging_subs = get_lagging_subjects(subjects)
    render_warning_panel([f"Low metrics in {s}" for s in lagging_subs], subjects)

def render_scheduler():
    page_header("TIME ALLOCATION", "Calendar Scheduler", "Design your weekly time allocation blocks.", "LOCKED", "var(--accent-yellow)")
    st.session_state.scheduler_state = render_scheduler_grid(st.session_state.scheduler_state)

if st.session_state.active_page == "Today Command Panel": render_today_panel()
elif st.session_state.active_page == "TNPSC Prelims Radar": render_prelims_radar()
elif st.session_state.active_page == "TNPSC Mains Depth Map": render_mains_depth_map()
elif st.session_state.active_page == "Skill Builder Engine": render_skill_engine()
elif st.session_state.active_page == "Health + Finance Control": render_health_finance()
elif st.session_state.active_page == "Idea Pipeline": render_idea_pipeline()
elif st.session_state.active_page == "Analytics Cockpit": render_analytics_cockpit()
elif st.session_state.active_page == "Calendar Scheduler": render_scheduler()
