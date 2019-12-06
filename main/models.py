from django.contrib.auth.models import AbstractUser
from django.db import models


class MartianUser(AbstractUser):
    about = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.username


class IPFSFile(models.Model):
    ipfs_hash = models.CharField(max_length=46)

    def __str__(self):
        return self.ipfs_hash


class Pin(models.Model):
    name = models.CharField(max_length=100)
    ipfs_file = models.ForeignKey(IPFSFile, on_delete=models.CASCADE)
    user = models.ForeignKey(MartianUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
