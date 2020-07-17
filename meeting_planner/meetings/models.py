from django.db import models
from datetime import time

class Room(models.Model):

    class FloorNumber(models.IntegerChoices):
        GROUNDFLOOR = 0
        FIRSTFLOOR = 1
        SECONDFLOOR = 2

    class RoomNumber(models.TextChoices):
        MERCURY = 10
        VENUS = 20
        EARTH = 30


    name = models.CharField(max_length=128)
    floor_number = models.IntegerField(FloorNumber.choices)
    room_number = models.IntegerField(RoomNumber.choices)

    def __str__(self):
        return f"{self.name} in room {self.floor_number}{self.room_number}"

class Meeting(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    start_time = models.TimeField(default = time(9))
    duration = models.IntegerField(default=1)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} at {self.start_time} on {self.date} for {self.duration} hours"

