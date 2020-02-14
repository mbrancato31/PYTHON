from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pathlib import Path
from string import Template
import smtplib

template = Template(Path("python\\course\\7\\template.html").read_text)


message = MIMEMultipart()
message["from"] = "Maurizio Brancato"
message["to"] = "axeld550@gmail.com"
message["subject"] = "prueba email desde python"
body = template.substitute(name="John")
message.attach(MIMEText(body, "html"))
message.attach(MIMEImage(Path("algo.png").read_bytes()))

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("solution.amj@gmail.com", "Perseverancia1!")
    smtp.send_message(message)
    print("sent...")
