
from django.shortcuts import render
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from requests import request
# from BulkMail.MailSend.serializer import mailSeriaizer
from .models import details
from tablib import Dataset
from yaml import serialize
from .resources import DetailsResource
from .serializer import mailSeriaizer
from rest_framework import generics
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,DestroyAPIView,UpdateAPIView
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView

from django.core.mail import EmailMessage
from django.conf import settings
from django.core.mail import send_mail




class StudentListCreate(generics.ListCreateAPIView):
    queryset=details.objects.all()
    serializer_class=mailSeriaizer   

class student_RetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset=details.objects.all()
    serializer_class=mailSeriaizer





def LogIn(request):
    return render(request,"login.html")


def massage(request):
    subject = 'sending Bulk email'
    message = f'Hackathon project testing  '
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['sainiyash2101@gmail.com','awanishchaurasiya89@gmail.com' ]
    send_mail( subject, message, email_from, recipient_list )