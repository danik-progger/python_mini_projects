import smtplib
import os
from dotenv import load_dotenv
load_dotenv()


def send_email(frm: str, app_password: str, to: str, subject: str, body: str):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(frm, app_password)

    msg = f'Subject: {subject}\n\n{body}'
    server.sendmail(frm, to, msg)
    server.quit()


if __name__ == "__main__":
    frm = input("Enter your email: ")
    to = input("Enter receiver email: ")
    subj = input("Enter subject of the email: ")
    body = input("Enter body of the email: ")

    password = os.environ.get("PASSWORD")

    send_email(frm, password, to, subj, body)
