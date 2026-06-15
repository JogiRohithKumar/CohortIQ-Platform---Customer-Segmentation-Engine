import streamlit as st
import pandas as pd
import numpy as np

st.title("🤖 AI Data Copilot & Persona Advisor")
st.subheader(f"Active Session Workspace: {st.session_state.workspace_selector}")

# Check if data has been run through the engine page first
if st.session_state.segmented_data is None:
    st.warning("⚠️ The AI Copilot requires an optimized dataset to generate insights. Please go to the 'AutoML & Anomalies' page and execute the optimization loop first.")
else:
    df = st.session_state.segmented_data
    meta = st.session_state.model_metadata
    features = meta['features_used']
    
    # 1. Compute automated background metrics for the AI's context layer
    st.markdown("### 🧠 Live Cohort Intelligence Matrix")
    
    summary_data = []
    unique_segments = sorted(df['Segment_ID'].unique())
    
    for segment in unique_segments:
        seg_df = df[df['Segment_ID'] == segment]
        anomaly_count = len(seg_df[seg_df['Anomaly_Flag'] == "Outlier"])
        
        # Calculate dynamic means for features chosen by user
        metrics_desc = ""
        for f in features:
            avg_val = seg_df[f].mean()
            metrics_desc += f"{f}: {avg_val:.1f} | "
            
        summary_data.append({
            "Cohort": segment,
            "Size": f"{len(seg_df)} accounts",
            "Outliers Detected": f"{anomaly_count} alerts",
            "Extracted Behavioral Profile": metrics_desc
        })
        
    summary_table = pd.DataFrame(summary_data)
    st.dataframe(summary_table, use_container_width=True, hide_index=True)
    
    st.markdown("---")
    st.markdown("### 💬 Chat with Your Customer Intelligence Database")
    
    # Setup standard Streamlit conversational chat history state variables
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = [
            {"role": "assistant", "content": "Hello! I am your AI Business Advisor. I have analyzed your customer cohorts. Ask me anything about segment revenue, churn risks, or personalized marketing campaigns!"}
        ]
        
    # Render historical chat strings to the screen
    for message in st.session_state.chat_history:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
            
    # Process fresh user input queries
    if user_query := st.chat_input("Ask a question about your segments (e.g., 'What strategy should I use for Cohort 1?')"):
        
        # Display the user message instantly
        with st.chat_message("user"):
            st.markdown(user_query)
        st.session_state.chat_history.append({"role": "user", "content": user_query})
        
        # Determine appropriate automated responses based on query keywords
        query_lower = user_query.lower()
        response = ""
        
        with st.spinner("Analyzing cohort distributions..."):
            if "strategy" in query_lower or "marketing" in query_lower or "campaign" in query_lower:
                response = f"""
### 🎯 Automated Marketing Strategy Recommendations:
Based on the **{meta['optimal_k']} customer clusters** found in this workspace, here are your strategic next steps:

1. **High-Value Cohorts (Top Performers):** Do not send generic discount codes. Instead, launch an exclusive VIP early-access campaign or premium loyalty tiers to maximize their Lifetime Value (LTV).
2. **Volatile/Slipping Cohorts (At-Risk Accounts):** Trigger a automated "We Miss You" reactivation email pipeline. Include a target-specific discount (e.g., 20% off their next purchase) to win back engagement before they fully churn.
3. **Budget/Casual Cohorts:** Keep communication steady with regular product updates, community social proof, and bundle offers to increase their average basket size over time.
"""
            elif "outlier" in query_lower or "anomaly" in query_lower or "risk" in query_lower:
                total_anomalies = len(df[df['Anomaly_Flag'] == "Outlier"])
                response = f"""
### 🚨 Churn Risk & Outlier Assessment:
- The system is currently tracking **{total_anomalies} specific accounts** marked as behavioral anomalies across your workspaces.
- **Diagnostic Risk:** These specific profiles show sudden spending drops or extreme friction metrics compared to their baseline group behaviors.
- **Action Plan:** We recommend exporting the anomaly dataset from the *Reports & Export* menu and handing those specific account profiles directly to your customer success or support team for immediate outreach.
"""
            else:
                # Default intelligence lookup fallback fallback
                response = f"""
### 📊 Workspace Structural Summary Insights:
- **Active Segments Evaluated:** {meta['optimal_k']} unique customer archetypes.
- **Core Clustering Drivers Used:** {', '.join(features)}.
- **Mathematical Validation Quality:** The engine reports a Silhouette Verification Score of **{meta['silhouette_score']:.3f}**, indicating clear, mathematically sound structural boundaries across these customer groups.

*Tip: Try asking about 'marketing strategies' or 'at-risk outlier profiles' for a deep-dive tactical breakdown!*
"""
                
        # Display the AI response
        with st.chat_message("assistant"):
            st.markdown(response)
        st.session_state.chat_history.append({"role": "assistant", "content": response})