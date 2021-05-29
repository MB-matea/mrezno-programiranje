import smtplib
import datetime

smtp_server ="mail.aspira.hr"
port = 587
sender_email = "matea.beslic@aspira.hr"
receiver_email = "mateabeslic1@gmail.com"
password = input("Unesi lozinku: ")

content = "From: matea.beslic@aspira.hr\nSubject: SMTP - slanje maila\n\nPozdrav profesore, trenutno vrijeme je: " + datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S") + ". Matea Beslic, vjezba8 - SMTP slanje maila."

mail = smtplib.SMTP(smtp_server, port)

mail.ehlo()
mail.starttls()
mail.login(sender_email, password)

mail.sendmail(sender_email, receiver_email, content)

mail.close()

