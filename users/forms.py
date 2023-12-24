from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
from .models import User


class UserCreationForm(UserCreationForm):
    avatar = forms.ImageField(label='Avatar', required=False)

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ("first_name", "last_name", "username", "phone_number", "avatar")


class UserChangeForm(UserChangeForm):
    password = None
    class Meta:
        model = get_user_model()
        fields = (
            "email",
            "first_name",
            "last_name",
            "username",
            "phone_number",
            "avatar"
        )