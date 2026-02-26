import sys
import os
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(ROOT_DIR)
import streamlit as st
import pandas as pd
from src.database import Session, SimulationLog
from src.metrics import compute_metrics

st.title("Adversarial LLM Security Dashboard")

session = Session()
logs = session.query(SimulationLog).all()

if not logs:
    st.warning("No simulation data available.")
else:
    # Creazione DataFrame dai log
    data = pd.DataFrame([{
        "Timestamp": l.timestamp,
        "Round": l.round,
        "Risk Score": l.risk_score,
        "Classification": l.classification,
        "Ground Truth": l.ground_truth,
        "Attack Success": l.attack_success
    } for l in logs])

    # Ordiniamo e convertiamo timestamp in Europe/Rome
    data["Timestamp"] = pd.to_datetime(data["Timestamp"], utc=True)
    data = data.sort_values("Timestamp")
    data["Timestamp"] = data["Timestamp"].dt.tz_convert("Europe/Rome")

    # Aggiungiamo colonna "Email Sent": TRUE solo per il primo falso negativo
    data["Email Sent"] = False
    first_falso_negativo_idx = data.index[data["Attack Success"]].tolist()
    if first_falso_negativo_idx:
        data.at[first_falso_negativo_idx[0], "Email Sent"] = True

    # Mostriamo tabella completa
    st.subheader("📡 Attack Attempts Log")
    st.dataframe(data)

    # Tabella separata per Falsi Negativi (Attack Success)
    st.subheader("🚨 Falsi Negativi")
    falsi_negativi = data[data["Attack Success"]]
    if not falsi_negativi.empty:
        st.table(falsi_negativi[["Round", "Risk Score", "Classification", "Ground Truth", "Email Sent"]])
    else:
        st.info("Nessun falso negativo rilevato finora.")

    # Grafico rischio nel tempo
    st.subheader("📈 Risk Score Over Time")
    st.line_chart(data.set_index("Timestamp")["Risk Score"])

    # Metriche generali
    asr, avg_risk, robustness = compute_metrics()
    st.subheader("📊 Metrics")
    st.metric("Attack Success Rate", round(asr, 3))
    st.metric("Average Risk", round(avg_risk, 3))
    st.metric("Robustness Score", round(robustness, 3))

session.close()