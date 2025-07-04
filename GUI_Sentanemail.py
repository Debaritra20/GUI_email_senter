import smtplib

sender = "debaabiswas65@gmail.com"
reciever = "biswasabhra69@gmail.com"
password = "pyhz fzgr ybvq lneq"
subject = "python email test"
body = "Hii! boss,I wrote an email to u "

message = f"""From: Debaritra{sender}
To: Pepsi :{reciever}
Subject: {subject}\n
{body}"""

server = smtplib.SMTP("smtp.gmail.com",587)
server.starttls()

try:
    server.login(sender,password)
    print("Logged in succesfully")
    server.sendmail(sender,reciever,message)
    print("Email has been sent")
    
except smtplib.SMTPAuthenticationError:
   print("Authentication failed")
    