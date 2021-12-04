from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from celery import shared_task # version 5.2.1
from .s3client import upload_img


User = get_user_model()



@shared_task
def send_img():
    upload_img()
    return 'success'

    
@shared_task
def say_greetings_beat():    
    print("greetings")
    return "done"
    
@shared_task
def send_mail_user(): 
    print('Email sent Ok')   
    send_mail('sweat dreams tonight','main email content ','tata-admin@mail.com',['uuuu@gmail.com']) 
    return "mail has been sent"


