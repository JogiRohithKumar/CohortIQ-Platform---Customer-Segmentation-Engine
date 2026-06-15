# CohortIQ | Customer Intelligence Platform
[![Live App](https://img.shields.io/badge/Streamlit-Live%20Demo-FF4B4B?logo=streamlit&logoColor=white)](https://customer-segmentation-engine-lo7qvs67rqmxk3sir5e6ey.streamlit.app/)
## Overview

CohortIQ is an AI-powered customer analytics platform that helps businesses understand customer behavior through automated segmentation, anomaly detection, customer health scoring, and business recommendations.

The platform transforms raw customer transaction data into meaningful customer groups and actionable insights, enabling businesses to identify high-value customers, detect churn risks, and improve marketing decisions.

Built as an end-to-end machine learning application, CohortIQ combines data preprocessing, unsupervised learning, anomaly detection, interactive analytics, and AI-assisted business intelligence within a single workspace.

---

## Problem Statement

Many businesses collect customer transaction data but lack the tools to analyze customer behavior effectively.

Common challenges include:

* Identifying valuable customer segments
* Detecting customers at risk of churn
* Understanding purchasing patterns
* Prioritizing retention efforts
* Generating actionable business insights

Traditional analytics platforms are often expensive, while manual analysis is time-consuming and difficult to scale.

CohortIQ addresses this problem by automating customer segmentation and analytics using machine learning.

---

## Key Features

### Customer Segmentation

* Automated customer grouping using clustering algorithms
* Identification of high-value, regular, and low-engagement customers
* Visual exploration of customer segments

### AutoML Optimization

* Automatic evaluation of clustering configurations
* Silhouette Score-based model selection
* Reduced need for manual parameter tuning

### Customer Health Scoring

* Calculates customer health using Recency, Frequency, and Monetary (RFM) metrics
* Identifies declining customer engagement patterns

### Anomaly Detection

* Detects unusual customer behavior using Isolation Forest
* Flags customers with abnormal spending or engagement changes

### AI Business Advisor

* Generates business-friendly insights from customer data
* Provides retention and marketing recommendations
* Converts analytical outputs into actionable strategies

### Interactive Analytics Dashboard

* Customer distribution visualization
* Segment-level insights
* KPI monitoring
* Trend analysis

### Export & Reporting

* Download segmented customer datasets
* Generate summary reports for business decision-making

---

## System Workflow

```text
Customer Dataset (CSV)
            │
            ▼
     Data Validation
            │
            ▼
    Data Preprocessing
            │
            ▼
    Feature Engineering
            │
            ▼
      Robust Scaling
            │
            ▼
     AutoML Segmentation
            │
            ├──────────────► K-Means
            │
            └──────────────► DBSCAN
            │
            ▼
   Silhouette Score Selection
            │
            ▼
     Customer Segments
            │
     ┌──────┴──────┐
     ▼             ▼
Health Scores   Anomaly Detection
     │             │
     └──────┬──────┘
            ▼
     Business Insights
            │
            ▼
 Dashboard & Reports
```

---

## Machine Learning Pipeline

### Data Preprocessing

* Missing value handling
* Feature selection
* Dataset validation

### Feature Scaling

* RobustScaler

Used to reduce the impact of extreme spending outliers and improve clustering performance.

### Clustering Algorithms

#### K-Means

* Customer segmentation
* Distance-based clustering
* Fast and scalable

#### DBSCAN

* Density-based clustering
* Handles irregular cluster shapes
* Identifies noise points

### Cluster Evaluation

#### Silhouette Score

Used to evaluate clustering quality and select the most appropriate segmentation model.

### Anomaly Detection

#### Isolation Forest

Detects abnormal customer behavior and potential churn indicators.

---

## Tech Stack

### Programming Language

* Python

### Frontend & UI

* Streamlit

### Data Processing

* Pandas
* NumPy

### Machine Learning

* Scikit-Learn

### Data Visualization

* Plotly

### Development Environment

* Jupyter Notebook
* VS Code

### Deployment

* Streamlit Cloud

---

## Project Structure

```text
CohortIQ/
│
├── app.py
├── modules/
│   ├── dashboard.py
│   ├── engine.py
│   ├── advisor.py
│   └── export.py
│
├── data/
│
├── notebooks/
│
├── requirements.txt
│
└── README.md
```

---

## Screenshots

### Dashboard

Add dashboard screenshot here

### Customer Segmentation

Add segmentation screenshot here

### Anomaly Detection

Add anomaly detection screenshot here

### AI Business Advisor

Add advisor screenshot here

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

## Business Applications

* Customer retention analysis
* Marketing campaign targeting
* Loyalty program optimization
* Customer lifetime value assessment
* Churn risk monitoring
* Revenue growth analysis

---

## Challenges Solved

### Handling Skewed Customer Data

Applied RobustScaler to reduce the influence of extreme outliers.

### Automatic Cluster Selection

Implemented Silhouette Score evaluation to avoid manual cluster tuning.

### Detecting Customer Anomalies

Integrated Isolation Forest to identify unusual behavioral patterns.

### Interactive Analytics

Built a user-friendly interface for non-technical users to explore customer insights.

---

## Future Enhancements

* User authentication and account management
* PostgreSQL integration
* FastAPI backend services
* Multi-tenant workspace support
* PDF report generation
* Historical cohort tracking
* Churn prediction models
* LLM-powered customer intelligence copilot
* Docker deployment
* Cloud-native infrastructure

---

## Key Learnings

* Unsupervised machine learning workflows
* Feature engineering for customer analytics
* Cluster evaluation techniques
* Anomaly detection methods
* Interactive dashboard development
* End-to-end ML application deployment
* Product-oriented problem solving

---

## Author

**Rohith Kumar**

Computer Science Engineering Student

GitHub: https://github.com/JogiRohithKumar

LinkedIn:https://www.linkedin.com/in/rohith-kumar-jogi-747a782b8
