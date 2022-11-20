from django.db import models

# Create your models here.
class Student(models.Model):
    rn = models.IntegerField()
    name = models.CharField(max_length=100)
    marks = models.IntegerField()
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.name