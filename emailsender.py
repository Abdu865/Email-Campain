import smtplib, ssl
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pyexcel_ods import get_data
import pprint
from emailcontents import email_contents

#wb = get_data('/home/abdullahhijazi/Documents/TestEmails.ods')
#pprint.pprint(wb) # "Sheet1" -  0,x is email   -- 1,x is recepitant name --2,x is custom msg

#for key in wb["Sheet1"]:
#    print(key)

#print(wb["Sheet1"][2][2])

#for x in wb["Sheet1"][2]:
#    if x == "":
#        print("hit")
print(email_contents)
sender = "isthisausernameidontknow@gmail.com"
receivers = ["abdullahhijaziUMI@gmail.com",]

path_to_file= "SARS-COV-2 Antigen Rapid Test Colloidal Gold Kit.pdf"#Attachment file

msg = MIMEMultipart()

with open(path_to_file, "rb") as f:
    # attach = email.mime.application.MIMEApplication(f.read(),_subtype="pdf")
    attach = MIMEApplication(f.read(), _subtype="pdf")
    attach.add_header('Content-Disposition', 'attachment', filename=str("SARS-COV-2 Antigen Rapid Test Colloidal Gold Kit"))
    msg.attach(attach)

msg.attach(MIMEText(email_contents,'html'))
msg["subject"] = "test email 2" #email subject like  TODO:Customize to sender
msg["From"] = sender
msg["To"] = ','.join(receivers)

print(msg)
Password= input("enter password: ")

s = smtplib.SMTP_SSL(host= 'smtp.gmail.com',port = 465)
s.login(user=sender,password=Password)
s.sendmail(sender,receivers,msg.as_string())
s.quit()
