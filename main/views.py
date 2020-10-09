from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.contrib.auth import settings
from pyexcel_xlsx import get_data as xlsx_get
from django.utils.datastructures import MultiValueDictKeyError
from django.shortcuts import redirect

def send_email(request):
    send_mail('Subject here', 'Here is the message.', 'swatantranigam9451@gmail.com',
    ['swatantranigam9166@gmail.com'], fail_silently=False)

def send_email(request):
    if request.method=="POST":
        excel_file = request.FILES["files"]
        data = xlsx_get(excel_file, column_limit=1)
        emails = data["Sheet1"]
        list_email=[]
        for email in emails:
            for i in email:
                list_email.append(i)
        print(list_email)
        send_mail('DSC JSS', 'Hello My name is Swatantra', 'swatantranigam9451@gmail.com',
        list_email, fail_silently=False)
        return HttpResponse("ok done")
    return render(request,'email/input.html')