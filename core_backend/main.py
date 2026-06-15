from fastapi import FastAPI, Depends, HTTPException, status, UploadFile, File
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import pandas as pd
import numpy as np
from pydantic import BaseModel
from typing import List
import jwt
from passlib.context import CryptContext
from sklearn.preprocessing import RobustScaler
from sklearn.cluster import KMeans
from sklearn.ensemble import IsolationForest

# System Configurations
SECRET_KEY = "COHORT_IQ_SUPER_SECRET_DEPLOYMENT_KEY"
ALGORITHM = "HS256"

app = FastAPI(title="CohortIQ Core Backend Engine", version="2.0.0")
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Mock In-Memory Persistence Layer (Replaces PostgreSQL Connector for Lightweight Testing)
DATABASE_MOCK = {"users": {}, "datasets": {}, "records": {}}

class UserRegister(BaseModel):
    email: str
    password: str

# --- AUTHENTICATION MODULE ---
@app.post("/auth/register", status_code=status.HTTP_201_CREATED)
def register_user(user: UserRegister):
    if user.email in DATABASE_MOCK["users"]:
        raise HTTPException(status_code=400, detail="User target space already allocated.")
    DATABASE_MOCK["users"][user.email] = pwd_context.hash(user.password)
    return {"message": "User environment provisioned successfully."}

@app.post("/token")
def login_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user_hashed_pass = DATABASE_MOCK["users"].get(form_data.username)
    if not user_hashed_pass or not pwd_context.verify(form_data.password, user_hashed_pass):
        raise HTTPException(status_code=400, detail="Invalid credential parameters.")
    
    token = jwt.encode({"sub": form_data.username}, SECRET_KEY, algorithm=ALGORITHM)
    return {"access_token": token, "token_type": "bearer"}

def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid session verification.")
        return username
    except jwt.PyJWTError:
        raise HTTPException(status_code=401, detail="Session credentials expired.")

# --- DATA INTELLIGENCE PIPELINE ENDPOINTS ---
@app.post("/api/v1/upload")
async def upload_dataset(file: UploadFile = File(...), current_user: str = Depends(get_current_user)):
    try:
        contents = await file.read()
        df = pd.read_csv(io.BytesIO(contents))
        dataset_id = str(np.random.randint(10000, 99999))
        
        # Stash matrix inside local repository dictionary
        DATABASE_MOCK["datasets"][dataset_id] = df.to_dict(orient="records")
        return {"dataset_id": dataset_id, "rows_parsed": len(df), "status": "Ready for Processing"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Data parsing exception structural failure: {str(e)}")

@app.post("/api/v1/analyze")
def run_core_analytics(dataset_id: str, features: List[str], current_user: str = Depends(get_current_user)):
    raw_records = DATABASE_MOCK["datasets"].get(dataset_id)
    if not raw_records:
        raise HTTPException(status_code=404, detail="Target dataset signature not found.")
        
    df = pd.DataFrame(raw_records)
    X = df[features].fillna(df[features].median())
    
    # 1. Scale Features to isolate variance safely
    scaler = RobustScaler()
    X_scaled = scaler.fit_transform(X)
    
    # 2. Execute `/segment` Core Task Loop
    km = KMeans(n_clusters=3, random_state=42, n_init=10)
    df["segment_assignment"] = [f"Cohort {l+1}" for l in km.fit_predict(X_scaled)]
    
    # 3. Execute `/health-score` Vector Routing
    # Normalized Recency, Frequency, and Monetary distribution score formula
    rfm_composite = np.mean(X_scaled, axis=1)
    df["health_score"] = np.clip(50 + (rfm_composite * 10), 0, 100).astype(int)
    
    # 4. Execute `/anomalies` Isolation Forest Thread
    iso = IsolationForest(contamination=0.03, random_state=42)
    df["is_anomaly"] = [True if a == -1 else False for a in iso.fit_predict(X_scaled)]
    
    # Commit changes back to state database dictionary mapping
    DATABASE_MOCK["records"][dataset_id] = df.to_dict(orient="records")
    return {"status": "Complete", "dataset_id": dataset_id, "metrics": {"total_anomalies": int(df["is_anomaly"].sum())}}

@app.post("/api/v1/advisor")
def get_advisor_insights(dataset_id: str, query: str, current_user: str = Depends(get_current_user)):
    processed_records = DATABASE_MOCK["records"].get(dataset_id)
    if not processed_records:
        raise HTTPException(status_code=404, detail="No analyzed cohort matrix maps available for this context record.")
        
    df = pd.DataFrame(processed_records)
    query_clean = query.lower()
    
    # Deterministic execution matching NLP context criteria
    if "anomaly" in query_clean or "churn" in query_clean:
        total_risk = df["is_anomaly"].sum()
        return {"response": f"Backend Scans reflect {total_risk} target anomalies showing highly volatile trajectory indicators."}
    elif "largest" in query_clean or "biggest" in query_clean:
        top_cohort = df["segment_assignment"].value_counts().idxmax()
        return {"response": f"Database scan identifies {top_cohort} as the largest workspace user distribution cluster."}
    
    return {"response": "General Advisor Status: System monitoring active. Ask specific cohort size or risk metrics."}