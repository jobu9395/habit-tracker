import os
import smtplib
from typing import List
from dotenv import load_dotenv

load_dotenv()

SMTP_HOST = os.environ.get('MAIL_SERVER')
SMTP_PORT = os.environ.get('MAIL_PORT')
SENDER = os.environ.get('ROOFHERO_USERNAME')
RECIPIENTS = os.environ.get('RECIPIENT_EMAIL')


def send_email(from_addr: str, to_addr: List[str], subject: str) -> None:
    msg = f"From: {from_addr}\r\nTo: {','.join(to_addr)}\r\nSubject: {subject}\r\n"
    
    with smtplib.SMTP(host=SMTP_HOST, port=SMTP_PORT) as server:
        server.starttls()
        server.login(SENDER, os.environ.get('ROOFHERO_PW'))
        server.sendmail(from_addr, to_addr, msg)


if __name__ == '__main__':
    send_email(SENDER, [RECIPIENTS], subject="RoofHero Lead")
