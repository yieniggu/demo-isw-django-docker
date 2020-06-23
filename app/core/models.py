from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
                                        PermissionsMixin

class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        """Crea un nuevo usuario con email y password"""
        if not email:
            raise ValueError('Se debe especificar un correo valido!')
        
        user = self.model(email=self.normalize_email(email), **extra_fields)

        # Password encriptada
        user.set_password(password)

        user.save(using=self._db)

        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """Crea un superusuario con email y password"""

        superuser = self.create_user(email, password, **extra_fields)

        superuser.is_superuser = True
        superuser.is_staff = True

        superuser.save(using=self._db)

        return superuser

class User(AbstractBaseUser, PermissionsMixin):
    """Modelo personalizado de usuario que permite el uso de
        email en vez de username"""

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'


