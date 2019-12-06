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


class PinCreationForm(forms.ModelForm):
    class Meta:
        model = models.Pin
        fields = ["name"]


class PinDeletionForm(forms.ModelForm):
    class Meta:
        model = models.Pin
        fields = ["id"]


class IPFSFileForm(forms.ModelForm):
    class Meta:
        model = models.IPFSFile
        fields = ["ipfs_hash"]


class UploadIPFSFileForm(forms.Form):
    ipfs_file = forms.FileField()
