from django.db import models
from django.utils.crypto import secrets

# Create your models here.
class URL(models.Model):
    long_url = models.CharField(max_length=200)
    short_url = models.CharField(max_length=200, primary_key=True, unique=True)
    visits = models.IntegerField(default=0)
    def __str__(self):
        return self.short_url
    # def generate_short_url(self):
    #     return secrets.token_urlsafe(8)