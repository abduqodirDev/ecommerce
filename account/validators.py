from django.core.exceptions import ValidationError


def check_otp_code(obj):
    if len(str(obj)) == 6 and str(obj).isdigit():
        return True
    else:
        raise ValidationError("Otp code is not valid")