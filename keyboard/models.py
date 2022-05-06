import datetime
from django.db import models
from django.utils import timezone
from django.utils.timezone import now


class Keyboard(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Switche(models.Model):
    name = models.CharField(max_length=200, null=True)
    description = models.TextField(max_length=400, null=True)
    model = models.ForeignKey(Keyboard, on_delete=models.CASCADE, null=True)
    keycap = models.ManyToManyField("Keycap", null=True)

    def __str__(self):
        return self.name


class Keycap(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
