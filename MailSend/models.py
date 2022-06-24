from django import forms
from django.db import models
from django.forms import IntegerField, ModelForm

class details(models.Model):
    Name=models.CharField(max_length=100)
    PhoneNo=IntegerField(max_value=10,min_value=10)
    Email=models.EmailField(max_length=100)
    Address = models.CharField(max_length=100,blank=True)
    City=models.CharField(max_length=100)
    def __str__(self):
        return self.Name
    
    
class Login(models.Model):
    UserName=models.CharField(max_length=50)
    # Email=models.EmailField(max_length=100)
    UserID= models.IntegerField(blank=False, default=1)
    Password=models.CharField(max_length=50)    
    def __str__(self):
        return self.UserName
    
class MailMessage(models.Model):
    subject=models.CharField(max_length=100)
    message=models.CharField(max_length=1000)
    senderID=models.EmailField(max_length=100)
    reciverId=models.EmailField(max_length=100)
    
    

