from django.db import models
from employees.models import Employees
from classes.models import Subject
# Create your models here.

class Teacher(models.Model):
    employees_id = models.ForeignKey(Employees, on_delete= models.CASCADE, null=True)
    def __str__(self):
        return self.employees_id.__str__()
class Teacher_subject(models.Model):
    teacherId = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, blank=False)
    subjectId = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True, blank=False)
    def __str__(self):
        return self.teacherId.__str__() + ' ' + self.subjectId.__str__()