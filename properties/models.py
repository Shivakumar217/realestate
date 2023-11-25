from django.db import models
from django.contrib.auth.models import User


class Property(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    zpid = models.CharField(max_length=255, unique=True, null=False)
    address = models.CharField(max_length=255)
    description = models.TextField(default="")  # Default value added

    def __str__(self):
        return f"{self.address} - {self.zpid}"
