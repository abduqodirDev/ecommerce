from django.test import TestCase
from django.urls import reverse

from account.models import User, VerificationOtp


class CreateUserTestCase(TestCase):
    def test_create_user(self):
        response = self.client.post(reverse('register'), data={
            "first_name": "abduqodir",
            "last_name": "dusmurodov",
            "email": "test@gmail.com",
            "password": "kiber4224"
        }
                           )

        user = User.objects.get(id=1)

        self.assertEqual(User.objects.all().count(), 1)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(user.first_name, "abduqodir")
        self.assertEqual(user.last_name, "dusmurodov")
        self.assertEqual(user.email, "test@gmail.com")
        self.assertTrue(user.check_password("kiber4224"))

        self.assertFalse(user.is_active)

        self.assertEqual(len(response.data), 4)
        self.assertEqual(response.data['password'], "kiber4224")
        self.assertEqual(response.data['first_name'], "abduqodir")
        self.assertEqual(response.data['last_name'], "dusmurodov")
        self.assertEqual(response.data['email'], "test@gmail.com")

    def test_create_user_with_invalid_email(self):
        response = self.client.post(reverse('register'), data={
            "first_name": "abduqodir",
            "last_name": "dusmurodov",
            "email": "testgmail.com",
            "password": "kiber4224"
        })

        self.assertEqual(response.data['email'][0], "Enter a valid email address.")
        self.assertEqual(response.status_code, 400)
        self.assertIn("email", response.data)

    def test_create_user_with_already_exist_email(self):
        user = User(first_name="abduqodir", last_name="dusmurodov", email="test@gmail.com")
        user.set_password("kiber4224")
        user.save()
        response = self.client.post(reverse('register'), data={
            "first_name": "abduqodir",
            "last_name": "dusmurodov",
            "email": "test@gmail.com",
            "password": "kiber4224"
        })

        self.assertEqual(response.data['email'][0], "User with this email address already exists.")
        self.assertEqual(response.status_code, 400)
        self.assertIn("email", response.data)

    def test_create_user_required_email_field(self):
        response = self.client.post(reverse('register'), data={
            "first_name": "abduqodir",
            "last_name": "dusmurodov",
            "password": "kiber4224"
        })

        self.assertEqual(response.status_code, 400)
        self.assertIn("email", response.data)
        self.assertEqual(response.data['email'][0], "This field is required.")

    def test_create_user_required_password_field(self):
        response = self.client.post(reverse('register'), data={
            "first_name": "abduqodir",
            "last_name": "dusmurodov",
            "email": "test@gmail.com"
        })

        self.assertEqual(response.status_code, 400)
        self.assertIn("password", response.data)
        self.assertEqual(response.data['password'][0], "This field is required.")


class VerifyOtpCodeTestCase(TestCase):
    def setUp(self):
        self.user = User(first_name="abduqodir", last_name="dusmurodov", email="test@gmail.com")
        self.user.set_password("kiber4224")
        self.user.save()
        self.sms = VerificationOtp.objects.get(user=self.user)

    def test_verify_otp(self):
        response = self.client.post(reverse('verify'), data={
            "code": self.sms.code,
            "email": self.user.email
        })
        self.sms.refresh_from_db()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['status'], True)
        self.assertEqual(response.data['message'], "code have been confirmed")
        self.assertEqual(len(response.data), 2)
        self.assertTrue(self.user.is_active)
        self.assertTrue(self.sms.is_confirmed)

    def test_invalid_verify_otp(self):
        response = self.client.post(reverse('verify'), data={
            "code": "123456",
            "email": self.user.email
        })
        self.sms.refresh_from_db()
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data['message'], "code is wrong")
        self.assertEqual(response.data['status'], "False")
        self.assertFalse(self.sms.is_confirmed)
        # self.assertFalse(self.user.is_active)

    def test_verify_notexist_email(self):
        response = self.client.post(reverse('verify'), data={
            "code": "123456",
            "email": "wrongemail@gmail.com"
        })
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data['status'], "False")
        self.assertEqual(response.data['message'], "User not found")
        self.assertEqual(len(response.data), 2)

    def test_verify_required_code(self):
        response = self.client.post(reverse('verify'), data={
            "email": "test@gmail.com"
        })
        self.assertEqual(response.status_code, 400)
        print("response: ", response.data)
        self.assertEqual(response.data['code'][0], "This field is required.")
        self.assertIn("code", response.data)

    def test_verify_required_email(self):
        response = self.client.post(reverse('verify'), data={
            "email": "test@gmail.com"
        })
        self.assertEqual(response.status_code, 400)
        print("response: ", response.data)
        self.assertEqual(response.data['code'][0], "This field is required.")
        self.assertIn("code", response.data)
