# CohortIQ | Customer Intelligence Platform
[![Live App](https://img.shields.io/badge/Streamlit-Live%20Demo-FF4B4B?logo=streamlit&logoColor=white)](https://customer-segmentation-engine-lo7qvs67rqmxk3sir5e6ey.streamlit.app/)
# CohortIQ | AI-Powered Customer Intelligence Platform

[![Live App](https://img.shields.io/badge/Streamlit-Live%20Demo-FF4B4B?logo=streamlit\&logoColor=white)](https://customer-segmentation-engine-lo7qvs67rqmxk3sir5e6ey.streamlit.app)

## Overview

CohortIQ is an end-to-end Customer Intelligence Platform that transforms raw customer transaction data into actionable business insights through automated segmentation, customer health scoring, anomaly detection, and AI-assisted analytics.

Designed for small businesses, analysts, and marketing teams, the platform eliminates the need for manual data exploration by automatically identifying customer groups, detecting unusual behavior patterns, calculating customer health metrics, and generating business recommendations.

Unlike traditional clustering projects that stop at visualization, CohortIQ extends the analytics workflow by combining AutoML optimization, anomaly detection, business intelligence reporting, and a conversational Data Copilot capable of answering business questions directly from uploaded datasets.

---

## Key Highlights

### AutoML Customer Segmentation

* Automatically evaluates multiple clustering configurations
* Uses Silhouette Score optimization to identify the best-performing segmentation strategy
* Removes the need for manual cluster selection

### Customer Health Intelligence

* Generates normalized customer health scores from behavioral features
* Highlights declining customer engagement patterns
* Helps identify customers requiring retention actions

### Anomaly Detection Engine

* Uses Isolation Forest to identify abnormal customer behavior
* Detects spending irregularities and engagement drops
* Surfaces high-risk customer profiles for investigation

### Data Copilot

* Converts business questions into real-time dataframe analytics
* Executes live customer data queries
* Generates contextual recommendations using actual dataset metrics

Example questions:

* Which segment is the largest?
* How many anomalies were detected?
* Which customer group generates the highest value?
* Which customers require retention campaigns?

### Interactive Business Analytics

* Segment visualization dashboards
* Customer distribution analysis
* KPI monitoring
* Trend exploration

### Reporting & Export

* Export enriched customer datasets
* Generate business summaries
* Download segmentation outputs for CRM workflows

---

## Business Problem

Most organizations collect customer data but struggle to transform it into actionable business decisions.

Common challenges include:

* Identifying high-value customers
* Detecting churn risks early
* Understanding purchasing behavior
* Prioritizing marketing efforts
* Creating targeted retention strategies

CohortIQ automates this process through machine learning and interactive analytics, allowing users to move from raw data to business decisions in minutes.

---

## Platform Workflow

```text
Upload Customer Dataset
            │
            ▼
     Data Validation
            │
            ▼
     Data Cleaning
            │
            ▼
   Feature Engineering
            │
            ▼
      Robust Scaling
            │
            ▼
 AutoML Segmentation Engine
     ├── K-Means
     └── DBSCAN
            │
            ▼
 Silhouette Score Selection
            │
            ▼
     Customer Segments
            │
     ┌──────┴──────┐
     ▼             ▼
Health Scores   Isolation Forest
     │             │
     └──────┬──────┘
            ▼
 Business Intelligence Layer
            │
     ┌──────┴─────────┐
     ▼                ▼
Data Copilot      Reports & Export
```

---

## Core Technologies

| Layer            | Technologies              |
| ---------------- | ------------------------- |
| Language         | Python                    |
| Frontend         | Streamlit                 |
| Data Processing  | Pandas, NumPy             |
| Machine Learning | Scikit-Learn              |
| Visualization    | Plotly                    |
| Deployment       | Streamlit Cloud           |
| Development      | VS Code, Jupyter Notebook |

---

## Machine Learning Components

| Component              | Purpose                                      |
| ---------------------- | -------------------------------------------- |
| RobustScaler           | Handles extreme outliers and feature scaling |
| K-Means                | Customer segmentation                        |
| DBSCAN                 | Density-based clustering and noise detection |
| Silhouette Score       | Automated cluster evaluation                 |
| Isolation Forest       | Customer anomaly detection                   |
| Customer Health Engine | Behavioral scoring and engagement analysis   |

---

## Engineering Highlights

* Built a modular multi-page analytics platform using Streamlit
* Implemented an AutoML clustering engine with automated model selection
* Developed a customer health scoring framework using normalized behavioral metrics
* Integrated Isolation Forest-based anomaly detection workflows
* Designed a deterministic Data Copilot capable of executing real-time dataframe analytics
* Created business-focused reporting and export functionality
* Deployed the platform as a publicly accessible cloud application



---

## Installation

Clone the repository:

```bash
git clone https://github.com/JogiRohithKumar/CohortIQ-Platform---Customer-Segmentation-Engine.git

cd CohortIQ-Platform---Customer-Segmentation-Engine
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

---

## Author

**Rohith Kumar Jogi**
GitHub: https://github.com/JogiRohithKumar
LinkedIn: https://www.linkedin.com/in/rohith-kumar-jogi-747a782b8
