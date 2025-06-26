
import streamlit as st
import numpy as np
from datetime import datetime, timedelta

# === Locked‑in coefficients (20‑feature model) ===
intercept = 4234.6749
coefs = {
    "Scope_B.O.": -46.2768,
    "Scope_EXP": -38.9121,
    "Scope_NEW": 48.1697,
    "Scope_RENO": 28.3512,
    "Contract_BB": -23.7471,
    "BT_Civic/Specialty": 12.5684,
    "BT_Commercial": 9.3347,
    "BT_Education": 14.9886,
    "BT_Healthcare": 31.2245,
    "BT_Hospitality/Residential": 34.5246,
    "BT_Industrial": 7.1183,
    "BT_Mission Critical": 27.4491,
    "Log Sq Ft": 67.8822,
    "Levels": 7.3205,
    "Levels * Log Sq Ft": 5.1122,
    "Levels * Scope_NEW": 5.8478,
    "Levels * Contract_BB": 3.9114,
    "Log Sq Ft * Contract_BB": 25.6414,
    # Filling remaining two interaction slots with zero if unused
    "Levels * Scope_RENO": 0.0,
    "Log Sq Ft * Scope_RENO": 0.0
}

feature_list = list(coefs.keys()) + ["Log Sq Ft", "Levels"]

st.title("📐 BIM Coordination Duration Estimator (Clean Locked‑in Model)")

start_date = st.date_input("Start Date", value=datetime.today())
scope = st.selectbox("Scope", ["NEW", "RENO", "EXP", "B.O."])
contract = st.selectbox("Contract", ["BB"])
bldg = st.selectbox("Building Type", [
    "Civic/Specialty", "Commercial", "Education", "Healthcare",
    "Hospitality/Residential", "Industrial", "Mission Critical"
])
sqft = st.number_input("Square Footage", min_value=1000, value=180000)
levels = st.number_input("Levels", min_value=1, value=1)

if st.button("Predict"):
    log_sqft = np.log(sqft)

    # Build feature dict
    feats = dict.fromkeys(coefs.keys(), 0.0)
    feats[f"Scope_{scope}"] = 1.0
    feats[f"Contract_{contract}"] = 1.0
    feats[f"BT_{bldg}"] = 1.0
    feats["Log Sq Ft"] = log_sqft
    feats["Levels"] = levels
    feats["Levels * Log Sq Ft"] = levels * log_sqft
    feats["Levels * Scope_NEW"] = levels if scope == "NEW" else 0.0
    feats["Levels * Contract_BB"] = levels
    feats["Log Sq Ft * Contract_BB"] = log_sqft

    # Prediction
    duration = intercept + sum(feats[k] * v for k, v in coefs.items())
    end_date = start_date + timedelta(days=round(duration))

    st.success(f"Predicted Duration: {round(duration, 1)} days")
    st.info(f"Predicted End Date: {end_date.strftime('%Y-%m-%d')}")
