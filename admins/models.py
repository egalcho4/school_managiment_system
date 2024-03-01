from django.db import models

# Create your models here.
class Account(models.Model):
    uname=models.CharField(max_length=233,null=True)
    fname=models.CharField(max_length=233,null=True)
    lname=models.CharField(max_length=233,null=True)
    age=models.DateTimeField(null=True)
    gender=models.CharField(max_length=233,null=True)
    image=models.TextField(null=True)
    role=models.CharField(max_length=233,null=True)

