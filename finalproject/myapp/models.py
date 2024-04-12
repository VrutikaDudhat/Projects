from django.db import models

# Create your models here.

class usersignup(models.Model):
    Create=models.DateTimeField(auto_now_add=True)
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    username=models.EmailField()
    password=models.CharField(max_length=12)
    city=models.CharField(max_length=20)
    state=models.CharField(max_length=20)
    mobile=models.BigIntegerField()


class mynotes(models.Model):
    Create=models.DateTimeField(auto_now_add=True)
    title=models.CharField(max_length=500)
    cate=models.CharField(max_length=500)
    myfile=models.FileField(upload_to='Media')
    comments=models.TextField()

class feedback(models.Model):
    Create=models.DateTimeField(auto_now_add=True)
    name=models.CharField(max_length=20) 
    email=models.EmailField()   
    subject=models.CharField(max_length=100)
    msg=models.TextField()

