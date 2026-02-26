from src.attacker import generate_attack
from src.defender import classify_prompt
from src.risk_engine import compute_risk
from src.database import Session, SimulationLog
from src.incident_service import send_alert
from src.config import MAX_ROUNDS

def run_simulation():

    session = Session()
    history = []
    incident_triggered = False  # per inviare email solo 1 volta

    for round_num in range(1, MAX_ROUNDS + 1):

        # Genera prompt dall'attacker
        prompt = generate_attack(history)

        # Ground truth (tutti gli attacchi generati sono malicious)
        ground_truth = "malicious"

        # Classifica prompt con il defender
        classification, confidence = classify_prompt(prompt)

        # Calcola risk score e attack_success
        risk_score, attack_success, incident_flag = compute_risk(
            classification,
            confidence,
            ground_truth
        )

        # Salva log su DB
        log = SimulationLog(
            round=round_num,
            prompt=prompt,
            ground_truth=ground_truth,
            classification=classification,
            confidence=confidence,
            risk_score=risk_score,
            attack_success=attack_success,
            incident_flag=incident_flag
        )
        session.add(log)
        session.commit()

        # Aggiorna history
        history.append(prompt)
        
        # Stampa debug
        print(
            f"Round {round_num}: classification={classification}, "
            f"confidence={confidence:.2f}, risk_score={risk_score:.2f}, "
            f"attack_success={attack_success}, incident_flag={incident_flag}"
        )

        # Email alert (solo la prima volta che attack_success = True)
        if attack_success and not incident_triggered:
            send_alert(round_num, risk_score, prompt)
            incident_triggered = True

        

    session.close()
    
    
    
