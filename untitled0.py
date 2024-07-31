from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

message = MIMEMultipart()
message["from"] = "Fayrouz Abd El Rahman"
message["to"] = "fayrouz.abdelrahman@ejust.edu.eg"
message["subject"] = "This is a test"
message.attach(MIMEText("Body"))

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("fayrouz.abdelrahman@ejust.edu.eg","fayrouzcookies")
    smtp.send_message(message)
    print("Sent...")
