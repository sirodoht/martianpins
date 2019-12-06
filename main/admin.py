from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from main import forms, models


class MartianUserAdmin(UserAdmin):
    add_form = forms.MartianUserCreationForm
    form = forms.MartianUserChangeForm
    model = models.MartianUser
    list_display = ["email", "username", "about"]


admin.site.register(models.MartianUser, MartianUserAdmin)


class PinAdmin(admin.ModelAdmin):
    list_display = ("name", "ipfs_file", "user")


admin.site.register(models.Pin, PinAdmin)


class IPFSFileAdmin(admin.ModelAdmin):
    list_display = ("ipfs_hash",)


admin.site.register(models.IPFSFile, IPFSFileAdmin)
