import streamlit as st
import pandas as pd

# 1. Platform Configuration & Page Styling
st.set_page_config(
    page_title="CohortIQ Platform",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Mock Multi-Tenant / Multi-Workspace State Initialization
if "current_workspace" not in st.session_state:
    st.session_state.current_workspace = "E-Commerce Main Store"
if "uploaded_data" not in st.session_state:
    st.session_state.uploaded_data = None
if "segmented_data" not in st.session_state:
    st.session_state.segmented_data = None
if "model_metadata" not in st.session_state:
    st.session_state.model_metadata = {}

# 3. Sidebar Workspace Controller Widget
st.sidebar.title("🏢 CohortIQ Workspaces")
selected_workspace = st.sidebar.selectbox(
    "Active Environment",
    ["E-Commerce Main Store", "B2B Wholesale Portal", "Retail Sandbox (Demo)"],
    key="workspace_selector"
)
st.sidebar.markdown("---")

# 4. Declarative Native Streamlit Page Navigation
pages = {
    "Operational Overview": [
        st.Page("modules/dashboard.py", title="Executive Dashboard", icon="📈"),
    ],
    "Analytics Engines": [
        st.Page("modules/engine.py", title="AutoML & Anomalies", icon="🧬"),
    ],
    "Decision Support": [
        st.Page("modules/advisor.py", title="AI Data Copilot", icon="🤖"),
        st.Page("modules/export.py", title="Reports & Export", icon="📥"),
    ]
}

# Run navigation routing
pg = st.navigation(pages)
pg.run()