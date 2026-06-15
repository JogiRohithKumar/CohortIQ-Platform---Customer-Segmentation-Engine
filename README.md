# CohortIQ | Customer Intelligence Platform

[![Live App](https://img.shields.io/badge/Streamlit-Live%20Demo-FF4B4B?logo=streamlit&logoColor=white)](https://customer-segmentation-engine-lo7qvs67rqmxk3sir5e6ey.streamlit.app/)
[![GitHub Repo](https://img.shields.io/badge/GitHub-Repository-181717?logo=github&logoColor=white)](https://github.com/JogiRohithKumar/Customer-Segmentation-Engine)

---

## 1. What Problem Does This Solve?
**The Industry Friction:** Businesses routinely capture thousands of lines of raw customer transaction data, but treat their customer base as a single, homogenous entity. Manually writing scripts to parse this data is slow, while enterprise business intelligence platforms are too expensive and complex for small-to-medium businesses (SMBs). 

**The Solution:** **CohortIQ** bridge this gap by transforming raw CSV transaction datasets into immediate, context-aware retention strategies. The platform automatically separates stable customer groups from volatile profiles, surfaces hidden anomaly vectors, tracks real-time customer health degradation, and converts abstract mathematical distance coordinates into natural language marketing playbooks.

---

## 2. What Exactly Did YOU Build?
This platform was engineered from scratch as a modular, end-to-end intelligence workspace.

* **Architected by:** Rohith Kumar
* **Role & Core Responsibilities:**
    * **Frontend Engineering:** Developed an intuitive, multi-page layout utilizing modern Streamlit states to simulate an isolated corporate workspace environment (`app.py`, `modules/`).
    * **Data Pipeline & Feature Engineering:** Developed automated missing value remediation workflows and applied advanced data transformation algorithms to neutralize heavy distribution skews.
    * **Machine Learning Architecture:** Implemented a multi-model AutoML engine running concurrent model evaluation loops, localized anomaly clustering, and dynamic health-scoring indices.
    * **Deployment Operations:** Set up version-controlled CI/CD parameters and successfully deployed the platform to an auto-scaling containerized instance on Streamlit Cloud.

---

## 3. What Technologies Are Used?
The complete system stack is built with the following technologies:

* **Core Language:** `Python (v3.11)`
* **Interface Layer:** `Streamlit`
* **Data Processing:** `Pandas`, `NumPy`
* **Machine Learning Engines:** `Scikit-Learn`
* **Visual Analytics:** `Plotly Express`
* **Planned Cloud Scale Stack:** `FastAPI` (Core REST API Layer), `PostgreSQL` (Relational Multi-Tenant Data Tier), `Redis` (Task Queue Broker), `Celery` (Asynchronous ML Compute Background Workers), `Docker` (Multi-stage Containerization), `AWS ECS` (Production Service Orchestration).

---

## 4. What Are The Main Features?

```markdown
✓ CSV Dataset Ingestion      → Flexible raw data parsing with instant format validation
✓ AutoML Segmentation       → Automated algorithm evaluation and mathematical structure validation
✓ Customer Health Scoring   → Multi-dimensional normalization calculations (Recency, Frequency, Monetary)
✓ Anomaly Detection         → Structural isolation forest routing to capture high-risk churn vectors
✓ AI Business Copilot       → Plain-English interface executing real-time algorithmic pandas queries
✓ Dashboard Analytics       → Comprehensive operational charts and scannable workspace KPI cards
✓ Interactive Reports       → Automated executive summaries and clean CSV segment data exports

```

---

## 5. How Does The System Work?

The application isolates complex math behind an automated sequence from initial file input down to direct text output:

```
[ Ingest Raw CSV Data ] 
           │
           ▼
[ Data Preprocessing ] ────► (Removes structural nulls & formats features)
           │
           ▼
[ Feature Engineering ] ───► (Calculates log-scaled metric baselines)
           │
           ▼
[ Robust Data Scaling ] ───► (Insulates distribution against extreme outliers)
           │
           ▼
[ AutoML Cluster Optimization Loop ] ──► (Evaluates competing models via Silhouette Scores)
           │
           ▼
[ Dual-Track Analytics Engine ]
    ├── Track A: Isolation Forest ─────► [ Flags Behavioral Anomaly Subsets ]
    └── Track B: Trajectory Analytics ──► [ Generates Composite Health Scores ]
           │
           ▼
[ Context Interface Delivery Layer ]
    ├── Portal 1: Smart Data Copilot ──► [ Runs Interactive Dynamic Queries ]
    └── Portal 2: Interactive Reports ─► [ Downloads Cleansed CRM Target Sheets ]

```

---

## 6. What ML Algorithms Are Used?

The analytical backend runs an ensemble of statistical functions rather than a single hardcoded script:

* **RobustScaler Preprocessing:** Used to standardize features by removing the median and scaling data according to the Interquartile Range (IQR). This ensures extreme spending outliers do not distort cluster definitions.
* **K-Means Clustering:** Evaluated iteratively across a dynamic range of target counts to partition customer records into tight spatial groups.
* **DBSCAN Clustering:** Evaluated alongside K-Means to identify non-linear, high-density distribution clusters while segregating background noise.
* **Silhouette Score Optimization:** Serves as the mathematical validation engine. It programmatically selects the model configuration that yields the highest separation quality, eliminating manual hyperparameter selection.
* **Isolation Forest:** An unsupervised ensemble algorithm used for anomaly detection. It isolates atypical data points, flagging accounts experiencing sudden engagement drops or severe retention decay.

---

## 7. What Makes This Project Different?

Most traditional customer segmentation projects stop at a generic Jupyter notebook displaying static 3D K-Means graphs.

**CohortIQ breaks the mold by combining:**

1. **Zero-Configuration AutoML:** Small business owners do not know what $K$-values or $\epsilon$-parameters mean; the platform automatically runs optimization checks and determines the mathematically perfect group separation in the background.
2. **Deterministic Data Copilot:** The integrated chat module does not just print generic, repetitive text blocks. It converts conversational questions into direct mathematical inquiries on the dataset, tracking the exact largest segment sizes, alert metrics, and active means in real-time.
3. **Operational Focus:** The final output is not just a statistical summary—it maps mathematical clusters directly to actionable next steps, anomaly alerts, and exportable data files.

---

## 8. Screen References & Layouts

### Executive Command Dashboard


*Provides multi-workspace selection matrices, file ingestion dropzones, and unified performance KPI card systems.*

### AutoML Cluster Mapping & Anomalies


*Renders optimized structural boundaries alongside dynamic Isolation Forest outlier alerts.*

### Conversational Data Copilot Interface


*Parses live language queries into instant analytical database executions.*

### Interactive Strategic Reports


*Compiles printable executive operational data briefings and handles multi-format dataset file exports.*

---

## 9. How Do I Run It Locally?

Get the platform running in your local environment in under 60 seconds by executing these commands:

```bash
# 1. Clone the structural repository assets
git clone [https://github.com/JogiRohithKumar/Customer-Segmentation-Engine.git](https://github.com/JogiRohithKumar/Customer-Segmentation-Engine.git)

# 2. Enter the project installation directory 
cd Customer-Segmentation-Engine

# 3. Install core system application dependencies
pip install -r requirements.txt

# 4. Fire up the local workspace application server
streamlit run app.py

```

---

## 10. What Did You Learn?

Building this platform provided deep, practical experience across full-stack machine learning engineering:

* **Unsupervised Learning Lifecycles:** Mastered how to cleanly evaluate data clustering quality using mathematical verification constraints rather than visual approximation.
* **Defensive Feature Engineering:** Learned how to handle extreme transactional data skewing using robust mathematical scaling transformations.
* **State Management Isolation:** Implemented structured, multi-page data passing using session caching layers, preventing unneeded model calculations or app lockups.
* **Product-Led Thinking:** Transitioned from writing simple, one-off code scripts to constructing multi-tenant operational products designed for actual business scenarios.

```
***

### 🚀 What to do next:
1. Open your local project text editor and paste this code block directly into your `README.md` file.
2. Ensure you place your screenshot image files inside a folder named `screenshots/` within your GitHub repository (e.g., save them as `dashboard.png`, `segmentation.png`, `copilot.png`, and `reports.png`). This tells GitHub exactly where to find and display them on your repository page. 

This completes your project transformation! You now have a high-quality, professional SaaS repository ready for interviews and applications.

```
