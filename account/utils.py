import secrets

from django.core.mail import send_mail

from config.settings.base import EMAIL_HOST


def send_email(code, email):
    message = f"Your OTP code is {code}"
    send_mail(subject = "Registration otp code", message=message, from_email = EMAIL_HOST, recipient_list = [email],
              fail_silently=True)


def generate_code():
    numbers = '123456789'
    return ''.join(secrets.choice(numbers) for _ in range(6))
