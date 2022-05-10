from django.db import models

# Create your models here.
class Student(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"