
import streamlit as st
import numpy as np
from datetime import datetime, timedelta

# Locked-in model coefficients
intercept = 4234.674948
coefs = {
    "Scope_B.O.": 67.725113,
    "Scope_DEMO\nNEW": -1.939899,
    "Scope_EXP": -3.104053,
    "Scope_NEW": -46.276831,
    "Scope_NEW\nRENO": -0.203653,
    "Scope_RENO": -16.200677,
    "BT_Civic/Specialty": 1.758746,
    "BT_Commercial": -0.733149,
    "BT_Education": -0.770473,
    "BT_Healthcare": 63.46743,
    "BT_Hospitality/Residential": -1.261809,
    "BT_Industrial": 1.589459,
    "BT_Mission Critical": -64.050205,
    "Log Sq Ft": -106.956702,
    "Levels": -8.384325,
    "Levels * Log Sq Ft": -127.235098,
    "Levels * Scope_NEW": -58.513194,
    "Levels * Contract_BB": -8.384325,
    "Log Sq Ft * Contract_BB": -106.956702,
    "Scope_B.O.^2": 67.725113,
    "Scope_B.O. Contract_BB": 67.725113,
    "Scope_B.O. BT_Commercial": -0.733149,
    "Scope_B.O. BT_Healthcare": 129.546964,
    "Scope_B.O. BT_Industrial": 8.25473,
    "Scope_B.O. BT_Mission Critical": -69.343432,
    "Scope_B.O. Log Sq Ft": -70.330252,
    "Scope_B.O. Levels": 89.233406,
    "Scope_B.O. Levels * Log Sq Ft": 33.040511,
    "Scope_B.O. Levels * Contract_BB": 89.233406,
    "Scope_B.O. Log Sq Ft * Contract_BB": -70.330252,
    "Scope_DEMO\nNEW^2": -1.939899,
    "Scope_DEMO\nNEW Contract_BB": -1.939899,
    "Scope_DEMO\nNEW BT_Civic/Specialty": -1.939899,
    "Scope_DEMO\nNEW Log Sq Ft": -21.342967,
    "Scope_DEMO\nNEW Levels": -11.639396,
    "Scope_DEMO\nNEW Levels * Log Sq Ft": -128.057801,
    "Scope_DEMO\nNEW Levels * Contract_BB": -11.639396,
    "Scope_DEMO\nNEW Log Sq Ft * Contract_BB": -21.342967,
    "Scope_EXP^2": -3.104053,
    "Scope_EXP Contract_BB": -3.104053,
    "Scope_EXP BT_Healthcare": -3.104053,
    "Scope_EXP Log Sq Ft": -1.999421,
    "Scope_EXP Levels": -10.857158,
    "Scope_EXP Levels * Log Sq Ft": -18.417179,
    "Scope_EXP Levels * Contract_BB": -10.857158,
    "Scope_EXP Log Sq Ft * Contract_BB": -1.999421,
    "Scope_NEW^2": -46.276831,
    "Scope_NEW Contract_BB": -46.276831,
    "Scope_NEW BT_Civic/Specialty": 3.698646,
    "Scope_NEW BT_Education": -0.770473,
    "Scope_NEW BT_Healthcare": 49.83378,
    "Scope_NEW BT_Hospitality/Residential": -1.261809,
    "Scope_NEW BT_Industrial": -103.070201,
    "Scope_NEW BT_Mission Critical": 5.293227,
    "Scope_NEW Log Sq Ft": -1.368087,
    "Scope_NEW Levels": -58.513194,
    "Scope_NEW Levels * Log Sq Ft": 0.226775,
    "Scope_NEW Levels * Scope_NEW": -58.513194,
    "Scope_NEW Levels * Contract_BB": -58.513194,
    "Scope_NEW Log Sq Ft * Contract_BB": -1.368087,
    "Scope_NEW\nRENO^2": -0.203653,
    "Scope_NEW\nRENO Contract_BB": -0.203653,
    "Scope_NEW\nRENO BT_Healthcare": -0.203653,
    "Scope_NEW\nRENO Log Sq Ft": -2.11143,
    "Scope_NEW\nRENO Levels": -0.407306,
    "Scope_NEW\nRENO Levels * Log Sq Ft": -4.22286,
    "Scope_NEW\nRENO Levels * Contract_BB": -0.407306,
    "Scope_NEW\nRENO Log Sq Ft * Contract_BB": -2.11143,
    "Scope_RENO^2": -16.200677,
    "Scope_RENO Contract_BB": -16.200677,
    "Scope_RENO BT_Healthcare": -112.605607,
    "Scope_RENO BT_Industrial": 96.40493,
    "Scope_RENO Log Sq Ft": -9.804545,
    "Scope_RENO Levels": -16.200677,
    "Scope_RENO Levels * Log Sq Ft": -9.804545,
    "Scope_RENO Levels * Contract_BB": -16.200677,
    "Scope_RENO Log Sq Ft * Contract_BB": -9.804545,
    "Contract_BB BT_Civic/Specialty": 1.758746,
    "Contract_BB BT_Commercial": -0.733149,
    "Contract_BB BT_Education": -0.770473,
    "Contract_BB BT_Healthcare": 63.46743,
    "Contract_BB BT_Hospitality/Residential": -1.261809,
    "Contract_BB BT_Industrial": 1.589459,
    "Contract_BB BT_Mission Critical": -64.050205,
    "Contract_BB Log Sq Ft": -106.956702,
    "Contract_BB Levels": -8.384325,
    "Contract_BB Levels * Log Sq Ft": -127.235098,
    "Contract_BB Levels * Scope_NEW": -58.513194,
    "Contract_BB Levels * Contract_BB": -8.384325,
    "Contract_BB Log Sq Ft * Contract_BB": -106.956702,
    "BT_Civic/Specialty^2": 1.758746,
    "BT_Civic/Specialty Log Sq Ft": 40.39975,
    "BT_Civic/Specialty Levels": -13.815081,
    "BT_Civic/Specialty Levels * Log Sq Ft": -45.522896,
    "BT_Civic/Specialty Levels * Scope_NEW": -2.175685,
    "BT_Civic/Specialty Levels * Contract_BB": -13.815081,
    "BT_Civic/Specialty Log Sq Ft * Contract_BB": 40.39975,
    "BT_Commercial^2": -0.733149,
    "BT_Commercial Log Sq Ft": -9.274523,
    "BT_Commercial Levels": -1.466298,
    "BT_Commercial Levels * Log Sq Ft": -18.549047,
    "BT_Commercial Levels * Contract_BB": -1.466298,
    "BT_Commercial Log Sq Ft * Contract_BB": -9.274523,
    "BT_Education^2": -0.770473,
    "BT_Education Log Sq Ft": -9.343132,
    "BT_Education Levels": -3.081892,
    "BT_Education Levels * Log Sq Ft": -37.372528,
    "BT_Education Levels * Scope_NEW": -3.081892,
    "BT_Education Levels * Contract_BB": -3.081892,
    "BT_Education Log Sq Ft * Contract_BB": -9.343132,
    "BT_Healthcare^2": 63.46743,
    "BT_Healthcare Log Sq Ft": 5.980686,
    "BT_Healthcare Levels": 119.177522,
    "BT_Healthcare Levels * Log Sq Ft": -50.858434,
    "BT_Healthcare Levels * Scope_NEW": 30.170487,
    "BT_Healthcare Levels * Contract_BB": 119.177522,
    "BT_Healthcare Log Sq Ft * Contract_BB": 5.980686,
    "BT_Hospitality/Residential^2": -1.261809,
    "BT_Hospitality/Residential Log Sq Ft": -15.458055,
    "BT_Hospitality/Residential Levels": -7.570853,
    "BT_Hospitality/Residential Levels * Log Sq Ft": -92.748333,
    "BT_Hospitality/Residential Levels * Scope_NEW": -7.570853,
    "BT_Hospitality/Residential Levels * Contract_BB": -7.570853,
    "BT_Hospitality/Residential Log Sq Ft * Contract_BB": -15.458055,
    "BT_Industrial^2": 1.589459,
    "BT_Industrial Log Sq Ft": -54.857339,
    "BT_Industrial Levels": 9.84419,
    "BT_Industrial Levels * Log Sq Ft": 39.111981,
    "BT_Industrial Levels * Scope_NEW": -103.070201,
    "BT_Industrial Levels * Contract_BB": 9.84419,
    "BT_Industrial Log Sq Ft * Contract_BB": -54.857339,
    "BT_Mission Critical^2": -64.050205,
    "BT_Mission Critical Log Sq Ft": -64.404087,
    "BT_Mission Critical Levels": -111.471913,
    "BT_Mission Critical Levels * Log Sq Ft": 78.704158,
    "BT_Mission Critical Levels * Scope_NEW": 27.21495,
    "BT_Mission Critical Levels * Contract_BB": -111.471913,
    "BT_Mission Critical Log Sq Ft * Contract_BB": -64.404087,
    "Log Sq Ft^2": 7.813474,
    "Log Sq Ft Levels": -127.235098,
    "Log Sq Ft Levels * Log Sq Ft": 26.24594,
    "Log Sq Ft Levels * Scope_NEW": 0.226775,
    "Log Sq Ft Levels * Contract_BB": -127.235098,
    "Log Sq Ft Log Sq Ft * Contract_BB": 7.813474,
    "Levels^2": 25.229723,
    "Levels Levels * Log Sq Ft": 127.108072,
    "Levels Levels * Scope_NEW": -41.614663,
    "Levels Levels * Contract_BB": 25.229723,
    "Levels Log Sq Ft * Contract_BB": -127.235098,
    "Levels * Log Sq Ft^2": -18.75231,
    "Levels * Log Sq Ft Levels * Scope_NEW": 15.516692,
    "Levels * Log Sq Ft Levels * Contract_BB": 127.108072,
    "Levels * Log Sq Ft Log Sq Ft * Contract_BB": 26.24594,
    "Levels * Scope_NEW^2": -41.614663,
    "Levels * Scope_NEW Levels * Contract_BB": -41.614663,
    "Levels * Scope_NEW Log Sq Ft * Contract_BB": 0.226775,
    "Levels * Contract_BB^2": 25.229723,
    "Levels * Contract_BB Log Sq Ft * Contract_BB": -127.235098,
    "Log Sq Ft * Contract_BB^2": 7.813474,
}

