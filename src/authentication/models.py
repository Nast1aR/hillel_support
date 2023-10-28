from django.db import models
from django.core.exceptions import ValidationError


def validate_role(value):
    if value not in ["junior", "senior"]:
        raise ValidationError('Invalid role. Choose from "junior" or "senior".')


class User(models.Model):
    email = models.CharField(max_length=40)
    password = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    role = models.CharField(max_length=10, default="junior", validators=[validate_role])
