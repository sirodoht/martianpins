from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from main import models


class MartianUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = models.MartianUser
        fields = ["username", "email"]


class MartianUserChangeForm(UserChangeForm):
    class Meta:
        model = models.MartianUser
        fields = ["username", "email", "about"]


class CreateHashPin(forms.ModelForm):
    class Meta:
        model = models.Pin
        fields = ["name", "ipfs_hash"]
