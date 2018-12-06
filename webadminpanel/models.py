import os

from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Media(models.Model):
    name = models.CharField(max_length=256)
    file = models.FileField(blank=True, null=True)
    duration = models.IntegerField()
    date_added = models.DateTimeField(auto_now_add=True, blank=True)
    last_edited = models.DateTimeField(auto_now=True, blank=True)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return f"{self.name}"

    def filename(self):
        return os.path.basename(self.file.name)


class Group(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True, blank=True)
    last_edited = models.DateTimeField(auto_now=True, blank=True)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"



# class Campaign(models.Model):
#     name = models.CharField(max_length=256)
#     media = models.ForeignKey(Media, on_delete=models.CASCADE, blank=True)
#     display_unit = models.ForeignKey(DisplayUnit, on_delete=models.CASCADE, blank=True)