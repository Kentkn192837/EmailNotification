from smtplib import SMTP_SSL
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import formatdate
import ssl

class GetConfig:
    def __init__(self, path):
        with open(path, encoding='utf-8') as fp:
            l = fp.readlines()
        l = [line.replace('\n', '') for line in l]
        self.user = l[0]
        self.password = l[1]
        self.host = l[2]
        self.port = l[3]

class CreateMail:
    def __init__(self, subject, from_email_address, to_email_address, message):
        self.subject = subject
        self.from_email_address = from_email_address
        self.to_email_address = to_email_address
        self.message = message
    
    def send(self, user, password, host, port):
        msg = MIMEText(self.message, "plain")
        msg["Subject"] = self.subject
        msg["From"] = self.from_email_address
        msg["To"] = self.to_email_address
        msg["Date"] = formatdate()

        context = ssl.create_default_context()
        server = SMTP_SSL(host, port, context=context)
        if server.has_extn('STARTTLS'):
            server.starttls()
        server.login(user, password)
        server.send_message(msg)
        server.quit()
