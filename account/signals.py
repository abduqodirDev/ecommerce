from datetime import datetime, timedelta

from django.db.models.signals import post_save
from django.dispatch import receiver

from account.models import User, VerificationOtp
from account.utils import generate_code, send_email


@receiver(post_save, sender=User)
def create_verification_otpcode(sender, instance, created, **kwargs):
    if created:
        code = generate_code()
        VerificationOtp.objects.create(user=instance, type='1',
                                       code=code, expires_at=datetime.now()+timedelta(minutes=5))

        print('code:', code)
        send_email(code, instance.email)



