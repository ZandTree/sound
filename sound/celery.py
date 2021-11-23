import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sound.settings')

app = Celery('sound',broker='redis://localhost')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


# each 30 sec min create a new user ( no argumnets)
# app.conf.beat_schedule = {
#     'create-new-users':{
#         'task':'users.tasks.create_new_user',
#         'schedule':30.0
#     }
# }