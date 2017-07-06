import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

SENDER = os.environ.get('MAIL_ADDRESS')
SERVER = os.environ.get('MAIL_SERVER')
PORT = os.environ.get('MAIL_PORT')
PASSWORD = os.environ.get('MAIL_PASSWORD')

def sendMail(client):
    msg = MIMEMultipart()
    msg['From'] = SENDER
    msg['To'] = client
    msg['Subject'] = "SUBJECT OF THE MAIL"

    body = "YOUR MESSAGE HERE"
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP(SERVER, PORT)
    server.starttls()
    try:
        server.login(SENDER, PASSWORD)
        text = msg.as_string()
        server.sendmail(SENDER, client, text)
    except:
        print 'error while login'

    server.quit()
