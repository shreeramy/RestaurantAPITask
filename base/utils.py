from django.conf import settings
import pyotp
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from datetime import datetime

def getotp():
    secret = pyotp.random_base32()
    totp = pyotp.TOTP(secret, interval=settings.INTERVAL_TIME)
    otp = totp.now()

    return {"otp":otp,"secret":secret}

def verify_otp(otp, secret):
    verify_otp = pyotp.TOTP(secret, interval=settings.INTERVAL_TIME)\
                             .verify(otp)

    return verify_otp


def send_otp(context, email, subject):
    email_from = settings.EMAIL_SENDER      
    message = render_to_string("otp_mail.html", 
                                {'context': context})
    mail= EmailMultiAlternatives(
    subject =subject,
    body=message,
    from_email=email_from,
    to=[email]
    )
    mail.attach_alternative(message, 'text/html')
    mail.send()


def get_today():
    today = datetime.now().date()
    return today