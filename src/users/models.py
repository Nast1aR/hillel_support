from django.db import models
import uuid


class Role(models.Model):
    value = models.CharField(max_length=15)


class User(models.Model):
    email = models.CharField(max_length=40)
    password = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    role = models.CharField(max_length=15)
    is_active = models.BooleanField(default=False)

    class ActivationKey(models.Model):
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        key = models.UUIDField(unique=True)