def make_features(scope, contract, btype, sqft, levels):
    log_sqft = np.log(sqft)
    feats = dict.fromkeys(coefs.keys(), 0.0)

    # Continuous
    feats["Log Sq Ft"] = log_sqft
    feats["Levels"] = levels
    feats["Levels * Log Sq Ft"] = levels * log_sqft
    feats["Levels * Scope_NEW"] = levels if scope == "NEW" else 0.0
    feats["Levels * Contract_BB"] = levels if contract == "BB" else 0.0
    feats["Log Sq Ft * Contract_BB"] = log_sqft if contract == "BB" else 0.0

    # Scope flags
    feats["Scope_NEW"] = 1.0 if scope == "NEW" else 0.0
    feats["Scope_RENO"] = 1.0 if scope == "RENO" else 0.0
    feats["Scope_EXP"] = 1.0 if scope == "EXP" else 0.0
    feats["Scope_B.O."] = 1.0 if scope == "B.O." else 0.0
    feats["Scope_DEMO\nNEW"] = 1.0 if scope == "DEMO\nNEW" else 0.0
    feats["Scope_NEW\nRENO"] = 1.0 if scope == "NEW\nRENO" else 0.0

    # Contract
    feats["Contract_BB"] = 1.0 if contract == "BB" else 0.0

    # Building type
    bt_key = "BT_" + btype
    if bt_key in feats:
        feats[bt_key] = 1.0

    return feats

# App Interface
st.title("📐 BIM Coordination Duration Estimator")

start_date = st.date_input("Start Date", value=datetime.today())
scope = st.selectbox("Scope", ["NEW", "RENO", "EXP", "B.O.", "DEMO\nNEW", "NEW\nRENO"])
contract = st.selectbox("Contract Type", ["BB", "DA", "AB"])
btype = st.selectbox("Building Type", [
    "Civic/Specialty", "Commercial", "Education", "Healthcare",
    "Hospitality/Residential", "Industrial", "Mission Critical"
])
sqft = st.number_input("Square Footage", min_value=1000, value=50000)
levels = st.number_input("Levels", min_value=1, value=1)

if st.button("Predict Duration"):
    feats = make_features(scope, contract, btype, sqft, levels)
    duration = intercept + sum(feats.get(k, 0.0) * v for k, v in coefs.items())
    end_date = start_date + timedelta(days=round(duration))
    st.success(f"📅 Predicted End Date: {end_date.strftime('%Y-%m-%d')}")
    st.info(f"🕒 Predicted Duration: {round(duration)} days")
