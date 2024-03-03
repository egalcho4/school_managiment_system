from django.db import models

# Create your models here.
class Section(models.Model):
    grade=models.CharField(max_length=255,null=True)
    section=models.CharField(max_length=20,null=True)
    nas=models.IntegerField(null=True)
    teach=models.IntegerField(null=True)
    grad=models.IntegerField(null=True)
class Account(models.Model):
    uname=models.CharField(max_length=233,null=True)
    fname=models.CharField(max_length=233,null=True)
    lname=models.CharField(max_length=233,null=True)
    age=models.DateTimeField(null=True)
    gender=models.CharField(max_length=233,null=True)
    image=models.TextField(null=True)
    role=models.CharField(max_length=233,null=True)
    sec=models.ForeignKey(Section,on_delete=models.CASCADE,null=True)


class Streem(models.Model):
    name=models.CharField(max_length=255,null=True)
    grade=models.IntegerField(null=True)
    streem=models.CharField(max_length=223,null=True)
    descr=models.TextField(null=True)
    nsub=models.IntegerField(null=True)
    section=models.ForeignKey(Section,on_delete=models.CASCADE,null=True)

