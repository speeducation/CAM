from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

#PARA GESTIONAR EL ADMINISTRADOR DE USUARIOS DE NUESTRO MODELO
class UserManager(BaseUserManager):

    #FUNCION PARA CREAR UN USUARIO GENERAL
    def _create_user(self, username, email, password, is_staff, is_superuser, **extra_fields):
        if not email:
            return ValueError('El email debe ser requerido')

        email = self.normalize_email(email)
        user = self.model(username=username, email=email, is_active=True, is_staff=is_staff, is_superuser=is_superuser,
                          **extra_fields)

        user.set_password(password)
        user.save(using=self._db)
        return user

    #FUNCION PARA CREAR UN USUARIO SIN PRIVELEGIOS DE SUPERUSUARIO
    def create_user(self, username, email, password=None, **extra_fields):
        return self._create_user(username, email, password, False, False, **extra_fields)

    #FUNCION PARA CREAR UN USUARIO CON PRIVELEGIOS DE SUPERUSUARIO
    def create_superuser(self, username, email, password, **extra_fields):
        return self._create_user(username, email, password, True, True, **extra_fields)

#MODELO DEL USUARIO AGREGAR AL SISTEMA
class User(AbstractBaseUser, PermissionsMixin):

    username =  models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=50, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    #PARA OBTENER ELEMENTOS DE NUESTRO MODELO SE HACE POR MEDIO DE OBJECTS
    objects = UserManager()

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def get_short_name(self):
        return self.username