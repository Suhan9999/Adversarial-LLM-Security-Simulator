import pandas as pd
from src.database import Session, SimulationLog

def compute_metrics():

    session = Session()
    logs = session.query(SimulationLog).all()

    if not logs:
        return 0, 0, 0

    df = pd.DataFrame([{
        "attack_success": l.attack_success,
        "risk_score": l.risk_score,
        "ground_truth": l.ground_truth,
        "classification": l.classification
    } for l in logs])

    attack_success_rate = df["attack_success"].mean()
    avg_risk = df["risk_score"].mean()
    robustness_score = 1 - attack_success_rate

    session.close()

    return attack_success_rate, avg_risk, robustness_score