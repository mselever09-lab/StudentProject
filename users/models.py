from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, phone_number, password=None, **extra_fields):
        if not phone_number:
            raise ValueError('Телефон є обов’язковим')
        
        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password) # Це зашифрує пароль
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('role', 'ADMIN') # Даємо роль адміна
        
        return self.create_user(phone_number, password, **extra_fields)


class User(AbstractUser):
    username = None

    phone_number = models.CharField(max_length=15, unique=True)

    ROLE_CHOICES = (
        ('ADMIN','Administrator'),
        ('TEACHER', 'Teacher'),
    )

    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='TEACHER') 

    USERNAME_FIELD = 'phone_number' #вказуєм що номер тепер і є логіном
    REQUIRED_FIELDS = []
    objects = UserManager()

    def ___str___(self):
        return f"{self.phone_number} ({self.role})"


    