from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Media(models.Model):
    name = models.CharField(max_length=256)
    file = models.FileField(blank=False)
    duration = models.IntegerField()