# from datetime import datetime, timezone
from datetime import datetime, timedelta

from django.shortcuts import render
from django.utils import timezone
from rest_framework import status
from rest_framework.exceptions import APIException, ValidationError
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from account.models import User, VerificationOtp
from account.serializers import UserCreateSerializer, VerificationOtpSerializer, LoginSerializer, \
PasswordResetSerializer, PasswordResetVerifySerializer, PasswordResetFinishSerializer
from account.utils import generate_code, send_email


class UserCreateView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer

    def perform_create(self, serializer):
        user = serializer.save()
        password = serializer.data['password']
        user.set_password(password)
        user.is_active=False
        user.save()


class VerificationOtpView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            data = request.data
            serializer = VerificationOtpSerializer(data=data)
            serializer.is_valid(raise_exception=True)
            user = User.objects.get(email=data.get('email'))
            sms = VerificationOtp.objects.filter(code=data.get('code'), user=user, type='1',
                                                 is_confirmed=False)
            if not sms.exists():
                context = {
                    'status':False,
                    'message':'code is wrong'
                }
                raise ValidationError(context)

            sms = sms.order_by('-id').first()
            if sms.expires_at <= timezone.localtime(timezone.now()):
                context = {
                    'status':False,
                    'message':'code is not actived'
                }
                raise ValidationError(context)

            user.is_active=True
            sms.is_confirmed=True
            user.save()
            sms.save()

            return Response({'status':True,'message':'code have been confirmed'}, status=status.HTTP_200_OK)

        except User.DoesNotExist:
            context = {
                'status': False,
                'message': 'User not found'
            }
            raise ValidationError(context)

        except Exception as e:
            raise e


class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        password = data.get('password')
        serializer = LoginSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        user = User.objects.filter(email=data.get('email'))
        if not user.exists():
            data = {
                'status': False,
                'message': 'User not found'
            }
            raise ValidationError(data)
        user = user.first()
        if not user.check_password(password):
            data = {
                'status': False,
                'message': 'Password is not correct'
            }
            raise ValidationError(data)

        refresh = RefreshToken.for_user(user)
        data = {
            'status': True,
            "username": user.username,
            "access": str(refresh.access_token),
            "refresh_token": str(refresh)
        }
        return Response(data, status=status.HTTP_200_OK)


class PasswordResetView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            data = request.data
            serializer = PasswordResetSerializer(data=data)
            serializer.is_valid(raise_exception=True)
            user = User.objects.get(email=serializer.validated_data.get('email'))
            code = generate_code()
            VerificationOtp.objects.create(user=user, type='2',
                                           code=code, expires_at=datetime.now() + timedelta(minutes=5))
            send_email(code, user.email)
            context = {
                'status': True,
                'message': 'send code your email address'
            }
            return Response(context)

        except User.DoesNotExist:
            context = {
                'status': False,
                'message': 'User does not found'
            }
            raise ValidationError(context)

        except Exception as e:
            raise e


class PasswordResetVerifyView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            data = request.data
            serializer = PasswordResetVerifySerializer(data=data)
            serializer.is_valid(raise_exception=True)
            user = User.objects.get(email=serializer.validated_data.get('email'))
            sms = VerificationOtp.objects.filter(code=data.get('code'), user=user, type='2',
                                                 is_confirmed=False, expires_at__gte=datetime.now())
            if not sms.exists():
                context = {
                    'status': False,
                    'message': 'code is wrong'
                }
                raise ValidationError(context)
            sms = sms.order_by('-id').first()
            sms.is_confirmed=True
            sms.save()
            context = {
                'status': True,
                'message': 'successfully',
                'verification': sms.id
            }
            return Response(context)

        except User.DoesNotExist:
            context = {
                'status': False,
                'message': 'User not found'
            }
            raise ValidationError(context)

        except Exception as e:
            raise e


class PasswordResetFinishView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            data = request.data
            serializer = PasswordResetFinishSerializer(data=data)
            serializer.is_valid(raise_exception=True)
            user = User.objects.get(email=serializer.validated_data.get('email'))
            sms = VerificationOtp.objects.get(user=user, type='2', id=serializer.validated_data.get('id'))
            password = data['password']
            user.set_password(password)
            user.save()
            context = {
                'status': True,
                'message': 'Successfully'
            }
            return Response(context)

        except User.DoesNotExist:
            context = {
                'status': False,
                'message': 'User not found'
            }
            raise ValidationError(context)

        except VerificationOtp.DoesNotExist:
            context = {
                'status': False,
                'message': 'sms id is wrong'
            }
            raise ValidationError(context)

        except Exception as e:
            raise e

