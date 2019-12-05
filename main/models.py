from django.contrib.auth.models import AbstractUser
from django.db import models


class MartianUser(AbstractUser):
    about = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.username


class Pin(models.Model):
    name = models.CharField(max_length=100)
    ipfs_hash = models.CharField(max_length=100)
    user = models.ForeignKey(MartianUser, on_delete=models.CASCADE)
