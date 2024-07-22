import smtplib
from email.message import EmailMessage

email = EmailMessage()

email['from'] = 'Cauan Vital'
email['to'] = 'cauanvital74@gmail.com'
email['subject'] = 'Hello World!'

email.set_content('I shit myself...')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('email@email.email','password123')
    smtp.send_message(email)
