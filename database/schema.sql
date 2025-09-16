CREATE TABLE loads (
    load_id VARCHAR(20) PRIMARY KEY,
    origin VARCHAR(100) NOT NULL,
    destination VARCHAR(100) NOT NULL,
    pickup_datetime TIMESTAMP NOT NULL,
    delivery_datetime TIMESTAMP NOT NULL,
    equipment_type VARCHAR(50) NOT NULL,
    loadboard_rate DECIMAL(10,2) NOT NULL,
    notes TEXT,
    weight INTEGER,
    commodity_type VARCHAR(100),
    num_of_pieces INTEGER,
    miles INTEGER,
    dimensions VARCHAR(50),
    status VARCHAR(20) DEFAULT 'available',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE carriers (
    mc_number VARCHAR(20) PRIMARY KEY,
    company_name VARCHAR(200),
    status VARCHAR(20),
    verified_at TIMESTAMP,
    equipment_types TEXT[],
    preferred_lanes TEXT[]
);

CREATE TABLE call_logs (
    call_id VARCHAR(50) PRIMARY KEY,
    mc_number VARCHAR(20),
    caller_phone VARCHAR(20),
    call_duration INTEGER,
    loads_presented TEXT[],
    final_rate DECIMAL(10,2),
    negotiation_rounds INTEGER DEFAULT 0,
    outcome VARCHAR(50),
    sentiment VARCHAR(20),
    satisfaction_score INTEGER,
    extracted_data JSONB,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE negotiations (
    id SERIAL PRIMARY KEY,
    call_id VARCHAR(50) REFERENCES call_logs(call_id),
    load_id VARCHAR(20) REFERENCES loads(load_id),
    round_number INTEGER,
    carrier_offer DECIMAL(10,2),
    system_response VARCHAR(20),
    system_counter_offer DECIMAL(10,2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
