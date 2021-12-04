import os
from celery import Celery
from celery.schedules import crontab
# from celery.signals import setup_logging


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sound.settings')

app = Celery('sound',broker='redis://localhost')

# prefix == CELERY in settings.py + where to look for all constants in settings.py
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()



# each 30 sec min create a new user ( no argumnets)
app.conf.beat_schedule = {
    'greet-each-five-min':{
        'task':'contacts.tasks.say_greetings_beat',
        #
        'schedule':crontab(minute='*/1')
    }
}

# TODO no output in console with logging

# @setup_logging.connect
# def config_loggers(*args,**kwargs):
#     from logging.config import dictConfig
#     from django.conf import settings

#     dictConfig(settings.LOGGING)
