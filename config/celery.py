from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings

# Django config faylini yuklash
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.base')

# Celery ilovasini yaratish
app = Celery('config')

# Django sozlamalarini Celeryga o'zgartirish
app.config_from_object('django.conf:settings', namespace='CELERY')

# Django app-laridagi tasklarni avtomatik topish
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
