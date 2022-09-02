from collections import UserString
from django.db import models
from django.contrib.auth.models import User

# Crear modelo de permit con campos - id: AutoField
# - permitName: CharField

class Permit(models.Model):
    permitName = models.CharField(max_length=50)

    def __str__(self):
        return self.permitName

# Crear modelo systemUser con los campos - id: AutoField, user: oneToOneField con User de django, y permit: ForeignKey con el modelo permit

class SystemUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    permit = models.ForeignKey(Permit, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

