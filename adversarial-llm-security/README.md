![Dashboard](docs/dashboard_1.png)

# 🔐 Adversarial LLM Security Simulator

A simulation framework for testing adversarial prompt injection attacks against Large Language Models (LLMs), with risk scoring, incident detection, and a Streamlit dashboard for monitoring results.

## 🚀 Project Overview

This project simulates an adversarial environment where:

- 🤖 An **Attacker LLM** generates prompt injection attempts
- 🛡 A **Defender LLM** classifies inputs as benign or malicious
- 📊 A **Risk Engine** computes a dynamic risk score
- 🚨 Incidents are flagged based on configurable thresholds
- 📧 An **incident_service** sends and email alerting the user
- 📈 A **Streamlit Dashboard** visualizes metrics and attack success rate

The goal is to study and measure LLM robustness against prompt injection attacks.

---

## 🧠 Architecture
adversarial-llm-security/
│
├── main.py # Simulation entrypoint
├── requirements.txt
├── README.md
│
├── dashboard/
│ └── dashboard.py # Streamlit monitoring UI
│
├── src/
│ ├── _init_.py
| |── config.py
│ ├── attacker.py 
│ ├── controller.py
│ ├── incident_service.py
│ ├── defender.py
│ ├── risk_engine.py
│ ├── metrics.py
│ ├── database.py
│
└── tests/
│ ├── test_email.py


---

## ⚙️ Features

- Adversarial prompt generation
- Defender classification with confidence score
- Risk score computation
- Incident detection threshold
- Persistent logging (SQLite via SQLAlchemy)
- Real-time Streamlit dashboard
- Metrics computation:
  - Attack success rate
  - Average risk score
  - Incident count
  - Confidence distribution

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/your-username/adversarial-llm-security.git
cd adversarial-llm-security

Create virtual environment:
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows

Install dependencies:
pip install -r requirements.txt

## ▶️ Run Simulation
python main.py

## 📊 Run Dashboard
streamlit run dashboard/dashboard.py
```
![Debug](docs/debug.png)

## 🎯 Learning Goals

- LLM adversarial robustness

- AI security evaluation

- Risk modeling systems

- Clean project architecture

- Monitoring dashboards

- Alerting with emails

![Email](docs/attack_email.png)

Project schema:
![Project_Schema](docs/schemaa.png)

## ⚠️ Disclaimer

This project is for educational and research purposes only.
It simulates adversarial behaviors to improve defensive AI systems.
