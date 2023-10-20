from django.db import models

# Create your models here.
class URL(models.Model):
    long_url = models.CharField(max_length=200)
    short_url = models.CharField(max_length=200)
    visits = models.IntegerField(default=0)
    def __str__(self):
        return self.short_url