import smtplib
import datetime
import smtpd

SERVER = 'localhost'
PORT = 1025

FROM = "matea.beslic@test.com"
TO = ["myemailaddress@something.com"]

SUBJECT = "test"

TEXT = "Matea Beslic " + datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")

message = """\
From: %s
To: %s
Subject: %s
%s
""" % (FROM, ",".join(TO), SUBJECT, TEXT)

server = smtplib.SMTP(SERVER, PORT)
server.sendmail(FROM,TO,message)
server.quit()