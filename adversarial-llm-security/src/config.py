from dotenv import load_dotenv

load_dotenv()

MAX_ROUNDS = 5
ALERT_THRESHOLD = 0.7

ATTACKER_MODEL = "llama3.2"
DEFENDER_MODEL = "llama3.2"

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587