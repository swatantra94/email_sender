from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.contrib.auth import settings
from pyexcel_xlsx import get_data as xlsx_get
from django.utils.datastructures import MultiValueDictKeyError
from django.shortcuts import redirect
from main import forms


def send_email(request):
    send_mail('Subject here', 'Here is the message.', 'swatantranigam9451@gmail.com',
    ['swatantranigam9166@gmail.com'], fail_silently=False)

def send_email(request):
    form = forms.WorkshopEmail()
    if request.method=="POST":
        form = forms.WorkshopEmail(request.POST)
        excel_file = request.FILES["files"]
        data = xlsx_get(excel_file, column_limit=1)
        emails = data["Sheet1"]
        list_email=[]
        file = open("main/workshop_email.txt","r")
        a=""
        for _ in range(6):
            a=a+file.readline()
        file.close()
        if form.is_valid():
            time = form.cleaned_data["time"]
            mentor = form.cleaned_data["mentor"]
            room = form.cleaned_data["room"]
            a = a+' "'
            a = a+time
            a = a+'" '
            file = open("main/workshop_email.txt","r")
            file.read(60)
            a = a+file.read(40)
            a = a+' Mentors Are:"'+mentor+'" '
            a=a+file.read(50)
            a = a+' room "'+room+'" '
            a=a+file.read()
            file.close()
            for email in emails:
                for i in email:
                    list_email.append(i)
            print(list_email)
            send_mail('DSC JSS', a, 'swatantranigam9451@gmail.com',
            list_email, fail_silently=False)
            return HttpResponse("ok done")
    context = {
        "form":form
    }
    return render(request,'email/input.html',context)