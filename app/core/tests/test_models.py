from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Prueba que verifica que se crea un usuario correctamente"""

        email = "test@test.com"
        password = 'test123'

        user = get_user_model().objects.create_user(
            email = email,
            password = password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Prueba que el email del nuevo usuario este normalizado"""

        email = 'test@TEST.COM'
        password = 'test123'
        user = get_user_model().objects.create_user(
            email = email,
            password = password
        )

        self.assertEqual(user.email, email.lower())
    
    def test_new_user_invalid_email(self):
        """Prueba que indica si un email es invalido"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_create_superuser(self):
        """Prueba que indica si se crea un superusuario correctamente"""

        user = get_user_model().objects.create_superuser(
            email='test@test.com',
            password = 'test123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
