from django.contrib import admin

# Register your models here.
#AGREGAR MODELOS DE APP SECURITY

from .models import SystemUser, Permit

admin.site.register(SystemUser)
admin.site.register(Permit)
