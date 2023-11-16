from django import forms
from django.core.exceptions import ValidationError

from users.models import Role, User


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("email", "password", "first_name", "last_name", "role")


def clean_role(self):
    role = self.cleaned_data["role"]
    if role not in ["junior", "senior"]:
        raise ValidationError('Invalid role. Choose between "junior" and "senior".')
    return role
