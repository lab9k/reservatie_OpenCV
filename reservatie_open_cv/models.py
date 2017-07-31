from datetime import datetime

from django.contrib.auth.models import User
from django.db import models


class FaceUser(User):
    """
    built-in Django user extended with the ID from openCV.
    """
    face_id = models.IntegerField(blank=False, default=9999999, db_index=True, unique=True)

    def __str__(self):
        return self.first_name + " " + self.last_name


class Zaal(models.Model):
    """
    This model represents a room, which can be reserved by Users
    """
    # name of the room (roomnumber e.g. : D01.24A)
    naam = models.CharField(max_length=100, blank=False)
    # location of the room, can be an address, or university campus, building, etc.
    locatie = models.CharField(max_length=100, blank=False)
    # amount of spots in the room
    aantal_plaatsen = models.IntegerField(default=0)

    def __str__(self):
        return self.locatie + " : " + self.naam

    def is_vrij_op_datum(self, datum):
        """

        :type datum: datetime
        """
        reservatie = self.reservaties.filter(date=datum.date())
        if reservatie:
            return False
        return True


class Reservatie(models.Model):
    """
    This model represents a reservation for a room, the object holds relations to the user, who made the reservation,
    And the room, where the meeting will be held.
    """
    # user who created the reservation
    face_user = models.ForeignKey(FaceUser)
    # date and time the meeting will be held
    date = models.DateTimeField(null=False, blank=False)
    # date and time the reservation was first made
    created = models.DateTimeField(auto_now_add=True)
    # date and time the reservation was last updated
    updated = models.DateTimeField(auto_now=True)
    # room the reservation will be held in
    for_zaal = models.ForeignKey(Zaal, on_delete=models.CASCADE, related_name='reservaties')

    def __str__(self):
        return "Reservatie: " + str(self.date) + " door user: " + str(self.face_user)
