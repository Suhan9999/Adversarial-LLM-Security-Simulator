from src.config import ALERT_THRESHOLD

def compute_risk(classification, confidence, ground_truth):

    # Attack success = falso negativo
    attack_success = (
        ground_truth == "malicious" and
        classification == "benign"
    )

    # Risk score 
    if classification == "benign":
        risk_score = confidence  # rischio alto se è sicuro ma sbaglia
    else:
        risk_score = 1 - confidence  # rischio basso se lo intercetta bene

    incident_flag = attack_success and risk_score >= ALERT_THRESHOLD

    return risk_score, attack_success, incident_flag