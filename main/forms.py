from django import forms

class WorkshopEmail(forms.Form):
    time = forms.CharField(max_length=256)
    mentor = forms.CharField(max_length=256)
    room = forms.CharField(max_length=256)
    link = forms.URLField(required=False)

class CustomEmailForm(forms.Form):
    body = forms.CharField(max_length = 2048)