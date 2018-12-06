import os

from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Media(models.Model):
    name = models.CharField(max_length=256)
    file = models.FileField(blank=True, null=True)
    duration = models.IntegerField()

    def __str__(self):
        return f"{self.name}"

    def filename(self):
        return os.path.basename(self.file.name)