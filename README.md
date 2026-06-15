# CohortIQ | Enterprise Customer Intelligence Platform (SaaS)

Transform raw customer transaction data into clear, actionable retention flows, growth tracking vectors, and context-aware business actions using an autonomous machine learning infrastructure.

## 🚀 Live Production Environment
- **Web Application Portal:** [https://customer-segmentation-engine-lo7qvs67rqmxk3sir5e6ey.streamlit.app/]
- **Core Repository Infrastructure:** (https://github.com/JogiRohithKumar/Customer-Segmentation-Engine)]

---

## 🛠️ System Architecture & Modular Design
CohortIQ is built using a decoupled, multi-page workspace architecture that transitions heavy data processing and analytical evaluation into isolated pipeline states, preserving UI responsiveness:

* **Executive Dashboard (`modules/dashboard.py`):** Handles multi-tenant style data ingestion, dataset format validation, and high-level workspace metric reporting.
* **AutoML Optimization Engine (`modules/engine.py`):** Automatically scales metrics, runs an iterative clustering loop, and validates boundaries to find the mathematically optimal segment count.
* **AI Data Copilot (`modules/advisor.py`):** A context-aware analytical assistant providing tactical marketing playbooks and segment profile breakdowns.
* **Data Hub & Report Exporter (`modules/export.py`):** Generates print-ready executive briefings and streams segment-appended CSV data directly back to active CRMs.

---

## 🧬 Advanced Analytics & Automated ML Engine
Instead of relying on manual parameter configuration or hardcoded constraints, CohortIQ runs a modern, unsupervised analytics suite:
* **Feature Invariant Scaling:** Implements `RobustScaler` preprocessing to safeguard multi-dimensional distances against extreme customer spending outliers.
* **Autonomous Hyperparameter Tuning:** Dynamically evaluates spatial density boundaries and cluster variants across `K-Means`, optimization loops, and automated `Silhouette Score` validation.
* **Unsupervised Anomaly Isolation:** Integrates an `Isolation Forest` pipeline to flag volatile purchasing profiles and sudden metric decay before customer churn occurs.

---

## 📦 Local Workspace Orchestration & Setup

1. **Clone the Infrastructure Repository:**
```bash
   git clone [https://github.com/JogiRohithKumar/Customer-Segmentation-Engine.git](https://github.com/JogiRohithKumar/Customer-Segmentation-Engine.git)
   cd Customer-Segmentation-Engine