from django.core.exceptions import ValidationError


def UrlCheckValidator(obj):
    data = ["https://www.instagram.com", "https://instagram.com", "http://instagram.com"]
    for i in data:
        if str(obj).startswith(i):
            return True
        else:
            raise ValidationError('Url in not valid!')
