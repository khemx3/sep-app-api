from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful"""
        email = 'test@gmail.com'
        password = '1234'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized"""
        email = 'test@GMAIL.com'
        user = get_user_model().objects.create_user(email, '1234')
        
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalie_email(self):
        """Test crreating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, '1234')

    def test_create_new_superuser(self):
        """Test creaing new superuser"""
        user = get_user_model().objects.create_superuser(
            'test@gmail.com',
            '1234'
        )
        
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
