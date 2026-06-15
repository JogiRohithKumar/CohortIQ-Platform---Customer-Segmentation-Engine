import streamlit as st
import pandas as pd
import numpy as np

st.title("🤖 AI Data Copilot & Persona Advisor")
st.subheader(f"Active Session Workspace: {st.session_state.workspace_selector}")

if st.session_state.segmented_data is None:
    st.warning("⚠️ The AI Copilot requires an optimized dataset to generate insights. Please go to the 'AutoML & Anomalies' page and execute the optimization loop first.")
else:
    df = st.session_state.segmented_data
    meta = st.session_state.model_metadata
    features = meta['features_used']
    
    # Render the Cohort Intelligence Matrix
    st.markdown("### 🧠 Live Cohort Intelligence Matrix")
    summary_data = []
    unique_segments = sorted(df['Segment_ID'].unique())
    
    for segment in unique_segments:
        seg_df = df[df['Segment_ID'] == segment]
        anomaly_count = len(seg_df[seg_df['Anomaly_Flag'] == "Outlier"])
        
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
        
    st.dataframe(pd.DataFrame(summary_data), use_container_width=True, hide_index=True)
    st.markdown("---")
    st.markdown("### 💬 Chat with Your Customer Intelligence Database")
    
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = [
            {"role": "assistant", "content": "Hello! I am your interactive data copilot. Ask me specific questions like 'Which segment is the largest?', 'How many outliers do we have?', or 'Give me a strategy for Cohort 1'."}
        ]
        
    for message in st.session_state.chat_history:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
            
    if user_query := st.chat_input("Ask a question about your customer data..."):
        with st.chat_message("user"):
            st.markdown(user_query)
        st.session_state.chat_history.append({"role": "user", "content": user_query})
        
        query_lower = user_query.lower()
        response = ""
        
        with st.spinner("Executing analytical memory queries..."):
            
            # CRITICAL FEATURE: Dynamic Largest Segment Query
            if "largest" in query_lower or "biggest" in query_lower or "most customers" in query_lower:
                largest_seg = df['Segment_ID'].value_counts().idxmax()
                largest_count = df['Segment_ID'].value_counts().max()
                pct = (largest_count / len(df)) * 100
                response = f"📊 **Data Copilot Analysis:** The largest cohort in your current dataset is **{largest_seg}** containing **{largest_count:,} customers**. This single segment represents **{pct:.1f}%** of your total tracked customer database base."
            
            # CRITICAL FEATURE: Dynamic Smallest Segment Query
            elif "smallest" in query_lower or "tiniest" in query_lower or "least customers" in query_lower:
                smallest_seg = df['Segment_ID'].value_counts().idxmin()
                smallest_count = df['Segment_ID'].value_counts().min()
                pct = (smallest_count / len(df)) * 100
                response = f"📊 **Data Copilot Analysis:** The smallest cohort identified is **{smallest_seg}** with **{smallest_count:,} customers** (**{pct:.1f}%** of workspace share)."
            
            # CRITICAL FEATURE: Dynamic Outlier / Churn Risk Counter Query
            elif "outlier" in query_lower or "anomaly" in query_lower or "churn" in query_lower:
                total_anomalies = len(df[df['Anomaly_Flag'] == "Outlier"])
                anomaly_pct = (total_anomalies / len(df)) * 100
                response = f"🚨 **Security & Retention Alert:** I scanned the cluster vectors using our Isolation Forest pipeline and flagged **{total_anomalies} customer accounts** as structural anomalies (**{anomaly_pct:.1f}%** of your active user base). These profiles are at high risk of immediate churn due to sudden drops in engagement metrics."
            
            # CRITICAL FEATURE: Dynamic Segment-Specific Marketing Actions
            elif "cohort" in query_lower or "segment" in query_lower:
                # Extract which specific number the user is asking about (e.g., Cohort 1)
                found_cohort = None
                for seg in unique_segments:
                    if seg.lower() in query_lower or seg.replace(" ", "").lower() in query_lower.replace(" ", ""):
                        found_cohort = seg
                        break
                
                if found_cohort:
                    sub_seg = df[df['Segment_ID'] == found_cohort]
                    response = f"""
🎯 **Target Analysis for {found_cohort}:**
- **Volume:** {len(sub_seg)} customer accounts.
- **Profile Signature:** Average values for this specific group are:
"""
                    for f in features:
                        response += f"  - Average `{f}`: **{sub_seg[f].mean():.1f}**\n"
                    
                    response += f"\n**Suggested Strategic Campaign Action:** Launch a targeted email workflow engineered specifically for {found_cohort}. If their metrics skew low, attach a 15% promotional incentive. If their metrics reflect premium high-value spending patterns, route them to an exclusive early-access portal instead."
                else:
                    response = "🔍 I noticed you mentioned a cohort group, but I couldn't verify which one. Please ask explicitly about 'Cohort 1', 'Cohort 2', etc., based on the matrix table shown above!"
            
            # General fallback summarizing baseline system states
            else:
                response = f"💡 **General Workspace Status:** I can currently query **{len(df):,} customer entries** broken into **{meta['optimal_k']} unique cohorts**. Try asking me exactly: *'Which segment is the largest?'* or *'How many outliers do we have?'* to see real-time data calculations."
                
        with st.chat_message("assistant"):
            st.markdown(response)
        st.session_state.chat_history.append({"role": "assistant", "content": response})