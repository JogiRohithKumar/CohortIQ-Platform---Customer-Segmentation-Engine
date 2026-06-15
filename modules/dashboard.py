import streamlit as st
import requests

BACKEND_URL = "http://localhost:8000" # Target localized container address

# Example UI Authentication Login State Routine
if "auth_token" not in st.session_state:
    st.session_state.auth_token = None

st.sidebar.subheader("🔒 Account Access Portal")
username = st.sidebar.text_input("Registered Workspace Email Key")
password = st.sidebar.text_input("Security Phrase", type="password")

if st.sidebar.button("Establish Platform Session"):
    response = requests.post(f"{BACKEND_URL}/token", data={"username": username, "password": password})
    if response.status_code == 200:
        st.session_state.auth_token = response.json()["access_token"]
        st.sidebar.success("JWT Token Extracted & Attached!")
    else:
        st.sidebar.error("Access rejected by verification backend.")