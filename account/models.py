from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

from account.manager import CustomManager
from account.validators import check_otp_code


class User(AbstractUser):
    phone_number = models.CharField(max_length=30, validators=[RegexValidator(regex=r'^\+998(90|91|93|94|95|97|98|99|33|88)\d{7}$')])
    address = models.TextField()
    email = models.EmailField("email address", unique=True)
    username = None

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    objects = CustomManager()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class VerificationOtp(models.Model):
    VERIFY_TYPE = (('1', 'REGISTER'), ('2', 'RESET_PASSWORD'))

    user = models.ForeignKey('account.User', on_delete=models.CASCADE, related_name='verification_otp')
    code = models.IntegerField(validators=[check_otp_code])
    type = models.CharField(max_length=1, choices=VERIFY_TYPE)
    expires_at = models.DateTimeField()
    is_confirmed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user} | code: {self.code}"

    class Meta:
        verbose_name = 'Verification otp'
        verbose_name_plural = 'Verification otps'


class UserAddress(models.Model):
    user = models.ForeignKey('account.User', on_delete=models.CASCADE, related_name='user_address')
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=30, validators=[RegexValidator(regex=r'^\+998(90|91|93|94|95|97|98|99|33|88)\d{7}$')])
    apartment = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    city = models.ForeignKey('common.Region', on_delete=models.CASCADE, blank=True, null=True)
    pin_code = models.CharField(max_length=30)

    def __str__(self):
        return  f"{self.user} | {self.name}"

    class Meta:
        verbose_name = 'User address'
        verbose_name_plural = 'User addresses'

