import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from dotenv import load_dotenv

load_dotenv()

def send_alert(round_num, risk_score, prompt):

    message = Mail(
        from_email=os.getenv("EMAIL_SENDER"),
        to_emails=os.getenv("EMAIL_RECEIVER"),
        subject="🚨 LLM Defense Compromised",
        html_content=f"""
        <h2>🚨 Attack Detected</h2>
        <p><b>Round:</b> {round_num}</p>
        <p><b>Risk Score:</b> {risk_score}</p>
        <p><b>Prompt:</b></p>
        <pre>{prompt}</pre>
        """
    )

    try:
        sg = SendGridAPIClient(os.getenv("SENDGRID_API_KEY"))
        response = sg.send(message)
        print("✅ Email sent. Status:", response.status_code)
    except Exception as e:
        print("❌ Email error:", str(e))