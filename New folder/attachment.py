import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication


sender_email="addagirivenky@gmail.com"
sender_passwd="bexy hlsy iqkm ljxe"
recipient_email='hr.exec@wisdomleaf.com'

msg=MIMEMultipart()
msg['From']=sender_email
msg['To']=recipient_email
msg['Subject']=" coding test completed"


body=" completed "
msg.attach(MIMEText(body,'plain'))


filename='file.py'
with open(filename,'rb') as f:
    attachment=MIMEApplication(f.read(), _subtype='.py')
    attachment.add_header('content-Disposition','attachment',filename=filename)
    msg.attach(attachment)
    
with smtplib.SMTP_SSL('smtp.gmail.com',465,) as smtp:
    smtp.starttls
    smtp.login(sender_email,sender_passwd)
    smtp.send_message(msg)
        
    
