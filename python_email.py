from pw import password, my_email
from email.message import EmailMessage
import ssl
import smtplib

def Email_function():
    email_sender = my_email
    email_password = password
    email_receiver = 'bran_thom@yahoo.com'
    subject = "This is an email sent from python"
    body = """
    You are doing great at  work. Don't forget to Buy, Buy and Sell, Sell. 
    """
    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com",465, context = context) as smtp:
        smtp.login(email_sender,email_password)
        smtp.sendmail(email_sender,email_receiver,em.as_string())
Email_function()