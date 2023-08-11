from django.db import models

# Create your models here.
class Class_room(models.Model):
    roomName = models.CharField(max_length=50, null=False, blank=False)
    def __str__(self):
        return self.roomName
class Subject(models.Model):
    subjectName = models.CharField(max_length=50, null=False, blank=False)
    def __str__(self):
        return self.subjectName

class Class_subject(models.Model):
    classRoomId = models.ForeignKey(Class_room, on_delete=models.SET_NULL, null=True, blank=False)
    subjectId = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True, blank=False)
    def __str__(self):
        return self.classRoomId.__str__() + ' ' + self.subjectId.__str__()