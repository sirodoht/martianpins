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
