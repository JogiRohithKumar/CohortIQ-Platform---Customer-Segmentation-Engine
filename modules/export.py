import streamlit as st
import pandas as pd
import numpy as np
import io

st.title("📥 Interactive Business Reports & Data Hub")
st.subheader(f"Active Workspace Segment Exporter: {st.session_state.workspace_selector}")

# Assert state presence before exposing workspace controls
if st.session_state.segmented_data is None:
    st.warning("⚠️ No segmented data metrics found for extraction. Please configure your model configurations inside the 'AutoML & Anomalies' panel first.")
else:
    df = st.session_state.segmented_data
    meta = st.session_state.model_metadata
    features = meta['features_used']
    
    st.markdown("### 📊 Cohort Comparative Analysis")
    
    # 1. Provide an interactive profile tool for the business owner to compare groups
    target_segment = st.selectbox("Select Target Cohort to Inspect", options=sorted(df['Segment_ID'].unique()))
    
    # Isolate subset targets
    seg_only_df = df[df['Segment_ID'] == target_segment]
    anomaly_subset = seg_only_df[seg_only_df['Anomaly_Flag'] == "Outlier"]
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Cohort Membership", f"{len(seg_only_df)} Accounts")
    with col2:
        st.metric("Flagged High-Risk Anomalies", f"{len(anomaly_subset)} Profiles")
    with col3:
        # Simple calculated share percentage indicator
        share_pct = (len(seg_only_df) / len(df)) * 100
        st.metric("Total Customer Share Group", f"{share_pct:.1f}%")

    st.markdown("#### Average Feature Baseline Profile Matrix")
    # Dynamically pull descriptive averages across chosen vectors 
    mean_profile = seg_only_df[features].mean().to_frame(name="Cohort Group Average")
    st.table(mean_profile)

    st.markdown("---")
    st.markdown("### 📋 Automated Executive Report Generator")
    
    # Create an on-the-fly markdown string layout representing an Executive Briefing document
    report_stream = io.StringIO()
    report_stream.write(f"# CohortIQ Executive Intelligence Briefing\n")
    report_stream.write(f"**Target Workspace Platform Profile:** {st.session_state.workspace_selector}\n")
    report_stream.write(f"**Model Computational Mode:** AutoML Optimized Configuration Loop\n")
    report_stream.write(f"**Optimal Structural Cohorts Found:** {meta['optimal_k']} Unique Profiles\n")
    report_stream.write(f"**Structural Boundary Validity Check (Silhouette Coefficient):** {meta['silhouette_score']:.3f}\n\n")
    report_stream.write(f"## Data Diagnostics & Behavioral Summary Matrix\n")
    
    for segment in sorted(df['Segment_ID'].unique()):
        sub_df = df[df['Segment_ID'] == segment]
        report_stream.write(f"- **{segment}**: Handles {len(sub_df)} distinct target profiles. Core attribute behaviors present averages of: ")
        for f in features:
            report_stream.write(f"[{f}: {sub_df[f].mean():.2f}] ")
        report_stream.write("\n")
        
    report_string = report_stream.getvalue()
    
    with st.expander("📄 Preview Generated Executive Summary Document", expanded=True):
        st.markdown(report_string)
        
    # 2. Expose the Data Pipeline Download Portals
    st.markdown("---")
    st.markdown("### 📦 Data Delivery Center")
    st.write("Extract your processed customer segments or the executive document for external distribution or direct CRM ingestion.")
    
    d_col1, d_col2 = st.columns(2)
    
    # Conversion of standard data frame assets to bytes ready for streaming downloads
    csv_bytes = df.to_csv(index=False).encode('utf-8')
    
    with d_col1:
        st.download_button(
            label="📥 Download Segmented Dataset (.CSV)",
            data=csv_bytes,
            file_name=f"cohort_iq_{st.session_state.workspace_selector.lower().replace(' ', '_')}_segments.csv",
            mime="text/csv",
            help="Provides the full customer input dataset appended with your custom Segment_ID and Anomaly_Flag evaluation columns.",
            use_container_width=True
        )
        
    with d_col2:
        st.download_button(
            label="📄 Export Executive Report (.MD)",
            data=report_string,
            file_name="cohort_iq_executive_briefing.md",
            mime="text/markdown",
            help="Downloads the structured Markdown executive summary file generated above.",
            use_container_width=True
        )