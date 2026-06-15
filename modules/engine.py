import streamlit as st
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import RobustScaler
from sklearn.ensemble import IsolationForest
import plotly.express as px

st.title("🧬 AutoML Cluster Engine & Anomaly Analytics")

if st.session_state.uploaded_data is None:
    st.warning("⚠️ No active dataset found in this workspace. Go to the Executive Dashboard page to upload your file.")
else:
    df = st.session_state.uploaded_data.copy()
    
    st.markdown("### Engine Optimization Setup")
    numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    
    selected_features = st.multiselect(
        "Select Feature Matrix Vectors for Structural Clustering", 
        options=numeric_cols,
        default=numeric_cols[:3] if len(numeric_cols) >= 3 else numeric_cols
    )
    
    if st.button("Execute Autonomous Optimization Loop", type="primary"):
        if len(selected_features) < 2:
            st.error("Please select at least 2 numerical features to construct an actionable multi-dimensional clustering field.")
        else:
            with st.spinner("Executing AutoML Pipelines (Running Scalers, Iterating K, Scoring Structural Boundaries)..."):
                
                # 1. Robust Scaling to insulate against extreme spending anomalies
                scaler = RobustScaler()
                X_scaled = scaler.fit_transform(df[selected_features])
                
                # 2. Automated Silhouette Scoring Optimization Loop
                best_k = 2
                best_score = -1
                best_labels = None
                
                # Dynamically evaluate cluster counts from K=2 up to K=6 safely
                for k in range(2, min(7, len(df))):
                    km = KMeans(n_clusters=k, random_state=42, n_init=10)
                    labels = km.fit_predict(X_scaled)
                    score = silhouette_score(X_scaled, labels)
                    
                    if score > best_score:
                        best_score = score
                        best_k = k
                        best_labels = labels
                
                # 3. Unsupervised Anomaly Isolation Forest Layer
                iso = IsolationForest(contamination=0.03, random_state=42)
                anomalies = iso.fit_predict(X_scaled)
                
                # 4. Map findings back to our globally isolated session state objects
                df['Segment_ID'] = [f"Cohort {l+1}" for l in best_labels]
                df['Anomaly_Flag'] = ["Outlier" if a == -1 else "Normal" for a in anomalies]
                
                st.session_state.segmented_data = df
                st.session_state.model_metadata = {
                    "optimal_k": best_k,
                    "silhouette_score": best_score,
                    "features_used": selected_features
                }
                
            st.success("Automated processing iteration completed!")

    # Display processing results if active state exists
    if st.session_state.segmented_data is not None:
        meta = st.session_state.model_metadata
        res_df = st.session_state.segmented_data
        
        # Micro metrics dashboard display
        m1, m2 = st.columns(2)
        m1.metric("Optimal Segment Breakdown Found", f"{meta['optimal_k']} Cohorts")
        m2.metric("Cluster Structure Validity (Silhouette)", f"{meta['silhouette_score']:.3f}")
        
        # Render clean interactive 2D Projection Chart via Plotly
        st.markdown("### Workspace Segment Projection View")
        fig = px.scatter(
            res_df, 
            x=meta['features_used'][0], 
            y=meta['features_used'][1],
            color='Segment_ID', 
            symbol='Anomaly_Flag',
            title="AutoML Structural Cohort Breakdown Map",
            template="plotly_white"
        )
        st.plotly_chart(fig, use_container_width=True)
        
        # Display flagged anomalies
        anomaly_count = len(res_df[res_df['Anomaly_Flag'] == "Outlier"])
        st.warning(f"🚨 **Structural Anomaly Trigger:** The engine identified **{anomaly_count} customer accounts** exhibiting volatile purchasing trends or extreme metric decay.")