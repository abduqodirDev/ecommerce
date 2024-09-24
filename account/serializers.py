from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from account.models import User


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password')


class VerificationOtpSerializer(serializers.Serializer):
    code = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)

    def validate(self, data):
        code = data.get('code')
        email = data.get('email')
        if len(str(code)) != 6 or not str(code).isdigit():
            context = {
                'status': False,
                'message':'code is not valid'
            }
            raise ValidationError(context)

        return data


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)



