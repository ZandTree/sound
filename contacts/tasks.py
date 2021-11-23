from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from celery import shared_task


User = get_user_model()

@shared_task
def send_mail_user():
    send_mail('sweat dreams tonight','main email content ','tata-admin@mail.com',['uuuuu@gmail.com']) 
    return "mail has been sent"
