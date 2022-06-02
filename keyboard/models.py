import datetime
from django.db import models
from django.utils import timezone
from django.utils.timezone import now


class Switche(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Keyboard(models.Model):
    name = models.CharField(max_length=200, null=True)
    size = models.TextField(max_length=200, null=True)
    model = models.ForeignKey(Switche, on_delete=models.CASCADE, null=True)
    keycap = models.ManyToManyField("Keycap")

    def __str__(self):
        return self.name


class Keycap(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
