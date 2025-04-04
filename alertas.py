# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 11:05:31 2024

@author: Rafael

Alert MAIL
"""

import smtplib
from email.message import EmailMessage

def email_alert(subject, body, to):
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = subject
    msg['to'] = to
    
    user = "rlopezotero@hospitalsanmartin.gob.ar"
    msg['from'] = user
    password = "Lor247523"
    
    server = smtplib.SMTP("mail.hospitalsanmartin.gob.ar", 587)
    server.starttls()
    server.login(user, password)
    server.send_message(msg)
    server.quit()
    
if __name__ == '__main__':
    email_alert("Hola", "Esto es un TEST para automatizar envios de correos electronicos", "riosjesica342@gmail.com")