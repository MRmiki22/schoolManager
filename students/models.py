from django.db import models
from classes.models import Class_room

# Create your models here.
class Family_type(models.Model):
    typeName = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.typeName
class Family(models.Model):
    firstName     = models.CharField(max_length=50, null=False, blank=False)
    middelName    = models.CharField(max_length=50, null=False, blank=False)
    lastName      = models.CharField(max_length=50, null=False, blank=False)
    email         = models.EmailField(max_length=100, null=False, blank=False)
    phone         = models.IntegerField(null=False, blank=False)
    sex           = models.CharField(max_length=1, null=False, blank=False)
    family_type_id= models.ForeignKey(Family_type, on_delete= models.SET_NULL,null=True)
    def __str__(self):
        return self.firstName
class Student(models.Model):
    firstName  = models.CharField(max_length= 50, null = False, blank= False)
    middelName = models.CharField(max_length= 50, null = False, blank= False)
    lastName   = models.CharField(max_length= 50, null = False, blank= False)
    email      = models.EmailField(max_length= 100, null = False, blank= False)
    phone      = models.IntegerField(null=False, blank=False)
    age        = models.IntegerField(null = False, blank= False)
    sex        = models.CharField(max_length=1, null = False, blank= False)
    class_room_id = models.ForeignKey(Class_room, on_delete=models.SET_NULL, null=True)
    family_id = models.ForeignKey(Family, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.firstName
