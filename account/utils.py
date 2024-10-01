import secrets

from django.core.mail import send_mail

from config.settings.base import EMAIL_HOST


def generate_code():
    numbers = '123456789'
    return ''.join(secrets.choice(numbers) for _ in range(6))
