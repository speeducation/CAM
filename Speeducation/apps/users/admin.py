from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin

from .models import User

class UserAdmin(UserAdmin):

    fieldsets = (
        ('User', {'fields' : ('username', 'password')}),

        ('Persona Info', {'fields' : ('first_name',
                                       'last_name',
                                       'email')}),

        ('Persmissions', {'fields' : ('is_active',
                                     'is_staff',
                                     'is_superuser',
                                     'groups',
                                     'user_permissions')}),
    )

admin.site.register(User, UserAdmin)