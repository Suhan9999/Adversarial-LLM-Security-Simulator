# test_email.py used only for testing sendgrid
from src.incident_service import send_alert

send_alert(1, 0.95, "TEST PROMPT INJECTION")