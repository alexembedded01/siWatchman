import smtplib
from email.message import EmailMessage

def emailAlert(subject, body, to):
    msg = EmailMessage()
    msg.set_content(body)

    user = "alexembedded01@gmail.com"
    password = "ahbplwiktuanuhds"
    
    msg['subject'] = subject
    msg['to'] = to
    msg['from'] = user

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user, password)
    server.send_message(msg)

    server.quit()