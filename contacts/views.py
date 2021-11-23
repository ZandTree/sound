from django.shortcuts import render
from django.http import HttpResponse
from contacts.tasks import send_mail_user

def send_contact(request):
    """ test for sending email"""
    print('sending email via celery')
    send_mail_user.delay()
    return HttpResponse('<h1>There is a contact app with celery</h1>')

