import streamlit as st
import datetime
from utils import render_safe_html

def apply_chart_theme(fig, is_dark=True):
    text_color = "#EEEEFF" if is_dark else "#0D0D1E"
    grid_color = "#252538" if is_dark else "#D8DAE8"
    
    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(family="Inter", color=text_color, size=12),
        margin=dict(l=0, r=0, t=30, b=0),
        legend=dict(bgcolor="rgba(0,0,0,0)", font=dict(color=text_color, size=11), borderwidth=0)
    )
    fig.update_xaxes(gridcolor=grid_color, linecolor=grid_color, tickfont=dict(color=grid_color, size=11))
    fig.update_yaxes(gridcolor=grid_color, linecolor=grid_color, tickfont=dict(color=grid_color, size=11))
    return fig

def page_header(category_label, title, subtitle, status_text=None, status_color="var(--accent-green)"):
    date_str = datetime.datetime.now().strftime("%B %d, %Y")
    status_html = ""
    if status_text:
        status_html = f"""
        <div style="display: inline-block; background: rgba(45,212,160,0.12); color: {status_color}; padding: 3px 10px; border-radius: 99px; font-size: 11px; font-weight: 600; letter-spacing: 1px; margin-top: 6px;">● {status_text}</div>
        """
        
    html = f"""
    <div style="display: flex; justify-content: space-between; align-items: flex-start; padding: 8px 0 20px 0;">
        <div>
            <div style="font-size: 11px; font-weight: 600; letter-spacing: 3px; color: var(--text-muted); text-transform: uppercase; margin-bottom: 6px;">{category_label}</div>
            <div style="font-size: 26px; font-weight: 700; color: var(--text-primary); letter-spacing: -0.5px; line-height: 1.1;">{title}</div>
            <div style="font-size: 13px; color: var(--text-secondary); margin-top: 4px;">{subtitle}</div>
        </div>
        <div style="text-align: right;">
            <div style="font-size: 12px; color: var(--text-muted);">{date_str}</div>
            {status_html}
        </div>
    </div>
    <div style="height: 1px; background-color: var(--bg-border); width: 100%; margin-bottom: 24px;"></div>
    """
    render_safe_html(html)

def three_column_panel(ratios=[1,1,1]): return st.columns(ratios)
def two_column_panel(ratios=[1,1]): return st.columns(ratios)

def _get_card_style(elevated=False, accent_left=None, accent_top=None):
    bg_var = "var(--bg-elevated)" if elevated else "var(--bg-surface)"
    style = f"background: {bg_var}; border: 1px solid var(--bg-border); border-radius: 14px; padding: 20px 22px; margin-bottom: 12px; box-shadow: 0 1px 3px rgba(0,0,0,0.08), 0 4px 16px rgba(0,0,0,0.06);"
    if accent_left: style += f"border-left: 3px solid var({accent_left}); border-radius: 0 14px 14px 0;"
    if accent_top: style += f"border-top: 3px solid var({accent_top}); border-radius: 0 0 14px 14px;"
    return style

def card_container(content_fn, elevated=False, accent_left=None, accent_top=None):
    style = _get_card_style(elevated, accent_left, accent_top)
    with st.container():
        render_safe_html(f'<div style="{style}">')
        content_fn()
        render_safe_html('</div>')
