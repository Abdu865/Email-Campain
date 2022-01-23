import smtplib, ssl
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pyexcel_ods import get_data
import pprint

wb = get_data('/home/abdullahhijazi/Documents/TestEmails.ods')
pprint.pprint(wb) # "Sheet1" -  0,x is email   -- 1,x is recepitant name --2,x is custom msg

for key in wb["Sheet1"]:
    print(key)

print(wb["Sheet1"][2][2])

for x in wb["Sheet1"][2]:
    if x == "":
        print("hit")
sender = "isthisausernameidontknow@gmail.com"
receivers = ["abdullahhijaziUMI@gmail.com",]
body_of_email_html = """\
<html>
    <head></head>
    <body>
        <p>
        Hello [CN]<br>
        My name is Abdullah Hijazi with Universal Meditech Incorporated. <br><br>
        We're a manufacturer of High Quality covid-19 antigen tests. Product infomration is attachment as SARS-COV-2 Antigen Rapid Test Colloidal Gold Kit.  Our tests are affordable, easy to use, and a positive result is granted in 2 minutes with 98% accuracy (detailed statistics in the attached product information).   Faster then PCR tests, our test is perfect for preventing an outbreak after a workplace exposure. <br><br> 

        We are confident that our product will fulfill your organization’s needs. If you are interested in purchasing our tests, getting some free samples, or have any further inquiries, please contact me anytime. <br> 

        Thank you!<br><br>
        Best regards,<br>
        Abdullah Hijazi<br>
        Sales Representative<br> 
        Universal Meditech Inc.<br> 
        1320 E. Fortune Ave #102. Fresno, CA 93725<br> 
        Direct 304-751-5596
        <img src="http://76.26.76.89/gif" alt="1x1 pxl">
        </p>
    </body>
</html> 
"""

path_to_file= "/home/abdullahhijazi/Documents/SARS-COV-2 Antigen Rapid Test Colloidal Gold Kit.pdf"#Attachment file

msg = MIMEMultipart()

with open(path_to_file, "rb") as f:
    # attach = email.mime.application.MIMEApplication(f.read(),_subtype="pdf")
    attach = MIMEApplication(f.read(), _subtype="pdf")
    attach.add_header('Content-Disposition', 'attachment', filename=str("SARS-COV-2 Antigen Rapid Test Colloidal Gold Kit"))
    msg.attach(attach)

msg.attach(MIMEText(body_of_email_html,'html'))
msg["subject"] = "test email 2" #email subject like  TODO:Customize to sender
msg["From"] = sender
msg["To"] = ','.join(receivers)

print(msg)
Password= input("enter password: ")

s = smtplib.SMTP_SSL(host= 'smtp.gmail.com',port = 465)
s.login(user=sender,password=Password)
s.sendmail(sender,receivers,msg.as_string())
s.quit()
