from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Zaal(models.Model):
    naam = models.CharField(max_length=100, blank=False)
    locatie = models.CharField(max_length=100, blank=False)
    aantal_plaatsen = models.IntegerField(default=0)

    def __str__(self):
        return self.locatie + " : " + self.naam


class Reservatie(models.Model):
    user = models.ForeignKey(User)
    date = models.DateTimeField(null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    for_zaal = models.OneToOneField(
        Zaal,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return "Reservatie: " + str(self.date) + " door user: " + str(self.user)
