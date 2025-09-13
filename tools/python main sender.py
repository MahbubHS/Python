"""
Python Mail Sender
Created by Alpha Z Security Organization (Admin)
Adnan Khan
"""

import smtplib
sender_mail = input("Enter Sender Mail: ")
receiver = input("Enter Receiver Mail: ")
subject = "Alpha Z Security"
Message = input("Enter Massage: ")
psk = input("Enter Google app Password: ")
text = f"Subject: {subject}\n\n{Message}"
server = smtplib.SMTP("smtp.gmail.com",587)
server.starttls()
server.login(sender_mail,psk)
server.sendmail(sender_mail,receiver,text)
print("Success")
