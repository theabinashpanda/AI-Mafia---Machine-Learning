import smtplib
import getpass
from email.mime.text import MIMEText
def send_email():
    senders_address='abinashpanda246@gmail.com'
    recipients_address=['abinashp13@icloud.com','abhishek2002panda@gmail.com']
    password=getpass.getpass()
    subject='""""Learn.Inspire.Grow.""""'
    msg='''
        Hello Everyone
        We are pleased to announce that we are going to start a new batch of AI Mafia,
        Hope you will join.

        Regards
        Abinash Panda  
    '''
    #server initialisation
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(senders_address,password) 
    msg=MIMEText(msg)
    msg['Subject']=subject
    msg['From']=senders_address
    msg['To']=','.join(recipients_address)
    msg.set_param('importance','high value')
    server.sendmail(senders_address,recipients_address,msg.as_string())
send_email()