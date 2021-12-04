from django.shortcuts import render
from django.http import HttpResponse
from contacts.tasks import send_mail_user,say_greetings_beat,send_img


# def send_greet(request):
#     """ test for sending email"""
#     print('sending greetings')
#     say_greetings_beat.delay()
#     return HttpResponse('<h1>There is a contact app with celery</h1>')



def send_contact(request):
    """ test for sending email"""
    print('sending email via celery')    
    # send_mail_user.delay()  
    # # test async im upload via celery  
    send_img.delay()
    # send_img.apply_async(args=[localpath,path],ignore_result=True)
    
    return HttpResponse('<h1>There is a contact app with celery</h1>')

