from django.db import models

# Create your models here.

class Book(models.Model):
    title=models.CharField(max_length=20)
    author=models.CharField(max_length=20)
    pages=models.IntegerField()
    price=models.IntegerField()
    language=models.CharField(max_length=20)
    cover = models.ImageField(upload_to="images")
    pdf = models.FileField(upload_to="pdf")

    # table definition


    def __str__(self):
        return self.author


