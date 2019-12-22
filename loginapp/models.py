from django.db import models

# Create your models here.
class school(models.Model):

    name=models.CharField(max_length=200)
    principal=models.CharField(max_length=200)
    location=models.CharField(max_length=200)

    def __str__(self):
        return self.name

class student(models.Model):

    name=models.CharField(max_length=200)
    age=models.CharField(max_length=200)
    school=models.ForeignKey(school,on_delete=models.CASCADE,related_name="students")

    def __str__(self):
        return self.name
