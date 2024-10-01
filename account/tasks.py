from celery import shared_task
from django.core.mail import send_mail

from config.settings.base import EMAIL_HOST


@shared_task
def send_otp_code_to_email(code, email):
    message = f"Your OTP code is {code}"
    send_mail(subject="Registration otp code", message=message, from_email=EMAIL_HOST, recipient_list=[email],
              fail_silently=True)

@shared_task
def simple_task():

    return "Task is working..."
