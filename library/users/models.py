from django.db import models

# Create your models here
class Users(models.Model):
    name=models.CharField(max_length=20)
    age=models.IntegerField()
    email=models.CharField(max_length=20)
    place=models.CharField(max_length=20)
    gender=models.CharField(max_length=20)

    def __str__(self):
        return self.name
