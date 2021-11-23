from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from celery import shared_task


User = get_user_model()

@shared_task
def send_mail_user():
    send_mail('sweat dreams tonight','main email content for tata','tata-admin@mail.com',['alexriet2001@gmail.com']) 
    return "mail has been sent"
