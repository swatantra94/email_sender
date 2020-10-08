from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.contrib.auth import settings

def send_email(request):
    # send_mail('Subject here', 'Here is the message.', 'swatantranigam9451@gmail.com',
    # ['swatantranigam9166@gmail.com'], fail_silently=False)
    return render(request,'email/input.html')