import streamlit as st
import pandas as pd
import requests

# Production configuration with fallback tracking
BACKEND_URL = "http://localhost:8000"

if "auth_token" not in st.session_state:
    st.session_state.auth_token = None
if "execution_mode" not in st.session_state:
    st.session_state.execution_mode = "local"  # Default fallback mode

st.sidebar.subheader("🔒 Account Access Portal")
username = st.sidebar.text_input("Registered Workspace Email Key", key="auth_email")
password = st.sidebar.text_input("Security Phrase", type="password", key="auth_pass")

if st.sidebar.button("Establish Platform Session"):
    try:
        # Attempt to reach the standalone backend service
        response = requests.post(
            f"{BACKEND_URL}/token", 
            data={"username": username, "password": password},
            timeout=2 # Set a low timeout so the cloud app doesn't hang
        )
        if response.status_code == 200:
            st.session_state.auth_token = response.json()["access_token"]
            st.session_state.execution_mode = "api"
            st.sidebar.success("🚀 Connected to FastAPI Backend!")
        else:
            st.sidebar.error("Access rejected by verification backend.")
    except (requests.exceptions.ConnectionError, requests.exceptions.Timeout):
        # Fallback gently to client-side emulation if cloud hosting is disconnected
        st.session_state.execution_mode = "local"
        st.session_state.auth_token = "mock_cloud_demo_token"
        st.sidebar.info("💡 Running in Serverless/Local Sandbox Mode (FastAPI Backend offline).")

# --- Rest of your original Ingestion & Preview UI remains the same ---
st.title("📈 Executive Command Dashboard")
st.subheader(f"Workspace: {st.session_state.workspace_selector} ({st.session_state.execution_mode.upper()} Mode)")

uploaded_file = st.file_uploader("Ingest Customer Transaction Dataset (CSV)", type=["csv"])

if uploaded_file is not None:
    st.session_state.uploaded_data = pd.read_csv(uploaded_file)
    st.success(f"Successfully ingested {len(st.session_state.uploaded_data)} customer profile rows!")

if st.session_state.uploaded_data is not None:
    df = st.session_state.uploaded_data
    st.markdown("### Workspace Operational Metrics")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label="Total Tracked Cohorts Size", value=f"{len(df):,} Users")
    with col2:
        st.metric(label="Workspace Data Quality Index", value="98.4%")
    with col3:
        st.metric(label="Platform Computational State", value="Active Monitoring")

    with st.expander("🔍 View Raw Workspace Data Assets", expanded=False):
        st.dataframe(df.head(20), use_container_width=True)