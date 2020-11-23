from django.db import models

# Create your models here.

class Room(models.Model):
    code = models.IntegerField(default=0)
    floor = models.IntegerField(default=0)
    classification = models.CharField(max_length=200)

    def __str__(self):
        return str(self.code)

class DataFromRoom(models.Model):
    code = models.ForeignKey(Room, on_delete=models.CASCADE)
    people_in_room = models.IntegerField(default=0)
    people_entered = models.IntegerField(default=0)
    people_got_out = models.IntegerField(default=0)
    date_published = models.DateTimeField('date_published')

    def was_published_recently(self):
        return self.date_published >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return str(self.code) + " at " + str(self.date_published)
