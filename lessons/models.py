from django.db import models


class Lesson(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    place = models.CharField(max_length=500)
    teacher = models.CharField(max_length=100)
    startTime = models.TimeField()
    endTime = models.TimeField()
    weekDay = models.IntegerField()
    appointment_id = models.CharField(max_length=250)
    service_id = models.CharField(max_length=250)
    pay = models.BooleanField()
    appointment = models.BooleanField()
    teacher_v2 = models.ForeignKey('Teacher', on_delete=models.DO_NOTHING)
    color = models.CharField(max_length=100)
    availability = models.IntegerField()

    def __str__(self):
        return self.name


class Teacher(models.Model):
    short_name = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=250)
    imageUrl = models.CharField(max_length=500)

    def __str__(self):
        return self.name
