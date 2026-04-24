import streamlit as st

def apply_global_css_and_theme(is_dark_mode=True):
    if is_dark_mode:
        vars_css = """
        :root {
            --bg-base: #07070F;
            --bg-surface: #10101C;
            --bg-elevated: #18182A;
            --bg-border: #252538;
            --accent-primary: #7C6FFF;
            --accent-green: #2DD4A0;
            --accent-yellow: #F0A500;
            --accent-red: #F0516A;
            --accent-blue: #4DB8FF;
            --text-primary: #EEEEFF;
            --text-secondary: #8888AA;
            --text-muted: #55556A;
        }
        """
    else:
        vars_css = """
        :root {
            --bg-base: #F5F6FA;
            --bg-surface: #FFFFFF;
            --bg-elevated: #ECEEF6;
            --bg-border: #D8DAE8;
            --accent-primary: #5B50E8;
            --accent-green: #00A878;
            --accent-yellow: #D4900A;
            --accent-red: #D93D56;
            --accent-blue: #2E96D8;
            --text-primary: #0D0D1E;
            --text-secondary: #5C5C7A;
            --text-muted: #9898B0;
        }
        """

    global_css = f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
    
    {vars_css}

    /* Core Toggles and Fonts */
    .stApp, .stApp * {{
        font-family: 'Inter', sans-serif !important;
    }}
    .stApp {{
        background-color: var(--bg-base) !important;
        color: var(--text-primary) !important;
    }}
    
    /* Toolbar Kill Switch */
    header[data-testid="stHeader"] {{
        background: transparent !important;
        height: 0px !important;
    }}
    #MainMenu {{ visibility: hidden; }}
    footer {{ visibility: hidden; }}
    .stDeployButton {{ display: none; }}
    
    /* Native Container Intersect (Provides Box Model to st.container(border=True)) */
    [data-testid="stVerticalBlockBorderWrapper"] {{
        background: var(--bg-surface) !important;
        border: 1px solid var(--bg-border) !important;
        border-radius: 14px !important;
        padding: 6px !important;
        box-shadow: 0 1px 3px rgba(0,0,0,0.08), 0 4px 16px rgba(0,0,0,0.06);
    }}
    
    /* Sidebar Overrides */
    [data-testid="stSidebar"] {{
        background: var(--bg-surface) !important;
        border-right: 1px solid var(--bg-border) !important;
    }}
    [data-testid="stSidebar"] .stRadio > div {{
        gap: 2px !important;
    }}
    [data-testid="stSidebar"] .stRadio label {{
        font-size: 13px !important;
        font-weight: 500 !important;
        color: var(--text-secondary) !important;
        padding: 8px 12px !important;
        border-radius: 8px !important;
        cursor: pointer !important;
        transition: all 0.15s ease !important;
    }}
    [data-testid="stSidebar"] .stRadio label:hover {{
        background: var(--bg-elevated) !important;
        color: var(--text-primary) !important;
    }}
    [data-testid="stSidebar"] .stRadio [data-testid="stMarkdownContainer"] p {{
        font-size: 13px !important;
    }}
    div.stRadio > div[role="radiogroup"] > label[data-checked="true"] {{
        background-color: var(--accent-primary);
    }}
    div.stRadio > div[role="radiogroup"] > label[data-checked="true"] div p {{
        color: white !important;
        font-weight: 600;
    }}

    /* Selectbox Fix for Light Mode vs Dark Mode Integration */
    .stSelectbox > div > div {{
        background: var(--bg-elevated) !important;
        border: 1px solid var(--bg-border) !important;
        border-radius: 8px !important;
        color: var(--text-primary) !important;
        font-size: 12px !important;
    }}
    .stSelectbox > div > div:hover {{
        border-color: var(--accent-primary) !important;
    }}
    
    /* Progress Bar custom classes for semantic colors */
    div[data-testid="stProgressBar"] > div > div {{
        background: linear-gradient(90deg, var(--accent-primary), var(--accent-blue)) !important;
        border-radius: 99px !important;
    }}
    div[data-testid="stProgressBar"] {{
        background: var(--bg-elevated) !important;
        border-radius: 99px !important;
        height: 6px !important;
    }}
    .progress-red div[data-testid="stProgressBar"] > div > div {{ background: var(--accent-red) !important; }}
    .progress-yellow div[data-testid="stProgressBar"] > div > div {{ background: var(--accent-yellow) !important; }}
    .progress-green div[data-testid="stProgressBar"] > div > div {{ background: var(--accent-green) !important; }}

    /* Button System */
    .stButton > button {{
        background: var(--accent-primary) !important;
        color: white !important;
        border: none !important;
        border-radius: 8px !important;
        font-weight: 600 !important;
        font-family: 'Inter', sans-serif !important;
        padding: 8px 20px !important;
        width: 100% !important;
        transition: all 0.2s;
    }}
    .stButton > button:hover {{
        background: var(--accent-blue) !important;
        transform: translateY(-1px);
        box-shadow: 0 4px 12px rgba(108,99,255,0.3) !important;
    }}
    
    /* Hide metrics default box model if exposed */
    div[data-testid="stMetric"] {{
        background: transparent;
        border: none;
    }}
    </style>
    """
    st.markdown(global_css, unsafe_allow_html=True)

def apply_light_theme():
    apply_global_css_and_theme(is_dark_mode=False)

def apply_dark_theme():
    apply_global_css_and_theme(is_dark_mode=True)
