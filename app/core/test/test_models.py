from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTest(TestCase):
    def test_create_user_with_email_successfull(self):
        """create user with email and password """
        email = "pratikveer@demo.com"
        password = "test@1234"
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalize(self):
        email = "pratikveer@DEMO.COM"
        user = get_user_model().objects.create_user(email, "abcd")

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """ Test craeting user with no email raises error"""
        with self.assertRaises(
            ValueError
        ):  # hyachya khali je sentense astil te valuerror detata check krtoo
            get_user_model().objects.create_user(None, "test")
        # if raise error by above senetence then it test pass

    def test_creating_new_superuser(self):
        """ Test creating new superuser """
        user = get_user_model().objects.create_superuser(
            "admin@demo.com", "admin@1234")

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
