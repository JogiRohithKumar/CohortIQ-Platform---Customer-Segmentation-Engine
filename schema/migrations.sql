-- 1. Identity & Access Management Table
CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 2. Metadata Manifest for Ingested Files
CREATE TABLE datasets (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES users(id) ON DELETE CASCADE,
    file_name VARCHAR(255) NOT NULL,
    row_count INTEGER NOT NULL,
    uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 3. Historical Record Metrics Log
CREATE TABLE customer_records (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    dataset_id UUID REFERENCES datasets(id) ON DELETE CASCADE,
    customer_email VARCHAR(255),
    recency INTEGER,
    frequency INTEGER,
    monetary_value NUMERIC(12, 2),
    segment_assignment VARCHAR(100),
    health_score INTEGER,
    is_anomaly BOOLEAN,
    processed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);